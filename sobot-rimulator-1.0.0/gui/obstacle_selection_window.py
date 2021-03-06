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

from circle_dimension_window import *

# user response codes for file chooser dialog buttons
LS_DIALOG_RESPONSE_CANCEL = 1
LS_DIALOG_RESPONSE_ACCEPT = 2

class ObstacleSelectionWindow:

  def __init__( self, simulator ):

    # obstacle position
    self.x_obstacle = ''
    self.y_obstacle = ''

    # bind the simulator
    self.simulator = simulator

    # initialize the window
    self.window_draw_obstacle = gtk.Window(gtk.WINDOW_TOPLEVEL)
    self.window_draw_obstacle.set_title( "Obstacle Property Selection" )
    self.window_draw_obstacle.set_resizable(True)

    # == initialize the buttons

    # build the label for obstacle selection combobox
    self.label_obstacle_selection = gtk.Label( 'Obstacle type' )

    # build the obstacle selection combobox
    self.combobox_obstacle_selection = gtk.combo_box_new_text()
    self.combobox_obstacle_selection.append_text('Rectangle')
    self.combobox_obstacle_selection.append_text('Circle')
    self.text = self.combobox_obstacle_selection.get_active_text()
    self.combobox_obstacle_selection.connect('changed', self.on_change_cb)

    # build the dimension done buttons
    self.button_previous_map = gtk.Button( 'Previous Map' )
    self.button_previous_map.connect( 'clicked', self.on_previous_map )
    self.button_dimension = gtk.Button( 'DIMENSION' )
    self.button_done = gtk.Button( 'DONE' )
    self.button_dimension.connect('clicked', self.on_dimension)
    self.button_done.connect('clicked', self.on_done)


    # == lay out the window

    # pack the obstacle selection buttons
    obs_selection_box = gtk.HBox( spacing = 5 )
    obs_selection_box.pack_start( self.label_obstacle_selection )
    obs_selection_box.pack_start( self.combobox_obstacle_selection, False, False )

    # pack the ok cancel buttons
    ok_cancel_box = gtk.HBox( spacing = 5)
    ok_cancel_box.pack_start( self.button_previous_map, False, False)
    ok_cancel_box.pack_start( self.button_dimension, False, False)
    ok_cancel_box.pack_start( self.button_done, False, False)

    # align the controls
    obs_selection_alignment = gtk.Alignment( 0.5, 0.0, 0.0, 1.0 )
    obs_selection_alignment.add( obs_selection_box )

    ok_cancel_alignment = gtk.Alignment( 0.5, 0.0, 0.0, 1.0 )
    ok_cancel_alignment.add( ok_cancel_box )

    # create the alert box
    self.alert_box = gtk.Label()

    # lay out the obstacle selection window and all of the controls
    layout_box = gtk.VBox()
    layout_box.pack_start( obs_selection_alignment, False, False, 5 )
    layout_box.pack_start( ok_cancel_alignment, False, False, 5 )
    layout_box.pack_start( self.alert_box, False, False, 5 )


    # apply the layout
    self.window_draw_obstacle.add( layout_box )

    # show the simulator window
    self.window_draw_obstacle.show_all()

    # display alert to select a position
    self.alert_box.set_text( 'Select an obstacle shape from the Drop Down list' )


  def on_change_cb(self, widget):
    tree_iter = widget.get_active_iter()
    if tree_iter != None:
        model = self.combobox_obstacle_selection.get_model()
        #index = self.combobox_obstacle_selection.get_active()
        self.obstacle_type = model[tree_iter][0]
    print self.obstacle_type
    self.alert_box.set_text( 'Define dimension of obstacle - click DIMENSION button')


  def on_previous_map(self, widget):
    self.simulator.load_map( 'current map' )


  def on_dimension(self, widget):
    self.simulator.save_map( 'backup map' )
    self.window_circle_dimension = CircleDimensionWindow( self.simulator )


  def on_done(self, widget):
    self.window_draw_obstacle.destroy()


  def set_coordinate( self, x, y):
    self.x_obstacle = x
    self.y_obstacle = y
    self.window_circle_dimension.set_coordinate_circle( self.x_obstacle, self.y_obstacle )