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

# centre position of the simulation screen
CENTRE_X = 428   # 399.215
CENTRE_Y = 400   # 307.1984

def scale_set_default_values(scale):
    scale.set_update_policy(gtk.UPDATE_CONTINUOUS)
    scale.set_digits(1)
    scale.set_value_pos(gtk.POS_TOP)
    scale.set_draw_value(True)


class CircleDimensionWindow:

  def __init__( self, simulator ):

    # preview counter ( from the second selection, the old obstacles have to be replaced with the new)
    self.preview_count = 0

    # cirular obstacle dimensions
    self.x_circle = ''
    self.y_circle = ''
    self.radius_circle = ''

    # bind the simulator
    self.simulator = simulator


    # initialize the window
    self.window_circle_dimension = gtk.Window(gtk.WINDOW_TOPLEVEL)
    self.window_circle_dimension.set_title( "Circular Obstacle Dimension" )
    self.window_circle_dimension.set_resizable(True)

    # == initialize the buttons

    # build the label for obstacle x position
    self.label_obstacle_position_x = gtk.Label( 'X Obstacle Position' )

    # build horizontal scale for obstacle x
    self.hscale_obstacle_position_x = gtk.HScale()
    self.hscale_obstacle_position_x.set_range( 0, 800 )
    self.hscale_obstacle_position_x.set_size_request( 320, 50 )
    self.hscale_obstacle_position_x.set_value( 400 )
    self.hscale_obstacle_position_x.connect( 'value-changed', self.on_hscale_value_change_x )

    # build the entry for obstacle x position
    self.entry_obstacle_position_x = gtk.Entry()
    self.entry_obstacle_position_x.set_text( str(400) )

    # build the label for obstacle y position
    self.label_obstacle_position_y = gtk.Label( 'Y Obstacle Position' )

    # build horizontal scale for obstacle y
    self.hscale_obstacle_position_y = gtk.HScale()
    self.hscale_obstacle_position_y.set_range( 0, 800 )
    self.hscale_obstacle_position_y.set_size_request( 320, 50 )
    self.hscale_obstacle_position_y.set_value( 400 )
    self.hscale_obstacle_position_y.connect( 'value-changed', self.on_hscale_value_change_y )

    # build the entry for obstacle y position
    self.entry_obstacle_position_y = gtk.Entry()
    self.entry_obstacle_position_y.set_text( str(400) )

    # build the label for obstacle radius
    self.label_obstacle_radius = gtk.Label( 'Obstacle Radius' )

    # build horizontal scale for obstacle radius
    self.hscale_obstacle_radius = gtk.HScale()
    self.hscale_obstacle_radius.set_range( 0, 100 )
    self.hscale_obstacle_radius.set_size_request( 320, 50 )
    self.hscale_obstacle_radius.set_value( 400 )
    self.hscale_obstacle_radius.connect( 'value-changed', self.on_hscale_value_change_radius)

    # build the entry for obstacle radius
    self.entry_obstacle_radius = gtk.Entry()
    self.entry_obstacle_radius.set_text( str(50) )

    # build the preview button
    self.button_preview = gtk.Button( 'Preview' )
    self.button_preview.connect( 'clicked', self.on_preview )

    # build the ok cancel buttons
    self.button_ok = gtk.Button( 'OK' )
    self.button_cancel = gtk.Button( 'Cancel' )
    self.button_ok.connect( 'clicked', self.on_ok )
    self.button_cancel.connect( 'clicked', self.on_cancel )

    # build add obstacle button
    self.button_add_obstacle = gtk.Button( 'Add New Obstacle')
    self.button_add_obstacle.connect( 'clicked', self.on_add_obstacle )

    # build remove obstacle button
    self.button_remove_obstacle = gtk.Button( 'Remove Obstacle' )
    self.button_remove_obstacle.connect( 'clicked', self.on_remove_obstcle )

    # == lay out the window
    # pack the obstacle x positon label and entry
    obs_position_box_x = gtk.HBox( spacing = 5 )
    obs_position_box_x.pack_start( self.label_obstacle_position_x, False, False )
    obs_position_box_x.pack_start( self.hscale_obstacle_position_x, False, False )
    obs_position_box_x.pack_start( self.entry_obstacle_position_x, False, False )

    # pack the obstacle y positon label and entry
    obs_position_box_y = gtk.HBox( spacing = 5 )
    obs_position_box_y.pack_start( self.label_obstacle_position_y, False, False )
    obs_position_box_y.pack_start( self.hscale_obstacle_position_y, False, False )
    obs_position_box_y.pack_start( self.entry_obstacle_position_y, False, False )

    # pack the obstacle radius label and entry
    obs_radius_box = gtk.HBox( spacing = 5 )
    obs_radius_box.pack_start( self.label_obstacle_radius, False, False )
    obs_radius_box.pack_start( self.hscale_obstacle_radius, False, False )
    obs_radius_box.pack_start( self.entry_obstacle_radius, False, False )

    # pack the preview ok cancel buttons
    preview_ok_cancel_box = gtk.HBox( spacing = 5)
    preview_ok_cancel_box.pack_start( self.button_add_obstacle, False, False )
    preview_ok_cancel_box.pack_start( self.button_remove_obstacle, False, False )
    preview_ok_cancel_box.pack_start( self.button_preview, False, False )
    preview_ok_cancel_box.pack_start( self.button_ok, False, False )
    preview_ok_cancel_box.pack_start( self.button_cancel, False, False )

    # align the controls
    obs_position_x_alignment = gtk.Alignment( 0.5, 0.0, 0.0, 1.0 )
    obs_position_x_alignment.add( obs_position_box_x )

    obs_position_y_alignment = gtk.Alignment( 0.5, 0.0, 0.0, 1.0 )
    obs_position_y_alignment.add( obs_position_box_y )

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
    layout_box.pack_start( obs_radius_alignment, False, False, 5 )
    layout_box.pack_start( ok_cancel_alignment, False, False, 5 )
    layout_box.pack_start( self.alert_box, False, False, 5 )

    # apply the layout
    self.window_circle_dimension.add( layout_box )

    # show the simulator window
    self.window_circle_dimension.show_all()

    # display alert to select a position
    self.alert_box.set_text( 'To select position - click on the simulator window')


  # EVENT Handlers
  def on_hscale_value_change_x(self, widget):
    val = widget.get_value()
    self.entry_obstacle_position_x.set_text( str(val) )


  def on_hscale_value_change_y(self, widget):
    val = widget.get_value()
    self.entry_obstacle_position_y.set_text( str(val) )


  def on_hscale_value_change_radius(self, widget):
    val = widget.get_value()
    self.entry_obstacle_radius.set_text( str(val) )


  def on_add_obstacle(self, widget):
    self.preview_count = 0
    self.simulator.save_map( 'backup map' )
    self.window_circle_dimension.destroy()


  def on_remove_obstcle(self, widget):
    self.simulator.load_map( 'backup map' )
    self.preview_count = 0

  def on_preview(self, widget):
    print self.preview_count
    if self.preview_count == 0:
        self.update_map()
        self.preview_count += 1
    else:
        self.edit_map()


  def on_ok(self, widget):
    if self.preview_count == 0:
        self.update_map()
    else:
        pass
    self.preview_count == 0
    self.simulator.save_map( 'backup map' )
    self.window_circle_dimension.destroy()


  def on_cancel(self, widget):
    self.simulator.load_map( 'backup map' )
    self.window_circle_dimension.destroy()


  # Other functions
  def set_coordinate_circle(self, x, y):
    self.entry_obstacle_position_x.set_text( x )
    self.entry_obstacle_position_y.set_text( y )


  def compute_local_x_y(self):
    self.radius_circle = self.entry_obstacle_radius.get_text()
    self.x_circle = self.entry_obstacle_position_x.get_text()
    self.y_circle = self.entry_obstacle_position_y.get_text()
    x = float( self.x_circle )
    y = float( self.y_circle )
    radius = float( self.radius_circle )
    self.radius_local = radius * 0.01
    self.x_local = ( x - CENTRE_X ) * 0.01
    self.y_local = ( CENTRE_Y - y ) * 0.01


  def update_map(self):
    self.compute_local_x_y()
    self.simulator.update_map( 'circle', self.radius_local, self.x_local, self.y_local )


  def edit_map(self):
    self.compute_local_x_y()
    self.simulator.edit_map( 'circle', self.radius_local, self.x_local, self.y_local )
