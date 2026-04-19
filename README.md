# FRH Reader Project

This repository contains the working source and published HTML outputs for the FRH reader site.

## Project Structure

- `thread_clean_reader_site/` = published GitHub Pages site
- `FRH_HTML_Reader/` = structured portable/local reader
- `FRH_GMA_Portable_Review_Package/` = GMA source corpus
- `tools/convert_gma_package.py` = generator that keeps the two reader forms harmonized

## Update Flow

After local content changes, regenerate the GMA HTML output and push:

```powershell
python tools\convert_gma_package.py
git status
git add .
git commit -m "Update reader site"
git push
```

GitHub Actions publishes `thread_clean_reader_site/` to GitHub Pages.
