import re

# Matchup data extracted directly from your schedule screenshots
SCHEDULE = {
    1: [
        ("Catchy Football Name", "Donuts All Day 24/7"),
        ("Covfefe is for Closers", "Joydip's Scary Team"),
        ("AB's 3rd Quarter Uber", "Texas Determined Domination"),
        ("Kenz VishusLicks", "Herbert's Heros"),
        ("Lucas's Loud Team", "Nabers ate my Zombies"),
    ],
    2: [
        ("Donuts All Day 24/7", "Covfefe is for Closers"),
        ("Nabers ate my Zombies", "Joydip's Scary Team"),
        ("AB's 3rd Quarter Uber", "Catchy Football Name"),
        ("Herbert's Heros", "Lucas's Loud Team"),
        ("Kenz VishusLicks", "Texas Determined Domination"),
    ],
    3: [
        ("Catchy Football Name", "Nabers ate my Zombies"),
        ("Covfefe is for Closers", "Herbert's Heros"),
        ("Texas Determined Domination", "Donuts All Day 24/7"),
        ("AB's 3rd Quarter Uber", "Kenz VishusLicks"),
        ("Joydip's Scary Team", "Lucas's Loud Team"),
    ],
    4: [
        ("Nabers ate my Zombies", "Covfefe is for Closers"),
        ("AB's 3rd Quarter Uber", "Donuts All Day 24/7"),
        ("Texas Determined Domination", "Lucas's Loud Team"),
        ("Catchy Football Name", "Kenz VishusLicks"),
        ("Herbert's Heros", "Joydip's Scary Team"),
    ],
    5: [
        ("Lucas's Loud Team", "Covfefe is for Closers"),
        ("Kenz VishusLicks", "Donuts All Day 24/7"),
        ("Texas Determined Domination", "Catchy Football Name"),
        ("Joydip's Scary Team", "AB's 3rd Quarter Uber"),
        ("Nabers ate my Zombies", "Herbert's Heros"),
    ],
    6: [
        ("Donuts All Day 24/7", "Lucas's Loud Team"),
        ("Kenz VishusLicks", "Nabers ate my Zombies"),
        ("Herbert's Heros", "Texas Determined Domination"),
        ("Covfefe is for Closers", "AB's 3rd Quarter Uber"),
        ("Joydip's Scary Team", "Catchy Football Name"),
    ],
    7: [
        ("Catchy Football Name", "Herbert's Heros"),
        ("Lucas's Loud Team", "Kenz VishusLicks"),
        ("Texas Determined Domination", "Covfefe is for Closers"),
        ("Joydip's Scary Team", "Donuts All Day 24/7"),
        ("AB's 3rd Quarter Uber", "Nabers ate my Zombies"),
    ],
    8: [
        ("Joydip's Scary Team", "Texas Determined Domination"),
        ("AB's 3rd Quarter Uber", "Herbert's Heros"),
        ("Lucas's Loud Team", "Catchy Football Name"),
        ("Covfefe is for Closers", "Kenz VishusLicks"),
        ("Nabers ate my Zombies", "Donuts All Day 24/7"),
    ],
    9: [
        ("Kenz VishusLicks", "Joydip's Scary Team"),
        ("Lucas's Loud Team", "AB's 3rd Quarter Uber"),
        ("Covfefe is for Closers", "Catchy Football Name"),
        ("Texas Determined Domination", "Nabers ate my Zombies"),
        ("Herbert's Heros", "Donuts All Day 24/7"),
    ],
    10: [
        ("Donuts All Day 24/7", "Kenz VishusLicks"),
        ("AB's 3rd Quarter Uber", "Joydip's Scary Team"),
        ("Nabers ate my Zombies", "Lucas's Loud Team"),
        ("Herbert's Heros", "Covfefe is for Closers"),
        ("Catchy Football Name", "Texas Determined Domination"),
    ],
    11: [
        ("Texas Determined Domination", "AB's 3rd Quarter Uber"),
        ("Herbert's Heros", "Nabers ate my Zombies"),
        ("Kenz VishusLicks", "Catchy Football Name"),
        ("Lucas's Loud Team", "Joydip's Scary Team"),
        ("Covfefe is for Closers", "Donuts All Day 24/7"),
    ],
    12: [
        ("Herbert's Heros", "Catchy Football Name"),
        ("Covfefe is for Closers", "Lucas's Loud Team"),
        ("Joydip's Scary Team", "Nabers ate my Zombies"),
        ("Texas Determined Domination", "Kenz VishusLicks"),
        ("Donuts All Day 24/7", "AB's 3rd Quarter Uber"),
    ],
    13: [
        ("Donuts All Day 24/7", "Catchy Football Name"),
        ("Kenz VishusLicks", "AB's 3rd Quarter Uber"),
        ("Lucas's Loud Team", "Texas Determined Domination"),
        ("Covfefe is for Closers", "Nabers ate my Zombies"),
        ("Joydip's Scary Team", "Herbert's Heros"),
    ],
    14: [
        ("Joydip's Scary Team", "Covfefe is for Closers"),
        ("Donuts All Day 24/7", "Texas Determined Domination"),
        ("Nabers ate my Zombies", "Kenz VishusLicks"),
        ("Catchy Football Name", "AB's 3rd Quarter Uber"),
        ("Lucas's Loud Team", "Herbert's Heros"),
    ]
}

def generate_html_files():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            template = f.read()
    except FileNotFoundError:
        print("Error: index.html not found in the current directory.")
        return

    for week, matchups in SCHEDULE.items():
        content = template
        
        # Update Week Headers & Titles
        content = content.replace("<title>[LEAGUE NAME] Weekly Debrief — Week [X]</title>", f"<title>[LEAGUE NAME] Weekly Debrief — Week {week}</title>")
        content = content.replace('<div class="ffn-band">[League Name] · Week [X] Debrief</div>', f'<div class="ffn-band">[League Name] · Week {week} Debrief</div>')
        
        # Select active option in dropdown
        target_option = f'<option value="week{week}.html">'
        content = content.replace(target_option, f'<option value="week{week}.html" selected>')

        # Populate "This Week's Preview" Matchups
        # Replaces the 5 dummy matchup blocks in preview section
        preview_blocks = []
        for away, home in matchups:
            block = f'''    <div class="ffn-matchup">
      <div class="score">{away} <span style="color:var(--ink-dim)">vs</span> {home}</div>
      <p><strong>Projected:</strong> [{away} proj] – [{home} proj]<br>[Preview]</p>
      <span class="ffn-gif">[GIF: search a reaction fitting the storyline]</span>
    </div>'''
            preview_blocks.append(block)

        # Replace preview section content
        preview_pattern = re.compile(r'(<h2>This Week\'s Preview</h2>\s*<p class="sub">[^<]*</p>\s*)(.*?)(?=\s*<div class="ffn-section">\s*<h2>League Business</h2>)', re.DOTALL)
        new_preview_content = r'\1' + '\n\n'.join(preview_blocks) + '\n  '
        content = preview_pattern.sub(new_preview_content, content)

        # Write out to weekX.html
        filename = f"week{week}.html"
        with open(filename, "w", encoding="utf-8") as out:
            out.write(content)
        print(f"Created: {filename}")

if __name__ == "__main__":
    generate_html_files()