# Korea 2026 Trip Planner — Full Project Handoff

> **For the next agent:** This document is the complete record of everything built in this project. Read the entire document before touching any files. The project is a multi-page static HTML/CSS/JS travel planning application. No frameworks, no build tools, no npm. Everything is vanilla.

---

## Project Location

```
/Users/aydenmarthinus/Desktop/korea-trip-2026/
├── index.html          # Brochure — destination guide
├── itinerary.html      # Full Itinerary — day planner with drag UI
├── menu.html           # The Menu — food / activities / shopping hub
├── data.js             # ★ SHARED DATA — single source of truth for ALL menu/planner items
└── images/             # Brochure-style PNG illustrations (AI-generated)
    ├── ahyeon_cathedral.png
    ├── diamond_bay_yacht.png
    ├── gamcheon_village.png
    ├── gyeongbokgung_seoul.png
    ├── han_river_picnic.png
    ├── hanbok_palace.png
    ├── kbo_baseball_stadium.png
    ├── lol_park.png
    ├── noraebang.png
    ├── nseoul_tower.png
    ├── oryukdo_busan.png
    ├── secret_garden_pond.png
    ├── sky_capsule.png
    ├── starfield_library.png
    └── tongin_market_lunch.png
```
> [!IMPORTANT]
> **Decision Registry**: A complete table of all removed or rescheduled places, including their IDs, original times, trade-off friction profiles, and specific reasons for removal can be reviewed in:
> 👉 [removed_places_registry.md](file:///Users/aydenmarthinus/.gemini/antigravity-cli/brain/45f0c4f5-67a1-4a75-8da4-059641789c53/removed_places_registry.md)
> ## ⚡ DAY 12 PACING & DEPARTURE OPTIMIZATION (19 Jun 2026) — READ FIRST
>
> An audit of Day 12 (Museums, Gangnam & Departure) was performed to resolve scheduling gaps and optimize airport transit:
>
> - **Reinstated Farewell Dinner**: Re-added the premium celebratory K-BBQ dinner at Samwon Garden (Apgujeong, Gangnam) between 17:15 and 18:45, filling a 3-hour evening gap and matching the brochure's original farewell dinner promise.
> - **Optimized Airport Travel**: Moved the departure from Seodaemun slightly earlier to 19:30, arriving at Incheon T2 by 20:45 for a relaxed 3.5-hour pre-flight buffer (ET673 departs 00:20).
>
> ## ⚡ DAY 11 PACING & GEOGRAPHIC FLOW OPTIMIZATION (19 Jun 2026) — READ FIRST
>
> An audit of Day 11 (Jongno, Cinema & Baseball) was performed to resolve travel fatigue, stadium timing collisions, and closing hours:
>
> - **Resolved 4-Cross Han River Travel Yoyo**: Reordered the day so that all afternoon activities (Eunpyeong Hanok Village $\rightarrow$ Imun Seolnongtang lunch $\rightarrow$ Namdaemun Market $\rightarrow$ CGV Cinema in Yongsan) remain north of the river. You now cross the Han River *only once* in the evening to attend the baseball game in Jamsil, minimizing transit fatigue.
> - **Fixed Baseball Stadium Game Start Collision**: Moved the CGV Premium Cinema slot earlier (**14:45–17:00**) so that you can cross the river and arrive at Jamsil Baseball Stadium by **17:45** (45 minutes before the 18:30 KBO game starts). This allows you to purchase tickets, grab food, and catch the opening ceremonies.
> - **Resolved Sunday Burger Club Closing Hour Lockout**: Removed the 22:00 Sunday Burger Club stop, which closes at 21:00. Eating famous KBO stadium chicken (*chimaek*) and street food during the game makes a second heavy late-night burger meal redundant anyway. 
>
> ## ⚡ DAY 10 PACING & GEOGRAPHIC FLOW OPTIMIZATION (19 Jun 2026) — READ FIRST
>
> An audit of Day 10 (Busan to Seoul Travel Day) was performed to resync pre-booked transit and resolve local bugs:
>
> - **Resynced KTX Train to Booked Tickets**: Corrected the KTX travel block in `journey.html` and `index.html` from the incorrect 13:00 slot to the actual booked **KTX124 at 13:17** (arriving 16:34).
> - **Removed Redundant Bakery & Solved Walking Bug**: Removed the redundant Taeseongdang bakery visit in the morning (which was already done on Day 7). This also resolved a 6km teleportation walking bug (walking from the UN Cemetery in Nam-gu to Choryang-dong in 5 minutes).
> - **Added Busan Station Lunch**: Dedicated a 45-minute lunch window at Busan Station before departure to eat at a local station spot or pick up gourmet rail lunchboxes (*dosirak*) to eat comfortably on the KTX.
>
> ## ⚡ DAY 9 PACING & GEOGRAPHIC FLOW OPTIMIZATION (19 Jun 2026) — READ FIRST
>
> An audit of Day 9 (Old Busan Day) was performed to resolve a massive geographic conflict:
>
> - **Resolved 60km Double-Yoyo Conflict**: Discovered that the original itinerary had the user travel from Gamcheon (southwest) to Skyline Luge (northeast Gijang, 32km away), and then immediately back to Yeongdo Island (south-central, 28km away). 
> - **Moved Skyline Luge to Day 8 Morning**: Paired Skyline Luge (`a-luge`) directly with **Haedong Yonggungsa Temple** next door in Gijang-gun on Day 8 morning (opens at 9:00 AM on weekends). This groups the northeast attractions and saves **over 60km of driving and 3 hours of transit**.
> - **Created Circular South Busan Loop**: Day 9 is now a clean, compact loop of Gamcheon Culture Village $\rightarrow$ Huinnyeoul Culture Village (Yeongdo) $\rightarrow$ Momos Coffee Roastery $\rightarrow$ Jagalchi & Gukje Markets (Nampo-dong) $\rightarrow$ dinner at Gaya Milmyeon & hotteok at BIFF Square $\rightarrow$ Jeonpo Cafe Street stroll & Sulbing.
>
> ## ⚡ DAY 8 PACING & GEOGRAPHIC FLOW OPTIMIZATION (19 Jun 2026) — READ FIRST
>
> An audit of Day 8 (Ocean Cliffs & Drone Show) was performed to resolve walking and transit bugs in Busan:
>
> - **Resolved Green Railway Walk Illusion**: Corrected the travel time from Cheongsapo back to Mipo after the Haeundae Sky Capsule. It was marked as a "10-minute walk" but is actually a 4.5 km coastal walk. Formally added the **40-minute scenic Green Railway coastal walk** to the itinerary, preserving the linear pacing.
> - **Fixed Oryukdo Skywalk Transit and Close Risk**: Replaced the slow, convoluted public transit route (which would take over 1 hour 15 mins and cause you to miss the 18:00 skywalk closure) with a direct **30-minute taxi crossing the Gwangan Bridge** (~₩14,000 / R150), ensuring you arrive at 17:00 with plenty of time to visit.
> - **Direct Taxi to Gwangalli**: Replaced the public transit leg from Oryukdo to Gwangalli with a quick 15-minute taxi to ensure you make your 18:00 dinner at Handasot comfortably.
>
> ## ⚡ DAY 7 PACING & GEOGRAPHIC FLOW OPTIMIZATION (19 Jun 2026) — READ FIRST
>
> An audit of Day 7 (KTX to Busan & Choryang Tour) was performed to resolve logistical bugs and resync pre-booked tickets:
>
> - **Resynced KTX Train to Booked Tickets**: Changed KTX departure in `journey.html` and `index.html` from the incorrect 14:30 slot to the actual booked **KTX103 at 13:08** (arriving 16:28).
> - **Resolved 168 Stairs Monorail Lockout**: Moved the Choryang Ibagu-gil hillside trail to **16:50** (immediately upon arrival) so that you can ride the free community monorail before it closes at **18:00**, rather than climbing the steep steps in the dark.
> - **Fixed 6km Teleportation Bug**: Changed the flow to a locker-based loop at Busan Station (deposit bags $\rightarrow$ do Choryang trail $\rightarrow$ buy pastries at Taeseongdang 1950 $\rightarrow$ eat pork gukbap dinner at Bonjeon). Then retrieve bags and take a taxi to Daeyeon-dong to check in to Bonathree Hotel, eliminating a geographically impossible 5-minute walk from Daeyeon-dong to Choryang-dong.
>
> ## ⚡ DAY 6 PACING & GEOGRAPHIC FLOW OPTIMIZATION (18 Jun 2026) — READ FIRST
>
> An audit of Day 6 (Secret Garden & Han River) was performed to resolve palace tour timing conflicts and walking errors:
>
> - **Resolved Secret Garden Lockout**: Moved the English Secret Garden tour to **10:30 AM** (its exact slot) and deferred brunch at Parc Seoul to **13:00**, ensuring you don't miss the tour.
> - **Consolidated Han River Picnic at Banpo**: Removed the Yeouido Picnic (`a-hanriver`) and consolidated it directly at Banpo Hangang Park (`a-banpo`) to eliminate a grueling 6km walk (1 hr 15 mins) that was incorrectly styled as a 5-minute stroll.
>
> ## ⚡ DAY 5 PACING & GEOGRAPHIC FLOW OPTIMIZATION (18 Jun 2026) — READ FIRST
>
> An audit of Day 5 (Yeonnam & Myeongdong) was performed to resolve geographic doubling-back and scheduling redundancy:
>
> - **Removed Redundant Dongdaemun Detour**: Removed the 16:30 Dongdaemun Fashion Market stop. Visiting Dongdaemun in the late afternoon was out-of-the-way (creating a Yeonnam -> Myeongdong -> Dongdaemun -> Myeongdong loop) and logistically useless, as the wholesale markets open at 8:00 PM. Dongdaemun is already scheduled for Day 10 at 21:30, which is the perfect late-night window.
> - **Restored Clean Linear Flow**: By removing Dongdaemun, the day is now a clean linear transit path from West to East: Yeonnam (West) -> Myeongdong (Central) -> Deoksugung/City Hall (West-Central) -> Ahyeon (West). Bypassing the detour saves ~40 minutes of transit and eliminates a double transfer.
> - **Paced Afternoon Snacks**: Spaced out Egg Drop (14:30) and Sinjeon Tteokbokki (16:00) by 1.5 hours to avoid food overlap and preserve appetite for a 18:00 dinner at Myeongdong Kyoja.
> - **Direct and Early Return**: Streamlined the night-palace transit, utilizing a direct Subway Line 2 connection from City Hall back to Ahyeon Station (6-minute ride), returning to the apartment by 9:15 PM.
>
> ## ⚡ DAY 3 PACING & EVENING ROUTE OPTIMIZATION (18 Jun 2026) — READ FIRST
>
> An audit of Day 3 (Imperial Heritage) was performed to improve pacing and remove logistical outliers:
>
> - **Removed London Bagel Museum & Café Bora**: Skipped London Bagel Museum to avoid its legendary 2+ hour queue that would collide with Gyeongbokgung Palace guard ceremony and Hanbok rental bookings. Skipped Café Bora to prevent severe food/dessert fatigue before dinner.
> - **Replaced Namsan Mountain Gym**: Removed the 19:30 outdoor gym trek, which was a major transit and safety outlier (hiking a dark forest trail at night after a full day of walking).
> - **Added Ewha Womans University Shopping Streets**: Replaced the gym with a post-dinner stroll along Ewha Womans University Shopping Streets (`s-ewha`), a student boutique and cosmetics district right next to the Ahyeon Apartment, closing the day's loop early (returning by 9:00 PM).
> - **Added Map Coordinates**: Provided accurate lat/lng coordinates (`37.5585, 126.9455`) for the Ewha Shopping Streets in `data.js` to ensure the map renders the pin and routes correctly.
>
> ## ⚡ MAP CORRECTIONS, TAB SPACING, ZAR PRICING & DAY 2 ROUTE OPTIMIZATION (18 Jun 2026) — READ FIRST
>
> Major audit and optimization updates were performed to resolve map pin errors, visual tab formatting, and pacing issues:
>
> - **Tab Bar Styling**: Formatted day tabs to show the full day name with spaces (e.g. `Day 1 Saturday 27` instead of the un-spaced `Day 1Sat 27`), ensuring a cleaner, space-efficient look.
> - **Closed-Loop Journeys (All Days)**: Added return-to-hotel/apartment legs and check-ins for all days (Days 1 to 11) to close the loops and show correct return times, ensuring tourists return to their accommodation by ~11 PM.
> - **Map Pin Repairs**: Identified and added accurate latitude/longitude coordinates for **36 places** in `data.js` that previously lacked them, restoring all map pins, card-click zooms, and polyline route drawings.
> - **Cost Display in ZAR (Rand)**: Integrated the South African Rand (ZAR) conversion next to all Won (KRW) prices on timeline cards, map popups, and explore overlays, allowing for direct value comparisons on-the-fly.
> - **Day 2 Route Optimization**: 
>   - **Removed Mangwon Market** to eliminate 3.3 km of exhausting back-and-forth walking in the morning and reduce food fatigue (having 6 food/dessert stops was non-feasible).
>   - **Reordered Afternoon Activities**: Moved the Hongdae street stroll, photo booth, and street performers to 5:15 PM *before* heading to Haneul Park, eliminating doubling back.
>   - **Streamlined Transit**: Utilized a direct Subway Line 6 connection from Haneul Park to Gongdeok/Mapo Station (12-minute ride) for a timely 8:30 PM BBQ dinner at Mapo 최대포 and a Sulbing nightcap, getting you home to Ahyeon by 10:45 PM.
>
> ## ⚡ MORNING COFFEE, DIETARY ADJUSTMENTS & MUSEUM UPDATES (16 Jun 2026) — READ FIRST
>
> Swapped and added new curated items to better suit morning coffee preferences, traditional museum requirements, and dietary preferences:
>
> - **Morning Coffee Integration**: Prefixed Day 4 morning with **Camel Coffee** (`r-camel-coffee`) and Day 5 morning with **Reindeer Café** (`r-reindeer`) to ensure every morning starts with a unique local café.
> - **Remove Fish Cakes & Jagalchi**: Removed Jagalchi Fish Market (`r-jagalchi`) and Samjin Amook fish cake bakery (`r-amook`) on Day 9 evening. Replaced them with a combination of **Halmae Gaya Milmyeon** (`r-halmae-gaya-milmyeon`) for dinner, a walk through **BIFF Square Street Food** (`r-biff-square-street`) for **Ssiat Hotteok** (seed pancakes), and **Sulbing** (`r-sulbing`) for traditional bingsu.
> - **Actual Museum Fulfilling**: Added **Leeum Museum of Art** (`a-leeum`) to Day 12 afternoon (making it `'a-leeum;a-starfield'`) to ensure a balance of actual traditional and indoor museums alongside palaces and gardens.
> - **Day 10 Timeline Relocation**: Moved **Oryukdo Skywalk** (`a-oryukdo`) from Day 10 morning to Day 8 afternoon. This frees up Day 10 morning (checkout & KTX travel day) to focus solely on a relaxed visit to **UN Memorial Cemetery & Busan Museum** (`a-uncemetery`).
> - **Smart Migrations**: Updated the auto-migration blocks inside `loadUserTrack` so that returning users who had the old default slots on Day 4, Day 5, Day 8, Day 9, Day 10, and Day 12 are automatically upgraded to these new choices.
>
> ## ⚡ INTERACTIVITY, NAVIGATION, FAVORITES & MOBILE UPDATE (12-13 Jun 2026) — READ FIRST
>
> Major updates were made to improve the planner canvas drag & drop, card detail triggers, favorites integration, navigation, and mobile layout:
>
> - **Modal Carousel Navigation (13 Jun 2026)**: Added left and right chevron buttons (`.modal-nav-arrow`) inside the details modal. Users can click these arrows (or use the keyboard `ArrowLeft`/`ArrowRight` keys) to cycle through the currently active, searched, and filtered card list without closing the modal.
> - **Saturday June 27 Lockout**: Saturday morning slot is locked as `"✈️ In Transit / Flight"`.

> - **Intra-Itinerary Drag & Drop & Confirmation**: Enabled drag-and-drop between canvas slots. Dropping an activity onto an occupied slot triggers a custom confirmation modal overlay (`#confirmReplaceModal`) to prevent accidental replacements.
> - **Split-Click Triggers**: Clicking a card background serves as the drag handle. To open the details modal, users must click the underlined hyperlink card name or the new `ℹ️` info button.
> - **Favorites Feature & Match Score Boost**: Added a dynamic "Favorites" tab in the planner sidebar (persisted in localStorage under `itinerary_favorites_${user}`). Favorited items get a `+50` boost in match score calculations.
> - **Slot Picker Favorites Filter & Toggles**: Added a "⭐ Favorites" filter chip in the "+ Browse all options" slot picker modal. Cards inside this picker now display a favorite star button, allowing users to browse/search and favorite items on-the-fly, then filter by "Favorites" to easily add them to slots.
> - **Interactive Menu Favorites Badges**: The initials badges (`A`, `C`, `B`, `O`) on the cards in `menu.html` are now fully interactive buttons. Clicking an initial adds/removes that item from that specific family member's favorites list in real-time without needing to open the details modal (with event propagation blocked so the modal won't trigger).

