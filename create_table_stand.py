from PIL import Image, ImageDraw, ImageFont
import os

w, h = 1200, 1800
card = Image.new('RGB', (w, h), color='#070c18')
draw = ImageDraw.Draw(card)

# Double border in royal gold
draw.rectangle([(25, 25), (w-25, h-25)], outline='#c9a84c', width=6)
draw.rectangle([(38, 38), (w-38, h-38)], outline='#5a481c', width=2)
draw.rectangle([(48, 48), (w-48, h-48)], outline='#2a210d', width=1)

# Corner ornamental designs
for cx, cy in [(25,25), (w-25,25), (25,h-25), (w-25,h-25)]:
    draw.polygon([(cx, cy-15), (cx+15, cy), (cx, cy+15), (cx-15, cy)], fill='#f5c84c')

# Load standard Windows fonts
try:
    font_brand = ImageFont.truetype('C:/Windows/Fonts/georgiab.ttf', 72)
    font_sub = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 24)
    font_loc = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 20)
    font_scan = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 44)
    font_hint = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 26)
    font_tags = ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf', 24)
    font_foot = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 22)
    font_gold = ImageFont.truetype('C:/Windows/Fonts/georgia.ttf', 28)
except Exception:
    font_brand = font_sub = font_loc = font_scan = font_hint = font_tags = font_foot = font_gold = ImageFont.load_default()

def draw_centered_text(y, text, font, fill):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    draw.text(((w - text_w) // 2, y), text, font=font, fill=fill)

# Emblem top
draw_centered_text(100, '✦   ✦   ✦', font_sub, '#c9a84c')
draw_centered_text(150, 'HIDE N SEEK', font_brand, '#fdf7eb')
draw_centered_text(245, 'C  A  F  É', font_gold, '#f5c84c')
draw_centered_text(295, 'GOOD FOOD  ·  GOOD MOOD', font_sub, '#d4c295')
draw_centered_text(335, '📍 Khanapur Main Road, Belagavi Dist.', font_loc, '#98a5c0')

# Divider bar
draw.line([(w//2 - 250, 385), (w//2 + 250, 385)], fill='#c9a84c', width=2)
draw.polygon([(w//2 - 8, 385-6), (w//2 + 8, 385-6), (w//2, 385+8)], fill='#f5c84c')

# Scan title
draw_centered_text(420, 'SCAN FOR DIGITAL MENU', font_scan, '#ffffff')
draw_centered_text(480, 'Explore All 74 Dishes & Order Direct to WhatsApp', font_hint, '#ebd8af')

# QR Code placement
qr = Image.open('hide-n-seek-qr-code.png').convert('RGB')
qr = qr.resize((660, 660), Image.Resampling.LANCZOS)

# White rounded card behind QR
qr_box = [(w//2 - 365, 540), (w//2 + 365, 1270)]
draw.rectangle(qr_box, fill='#ffffff', outline='#c9a84c', width=6)
card.paste(qr, (w//2 - 330, 575))

# Camera hint below QR
draw_centered_text(1310, '📸 Open Camera on iPhone or Android to Scan', font_scan, '#f5c84c')
draw_centered_text(1375, 'Instant Loading  ·  No App Download Required', font_hint, '#c2d0eb')

# Food badges
draw.line([(w//2 - 380, 1440), (w//2 + 380, 1440)], fill='#344265', width=1)
draw_centered_text(1475, '🥟 Sizzling Momos  ·  🍕 Handcrafted Pizzas  ·  🍜 Hakka Noodles', font_tags, '#ffffff')
draw_centered_text(1525, '🍟 Golden Fries  ·  🥤 Mocktails & Cold Coffee  ·  🍲 Soups & Pasta', font_tags, '#f0d9a6')
draw_centered_text(1575, '🟢 100% Pure Veg  &  🔴 Sizzling Non-Veg Options', font_sub, '#5fe384')

# Footer
draw.rectangle([(60, 1640), (w-60, 1730)], fill='#0d1527', outline='#c9a84c', width=2)
draw_centered_text(1658, 'DINE-IN  ·  TAKEAWAY  ·  PARTY ORDERS', font_tags, '#f5c84c')
draw_centered_text(1692, 'Open Daily: 11:00 AM – 11:00 PM  ·  Free WiFi For Guests', font_foot, '#b5c5e3')

card.save('hide-n-seek-table-stand.png', 'PNG')
print('Table stand image successfully generated!')
