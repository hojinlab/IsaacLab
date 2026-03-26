# Copyright (c) 2022-2026, The Isaac Lab Project Developers (https://github.com/isaac-sim/IsaacLab/blob/main/CONTRIBUTORS.md).
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Configuration for TurtleBot3 robots.

The following configurations are available:

* :obj:`TURTLEBOT3_WAFFLE_PI_CFG`: TurtleBot3 Waffle Pi differential drive robot

Reference: https://github.com/ROBOTIS-GIT/turtlebot3
"""

import os

import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg
from isaaclab.assets.articulation import ArticulationCfg

##
# Paths
##

_TURTLEBOT3_DESCRIPTION_DIR = os.path.join(os.path.dirname(__file__), "turtlebot3_description")
"""Path to the TurtleBot3 description directory."""

##
# Configuration
##

TURTLEBOT3_WAFFLE_PI_CFG = ArticulationCfg(
    spawn=sim_utils.UrdfFileCfg(
        asset_path=os.path.join(_TURTLEBOT3_DESCRIPTION_DIR, "urdf", "turtlebot3_waffle_pi.urdf"),
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=4,
            solver_velocity_iteration_count=0,
        ),
        fix_base=False,
        merge_fixed_joints=True,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.01),
        joint_pos={
            "wheel_left_joint": 0.0,
            "wheel_right_joint": 0.0,
        },
        joint_vel={
            "wheel_left_joint": 0.0,
            "wheel_right_joint": 0.0,
        },
    ),
    actuators={
        "wheels": ImplicitActuatorCfg(
            joint_names_expr=["wheel_left_joint", "wheel_right_joint"],
            effort_limit_sim=1.0,
            velocity_limit=6.0,
            stiffness=0.0,
            damping=1.0,
        ),
    },
)
"""Configuration for the TurtleBot3 Waffle Pi robot.

The TurtleBot3 Waffle Pi is a small, affordable, programmable, ROS-based mobile robot.
It uses a differential drive mechanism with two motorized wheels and two passive casters.

Specifications:
- Wheel separation: 0.288 m
- Wheel radius: 0.033 m
- Maximum translational velocity: 0.26 m/s
- Maximum rotational velocity: 1.82 rad/s
- Sensors: LDS-01 LiDAR, Raspberry Pi Camera v2 (8MP)
"""
