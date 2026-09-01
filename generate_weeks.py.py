SCHEDULE = {
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

WEEK1_MATCHUPS = [
    ("Catchy Football Name", "Donuts All Day 24/7"),
    ("Covfefe is for Closers", "Joydip's Scary Team"),
    ("AB's 3rd Quarter Uber", "Texas Determined Domination"),
    ("Kenz VishusLicks", "Herbert's Heros"),
    ("Lucas's Loud Team", "Nabers ate my Zombies"),
]

def generate_html_files():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            template = f.read()
    except FileNotFoundError:
        print("Error: index.html not found.")
        return

    preview_start_marker = "<h2>This Week's Preview</h2>"
    preview_end_marker = '<div class="ffn-section">\n    <h2>League Business</h2>'

    p_start = template.find(preview_start_marker)
    p_end = template.find(preview_end_marker)

    if -1 in (p_start, p_end):
        print("Error: Could not locate preview markers in index.html.")
        return

    for week in range(2, 15):
        # Update title and header text for current week
        content = template.replace("Week 1", f"Week {week}")

        # Ensure Week 1 option in dropdown explicitly links to index.html and is unselected
        content = content.replace(
            '<option value="index.html" selected>Week 1</option>',
            '<option value="index.html">Week 1</option>'
        )
        
        # Select current week in dropdown
        target_opt = f'<option value="week{week}.html">'
        content = content.replace(target_opt, f'<option value="week{week}.html" selected>')

        # --- 1. BUILD RECAP & AWARDS BLOCKS ---
        prev_week = week - 1
        prev_matchups = WEEK1_MATCHUPS if prev_week == 1 else SCHEDULE[prev_week]

        recap_and_awards_html = f'''<div class="ffn-section">
    <h2>Last Week's Recap</h2>
    <p class="sub">Here's what happened while you were pretending to work</p>\n\n'''
        
        for away, home in prev_matchups:
            recap_and_awards_html += f'''    <div class="ffn-matchup">
      <div class="score"><span class="win">{away} [Score]</span> — <span class="lose">[Score] {home}</span></div>
      <p>[Recap of Week {prev_week} game]</p>
      <span class="ffn-gif">[GIF: search a reaction fitting this game's outcome]</span>
    </div>\n\n'''
        
        recap_and_awards_html = recap_and_awards_html.rstrip() + '''\n  </div>\n\n  <div class="ffn-section">
    <h2>Weekly Awards</h2>
    <ul class="ffn-awards">
      <li><span class="tag">🚽 Toilet Bowl MVP:</span>[Manager who lost despite highest bench points]</li>
      <li><span class="tag">🧠 Big Brain Move:</span>[Best waiver pickup or start/sit call]</li>
      <li><span class="tag">🤡 Clown of the Week:</span>[Worst decision — started a bye week guy, etc.]</li>
      <li><span class="tag">💰 Should've Bet On It:</span>[Biggest blowout]</li>
      <li><span class="tag">😰 Heartbreak Hotel:</span>[Closest loss]</li>
    </ul>
  </div>\n\n  '''

        # --- 2. BUILD THIS WEEK'S PREVIEW BLOCK ---
        preview_html = '''<h2>This Week's Preview</h2>\n    <p class="sub">Predictions nobody asked for, delivered anyway</p>\n\n'''
        for away, home in SCHEDULE[week]:
            preview_html += f'''    <div class="ffn-matchup">
      <div class="score">{away} <span style="color:var(--ink-dim)">vs</span> {home}</div>
      <p><strong>Projected:</strong> [{away} proj] – [{home} proj]<br>[Preview]</p>
      <span class="ffn-gif">[GIF: search a reaction fitting the storyline]</span>
    </div>\n\n'''
        preview_html = preview_html.rstrip()

        # Insert Recap & Awards before Preview, then replace Preview content
        p_start_current = content.find(preview_start_marker)
        preview_block_start = content.rfind('<div class="ffn-section">', 0, p_start_current)

        final_content = (
            content[:preview_block_start]
            + recap_and_awards_html
            + '<div class="ffn-section">\n    '
            + preview_html
            + '\n  </div>\n\n  '
            + content[p_end:]
        )

        filename = f"week{week}.html"
        with open(filename, "w", encoding="utf-8") as out:
            out.write(final_content)
        print(f"Generated: {filename}")

if __name__ == "__main__":
    generate_html_files()