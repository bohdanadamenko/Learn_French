"""
Generate modern Belgian-themed logo and favicon assets.
Features the Belgian tricolor (Black, Yellow/Gold, Red) with modern glassmorphism aesthetic and letter F / Belgium motif.
"""
import os
from PIL import Image, ImageDraw, ImageFont

def generate_assets():
    static_dir = "/Users/dee7even/Documents/project-valerie/FF_Gemini/apps/core/static"
    images_dir = os.path.join(static_dir, "core", "images")
    os.makedirs(images_dir, exist_ok=True)

    # 1. Generate 512x512 Master Icon (Apple Touch Icon & Favicon Source)
    size = 512
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw rounded square base with subtle shadow/border
    corner_radius = 110
    
    # 3-Stripe Belgian Flag background inside rounded container
    # Mask for rounded rectangle
    mask = Image.new("L", (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([(0, 0), (size, size)], radius=corner_radius, fill=255)

    # Tricolor canvas
    tricolor = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    t_draw = ImageDraw.Draw(tricolor)
    
    stripe_w = size / 3
    # Black stripe (left)
    t_draw.rectangle([(0, 0), (stripe_w, size)], fill=(24, 24, 27, 255))
    # Yellow / Gold stripe (middle)
    t_draw.rectangle([(stripe_w, 0), (stripe_w * 2, size)], fill=(253, 216, 53, 255))
    # Red stripe (right)
    t_draw.rectangle([(stripe_w * 2, 0), (size, size)], fill=(239, 68, 68, 255))

    # Apply mask
    img.paste(tricolor, (0, 0), mask)

    # Add a glowing glass center badge for the "F" letter
    badge_size = 320
    b_offset = (size - badge_size) // 2
    
    # Center dark glass disc
    glass_disc = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(glass_disc)
    g_draw.ellipse(
        [(b_offset, b_offset), (b_offset + badge_size, b_offset + badge_size)],
        fill=(15, 23, 42, 235),
        outline=(255, 255, 255, 120),
        width=8
    )
    img = Image.alpha_composite(img, glass_disc)

    # Draw stylized "F" in the center with modern geometric lines
    draw = ImageDraw.Draw(img)
    
    # Draw Bold Modern "F" in white / gold
    # Vertical stem
    stem_x = 210
    stem_top = 175
    stem_bot = 335
    stem_w = 34
    
    draw.rounded_rectangle([(stem_x, stem_top), (stem_x + stem_w, stem_bot)], radius=12, fill=(255, 255, 255, 255))
    # Top horizontal bar
    bar_top_w = 95
    draw.rounded_rectangle([(stem_x, stem_top), (stem_x + bar_top_w, stem_top + stem_w)], radius=12, fill=(255, 255, 255, 255))
    # Middle horizontal bar (Gold accent)
    bar_mid_y = 240
    bar_mid_w = 75
    draw.rounded_rectangle([(stem_x, bar_mid_y), (stem_x + bar_mid_w, bar_mid_y + stem_w - 4)], radius=10, fill=(253, 216, 53, 255))

    # Save apple-touch-icon.png (180x180)
    apple_icon = img.resize((180, 180), Image.LANCZOS)
    apple_path = os.path.join(static_dir, "apple-touch-icon.png")
    apple_icon.save(apple_path, "PNG")
    print("Generated:", apple_path)

    # Save favicon.ico (multi-res 16, 32, 48, 64, 128, 256)
    ico_path = os.path.join(static_dir, "favicon.ico")
    img.save(ico_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    print("Generated:", ico_path)

    # Save high-res png logo
    logo_png_path = os.path.join(images_dir, "belgian_logo.png")
    img.save(logo_png_path, "PNG")
    print("Generated:", logo_png_path)

    # 2. Generate Crisp SVG Vector Logo
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <clipPath id="rounded">
      <rect width="100" height="100" rx="22" ry="22"/>
    </clipPath>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.3"/>
    </filter>
  </defs>
  
  <!-- Belgian Tricolor Background -->
  <g clip-path="url(#rounded)">
    <rect x="0" y="0" width="33.33" height="100" fill="#18181B"/>
    <rect x="33.33" y="0" width="33.33" height="100" fill="#FDD835"/>
    <rect x="66.66" y="0" width="33.34" height="100" fill="#EF4444"/>
  </g>
  
  <!-- Center Dark Glass Disc with Border -->
  <circle cx="50" cy="50" r="32" fill="#0F172A" fill-opacity="0.9" stroke="rgba(255,255,255,0.4)" stroke-width="2" filter="url(#shadow)"/>
  
  <!-- Letter F Symbol -->
  <!-- Stem -->
  <rect x="41" y="32" width="7" height="36" rx="2.5" fill="#FFFFFF"/>
  <!-- Top Bar -->
  <rect x="41" y="32" width="20" height="7" rx="2.5" fill="#FFFFFF"/>
  <!-- Mid Bar (Belgian Gold) -->
  <rect x="41" y="47" width="15" height="6" rx="2" fill="#FDD835"/>
</svg>
"""
    svg_path = os.path.join(images_dir, "belgian_logo.svg")
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("Generated SVG:", svg_path)

if __name__ == '__main__':
    generate_assets()
