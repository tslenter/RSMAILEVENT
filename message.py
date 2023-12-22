#import required modules
import requests
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def extract_data(output, username, password, backtime, index, searchword, headers, data_url, json_data):
    #Process data
    query = json.dumps(json_data)
    data_response = requests.get(data_url, data = query, auth=(username,password), verify=False, headers = headers)
    #Check valid request
    if data_response.status_code == 200:
    #    Could be used to print the json response pretty (Debug)
    #    print(json.dumps(response.json(), indent=4, sort_keys=True))
        json_data_processed = json.loads(json.dumps(data_response.json()))
        count = len(json_data_processed['hits']['hits'])
        #Loop count with data and add a new line
        output = "Please check the following AP's:<br>\n"
        for i in range(count):
            # Use for HTML
            output += str(json_data_processed['hits']['hits'][i]['_source']['MESSAGE'])+"<br/>"+"\n"
        #check if the output is not default
        if output == "Please check the following AP's:<br>\n":
            print("Nothing to do ...")
            exit()
    else:
        print("Nothing to do ...")
        exit()

    #Show requested output
    return output

def send_email(subject, body, to_email, smtp_server, smtp_port, sender_email):
    # Create the MIME object
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, "html"))

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:

        # Send the email
        server.sendmail(sender_email, to_email, message.as_string())

    print("Email sent successfully!")

#set elastic variables
output=''
username='elastic'
password='password'
backtime='now-1h/h'
index='rse*'
searchword='Disjoined'
headers={'Accept': 'application/json', 'Content-type': 'application/json'}
data_url = 'http://localhost:9200/'+index+'/_search'
json_data = { "query" : { "bool" : { "must": [ { "match": { "MESSAGE": searchword } }, { "range": { "@timestamp": { "gte": backtime } } } ] } } , "size": 10000 }
#Can be used to validate the count (debug)
#json_count = { "size": 0, "query": { "bool" : { "must": [ { "match": { "MESSAGE": searchword } }, { "range": { "@timestamp": { "gte": backtime } } } ] } } }

output = extract_data(output, username, password, backtime, index, searchword, headers, data_url, json_data)

# Mail var
subject = "WiFi AP CHECK!!"
body = output
to_email = "send_to_mail@mail.nl"
smtp_server = "<server>"
smtp_port = 25
sender_email = "from_to_mail@mail.nl"

send_email(subject, body, to_email, smtp_server, smtp_port, sender_email)
