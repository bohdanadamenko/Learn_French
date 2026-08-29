"""
Generate high-contrast, luminous Belgian-themed logo and favicon assets.
Optimized for maximum contrast and vivid visibility in both Dark and Light themes.
"""
import os
from PIL import Image, ImageDraw

def generate_assets():
    static_dir = "/Users/dee7even/Documents/project-valerie/FF_Gemini/apps/core/static"
    images_dir = os.path.join(static_dir, "core", "images")
    os.makedirs(images_dir, exist_ok=True)

    size = 512
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))

    # Outer border ring for high visibility against dark backgrounds
    corner_radius = 110
    outer_pad = 12
    inner_size = size - (outer_pad * 2)

    # 1. Base luminous rim
    rim_mask = Image.new("L", (size, size), 0)
    rim_draw = ImageDraw.Draw(rim_mask)
    rim_draw.rounded_rectangle([(outer_pad - 6, outer_pad - 6), (size - outer_pad + 6, size - outer_pad + 6)], radius=corner_radius + 4, fill=255)
    
    rim_layer = Image.new("RGBA", (size, size), (255, 255, 255, 180))
    img.paste(rim_layer, (0, 0), rim_mask)

    # 2. Tricolor body
    body_mask = Image.new("L", (size, size), 0)
    b_draw = ImageDraw.Draw(body_mask)
    b_draw.rounded_rectangle([(outer_pad, outer_pad), (size - outer_pad, size - outer_pad)], radius=corner_radius, fill=255)

    tricolor = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    t_draw = ImageDraw.Draw(tricolor)
    
    stripe_w = inner_size / 3
    x0 = outer_pad
    # High-contrast deep black with warm tone
    t_draw.rectangle([(x0, outer_pad), (x0 + stripe_w, size - outer_pad)], fill=(28, 30, 36, 255))
    # Radiant Belgian Gold
    t_draw.rectangle([(x0 + stripe_w, outer_pad), (x0 + (stripe_w * 2), size - outer_pad)], fill=(255, 209, 0, 255))
    # Radiant Belgian Scarlet Red
    t_draw.rectangle([(x0 + (stripe_w * 2), outer_pad), (size - outer_pad, size - outer_pad)], fill=(239, 43, 62, 255))

    img.paste(tricolor, (0, 0), body_mask)

    # 3. Center Luminous Glass Diamond / Disc for the "F"
    badge_size = 280
    b_offset = (size - badge_size) // 2
    
    center_glass = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    cg_draw = ImageDraw.Draw(center_glass)
    # Bright frosted circle
    cg_draw.ellipse(
        [(b_offset, b_offset), (b_offset + badge_size, b_offset + badge_size)],
        fill=(15, 23, 42, 230),
        outline=(255, 255, 255, 220),
        width=10
    )
    img = Image.alpha_composite(img, center_glass)

    # 4. Bold Modern "F" Monogram
    draw = ImageDraw.Draw(img)
    stem_x = 215
    stem_top = 180
    stem_bot = 332
    stem_w = 34
    
    # White vertical bar
    draw.rounded_rectangle([(stem_x, stem_top), (stem_x + stem_w, stem_bot)], radius=10, fill=(255, 255, 255, 255))
    # White top bar
    bar_top_w = 88
    draw.rounded_rectangle([(stem_x, stem_top), (stem_x + bar_top_w, stem_top + stem_w)], radius=10, fill=(255, 255, 255, 255))
    # Gold middle bar
    bar_mid_y = 244
    bar_mid_w = 70
    draw.rounded_rectangle([(stem_x, bar_mid_y), (stem_x + bar_mid_w, bar_mid_y + stem_w - 4)], radius=8, fill=(255, 209, 0, 255))

    # Save apple-touch-icon.png (180x180)
    apple_icon = img.resize((180, 180), Image.LANCZOS)
    apple_path = os.path.join(static_dir, "apple-touch-icon.png")
    apple_icon.save(apple_path, "PNG")
    print("Generated:", apple_path)

    # Save favicon.ico
    ico_path = os.path.join(static_dir, "favicon.ico")
    img.save(ico_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    print("Generated:", ico_path)

    # Save high-res png logo
    logo_png_path = os.path.join(images_dir, "belgian_logo.png")
    img.save(logo_png_path, "PNG")
    print("Generated:", logo_png_path)

    # 5. Crisp Vector SVG with Outer Glow & High-Contrast Light Rim
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <clipPath id="innerRounded">
      <rect x="2" y="2" width="96" height="96" rx="20" ry="20"/>
    </clipPath>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-color="#FFD100" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Outer Luminous White Frame for Dark Theme Contrast -->
  <rect x="1" y="1" width="98" height="98" rx="22" ry="22" fill="#FFFFFF" fill-opacity="0.25" stroke="rgba(255,255,255,0.7)" stroke-width="1.5"/>

  <!-- Belgian Tricolor Background -->
  <g clip-path="url(#innerRounded)">
    <rect x="2" y="2" width="32" height="96" fill="#1C1E24"/>
    <rect x="34" y="2" width="32" height="96" fill="#FFD100"/>
    <rect x="66" y="2" width="32" height="96" fill="#EF2B3E"/>
  </g>

  <!-- Inner High-Contrast Dark Glass Disc with Bright Ring -->
  <circle cx="50" cy="50" r="30" fill="#0F172A" fill-opacity="0.95" stroke="#FFFFFF" stroke-width="2.5" filter="url(#glow)"/>

  <!-- Letter F Symbol -->
  <rect x="41" y="32" width="7.5" height="36" rx="2.5" fill="#FFFFFF"/>
  <rect x="41" y="32" width="20" height="7.5" rx="2.5" fill="#FFFFFF"/>
  <rect x="41" y="47" width="15" height="6.5" rx="2" fill="#FFD100"/>
</svg>
"""
    svg_path = os.path.join(images_dir, "belgian_logo.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Generated SVG:", svg_path)

if __name__ == '__main__':
    generate_assets()
