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


class Urinal_Floor:
    """ A class representing a urinal floor used as part of
    a composting toilet project"""
    
    
    def __init__(self,
                freecad_document,
                structure_label,
                rotation = App.Rotation(0,0,0),
                centre = App.Vector(0,0,0)):
        """ Constructs a Urinal Floor in the freecad_document, with label attribute
        given by parameter structure_label and centre and rotation given by the
        corresponding parameters.  """

        # Calculate z and y coordinates for joints
        joint_seat_z = seat_height_from_ground + pole_diameter + floor_board_thickness * 2
        joint_floor_z = joint_seat_z - seat_height_from_floor
        front_y = 0
        back_y = front_y + board_width - pole_diameter
        far_y = back_y - (seat_depth - pole_diameter)
        near_y = (front_y + far_y) / 2
        pole_radius = pole_diameter / 2
        side_panel_separation = board_length + side_panel_board_thickness
        left_x = pole_radius
        right_x = side_panel_separation - pole_radius
        left_centre_x = side_panel_separation / 3
        right_centre_x = side_panel_separation / 3


        # Make poles
        front_pole_start = App.Vector(left_x, front_y, joint_floor_z)
        front_pole_end = App.Vector(right_x, front_y, joint_floor_z)
        front_pole_line = Draft.make_line(front_pole_start, front_pole_end)
        front_pole = make_pole(front_pole_line, "Front_Pole")

        near_pole_start = App.Vector(left_x, near_y, joint_floor_z)
        near_pole_end = App.Vector(right_x, near_y, joint_floor_z)
        near_pole_line = Draft.make_line(near_pole_start, near_pole_end)
        near_pole = make_pole(near_pole_line, "Near_Pole")

        far_pole_start = App.Vector(left_x, far_y, joint_floor_z)
        far_pole_end = App.Vector(right_x, far_y, joint_floor_z)
        far_pole_line = Draft.make_line(far_pole_start, far_pole_end)
        far_pole = make_pole(far_pole_line, "Far_Pole")

        back_pole_start = App.Vector(left_x, back_y, joint_floor_z)
        back_pole_end = App.Vector(right_x, back_y, joint_floor_z)
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
                                       joint_floor_z + pole_radius + joint_wall_thickness))

        # TODO: Add fixings for boards


        # TODO: Add joints for Rear and Front



        

        # # # Create a compound of all objects
        parts_list = [front_pole,
                      near_pole,
                      far_pole,
                      back_pole,
                      floor_panel]
        
        # Create compound
        structure = freecad_document.addObject("Part::Compound", structure_label)
        structure.Links = parts_list
        # Set visibility of all objects in compound to true (not sure why adding them to a compound set them to invisible.)
        for part in parts_list :
            part.Visibility = True
        # # Rotate
        structure.Placement = App.Placement(App.Vector(0,0,0), rotation, App.Vector(0,0,0))
        # Move
        Draft.move(structure, centre)
        self.structure = structure
