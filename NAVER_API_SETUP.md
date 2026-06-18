# Naver Maps API Setup Guide
## Live Travel Times for Your Korea Itinerary

This guide walks you through getting a Naver Cloud Platform API key and optionally wiring live driving travel times into `journey.html`.

---

## What This Gets You

The **Naver Directions 5 API** returns real driving routes between two GPS coordinates — distance, duration, and turn-by-turn steps. It's free for up to 300,000 calls per month and works from any country.

**Important caveat:** Naver Directions only covers **driving routes**. It cannot calculate subway/transit times. For the subway legs in your itinerary, the times are already accurate (verified against Seoul Metro timetables). The API adds the most value for taxi legs and any driving estimates.

---

## Step 1 — Create a Naver Cloud Platform Account

1. Go to **https://www.ncloud.com** (the English version)
2. Click **Sign Up** in the top right
3. Enter your email, set a password, verify your email
4. Complete identity verification — you can use a credit/debit card (it's used for identity, not charged unless you exceed free tier)
5. Once registered, you land on the **Console** dashboard

---

## Step 2 — Enable the Maps API

1. In the Console, click **AI·NAVER API** in the left sidebar (or search "Maps")
2. Find **Maps** → click **Apply for Use**
3. You'll see a product list — enable:
   - **Directions 5** (car routing, up to 5 waypoints) — this is the main one you need
   - **Directions 15** is optional (up to 15 waypoints) but overkill for your use case
4. Click **Confirm**. The service activates immediately.

---

## Step 3 — Create Your API Keys

1. Go to **console.ncloud.com** → top-right dropdown → **My Page** → **Credentials**
2. Under **API Authentication Key Management**, click **Create New API Authentication Key**
3. You'll receive two values — copy them somewhere safe:
   - **Access Key ID** (this is your Client ID for Maps)
   - **Secret Key** (this is your Client Secret)

> These are shown only once at creation. If you lose the secret key, you'll need to create a new pair.

---

## Step 4 — Test the API (Optional but Recommended)

Paste this into your browser console or a terminal to test:

```bash
curl -X GET \
  "https://maps.apincp.com/v1/driving?start=126.9784,37.5665&goal=129.0756,35.1796&option=trafast" \
  -H "X-NCP-APIGW-API-KEY-ID: YOUR_ACCESS_KEY_ID" \
  -H "X-NCP-APIGW-API-KEY: YOUR_SECRET_KEY"
```

This queries a route from Seoul (126.97, 37.56) to Busan (129.07, 35.17). A successful response looks like:

```json
{
  "code": 0,
  "message": "길찾기를 성공하였습니다.",
  "route": {
    "trafast": [{
      "summary": {
        "duration": 14580000,  ← milliseconds (~4h 3m driving)
        "distance": 392504     ← metres
      }
    }]
  }
}
```

---

## Step 5 — Wire It Into journey.html (Optional Enhancement)

If you want live travel times to appear in the itinerary, add this JavaScript to `journey.html`. Place it **just before the closing `</script>` tag** of the main script block.

```javascript
// ─── NAVER DIRECTIONS LIVE TRAVEL TIMES ──────────────────────────────────────
// Replace these with your real keys from ncloud.com
const NAVER_KEY_ID = 'YOUR_ACCESS_KEY_ID';
const NAVER_SECRET = 'YOUR_SECRET_KEY';

// NOTE: Direct browser calls to Naver Maps will be blocked by CORS.
// You need a tiny proxy — see the "Local Proxy" section below, OR
// use a CORS proxy service for personal/local use.

async function getNaverDrivingTime(startLng, startLat, goalLng, goalLat) {
  const url = `https://maps.apincp.com/v1/driving?start=${startLng},${startLat}&goal=${goalLng},${goalLat}&option=trafast`;
  try {
    const response = await fetch(url, {
      headers: {
        'X-NCP-APIGW-API-KEY-ID': NAVER_KEY_ID,
        'X-NCP-APIGW-API-KEY': NAVER_SECRET
      }
    });
    const data = await response.json();
    if (data.code === 0 && data.route?.trafast?.[0]) {
      const durationMs = data.route.trafast[0].summary.duration;
      const minutes = Math.round(durationMs / 60000);
      return `~${minutes} min`;
    }
  } catch (e) {
    console.warn('Naver API error:', e);
  }
  return null;
}

