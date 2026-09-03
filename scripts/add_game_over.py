import sys
import re
from pathlib import Path

if len(sys.argv) != 2:
    print("Usage: python add_game_over.py <svg>")
    sys.exit(1)

svg_path = Path(sys.argv[1])

svg = svg_path.read_text(encoding="utf-8")

overlay = r'''
<style>
@keyframes game-over {
  0% {
    opacity: 0;
  }

  10% {
    opacity: 1;
  }

  70% {
    opacity: 1;
  }

  100% {
    opacity: 0;
  }
}

.game-over-text {
  animation: game-over 4s ease-in-out 1 forwards;
}
</style>

<text
  x="50%"
  y="50%"
  text-anchor="middle"
  dominant-baseline="middle"
  class="game-over-text"
  font-family="monospace"
  font-size="28"
  font-weight="bold"
  fill="#ff0000">
  GAME OVER
</text>
'''

svg = re.sub(
    r'</svg>\s*$',
    overlay + '\n</svg>',
    svg
)

svg_path.write_text(svg, encoding="utf-8")

print(f"Added GAME OVER overlay to {svg_path}")
