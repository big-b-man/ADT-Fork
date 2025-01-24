# Aircraft design tool
#
# Copyright (C) 2022 Mario Bras
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# This Python version is a translation of the original MATLAB file by
# Mario Bras. Modified and translated by Bennett Steers, 2025.

import json, csv, numpy as np

"""
def load_project(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
"""
#implementation of read_file() from read_file.m
def read_file(filename, type):
    temp = []
    with open(filename) as file:
        reader = csv.reader(file)
        #extracts first row of data which should be data column titles
        titles = next(reader)#reads column titles from first row
        temp = np.array([[x for x in row] for row in reader])#reads data from remaining rows     

    if type == "source":
        class data:
            type = temp[:,0].tolist()
            specific_energy = temp[:,1].tolist()
            operation_EI_CO2 = temp[:,2].tolist()
            production_EI_CO2_per_kwh = temp[:,3].tolist()
            production_EI_CO2_per_kw = temp[:,4].tolist()
            max_hours_operation = temp[:,5].tolist()
            max_num_cycles = temp[:,6].tolist()
        return data
    if type == "gwp":
        class data:
            region = temp[:,0].tolist()
            value = temp[:,1].tolist()