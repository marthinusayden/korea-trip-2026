import urllib.request
import re
import os
import ssl

def check_url(url):
    print(f"\nFetching {url}...")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36'}
    
    # Disable SSL verification
    ctx = ssl._create_unverified_context()
    
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
            # Find all img src urls
            img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
            print(f"Found {len(img_srcs)} img tags.")
            for src in img_srcs:
                if any(k in src.lower() for k in ['logo', 'brand', 'symbol', 'wordmark', 'main']):
                    print(f"Candidate img src: {src}")
            
            # Find all svg tag classes/ids
            svgs = re.findall(r'<svg([^>]+)>', html)
            print(f"Found {len(svgs)} svg tags.")
            for i, svg in enumerate(svgs[:10]):
                print(f"SVG #{i}: {svg.strip()}")
                
            # Print a snippet of header HTML if possible to manually inspect
            header_match = re.search(r'<header[^>]*>(.*?)</header>', html, re.DOTALL | re.IGNORECASE)
            if header_match:
                print("\nHeader Snippet:")
                print(header_match.group(1)[:1500] + "...")
            else:
                # print first 1000 chars of body
                print("\nNo header tag found. First 1000 chars of html:")
                print(html[:1000] + "...")
    except Exception as e:
        print(f"Error checking {url}: {e}")

print("Checking Nomanual:")
check_url("https://nomanual-official.com/collection/")
print("\nChecking Wooyoungmi:")
check_url("https://www.wooyoungmi.com/index.html")
