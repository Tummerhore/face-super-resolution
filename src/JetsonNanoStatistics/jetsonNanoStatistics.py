#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# This file is part of the jetson_stats package (https://github.com/rbonghi/jetson_stats or http://rnext.it).
# Copyright (c) 2019 Raffaello Bonghi.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from jtop import jtop
import time
from enumComponent import EnumComponent

class JetsonNanoStatistics:
    def __init__(self):
        with jtop() as jetson:
            while True:
                self.__powerConsumptionInMilliwatts = jetson.stats["WATT"]
	       # print("I'm the energy " + self.__temperature)
                print(self.getAveragePowerConsumptionInMilliwattsFor(EnumComponent.CPU.value))

    """
    component - every possible component listet in EnumComponent, e.g. EnumComponent.CPU.value to get the value of CPU
    """
    def getAveragePowerConsumptionInMilliwattsFor(self, component):
        return self.__powerConsumptionInMilliwatts[component]['avg']
		
"""
if __name__ == "__main__":

    print("Simple Tegrastats reader")

    with jtop() as jetson:
        while True:
            # Read tegra stats
            print(jetson.stats)
	    print(jetson.stats["TEMP"])
            # Status disk
           # print(jetson.disk)
            # Status fans
           # if hasattr(jetson, 'fan'):
           #     print(jetson.fan)
            # uptime
           # print(jetson.uptime)
            # nvpmodel
           # print(jetson.nvpmodel)
            # local interfaces
           # print(jetson.local_interfaces)
            # boards
            #print(jetson.board)
            # Sleep before send new stat
            time.sleep(1)
"""
statistics = JetsonNanoStatistics()
# EOF
