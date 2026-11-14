# dingo-meal-planner.com

Website for the Dingo Meal Planner iPhone app, built with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) and published to GitHub Pages by `.github/workflows/pages.yml` on every push to `main`.

```sh
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve          # preview at http://127.0.0.1:8000
.venv/bin/mkdocs build --strict # what CI runs
```

- `docs/index.md` uses the custom landing template in `overrides/home.html`.
- `docs/support.md` and `docs/privacy.md` are the App Store Support and Privacy Policy URLs. Keep their paths stable.
- New recipe: copy `templates/recipe.md` to `docs/recipes/<short-name>.md` and fill in the front matter. The page and the schema.org Recipe JSON-LD that Dingo's **Import Recipe** reads are both generated from it (`overrides/recipe.html`); `hooks/recipes.py` adds it to the Recipes index.
- Blog posts go in `docs/blog/posts/` with a `date:` in the front matter.
- `docs/privacy.html` redirects the old `/privacy.html` URL to `/privacy/`.
