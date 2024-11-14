from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'mysql',
    'user': 'root',
    'password': 'password',
    'database': 'mydatabase'
}

@app.route('/input', methods=['POST'])
def add_input():
    data = request.json
    user_input = data.get('input')
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO user_inputs (input) VALUES (%s)", (user_input,))
        connection.commit()
        return jsonify({"message": "Input stored successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)})            
    finally:
        if connection.is_connected():
           cursor.close()
           connection.close()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
