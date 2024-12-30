# This file contains all the class used for drawing

#  Import the packages that we need
import FreeCAD as App
import Arch
import Draft
from BasicShapes import Shapes
from parameters import seat_height_from_ground
from parameters import pole_diameter
from parameters import floor_board_thickness
from parameters import seat_height_from_floor
from parameters import roof_height_from_floor
from parameters import wall_top_from_roof
from parameters import board_width
from parameters import seat_depth
from fittings import *


class Side_Panel:
    """ A class representing a modular side panel used in constructing
    composting toilets. The panel can be used on both left and right
    and can be configured with either a urinal floor or a sit down toilet floor."""
    
    # This is copy and paste guff TODO check.
    # length = 44.5
    # distance_to_hole = 53
    # pad_width = distance_to_hole - pole_diameter / 2 + length / 2
    
    def __init__(self,
                freecad_document,
                structure_label,
                rotation = App.Rotation(0,0,0),
                centre = App.Vector(0,0,0)):
        """ Constructs a Side Panel in the freecad_document, with label attribute
        given by parameter structure_label and centre and rotation given by the
        corresponding parameters.  """

        # Calculate z and y coordinates for joints
        joint_ground_z = 0
        joint_seat_z = seat_height_from_ground + pole_diameter + floor_board_thickness * 2
        joint_floor_z = joint_seat_z - seat_height_from_floor
        roof_mid_height = joint_floor_z + roof_height_from_floor
        joint_front_roof_z = roof_mid_height + roof_pitch_differance / 2
        joint_back_roof_z = roof_mid_height - roof_pitch_differance / 2
        joint_wall_top_z = roof_mid_height - wall_top_from_roof
        front_y = 0
        back_y = front_y + board_width - pole_diameter
        far_y = back_y - (seat_depth - pole_diameter)
        near_y = (front_y + far_y) / 2

        # Calculate point vectors for joints and connecting poles.
        ##########################################################
        offset = pole_diameter / 2

        # Ground Joints
        ground_front_centre = App.Vector(0, front_y, joint_ground_z)
        self.ground_front_left = ground_front_centre - App.Vector(-offset, 0, 0)
        self.ground_front_right = ground_front_centre - App.Vector(offset, 0, 0)

        ground_near_centre = App.Vector(0, near_y, joint_ground_z)
        self.ground_near_left = ground_near_centre - App.Vector(-offset, 0, 0)
        self.ground_near_right = ground_near_centre - App.Vector(offset, 0, 0)

        ground_far_centre = App.Vector(0, far_y, joint_ground_z)
        self.ground_far_left = ground_far_centre + App.Vector(-offset, 0, 0)
        self.ground_far_right = ground_far_centre + App.Vector(offset, 0, 0)

        ground_back_centre = App.Vector(0, back_y, joint_ground_z)
        self.ground_back_left = ground_back_centre + App.Vector(-offset, 0, 0)
        self.ground_back_right = ground_back_centre + App.Vector(offset, 0, 0)

        # Floor Joints
        floor_front_centre = App.Vector(0, front_y, joint_floor_z)
        self.floor_front_left = floor_front_centre - App.Vector(-offset, 0, 0)
        self.floor_front_right = floor_front_centre - App.Vector(offset, 0, 0)

        floor_near_centre = App.Vector(0, near_y, joint_floor_z)
        self.floor_near_left = floor_near_centre - App.Vector(-offset, 0, 0)
        self.floor_near_right = floor_near_centre - App.Vector(offset, 0, 0)

        floor_far_centre = App.Vector(0, far_y, joint_floor_z)
        self.floor_far_left = floor_far_centre + App.Vector(-offset, 0, 0)
        self.floor_far_right = floor_far_centre + App.Vector(offset, 0, 0)

        floor_back_centre = App.Vector(0, back_y, joint_floor_z)
        self.floor_back_left = floor_back_centre + App.Vector(-offset, 0, 0)
        self.floor_back_right = floor_back_centre + App.Vector(offset, 0, 0)

        # Seat Joints
        seat_far_centre = App.Vector(0, far_y, joint_seat_z)
        self.seat_far_left = seat_far_centre + App.Vector(-offset, 0, 0)
        self.seat_far_right = seat_far_centre + App.Vector(offset, 0, 0)

        seat_back_centre = App.Vector(0, back_y, joint_seat_z)
        self.seat_back_left = seat_back_centre + App.Vector(-offset, 0, 0)
        self.seat_back_right = seat_back_centre + App.Vector(offset, 0, 0)

        # Wall Top Joints
        wall_top_front_centre = App.Vector(0, front_y, joint_wall_top_z)
        self.wall_top_front_left = wall_top_front_centre - App.Vector(-offset, 0, 0)
        self.wall_top_front_right = wall_top_front_centre - App.Vector(offset, 0, 0)

        wall_top_back_centre = App.Vector(0, back_y, joint_wall_top_z)
        self.wall_top_back_left = wall_top_back_centre + App.Vector(-offset, 0, 0)
        self.wall_top_back_right = wall_top_back_centre + App.Vector(offset, 0, 0)

        # Roof Joints
        roof_front_centre = App.Vector(0, front_y, joint_front_roof_z)
        self.roof_front_left = roof_front_centre - App.Vector(0, 0, 0)
        self.roof_front_right = roof_front_centre - App.Vector(0, 0, 0)

        roof_back_centre = App.Vector(0, back_y, joint_back_roof_z)
        self.roof_back_left = roof_back_centre + App.Vector(0, 0, 0)
        self.roof_back_right = roof_back_centre + App.Vector(0, 0, 0)


        # Create Joints
        ###############

        # Create ground joints
        ground_front_joint = Side_Outlet_T(freecad_document = freecad_document, #TODO Change fitting to Long/Short T and rotate sifferently
                                           fitting_label = "Ground_Front_Joint",
                                           rotation = App.Rotation(0, 0, 90),
                                           centre = ground_front_centre)
        ground_near_joint = Four_Way_Cross(freecad_document = freecad_document, #TODO change rotation so that sides dont protrude.
                                           fitting_label = "Ground_Near_Joint",
                                           rotation = App.Rotation(0, 0, 270),
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
        seat_back_joint = Side_Outlet_T(freecad_document = freecad_document,
                                           fitting_label = "Seat_Back_Joint",
                                           rotation = App.Rotation(0, 0, 270),
                                           centre = seat_back_centre)
        # Create wall top joints
        wall_top_front_joint = Side_Outlet_T(freecad_document = freecad_document, # Change to Long/Short T
                                           fitting_label = "Wall_Top_Front_Joint",
                                           rotation = App.Rotation(0, 90, 90),
                                           centre = wall_top_front_centre)
        wall_top_back_joint = Side_Outlet_T(freecad_document = freecad_document, # Change to Long/Short T
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
        pole_radius = pole_diameter / 2

        # Uprights
        front_upright_start = ground_front_centre + App.Vector(0, 0, - (max_pole_underground + pole_radius))
        front_upright_end = roof_front_centre + App.Vector(0, 0,- pole_radius)
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
        panel_height = joint_wall_top_z - joint_floor_z - pole_diameter
        rect_1 = Draft.makeRectangle(panel_height, panel_width)
        panel_1 = Arch.makePanel(rect_1, thickness = side_panel_board_thickness)
        panel_1.Placement = App.Placement(
                App.Vector(0, 0, 0),
                App.Rotation(0, 270, 0),
                App.Vector(0, 0, 0))
        Draft.move(panel_1, App.Vector(x_panel_offset, pole_radius, pole_radius + joint_floor_z))


        # # Create a compound of all objects
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
        
        # Create compound
        structure = freecad_document.addObject("Part::Compound", structure_label)
        structure.Links = parts_list
        # Set visibility of all objects in compound to true (not sure why adding them to a compound set them to invisible.)
        for part in parts_list :
            part.Visibility = True
        # Rotate
        structure.Placement = App.Placement(App.Vector(0,0,0), rotation, App.Vector(0,0,0))
        # Move
        Draft.move(structure, centre)
        self.structure = structure
