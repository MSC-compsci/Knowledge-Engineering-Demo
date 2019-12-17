# AReA: Advising Residential Areas

## Introduction

This project serves as a codebase for the demo presented as a part of the course Knowledge Engineering @ VU, Amsterdam.
It is a knowledge-based system that using a real-estate DB and under the preferences of the user, 
suggests a residential area tailored to personal needs.

## How is the project organised

The program at hand has two main operations:
1. receives the user's input
2. quiries the dataset and presents the proposed list of areas

`menu.py` is the start of the control flow. It spawns a CLI and based on the user's input (Add a property or get suggestions) calls the corresponding function. 
Desired Property is a concept defined in our domain schema representing from Points of interest to safety levels. All such types of properties are organised as distinct modules.

`quieries.py` is the module responsible for searching into the dataset and based on the user's input presents the suggestion list of the system.

## How to use
This project is developed in python 3.7.
To use this project, you must have python and pip (package manager of python) installed on your machine.
Every library you need for this project can be installed via the following command:
`pip install -r requirements.txt`