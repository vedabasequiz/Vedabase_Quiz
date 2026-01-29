Place your Vedabase brand TTF/OTF font file here as `Vedabase-Regular.ttf`.

Why: The server-side OG generator (app/api/og/route.js) will look for `public/fonts/Vedabase-Regular.ttf` and embed it when present. Satori requires a font binary to render custom fonts server-side.

If you don't have the font, the generator will fall back to Arial/sans-serif.

To add the font:

1. Copy your TTF/OTF file into this folder and rename it to `Vedabase-Regular.ttf`.
2. Restart the Next dev server (if running):

```bash
npm run dev
```

3. Test the OG generator locally (after installing dependencies):

```bash
node scripts/generate-og.js
# opens or writes to og_cache/sample.png
```