> - **Menu Details Modal Favorites Toggles**: Inside the `menu.html` details modal, a row of toggles (`⭐ Ayden`, `⭐ Claudine`, etc.) allows checking and toggling favorites for anyone reactively.
> - **Coordination Legend**: A Coordination Key panel is rendered above the day canvas in `itinerary.html` explaining the slot borders and statuses (**Fully Synced**, **Same Region**, **Split Region**, **Wishlist**).
> - **Mobile CSS Stack Layout**: Stacks the planner controls (`.planner-controls`) vertically on screens `< 600px` so that buttons do not overflow.
>

> ## ⚡ ARCHITECTURE UPDATE (11 Jun 2026) — READ FIRST
>
> The data layer was refactored. **All items now live in `data.js`** (`window.TRIP_DATA` with
> `foodGuide`, `restaurants`, `activities`, `shopping`, `aliases`). Both `menu.html` and
> `itinerary.html` load it via `<script src="data.js">`.
>
> - **menu.html** renders TRIP_DATA directly (122 items). New restaurant cats: `bakery`, `chain`.
> - **itinerary.html** derives its draggable sidebar from TRIP_DATA at runtime — every plannable
>   menu item (restaurants, cafés, bakeries, convenience run, activities, shopping) is available
>   in the planner automatically. **To add a venue anywhere, add it to data.js only.**
> - Planner metadata per item: `plannable`, `interest[]` (fashion/culture/thrills/foodie),
>   `diet[]` (pork/beef/seafood/spicy), `vegOk`, `wish` (survey wishlist key), `foodCat`
>   (bbq/stews/street/cafes ranking bucket), `indoor`, `needsBooking`, `closedDay`, `expensive`.
> - **Survey-aware sidebar**: items conflicting with dietary exclusions are hidden (with a count),
>   `expensive` items hidden under R12,000 budget, and every card gets a 0–100 **match score**
>   (priority interest +40, interest +25, wishlist +30, food ranking +18/12/6, family-sync +15).
>   Sorted best-first with "✨ Best matches" / "Everything else" sections, ★ Top Picks filter,
>   and a preference-chip strip (`#prefStrip`) summarising the active user's survey.
> - **Ghost suggestions**: empty unlocked slots show the best unused, region-valid, survey-valid
>   item (time-of-day weighted: food→evening etc.), recomputed every render and aware of what
>   other family members planned. `+` accepts (`acceptSuggestion()`).
> - **Legacy IDs**: old itinerary ids (e.g. `hanbok-day`) are remapped to canonical menu ids
>   (e.g. `a-hanbok`) via `TRIP_DATA.aliases` — `normalizeItinerary()` runs on every load, so
>   old localStorage tracks keep working. Auto-populate (`submitQuestionnaire`) now builds its
>   pools by match score instead of hardcoded id lists.
> - Buttons/inputs now inherit the page font globally (`button, input, select, textarea`).
> - Old inline data arrays were removed from menu.html/itinerary.html. The sections below that
>   describe them are **historical**; trust this note + the code.

