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

class CircleDimensionWindow:

  def __init__( self ):

    self.x_circle = ''
    self.y_circle = ''

  def create_circle_dimension_window( self ):

    # initialize the window
    self.window_circle_dimension = gtk.Window(gtk.WINDOW_TOPLEVEL)
    self.window_circle_dimension.set_title( "Circular Obstacle Dimension" )
    self.window_circle_dimension.set_resizable(True)

    # == initialize the buttons

    # build the label for obstacle x position
    self.label_obstacle_position_x = gtk.Label( 'X Obstacle Position' )

    # build the entry for obstacle x position
    self.entry_obstacle_position_x = gtk.Entry()

    # build position update button
    self.button_position_update = gtk.Button( 'Click to Update X, Y position' )
    self.button_position_update.connect( 'clicked', self.on_update )

    # build the label for obstacle y position
    self.label_obstacle_position_y = gtk.Label( 'Y Obstacle Position' )

    # build the entry for obstacle y position
    self.entry_obstacle_position_y = gtk.Entry()

    # build the label for obstacle radius
    self.label_obstacle_radius = gtk.Label( 'Obstacle Radius' )

    # build the entry for obstacle radius
    self.entry_obstacle_radius = gtk.Entry()

    # build the preview button
    self.button_preview = gtk.Button( 'Preview' )
    self.button_preview.connect( 'clicked', self.on_preview )

    # build the ok cancel buttons
    self.button_ok = gtk.Button('OK')
    self.button_cancel = gtk.Button('Cancel')
    self.button_ok.connect('clicked', self.on_ok)
    self.button_cancel.connect('clicked', self.on_cancel)


    # == lay out the window
    # pack the obstacle x positon label and entry
    obs_position_box_x = gtk.HBox( spacing = 5 )
    obs_position_box_x.pack_start( self.label_obstacle_position_x, False, False )
    obs_position_box_x.pack_start( self.entry_obstacle_position_x, False, False )

    # pack the obstacle y positon label and entry
    obs_position_box_y = gtk.HBox( spacing = 5 )
    obs_position_box_y.pack_start( self.label_obstacle_position_y, False, False )
    obs_position_box_y.pack_start( self.entry_obstacle_position_y, False, False )

    # pack the update x and y position button
    obs_position_update_box = gtk.HBox( spacing = 5 )
    obs_position_update_box.pack_start( self.button_position_update, False, False )

    # pack the obstacle radius label and entry
    obs_radius_box = gtk.HBox( spacing = 5 )
    obs_radius_box.pack_start( self.label_obstacle_radius, False, False )
    obs_radius_box.pack_start( self.entry_obstacle_radius, False, False )

    # pack the preview ok cancel buttons
    preview_ok_cancel_box = gtk.HBox( spacing = 5)
    preview_ok_cancel_box.pack_start( self.button_preview, False, False )
    preview_ok_cancel_box.pack_start( self.button_ok, False, False )
    preview_ok_cancel_box.pack_start( self.button_cancel, False, False )

    # align the controls
    obs_position_x_alignment = gtk.Alignment( 0.5, 0.0, 0.0, 1.0 )
    obs_position_x_alignment.add( obs_position_box_x )

    obs_position_y_alignment = gtk.Alignment( 0.5, 0.0, 0.0, 1.0 )
    obs_position_y_alignment.add( obs_position_box_y )

    obs_position_update_alignment = gtk.Alignment( 0.5, 0.0, 0.0, 1.0 )
    obs_position_update_alignment.add( obs_position_update_box )

    obs_radius_alignment = gtk.Alignment( 0.5, 0.0, 0.0, 1.0)
    obs_radius_alignment.add( obs_radius_box )

    ok_cancel_alignment = gtk.Alignment( 0.5, 0.0, 0.0, 1.0 )
    ok_cancel_alignment.add( preview_ok_cancel_box )

    # create the alert box
    self.alert_box = gtk.Label()

    # lay out the obstacle selection window and all of the controls
    layout_box = gtk.VBox()
    layout_box.pack_start( obs_position_x_alignment, False, False, 5 )
    layout_box.pack_start( obs_position_y_alignment, False, False, 5 )
    layout_box.pack_start( obs_position_update_alignment, False, False, 5 )
    layout_box.pack_start( obs_radius_alignment, False, False, 5 )
    layout_box.pack_start( ok_cancel_alignment, False, False, 5 )
    layout_box.pack_start( self.alert_box, False, False, 5 )


    # apply the layout
    self.window_circle_dimension.add( layout_box )

    # show the simulator window
    self.window_circle_dimension.show_all()

    # display alert to select a position
    self.alert_box.set_text( 'To select position - click on the simulator window')

  def on_ok(self, widget):
    pass


  def on_cancel(self, widget):
    self.window_circle_dimension.destroy()

  def on_update(self, widget):
    self.entry_obstacle_position_x.set_text( self.x_circle )
    self.entry_obstacle_position_y.set_text( self.y_circle )


  def on_preview(self, widget):
    pass

  def set_coordinate_circle(self, x, y):
    self.x_circle = x
    self.y_circle = y