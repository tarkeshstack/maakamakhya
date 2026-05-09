from PIL import Image, ImageDraw, ImageFont
import os

sizes = [72, 96, 128, 144, 192, 512]
os.makedirs('icons', exist_ok=True)

for size in sizes:
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Background gradient simulation — saffron circle
    for i in range(size):
        for j in range(size):
            dx = i - size/2
            dy = j - size/2
            dist = (dx**2 + dy**2)**0.5
            r = size * 0.48
            if dist <= r:
                # corner rounding
                t = dist / r
                r_col = int(200 + (232 - 200) * t)
                g_col = int(72 + (128 - 72) * t)
                b_col = int(0)
                a_col = 255
                img.putpixel((i, j), (r_col, g_col, b_col, a_col))

    # Draw cow emoji-like shape via text
    emoji_size = int(size * 0.55)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf", emoji_size)
    except:
        font = ImageFont.load_default()

    emoji = "🐄"
    try:
        bbox = draw.textbbox((0, 0), emoji, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        x = (size - tw) // 2
        y = (size - th) // 2 - int(size * 0.04)
        draw.text((x, y), emoji, font=font, embedded_color=True)
    except:
        # fallback: draw a simple circle
        margin = size // 6
        draw.ellipse([margin, margin, size - margin, size - margin], fill=(255, 255, 255, 180))

    img.save(f'icons/icon-{size}.png')
    print(f"Created icon-{size}.png")

print("All icons generated!")
