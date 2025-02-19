# This file contains all the class used for drawingused for drawing the component structures
# used for assembling composting toilets and urinals.

#  Import the packages that we need
import FreeCAD as App
import Arch
import Draft
import math
from BasicShapes import Shapes
from parameters import *
from fittings import *

class Structure:
    """ A class representing a generic component structure. It should 
    be subclassed by all component structures. Subclasses should create
    a list of parts and then call the class constructor with that list."""
    
    
    def __init__(self,
                freecad_document,
                structure_label,
                rotation = App.Rotation(0,0,0),
                location = App.Vector(0,0,0),
                parts_list = []):
        """ Constructs a Structure in the freecad_document, from the parts
        given in the parts_list parameter, with label attribute  given by
        parameter structure_label and centre and rotation given by the
        corresponding parameters.  """
        
        # Create structure
        structure = freecad_document.addObject("App::Part", structure_label)
        structure.addObjects(parts_list)

        # # Rotate
        structure.Placement = App.Placement(App.Vector(0,0,0), rotation, App.Vector(0,0,0))
        # Move
        Draft.move(structure, location)
        self.structure = structure

class Side_Panel(Structure):
    """ A class representing a modular side panel used in constructing
    composting toilets. The panel can be used on both left and right
    and can be configured with either a urinal floor or a sit down toilet floor."""
    
    def __init__(self,
                freecad_document,
                structure_label,
                rotation = App.Rotation(0,0,0),
                location = App.Vector(0,0,0)):
        """ Constructs a Side Panel in the freecad_document, with label attribute
        given by parameter structure_label and centre and rotation given by the
        corresponding parameters.  """

        # Create Joints
        ###############

        # Create ground joints
        ground_front_joint = Short_T(freecad_document = freecad_document,
                                           fitting_label = "Ground_Front_Joint",
                                           rotation = App.Rotation(0, 90, 90),
                                           centre = ground_front_centre)
        ground_near_joint = Four_Way_Cross(freecad_document = freecad_document, 
                                           fitting_label = "Ground_Near_Joint",
                                           rotation = App.Rotation(90, 0, 0),
                                           centre = ground_near_centre)
        ground_far_joint = Four_Way_Cross(freecad_document = freecad_document,
                                           fitting_label = "Ground_Far_Joint",
                                           rotation = App.Rotation(0, 0, 90),
                                           centre = ground_far_centre)
        ground_back_joint = Side_Outlet_T(freecad_document = freecad_document,
                                           fitting_label = "Ground_Back_Joint",
                                           rotation = App.Rotation(0, 0, 270),
                                           centre = ground_back_centre)
        # Create floor joints
        floor_front_joint = Side_Outlet_T(freecad_document = freecad_document,
                                           fitting_label = "Floor_Front_Joint",
                                           rotation = App.Rotation(0, 0, 90),
                                           centre = floor_front_centre)
        floor_near_joint = Side_Outlet_T(freecad_document = freecad_document,
                                           fitting_label = "Floor_Near_Joint",
                                           rotation = App.Rotation(0, 0, 0),
                                           centre = floor_near_centre)
        floor_far_joint = Four_Way_Cross(freecad_document = freecad_document,
                                           fitting_label = "Floor_Far_Joint",
                                           rotation = App.Rotation(0, 0, 90),
                                           centre = floor_far_centre)
        floor_back_joint = Side_Outlet_T(freecad_document = freecad_document,
                                           fitting_label = "Floor_Back_Joint",
                                           rotation = App.Rotation(0, 0, 270),
                                           centre = floor_back_centre)
        # Create seat joints
        seat_far_joint = Side_Outlet_T(freecad_document = freecad_document,
                                           fitting_label = "Seat_Far_Joint",
                                           rotation = App.Rotation(0, 0, 0),
                                           centre = seat_far_centre)
        seat_back_joint = Short_T(freecad_document = freecad_document,
                                           fitting_label = "Seat_Back_Joint",
                                           rotation = App.Rotation(0, 90, 270),
                                           centre = seat_back_centre)
        seat_back_support_joint = Two_Socket_Cross(freecad_document = freecad_document,
                                           fitting_label = "Seat_Back_Support_Joint",
                                           rotation = App.Rotation(0, 90, 0),
                                           centre = seat_back_support_centre)
        # Create wall top joints
        wall_top_front_joint = Short_T(freecad_document = freecad_document,
                                           fitting_label = "Wall_Top_Front_Joint",
                                           rotation = App.Rotation(0, 90, 90),
                                           centre = wall_top_front_centre)
        wall_top_back_joint = Short_T(freecad_document = freecad_document,
                                           fitting_label = "Wall_Top_Back_Joint",
                                           rotation = App.Rotation(0, 90, 270),
                                           centre = wall_top_back_centre)
        # Create roof joints
        roof_front_joint = Side_Outlet_T(freecad_document = freecad_document,
                                           fitting_label = "Roof_Front_Joint",
                                           rotation = App.Rotation(0, 0, 0),
                                           centre = roof_front_centre)
        roof_back_joint = Side_Outlet_T(freecad_document = freecad_document,
                                           fitting_label = "Roof_Back_Joint",
                                           rotation = App.Rotation(0, 0, 0),
                                           centre = roof_back_centre)

        # Make poles
        ############

        # Uprights
        front_upright_start = ground_front_centre + App.Vector(0, 0, - (max_pole_underground + pole_radius))
        front_upright_end = roof_front_centre + App.Vector(0, 0, - pole_radius)
        front_upright_line = Draft.make_line(front_upright_start, front_upright_end)
        front_upright = make_pole(front_upright_line, "Front_Upright")

        near_upright_start = ground_near_centre + App.Vector(0, 0, - (max_pole_underground + pole_radius))
        near_upright_end = floor_near_centre + App.Vector(0, 0,- pole_radius)
        near_upright_line = Draft.make_line(near_upright_start, near_upright_end)
        near_upright = make_pole(near_upright_line, "Near_Upright")

        far_upright_start = ground_far_centre + App.Vector(0, 0, - (max_pole_underground + pole_radius))
        far_upright_end = seat_far_centre + App.Vector(0, 0,- pole_radius)
        far_upright_line = Draft.make_line(far_upright_start, far_upright_end)
        far_upright = make_pole(far_upright_line, "Far_Upright")

        back_upright_start = ground_back_centre + App.Vector(0, 0, - (max_pole_underground + pole_radius))
        back_upright_end = roof_back_centre + App.Vector(0, 0,- pole_radius)
        back_upright_line = Draft.make_line(back_upright_start, back_upright_end)
        back_upright = make_pole(back_upright_line, "Back_Upright")

        #Cross Pieces
        wall_top_cross_start = wall_top_front_centre + App.Vector(0, pole_radius, 0)
        wall_top_cross_end = wall_top_back_centre + App.Vector(0, -pole_radius, 0)
        wall_top_cross_line = Draft.make_line(wall_top_cross_start, wall_top_cross_end)
        wall_top_cross = make_pole(wall_top_cross_line, "Wall_Top_Cross")

        seat_cross_start = seat_far_centre + App.Vector(0, - (pole_radius + joint_wall_thickness), 0)
        seat_cross_end = seat_back_centre + App.Vector(0, - pole_radius, 0)
        seat_cross_line = Draft.make_line(seat_cross_start, seat_cross_end)
        seat_cross = make_pole(seat_cross_line, "Seat_Cross")

        floor_front_cross_start = floor_front_centre + App.Vector(0, pole_radius , 0)
        floor_front_cross_end = floor_far_centre + App.Vector(0, - pole_radius, 0)
        floor_front_cross_line = Draft.make_line(floor_front_cross_start, floor_front_cross_end)
        floor_front_cross = make_pole(floor_front_cross_line, "Floor_Front_Cross")

        floor_rear_cross_start = floor_far_centre + App.Vector(0, pole_radius , 0)
        floor_rear_cross_end = floor_back_centre + App.Vector(0, - pole_radius, 0)
        floor_rear_cross_line = Draft.make_line(floor_rear_cross_start, floor_rear_cross_end)
        floor_rear_cross = make_pole(floor_rear_cross_line, "Floor_Rear_Cross")

        ground_front_cross_start = ground_front_centre + App.Vector(0, pole_radius , 0)
        ground_front_cross_end = ground_near_centre + App.Vector(0, - pole_radius, 0)
        ground_front_cross_line = Draft.make_line(ground_front_cross_start, ground_front_cross_end)
        ground_front_cross = make_pole(ground_front_cross_line, "Ground_Front_Cross")

        ground_mid_cross_start = ground_near_centre + App.Vector(0, pole_radius , 0)
        ground_mid_cross_end = ground_far_centre + App.Vector(0, - pole_radius, 0)
        ground_mid_cross_line = Draft.make_line(ground_mid_cross_start, ground_mid_cross_end)
        ground_mid_cross = make_pole(ground_mid_cross_line, "Ground_Mid_Cross")

        ground_back_cross_start = ground_far_centre + App.Vector(0, pole_radius , 0)
        ground_back_cross_end = ground_back_centre + App.Vector(0, - pole_radius, 0)
        ground_back_cross_line = Draft.make_line(ground_back_cross_start, ground_back_cross_end)
        ground_back_cross = make_pole(ground_back_cross_line, "Ground_Back_Cross")

        # Add plywood panels
        ####################

        x_panel_offset = side_panel_board_thickness / 2
        panel_width = back_y - front_y - pole_diameter
        panel_height = wall_top_z - floor_z - pole_diameter
        rect_1 = Draft.makeRectangle(panel_height, panel_width)
        panel_1 = Arch.makePanel(rect_1, thickness = side_panel_board_thickness)
        panel_1.Placement = App.Placement(
                App.Vector(0, 0, 0),
                App.Rotation(0, 270, 0),
                App.Vector(0, 0, 0))
        Draft.move(panel_1, App.Vector(x_panel_offset, pole_radius, pole_radius + floor_z))

        # TODO: Split single panel into 2-

        # TODO: Add fixings for panels.


        # Create a part containing all objects
        ######################################

        # Creat Parts List
        parts_list = [ground_front_joint.fitting,
                       ground_near_joint.fitting,
                       ground_far_joint.fitting,
                       ground_back_joint.fitting,
                       floor_front_joint.fitting,
                       floor_near_joint.fitting,
                       floor_far_joint.fitting,
                       floor_back_joint.fitting,
                       seat_far_joint.fitting,
                       seat_back_joint.fitting,
                       seat_back_support_joint.fitting,
                       wall_top_front_joint.fitting,
                       wall_top_back_joint.fitting,
                       roof_front_joint.fitting,
                       roof_back_joint.fitting,
                       front_upright,
                       near_upright,
                       far_upright,
                       back_upright,
                       wall_top_cross,
                       seat_cross,
                       floor_front_cross,
                       floor_rear_cross,
                       ground_front_cross,
                       ground_mid_cross,
                       ground_back_cross,
                       panel_1]
        
        super().__init__(freecad_document,
                        structure_label,
                        rotation,
                        location,
                        parts_list)

