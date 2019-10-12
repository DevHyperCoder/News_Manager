# -*- coding: utf-8 -*-

###############################################################################
#
# PlotLineGraph
# Plots an array of points on a line graph.
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

class PlotLineGraph(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the PlotLineGraph Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(PlotLineGraph, self).__init__(temboo_session, '/Library/Plotly/PlotLineGraph')


    def new_input_set(self):
        return PlotLineGraphInputSet()

    def _make_result_set(self, result, path):
        return PlotLineGraphResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PlotLineGraphChoreographyExecution(session, exec_id, path)

class PlotLineGraphInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the PlotLineGraph
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Plotly.)
        """
        super(PlotLineGraphInputSet, self)._set_input('APIKey', value)
    def set_FileName(self, value):
        """
        Set the value of the FileName input for this Choreo. ((required, string) The file name of your Plotly graph. If the file is nested within a directory, you can specify a path here (e.g., myFolder/myPlot).)
        """
        super(PlotLineGraphInputSet, self)._set_input('FileName', value)
    def set_FileOption(self, value):
        """
        Set the value of the FileOption input for this Choreo. ((optional, string) The file operation being performed. Valid values are: "new", "overwrite", "append", or "extend". See Choreo description for more details. This defaults to "overwrite".)
        """
        super(PlotLineGraphInputSet, self)._set_input('FileOption', value)
    def set_Title(self, value):
        """
        Set the value of the Title input for this Choreo. ((optional, string) The title of the graph.)
        """
        super(PlotLineGraphInputSet, self)._set_input('Title', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) A valid Plotly username.)
        """
        super(PlotLineGraphInputSet, self)._set_input('Username', value)
    def set_WorldReadable(self, value):
        """
        Set the value of the WorldReadable input for this Choreo. ((optional, boolean) When set to true, the graph is viewable by anyone who has the link. If false (the default), the graph is only viewable in the owner's Plotly account.)
        """
        super(PlotLineGraphInputSet, self)._set_input('WorldReadable', value)
    def set_XValues(self, value):
        """
        Set the value of the XValues input for this Choreo. ((required, json) A JSON array containing the "x" coordinate values to be plotted on the graph.)
        """
        super(PlotLineGraphInputSet, self)._set_input('XValues', value)
    def set_YValues(self, value):
        """
        Set the value of the YValues input for this Choreo. ((required, json) A JSON array containing the "y" coordinate values to be plotted on the graph.)
        """
        super(PlotLineGraphInputSet, self)._set_input('YValues', value)

class PlotLineGraphResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the PlotLineGraph Choreo.
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

class PlotLineGraphChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return PlotLineGraphResultSet(response, path)
