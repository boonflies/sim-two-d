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

# user response codes for file chooser dialog buttons
LS_DIALOG_RESPONSE_CANCEL = 1
LS_DIALOG_RESPONSE_ACCEPT = 2

class ObstacleSelectionWindow:

  def __init__( self ):
    self.window_draw_obstacle = gtk.Window(gtk.WINDOW_TOPLEVEL)

    # Initialize the buttons
    self.combobox = gtk.combo_box_new_text()
    self.combobox.append_text('Rectangle')
    self.combobox.append_text('Circle')
    self.text = self.combobox.get_active_text()
    self.combobox.connect('changed', self.on_change_cb)


    self.window_draw_obstacle.add( self.combobox )
    #self.combobox.set_active(0)

    # == lay out the window

    # pack the simulation control buttons
    sim_controls_box = gtk.HBox( spacing = 5 )

##    sim_controls_box.pack_start( self.combobox, False, False )
##    sim_controls_box.pack_start( self.button_stop, False, False )
##    sim_controls_box.pack_start( self.button_step, False, False )
##    sim_controls_box.pack_start( self.button_reset, False, False )

##    # pack the map control buttons
##    map_controls_box = gtk.HBox( spacing = 5 )
##    map_controls_box.pack_start( self.button_draw_obstacle, False, False)
##    map_controls_box.pack_start( self.button_save_map, False, False )
##    map_controls_box.pack_start( self.button_load_map, False, False )
##    map_controls_box.pack_start( self.button_random_map, False, False )
##
##    # pack the invisibles button
##    invisibles_button_box = gtk.HBox()
##    invisibles_button_box.pack_start( self.button_draw_invisibles, False, False )
##
    # align the controls
    sim_controls_alignment = gtk.Alignment( 0.5, 0.0, 0.0, 1.0 )
##    map_controls_alignment = gtk.Alignment( 0.5, 0.0, 0.0, 1.0 )
##    invisibles_button_alignment = gtk.Alignment( 0.5, 0.0, 0.0, 1.0 )
##    sim_controls_alignment.add( sim_controls_box )
##    map_controls_alignment.add( map_controls_box )
##    invisibles_button_alignment.add( invisibles_button_box )
##
    # create the alert box
    self.alert_box = gtk.Label()

    # lay out the simulation view and all of the controls
    layout_box = gtk.VBox()
##    layout_box.pack_start( self.drawing_area )
##    layout_box.pack_start( self.alert_box, False, False, 5 )
    layout_box.pack_start( sim_controls_alignment, False, False, 5 )
##    layout_box.pack_start( map_controls_alignment, False, False, 5 )
##    layout_box.pack_start( invisibles_button_alignment, False, False, 5 )

    # apply the layout
##    self.window_draw_obstacle.add( layout_box )

    # show the simulator window
    self.window_draw_obstacle.show_all()



  def on_change_cb(self, widget):
    model = self.combobox.get_model()
    index = self.combobox.get_active()
    print model, index