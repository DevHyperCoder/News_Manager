"""
google_docs_client.py
This module provides methods to read the contents (text only) of a google docs document
The code is mostly based on the google docs devolopers page and the quickstart.py file provided by google
All rights reserved
"""

from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from temboo.Library.Dropbox.Files import Upload
from temboo.core.session import TembooSession
from os.path import join as pjoin
from bs4 import BeautifulSoup
import html5lib
import requests
import urllib3
import re
import lxml
DEBUG = False
#Reads the paragraph element of a google doc
def read_paragraph_element(element):
    """Returns the text in the given ParagraphElement.

        Args:
            element: a ParagraphElement from a Google Doc.
    """
    text_run = element.get('textRun')
    if not text_run:
        return ''
    return text_run.get('content')
#Reads all the structural elements of a google doc
def read_strucutural_elements(elements):
    """Recurses through a list of Structural Elements to read a document's text where text may be
        in nested elements.

        Args:
            elements: a list of Structural Elements.
    """
    text = ''
    for value in elements:
        if 'paragraph' in value:
            elements = value.get('paragraph').get('elements')
            for elem in elements:
                text += read_paragraph_element(elem)
    return text
#Reads all the contetns (paragraph) of a google doc.
def retrieve_contents(doc_id):
    """Shows basic usage of the Docs API.
        Prints the title of a sample document.
        """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('docs', 'v1', credentials=creds)


    doc = service.documents().get(documentId=doc_id).execute()
    doc_content = doc.get('body').get('content')
    s = read_strucutural_elements(doc_content)

    if DEBUG:
        print(s)
    return s


def retrieve_title(doc_id):
    """Shows basic usage of the Docs API.
        Prints the title of a sample document.
        """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('docs', 'v1', credentials=creds)


    doc = service.documents().get(documentId=doc_id).execute()
    doc_content = doc.get('title')
    if DEBUG:
        print(doc_content)

    return doc_content



def upload_to_google_docs(_title,_contents):
    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('docs', 'v1', credentials=creds)

    # # Retrieve the documents contents from the Docs service.
    # document = service.documents().get(documentId=DOCUMENT_ID).execute()
    title = _title
    text = _contents
    body = {


        'title': title

    }
    requests = [
        {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': text
            }
        }
    ]

    doc = service.documents().create(body=body).execute()
    if DEBUG:
        print('Created document with title: {0}'.format(
            doc.get('title')))
    docid = doc.get('documentId')
    if DEBUG:
      print(docid)
    result = service.documents().batchUpdate(documentId=docid, body={'requests': requests}).execute()
    return  docid