The site is also deployed to **Vercel** (`.vercel` directory present). Deployment is via `vercel --prod` from the project root.

---

## Trip Details (hardcoded context throughout)

| Detail | Value |
|---|---|
| Traveller | Ayden Marthinus |
| Trip dates | Friday 26 June – Thursday 9 July 2026 (13 nights) |
| Leg 1 — Seoul Ahyeon | 27 Jun – 3 Jul (6 nights) |
| Leg 2 — Busan | 3 Jul – 6 Jul (3 nights, 2 rooms at Bonathree Hotel) |
| Leg 3 — Seoul Seodaemun | 6 Jul – 9 Jul (3 nights) |
| Flights | Ethiopian Airlines (specific flight numbers in itinerary.html) |
| KTX booked | Seoul→Busan: Jul 3 13:08→16:28 · Busan→Seoul: Jul 6 13:17→16:34 |
| Currency | Korean Won (₩) displayed; ZAR conversions shown at rate ₩10,000 ≈ R108 |
| Origin | South Africa |

---

## Design System (shared across all 3 files)

All three files duplicate the same CSS variables in their `<style>` block — there is NO shared CSS file.

### Color Tokens
```css
--primary: #4A6B53;          /* Forest green — primary actions, active states */
--primary-light: #70937A;    /* Lighter green — hover states */
--primary-dark: #344B3A;     /* Dark green — pressed states */
--accent: #C8963E;           /* Amber/gold — prices, highlights, tips */
--bg-body: #F5F7F6;          /* Off-white page background */
--bg-card: #FFFFFF;          /* Card / panel white */
--text-main: #2F3E46;        /* Body text */
--text-heading: #1C2723;     /* Headings */
--text-muted: #5C6F67;       /* Secondary text, placeholders */
--border: #E3E7E5;           /* Card borders, dividers */
```

