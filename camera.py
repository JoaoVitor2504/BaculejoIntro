import bpy
import math


CAMERA_NAME = "IntroCamera"


def delete_old_camera():

    if CAMERA_NAME in bpy.data.objects:

        obj = bpy.data.objects[CAMERA_NAME]

        bpy.data.objects.remove(obj, do_unlink=True)


def create_camera():

    delete_old_camera()

    cam_data = bpy.data.cameras.new(CAMERA_NAME)

    cam = bpy.data.objects.new(CAMERA_NAME, cam_data)

    bpy.context.collection.objects.link(cam)

    bpy.context.scene.camera = cam

    ##################################################
    # Lens
    ##################################################

    cam.data.lens = 85

    cam.data.clip_start = 0.1

    cam.data.clip_end = 1000

    ##################################################
    # DOF
    ##################################################

    cam.data.dof.use_dof = True

    cam.data.dof.aperture_fstop = 1.8

    ##################################################
    # Position
    ##################################################

    cam.location = (
        0,
        -7,
        0.25
    )

    ##################################################
    # Rotation
    ##################################################

    cam.rotation_euler = (
        math.radians(90),
        0,
        0
    )

    ##################################################
    # Focus
    ##################################################

    if "Nickname" in bpy.data.objects:

        cam.data.dof.focus_object = bpy.data.objects["Nickname"]

    return cam


def animate_camera():

    cam = bpy.data.objects.get(CAMERA_NAME)

    if cam is None:
        return

    ##################################################

    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 180

    ##################################################

    cam.location = (
        0,
        -7,
        0.25
    )

    cam.keyframe_insert(
        data_path="location",
        frame=1
    )

    ##################################################

    cam.location = (
        0,
        -5.5,
        0.25
    )

    cam.keyframe_insert(
        data_path="location",
        frame=180
    )

    ##################################################

    if cam.animation_data:

        action = cam.animation_data.action

        for fc in action.fcurves:

            for kp in fc.keyframe_points:

                kp.interpolation = 'BEZIER'
