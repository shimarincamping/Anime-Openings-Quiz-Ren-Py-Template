# Ren'Py Generator for Anime Opening Quiz Videos

A generic template for "Easy to Impossible" style anime opening quiz videos

Screen recording required


Steps:
- Fill `Song List Sheet.xlsx` with [compatible data](https://docs.google.com/spreadsheets/d/1_601RwB9Sl3yTJQ3k0IMI8o319iZXAV4/edit?usp=drive_link&ouid=108270624448384351060&rtpof=true&sd=true)
- Copy columns C-Q to `data.txt`
- Copy output into `songlist` in `script.rpy`
- Customise as necessary
- Batch download webm and mp3 links in columns S-T into `game/audio` (requires `yt-dlp`)
- Customise the `00bgm.mp3` file
- Customise `game/images` by replacing files (display / footers / backgrounds)
- Customise `game/gui/main_menu.png` to replace starting image (thumbnail)
