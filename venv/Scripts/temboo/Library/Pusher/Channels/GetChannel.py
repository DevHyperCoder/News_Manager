# -*- coding: utf-8 -*-

###############################################################################
#
# GetChannel
# Retrieves information for a specific channel.
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

class GetChannel(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetChannel Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetChannel, self).__init__(temboo_session, '/Library/Pusher/Channels/GetChannel')


    def new_input_set(self):
        return GetChannelInputSet()

    def _make_result_set(self, result, path):
        return GetChannelResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetChannelChoreographyExecution(session, exec_id, path)

class GetChannelInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetChannel
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AppID(self, value):
        """
        Set the value of the AppID input for this Choreo. ((required, string) The application ID provided by Pusher.)
        """
        super(GetChannelInputSet, self)._set_input('AppID', value)
    def set_AppKey(self, value):
        """
        Set the value of the AppKey input for this Choreo. ((required, string) The authenticaion key provided by Pusher.)
        """
        super(GetChannelInputSet, self)._set_input('AppKey', value)
    def set_AppSecret(self, value):
        """
        Set the value of the AppSecret input for this Choreo. ((required, string) The authentication secret provided by Pusher.)
        """
        super(GetChannelInputSet, self)._set_input('AppSecret', value)
    def set_ChannelName(self, value):
        """
        Set the value of the ChannelName input for this Choreo. ((required, string) The name of the channel to retrieve.)
        """
        super(GetChannelInputSet, self)._set_input('ChannelName', value)
    def set_Info(self, value):
        """
        Set the value of the Info input for this Choreo. ((optional, string) A comma separated list of attributes which should be returned for the channel (e.g., user_count, subscription_count). Note that the user_count attribute is only applicable for presence channels.)
        """
        super(GetChannelInputSet, self)._set_input('Info', value)

class GetChannelResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetChannel Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Pusher.)
        """
        return self._output.get('Response', None)

class GetChannelChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetChannelResultSet(response, path)
