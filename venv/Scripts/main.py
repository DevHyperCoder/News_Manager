from __future__ import print_function
import webbrowser
from functools import partial
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import google_docs_client
import tkinter
import tkhyperlinkManager
from temboo.Library.Dropbox.Files import Upload
from temboo.core.session import TembooSession
from os.path import join as pjoin
from bs4 import BeautifulSoup
import html5lib
import requests
import urllib3
import re
import lxml
from flask import Flask , render_template , request
import parse
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']



#Read the contetns of the files
# C:\Users\user\Documents\News Aggregator
path_to_file = pjoin("C:\\", "Users", "user", "Documents", "News Aggregator", "document.txt")
f = open(path_to_file, "r")
texts_in_file = f.readlines()
f.close()

text_in_file = [""]
text_in_file_revised = [""]
DEBUG = False
GUI = False
array_of_doc_id = [""]
array_of_doc_title = [""]

for line in texts_in_file:
    text_in_file.append(line)


if DEBUG:
    for text in text_in_file:
        print(text)


def upload_to_dropbox(file_name,file_contents):
    # Create a session with your Temboo account details
    session = TembooSession("temboosign", "myFirstApp", "OOqKKwbTUhELCgBZC5T2CuXmJ9CqYvrb")

    # Instantiate the Choreo
    uploadChoreo = Upload(session)

    # Get an InputSet object for the Choreo
    uploadInputs = uploadChoreo.new_input_set()

    # Set the Choreo inputs
    file_name=file_name.replace(' ','')
    print("FILE"+file_name)
    uploadInputs.set_Path("/Apps/Parrot Teleprompter/"+file_name+".txt")
    uploadInputs.set_FileContent(file_contents)
    uploadInputs.set_ContentType("text/plain")
    uploadInputs.set_AccessToken("cG2kM3HuQMAAAAAAAAAAKBefSA5DdwNZ0Ll1sMjYyMShP8gCDt2FXLqwZrwbVJG6")

    # Execute the Choreo
    uploadResults = uploadChoreo.execute_with_results(uploadInputs)
    if DEBUG:
       print(format(uploadResults))

    # # Print the Choreo outputs
    # print("Response: " + uploadResults.get_Response())






for text in text_in_file:
    # print("url found")
    # print(text)
    if not text == "":
        contents = parse.parse(text)
        title = parse.parse_title(text)
        if not contents:
            contents=" "
        if not title:
            title = " "



        if DEBUG:
            print(text)
            print(contents)
            print("////////////////////////////////////")

        # upload to google docs for editing
        doc_id = google_docs_client.upload_to_google_docs(title, contents)
        array_of_doc_title.append(title)
        array_of_doc_id.append(doc_id)
        # # asdfasdf
        # google_docs_client.retrieve(doc_id)

def on_click_doc_id(docId):
    link = 'https://docs.google.com/document/d/'+docId
    if DEBUG:
        print(link)
    webbrowser.open(link)

def on_click_save_to_dropbox(docId):
    text = google_docs_client.retrieve_contents(docId)
    title = google_docs_client.retrieve_title(docId)

    print(text)
    print(title)

    upload_to_dropbox(title,text)


if GUI:
    m = tkinter.Tk()

    m.attributes("-fullscreen", True)

    m.bind("<Escape>", lambda e: m.quit())
    t = tkinter.Text(m)
    t.insert(tkinter.END, "Please wait: \n")

    m.mainloop()
    t.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES)
    text_for_tkinter = [""]
    hyperlink = tkhyperlinkManager.HyperlinkManager(t)

    for (docId,title) in zip(array_of_doc_id,array_of_doc_title):
      # Add the hyper link
      t.insert(tkinter.INSERT, title,
               hyperlink.add(partial(on_click_doc_id, docId)))
      t.insert(tkinter.END, "\n")
      t.insert(tkinter.INSERT, docId,
               hyperlink.add(partial(on_click_save_to_dropbox, docId)))
      t.insert(tkinter.END, "\n")

    t.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES)
    m.mainloop()



