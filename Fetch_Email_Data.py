from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        #Returns dictionary of ids
        results = service.users().messages().list(userId='me').execute()

        id_list = results.get('messages', [])
        print(id_list[1])
        # message = service.users().messages().get(userId='me', id='186035da1a0ac3c8').execute()
        # print(message['payload']['headers'][19])
        # print(message['labelIds'])
        # date_received = service.users().messages().get(userId='me', id='186035da1a0ac3c8').execute()['payload']['headers'][1]['value'].split(";")[1].strip()

        message_body = []
        print("This might take a while...")

        for i in range(5):

            id = id_list[i-1]['id']
            email = service.users().messages().get(userId='me', id=id).execute()
            sender = email['payload']['headers'][15]['value']
            label = email['labelIds'][0]
            date_received = email['payload']['headers'][1]['value'].split(";")[1].strip()
            message = email['snippet']
            if email['payload']['headers'][19]['name'] == "Subject":
                subject = email['payload']['headers'][19]['value']
            else:
                subject = "No subject"
            message_body.append([date_received, sender, label, message, subject])
        return message_body

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()