### Dark Mode Overrides (applied by toggling `.dark-theme` on `<body>`)
```css
.dark-theme {
    --bg-body: #101614;
    --bg-card: #161E1B;
    --text-main: #C0CFC7;
    --text-heading: #F5F7F6;
    --text-muted: #8FA399;
    --border: #242E2A;
}
```
Dark mode state is persisted in `localStorage` key `theme` ('dark' | 'light').

### Typography
- **Sans-serif:** `'Outfit'` (Google Fonts) — body text, buttons, UI
- **Serif:** `'Playfair Display'` (Google Fonts) — `h1`, `.serif-font`, modal titles
- **Icons:** Font Awesome 6.4.0 (CDN) — `fa-solid`, `fa-brands`

### Key Shared UI Patterns
- **Section Switcher Bar** — fixed dark top bar (52px height, `z-index: 2000`) with 🇰🇷 Korea 2026 logo and 3 section buttons. Present on ALL three pages. Active section has `.active` filled green pill. CSS class: `#sectionSwitcher`, `.switcher-btn`, `.switcher-btn.active`.
- **Control Bar** — floating dark pill fixed at `bottom: 20px`, `z-index: 1000`. Contains Dark Mode toggle and Print/Save PDF. CSS class: `.control-bar`.
- **Tab navigation** — `.nav-tabs` row of `.tab-btn` pills. Active state: `.tab-btn.active`.
- **Cards** — `.card` with border-radius 16px, subtle shadow, `--bg-card` background.
- **Highlight box** — `.highlight-box` — left-bordered amber infobox for tips/warnings.

