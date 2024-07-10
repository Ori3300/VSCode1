import requests
import time


# Define your API key (replace 'YOUR_API_KEY' with your actual VirusTotal API key)
api_key = '7f40c72a12e21a6064f1de660c492bee64191c5a3dc2bfc8645a5c207a287db4'

# The file you want to upload
file_path = "C:\\Users\\user\\Desktop\\Footy\\Footy1.png"

# URL for VirusTotal file scan
url = 'https://www.virustotal.com/api/v3/files'

# Open the file in binary mode
with open(file_path, 'rb') as file:
    files = {'file': (file_path, file)}
    headers = {
        'x-apikey': api_key,
    }

    response = requests.post(url, headers=headers, files=files)

    # Check if the request was successful
    if response.status_code == 200:
        response_json = response.json()
        print("File successfully uploaded")
        print("Response JSON:", response_json)

        # Extract the analysis_id
        analysis_id = response_json['data']['id']
        print(f"Analysis ID: {analysis_id}")

        # Use the analysis_id to get the report URL
        report_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"

        # Wait for a short period to allow analysis to complete
        time.sleep(10)

        # Make the GET request to retrieve the analysis report
        report_response = requests.get(report_url, headers=headers)

        if report_response.status_code == 200:
            report_json = report_response.json()
            print("Analysis Report:")
            print(report_json)
        else:
            print(f"Failed to retrieve report, status code: {report_response.status_code}")
            print("Report Response JSON:", report_response.json())
    else:
        print(f"Failed to upload file, status code: {response.status_code}")
        print("Response JSON:", response.json())