# Blender Starter Kit — low-poly fox head in pure `bpy`

A commented, beginner-proof Blender Python script that builds a stylized low-poly fox head from primitives — the "blockout" stage of the VRChat-avatar workflow: block the shape first, refine and rig later.

## Run it (2 minutes)

1. Install **Blender 4.5 LTS** (runs fully CPU-only — no GPU needed)
2. Open Blender → **Scripting** tab → **New** → paste `fox_head_base.py` → **Run Script**
3. A cartoon fox head appears. Press **Z → 8** for rendered view.

## What the script builds

UV-sphere head, cone ears, cylinder snout, sphere eyes — flat shading, two materials (orange fur, white muzzle). A few hundred polygons, so it runs fine on modest hardware.

## Laptop rules (baked into the docs)

- **Low-poly everything** while learning — hundreds to low-thousands of polygons
- **Eevee, not Cycles** — Cycles on CPU takes minutes per frame; Eevee previews in seconds
- **Test at 50% resolution** while iterating; full-res only for final exports

## Where this goes next

- **Avatar lane:** body, ear refinement, then rigging (Live2D/VRChat direction)
- **Asset lane:** the same primitive-combining skills build low-poly props for CGTrader/Sketchfab

---
*Script and guide written with Muse (Meta's AI assistant) to Vince Pham's spec — CPU-only 3D on a laptop with no discrete GPU.*