---

## Page 1: `index.html` — South Korea Travel Brochure

### Purpose
The main editorial reference guide. Rich text about each destination: accommodation area, restaurants, sights, shopping, logistics tips, language, emergency contacts, and a day-by-day suggested agenda.

### Navigation Structure
- **Section Switcher** (top, fixed) — Brochure active, links to Itinerary + Menu
- **Brochure Sub-Nav** (below header) — 5 internal tabs using `switchTab(event, tabId)`:
  - `ahyeon` — Seoul Ahyeon & Mapo area
  - `busan` — Busan (Nam-gu / Haeundae)
  - `central-seoul` — Gyeongbokgung, Gangnam, Starfield Library
  - `logistics` — KTX, T-money, apps, weather, money, emergency contacts
  - `agenda` — Suggested day-by-day agenda with collapsible day items

### Key JS Functions (index.html)
```js
switchTab(event, tabId)      // shows/hides .tab-content divs, updates .active
toggleAgendaDay(el)          // expands/collapses .agenda-day items
toggleTheme()                // dark/light mode toggle
```

### Images Used in index.html
Images are embedded as `<img src="images/filename.png">` within card content:
- `oryukdo_busan.png` — Busan section hero
- `hanbok_palace.png` — Gyeongbokgung section hero
- `ahyeon_cathedral.png` — Ahyeon section

### Agenda Format
Each agenda day is an `.agenda-day` div with:
- `.agenda-header` (clickable, triggers collapse toggle)
- `.day-badge` — "Day 1", "Day 2" etc.
- `.day-date` — date string
- `.day-summary` — italic one-liner
- `.agenda-content` — detailed timeline

Days are collapsed by default (`.collapsed` class on `.agenda-day`). Toggled by `toggleAgendaDay()`.

---

## Page 2: `itinerary.html` — Master Itinerary

### Purpose
The main planning tool for Ayden. A two-tab page:
1. **Day-by-Day Itinerary** — hour-by-hour plan across 13 days with a drag-and-drop activity sidebar
2. **Pre-Trip Checklist** — preparation tasks before departure

### Navigation Structure
- **Section Switcher** (top, fixed) — Itinerary active, links to Brochure + Menu
- **Itinerary Sub-Nav** — 2 tabs only:
  - `itinerary` (Day-by-Day)
  - `prep` (Pre-Trip Checklist)
- Cross-section navigation is ONLY in the Section Switcher — NOT mixed into this tab row

### Day Structure
Each day in the itinerary is rendered as an accordion-style `.day-container` with:
- A day header (date, day number, location badge)
- Morning / Afternoon / Evening **time slots** (`.time-slot`)
- Each time slot accepts draggable activity cards

### Activity Sidebar
The right panel contains draggable activity cards (`.draggable-card`) with:
- Emoji + name + cost chips
- Drag handle
- `draggable="true"` attribute
- `dragstart` / `dragend` event listeners

Dropping a card into a time slot fires the slot's `dragover` / `drop` handlers. Invalid drops (e.g. wrong leg) visually reject with `.drag-invalid` class.

### Survey / Intake Wizard
A multi-step modal wizard that appears on first visit (when `localStorage.getItem('itinerary_survey_completed')` is falsy).

**Steps:**
1. Welcome + username entry
2. Who is coming (names)
3. Interests (culture, food, adventure, shopping, family-fun — multiple select)
4. Dietary restrictions / exclusions (beef, seafood, spicy, pork, vegetarian) — these feed the restaurant filtering logic
5a. Budget slider — range ₩5,000 to ₩20,000 ZAR (displayed in ZAR: R5,000–R20,000) — the max was set per user request
5b. Food wishlist — 9 clickable items:
   - `bbq`, `crab`, `chicken`, `noodles`, `soup`, `kalguksu`, `hotteok`, `bingsu`, `convenience`
6. Food priority ranking — 4 draggable items ranked 1–4:
   - Korean BBQ & Grills, Hot Soups & Stews, Traditional Street Food, Trendy Cafés & Bakeries
   - **Drag to reorder** (not click-to-set-number, the user explicitly requested drag-reorder)
7. Itinerary layout choice (auto-populate vs. manual)

