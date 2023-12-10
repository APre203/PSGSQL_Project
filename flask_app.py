from flask import Flask, render_template, request
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_PASS = os.getenv('db_password')

# Database connection parameters
db_host = 'localhost'  # Replace with your database host
db_name = 'Music_460_Project'  # Replace with your database name
db_user = 'postgres'  # Replace with your database username
db_password = DB_PASS  # Replace with your database password
db_port = 5432  # Replace with your database port (default PostgreSQL port is 5432)




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    db_connection = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
)
    try:
        
        query = request.form.get('query')

        # Perform a database query with the user's input
        cursor = db_connection.cursor()
        cursor.execute(query + ";")
        
        if "insert into" in str(query.lower()) or "delete from" in str(query.lower()) or "UPDATE" in str(query):
            e = ""
            if "insert into" in query.lower():
                e = "Insert"
            elif "UPDATE" in query:
                e = "Update"
            else:
                e = "Delete"
            db_connection.commit()
            cursor.close()
            db_connection.close()
            return render_template('insert_delete.html', error=e)

        results = cursor.fetchall()
        qu = query.lower().split(" ")
        ind = qu.index("from")
        from_where = qu[ind+1].replace(";","")
        col_names = [desc[0] for desc in cursor.description]


        db_connection.commit()
        cursor.close()
        db_connection.close()
        #print(results)
        # Process the retrieved data and render a template with the results
        return render_template('search_results.html', results=results, col_names=col_names, fr=from_where, num = len(results))

    except Exception as e:
        try:
            db_connection.rollback()
            return render_template('error.html', error=str(e))
        except:
            db_connection.close()
            return render_template('error.html', error=str(e))
if __name__ == '__main__':
    app.run()