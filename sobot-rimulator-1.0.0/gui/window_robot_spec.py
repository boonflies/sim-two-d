# Boon's simulator - A Robot Programming Tool
# Copyright (C) 2013-2014 David Boon Moses E
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Email boonflies@gmail.com for questions, comments, or to report bugs.


import pygtk
pygtk.require('2.0')
import gtk
import gobject


# user response codes for file chooser dialog buttons
LS_DIALOG_RESPONSE_CANCEL = 1
LS_DIALOG_RESPONSE_ACCEPT = 2

# centre position of the simulation screen
CENTRE_X = 428   # 399.215
CENTRE_Y = 400   # 307.1984

def scale_set_default_values(scale):
    scale.set_update_policy(gtk.UPDATE_CONTINUOUS)
    scale.set_digits(1)
    scale.set_value_pos(gtk.POS_TOP)
    scale.set_draw_value(True)


class WindowRobotSpec:

  def __init__( self, simulator ):

    # bind the simulator
    self.simulator = simulator


    # initialize the window
    self.window_robot_specs = gtk.Window( gtk.WINDOW_TOPLEVEL )
    self.window_robot_specs.set_title( 'Robot Specification' )
    self.window_robot_specs.set_resizable( True )
    self.window_robot_specs.set_border_width( 8 )

    # == initialize the glade window

    builder = gtk.Builder()
    builder.add_from_file("work.glade")

    self.window = builder.get_object("window_robot_spec")

    # == sensor type combo box add entries

    # create a model
    store = gtk.ListStore(gobject.TYPE_STRING)
    store.append (["Proximity Sensor"])

    # assaign model to combobox
    self.combo_sensor_type = builder.get_object("combo_sensor_type")
    self.combo_sensor_type.set_model(store)

    # pack the renderer into it
    cell = gtk.CellRendererText()
    self.combo_sensor_type.pack_start(cell, True)
    self.combo_sensor_type.add_attribute(cell, 'text',0)

    self.window.show_all()

    # Event handlers
    def combo_sensor_type_changed_cb(self, widget):
        tree_iter = widget.get_active_iter()
        if tree_iter != None:
            model = self.combo_sensor_type.get_model()
            #index = self.combobox_obstacle_selection.get_active()
            self.obstacle_type = model[tree_iter][0]
        print self.obstacle_type