Survey results saved to: `localStorage.key = 'itinerary_survey_${currentTrackUser}'`

Survey completion flag: `localStorage.key = 'itinerary_survey_completed'` (set to `'true'`)

### Food Wishlist Tooltip System
On the wishlist step (5b), hovering over a food item shows a rich tooltip:

- **Function:** `showFoodTip(event, key)` / `hideFoodTip()`
- **Data source:** JS object `FOOD_DATA` in itinerary.html (lines ~2050–2100 approx)
- **Tooltip content:** food name, emoji, taste tags, ingredients list, and a short description
- **Tooltip positioning:** cursor-relative (uses `event.clientX/Y` with viewport clamping)
- **CSS class:** `.food-tooltip` — brochure-styled card with gradient header and emoji
- **Images:** Currently using emoji as placeholder. The plan was to replace with brochure-style PNGs once image generation quota reset (image quota was exhausted during session). The `FOOD_DATA` object has an `img` field for this (currently set to `null` or empty).

### Itinerary Lock / AI Guide
- **Lock button** — `id="lockItineraryBtn"`, calls `toggleItineraryLock()`
- When the itinerary is **locked**, the AI Travel Guide feature is enabled/unlocked
- When **unlocked**, the AI Guide is disabled/hidden
- The AI Guide generates a narration/summary of the locked itinerary — it is NOT auto-generated on page load; it only activates after the user explicitly locks their plan

### Key JS Functions (itinerary.html)
```js
switchTab(event, tabId)          // tab switching (itinerary / prep)
toggleItineraryLock()            // lock/unlock itinerary, enables AI guide
initSurvey()                     // initialises survey wizard on first load
nextSurveyStep(step)             // advances survey step
prevSurveyStep(step)             // goes back in survey
toggleFoodWishlist(key)          // adds/removes food item from wishlist array
showFoodTip(event, key)          // shows hover tooltip for food wishlist item
hideFoodTip()                    // hides tooltip
selectQuestLayout(layout)        // sets auto-populate vs. manual in survey
buildDayCards()                  // renders the day-by-day itinerary structure
renderActivitySidebar()          // renders draggable activity cards in sidebar
dropActivityInSlot(slotEl, id)   // handles drop event
toggleAgendaDay(el)              // generic accordion toggle
toggleTheme()                    // dark/light mode toggle
```

### LocalStorage Schema (itinerary.html)
```
theme                                    → 'dark' | 'light'
itinerary_survey_completed               → 'true' | null
itinerary_survey_{username}              → JSON object:
    {
        username: string,
        who: string[],
        interests: string[],
        exclusions: string[],     // dietary: 'beef','seafood','spicy','pork','vegetarian'
        budget: number,           // in ZAR (R5000–R20000)
        wishlist: string[],       // food keys: 'bbq','crab','chicken',...
        foodPriority: string[],   // ordered: ['bbq','stews','street','cafes']
        layout: 'auto' | 'manual'
    }
itinerary_slots_{username}               → JSON object: day→slot→activityId mapping
itinerary_locked_{username}              → 'true' | null
```

---

## Page 3: `menu.html` — The Menu

### Purpose
A comprehensive interactive reference hub with 90 total entries across three major sections: Food, Activities, Shopping. Every item is a clickable card that opens a full-screen detail modal.

### Navigation Structure
- **Section Switcher** (top, fixed) — Menu/Activity Menu active, links to Brochure + Itinerary
- **3 main tabs** (`.tab-btn`):
  - `food` — Korean Food Guide + Restaurants & Dining
  - `activities` — All activities with search + filter
  - `shopping` — Shopping venues with filter
- **Food has 2 sub-tabs** (`.sub-tab-btn`):
  - `guide` — Food knowledge cards (must-try / convenience / etiquette)
  - `restaurants` — Specific venue cards

### Data Architecture (menu.html)
All data lives in 4 JavaScript arrays at the top of the `<script>` block:

```js
const FOOD_GUIDE = [...];      // 18 items — food knowledge cards
const RESTAURANTS = [...];     // 16 items — restaurant/café venue cards
const ACTIVITIES = [...];      // 22 items — activity venue cards
const SHOPPING = [...];        // 16 items — shopping venue cards
```

Each item object follows this schema:
```js
{
    id: 'unique-string',         // used for openModal() lookup
    cat: 'category-string',      // used for filter pills
    name: 'Display Name',
    emoji: '🍜',
    gradient: 'linear-gradient(135deg, #color1, #color2)',  // card hero background
    region: 'seoul1' | 'busan' | 'seoul2' | 'any',
    cost: '₩15,000–25,000',
    costZAR: '≈ R162–270',
    duration: '1.5 hrs',
    teaser: 'One-sentence summary shown on card.',
    desc: 'Full 3–5 sentence description for modal.',
    highlights: ['array', 'of', 'bullet', 'strings'],      // shown as pills in modal
    tips: 'Advice / Reddit tips paragraph for amber box.',
    hours: 'Hours string',
    address: 'Area or full address',
    mapLink: 'https://naver.me/...',    // Opens in Naver Maps
    link: 'https://...',                // Official page or Instagram

    // ACTIVITIES ONLY:
    onItinerary: true | false,          // shows green "★ On Itinerary" badge
    needsBooking: true | false,         // shows red "Book Ahead!" badge
}
```

### Filter Categories

| Section | Filter keys |
|---|---|
| Food Guide (`cat`) | `must-try`, `convenience`, `etiquette` |
| Restaurants (`cat`) | `seoul`, `busan`, `cafe` |
| Activities (`cat`) | `culture`, `family-fun`, `shows`, `hands-on` + region `busan` |
| Shopping (`cat`) | `beauty`, `fashion`, `unique` |

