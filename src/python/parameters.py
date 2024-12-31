# This file defines all of the global parameters that are used in the toilet block design
# and common calculated values that are determined from these parameters
# all measurements are in milimeters mm.

# TODO see if these can be set as constants - god my python is rubbish.

#  Import the packages that we need 
import FreeCAD as App


# Parameterized Size Variables in mm

# Poles and Joints
pole_diameter = 48 # The diameter of the scafolding poles that we are using.
pole_wall_thickness = 3 # The thickness of the walls of the poles
joint_wall_thickness = 5 # The thickness of the walls of the joints
clip_wall_thickness = 1 # The thickness of the walls of the clips


# Boards
board_length = 2500 # Width of a standard plywood board
board_width = 1220 # Length of a standard plywood board
floor_board_thickness = 18 # The thickness of plywood boards used for the floor.
side_panel_board_thickness = 10 # Thickness of boards used in side panels. This has a max of 10mm due to fittings.
other_board_thickness = 10 # The tickness of the boards used for the walls and roof.


# Structure measurements
seat_height_from_ground = 1100 # The height that the toilet seat has to be from the ground to enable a solid waste container to be placed underneath.
seat_depth = 600 # The distance from the back wall to the edge of the seat.
seat_height_from_floor = 450 # The heignt the seat is from the floor of the structure
back_roof_height_from_floor = 2000 # The distance from the floor to the roof at the rear of the structure.
front_roof_height_from_floor = 2200 # The distance from the floor to the roof at the front of the structure.
wall_height_from_floor = 1900 # The distance from the floor and the top of the walls.
max_pole_underground = 500 # The maximum amount the poles will be sunk into the ground. Note on a slope only the higest points would be sunk in that much.
# TODO Check if this is used
board_overlap = 12 # The amount the boards are routed to overlap the scafolding pole. This should be a circular rout matching the diameter of the scaffolding pole as far as possible


# Calculated values based upon above parameters
###############################################
###############################################

# Diameters and radii
#####################
joint_diameter = pole_diameter + joint_wall_thickness * 2 # The overall diameter of the joint.
pole_radius = pole_diameter / 2
joint_radius = joint_diameter / 2

# Side panel separation
#######################
side_panel_seperation_x = board_length + side_panel_board_thickness

# Key planes in the y and z direction
#####################################

# In the y direction (front to back) there are 4 key planes
# The plane in which all the front joints are located
front_y = 0
# The plane in which all the back joints are located
back_y = front_y + board_width
# The plane that contains the joints supports the seat or urinal floor.
far_y = back_y - (seat_depth - pole_diameter)
# The plane that supports the cabin floor and the urinal floor
near_y = (front_y + far_y) / 2

# In the z direction (down to up) there are
# The plane for the joints at ground level
ground_z = 0
# The plane for the joints at seat level.
seat_z = seat_height_from_ground + pole_diameter + floor_board_thickness * 2
# The plane for the joints used for seat back support.
# Needed so that wheelie bins can slide straight in without obstructions.
seat_support_z = seat_z + joint_diameter
# The plane for joints at floor level.
floor_z = seat_z - seat_height_from_floor
# The plane for joints for the top of the side wall
wall_top_z = floor_z + wall_height_from_floor
# The plane for joints at the front of the roof.
front_roof_z = floor_z + front_roof_height_from_floor
# The plane for joints at the rear of the roof.
back_roof_z = floor_z + back_roof_height_from_floor

# Centre Vectors for Side_Panel joints.
#######################################

# Ground Joints
ground_front_centre = App.Vector(0, front_y, ground_z)
ground_near_centre = App.Vector(0, near_y, ground_z)
ground_far_centre = App.Vector(0, far_y, ground_z)
ground_back_centre = App.Vector(0, back_y, ground_z)

# Floor Joints
floor_front_centre = App.Vector(0, front_y, floor_z)
floor_near_centre = App.Vector(0, near_y, floor_z)
floor_far_centre = App.Vector(0, far_y, floor_z)
floor_back_centre = App.Vector(0, back_y, floor_z)

# Seat Joints
seat_far_centre = App.Vector(0, far_y, seat_z)
seat_back_centre = App.Vector(0, back_y, seat_z)
seat_back_support_centre = App.Vector(0, back_y, seat_support_z)

# Wall Top Joints
wall_top_front_centre = App.Vector(0, front_y, wall_top_z)
wall_top_back_centre = App.Vector(0, back_y, wall_top_z)

# Roof Joints
roof_front_centre = App.Vector(0, front_y, front_roof_z)
roof_back_centre = App.Vector(0, back_y, back_roof_z)