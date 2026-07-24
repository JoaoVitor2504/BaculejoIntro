import bpy


def clear_scene():

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)


def create_single_text(name, body, size, location):

    bpy.ops.object.text_add(location=location)

    obj = bpy.context.active_object

    obj.name = name

    txt = obj.data

    txt.body = body

    txt.align_x = 'CENTER'

    txt.align_y = 'CENTER'

    txt.extrude = 0.08

    txt.bevel_depth = 0.012

    txt.bevel_resolution = 8

    txt.size = size

    return obj


def convert_to_mesh(obj):

    name = obj.name

    bpy.context.view_layer.objects.active = obj

    obj.select_set(True)

    bpy.ops.object.convert(target='MESH')

    new_obj = bpy.context.active_object

    new_obj.name = name

    new_obj.select_set(False)

    return new_obj


def create_text(nickname, subtitle):

    clear_scene()

    subtitle_obj = create_single_text(
        "Subtitle",
        subtitle,
        0.45,
        (0, 0, 0.25)
    )

    nickname_obj = create_single_text(
        "Nickname",
        nickname,
        1.15,
        (0, 0, -0.10)
    )

    subtitle_obj = convert_to_mesh(subtitle_obj)
    nickname_obj = convert_to_mesh(nickname_obj)

    return subtitle_obj, nickname_obj
