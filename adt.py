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

from fileio import read_file, load_project

def adt(filename, *args):
    print('Aircraft Design Tool  Copyright (C) 2022  Mario Bras\n')
    print('This program comes with ABSOLUTELY NO WARRANTY.\n')
    print('This is free software, and you are welcome to redistribute it under certain conditions;\n')
    print('see details in the included LICENSE file.\n\n')

    #declaring gravity constant
    gravity = 9.81 # m/s^2
    
    #importing databases 
    source = read_file('energy_source_data.txt','source')
    gwp = read_file('gwp_data.txt','gwp')

    # Load project file
    # TODO: Implement load_project() function
    data = load_project(filename)

    # Concept
    # This still uses matlab syntax, will have to switch to dictionary or 
    # List syntax once i've decided what datatype will be imported by load_project
    data.concept = ahp(data.concept)
    print_concepts(data.concept)

    # Add missing mission segment and vehicle component parameters
    data.mission = build_mission(data.mission)
    data.vehicle = build_vehicle(data.vehicle)

    # Plot mission profile
    plot_mission(data.mission)

    # Mission analyses
    data.vehicle = aero_analysis(data.mission, data.vehicle)
    [data.mission, data.vehicle] = mass_analysis(data.mission, data.vehicle, data.energy)
    data.vehicle = design_space_analysis(data.mission, data.vehicle, data.energy)
    [data.vehicle,data.mission] = emissions(data.mission, data.vehicle)

    # Plot aircraft configuration
    data.vehicle = plot_aircraft(data.vehicle)

    # Save new project file
    if ~isempty(varargin)
        save_project(data, varargin{1})