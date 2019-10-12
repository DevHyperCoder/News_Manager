# -*- coding: utf-8 -*-

###############################################################################
#
# CaptureKeyPadEntry
# Initiates a call from the specified Twilio account and returns a key pad entry.
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

class CaptureKeyPadEntry(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the CaptureKeyPadEntry Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(CaptureKeyPadEntry, self).__init__(temboo_session, '/Library/Twilio/Calls/CaptureKeyPadEntry')


    def new_input_set(self):
        return CaptureKeyPadEntryInputSet()

    def _make_result_set(self, result, path):
        return CaptureKeyPadEntryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return CaptureKeyPadEntryChoreographyExecution(session, exec_id, path)

class CaptureKeyPadEntryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the CaptureKeyPadEntry
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccountSID(self, value):
        """
        Set the value of the AccountSID input for this Choreo. ((required, string) The AccountSID provided when you signed up for a Twilio account.)
        """
        super(CaptureKeyPadEntryInputSet, self)._set_input('AccountSID', value)
    def set_AnswerURL(self, value):
        """
        Set the value of the AnswerURL input for this Choreo. ((conditional, string) The URL for the Twiml file containing your Temboo Callback URL. See Choreo notes below.)
        """
        super(CaptureKeyPadEntryInputSet, self)._set_input('AnswerURL', value)
    def set_AuthToken(self, value):
        """
        Set the value of the AuthToken input for this Choreo. ((required, string) The authorization token provided when you signed up for a Twilio account.)
        """
        super(CaptureKeyPadEntryInputSet, self)._set_input('AuthToken', value)
    def set_From(self, value):
        """
        Set the value of the From input for this Choreo. ((required, string) The Twilio phone number or client identifier to use as the caller id.)
        """
        super(CaptureKeyPadEntryInputSet, self)._set_input('From', value)
    def set_GoodbyeURL(self, value):
        """
        Set the value of the GoodbyeURL input for this Choreo. ((required, string) The URL for the Twiml file that contains a "goodbye" message that will be evalated after a Twilio webhook event. This is an optional input that can be used when passing the AnswerURL.)
        """
        super(CaptureKeyPadEntryInputSet, self)._set_input('GoodbyeURL', value)
    def set_IfMachine(self, value):
        """
        Set the value of the IfMachine input for this Choreo. ((optional, string) Indicates if Twilio should to try and determine if a machine (like voicemail) or a human has answered the call. Possible values are "Continue" and "Hangup".)
        """
        super(CaptureKeyPadEntryInputSet, self)._set_input('IfMachine', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are: json (the default) and xml.)
        """
        super(CaptureKeyPadEntryInputSet, self)._set_input('ResponseFormat', value)
    def set_SubAccountSID(self, value):
        """
        Set the value of the SubAccountSID input for this Choreo. ((optional, string) The SID of the subaccount associated with this call. If not specified, the main AccountSID used to authenticate is used in request.)
        """
        super(CaptureKeyPadEntryInputSet, self)._set_input('SubAccountSID', value)
    def set_Timeout(self, value):
        """
        Set the value of the Timeout input for this Choreo. ((optional, integer) The integer number of seconds that Twilio should allow the phone to ring before assuming there is no answer. Default is 60 seconds, the maximum is 999 seconds.)
        """
        super(CaptureKeyPadEntryInputSet, self)._set_input('Timeout', value)
    def set_To(self, value):
        """
        Set the value of the To input for this Choreo. ((required, string) The phone number or client identifier to call.)
        """
        super(CaptureKeyPadEntryInputSet, self)._set_input('To', value)

class CaptureKeyPadEntryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the CaptureKeyPadEntry Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_CallbackData(self):
        """
        Retrieve the value for the "CallbackData" output from this Choreo execution. ((string) The Twilio callback data retrieved after a user has entered a pin code.)
        """
        return self._output.get('CallbackData', None)
    def get_Digits(self):
        """
        Retrieve the value for the "Digits" output from this Choreo execution. ((integer) The digits that the call recipient entered into the keypad after receiving the call from Twilio.)
        """
        return self._output.get('Digits', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Twilio.)
        """
        return self._output.get('Response', None)

class CaptureKeyPadEntryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return CaptureKeyPadEntryResultSet(response, path)
