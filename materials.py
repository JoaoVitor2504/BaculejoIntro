import bpy

# ----------------------------------------------------------
# MATERIAL PRINCIPAL
# ----------------------------------------------------------

def create_main_material():

    material = bpy.data.materials.new("Baculejo_Metal")

    material.use_nodes = True

    nodes = material.node_tree.nodes
    links = material.node_tree.links

    nodes.clear()

    output = nodes.new("ShaderNodeOutputMaterial")
    output.location = (700,0)

    principled = nodes.new("ShaderNodeBsdfPrincipled")
    principled.location = (250,0)

    emission = nodes.new("ShaderNodeEmission")
    emission.location = (250,-220)

    mix = nodes.new("ShaderNodeAddShader")
    mix.location = (500,-50)

    # Metallic
    principled.inputs["Base Color"].default_value = (
        0.78,
        0.78,
        0.82,
        1
    )

    principled.inputs["Metallic"].default_value = 1.0

    principled.inputs["Roughness"].default_value = 0.18

    principled.inputs["Specular IOR Level"].default_value = 0.65

    # Glow Roxo
    emission.inputs["Color"].default_value = (
        0.50,
        0.15,
        1.00,
        1
    )

    emission.inputs["Strength"].default_value = 2.5

    links.new(principled.outputs["BSDF"], mix.inputs[0])
    links.new(emission.outputs["Emission"], mix.inputs[1])
    links.new(mix.outputs["Shader"], output.inputs["Surface"])

    return material


# ----------------------------------------------------------
# MATERIAL SECUNDÁRIO
# ----------------------------------------------------------

def create_dark_material():

    material = bpy.data.materials.new("Dark")

    material.use_nodes = True

    bsdf = material.node_tree.nodes["Principled BSDF"]

    bsdf.inputs["Base Color"].default_value = (
        0.03,
        0.03,
        0.03,
        1
    )

    bsdf.inputs["Metallic"].default_value = 0

    bsdf.inputs["Roughness"].default_value = 1

    return material


# ----------------------------------------------------------
# APLICAÇÃO
# ----------------------------------------------------------

def apply_material(obj, material):

    obj.data.materials.clear()

    obj.data.materials.append(material)


# ----------------------------------------------------------
# CRIA TODOS
# ----------------------------------------------------------

def create_materials():

    main = create_main_material()

    dark = create_dark_material()

    for obj in bpy.data.objects:

        if obj.type != "MESH":
            continue

        if obj.name == "Nickname":

            apply_material(obj, main)

        elif obj.name == "Subtitle":

            apply_material(obj, main)

        else:

            apply_material(obj, dark)

    return main
