# This file contains all the classes used for making
# fittings used to connect scaffolding pipes.

#  Import the packages that we need
import FreeCAD as App
import Arch
import Draft
from BasicShapes import Shapes
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


class Double_Fixing_Pad:
    """ A class representing a Double Fixing Pad object for standard 48,3 scaffolding
     This is a model of the following fitting:
    https://pipedreamfittings.com/product/double-fixing-pad-48mm-d48/ """
    
    length = 35
    width = 140
    
    def __init__(self,
                freecad_document,
                fitting_label,
                rotation = App.Rotation(0,0,0),
                centre = App.Vector(0,0,0)):
        """ Constructs a Double Fixing Pad in the freecad_document, with label attribute
        given by parameter fitting_lable and centre and rotation given by the
        corresponding parameters.  """
        # Make the tube
        tube = Shapes.addTube(freecad_document, "Tube")
        pole_radius = pole_diameter / 2
        tube.InnerRadius = pole_radius
        tube.OuterRadius = pole_radius + joint_wall_thickness
        tube.Height = Double_Fixing_Pad.length
        # Make the pad
        box = freecad_document.addObject("Part::Box", "Double Pad")
        box.Length = Double_Fixing_Pad.width
        box.Width = joint_wall_thickness
        box.Height = Double_Fixing_Pad.length
        box.Placement = App.Placement(
                    App.Vector(-box.Length / 2 , 
                               pole_radius,
                               0),
                    App.Rotation(0, 0, 0))
        # Create a compond of the two objects
        fitting = freecad_document.addObject("Part::Compound", fitting_label)
        fitting.Links = [tube, box]
        # Rotate
        fitting.Placement = App.Placement(App.Vector(0,0,0), rotation, App.Vector(0,0,0))
        # Move
        Draft.move(fitting, centre)


class Double_Sided_Collar:
    """ A class representing a Double Sided Collar object for standard 48,3 scaffolding
     This is a model of the following fitting:
    https://pipedreamfittings.com/product/double-sided-collar-plate-90-48mm-d48-2/ """
    
    length = 35
    width = 70
    
    def __init__(self,
                freecad_document,
                fitting_label,
                rotation = App.Rotation(0,0,0),
                centre = App.Vector(0,0,0)):
        """ Constructs a Double Sided Collar in the freecad_document, with label attribute
        given by parameter fitting_lable and centre and rotation given by the
        corresponding parameters.  """
        # Make the tube
        tube = Shapes.addTube(freecad_document, "Tube")
        pole_radius = pole_diameter / 2
        tube.InnerRadius = pole_radius
        tube.OuterRadius = pole_radius + joint_wall_thickness
        tube.Height = Double_Sided_Collar.length
        # Make the pads
        box_1 = freecad_document.addObject("Part::Box", "Collar_Pad_1")
        box_1.Length = Double_Sided_Collar.width
        box_1.Width = joint_wall_thickness
        box_1.Height = Double_Sided_Collar.length
        box_1.Placement = App.Placement(
                    App.Vector(0 , 
                               pole_radius,
                               0),
                    App.Rotation(0, 0, 0))
        box_2 = freecad_document.addObject("Part::Box", "Collar_Pad_2")
        box_2.Length = joint_wall_thickness
        box_2.Width = Double_Sided_Collar.width
        box_2.Height = Double_Sided_Collar.length
        box_2.Placement = App.Placement(
                    App.Vector(-(pole_radius + joint_wall_thickness) , 
                               - Double_Sided_Collar.width,
                               0),
                    App.Rotation(0, 0, 0))
        # Create a compond of the three objects
        fitting = freecad_document.addObject("Part::Compound", fitting_label)
        fitting.Links = [tube, box_1, box_2]
        # Rotate
        fitting.Placement = App.Placement(App.Vector(0,0,0), rotation, App.Vector(0,0,0))
        # Move
        Draft.move(fitting, centre)

