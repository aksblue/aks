# Match Score Algorithm

This script is designed to help find the best matching anime from a list based on a search term.

It works by comparing the search term to anime titles and calculating a score for how closely they match. If no good match is found, it uses a fallback method to try again with a different algorithm.

## Features

- Compares search input with anime titles using a scoring system
- Can return the result as plain text or JSON format
- Supports partial matches and basic symbol replacement (like "Ω" → "omega")
- Uses a backup algorithm if the first one doesn’t give a good match

## How It Works

1. You enter a search term (anime title).
2. The script checks each title in the list and gives it a match score.
3. If no score is high enough, it tries a fallback matching method.
4. The best match is returned in either text or JSON format.

## Settings

- `matchDataAsText`:  
  Set this to `true` to get plain text output.  
  Set to `false` to get JSON output.

## Dependencies

- Uses a fallback algorithm from:  
  `anime_algorithm/animeAlgorithmBitBitMatch@2`

## Usage

This script is meant to be used with a shortcut or automation system that sends in:
- A search term
- Anime data in JSON format

You can also test it using your own data if you’re familiar with JavaScript.

## Example

If you search for `"My Hero"`, the script might match it with `"My Hero Academia"` and return the full anime info.

---
