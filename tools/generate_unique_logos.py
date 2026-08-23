#!/usr/bin/env python3
"""Generate unique, color-coded, role-specific SVG logos and update openai.yaml brand colors for all 21 skills."""
import re
import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"

SKILL_DESIGNS = {
    "designly-director": {
        "color": "#0F172A",
        "accent": "#F59E0B",
        "bg_gradient": ("#1E293B", "#0F172A"),
        "icon_svg": """
          <!-- Central Neural Hub & Director Compass -->
          <circle cx="256" cy="256" r="140" stroke="#F59E0B" stroke-width="8" stroke-dasharray="16 12" fill="none" opacity="0.6"/>
          <circle cx="256" cy="256" r="90" fill="#0F172A" stroke="#F59E0B" stroke-width="12"/>
          <path d="M256 186L276 236L326 256L276 276L256 326L236 276L186 256L236 236Z" fill="#F59E0B"/>
          <circle cx="256" cy="116" r="16" fill="#F8FAFC"/>
          <circle cx="396" cy="256" r="16" fill="#F8FAFC"/>
          <circle cx="256" cy="396" r="16" fill="#F8FAFC"/>
          <circle cx="116" cy="256" r="16" fill="#F8FAFC"/>
          <path d="M256 132V166M380 256H346M256 380V346M132 256H166" stroke="#94A3B8" stroke-width="8" stroke-linecap="round"/>
        """
    },
    "creative-strategy": {
        "color": "#2563EB",
        "accent": "#60A5FA",
        "bg_gradient": ("#3B82F6", "#1D4ED8"),
        "icon_svg": """
          <!-- Strategy Target & Upward Vector -->
          <circle cx="256" cy="256" r="130" stroke="#93C5FD" stroke-width="10" fill="none" opacity="0.4"/>
          <circle cx="256" cy="256" r="85" stroke="#FFFFFF" stroke-width="12" fill="none"/>
          <circle cx="256" cy="256" r="32" fill="#FFFFFF"/>
          <path d="M140 372L340 172M340 172H240M340 172V272" stroke="#FEF08A" stroke-width="22" stroke-linecap="round" stroke-linejoin="round"/>
        """
    },
    "creative-director": {
        "color": "#D97706",
        "accent": "#FCD34D",
        "bg_gradient": ("#F59E0B", "#B45309"),
        "icon_svg": """
          <!-- Cannes Gold Diamond Spark -->
          <path d="M256 110L350 210L256 390L162 210Z" fill="#FEF3C7" stroke="#FFFFFF" stroke-width="12" stroke-linejoin="round"/>
          <path d="M162 210H350M256 110V390" stroke="#D97706" stroke-width="8" stroke-linejoin="round"/>
          <path d="M210 210L256 390L302 210L256 110Z" fill="#FDE68A" opacity="0.7"/>
          <path d="M380 140L392 165L417 177L392 189L380 214L368 189L343 177L368 165Z" fill="#FFFFFF"/>
          <path d="M120 310L130 330L150 340L130 350L120 370L110 350L90 340L110 330Z" fill="#FFFFFF"/>
        """
    },
    "insight-mining": {
        "color": "#7C3AED",
        "accent": "#C4B5FD",
        "bg_gradient": ("#8B5CF6", "#6D28D9"),
        "icon_svg": """
          <!-- Tension Mining Gem & Radiance -->
          <polygon points="256,120 370,195 325,365 187,365 142,195" fill="#DDD6FE" stroke="#FFFFFF" stroke-width="12" stroke-linejoin="round"/>
          <polygon points="256,170 320,215 295,320 217,320 192,215" fill="#6D28D9"/>
          <circle cx="256" cy="256" r="24" fill="#FBBF24"/>
          <path d="M256 80V105M400 170L380 185M370 400L350 380M142 400L162 380M112 170L132 185" stroke="#EDE9FE" stroke-width="10" stroke-linecap="round"/>
        """
    },
    "campaign-canon": {
        "color": "#B45309",
        "accent": "#FDE68A",
        "bg_gradient": ("#D97706", "#78350F"),
        "icon_svg": """
          <!-- Classical Trophy & Pillar Canon -->
          <path d="M150 380H362M170 340H342M190 340V180M256 340V180M322 340V180M160 180H352M140 140H372" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>
          <polygon points="256,75 272,112 312,115 281,141 291,180 256,158 221,180 231,141 200,115 240,112" fill="#FDE68A" stroke="#FFFFFF" stroke-width="6"/>
        """
    },
    "brand-activation": {
        "color": "#DC2626",
        "accent": "#FCA5A5",
        "bg_gradient": ("#EF4444", "#B91C1C"),
        "icon_svg": """
          <!-- Megaphone & Stunt Signal Wave -->
          <path d="M150 210H200L290 140V372L200 302H150C136 302 125 291 125 277V235C125 221 136 210 150 210Z" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="8"/>
          <path d="M175 302V365C175 376 184 385 195 385C206 385 215 376 215 365V302" fill="#FFFFFF"/>
          <path d="M335 190C360 210 375 235 375 256C375 277 360 302 335 322" stroke="#FEF08A" stroke-width="18" stroke-linecap="round" fill="none"/>
          <path d="M375 145C415 180 435 215 435 256C435 297 415 332 375 367" stroke="#FFFFFF" stroke-width="16" stroke-linecap="round" fill="none"/>
        """
    },
    "visual-storytelling": {
        "color": "#EA580C",
        "accent": "#FED7AA",
        "bg_gradient": ("#F97316", "#C2410C"),
        "icon_svg": """
          <!-- Narrative Arc & Open Story Scroll -->
          <path d="M120 340C180 340 220 180 280 180C340 180 360 300 410 300" stroke="#FFFFFF" stroke-width="20" stroke-linecap="round" fill="none"/>
          <circle cx="120" cy="340" r="20" fill="#FEF08A"/>
          <circle cx="280" cy="180" r="28" fill="#FFFFFF"/>
          <circle cx="410" cy="300" r="20" fill="#FEF08A"/>
          <path d="M256 130L266 150L286 160L266 170L256 190L246 170L226 160L246 150Z" fill="#FFFFFF"/>
          <path d="M150 370H370" stroke="#FED7AA" stroke-width="10" stroke-linecap="round" stroke-dasharray="16 12"/>
        """
    },
    "video-director": {
        "color": "#4F46E5",
        "accent": "#A5B4FC",
        "bg_gradient": ("#6366F1", "#3730A3"),
        "icon_svg": """
          <!-- Director Clapperboard & Motion Slate -->
          <path d="M120 190H392V365C392 376 383 385 372 385H140C129 385 120 376 120 365V190Z" fill="#1E1B4B" stroke="#FFFFFF" stroke-width="12"/>
          <polygon points="230,250 230,330 300,290" fill="#FBBF24"/>
          <!-- Slanted Clapper Top -->
          <g transform="rotate(-12 120 190)">
            <rect x="120" y="125" width="272" height="60" rx="10" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="6"/>
            <polygon points="150,125 180,125 140,185 110,185" fill="#4F46E5"/>
            <polygon points="210,125 240,125 200,185 170,185" fill="#4F46E5"/>
            <polygon points="270,125 300,125 260,185 230,185" fill="#4F46E5"/>
            <polygon points="330,125 360,125 320,185 290,185" fill="#4F46E5"/>
          </g>
        """
    },
    "image-director": {
        "color": "#C026D3",
        "accent": "#F0ABFC",
        "bg_gradient": ("#D946EF", "#A21CAF"),
        "icon_svg": """
          <!-- Multi-Panel Canvas Grid & Aperture -->
          <rect x="130" y="130" width="115" height="115" rx="16" fill="#FAE8FF" stroke="#FFFFFF" stroke-width="8"/>
          <rect x="267" y="130" width="115" height="115" rx="16" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="8"/>
          <rect x="130" y="267" width="115" height="115" rx="16" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="8"/>
          <rect x="267" y="267" width="115" height="115" rx="16" fill="#F5D0FE" stroke="#FFFFFF" stroke-width="8"/>
          <circle cx="256" cy="256" r="42" fill="#FDE047" stroke="#C026D3" stroke-width="8"/>
          <path d="M256 230V282M230 256H282" stroke="#701A75" stroke-width="8" stroke-linecap="round"/>
        """
    },
    "brand-intelligence": {
        "color": "#1D4ED8",
        "accent": "#93C5FD",
        "bg_gradient": ("#2563EB", "#1E40AF"),
        "icon_svg": """
          <!-- Brand Guardian Shield & Seal -->
          <path d="M256 110L370 160V260C370 335 320 385 256 410C192 385 142 335 142 260V160L256 110Z" fill="#1E3A8A" stroke="#FFFFFF" stroke-width="14" stroke-linejoin="round"/>
          <path d="M205 255L240 290L310 215" stroke="#60A5FA" stroke-width="20" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
        """
    },
    "taste-engine": {
        "color": "#9333EA",
        "accent": "#E9D5FF",
        "bg_gradient": ("#A855F7", "#7E22CE"),
        "icon_svg": """
          <!-- Swatch Fan & Synthesis Drop -->
          <path d="M256 120C256 120 180 230 180 290C180 332 214 366 256 366C298 366 332 332 332 290C332 230 256 120 256 120Z" fill="#FFFFFF"/>
          <path d="M256 210C256 210 210 270 210 300C210 325 230 345 256 345C282 345 302 325 302 300C302 270 256 210 256 210Z" fill="#F472B6"/>
          <circle cx="160" cy="180" r="22" fill="#FDE047"/>
          <circle cx="352" cy="180" r="22" fill="#38BDF8"/>
        """
    },
    "reference-memory": {
        "color": "#0D9488",
        "accent": "#99F6E4",
        "bg_gradient": ("#14B8A6", "#0F766E"),
        "icon_svg": """
          <!-- Memory Chip & Indexed REF Ribbon -->
          <rect x="150" y="150" width="212" height="212" rx="28" fill="#134E4A" stroke="#FFFFFF" stroke-width="12"/>
          <rect x="200" y="200" width="112" height="112" rx="16" fill="#5EEAD4"/>
          <path d="M210 115V150M256 115V150M302 115V150M210 362V397M256 362V397M302 362V397M115 210H150M115 256H150M115 302H150M362 210H397M362 256H397M362 302H397" stroke="#FFFFFF" stroke-width="10" stroke-linecap="round"/>
        """
    },
    "composition-director": {
        "color": "#0891B2",
        "accent": "#A5F3FC",
        "bg_gradient": ("#06B6D4", "#0E7490"),
        "icon_svg": """
          <!-- Golden Ratio & Alignment Grid -->
          <rect x="120" y="120" width="272" height="272" rx="20" fill="none" stroke="#FFFFFF" stroke-width="12"/>
          <path d="M210 120V392M302 120V392M120 210H392M120 302H392" stroke="#CFFAFE" stroke-width="6" stroke-dasharray="10 8"/>
          <circle cx="210" cy="210" r="14" fill="#FDE047"/>
          <circle cx="302" cy="210" r="14" fill="#FDE047"/>
          <circle cx="210" cy="302" r="14" fill="#FDE047"/>
          <circle cx="302" cy="302" r="14" fill="#FDE047"/>
        """
    },
    "typography-director": {
        "color": "#475569",
        "accent": "#CBD5E1",
        "bg_gradient": ("#64748B", "#334155"),
        "icon_svg": """
          <!-- Elegant Serif Letterform 'T' with Baseline Guides -->
          <path d="M110 135H402M110 377H402" stroke="#94A3B8" stroke-width="8" stroke-dasharray="14 10"/>
          <path d="M160 165H352V205H282V350H312V375H200V350H230V205H160V165Z" fill="#FFFFFF"/>
          <circle cx="352" cy="185" r="8" fill="#38BDF8"/>
          <circle cx="160" cy="185" r="8" fill="#38BDF8"/>
        """
    },
    "photography-director": {
        "color": "#C2410C",
        "accent": "#FFEDD5",
        "bg_gradient": ("#EA580C", "#9A3412"),
        "icon_svg": """
          <!-- Camera Aperture & 3-Point Light Rays -->
          <circle cx="256" cy="256" r="130" stroke="#FFFFFF" stroke-width="12" fill="#7C2D12"/>
          <polygon points="256,156 326,206 306,296 216,306 176,226" fill="#FB923C" stroke="#FFFFFF" stroke-width="6"/>
          <circle cx="256" cy="256" r="32" fill="#FEF08A"/>
          <path d="M125 125L165 165M387 125L347 165M256 80V120" stroke="#FDE047" stroke-width="12" stroke-linecap="round"/>
        """
    },
    "manipulation-director": {
        "color": "#059669",
        "accent": "#A7F3D0",
        "bg_gradient": ("#10B981", "#047857"),
        "icon_svg": """
          <!-- 3D Layer Compositing Planes -->
          <polygon points="256,120 375,180 256,240 137,180" fill="#D1FAE5" stroke="#FFFFFF" stroke-width="8" stroke-linejoin="round"/>
          <polygon points="256,190 375,250 256,310 137,250" fill="#34D399" stroke="#FFFFFF" stroke-width="8" stroke-linejoin="round"/>
          <polygon points="256,260 375,320 256,380 137,320" fill="#065F46" stroke="#FFFFFF" stroke-width="8" stroke-linejoin="round"/>
        """
    },
    "arabic-rtl-director": {
        "color": "#047857",
        "accent": "#6EE7B7",
        "bg_gradient": ("#059669", "#064E3B"),
        "icon_svg": """
          <!-- Arabic Diacritic / Calligraphic Nuqta & RTL Flow -->
          <path d="M370 230C350 160 270 160 220 200C170 240 140 310 200 350C260 390 340 350 360 280H160" stroke="#FFFFFF" stroke-width="16" stroke-linecap="round" fill="none"/>
          <!-- Calligraphic Diamond Nuqtas (Dots) -->
          <polygon points="280,120 305,145 280,170 255,145" fill="#FDE047"/>
          <polygon points="330,120 355,145 330,170 305,145" fill="#FDE047"/>
          <!-- RTL Directional Arrow -->
          <path d="M380 390H130M130 390L170 360M130 390L170 420" stroke="#FDE047" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
        """
    },
    "campaign-dna": {
        "color": "#E11D48",
        "accent": "#FECDD3",
        "bg_gradient": ("#F43F5E", "#BE123C"),
        "icon_svg": """
          <!-- Multi-Asset DNA Helix -->
          <path d="M160 140C220 200 292 312 352 372M352 140C292 200 220 312 160 372" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round"/>
          <path d="M185 165H327M210 215H302M235 256H277M210 297H302M185 347H327" stroke="#FDE047" stroke-width="10" stroke-linecap="round"/>
          <circle cx="160" cy="140" r="18" fill="#FFFFFF"/>
          <circle cx="352" cy="140" r="18" fill="#FDE047"/>
          <circle cx="160" cy="372" r="18" fill="#FDE047"/>
          <circle cx="352" cy="372" r="18" fill="#FFFFFF"/>
        """
    },
    "edit-sanitizer": {
        "color": "#F97316",
        "accent": "#FFEDD5",
        "bg_gradient": ("#FB923C", "#C2410C"),
        "icon_svg": """
          <!-- Inpainting Bounding-Box & Security Lock -->
          <rect x="135" y="135" width="242" height="242" rx="20" fill="none" stroke="#FFFFFF" stroke-width="12" stroke-dasharray="18 12"/>
          <rect x="120" y="120" width="30" height="30" fill="#FEF08A"/>
          <rect x="362" y="120" width="30" height="30" fill="#FEF08A"/>
          <rect x="120" y="362" width="30" height="30" fill="#FEF08A"/>
          <rect x="362" y="362" width="30" height="30" fill="#FEF08A"/>
          <!-- Central Padlock -->
          <rect x="216" y="240" width="80" height="65" rx="14" fill="#FFFFFF"/>
          <path d="M232 240V210C232 196 243 185 256 185C269 185 280 196 280 210V240" stroke="#FFFFFF" stroke-width="12" fill="none"/>
          <circle cx="256" cy="272" r="8" fill="#C2410C"/>
        """
    },
    "prompt-compiler": {
        "color": "#16A34A",
        "accent": "#BBF7D0",
        "bg_gradient": ("#22C55E", "#15803D"),
        "icon_svg": """
          <!-- Code Terminal Prompt & Compiler Nodes -->
          <rect x="120" y="140" width="272" height="232" rx="24" fill="#052E16" stroke="#FFFFFF" stroke-width="12"/>
          <path d="M170 210L220 256L170 302" stroke="#4ADE80" stroke-width="18" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
          <line x1="245" y1="302" x2="310" y2="302" stroke="#FEF08A" stroke-width="18" stroke-linecap="round"/>
          <circle cx="160" cy="172" r="8" fill="#EF4444"/>
          <circle cx="185" cy="172" r="8" fill="#F59E0B"/>
          <circle cx="210" cy="172" r="8" fill="#10B981"/>
        """
    },
    "visual-qa": {
        "color": "#831843",
        "accent": "#FBCFE8",
        "bg_gradient": ("#9D174D", "#500724"),
        "icon_svg": """
          <!-- Quality Gate Loupe & Release Seal -->
          <circle cx="236" cy="236" r="95" fill="#500724" stroke="#FFFFFF" stroke-width="14"/>
          <path d="M305 305L385 385" stroke="#FFFFFF" stroke-width="24" stroke-linecap="round"/>
          <path d="M195 235L225 265L285 200" stroke="#34D399" stroke-width="18" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
          <circle cx="340" cy="170" r="28" fill="#FDE047" stroke="#FFFFFF" stroke-width="6"/>
          <path d="M340 156V184M326 170H354" stroke="#831843" stroke-width="6" stroke-linecap="round"/>
        """
    }
}