class Single_Male_Swivel:
    """ A class representing a Signle Male Swivel object for standard 48,3 scaffolding
     This is a model of the following fitting:
    https://pipedreamfittings.com/product/single-male-swivel-48mm-d48/ """
    
    length = 44.5
    distance_to_hole = 53
    pad_width = distance_to_hole - pole_diameter / 2 + length / 2
    
    def __init__(self,
                freecad_document,
                fitting_label,
                rotation = App.Rotation(0,0,0),
                centre = App.Vector(0,0,0)):
        """ Constructs a Single Male Swivel in the freecad_document, with label attribute
        given by parameter fitting_lable and centre and rotation given by the
        corresponding parameters.  """
        # Make the tube
        tube = Shapes.addTube(freecad_document, "Tube")
        pole_radius = pole_diameter / 2
        tube.InnerRadius = pole_radius
        tube.OuterRadius = pole_radius + joint_wall_thickness
        tube.Height = Single_Male_Swivel.length
        # Make the pads
        box_1 = freecad_document.addObject("Part::Box", "Swivel_Pad_1")
        box_1.Length = Single_Male_Swivel.pad_width
        box_1.Width = joint_wall_thickness
        box_1.Height = Single_Male_Swivel.length
        box_1.Placement = App.Placement(
                    App.Vector(pole_radius , 
                               - box_1.Width / 2,
                               0),
                    App.Rotation(0, 0, 0))
        # Create a compond of the two objects
        fitting = freecad_document.addObject("Part::Compound", fitting_label)
        fitting.Links = [tube, box_1]
        # Rotate
        fitting.Placement = App.Placement(App.Vector(0,0,0), rotation, App.Vector(0,0,0))
        # Move
        Draft.move(fitting, centre)



class Double_Male_Swivel:
    """ A class representing a Signle Male Swivel object for standard 48,3 scaffolding
     This is a model of the following fitting:
    https://pipedreamfittings.com/product/double-male-swivel-48mm-d48// """
    
    length = 44.5
    distance_to_hole = 53
    pad_width = distance_to_hole - pole_diameter / 2 + length / 2
    
    def __init__(self,
                freecad_document,
                fitting_label,
                rotation = App.Rotation(0,0,0),
                centre = App.Vector(0,0,0)):
        """ Constructs a Double Male Swivel in the freecad_document, with label attribute
        given by parameter fitting_lable and centre and rotation given by the
        corresponding parameters.  """
        # Make the tube
        tube = Shapes.addTube(freecad_document, "Tube")
        pole_radius = pole_diameter / 2
        tube.InnerRadius = pole_radius
        tube.OuterRadius = pole_radius + joint_wall_thickness
        tube.Height = Double_Male_Swivel.length
        # Make the pads
        box_1 = freecad_document.addObject("Part::Box", "Swivel_Pad_1")
        box_1.Length = Double_Male_Swivel.pad_width
        box_1.Width = joint_wall_thickness
        box_1.Height = Double_Male_Swivel.length
        box_1.Placement = App.Placement(
                    App.Vector(pole_radius , 
                               - box_1.Width / 2,
                               0),
                    App.Rotation(0, 0, 0))
        box_2 = freecad_document.addObject("Part::Box", "Swivel_Pad_2")
        box_2.Length = Double_Male_Swivel.pad_width
        box_2.Width = joint_wall_thickness
        box_2.Height = Double_Male_Swivel.length
        box_2.Placement = App.Placement(
                    App.Vector(-(pole_radius + Double_Male_Swivel.pad_width) , 
                               - box_2.Width / 2,
                               0),
                    App.Rotation(0, 0, 0))
        # Create a compond of the three objects
        fitting = freecad_document.addObject("Part::Compound", fitting_label)
        fitting.Links = [tube, box_1, box_2]
        # Rotate
        fitting.Placement = App.Placement(App.Vector(0,0,0), rotation, App.Vector(0,0,0))
        # Move
        Draft.move(fitting, centre)
