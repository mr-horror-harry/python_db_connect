from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    user_data = request.form['data']
    try:
        name, dept, gender, mobile = (column.strip() for column in user_data.split(","))
        
        if gender in ['m', 'male', 'Male']:
            gender = 'M'
        elif gender in ['f', 'female', 'Female']:
            gender = 'F'

        if (name and dept and gender):
            subprocess.run(['python3', 'database/db_process.py', name, dept, gender, mobile])
            return jsonify({'message': 'Data processed successfully'}), 200
        else:
            raise Exception("Enter data appropriately!!!")
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__=="__main__":
    app.run(host='0.0.0.0', port=5001)  
