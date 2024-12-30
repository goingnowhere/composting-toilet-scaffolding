# This FreeCAD macro script makes a multiple side outlet T object
# for advanced positioning and rotation testing as well as to
# indicate how these fittings can be used to create larger scaffolding
# based structures.

#  Import the packages that we need - TODO check that all of these are needed
import FreeCAD as App
import FreeCADGui as Gui
import Draft
import Arch

from parameters import *
from fittings import Four_Way_Cross, make_pole

# Set Up Freecad and Select Workbench
App.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")

# Draw a a set of side outlet T object rotated in all directions
# connected by scaffolding poles.
centre_1 = App.Vector(0, 0 ,0)
centre_2 = App.Vector(300, 0, 0)
centre_3 = App.Vector(0, 300 , 0)
centre_4 = App.Vector(300,300, 0)
centre_5 = App.Vector(0, 0 , 300)
centre_6 = App.Vector(300, 0, 300)
centre_7 = App.Vector(0, 300 , 300)
centre_8 = App.Vector(300, 300, 300)
four_way_cross_1 = Four_Way_Cross(freecad_document = document,
                    fitting_label = "Four_Way_Cross_1",
                    centre = centre_1,
                    rotation = App.Rotation(0, 180, 0))
four_way_cross_2 = Four_Way_Cross(freecad_document = document,
                    fitting_label = "Four_Way_Cross_2",
                    centre = centre_2,
                    rotation = App.Rotation(90, 180, 0))
four_way_cross_3 = Four_Way_Cross(freecad_document = document,
                    fitting_label = "Four_Way_Cross_3",
                    centre = centre_3,
                    rotation = App.Rotation(0, 0, 270))
four_way_cross_4 = Four_Way_Cross(freecad_document = document,
                    fitting_label = "Four_Way_Cross_4",
                    centre = centre_4,
                    rotation = App.Rotation(0, 90, 270))
four_way_cross_5 = Four_Way_Cross(freecad_document = document,
                    fitting_label = "Four_Way_Cross_5",
                    centre = centre_5,
                    rotation = App.Rotation(0, 0, 90))
four_way_cross_6 = Four_Way_Cross(freecad_document = document,
                    fitting_label = "Four_Way_Cross_6",
                    centre = centre_6,
                    rotation = App.Rotation(0, 0, 0))
four_way_cross_7 = Four_Way_Cross(freecad_document = document,
                    fitting_label = "Four_Way_Cross_7",
                    centre = centre_7,
                    rotation = App.Rotation(270, 0, 90))
four_way_cross_8 = Four_Way_Cross(freecad_document = document,
                    fitting_label = "Four_Way_Cross_8",
                    centre = centre_8,
                    rotation = App.Rotation(270, 90, 270))

#Offsets for the side outlet t joint
through_short_offset = pole_diameter/2 + joint_wall_thickness
through_long_offset = Four_Way_Cross.through_long_distance
offset = pole_diameter/2
# Make Connection poles.
line_1_2 = Draft.make_line(
    centre_1 + App.Vector(offset, 0, 0),
    centre_2 + App.Vector(through_long_offset, 0, 0))
make_pole(line_1_2, "Pole_1_2")
line_1_3 = Draft.make_line(
    centre_1 + App.Vector(0, -through_long_offset, 0),
    centre_3 + App.Vector(0, -offset, 0))
make_pole(line_1_3, "Pole_1_3")
line_1_5 = Draft.make_line(
    centre_1 + App.Vector(0, 0, offset),
    centre_5 + App.Vector(0, 0, through_short_offset))
make_pole(line_1_5, "Pole_1_5")
line_2_4 = Draft.make_line(
    centre_2 + App.Vector(0, offset, 0),
    centre_4 + App.Vector(0, -offset, 0))
make_pole(line_2_4, "Pole_2_4")
line_2_6 = Draft.make_line(
    centre_2 + App.Vector(0, 0, offset),
    centre_6 + App.Vector(0, 0, -offset))
make_pole(line_2_6, "Pole_2_6")
line_3_4 = Draft.make_line(
    centre_3 + App.Vector(offset, 0, 0),
    centre_4 + App.Vector(through_long_offset, 0, 0))
make_pole(line_3_4, "Pole_3_4")
line_3_7 = Draft.make_line(
    centre_3 + App.Vector(0, 0, -through_short_offset),
    centre_7 + App.Vector(0, 0, through_short_offset))
make_pole(line_3_7, "Pole_3_7")
line_4_8 = Draft.make_line(
    centre_4 + App.Vector(0, 0, offset),
    centre_8 + App.Vector(0, 0, -offset))
make_pole(line_4_8, "Pole_4_8")
line_5_6 = Draft.make_line(
    centre_5 + App.Vector(offset, 0, 0),
    centre_6 + App.Vector(-offset, 0, 0))
make_pole(line_5_6, "Pole_5_6")
line_5_7 = Draft.make_line(
    centre_5 + App.Vector(0, offset, 0),
    centre_7 + App.Vector(0, offset, 0))
make_pole(line_5_7, "Pole_5_7")
line_6_8 = Draft.make_line(
    centre_6 + App.Vector(0, -through_long_offset, 0),
    centre_8 + App.Vector(0, through_short_offset, 0))
make_pole(line_6_8, "Pole_6_8")
line_7_8 = Draft.make_line(
    centre_7 + App.Vector(offset, 0, 0),
    centre_8 + App.Vector(-offset, 0, 0))
make_pole(line_7_8, "Pole_7_8")
