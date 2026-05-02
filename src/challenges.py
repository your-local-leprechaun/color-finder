import random
from datetime import date, timedelta

# Curated colors: (prompt_name, hex)
COLORS = [
    ("Coral",           "#FF6B6B"),
    ("Ocean Blue",      "#1A6CA8"),
    ("Forest Green",    "#228B22"),
    ("Sunset Orange",   "#FF4500"),
    ("Lavender",        "#9B7EBD"),
    ("Golden Yellow",   "#FFD700"),
    ("Slate Gray",      "#708090"),
    ("Hot Pink",        "#FF69B4"),
    ("Turquoise",       "#40E0D0"),
    ("Burnt Sienna",    "#E97451"),
    ("Midnight Blue",   "#191970"),
    ("Lime Green",      "#32CD32"),
    ("Crimson",         "#DC143C"),
    ("Peach",           "#FFBE98"),
    ("Steel Blue",      "#4682B4"),
    ("Olive",           "#808000"),
    ("Magenta",         "#FF00FF"),
    ("Teal",            "#008080"),
    ("Amber",           "#FFBF00"),
    ("Indigo",          "#4B0082"),
    ("Salmon",          "#FA8072"),
    ("Chartreuse",      "#7FFF00"),
    ("Rust",            "#B7410E"),
    ("Sky Blue",        "#87CEEB"),
    ("Plum",            "#8E4585"),
    ("Mint",            "#98FF98"),
    ("Copper",          "#B87333"),
    ("Periwinkle",      "#CCCCFF"),
    ("Terracotta",      "#C1440E"),
    ("Sage",            "#8FAF7E"),
    ("Marigold",        "#EAA220"),
    ("Dusty Rose",      "#C4A0A0"),
    ("Cobalt",          "#0047AB"),
    ("Tangerine",       "#F28500"),
    ("Cream",           "#FFFDD0"),
    ("Burgundy",        "#800020"),
    ("Seafoam",         "#93E9BE"),
    ("Mustard",         "#FFDB58"),
    ("Lilac",           "#C8A2C8"),
    ("Mahogany",        "#C04000"),
    ("Jade",            "#00A86B"),
    ("Blush",           "#DE5D83"),
    ("Denim",           "#1560BD"),
    ("Ochre",           "#CC7722"),
    ("Moss",            "#8A9A5B"),
    ("Fuchsia",         "#FF00BF"),
    ("Caramel",         "#C68642"),
    ("Powder Blue",     "#B0E0E6"),
    ("Brick Red",       "#CB4154"),
    ("Pine",            "#01796F"),
]

PROMPTS = [
    "Find something {}",
    "Spot something {}",
    "Hunt down something {}",
    "Show us something {}",
    "Capture something {}",
]


def generate_challenge(for_date: date) -> dict:
    """Deterministically pick a color for a given date — same result for all users."""
    seed = int(for_date.strftime("%Y%m%d"))
    rng = random.Random(seed)
    name, hex_color = rng.choice(COLORS)
    prompt_template = rng.choice(PROMPTS)
    return {
        "prompt": prompt_template.format(name),
        "color_hex": hex_color,
        "date": for_date.isoformat(),
    }


def two_days_ago(for_date: date) -> str:
    return (for_date - timedelta(days=2)).isoformat()
