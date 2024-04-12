import requests

prompt_text = """
Enter input seperated with comma:
1) Name
2) Department
3) Gender
4) Phone No.
...
"""

def send_data():
    user_input = input(prompt_text)
    print("Data entered successfully...")
    response = requests.post('http://app-backend:5001/process_data', data={'data': user_input})
    # curl -X POST -d "data=your_data_here" http://localhost:5001/process_data #  for linux use

    if response.status_code == 200:
        print("Data processed successfully!")
    else:
        print("Error:", response.text)
send_data()