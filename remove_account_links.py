#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from pathlib import Path

def clean_account_links(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Remove "Мои покупки" buttons
        content = re.sub(r'<a class="button-secondary" href="[^"]*myorders\.html[^"]*">\s*<span class="button">Мои покупки</span>\s*</a>', '', content)
        content = re.sub(r'<a class="button-secondary" href="[^"]*myorders\.html[^"]*">\s*<span class="button">Мои покупки</span>\s*</a>', '', content)
        
        # Remove "Личный кабинет клиента" links
        content = re.sub(r'<li><a href="[^"]*lichnyy-kabinet-klienta\.html[^"]*">Личный кабинет клиента</a></li>', '', content)
        
        # Remove any remaining myorders links
        content = re.sub(r'href="[^"]*myorders\.html[^"]*"', '', content)
        content = re.sub(r'href="[^"]*lichnyy-kabinet-klienta\.html[^"]*"', '', content)
        
        # Clean up empty list items
        content = re.sub(r'<li>\s*</li>', '', content)
        content = re.sub(r'<li>\s*<a[^>]*>\s*</a>\s*</li>', '', content)
        
        # Remove empty control--mybuy divs (entire sections)
        content = re.sub(r'<div class="header__control control--mybuy">[^<]*(?:<!--[^>]*>)?[^<]*(?:[^<]|<(?!\s*/?div))*(?:</div>)?', '', content, flags=re.DOTALL)
        # Try multiline version to handle commented sections
        content = re.sub(r'<div class="header__control control--mybuy">.*?</div>', '', content, flags=re.DOTALL)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    base_dir = Path('.')
    html_files = list(base_dir.rglob('*.html')) + list(base_dir.rglob('*.htm'))
    html_files = [f for f in html_files if 'remove_account' not in str(f) and 'webcopy-origin' not in str(f)]
    
    processed = 0
    for filepath in html_files:
        if clean_account_links(filepath):
            processed += 1
    
    print(f"Processed {processed} files", flush=True)

if __name__ == '__main__':
    main()
