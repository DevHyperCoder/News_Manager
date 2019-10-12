# -*- coding: utf-8 -*-

###############################################################################
#
# ConfigureGraph
# Creates, modifies, or styles a graph.
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

class ConfigureGraph(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ConfigureGraph Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ConfigureGraph, self).__init__(temboo_session, '/Library/Plotly/ConfigureGraph')


    def new_input_set(self):
        return ConfigureGraphInputSet()

    def _make_result_set(self, result, path):
        return ConfigureGraphResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ConfigureGraphChoreographyExecution(session, exec_id, path)

class ConfigureGraphInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ConfigureGraph
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Plotly.)
        """
        super(ConfigureGraphInputSet, self)._set_input('APIKey', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((required, string) The file name of your Plotly graph. If the file is nested within a directory, you can specify a path here (e.g., myFolder/myPlot).)
        """
        super(ConfigureGraphInputSet, self)._set_input('FileName', value)
    def set_FileOption(self, value):
        """
        Set the value of the FileOption input for this Choreo. ((required, string) The file operation being performed. Valid values are: "new", "overwrite", "append", or "extend". See Choreo description for more details.)
        """
        super(ConfigureGraphInputSet, self)._set_input('FileOption', value)
    def set_GraphArguments(self, value):
        """
        Set the value of the GraphArguments input for this Choreo. ((conditional, json) The data and/or styling arguments. Typically, this is in the form of a JSON array where x and y are represented as arrays of numbers or strings. See Choreo description for more details.)
        """
        super(ConfigureGraphInputSet, self)._set_input('GraphArguments', value)
    def set_Layout(self, value):
        """
        Set the value of the Layout input for this Choreo. ((optional, json) A key-value paired JSON object that describes the layout of the plot (e.g., {"title": "Sensor Data"}).)
        """
        super(ConfigureGraphInputSet, self)._set_input('Layout', value)
    def set_Origin(self, value):
        """
        Set the value of the Origin input for this Choreo. ((optional, string) Specifies the type of call and the type of data in the Arguments parameter. Valid values are: plot (the default), style, or layout.)
        """
        super(ConfigureGraphInputSet, self)._set_input('Origin', value)
    def set_Style(self, value):
        """
        Set the value of the Style input for this Choreo. ((optional, json) A JSON object describing the style of the graph (e.g., {"type": "bar"}). This can be applied to every single trace (default) or to the traces specified in the optional Traces input.)
        """
        super(ConfigureGraphInputSet, self)._set_input('Style', value)
    def set_Traces(self, value):
        """
        Set the value of the Traces input for this Choreo. ((optional, json) Specifies the indices that the Style input object should be applied to. This should be formatted as a JSON array.)
        """
        super(ConfigureGraphInputSet, self)._set_input('Traces', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A valid Plotly username.)
        """
        super(ConfigureGraphInputSet, self)._set_input('Username', value)
    def set_WorldReadable(self, value):
        """
        Set the value of the WorldReadable input for this Choreo. ((optional, boolean) When set to true, the graph is viewable by anyone who has the link. If false (the default), the graph is only viewable in the owner's Plotly account.)
        """
        super(ConfigureGraphInputSet, self)._set_input('WorldReadable', value)

class ConfigureGraphResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ConfigureGraph Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_URL(self):
        """
        Retrieve the value for the "URL" output from this Choreo execution. ((string) The Plotly URL for the graph.)
        """
        return self._output.get('URL', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Plotly)
        """
        return self._output.get('Response', None)

class ConfigureGraphChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ConfigureGraphResultSet(response, path)
