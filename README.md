# Composting Toilet Design

This repository contains a set of python files that are used to generate the components and full designs for scaffolding based composting toilets and urinals. This document contains the following sections 

- Design Goals
- Scaffolding Approach
- Plumbing Approach
- Design Tools

## Design Goals

The design should

- Optimise financial costs for
    - Construction Materials
    - Maintenance
- Optimise volunteer time costs for:
    - Construction
    - Setup
    - Cleaning and Maintenance
    - Strike
- Seperate liquid and solid waste to aid disposal. 
- Ensure that human waste is sealed in order to prevent the spread of gastro intestinal infections.
- Should be able to cope with expected volumes (to be determined) of liquid and solid matter
– TODO More

## Scaffolding Approach

The primary design approach is to construct scaffolding based interchangeable modular side panels that are easily connected together to create either:

- Composting Toilet Cabins
- Urinals

The side panels are constructed once and stored whole to enable easy set up and strike.

## Plumbing Approach

The plan is to store solid waste in wheelie bin containers and liquid waste in IBCs.

For the composting cabin the liquid waste is separated at the toilet. This enables:

- Liquid waste to flow into IBCs using gravity (Assuming collection point is above the top of the IBC).
- Simplified solid waste collection. Where changing the solid waste container only involves moving a wheelie bin and no messing around with plumbing.

## Design Tools

The files contained in this repository primarily deal with the design of the structure. They consist of a set of python files in directory /src/puthon with extension ".py". There two sorts of python files:

- **Macro files** - These are files that are used to generate 3d models in the open source software [FreeCAD](https://www.freecad.org/). To use FreeCAD to generate the models use the Freecad menu Macro > Macros to navigate to the file you wish to use. The freFreeCAD version used for this project is 0.21.2. Currently the following Macro files have been created:

    - macro_fitting_side_outlet_t.py - Draws a simple side outlet t scaffolding joint.
    - macro_fitting-sideoutlet_t_test.py - Tests all rotations of the side outlet and illustrates how they can be connected to scaffolding pipe.
    - TODO create and document extra files
- **Support Files** - 
 
    - parameters.py - contains key parameters upon which the design is based. For example seat_height_from_ground specifies the height in millimeters that the toilet seat needs to above the ground.
    - make_fittings.py - this contains functions used to make 3d models of scaffolding fittings.