class Urinal_Floor(Structure):
    """ A class representing a Urinal Floor that would 
    form part of a set of composting toilet blocks."""
    
    
    def __init__(self,
                freecad_document,
                structure_label,
                rotation = App.Rotation(0,0,0),
                location = App.Vector(0,0,0)):
        """ Constructs a Urinal Floor in the freecad_document, with label attribute
        given by parameter structure_label and centre and rotation given by the
        corresponding parameters.  """

        left_offset = App.Vector(pole_radius, 0, 0)
        right_offset = App.Vector(side_panel_seperation_x - pole_radius, 0, 0)


        # Make poles
        front_pole_start = floor_front_centre + left_offset
        front_pole_end = floor_front_centre + right_offset
        front_pole_line = Draft.make_line(front_pole_start, front_pole_end)
        front_pole = make_pole(front_pole_line, "Front_Pole")

        near_pole_start = floor_near_centre + left_offset
        near_pole_end = floor_near_centre + right_offset
        near_pole_line = Draft.make_line(near_pole_start, near_pole_end)
        near_pole = make_pole(near_pole_line, "Near_Pole")

        far_pole_start = floor_far_centre + left_offset
        far_pole_end = floor_far_centre + right_offset
        far_pole_line = Draft.make_line(far_pole_start, far_pole_end)
        far_pole = make_pole(far_pole_line, "Far_Pole")

        back_pole_start = floor_back_centre + left_offset
        back_pole_end = floor_back_centre + right_offset
        back_pole_line = Draft.make_line(back_pole_start, back_pole_end)
        back_pole = make_pole(back_pole_line, "Back_Pole")

        # Make Board
        floor_rect = Draft.makeRectangle(board_length, board_width)
        floor_panel = Arch.makePanel(floor_rect, thickness = floor_board_thickness)
        floor_panel.Placement = App.Placement(
                App.Vector(0, 0, 0),
                App.Rotation(0, 0, 0),
                App.Vector(0, 0, 0))
        floor_panel.Label = "Floor"
        Draft.move(floor_panel, App.Vector(side_panel_board_thickness / 2,
                                       0,
                                       floor_z + joint_radius))

        # TODO: Add fixings for boards


        # Add joints for Rear and Front
        front_left_third_joint  = Short_T(freecad_document = freecad_document,
                                           fitting_label = "Front_Left_Third_Joint",
                                           rotation = App.Rotation(0, 0, 180),
                                           centre = front_floor_left_third_centre)
        front_right_third_joint  = Short_T(freecad_document = freecad_document,
                                           fitting_label = "Front_Right_Third_Joint",
                                           rotation = App.Rotation(0, 0, 180),
                                           centre = front_floor_right_third_centre)
        back_left_third_joint  = Short_T(freecad_document = freecad_document,
                                           fitting_label = "Back_Left_Third_Joint",
                                           rotation = App.Rotation(0, 0, 180),
                                           centre = back_floor_left_third_centre)
        back_right_third_joint  = Short_T(freecad_document = freecad_document,
                                           fitting_label = "Back_Right_Third_Joint",
                                           rotation = App.Rotation(0, 0, 180),
                                           centre = back_floor_right_third_centre)



        # # # Create a compound of all objects
        parts_list = [front_pole,
                      near_pole,
                      far_pole,
                      back_pole,
                      floor_panel,
                      front_left_third_joint.fitting,
                      front_right_third_joint.fitting,
                      back_left_third_joint.fitting,
                      back_right_third_joint.fitting]
        
        super().__init__(freecad_document,
                        structure_label,
                        rotation,
                        location,
                        parts_list)



