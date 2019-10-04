##########
To Do List
##########

List of tasks to perform:

* (done) change generanoms so it accepts a format

  Now it allows just to specify the number of names

  It always generates "name surnames"

  I'd like to generate also "surnames, name"

  Proposed format:

  $ generatenames.py -f name_space_surnames     # current one
  $ generatenames.py -f surname_comma_name
  $ generatenames.py -n 5                       # currently the only arg

* make it more robust

* consider programming it as a generator so it can be used directly from a program

* add gneranoms.py commandline options to specify attributes like accepting one surname only

* consider doc translation to English
