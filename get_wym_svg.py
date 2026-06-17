import urllib.request
import re
import os
import ssl

def extract_svgs(url, dest_dir):
    print(f"Fetching {url}...")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36'}
    ctx = ssl._create_unverified_context()
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
            # Find all SVG tags and their contents
            svg_matches = re.finditer(r'(<svg[^>]*>.*?</svg>)', html, re.DOTALL | re.IGNORECASE)
            
            os.makedirs(dest_dir, exist_ok=True)
            
            count = 0
            for i, match in enumerate(svg_matches):
                svg_content = match.group(1)
                # Let's check if it's the logo
                if 'viewbox="0 0 371 65.4"' in svg_content.lower() or 'wooyoungmi' in svg_content.lower() or count < 5:
                    file_path = os.path.join(dest_dir, f"wooyoungmi_logo_{count}.svg")
                    with open(file_path, 'w') as f:
                        f.write(svg_content)
                    print(f"Saved SVG #{i} to {file_path}")
                    count += 1
    except Exception as e:
        print(f"Error: {e}")

dest = "/Users/aydenmarthinus/Desktop/korea-trip-2026/images"
extract_svgs("https://www.wooyoungmi.com/index.html", dest)