### Region Chip Classes
```css
.cc-seoul1  /* green  — Seoul Leg 1, Jun 27–Jul 3 */
.cc-busan   /* blue   — Busan, Jul 3–6 */
.cc-seoul2  /* brown  — Seoul Leg 2, Jul 6–9 */
.cc-any     /* purple — Anywhere / any leg */
.cc-price   /* amber  — price chips */
.cc-book    /* red    — "Book Ahead!" */
.cc-free    /* green bg — free entry or on-itinerary */
```

### Modal System
- **Overlay:** `#menuModal` with class `.menu-modal-overlay`
- **Open:** adds class `.open` to overlay → triggers CSS opacity + sheet slide-up animation
- **Close triggers:** X button, clicking backdrop, pressing `Escape`
- **Blur:** `backdrop-filter: blur(8px)` on the overlay
- **Sheet:** `.modal-sheet` — max-height 92vh, border-radius 24px 24px 0 0, slides up from `translateY(48px)`
- **Populated by:** `openModal(dataset, itemId)` — looks up item in the 4 data arrays, then injects into `#mHero`, `#mTitle`, `#mChips`, `#mDesc`, `#mGrid`, `#mHighlights`, `#mTips`, `#mActions`

### Key JS Functions (menu.html)
```js
switchMain(tab)                   // switches between food/activities/shopping main tabs
switchFoodSub(sub)                // switches between guide/restaurants sub-tabs
initFilters()                     // builds all 4 filter pill rows
buildPills(containerId, pills, type)  // renders filter pill buttons into a container
setFilter(type, val)              // updates active filter + re-renders grid
renderGuide()                     // filters + renders food guide cards
renderRestaurants()               // filters + renders restaurant cards
renderActivities()                // filters + searches + renders activity cards
renderShopping()                  // filters + renders shopping cards
cardHtml(item, dataset)           // returns card HTML string for one item
openModal(dataset, itemId)        // populates + shows modal for clicked card
closeModal()                      // hides modal overlay
modalBgClose(event)               // closes modal if click is on overlay (not sheet)
toggleTheme()                     // dark/light mode toggle
```

### Activity Search
Activities tab has a live search bar (`#activitySearch`). The `renderActivities()` function reads `input.value`, lowercases it, and filters against `item.name + item.teaser + item.desc`. Tied to `oninput` event.

---

## Section Switcher Bar (shared across all 3 pages)

This is the persistent dark navigation bar pinned to the top of every page. It is **duplicated** in each file's `<style>` and `<body>` — not shared via a file.

### HTML (same in all 3 files, only `active` changes)
```html
<nav id="sectionSwitcher" class="no-print" aria-label="Main sections">
    <div class="switcher-logo"><span>🇰🇷</span> Korea 2026</div>
    <div class="switcher-divider"></div>
    <div class="switcher-sections">
        <a class="switcher-btn [active]" href="index.html">    <i class="fa-solid fa-book-open"></i> Brochure </a>
        <a class="switcher-btn [active]" href="itinerary.html"><i class="fa-solid fa-route"></i> Itinerary </a>
        <a class="switcher-btn [active]" href="menu.html">     <i class="fa-solid fa-list"></i> Menu </a>
    </div>
</nav>
```

Active page uses a `<button>` (not `<a>`), with `class="switcher-btn active"` and `aria-current="page"`.

### Key CSS
```css
#sectionSwitcher { position: fixed; top: 0; height: 52px; z-index: 2000; background: rgba(16,22,20,0.97); backdrop-filter: blur(16px); }
.switcher-btn.active { background: var(--primary); color: #FFFFFF; }
body { padding-top: 52px; }   /* prevents content being hidden behind bar */
```

---

## Control Bar (shared across all 3 pages)

```html
<div class="control-bar no-print">
    <button id="themeToggle" onclick="toggleTheme()"><i class="fa-solid fa-moon"></i> <span>Dark Mode</span></button>
    <button onclick="window.print()"><i class="fa-solid fa-print"></i> <span>Save / Print PDF</span></button>
</div>
```

- Positioned `fixed` at `bottom: 20px`, centered via `left: 50%; transform: translateX(-50%)`
- Hidden on print via `.no-print { display: none !important }`
- On mobile (≤600px), button text is hidden, showing icon-only circles

---

## Print Styles

All three files have `@media print` blocks that:
- Hide `.no-print` elements (section switcher, control bar, nav tabs, filter pills)
- Force all `.tab-content` to `display: block` (so all sections print)
- Remove shadows and decorative borders
- Set body font to serif for legibility

---

## Known Issues / Limitations

### ⚠️ Emoji images not yet added to food wishlist tooltips (itinerary.html)
The `FOOD_DATA` object in `itinerary.html` has an `img` field that currently holds `null` or empty string. The plan was to generate brochure-style PNG images for each of the 9 food wishlist items (bbq, crab, chicken, noodles, soup, kalguksu, hotteok, bingsu, convenience) using `generate_image`. **Image generation quota was exhausted during the session** (resets ~hourly). When quota is available:
1. Generate 9 images in brochure illustration style
2. Save to `/Users/aydenmarthinus/Desktop/korea-trip-2026/images/` as `food_[key].png`
3. Update the `img` field in `FOOD_DATA` in `itinerary.html` for each item
4. The tooltip CSS (`.food-tooltip`) already has an `img` element that shows/hides based on whether `img` is set

