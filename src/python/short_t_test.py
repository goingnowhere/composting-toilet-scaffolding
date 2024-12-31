# This FreeCAD script tests double sided script objects
# for advanced positioning and rotation testing as well as to
# indicate how these fittings can be used to fix boards to scafolding.

#  Import the packages that we need - TODO check that all of these are needed
import FreeCAD as App
import FreeCADGui as Gui
import Draft
import Arch

from parameters import *
from fittings import make_pole
from fittings import Short_T

# Set Up Freecad and Select Workbench
App.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")

# Draw a a set of double fixing pad objects rotated in all directions
# connected by scaffolding poles and a panel
joint_distance= 600
centre_1 = App.Vector(0, 0 ,0)
centre_2 = App.Vector(0, 0, joint_distance)
centre_3 = App.Vector(joint_distance, 0 , 0)
centre_4 = App.Vector(joint_distance, joint_distance , 0)
centre_5 = App.Vector(joint_distance, joint_distance, -joint_distance)
centre_6 = App.Vector(joint_distance, 0, -joint_distance)

short_t_1 = Short_T(freecad_document = document,
                    fitting_label = "Short_T_1",
                    centre = centre_1,
                    rotation = App.Rotation(0, 0, 180))

short_t_2 = Short_T(freecad_document = document,
                    fitting_label = "Short_T_2",
                    centre = centre_2,
                    rotation = App.Rotation(0, 270, 0))

short_t_3 = Short_T(freecad_document = document,
                    fitting_label = "Short_T_3",
                    centre = centre_3,
                    rotation = App.Rotation(0, 0, 90))

short_t_4 = Short_T(freecad_document = document,
                    fitting_label = "Short_T_4",
                    centre = centre_4,
                    rotation = App.Rotation(90, 0, 0))

short_t_5 = Short_T(freecad_document = document,
                    fitting_label = "Short_T_5",
                    centre = centre_5,
                    rotation = App.Rotation(0, 90, 270))

short_t_6 = Short_T(freecad_document = document,
                    fitting_label = "Short_T_6",
                    centre = centre_6,
                    rotation = App.Rotation(90, 0, 90))

# Offsets for double fixing pad
across_offset = joint_diameter / 2
down_offset = pole_diameter / 2

# Make Connection poles.
line_1_2 = Draft.make_line(
    centre_1 + App.Vector(0, 0, down_offset),
    centre_2 + App.Vector(0, 0, across_offset))
make_pole(line_1_2, "Pole_1_2")
line_1_3 = Draft.make_line(
    centre_1 + App.Vector(-across_offset, 0, 0),
    centre_3 + App.Vector(across_offset, 0, 0))
make_pole(line_1_3, "Pole_1_3")
line_3_4 = Draft.make_line(
    centre_3 + App.Vector(0, down_offset, 0),
    centre_4 + App.Vector(0, across_offset, 0))
make_pole(line_3_4, "Pole_3_4")
line_4_5 = Draft.make_line(
    centre_4 + App.Vector(0, 0, down_offset),
    centre_5 + App.Vector(0, 0, across_offset))
make_pole(line_4_5, "Pole_4_5")
line_5_6 = Draft.make_line(
    centre_5 + App.Vector(0, down_offset, 0),
    centre_6 + App.Vector(0, across_offset, 0))
make_pole(line_5_6, "Pole_5_6")

