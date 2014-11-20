dt = self.dt

# step all the robots
for robot in self.robots:
  # step robot motion
  robot.step_motion( dt )
##    def step_motion( self, dt ):
##        v_l = self.left_wheel_drive_rate
##        v_r = self.right_wheel_drive_rate
##
##        # apply the robot dynamics to moving parts
##        self.dynamics.apply_dynamics( v_l, v_r, dt,
##                                      self.pose, self.wheel_encoders )
##
##        # update global geometry
##        self.global_geometry = self.geometry.get_transformation_to_pose( self.pose )
##
##        # update all of the sensors
##        for ir_sensor in self.ir_sensors:
##          ir_sensor.update_position()

# apply physics interactions
self.physics.apply_physics()
##    def apply_physics( self ):
##        self._detect_collisions()
##        self._update_proximity_sensors()

# NOTE: the supervisors must run last to ensure they are observing the "current" world
# step all of the supervisors
for supervisor in self.supervisors:
  supervisor.step( dt )
##   def step( self, dt ):
##        # increment the internal clock time
##        self.time += dt
##
##        # NOTE: for simplicity, we assume that the onboard computer executes exactly one control loop for every simulation time increment
##        # although technically this is not likely to be realistic, it is a good simplificiation
##
##        # execute one full control loop
##        self.execute()

# increment world time
self.world_time += dt