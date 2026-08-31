# utils/text_formatter.py

def format_lyrics(raw_text):
    """
    Takes a raw quote or poem and formats it with song tags 
    to guide the AI music model.
    """
    # Clean up whitespace
    clean_text = raw_text.strip()
    
    # If the text is very short, treat it as a single chorus
    if len(clean_text.split()) < 15:
        return f"[Chorus]\n{clean_text}"
    
    # Otherwise, split it into a verse and chorus structure
    lines = clean_text.split('\n')
    formatted_lyrics = "[Verse]\n"
    
    # Just a simple logic: split halfway through for Verse/Chorus
    midpoint = len(lines) // 2
    
    for i, line in enumerate(lines):
        if i == midpoint and midpoint > 0:
            formatted_lyrics += "\n[Chorus]\n"
        formatted_lyrics += f"{line}\n"
        
    return formatted_lyrics.strip()