class Cabin_Ground(Structure):
    """ A class representing a Cabin Ground structure used as part of
    a composting toilet project. The solid waste container sits
    snugly between the Cabin Ground and the toilet seat that is
    part of the Cabin Floor structure so as to prevent the entry
    flies into the container."""
    
    
    def __init__(self,
                freecad_document,
                structure_label,
                rotation = App.Rotation(0,0,0),
                location = App.Vector(0,0,0)):
        """ Constructs a Cabin_Ground in the freecad_document, with label attribute
        given by parameter structure_label and centre and rotation given by the
        corresponding parameters.  """

        left_offset = App.Vector(pole_radius, 0, 0)
        right_offset = App.Vector(side_panel_seperation_x - pole_radius, 0, 0)


        # Make poles

        far_pole_start = ground_far_centre + left_offset
        far_pole_end = ground_far_centre + right_offset
        far_pole_line = Draft.make_line(far_pole_start, far_pole_end)
        far_pole = make_pole(far_pole_line, "Far_Pole")

        back_pole_start = ground_back_centre + left_offset
        back_pole_end = ground_back_centre + right_offset
        back_pole_line = Draft.make_line(back_pole_start, back_pole_end)
        back_pole = make_pole(back_pole_line, "Back_Pole")

        # Make Board
        board_overlap = Double_Fixing_Pad.width / 2
        floor_rect = Draft.makeRectangle(board_length, back_y - far_y + board_overlap *2)
        floor_panel = Arch.makePanel(floor_rect, thickness = floor_board_thickness)
        floor_panel.Label = "Ground"
        Draft.move(floor_panel, App.Vector(side_panel_board_thickness / 2,
                                       far_y - board_overlap,
                                       ground_z + joint_radius))

        # TODO: Add fixings for boards



        # # # Create a compound of all objects
        parts_list = [far_pole,
                      back_pole,
                      floor_panel]
        
        super().__init__(freecad_document,
                        structure_label,
                        rotation,
                        location,
                        parts_list)


