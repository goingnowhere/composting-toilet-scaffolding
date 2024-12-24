# This file contains all the functions used for drawing
# fittings used to connect scaffolding pipes.

#  Import the packages that we need - TODO check that all of these are needed
import FreeCAD as App
# import Part
# import Sketcher
import Arch
# import Part
import Draft
# import FreeCADGui as Gui
# import math
# import WorkingPlane
# import App

from parameters import *

def display_variable(name, value):
    App.Console.PrintMessage(name)
    App.Console.PrintMessage(": ")
    App.Console.PrintMessage(value)
    App.Console.PrintMessage("\n")

def make_pole(line, name):
    """ Makes a standard 48,3 scafolding pole along the 
    given line with the given name """
    pole = Arch.makePipe(line, diameter=pole_diameter)
    pole.WallThickness = joint_wall_thickness
    pole.Label = name
    return pole

class Side_Outlet_T:
    """ A class representing a Side Outlet T fitting for standard 48,3 scaffolding
     This is a model of the following fitting:
    https://pipedreamfittings.com/product/side-outlet-tee-42mm-c42/  """

    distance_from_centre = 68

    def __init__(self,
                freecad_document,
                fitting_label,
                rotation = App.Rotation(0,0,0),
                centre = App.Vector(0,0,0)):
        """ Constructs a Side Outlet Tee in the freecad_document, with label attribute
        given by parameter fitting_lable and centre and rotation given by the
        corresponding parameters.
        """
        # Strategy draw all the outside tubes, place them in the correct location and rotation,
        # then cut 48mm diameter solids
        distance_from_centre = Side_Outlet_T.distance_from_centre
        t_across_start = App.Vector( -distance_from_centre,0,0)
        t_across_end = App.Vector(distance_from_centre,0,0)                           
        t_across_line = Draft.make_line(t_across_start,t_across_end)
        t_down_start = App.Vector(0, 0, -distance_from_centre)
        t_down_end = App.Vector(0, 0, 0)
        t_down_line = Draft.make_line(t_down_start,t_down_end)
        through_distance_from_centre = joint_diameter/2
        t_through_start = App.Vector(0, -through_distance_from_centre, 0)
        t_through_end = App.Vector(0, through_distance_from_centre, 0)
        t_through_line = Draft.make_line(t_through_start,t_through_end)
        # Place the lines in the correct locations to take account of rotation and centre.
        # t_across_line.Placement = App.Placement(t_across_line.Placement.Base, rotation, centre)
        # t_down_line.Placement = App.Placement(t_down_line.Placement.Base, rotation, centre)
        # t_through_line.Placement = App.Placement(t_through_line.Placement.Base, rotation, centre)
        #Draw solid sections
        t_across = Arch.makePipe(t_across_line, diameter=joint_diameter)
        t_across.WallThickness = joint_wall_thickness
        t_down_inside = Arch.makePipe(t_down_line, diameter=pole_diameter)
        t_through_inside = Arch.makePipe(t_through_line, diameter=pole_diameter)
        t_across = Draft.cut(t_across, t_through_inside)
        t_across = Draft.cut(t_across, t_down_inside)
        t_across.Label = "T_Across"
        t_down = Arch.makePipe(t_down_line, diameter=joint_diameter)
        t_down.WallThickness = joint_wall_thickness
        t_across_inside = Arch.makePipe(t_across_line, diameter=pole_diameter)
        t_through_inside = Arch.makePipe(t_through_line, diameter=pole_diameter)
        t_down = Draft.cut(t_down, t_across_inside)
        t_down = Draft.cut(t_down, t_through_inside)
        t_down.Label = "T_Down"
        t_through = Arch.makePipe(t_through_line, diameter=joint_diameter)
        t_through.WallThickness = joint_wall_thickness
        t_across_inside = Arch.makePipe(t_across_line, diameter=pole_diameter)
        t_down_inside = Arch.makePipe(t_down_line, diameter=pole_diameter)
        t_through = Draft.cut(t_through, t_across_inside)
        t_through = Draft.cut(t_through, t_down_inside)
        t_through.Label = "T_Through"
        # Rotate solid sections around the orign
        t_across.Placement = App.Placement(App.Vector(0,0,0), rotation, App.Vector(0,0,0))
        t_down_base = t_down.Placement.Base
        t_down.Placement = App.Placement(t_down.Placement.Base, rotation, App.Vector(0,0,0))
        t_through.Placement = App.Placement(App.Vector(0,0,0), rotation, App.Vector(0,0,0))
        # Move objects to defined centre
        Draft.move(t_across, centre)
        Draft.move(t_down, centre)
        Draft.move(t_through, centre)
        # Group sections
        self.fitting = freecad_document.addObject("App::DocumentObjectGroup","Group")
        self.fitting.addObject(t_across)
        self.fitting.addObject(t_down)
        self.fitting.addObject(t_through)
        self.fitting.Label=fitting_label

