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

def adt(filename, *args):
    print('Aircraft Design Tool  Copyright (C) 2022  Mario Bras\n');
    print('This program comes with ABSOLUTELY NO WARRANTY.\n');
    print('This is free software, and you are welcome to redistribute it under certain conditions;\n');
    print('see details in the included LICENSE file.\n\n');

    # I'm probably throwing these in a separate file at some point
    # Constants
    class constants:
        g = 9.81; # m/s^2

    # Databases
    class databases;
    databases.source = read_file('energy_source_data.txt','source');
    databases.gwp = read_file('gwp_data.txt','gwp');

    # Load project file
    data = load_project(filename);

    # Concept
    data.concept = ahp(data.concept);
    print_concepts(data.concept)

    # Add missing mission segment and vehicle component parameters
    data.mission = build_mission(data.mission);
    data.vehicle = build_vehicle(data.vehicle);

    # Plot mission profile
    plot_mission(data.mission);

    # Mission analyses
    data.vehicle = aero_analysis(data.mission, data.vehicle);
    [data.mission, data.vehicle] = mass_analysis(data.mission, data.vehicle, data.energy);
    data.vehicle = design_space_analysis(data.mission, data.vehicle, data.energy);
    [data.vehicle,data.mission] = emissions(data.mission, data.vehicle);

    # Plot aircraft configuration
    data.vehicle = plot_aircraft(data.vehicle);

    # Save new project file
    if ~isempty(varargin)
        save_project(data, varargin{1})