class Cabin_Floor(Structure):
    """ A class representing a Cabin Floor that would 
    form part of a set of composting toilet blocks."""

    seat_start_y = far_y - pole_radius - floor_board_thickness
    
    def __init__(self,
                freecad_document,
                structure_label,
                rotation = App.Rotation(0,0,0),
                location = App.Vector(0,0,0)):
        """ Constructs a Cabin Floor in the freecad_document, with label attribute
        given by parameter structure_label and centre and rotation given by the
        corresponding parameters.  """

        left_offset = App.Vector(pole_radius, 0, 0)
        right_offset = App.Vector(side_panel_seperation_x - pole_radius, 0, 0)


        # Make poles
        front_pole_start = floor_front_centre + left_offset
        front_pole_end = floor_front_centre + right_offset
        front_pole_line = Draft.make_line(front_pole_start, front_pole_end)
        front_pole = make_pole(front_pole_line, "Front_Pole")

        near_pole_start = floor_near_centre + left_offset
        near_pole_end = floor_near_centre + right_offset
        near_pole_line = Draft.make_line(near_pole_start, near_pole_end)
        near_pole = make_pole(near_pole_line, "Near_Pole")

        far_pole_1_start = floor_far_centre + left_offset
        far_pole_1_end = floor_far_centre + right_offset
        far_pole_1_line = Draft.make_line(far_pole_1_start, far_pole_1_end)
        far_pole_1 = make_pole(far_pole_1_line, "Far_Pole_1")

        far_pole_2_start = seat_far_centre + left_offset
        far_pole_2_end = seat_far_centre + right_offset
        far_pole_2_line = Draft.make_line(far_pole_2_start, far_pole_2_end)
        far_pole_2 = make_pole(far_pole_2_line, "Far_Pole_2")

        back_pole_start = seat_back_support_centre + left_offset
        back_pole_end = seat_back_support_centre + right_offset
        back_pole_line = Draft.make_line(back_pole_start, back_pole_end)
        back_pole = make_pole(back_pole_line, "Back_Pole")

        # Make Boards
        floor_width = far_y + Double_Fixing_Pad.width / 2
        floor_rect = Draft.makeRectangle(board_length, floor_width)
        floor_panel = Arch.makePanel(floor_rect, thickness = floor_board_thickness)
        floor_panel.Label = "Floor"
        floor_start_z = floor_z + joint_radius
        Draft.move(floor_panel, App.Vector(side_panel_board_thickness / 2,
                                       0,
                                       floor_start_z))
        
        seat_end_y = back_y + Double_Fixing_Pad.width / 2
        seat_width = seat_end_y - Cabin_Floor.seat_start_y
        seat_rect = Draft.makeRectangle(board_length, seat_width)
        seat_panel = Arch.makePanel(seat_rect, thickness = floor_board_thickness)
        seat_panel.Label = "Seat"
        seat_start_z = seat_z + pole_radius
        Draft.move(seat_panel, App.Vector(side_panel_board_thickness / 2,
                                       Cabin_Floor.seat_start_y,
                                       seat_start_z))
        
        side_start_z = floor_start_z + floor_board_thickness
        side_end_z = seat_start_z
        side_width = side_end_z - side_start_z
        side_rect = Draft.makeRectangle(board_length, side_width)
        side_panel = Arch.makePanel(side_rect, thickness = floor_board_thickness)
        side_panel.Label = "Side"
        side_panel.Placement = App.Placement(
                App.Vector(0, 0, 0),
                App.Rotation(0, 0, 90),
                App.Vector(0, 0, 0))
        Draft.move(side_panel, App.Vector(0,
                                       Cabin_Floor.seat_start_y + floor_board_thickness,
                                       side_start_z))

        # TODO: Add fixings for boards


        # TODO: Add joints for Rear and Front
        front_left_third_joint  = Short_T(freecad_document = freecad_document,
                                           fitting_label = "Front_Left_Third_Joint",
                                           rotation = App.Rotation(0, 0, 180),
                                           centre = front_floor_left_third_centre)
        front_right_third_joint  = Short_T(freecad_document = freecad_document,
                                           fitting_label = "Front_Right_Third_Joint",
                                           rotation = App.Rotation(0, 0, 180),
                                           centre = front_floor_right_third_centre)
        back_left_third_joint  = Short_T(freecad_document = freecad_document,
                                           fitting_label = "Back_Left_Third_Joint",
                                           rotation = App.Rotation(0, 0, 180),
                                           centre = back_seat_left_third_centre)
        back_right_third_joint  = Short_T(freecad_document = freecad_document,
                                           fitting_label = "Back_Right_Third_Joint",
                                           rotation = App.Rotation(0, 0, 180),
                                           centre = back_seat_right_third_centre)



        # # # Create a compound of all objects
        parts_list = [front_pole,
                      near_pole,
                      far_pole_1,
                      far_pole_2,
                      back_pole,
                      floor_panel,
                      seat_panel,
                      side_panel,
                      front_left_third_joint.fitting,
                      front_right_third_joint.fitting,
                      back_left_third_joint.fitting,
                      back_right_third_joint.fitting]
        
        super().__init__(freecad_document,
                        structure_label,
                        rotation,
                        location,
                        parts_list)