def make_svg(size: int, design: dict) -> str:
    c1, c2 = design["bg_gradient"]
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 512 512" fill="none">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{c1}" />
      <stop offset="100%" stop-color="{c2}" />
    </linearGradient>
  </defs>
  <rect x="40" y="40" width="432" height="432" rx="92" fill="url(#bgGrad)" stroke="#FFFFFF" stroke-width="10"/>
  {design['icon_svg']}
</svg>
"""
    return svg


def update_skill(slug: str, design: dict):
    skill_dir = SKILLS_DIR / slug
    assets_dir = skill_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    
    # Write small & large SVGs
    (assets_dir / "small-logo.svg").write_text(make_svg(128, design), encoding="utf-8")
    (assets_dir / "large-logo.svg").write_text(make_svg(512, design), encoding="utf-8")
    
    # Update openai.yaml brand_color
    yaml_path = skill_dir / "agents/openai.yaml"
    if yaml_path.is_file():
        text = yaml_path.read_text(encoding="utf-8")
        text = re.sub(r'brand_color:\s*"#[0-9a-fA-F]{3,8}"', f'brand_color: "{design["color"]}"', text)
        yaml_path.write_text(text, encoding="utf-8")
    print(f"Updated {slug} with unique color {design['color']}")


def main():
    print(f"Generating unique logos and brand colors for {len(SKILL_DESIGNS)} skills...")
    for slug, design in SKILL_DESIGNS.items():
        update_skill(slug, design)
    print("\nAll 21 skill logos and brand colors successfully generated!")


if __name__ == "__main__":
    main()
