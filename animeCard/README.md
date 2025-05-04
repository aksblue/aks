# Anime Info Card - iOS Shortcut

This is an iOS Shortcut that fetches anime data using the Jikan API and displays it in a clean, animated HTML card using a Web View. The card shows the title, genre tags, summary, episode info, release dates, and includes interactivity like copying the title and toggling the summary.

### Features
- Uses the Jikan API (MyAnimeList unofficial) to fetch anime details.
- Nicely styled Web View with support for both light and dark mode.
- Tap-to-copy anime title.
- "Show More / Show Less" toggle for the anime summary.
- Click on the title to switch between English and Japanese name (if available).
- Clean layout for anime genres and episode data.
- Includes Jellycuts-compatible code for easier editing and backup.

### Shortcut Download
You can install the Anime Info Card shortcut using the link below:

**[Install Anime Info Card Shortcut](https://www.icloud.com/shortcuts/a785cbddd29244d495e1e53e39b574e2)**  

### Requirements
- **iOS Shortcuts app**
- **Another shortcut called `Limit Check For Jikan API`**  
  (This shortcut is not included here but is required to handle rate limits when using Jikan API.)

### How to Use
This shortcut expects input as a dictionary from another shortcut (such as an anime tracker or custom input form). It pulls relevant keys like `title`, `episodes`, `watched`, `start`, `end`, etc., and formats them into a Web View display.

### Dependencies
- Jikan API: [https://api.jikan.moe/v4](https://api.jikan.moe/v4)
- A secondary shortcut for API limit handling (`Limit Check For Jikan API`)
- Jellycuts (optional): You can use the included `.jellycut` file to edit this shortcut in code format.

### Note
This shortcut depends on data passed from **other shortcuts** that are not currently public. Because of that, this is **not a standalone shortcut**.  
If you want to use this or adapt it for your own workflow, feel free to reach out.

### Contact
If you want to request access to the full system, suggest improvements, or use parts of it in your own setup, please contact me first.

---

Created by Aksblue