class Cabin_Back(Structure):
    """ A class representing a Cabin Back structure used as part of
    a composting toilet project."""
    
    board_start_y = back_y - joint_radius

    def __init__(self,
                freecad_document,
                structure_label,
                rotation = App.Rotation(0,0,0),
                location = App.Vector(0,0,0)):
        """ Constructs a Cabin_Back in the freecad_document, with label attribute
        given by parameter structure_label and centre and rotation given by the
        corresponding parameters.  """

        left_offset = App.Vector(pole_radius, 0, 0)
        right_offset = App.Vector(side_panel_seperation_x - pole_radius, 0, 0)

        # Make joints

        roof_Left_Third_joint  = Short_T(freecad_document = freecad_document,
                                           fitting_label = "Roof_left_third_Joint",
                                           rotation = App.Rotation(0, 0, 0),
                                           centre = back_roof_left_third_centre)
        roof_right_third_joint  = Short_T(freecad_document = freecad_document,
                                           fitting_label = "Roof_Right_Third_Joint",
                                           rotation = App.Rotation(0, 0, 0),
                                           centre = back_roof_right_third_centre)

        # Make poles

        pole_offset = App.Vector(0, 0, pole_radius)

        left_third_pole_start = back_seat_left_third_centre + pole_offset
        left_third_pole_end = back_roof_left_third_centre - pole_offset
        left_third_pole_line = Draft.make_line(left_third_pole_start, left_third_pole_end)
        left_third_pole = make_pole(left_third_pole_line, "Left_Third_Pole")

        right_third_pole_start = back_seat_right_third_centre + pole_offset
        right_third_pole_end = back_roof_right_third_centre - pole_offset
        right_third_pole_line = Draft.make_line(right_third_pole_start, right_third_pole_end)
        right_third_pole = make_pole(right_third_pole_line, "Right_Third_Pole")

        # Make Board
        board_start_z = seat_z + pole_radius + floor_board_thickness
        back_panel_rect = Draft.makeRectangle(board_length, 
                                              wall_top_z - 
                                              board_start_z)
        back_panel = Arch.makePanel(back_panel_rect, 
                                    thickness = other_board_thickness)
        back_panel.Label = "Back_Panel"
        back_panel.Placement = App.Placement(
                App.Vector(0, 0, 0),
                App.Rotation(0, 0, 90),
                App.Vector(0, 0, 0))
        Draft.move(back_panel, App.Vector(0,
                        Cabin_Back.board_start_y,
                        board_start_z))

        # TODO: Add fixings for boards

        # Create a parts list
        parts_list = [roof_Left_Third_joint.fitting,
                      roof_right_third_joint.fitting,
                      left_third_pole,
                      right_third_pole,
                      back_panel]
        
        super().__init__(freecad_document,
                        structure_label,
                        rotation,
                        location,
                        parts_list)
        
