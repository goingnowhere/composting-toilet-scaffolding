# This FreeCAD macro script makes a double fixing pad objects
# for advanced positioning and rotation testing as well as to
# indicate how these fittings can be used to fix boards to scafolding.

#  Import the packages that we need - TODO check that all of these are needed
import FreeCAD as App
import FreeCADGui as Gui
import Draft
import Arch

from parameters import *
from fittings import Double_Fixing_Pad, make_pole

# Set Up Freecad and Select Workbench
App.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")

# Draw a a set of double fixing pad objects rotated in all directions
# connected by scaffolding poles and a panel
panel_sides = 600
centre_1 = App.Vector(200, 0 ,0)
centre_2 = App.Vector(400, 0, 0)
centre_3 = App.Vector(0, 200 , 0)
centre_4 = App.Vector(0, 400 , 0)
centre_5 = App.Vector(panel_sides, 200, 0)
centre_6 = App.Vector(panel_sides, 400, 0)
centre_7 = App.Vector(200, panel_sides , 0)
centre_8 = App.Vector(400, panel_sides, 0)
double_fixing_pad_1 = Double_Fixing_Pad(freecad_document = document,
                    fitting_label = "Double_Fixing_Pad_1",
                    centre = centre_1,
                    rotation = App.Rotation(90, 0, 90))
double_fixing_pad_2 = Double_Fixing_Pad(freecad_document = document,
                    fitting_label = "Double_Fixing_Pad_2",
                    centre = centre_2,
                    rotation = App.Rotation(90, 0, 90))
double_fixing_pad_3 = Double_Fixing_Pad(freecad_document = document,
                    fitting_label = "Double_Fixing_Pad_3",
                    centre = centre_3,
                    rotation = App.Rotation(0, 0, 90))
double_fixing_pad_4 = Double_Fixing_Pad(freecad_document = document,
                    fitting_label = "Double_Fixing_Pad_4",
                    centre = centre_4,
                    rotation = App.Rotation(0, 0, 90))
double_fixing_pad_5 = Double_Fixing_Pad(freecad_document = document,
                    fitting_label = "Double_Fixing_Pad_5",
                    centre = centre_5,
                    rotation = App.Rotation(0, 0, 90))
double_fixing_pad_6 = Double_Fixing_Pad(freecad_document = document,
                    fitting_label = "Double_Fixing_Pad_6",
                    centre = centre_6,
                    rotation = App.Rotation(0, 0, 90))
double_fixing_pad_7 = Double_Fixing_Pad(freecad_document = document,
                    fitting_label = "Double_Fixing_Pad_7",
                    centre = centre_7,
                    rotation = App.Rotation(90, 0, 90))
double_fixing_pad_8 = Double_Fixing_Pad(freecad_document = document,
                    fitting_label = "Double_Fixing_Pad_8",
                    centre = centre_8,
                    rotation = App.Rotation(90, 0, 90))

# Offsets for double fixing pad
offset = Double_Fixing_Pad.length
# Make Connection poles.
line_1_2 = Draft.make_line(
    centre_1 + App.Vector(0, 0, 0),
    centre_2 + App.Vector(offset, 0, 0))
make_pole(line_1_2, "Pole_1_2")
line_3_4 = Draft.make_line(
    centre_3 + App.Vector(0, -offset, 0),
    centre_4 + App.Vector(0, 0, 0))
make_pole(line_3_4, "Pole_3_4")
line_5_6 = Draft.make_line(
    centre_5 + App.Vector(0, -offset, 0),
    centre_6 + App.Vector(0, 0, 0))
make_pole(line_5_6, "Pole_5_6")
line_7_8 = Draft.make_line(
    centre_7 + App.Vector(0, 0, 0),
    centre_8 + App.Vector(offset, 0, 0))
make_pole(line_7_8, "Pole_7_8")

# Add Panel
rect = Draft.makeRectangle(panel_sides, panel_sides)
panel = Arch.makePanel(rect, thickness = 18)
Draft.move(panel, App.Vector(0, 0, pole_diameter/2 + joint_wall_thickness))
