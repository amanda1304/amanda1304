from datetime import datetime
import random

# Tamanho da área
WIDTH = 800
HEIGHT = 400

# Gato simples em SVG (desenho vetorial)
GATO_SVG = """
<g id="gato" transform="translate(350, 250)">
    <!-- Corpo -->
    <ellipse cx="50" cy="50" rx="50" ry="35" fill="#f4a460" />
    <!-- Cabeça -->
    <circle cx="50" cy="0" r="30" fill="#f4a460" />
    <!-- Olhos -->
    <circle cx="40" cy="-5" r="5" fill="white" />
    <circle cx="60" cy="-5" r="5" fill="white" />
    <circle cx="40" cy="-5" r="2" fill="black" />
    <circle cx="60" cy="-5" r="2" fill="black" />
    <!-- Boca -->
    <path d="M 45 10 Q 50 15 55 10" stroke="black" fill="transparent" />
    <!-- Orelhas -->
    <polygon points="30,-15 40,-35 50,-15" fill="#f4a460" />
    <polygon points="70,-15 60,-35 50,-15" fill="#f4a460" />
</g>
"""

# Gerar blocos (comida caindo)
blocos = []
for _ in range(10):
    x = random.randint(0, WIDTH - 20)
    y = random.randint(0, 200)
    cor = random.choice(["#ff4500", "#ffd700", "#adff2f", "#87cefa"])
    blocos.append(f'<rect x="{x}" y="{y}" width="20" height="20" fill="{cor}" />')

# Criar SVG
svg_content = f"""<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
<style>
    text {{ font-family: Arial, sans-serif; }}
</style>
<rect width="100%" height="100%" fill="#f0f8ff" />
<text x="10" y="20" font-size="16" fill="#333">Gato Food Drop - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</text>
{''.join(blocos)}
{GATO_SVG}
</svg>
"""

# Salvar arquivo
with open("animacao.svg", "w", encoding="utf-8") as f:
    f.write(svg_content)

print("Arquivo animacao.svg gerado com sucesso!")
