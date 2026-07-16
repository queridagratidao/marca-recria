# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W = H = 1080
BLACK = (10, 10, 10)
GOLD = (201, 162, 78)
GOLD_LIGHT = (228, 201, 136)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)

FONT_DIR = "/c/Windows/Fonts"

def font(name, size):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)

f_badge = font("calibrib.ttf", 26)
f_headline = font("georgiab.ttf", 60)
f_sub = font("georgiai.ttf", 32)
f_button = font("calibrib.ttf", 34)
f_logo = font("calibrib.ttf", 28)

def wrap_draw(draw, text, fnt, max_width, x_center, y, fill, line_spacing=1.15):
    words = text.split(" ")
    lines = []
    cur = ""
    for w in words:
        test = (cur + " " + w).strip()
        if draw.textlength(test, font=fnt) <= max_width:
            cur = test
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    line_h = fnt.size * line_spacing
    cy = y
    for line in lines:
        w_line = draw.textlength(line, font=fnt)
        draw.text((x_center - w_line / 2, cy), line, font=fnt, fill=fill)
        cy += line_h
    return cy

def rounded_rect(draw, box, radius, fill):
    draw.rounded_rectangle(box, radius=radius, fill=fill)

def base_canvas():
    img = Image.new("RGB", (W, H), BLACK)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    odraw.ellipse([-350, -350, 450, 450], fill=(201, 162, 78, 55))
    odraw.ellipse([W-550, H-550, W+350, H+350], fill=(201, 162, 78, 40))
    overlay = overlay.filter(ImageFilter.GaussianBlur(120))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(img)
    draw.ellipse([60, 56, 84, 80], fill=GOLD)
    draw.text((96, 52), "RECRIA", font=f_logo, fill=GOLD)
    return img, draw

def badge(draw, text):
    w_text = draw.textlength(text, font=f_badge)
    pad_x, pad_y = 28, 14
    box_w = w_text + pad_x * 2
    box_h = f_badge.size + pad_y * 2
    x0 = (W - box_w) / 2
    y0 = 150
    draw.rounded_rectangle([x0, y0, x0 + box_w, y0 + box_h], radius=box_h/2, outline=GOLD, width=2)
    draw.text((W/2, y0 + box_h/2), text, font=f_badge, fill=GOLD_LIGHT, anchor="mm")

def cta_button(draw, text):
    box_w, box_h = 460, 90
    x0 = (W - box_w) / 2
    y0 = H - 170
    rounded_rect(draw, [x0, y0, x0 + box_w, y0 + box_h], radius=box_h/2, fill=GOLD)
    draw.text((W/2, y0 + box_h/2), text, font=f_button, fill=BLACK, anchor="mm")

def build(filename, badge_text, headline, sub, button_text):
    img, draw = base_canvas()
    badge(draw, badge_text)
    y = wrap_draw(draw, headline, f_headline, 920, W/2, 280, WHITE, line_spacing=1.12)
    wrap_draw(draw, sub, f_sub, 820, W/2, y + 30, GOLD_LIGHT, line_spacing=1.25)
    cta_button(draw, button_text)
    draw.text((W/2, H - 50), "agenciarecria.com.br/diagnostico-recria", font=font("calibri.ttf", 20), fill=GRAY, anchor="mm")
    img.save(filename, quality=95)
    print("salvo:", filename)

# Criativo 1 - Topo de funil
build(
    "criativo-1-topo.png",
    "VAGAS LIMITADAS",
    "O seu negócio não vende como você gostaria?",
    "Descubra o gargalo em 1h de consultoria. Custa menos que uma pizza.",
    "SAIBA MAIS",
)

# Criativo 1B - Topo de funil (espelha a headline da LP)
build(
    "criativo-1b-topo.png",
    "VAGAS LIMITADAS · R$ 67",
    "Descubra onde estão os gargalos que travam suas vendas",
    "Consultoria online de 1h com quem tem mais de dez anos de experiência. Diagnóstico documentado incluso.",
    "SAIBA MAIS",
)

# Criativo 2 - Meio de funil
build(
    "criativo-2-meio.png",
    "DE R$ 297 POR R$ 67",
    "Onze anos de experiência disponíveis para o seu negócio, por uma hora.",
    "Diagnóstico documentado com o passo a passo para você agir.",
    "QUERO SABER MAIS",
)

# Criativo 3 - Fundo de funil
build(
    "criativo-3-fundo.png",
    "VAGAS LIMITADAS",
    "Consultoria online para o seu negócio",
    "Por R$ 67, descubra o que está travando suas vendas. Pix, boleto ou cartão.",
    "GARANTIR MINHA VAGA",
)
