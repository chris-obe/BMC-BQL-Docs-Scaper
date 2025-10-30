# BMC BQL Docs Scraper

I got tired of re-explaining BMC Helix Query Language to ChatGPT, so I scraped the docs I actually read and smushed them into one Markdown file. Double laziness: now I can drag-and-drop the bundle into a chat and say "here, read this."

## What's here
- `bmc_download_docs.py` grabs the public docs listed in `URLS` and dumps the cleaned text into `bmc_query_language_docs.md` (or any filename you pass in).

## How I use it
1. Make sure Python 3.10+ is around.
2. `pip install requests beautifulsoup4 tqdm`
3. `python bmc_download_docs.py` – that'll refresh `bmc_query_language_docs.md`.

Feel free to swap URLs in the list if you want a different bundle. I just wanted the stuff I pester the docs team about the most.
