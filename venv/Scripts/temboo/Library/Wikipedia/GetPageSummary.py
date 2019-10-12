# -*- coding: utf-8 -*-

###############################################################################
#
# GetPageSummary
# Retrieves a summary response including a text extract of the first several sentences, as well as information about a thumbnail that represents the page.
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

class GetPageSummary(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetPageSummary Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetPageSummary, self).__init__(temboo_session, '/Library/Wikipedia/GetPageSummary')


    def new_input_set(self):
        return GetPageSummaryInputSet()

    def _make_result_set(self, result, path):
        return GetPageSummaryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetPageSummaryChoreographyExecution(session, exec_id, path)

class GetPageSummaryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetPageSummary
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((required, string) The Wikipedia page title.)
        """
        super(GetPageSummaryInputSet, self)._set_input('Title', value)

class GetPageSummaryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetPageSummary Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Extract(self):
        """
        Retrieve the value for the "Extract" output from this Choreo execution. ((string) The page summary.)
        """
        return self._output.get('Extract', None)
    def get_ResponseCode(self):
        """
        Retrieve the value for the "ResponseCode" output from this Choreo execution. ((integer) The response code returned by the API.)
        """
        return self._output.get('ResponseCode', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Wikipedia.)
        """
        return self._output.get('Response', None)

class GetPageSummaryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetPageSummaryResultSet(response, path)
