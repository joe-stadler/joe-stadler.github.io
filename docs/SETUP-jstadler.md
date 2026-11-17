# Setting up jstadler.eu

Your site lives in this folder (a customized al-folio / Jekyll site). You never need to write HTML: text goes into Markdown files, papers into one BibTeX file, your CV into one data file.

## 1. Add your publications

1. Open your public library on SciX and use the export function to get **BibTeX**.
2. Save the result as `_bibliography/papers.bib` (replace the placeholder).
3. Optional: add `selected={true}` to up to a few entries to show them on the home page.

## 2. Put the site on GitHub

1. Create a **public** repository named exactly `joe-stadler.github.io` on your GitHub account.
2. Upload this folder's contents (GitHub Desktop is easiest; including the hidden `.github` folder matters). Or from a terminal inside this folder:

   ```
   git init -b main
   git add .
   git commit -m "Initial site"
   git remote add origin https://github.com/joe-stadler/joe-stadler.github.io.git
   git push -u origin main
   ```

3. In the repo: **Settings → Actions → General → Workflow permissions → Read and write permissions → Save**.
4. Open the **Actions** tab. The "Deploy site" workflow runs (about 4 minutes) and creates a `gh-pages` branch.
5. **Settings → Pages**: Source "Deploy from a branch", branch `gh-pages`, folder `/ (root)`. Under *Custom domain* enter `jstadler.eu` and save.

The file `CNAME` in this folder already contains `jstadler.eu`.

## 3. Point the domain at GitHub

In the DNS settings of the place where `jstadler.eu` is registered (Squarespace Domains if you keep it there):

- Remove the old records that point the domain to the Squarespace website (the apex A records and the `www` CNAME). Keep any MX/TXT records if you use email on this domain.
- Add four **A** records for the apex (`@`): `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
- Optional **AAAA** records for `@`: `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`
- Add a **CNAME** record `www` → `joe-stadler.github.io`

DNS changes can take from minutes to a day. When GitHub's Pages settings show the domain as verified, tick **Enforce HTTPS**.

## 4. Cancel the Squarespace subscription

Do this only after the new site works. Cancel the *website plan*, but keep the *domain* (check in Squarespace that the domain has its own renewal and is not tied to the plan, and that its renewal price suits you; you can also transfer it to another registrar).

## 5. Everyday editing

| What | File |
|---|---|
| Name, site settings | `_config.yml` |
| Home page text, subtitle, photo | `_pages/about.md`, `assets/img/prof_pic.jpg` |
| Publications | `_bibliography/papers.bib` |
| CV | `_data/cv.yml` (and an optional PDF in `assets/pdf/`) |
| Outreach cards | files in `_projects/` (one per card) |
| News on the home page | files in `_news/` |
| Blog posts | files in `_posts/`, named `YYYY-MM-DD-title.md` |
| Social links | `_data/socials.yml` |

## Things to finish

- Add your institution/position (see the comment in `_pages/about.md`) and your CV details.
- The images on the outreach cards are schematic illustrations, not observations. Replace them with your own ALMA images when you want (keep a credit line).
- `_pages/impressum.md` is an unpublished template. A public site run from Germany usually needs a legal notice; fill it in, set `published: true`, and set `impressum_path: /impressum/` in `_config.yml`.
- Your email address is not shown anywhere on the site. Add it to `_data/socials.yml` only if you want it public.
