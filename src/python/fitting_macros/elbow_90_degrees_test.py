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
from fittings import Elbow_90_Degrees



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
centre_2 = App.Vector(joint_distance, 0, 0)
centre_3 = App.Vector(joint_distance, joint_distance, 0)

elbow_90_degrees_1 = Elbow_90_Degrees(freecad_document = document,
                    fitting_label = "Elbow_90_Degrees_1",
                    centre = centre_1,
                    rotation = App.Rotation(0, 0, 0))

elbow_90_degrees_2 = Elbow_90_Degrees(freecad_document = document,
                    fitting_label = "Elbow_90_Degrees_2",
                    centre = centre_2,
                    rotation = App.Rotation(90, 0, 90))

elbow_90_degrees_3 = Elbow_90_Degrees(freecad_document = document,
                    fitting_label = "Elbow_90_Degrees_3",
                    centre = centre_3,
                    rotation = App.Rotation(270, 0, 90))


# Make Connection poles.
line_1 = Draft.make_line(
    centre_1 + App.Vector(pole_radius, 0, 0),
    centre_2 + App.Vector(- pole_radius, 0, 0))
make_pole(line_1, "Pole_1")
line_2 = Draft.make_line(
    centre_2 + App.Vector(0, pole_radius, 0),
    centre_3 + App.Vector(0, - pole_radius, 0))
make_pole(line_2, "Pole_2")