class Urinal_Back(Structure):
    """ A class representing a Urinal Back structure used as part of
    a composting toilet project."""
    
    board_start_y = back_y - joint_radius
    
    def __init__(self,
                freecad_document,
                structure_label,
                rotation = App.Rotation(0,0,0),
                location = App.Vector(0,0,0)):
        """ Constructs a Urinal Back in the freecad_document, with label attribute
        given by parameter structure_label and centre and rotation given by the
        corresponding parameters.  """

        left_offset = App.Vector(pole_radius, 0, 0)
        right_offset = App.Vector(side_panel_seperation_x - pole_radius, 0, 0)

        # Make joints

        roof_left_third_joint  = Short_T(freecad_document = freecad_document,
                                           fitting_label = "Roof_Left_Third_Joint",
                                           rotation = App.Rotation(0, 0, 0),
                                           centre = back_roof_left_third_centre)
        roof_right_third_joint  = Short_T(freecad_document = freecad_document,
                                           fitting_label = "Roof_Right_Third_Joint",
                                           rotation = App.Rotation(0, 0, 0),
                                           centre = back_roof_right_third_centre)

        # Make poles

        pole_offset = App.Vector(0, 0, pole_radius)

        left_third_pole_start = back_floor_left_third_centre + pole_offset
        left_third_pole_end = back_roof_left_third_centre - pole_offset
        left_third_pole_line = Draft.make_line(left_third_pole_start, left_third_pole_end)
        left_third_pole = make_pole(left_third_pole_line, "Left_Third_Pole")

        right_third_pole_start = back_floor_right_third_centre + pole_offset
        right_third_pole_end = back_roof_right_third_centre - pole_offset
        right_third_pole_line = Draft.make_line(right_third_pole_start, right_third_pole_end)
        right_third_pole = make_pole(right_third_pole_line, "Right_Third_Pole")

        # Make Board
        board_start_z = floor_z + pole_radius + floor_board_thickness
        back_panel_rect = Draft.makeRectangle(board_length, 
                                              wall_top_z - 
                                              board_start_z)
        back_panel = Arch.makePanel(back_panel_rect, 
                                    thickness = other_board_thickness)
        back_panel.Label = "Back_Panel"
        back_panel.Placement = App.Placement(
                App.Vector(0, 0, 0),
                App.Rotation(0, 0, 90),
                App.Vector(0, 0, 0))
        Draft.move(back_panel, App.Vector(0,
                        Urinal_Back.board_start_y,
                        board_start_z))

        # TODO: Add fixings for boards

        # Create a parts list
        parts_list = [roof_left_third_joint.fitting,
                      roof_right_third_joint.fitting,
                      left_third_pole,
                      right_third_pole,
                      back_panel]
        
        super().__init__(freecad_document,
                        structure_label,
                        rotation,
                        location,
                        parts_list)
        
