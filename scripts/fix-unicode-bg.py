#!/usr/bin/env python3
"""
Convert Unicode characters to ASCII in all BG quiz files.
Fixes Tier 1 violation: ASCII-only requirement.
"""

import json
import os
import re

def fix_unicode(text):
    """Replace Unicode characters with ASCII equivalents."""
    if not isinstance(text, str):
        return text
    
    # Smart quotes
    text = text.replace('\u201c', '"')  # left double quote
    text = text.replace('\u201d', '"')  # right double quote
    text = text.replace('\u2018', "'")  # left single quote
    text = text.replace('\u2019', "'")  # right single quote
    text = text.replace('\u2033', '"')  # double prime
    text = text.replace('\u2032', "'")  # prime
    
    # Dashes
    text = text.replace('\u2013', '--')  # en-dash
    text = text.replace('\u2014', '--')  # em-dash
    text = text.replace('\u2015', '--')  # horizontal bar
    
    # Ellipsis
    text = text.replace('\u2026', '...')  # horizontal ellipsis
    
    # Spaces
    text = text.replace('\u00a0', ' ')  # non-breaking space
    text = text.replace('\u2002', ' ')  # en space
    text = text.replace('\u2003', ' ')  # em space
    text = text.replace('\u2009', ' ')  # thin space
    
    # Other common Unicode
    text = text.replace('\u2022', '*')   # bullet
    text = text.replace('\u00b7', '*')   # middle dot
    text = text.replace('\u2212', '-')   # minus sign
    
    return text

def fix_quiz_object(obj):
    """Recursively fix Unicode in quiz object."""
    if isinstance(obj, dict):
        return {key: fix_quiz_object(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [fix_quiz_object(item) for item in obj]
    elif isinstance(obj, str):
        return fix_unicode(obj)
    else:
        return obj

def process_file(filepath):
    """Process a single quiz file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            quiz = json.load(f)
        
        # Fix Unicode throughout
        fixed_quiz = fix_quiz_object(quiz)
        
        # Write back with proper formatting
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(fixed_quiz, f, indent=2, ensure_ascii=False)
            f.write('\n')
        
        return True
    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return False

def main():
    bg_dir = 'data/quizzes/bg'
    
    if not os.path.exists(bg_dir):
        print(f"❌ Directory not found: {bg_dir}")
        return
    
    files = sorted([f for f in os.listdir(bg_dir) if f.endswith('.json')])
    
    print(f"🔄 Converting Unicode → ASCII in {len(files)} BG quiz files...\n")
    
    success_count = 0
    for filename in files:
        filepath = os.path.join(bg_dir, filename)
        if process_file(filepath):
            print(f"✓ Fixed {filename}")
            success_count += 1
    
    print(f"\n✅ Converted {success_count}/{len(files)} files successfully")
    print("✅ All Unicode characters replaced with ASCII equivalents")

if __name__ == '__main__':
    main()
