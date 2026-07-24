bl_info = {
    "name": "Baculejo Intro Generator",
    "author": "OpenAI + JoaoVitor2504",
    "version": (1, 0, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Baculejo",
    "description": "Create a cinematic intro automatically",
    "category": "Object",
}

import bpy

# -------------------------------------------------
# IMPORT MODULES
# -------------------------------------------------

try:
    from . import camera
    from . import materials
    from . import text
    from . import particles
    from . import smoke
    from . import compositor
    from . import animation
    from . import render
except Exception:
    camera = None
    materials = None
    text = None
    particles = None
    smoke = None
    compositor = None
    animation = None
    render = None


# -------------------------------------------------
# PROPERTIES
# -------------------------------------------------

class BaculejoProperties(bpy.types.PropertyGroup):

    nickname: bpy.props.StringProperty(
        name="Nickname",
        default="Baculejo"
    )

    subtitle: bpy.props.StringProperty(
        name="Subtitle",
        default="Edit by"
    )

    glow_strength: bpy.props.FloatProperty(
        name="Glow",
        default=3.0,
        min=0,
        max=20
    )

    particle_amount: bpy.props.IntProperty(
        name="Particles",
        default=300,
        min=0,
        max=5000
    )

    smoke_density: bpy.props.FloatProperty(
        name="Smoke",
        default=0.05,
        min=0,
        max=1
    )


# -------------------------------------------------
# OPERATOR
# -------------------------------------------------

class BACULEJO_OT_CreateIntro(bpy.types.Operator):

    bl_idname = "baculejo.create_intro"
    bl_label = "Create Intro"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        props = context.scene.baculejo

        self.report({'INFO'}, "Creating Intro...")

        if text:
          subtitle_obj, nickname_obj = text.create_text(
            props.nickname,
                props.subtitle
            )
        if materials:
            materials.create_materials()

        if camera:
            camera.create_camera()
            camera.animate_camera()

        if particles:
            particles.create_particles(
                props.particle_amount
            )

        if smoke:
            smoke.create_smoke(
                props.smoke_density
            )

        if compositor:
            compositor.create_compositor(
                props.glow_strength
            )

        if animation:
            animation.create_animation()

        if render:
            render.setup_render()

        self.report({'INFO'}, "Finished!")

        return {'FINISHED'}


# -------------------------------------------------
# PANEL
# -------------------------------------------------

class BACULEJO_PT_MainPanel(bpy.types.Panel):

    bl_label = "Baculejo Intro"

    bl_idname = "BACULEJO_PT_PANEL"

    bl_space_type = "VIEW_3D"

    bl_region_type = "UI"

    bl_category = "Baculejo"

    def draw(self, context):

        layout = self.layout

        props = context.scene.baculejo

        layout.label(text="Intro Generator")

        layout.separator()

        layout.prop(props, "subtitle")

        layout.prop(props, "nickname")

        layout.separator()

        layout.prop(props, "glow_strength")

        layout.prop(props, "particle_amount")

        layout.prop(props, "smoke_density")

        layout.separator()

        layout.operator(
            "baculejo.create_intro",
            icon="RENDER_ANIMATION"
        )


# -------------------------------------------------
# REGISTER
# -------------------------------------------------

classes = (

    BaculejoProperties,

    BACULEJO_OT_CreateIntro,

    BACULEJO_PT_MainPanel,

)


def register():

    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.baculejo = bpy.props.PointerProperty(
        type=BaculejoProperties
    )


def unregister():

    del bpy.types.Scene.baculejo

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