class Cabin_Partition(Structure):
    """ A class representing a Cabin Partition structure used as part of
    a composting toilet project."""
    
    def __init__(self,
                freecad_document,
                structure_label,
                rotation = App.Rotation(0,0,0),
                location = App.Vector(0,0,0)):
        """ Constructs a Cabin Partition in the freecad_document, with label attribute
        given by parameter structure_label and centre and rotation given by the
        corresponding parameters.  """

        # Make joint

        roof_joint  = Short_T(freecad_document = freecad_document,
                                fitting_label = "Roof_Joint",
                                rotation = App.Rotation(0, 0, 0),
                                centre = roof_front_centre)


        # Make pole

        pole_offset = App.Vector(0, 0, pole_radius)

        pole_start = floor_front_centre + pole_offset
        pole_end = roof_front_centre - pole_offset
        pole_line = Draft.make_line(pole_start, pole_end)
        pole = make_pole(pole_line, "Pole")

        # Make Board
        board_start_z = floor_z + joint_radius + floor_board_thickness
        panel_width = board_width - pole_radius - joint_radius - other_board_thickness
        panel_rect = Draft.makeRectangle(wall_top_z - 
                                        board_start_z,
                                        panel_width)
        panel = Arch.makePanel(panel_rect, 
                                    thickness = side_panel_board_thickness)
        panel.Label = "Panel"
        cutout_height = seat_z - floor_z
        cutout_width = Cabin_Back.board_start_y - Cabin_Floor.seat_start_y
        cutout_rect = Draft.makeRectangle(cutout_height, cutout_width)
        cutout = Arch.makePanel(cutout_rect, 
                                thickness = side_panel_board_thickness)
        Draft.move(cutout, App.Vector(0, panel_width - cutout_width, 0))
        panel = Draft.cut(panel, cutout)
        panel.Placement = App.Placement(
                App.Vector(0, 0, 0),
                App.Rotation(0, 270, 0),
                App.Vector(0, 0, 0))
        Draft.move(panel, App.Vector(side_panel_board_thickness / 2,
                                     pole_radius,
                                     board_start_z))

        # TODO: Add fixings for boards

        # Create a parts list
        parts_list = [roof_joint.fitting,
                      pole,
                      panel]
        
        super().__init__(freecad_document,
                        structure_label,
                        rotation,
                        location,
                        parts_list)
        

       
