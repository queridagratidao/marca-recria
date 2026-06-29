# Manual de Identidade Visual — Recria

**Marca:** Recria (@agencia.recria no Instagram; CEO @amandarecria)
**Tagline:** "Recriando marketing, simplificando vendas"
**Bio:** "Te ajudamos a vender todo santo dia através da comunicação certa para as pessoas certas."

## Cores

| Uso | Cor | Hex |
|---|---|---|
| Fundo principal | Preto | `#000000` |
| Texto/contraste | Branco | `#FFFFFF` |
| Detalhes, CTAs, destaques | Dourado | `#C9A24E` |
| Dourado claro (variação/realce) | Dourado claro | `#E4C988` |

## Tipografia

- **Títulos:** Playfair Display (serifa alta, elegante)
- **Corpo de texto:** Lora
- **Destaque de palavra-chave:** itálico dourado

## Logo

Lâmpada + cérebro em dourado, combinada com o wordmark "RECRIA".
Arquivo: `Recria  Marketing evento IBGE.png` (dourado, fundo transparente) em `agencia-ia-toolkit\`.

> Sempre usar o logo real do arquivo — nunca recriar/redesenhar uma versão genérica.

## Padrão de produção (carrosséis e criativos)

- Template HTML em preto/dourado seguindo as cores e fontes acima
- Renderização via Chrome headless:
  `chrome --headless=new --screenshot --window-size=1080,1350 --force-device-scale-factor=2`
- Imagens embutidas em base64 no HTML antes de renderizar
- Motivo: html2canvas + file:// quebra a exportação