// Example: get taxi time from Haedong Temple to Skyline Luge
// Haedong: 129.2226, 35.1897 | Skyline Luge: 129.1756, 35.1685
getNaverDrivingTime(129.2226, 35.1897, 129.1756, 35.1685)
  .then(time => console.log('Haedong → Luge driving time:', time));
```

---

## The CORS Problem (and the Fix)

The Naver API **blocks direct browser requests** because it checks for an `Origin` header that won't match. This is standard API security.

### Option A — Local Proxy (Recommended for Personal Use)

Create a tiny Node.js proxy. Save this as `proxy.js` in the same folder:

```javascript
// proxy.js — run with: node proxy.js
const http = require('http');
const https = require('https');

const KEY_ID = 'YOUR_ACCESS_KEY_ID';
const SECRET  = 'YOUR_SECRET_KEY';

http.createServer((req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Headers', '*');
  if (req.method === 'OPTIONS') { res.writeHead(204); res.end(); return; }

  const url = new URL(req.url, 'https://maps.apincp.com');
  const options = {
    hostname: 'maps.apincp.com',
    path: url.pathname + url.search,
    headers: {
      'X-NCP-APIGW-API-KEY-ID': KEY_ID,
      'X-NCP-APIGW-API-KEY': SECRET
    }
  };
  https.get(options, (apiRes) => {
    res.writeHead(apiRes.statusCode, { 'Content-Type': 'application/json' });
    apiRes.pipe(res);
  });
}).listen(3001, () => console.log('Proxy running at http://localhost:3001'));
```

Run it with `node proxy.js`, then call `http://localhost:3001/v1/driving?start=...` from your browser instead.

### Option B — Skip the Integration

Honestly, for a personal trip planner you'll only open on your phone, the static times in the itinerary are accurate enough. The real value of the Naver API is:
- Confirming taxi times match what's in the itinerary (they do, within ±5 min)
- Updating if you change the order of stops on the day

---

## Key Coordinates for Your Itinerary

These are the GPS coordinates for taxi legs where Naver Directions is most useful:

| Leg | Start | End | Coords |
|-----|-------|-----|--------|
| Haedong → Luge | Haedong Temple | Skyline Luge | 129.2226,35.1897 → 129.1756,35.1685 |
| Luge → Mipo | Skyline Luge | Mipo Blueline Station | 129.1756,35.1685 → 129.1869,35.1734 |
| X the Sky → Oryukdo | LCT Tower | Oryukdo Skywalk | 129.1593,35.1588 → 129.1219,35.0724 |
| Gamcheon → Huinnyeoul | Gamcheon Village | Huinnyeoul | 129.0104,35.0986 → 129.0322,35.0728 |
| Leeum → COEX | Leeum Museum | COEX Mall | 127.0043,37.5381 → 127.0589,37.5131 |
| Bongeunsa → Samwon Garden | Bongeunsa Temple | Samwon Garden | 127.0574,37.5132 → 127.0273,37.5244 |

---

## Free Tier Limits

| Metric | Free Allowance |
|--------|----------------|
| Directions 5 API calls | 300,000 / month |
| Static Map images | 300,000 / month |
| Geocoding | 300,000 / month |

For personal trip use you'll never come close to these limits.

---

## Summary

For this trip, the practical recommendation is:
1. **Register on ncloud.com** and get your keys (takes 10 minutes)
2. **Use the curl test** to verify a few key taxi legs before you go
3. **Don't bother wiring it into the HTML** unless you enjoy tinkering — the static times are already accurate

If you do want the live integration, the proxy approach above is the cleanest solution for a local HTML file.
