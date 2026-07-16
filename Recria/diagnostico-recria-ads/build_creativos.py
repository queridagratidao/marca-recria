# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W = H = 1080
BLACK = (10, 10, 10)
GOLD = (201, 162, 78)
GOLD_LIGHT = (228, 201, 136)
WHITE = (255, 255, 255)

FONT_DIR = "/c/Windows/Fonts"

def font(name, size):
    return ImageFont.truetype(f"{FONT_DIR}/{name}", size)

f_badge = font("calibrib.ttf", 26)
f_button = font("calibrib.ttf", 32)

# Logo real (icone + wordmark + tagline), recortado para a caixa de conteudo real
LOGO_PATH = "../site-institucional/diagnostico-recria/assets/logo.png"
_logo_full = Image.open(LOGO_PATH).convert("RGBA")
_logo_crop = _logo_full.crop(_logo_full.getbbox())
LOGO_H = 108
_ratio = LOGO_H / _logo_crop.height
LOGO = _logo_crop.resize((int(_logo_crop.width * _ratio), LOGO_H), Image.LANCZOS)

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

def base_canvas():
    img = Image.new("RGB", (W, H), BLACK)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    odraw.ellipse([-350, -350, 450, 450], fill=(201, 162, 78, 55))
    odraw.ellipse([W-550, H-550, W+350, H+350], fill=(201, 162, 78, 40))
    overlay = overlay.filter(ImageFilter.GaussianBlur(120))
    img = Image.alpha_composite(img.convert("RGBA"), overlay)
    img.alpha_composite(LOGO, (56, 44))
    img = img.convert("RGB")
    draw = ImageDraw.Draw(img)
    return img, draw

def badge(draw, text):
    w_text = draw.textlength(text, font=f_badge)
    pad_x, pad_y = 28, 14
    box_w = w_text + pad_x * 2
    box_h = f_badge.size + pad_y * 2
    x0 = (W - box_w) / 2
    y0 = 195
    draw.rounded_rectangle([x0, y0, x0 + box_w, y0 + box_h], radius=box_h/2, outline=GOLD, width=2)
    draw.text((W/2, y0 + box_h/2), text, font=f_badge, fill=GOLD_LIGHT, anchor="mm")
    return y0 + box_h

def cta_button(draw, text, y0):
    w_text = draw.textlength(text, font=f_button)
    box_w = max(420, w_text + 90)
    box_h = 92
    x0 = (W - box_w) / 2
    draw.rounded_rectangle([x0, y0, x0 + box_w, y0 + box_h], radius=box_h/2, fill=GOLD)
    draw.text((W/2, y0 + box_h/2), text, font=f_button, fill=BLACK, anchor="mm")

def build(filename, badge_text, headline, sub, button_text, headline_size=54, sub_size=28):
    f_headline = font("georgiab.ttf", headline_size)
    f_sub = font("georgiai.ttf", sub_size)
    img, draw = base_canvas()
    y = badge(draw, badge_text)
    y = wrap_draw(draw, headline, f_headline, 940, W/2, y + 55, WHITE, line_spacing=1.14)
    y = wrap_draw(draw, sub, f_sub, 860, W/2, y + 34, GOLD_LIGHT, line_spacing=1.3)
    cta_y = min(y + 50, H - 150)
    cta_button(draw, button_text, cta_y)
    img.save(filename, quality=95)
    print("salvo:", filename)

# Criativo 1 - Topo de funil
build(
    "criativo-1-topo.png",
    "VAGAS LIMITADAS",
    "O seu negócio não vende como você gostaria?",
    "O gargalo pode estar no seu marketing, comercial ou até mesmo no modelo de negócio. Em uma consultoria de uma hora, com quem tem mais de dez anos de experiência, você vai descobrir onde está esse gargalo que está travando o crescimento do seu negócio e suas vendas. E olha, a consultoria custa menos do que uma pizza.",
    "SAIBA MAIS",
    headline_size=52,
    sub_size=27,
)

# Criativo 1B - Topo de funil (espelha a headline da LP)
build(
    "criativo-1b-topo.png",
    "VAGAS LIMITADAS · R$ 67",
    "Descubra onde estão os gargalos que estão travando as vendas e o crescimento do seu negócio, em uma consultoria online de uma hora.",
    "Com um profissional com mais de dez anos de experiência. Receba também um diagnóstico documentado após a sessão de consultoria.",
    "SAIBA MAIS",
    headline_size=42,
    sub_size=28,
)

# Criativo 2 - Meio de funil
build(
    "criativo-2-meio.png",
    "VAGAS LIMITADAS",
    "Onze anos de experiência disponíveis para o seu negócio, por uma hora.",
    "Uma consultoria individual onde vamos analisar o seu negócio de ponta a ponta e entregar um diagnóstico documentado com o passo a passo para você agir. De R$ 297 por R$ 67.",
    "QUERO SABER MAIS",
    headline_size=50,
    sub_size=28,
)

# Criativo 3 - Fundo de funil
build(
    "criativo-3-fundo.png",
    "VAGAS LIMITADAS",
    "Consultoria online para o seu negócio. Descubra o que está travando as suas vendas.",
    "Por apenas R$ 67, uma hora de consultoria ao vivo e online, com quem tem mais de dez anos de experiência em marketing e comercial. Você vai descobrir os possíveis gargalos que estão impedindo o crescimento do seu negócio e reduzindo as vendas, e ainda vai receber um diagnóstico documentado. Pagamento facilitado por Pix, boleto ou cartão de crédito.",
    "GARANTIR MINHA VAGA",
    headline_size=44,
    sub_size=25,
)
