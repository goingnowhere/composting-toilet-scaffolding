# This file defines all of the global parameters that are used in the toilet block design
# and common calculated values that are determined from these parameters
# all measurements are in milimeters mm.

# TODO see if these can be set as constants - god my python is rubbish.

#  Import the packages that we need - TODO check that all of these are needed
# import FreeCAD


# Parameterized Size Variables in mm

# Poles and Joints
pole_diameter = 48 # The diameter of the scafolding poles that we are using.
pole_wall_thickness = 3 # The thickness of the walls of the poles
joint_wall_thickness = 5 # The thickness of the walls of the joints


# Boards
board_width = 2500 # Width of a standard plywood board
board_length = 1220 # Length of a standard plywood board
floor_board_thickness = 18 # The thickness of plywood boards used for the floor.
other_board_thickness = 12 # The tickness of the boards used for the walls and roof.


# Structure measurements
seat_height_from_ground = 1250 # The height that the toilet seat has to be from the ground to enable a solid waste container to be placed underneath.
seat_depth = 500 # The distance from the back wall to the edge of the seat.
seat_height_from_floor = 450 # The heignt the seat is from the floor of the structure
roof_height_from_floor = 2000 # The distance between the floor of the structure and the roof of the structure.
max_pole_underground = 500 # The maximum amount the poles will be sunk into the ground. Note on a slope only the higest points would be sunk in that much.
board_overlap = 12 # The amount the boards are routed to overlap the scafolding pole. This should be a circular rout matching the diameter of the scaffolding pole as far as possible


# Calcualted values based upon above parameters

joint_diameter = pole_diameter + joint_wall_thickness * 2 # The overall diameter of the joint.

building_height = roof_height_from_floor + (seat_height_from_ground - seat_height_from_floor) # The overall heignt of the building
# FreeCAD.Console.PrintMessage("Building height: ")
# FreeCAD.Console.PrintMessage(building_height)
# FreeCAD.Console.PrintMessage("mm\n")

pole_height = building_height + max_pole_underground # The length of the upright poles taking account of them being sunk into the ground.
# FreeCAD.Console.PrintMessage("Pole height: ")
# FreeCAD.Console.PrintMessage(pole_height)
# FreeCAD.Console.PrintMessage("mm\n")

pole_width = board_width + pole_diameter - board_overlap * 2 # The distance between the front and back poles.
# FreeCAD.Console.PrintMessage("Pole width: ")
# FreeCAD.Console.PrintMessage(pole_width)
# FreeCAD.Console.PrintMessage("mm\n")

middle_back_pole_height = max_pole_underground + seat_height_from_ground - floor_board_thickness - pole_diameter 
# The length of the upright poles taking account of them being sunk into the ground.
# TODO account for flange on joint. Also add this calc to earlier stuff where apropriate (probably just the heights)
# FreeCAD.Console.PrintMessage("Middle back pole height: ")
# FreeCAD.Console.PrintMessage(middle_back_pole_height)
# FreeCAD.Console.PrintMessage("mm\n")