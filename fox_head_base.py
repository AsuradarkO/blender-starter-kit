"""
Low-poly fox head — Vince's first Blender run.
================================================
HOW TO RUN IT (2 minutes):
  1. Open Blender -> switch to the "Scripting" tab at the top.
  2. Click New, paste this whole file, press the ▶ Run Script button.
  3. A cartoon fox head appears. Press Z -> 8 (Rendered view) to see it shaded.

WHAT IT DOES: builds a stylized fox head from primitives —
UV sphere head, cone ears, cylinder snout, sphere eyes —
with flat shading and two materials (orange fur, white muzzle).
This is the "low-poly base mesh" workflow used for VRChat avatars:
block out the shape first, refine and rig later.

Laptop note (i7 10th gen, 8GB, no GPU): this scene is tiny
(a few hundred polygons), so it runs fine. For test renders keep
Eevee at 50-100% resolution until you're used to the timing.
"""

import bpy
import math

# ---------------------------------------------------------------
# Clean slate: delete the default cube, light and camera
# ---------------------------------------------------------------
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

def new_part(name, make_op, **op_kwargs):
    """Create a primitive, name it, return the object."""
    make_op(**op_kwargs)
    obj = bpy.context.active_object
    obj.name = name
    return obj

def paint(obj, color):
    """Give an object a flat Principled material of an RGBA color."""
    mat = bpy.data.materials.new(name=f"{obj.name}_mat")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = color
    obj.data.materials.append(mat)

def flat_shade(obj):
    """Low-poly look: turn off smooth shading on every face."""
    for poly in obj.data.polygons:
        poly.use_smooth = False

ORANGE = (0.85, 0.42, 0.13, 1.0)   # fox fur
WHITE  = (0.96, 0.94, 0.90, 1.0)   # muzzle / ear tips
DARK   = (0.10, 0.09, 0.09, 1.0)   # eyes / nose

# ---------------------------------------------------------------
# Head — a squashed sphere
# ---------------------------------------------------------------
head = new_part("FoxHead", bpy.ops.mesh.primitive_uv_sphere_add,
                segments=12, ring_count=8, radius=1.0,
                location=(0, 0, 0))
head.scale = (1.0, 0.85, 0.9)
paint(head, ORANGE)
flat_shade(head)

# ---------------------------------------------------------------
# Ears — cones, tilted outward, tips up
# ---------------------------------------------------------------
for side, x in (("L", -0.55), ("R", 0.55)):
    ear = new_part(f"Ear{side}", bpy.ops.mesh.primitive_cone_add,
                   radius1=0.32, depth=0.75,
                   location=(x, 0.05, 1.05))
    ear.rotation_euler = (0.0, -0.35 * (1 if x > 0 else -1), 0.0)
    paint(ear, ORANGE)
    flat_shade(ear)

# ---------------------------------------------------------------
# Snout — a tapered cylinder pointing at the camera
# ---------------------------------------------------------------
snout = new_part("Snout", bpy.ops.mesh.primitive_cylinder_add,
                 vertices=10, radius=0.42, depth=0.6,
                 location=(0, -0.85, -0.15))
snout.rotation_euler = (math.radians(90), 0, 0)
snout.scale = (1.0, 1.0, 0.8)
paint(snout, WHITE)
flat_shade(snout)

# Nose — small dark cone on the snout tip
nose = new_part("Nose", bpy.ops.mesh.primitive_cone_add,
                radius1=0.12, depth=0.16,
                location=(0, -1.12, -0.05))
nose.rotation_euler = (math.radians(-90), 0, 0)
paint(nose, DARK)
flat_shade(nose)

# ---------------------------------------------------------------
# Eyes — two dark spheres, slightly forward
# ---------------------------------------------------------------
for side, x in (("L", -0.38), ("R", 0.38)):
    eye = new_part(f"Eye{side}", bpy.ops.mesh.primitive_uv_sphere_add,
                   segments=10, ring_count=6, radius=0.14,
                   location=(x, -0.68, 0.28))
    paint(eye, DARK)
    flat_shade(eye)

# ---------------------------------------------------------------
# Join everything into one object called FoxHead
# ---------------------------------------------------------------
bpy.ops.object.select_all(action='SELECT')
bpy.context.view_layer.objects.active = head
bpy.ops.object.join()
bpy.context.active_object.name = "FoxHead"

# Frame it nicely in the viewport
print("Done — FoxHead built. Press Z, then 8, to preview the shaded result.")