class Four_Way_Cross:
    """ A class representing a 4 way cross object for standard 48,3 scaffolding
     This is a model of the following fitting:
    https://pipedreamfittings.com/product/4-way-cross-with-central-tube-48mm-d48/ """
    
    distance_from_centre = 68
    through_long_distance = 49.5
    
    def __init__(self,
                freecad_document,
                fitting_label,
                rotation = App.Rotation(0,0,0),
                centre = App.Vector(0,0,0)):
        """ Constructs a 4 Way Cross in the freecad_document, with label attribute
        given by parameter fitting_lable and centre and rotation given by the
        corresponding parameters.  """
        # Strategy draw all the outside tubes, place them in the correct location and rotation,
        # then cut 48mm diameter solids
        distance_from_centre = Four_Way_Cross.distance_from_centre
        through_long_distance = Four_Way_Cross.through_long_distance
        t_across_start = App.Vector( -distance_from_centre,0,0)
        t_across_end = App.Vector(distance_from_centre,0,0)                           
        t_across_line = Draft.make_line(t_across_start,t_across_end)
        t_down_start = App.Vector(0, 0, -distance_from_centre)
        t_down_end = App.Vector(0, 0, distance_from_centre)
        t_down_line = Draft.make_line(t_down_start,t_down_end)
        through_short_distance = joint_diameter/2
        t_through_start = App.Vector(0, -through_long_distance, 0)
        t_through_end = App.Vector(0, through_short_distance, 0)
        t_through_line = Draft.make_line(t_through_start,t_through_end)
        # Place the lines in the correct locations to take account of rotation and centre.
        # t_across_line.Placement = App.Placement(t_across_line.Placement.Base, rotation, centre)
        # t_down_line.Placement = App.Placement(t_down_line.Placement.Base, rotation, centre)
        # t_through_line.Placement = App.Placement(t_through_line.Placement.Base, rotation, centre)
        #Draw solid sections
        t_across = Arch.makePipe(t_across_line, diameter=joint_diameter)
        t_across.WallThickness = joint_wall_thickness
        t_down_inside = Arch.makePipe(t_down_line, diameter=pole_diameter)
        t_through_inside = Arch.makePipe(t_through_line, diameter=pole_diameter)
        t_across = Draft.cut(t_across, t_through_inside)
        t_across = Draft.cut(t_across, t_down_inside)
        t_across.Label = "T_Across"
        t_down = Arch.makePipe(t_down_line, diameter=joint_diameter)
        t_down.WallThickness = joint_wall_thickness
        t_across_inside = Arch.makePipe(t_across_line, diameter=pole_diameter)
        t_through_inside = Arch.makePipe(t_through_line, diameter=pole_diameter)
        t_down = Draft.cut(t_down, t_across_inside)
        t_down = Draft.cut(t_down, t_through_inside)
        t_down.Label = "T_Down"
        t_through = Arch.makePipe(t_through_line, diameter=joint_diameter)
        t_through.WallThickness = joint_wall_thickness
        t_across_inside = Arch.makePipe(t_across_line, diameter=pole_diameter)
        t_down_inside = Arch.makePipe(t_down_line, diameter=pole_diameter)
        t_through = Draft.cut(t_through, t_across_inside)
        t_through = Draft.cut(t_through, t_down_inside)
        t_through.Label = "T_Through"
        # Rotate solid sections around the orign
        t_across.Placement = App.Placement(App.Vector(0,0,0), rotation, App.Vector(0,0,0))
        t_down_base = t_down.Placement.Base
        t_down.Placement = App.Placement(t_down.Placement.Base, rotation, App.Vector(0,0,0))
        t_through.Placement = App.Placement(App.Vector(0,0,0), rotation, App.Vector(0,0,0))
        # Move objects to defined centre
        Draft.move(t_across, centre)
        Draft.move(t_down, centre)
        Draft.move(t_through, centre)
        # Group sections
        self.fitting = freecad_document.addObject("App::DocumentObjectGroup","Group")
        self.fitting.addObject(t_across)
        self.fitting.addObject(t_down)
        self.fitting.addObject(t_through)
        self.fitting.Label=fitting_label