### ⚠️ CSS variables duplicated across 3 files
There is no shared CSS file or build step. If the color palette needs changing, it must be updated in all three `<style>` blocks. Consider creating a `styles.css` if more maintenance is needed.
(✅ The DATA duplication problem was solved on 11 Jun 2026 via the shared `data.js` — see Architecture Update at the top.)

### ⚠️ Section switcher HTML duplicated across 3 files
Same as above — the switcher bar HTML and CSS is copied into each file. If adding a 4th page, copy the pattern and add the new link to all 3 existing files.

### ⚠️ No server-side functionality
This is a 100% static site. Survey responses, itinerary arrangements, and dark mode preference are stored in `localStorage` — they are device and browser-specific. There is no backend, no database, no user accounts.

---

## Outstanding / Future Tasks

These were either mentioned by the user and not yet built, or are logical next steps:

### High Priority
1. **Food wishlist tooltip images** — Generate 9 brochure-style food PNG images (see Known Issues above) and wire them into `FOOD_DATA` in `itinerary.html`
2. **AI Guide narration** — When itinerary is locked, the AI Guide section should generate a narrative travel guide from the locked plan. Currently only the lock/unlock toggle exists — the actual generation logic is stubbed
3. **More transcript/blog content fed into menu.html** — User mentioned they will supply YouTube/blog transcripts of venues to add to the menu. When provided, add items to the relevant `RESTAURANTS`, `ACTIVITIES`, or `SHOPPING` arrays in `menu.html` following the existing item schema

### Medium Priority
4. **Brochure scroll-spy sub-nav** — `index.html` currently uses click-to-show tab panels. A scroll-spy approach that highlights the current brochure section as you scroll was discussed but not implemented
5. **Survey results display on itinerary** — After completing the survey, the itinerary should show a personalized header acknowledging the user's name, budget, and wishlist preferences
6. **Activity card detail modals in itinerary.html** — The sidebar activity cards on the itinerary page have hover tooltips but not full modals. Could mirror the `menu.html` modal system

### Lower Priority
7. **Shared CSS file** — Refactor the duplicated variables and shared component CSS into a single `styles.css` import
8. **Packing list / countdown feature** — A simple day-countdown to departure and checklist for packing could be added to the Pre-Trip Checklist tab in `itinerary.html`

---

## How to Continue Development

1. **Open all 3 files** in a browser to test before and after changes
2. **Never introduce npm, a bundler, or a framework** — the user has not requested any, and the project is intentionally simple static HTML
3. **Maintain the CSS variable system** — never use hardcoded colors; always use `var(--primary)` etc.
4. **When adding data to menu.html** — follow the item schema exactly. The `id` field must be unique across the entire file. The `dataset` parameter passed to `openModal` must match one of the 4 array names: `'foodGuide'`, `'restaurants'`, `'activities'`, `'shopping'`
5. **Dark mode** — when adding new HTML components, test in both light and dark by toggling the `.dark-theme` class on `<body>`. Use CSS variables only; don't hardcode colors in new components
6. **Print styles** — any new major components should have a `@media print` rule if they should appear in print output
7. **The section switcher** — if adding a new page to the site, copy the switcher bar from any existing page, add the new page's link to all 3 existing pages, and mark the new page's own button as `active`

---

## Development Session Log

| Feature | File | Status |
|---|---|---|
| Budget slider (ZAR, R5k–R20k max) | itinerary.html | ✅ Done |
| Food priority: drag-to-reorder (not click-to-number) | itinerary.html | ✅ Done |
| AI Guide narration: button, only enabled after lock | itinerary.html | ✅ Done |
| Food wishlist: select items to try, feed into itinerary | itinerary.html | ✅ Done |
| Food wishlist hover tooltips (taste, ingredients, description) | itinerary.html | ✅ Done |
| Tooltip brochure-style images (9 foods) | itinerary.html | ⏳ Pending (quota) |
| Korean food research (blogs + guides) | research | ✅ Done |
| Cinema card added to activity sidebar | itinerary.html | ✅ Done |
| Section switcher bar (3-page nav, section isolation) | all 3 files | ✅ Done |
| Brochure sub-nav cleaned (cross-page links removed) | index.html | ✅ Done |
| Itinerary sub-nav cleaned (only Day-by-Day + Pre-Trip) | itinerary.html | ✅ Done |
| Menu old flat nav-tabs removed | menu.html | ✅ Done |
| Complete menu.html rebuild — 3 sections, card+modal UI | menu.html | ✅ Done |
| Food Guide cards (18 items: must-try, convenience, etiquette) | menu.html | ✅ Done |
| Restaurant cards (16 items: Seoul, Busan, cafés) | menu.html | ✅ Done |
| Activity cards (22 items with search + filter) | menu.html | ✅ Done |
| Shopping cards (16 items: beauty, fashion, unique) | menu.html | ✅ Done |
| Full-screen modal with blur backdrop | menu.html | ✅ Done |
| Filter pills + live search | menu.html | ✅ Done |
| Morning Coffee: Prefix Day 4 (Camel Coffee) & Day 5 (Reindeer Cafe) | itinerary.html | ✅ Done |
| Remove Fish Cakes: Swap Jagalchi & Samjin Amook on Day 9 Evening for Milmyeon, BIFF Square (Hotteok), and Sulbing | itinerary.html | ✅ Done |
| Add Traditional Museum: Inject Leeum Museum of Art on Day 12 Afternoon alongside National Museum of Korea | itinerary.html | ✅ Done |
| Relocate Skywalk: Move Oryukdo Skywalk from Day 10 morning to Day 8 afternoon to optimize KTX travel pacing | itinerary.html | ✅ Done |
| Morning Coffee: Prefix Day 11 (Milestone Coffee) | itinerary.html | ✅ Done |
