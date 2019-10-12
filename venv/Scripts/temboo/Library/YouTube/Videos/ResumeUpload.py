# -*- coding: utf-8 -*-

###############################################################################
#
# ResumeUpload
# Inserts a new file.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ResumeUpload(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ResumeUpload Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ResumeUpload, self).__init__(temboo_session, '/Library/YouTube/Videos/ResumeUpload')


    def new_input_set(self):
        return ResumeUploadInputSet()

    def _make_result_set(self, result, path):
        return ResumeUploadResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ResumeUploadChoreographyExecution(session, exec_id, path)

class ResumeUploadInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ResumeUpload
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_RequestBody(self, value):
        """
        Set the value of the RequestBody input for this Choreo. ((conditional, json) A JSON representation of fields in a file resource. File metadata information (such as the title) can be inserted using this input. See documentation for formatting examples.)
        """
        super(ResumeUploadInputSet, self)._set_input('RequestBody', value)
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid access token retrieved during the OAuth2 process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new access token.)
        """
        super(ResumeUploadInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(ResumeUploadInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(ResumeUploadInputSet, self)._set_input('ClientSecret', value)
    def set_ContentType(self, value):
        """
        Set the value of the ContentType input for this Choreo. ((optional, string) The Content-Type of the file that is being uploaded. Defaults to application/octet-stream.)
        """
        super(ResumeUploadInputSet, self)._set_input('ContentType', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Selector specifying a subset of fields to include in the response.)
        """
        super(ResumeUploadInputSet, self)._set_input('Fields', value)
    def set_FileContent(self, value):
        """
        Set the value of the FileContent input for this Choreo. ((conditional, string) The Base64 encoded contents of the file to upload.)
        """
        super(ResumeUploadInputSet, self)._set_input('FileContent', value)
    def set_Index(self, value):
        """
        Set the value of the Index input for this Choreo. ((conditional, any) )
        """
        super(ResumeUploadInputSet, self)._set_input('Index', value)
    def set_LastByte(self, value):
        """
        Set the value of the LastByte input for this Choreo. ((conditional, integer) )
        """
        super(ResumeUploadInputSet, self)._set_input('LastByte', value)
    def set_Offset(self, value):
        """
        Set the value of the Offset input for this Choreo. ((conditional, any) )
        """
        super(ResumeUploadInputSet, self)._set_input('Offset', value)
    def set_Part(self, value):
        """
        Set the value of the Part input for this Choreo. ((required, string) This parameter identifies the properties that the write operation will set as well as the properties that the API response will include (e.g. snippet).)
        """
        super(ResumeUploadInputSet, self)._set_input('Part', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth refresh token used to generate a new access token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(ResumeUploadInputSet, self)._set_input('RefreshToken', value)
    def set_ResumeUploadID(self, value):
        """
        Set the value of the ResumeUploadID input for this Choreo. ((optional, string) The UploadID used to resume a partially uploaded file.)
        """
        super(ResumeUploadInputSet, self)._set_input('ResumeUploadID', value)
    def set_Size(self, value):
        """
        Set the value of the Size input for this Choreo. ((required, integer) )
        """
        super(ResumeUploadInputSet, self)._set_input('Size', value)


class ResumeUploadResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ResumeUpload Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)
    def get_ResponseCode(self):
        """
        Retrieve the value for the "ResponseCode" output from this Choreo execution. ((integer) The response status code. A successful upload returns 201. An incomplete upload returns 308.)
        """
        return self._output.get('ResponseCode', None)
    def get_UploadID(self):
        """
        Retrieve the value for the "UploadID" output from this Choreo execution. ((string) )
        """
        return self._output.get('UploadID', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)

class ResumeUploadChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ResumeUploadResultSet(response, path)
