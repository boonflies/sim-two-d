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

from frame import *

# user response codes for file chooser dialog buttons
LS_DIALOG_RESPONSE_CANCEL = 1
LS_DIALOG_RESPONSE_ACCEPT = 2

class ObstacleSelectionWindow:

  def __init__( self ):

    # initialize frame
    self.current_frame = Frame()

    # initialize the window
    self.window_draw_obstacle = gtk.Window(gtk.WINDOW_TOPLEVEL)
    self.window_draw_obstacle.set_title( "Obstacle Property Selection" )
    self.window_draw_obstacle.set_resizable(True)

    # == initialize the buttons

    # build the obstacle type selection static text


    # build the obstacle selection combobox
    self.combobox_obstacle_selection = gtk.combo_box_new_text()
    self.combobox_obstacle_selection.append_text('Rectangle')
    self.combobox_obstacle_selection.append_text('Circle')
    self.text = self.combobox_obstacle_selection.get_active_text()
    self.combobox_obstacle_selection.connect('changed', self.on_change_cb)


    # build the ok cancel buttons
    self.button_ok = gtk.Button('OK')
    self.button_cancel = gtk.Button('Cancel')
    self.button_ok.connect('clicked', self.on_ok)
    self.button_cancel.connect('clicked', self.on_cancel)


    # == lay out the window

    # pack the obstacle selection buttons
    obs_selection_box = gtk.HBox( spacing = 5 )
    obs_selection_box.pack_start( )
    obs_selection_box.pack_start( self.combobox_obstacle_selection, False, False )

    # pack the ok cancel buttons
    ok_cancel_box = gtk.HBox( spacing = 5)
    ok_cancel_box.pack_start( self.button_ok, False, False)
    ok_cancel_box.pack_start( self.button_cancel, False, False)

    # align the controls
    obs_selection_alignment = gtk.Alignment( 0.5, 0.0, 0.0, 1.0 )
    obs_selection_alignment.add( obs_selection_box )

    ok_cancel_alignment = gtk.Alignment( 0.5, 0.0, 0.0, 1.0 )
    ok_cancel_alignment.add( ok_cancel_box )

    # create the alert box
    self.alert_box = gtk.Label()

    # lay out the simulation view and all of the controls
    layout_box = gtk.VBox()
    layout_box.pack_start( obs_selection_alignment, False, False, 5 )
    layout_box.pack_start( ok_cancel_alignment, False, False, 5 )
    layout_box.pack_start( self.alert_box, False, False, 5 )


    # apply the layout
    self.window_draw_obstacle.add( layout_box )

    # show the simulator window
    self.window_draw_obstacle.show_all()


  def on_change_cb(self, widget):
    model = self.combobox_obstacle_selection.get_model()
    index = self.combobox_obstacle_selection.get_active()
    print model, index

  def on_ok(self, widget):
    pass

  def on_cancel(self, widget):
    pass