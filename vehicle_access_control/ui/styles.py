# ui/styles.py
COLORS = {
    "background": "#20232a",  # Slightly lighter dark background
    "primary": "#61dafb",     # Light blue
    "success": "#28a745",     # Green
    "danger": "#dc3545",      # Red
    "text": "#f8f9fa",        # White
    "accent": "#ff9800"       # Orange
}

FONTS = {
    "title": ("Helvetica", 18, "bold"),
    "body": ("Arial", 14),
    "status": ("Arial", 12, "italic")
}

STYLES = {
    "button": {
        "bg": COLORS["primary"],
        "fg": COLORS["text"],
        "activebackground": COLORS["accent"],
        "borderwidth": 0,
        "font": FONTS["body"],
        "padx": 15,
        "pady": 7
    },
    "label": {
        "bg": COLORS["background"],
        "fg": COLORS["text"],
        "font": FONTS["body"]
    }
}