class Roof(Structure):
    """ A class representing a Roof structure used as part of
    a composting toilet project."""
    
    def __init__(self,
                freecad_document,
                structure_label,
                rotation = App.Rotation(0,0,0),
                location = App.Vector(0,0,0)):
        """ Constructs a Roof in the freecad_document, with label attribute
        given by parameter structure_label and centre and rotation given by the
        corresponding parameters.  """

        # Calculate angles and pole offset vectors
        opposite_side = front_roof_z - back_roof_z
        adjacent_side = board_width
        pitch_angle_radians = math.atan(opposite_side/adjacent_side)
        pitch_angle_degrees = math.degrees(pitch_angle_radians)
        down_angle = - pitch_angle_degrees + 90
        up_angle = - pitch_angle_degrees + 270
        # So to to find how much the y and z are scaled for a unit length
        # y^2 + z^2 = 1^2 and ....1 (Pythagoras Theorem)
        # If we define
        # y_z_ratio = y/z  ....2
        # WhereThen for this case:
        y_z_ratio = adjacent_side / opposite_side
        # From 2. y = z * y_z_ratio  ....3
        # So from 1. (z * y_z_ratio)^2 + z^2 = 1
        # So z^2*(y_Z_ratio^2 + 1) = 1
        # So
        scale_z = 1 / math.sqrt(y_z_ratio**2 + 1)
        # From 3.
        scale_y = scale_z * y_z_ratio
        pole_offset = pole_radius * App.Vector(0, scale_y, -scale_z)

        # Make joints
        front_left_quarter_joint  = Short_T(freecad_document = freecad_document,
                                fitting_label = "Front_Left_Quarter_Joint",
                                rotation = App.Rotation(0, 0, down_angle),
                                centre = front_roof_left_quarter_centre)
        front_middle_joint  = Short_T(freecad_document = freecad_document,
                                fitting_label = "Front_Middle_Joint",
                                rotation = App.Rotation(0, 0, down_angle),
                                centre = front_roof_middle_centre)
        front_right_quarter_joint  = Short_T(freecad_document = freecad_document,
                                fitting_label = "Front Right_Quarter_Joint",
                                rotation = App.Rotation(0, 0, down_angle),
                                centre = front_roof_right_quarter_centre)
        

        back_left_quarter_joint  = Short_T(freecad_document = freecad_document,
                                fitting_label = "Back_Left_Quarter_Joint",
                                rotation = App.Rotation(0, 0, up_angle),
                                centre = back_roof_left_quarter_centre)
        back_middle_joint  = Short_T(freecad_document = freecad_document,
                                fitting_label = "Back_Middle_Joint",
                                rotation = App.Rotation(0, 0, up_angle),
                                centre = back_roof_middle_centre)
        back_right_quarter_joint  = Short_T(freecad_document = freecad_document,
                                fitting_label = "Back_Right_Quarter_Joint",
                                rotation = App.Rotation(0, 0, up_angle),
                                centre = back_roof_right_quarter_centre)


        # Make poles

        left_quarter_pole_start = front_roof_left_quarter_centre + pole_offset
        left_quarter_pole_end = back_roof_left_quarter_centre - pole_offset
        left_quarter_pole_line = Draft.make_line(left_quarter_pole_start, left_quarter_pole_end)
        left_quarter_pole = make_pole(left_quarter_pole_line, "Left_Quarter_Pole")
        
        middle_pole_start = front_roof_middle_centre + pole_offset
        middle_pole_end = back_roof_middle_centre - pole_offset
        middle_pole_line = Draft.make_line(middle_pole_start, middle_pole_end)
        middle_pole = make_pole(middle_pole_line, "Middle_Pole")

        right_quarter_pole_start = front_roof_right_quarter_centre + pole_offset
        right_quarter_pole_end = back_roof_right_quarter_centre - pole_offset
        right_quarter_pole_line = Draft.make_line(right_quarter_pole_start, right_quarter_pole_end)
        right_quarter_pole = make_pole(right_quarter_pole_line, "Right_Quarter_Pole")

        # # Make Board
        board_start_y = -roof_overlap * scale_y
        board_start_z = front_roof_z + (roof_overlap * scale_z) + joint_radius

        panel_width = board_width + roof_overlap * 2
        panel_rect = Draft.makeRectangle(board_length,
                                        panel_width)
        panel = Arch.makePanel(panel_rect, 
                                    thickness = side_panel_board_thickness)
        panel.Label = "Panel"
        panel.Placement = App.Placement(
                App.Vector(0, 0, 0),
                App.Rotation(0, 0, -pitch_angle_degrees),
                App.Vector(0, 0, 0))
        Draft.move(panel, App.Vector(0,
                                     board_start_y,
                                     board_start_z))

        # TODO: Add fixings for boards

        # Create a parts list
        parts_list = [front_left_quarter_joint.fitting,
                      front_middle_joint.fitting,
                      front_right_quarter_joint.fitting,
                      back_left_quarter_joint.fitting,
                      back_middle_joint.fitting,
                      back_right_quarter_joint.fitting,
                      left_quarter_pole,
                      middle_pole,
                      right_quarter_pole,
                      panel]
        
        super().__init__(freecad_document,
                        structure_label,
                        rotation,
                        location,
                        parts_list)
        
class Front_Roof_Pole(Structure):
    """ A class representing a Front Roof Pole structure used as part of
    a composting toilet project."""
    
    def __init__(self,
                freecad_document,
                structure_label,
                rotation = App.Rotation(0,0,0),
                location = App.Vector(0,0,0)):
        """ Constructs a Front Roof Pole in the freecad_document, with label attribute
        given by parameter structure_label and centre and rotation given by the
        corresponding parameters.  """

        # Make pole
        pole_start = roof_front_centre
        pole_end = front_roof_right_centre
        pole_line = Draft.make_line(pole_start, pole_end)
        pole = make_pole(pole_line, "Pole")

        # Create a parts list
        parts_list = [pole]
        
        super().__init__(freecad_document,
                        structure_label,
                        rotation,
                        location,
                        parts_list)
        
class Back_Roof_Pole(Structure):
    """ A class representing a Back Roof Pole structure used as part of
    a composting toilet project."""
    
    def __init__(self,
                freecad_document,
                structure_label,
                rotation = App.Rotation(0,0,0),
                location = App.Vector(0,0,0)):
        """ Constructs a Back Roof Pole in the freecad_document, with label attribute
        given by parameter structure_label and centre and rotation given by the
        corresponding parameters.  """

        # Make pole
        pole_start = roof_back_centre
        pole_end = back_roof_right_centre
        pole_line = Draft.make_line(pole_start, pole_end)
        pole = make_pole(pole_line, "Pole")

        # Create a parts list
        parts_list = [pole]
        
        super().__init__(freecad_document,
                        structure_label,
                        rotation,
                        location,
                        parts_list)
        

