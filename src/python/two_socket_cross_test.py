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
from fittings import Two_Socket_Cross

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
centre_3 = App.Vector(0, 0, -joint_distance)

two_socket_cross_1 = Two_Socket_Cross(freecad_document = document,
                    fitting_label = "Two_Socket_Cross_1",
                    centre = centre_1,
                    rotation = App.Rotation(0, 0, 0))

two_socket_cross_2 = Two_Socket_Cross(freecad_document = document,
                    fitting_label = "Two_Socket_Cross_2",
                    centre = centre_2,
                    rotation = App.Rotation(0, 90, 0))

two_socket_cross_3 = Two_Socket_Cross(freecad_document = document,
                    fitting_label = "Two_Socket_Cross_3",
                    centre = centre_3,
                    rotation = App.Rotation(0, 90, 90))

# Offsets for double fixing pad
pole_length = joint_distance * 3 /2

# Make Connection poles.
line_1 = Draft.make_line(
    centre_1 + App.Vector(-pole_length / 2, 0),
    centre_1 + App.Vector(pole_length / 2, 0))
make_pole(line_1, "Pole_1")
line_2 = Draft.make_line(
    centre_1 + App.Vector(0, 0, pole_radius),
    centre_1 + App.Vector(0, 0, pole_length + pole_radius))
make_pole(line_2, "Pole_2")
line_3 = Draft.make_line(
    centre_1 + App.Vector(0, 0, -(pole_length + pole_radius)),
    centre_1 + App.Vector(0, 0, -pole_radius))
make_pole(line_3, "Pole_3")
line_4 = Draft.make_line(
    centre_2 + App.Vector(pole_radius, 0, 0),
    centre_2 + App.Vector(pole_length + pole_radius, 0, 0))
make_pole(line_4, "Pole_4")
line_5 = Draft.make_line(
    centre_3 + App.Vector(0, pole_radius, 0),
    centre_3 + App.Vector(0, pole_length + pole_radius, 0))
make_pole(line_5, "Pole_5")

