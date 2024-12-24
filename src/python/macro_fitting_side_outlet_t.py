# This FreeCAD macro script makes a single side outlet T object
# for basic testing illustration purposes

#  Import the packages that we need - TODO check that all of these are needed
import FreeCAD
import FreeCADGui as Gui


from make_fittings import Side_Outlet_T

# Set Up Freecad and Select Workbench
FreeCAD.Console.PrintMessage("Starting FreeCAD generation.\n")
doc_name = "Fittings"
document = App.newDocument(doc_name)
Gui.activeDocument().activeView().viewDefaultOrientation()
Gui.runCommand('Std_OrthographicCamera',1)
Gui.activateWorkbench("BIMWorkbench21")

# Draw a simple side outlet T object
side_outlet_t_1 = Side_Outlet_T(freecad_document = document,
                               fitting_label = "Side_Outlet_T_1")