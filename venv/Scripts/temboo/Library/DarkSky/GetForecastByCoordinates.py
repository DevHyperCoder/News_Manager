# -*- coding: utf-8 -*-

###############################################################################
#
# GetForecastByCoordinates
# Returns the current weather conditions for a specified location by geo-coordinates.
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

class GetForecastByCoordinates(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetForecastByCoordinates Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetForecastByCoordinates, self).__init__(temboo_session, '/Library/DarkSky/GetForecastByCoordinates')


    def new_input_set(self):
        return GetForecastByCoordinatesInputSet()

    def _make_result_set(self, result, path):
        return GetForecastByCoordinatesResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetForecastByCoordinatesChoreographyExecution(session, exec_id, path)

class GetForecastByCoordinatesInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetForecastByCoordinates
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_APIKey(self, value):
        """
        Set the value of the APIKey input for this Choreo. ((required, string) The API Key provided by Dark Sky.)
        """
        super(GetForecastByCoordinatesInputSet, self)._set_input('APIKey', value)
    def set_Exclude(self, value):
        """
        Set the value of the Exclude input for this Choreo. ((optional, string) Exclude some number of data blocks from the API response. Valid values are: currently, minutely, hourly, daily, alerts, and flags.)
        """
        super(GetForecastByCoordinatesInputSet, self)._set_input('Exclude', value)
    def set_Extend(self, value):
        """
        Set the value of the Extend input for this Choreo. ((optional, string) When present, returns hour-by-hour data for the next 168 hours, instead of the next 48. Valid value: hourly.)
        """
        super(GetForecastByCoordinatesInputSet, self)._set_input('Extend', value)
    def set_Language(self, value):
        """
        Set the value of the Language input for this Choreo. ((optional, string) The language in which to return results e.g., es, fr, it, en (the default). See Choreo notes for a link to a full list of supported languages.)
        """
        super(GetForecastByCoordinatesInputSet, self)._set_input('Language', value)
    def set_Latitude(self, value):
        """
        Set the value of the Latitude input for this Choreo. ((required, decimal) The latitude of the location.)
        """
        super(GetForecastByCoordinatesInputSet, self)._set_input('Latitude', value)
    def set_Longitude(self, value):
        """
        Set the value of the Longitude input for this Choreo. ((required, decimal) The longitude of the location.)
        """
        super(GetForecastByCoordinatesInputSet, self)._set_input('Longitude', value)
    def set_Units(self, value):
        """
        Set the value of the Units input for this Choreo. ((optional, string) Return weather conditions in the requested units. Valid values are: auto, ca, uk2, us (use for Farenheit), and si (use for Celsius).)
        """
        super(GetForecastByCoordinatesInputSet, self)._set_input('Units', value)

class GetForecastByCoordinatesResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetForecastByCoordinates Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_HourlySummary(self):
        """
        Retrieve the value for the "HourlySummary" output from this Choreo execution. ((string) The hourly summary.)
        """
        return self._output.get('HourlySummary', None)
    def get_Humidity(self):
        """
        Retrieve the value for the "Humidity" output from this Choreo execution. ((decimal) The current humidity.)
        """
        return self._output.get('Humidity', None)
    def get_Pressure(self):
        """
        Retrieve the value for the "Pressure" output from this Choreo execution. ((decimal) The current pressure.)
        """
        return self._output.get('Pressure', None)
    def get_Summary(self):
        """
        Retrieve the value for the "Summary" output from this Choreo execution. ((string) The current weather summary.)
        """
        return self._output.get('Summary', None)
    def get_Temperature(self):
        """
        Retrieve the value for the "Temperature" output from this Choreo execution. ((decimal) The current temperature.)
        """
        return self._output.get('Temperature', None)
    def get_UVIndex(self):
        """
        Retrieve the value for the "UVIndex" output from this Choreo execution. ((integer) The current uv index.)
        """
        return self._output.get('UVIndex', None)
    def get_Visibility(self):
        """
        Retrieve the value for the "Visibility" output from this Choreo execution. ((decimal) The current visibility.)
        """
        return self._output.get('Visibility', None)
    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Dark Sky.)
        """
        return self._output.get('Response', None)

class GetForecastByCoordinatesChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetForecastByCoordinatesResultSet(response, path)
