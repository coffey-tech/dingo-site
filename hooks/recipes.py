"""Lists every page in docs/recipes/ on the Recipes index (overrides/recipes-index.html).

New recipe files show up there automatically; nothing to add to mkdocs.yml.
"""

_files = None


def on_files(files, config):
	global _files
	_files = files
	return files


def total_minutes(meta):
	if meta.get('total_minutes'):
		return meta['total_minutes']
	return (meta.get('prep_minutes') or 0) + (meta.get('cook_minutes') or 0) or None


def on_page_context(context, page, config, nav):
	if page.file.src_uri != 'recipes/index.md':
		return context
	recipes = []
	for f in _files.documentation_pages():
		if not f.src_uri.startswith('recipes/') or f.src_uri == 'recipes/index.md' or f.page is None:
			continue
		meta = f.page.meta
		recipes.append(dict(
			title=meta.get('title') or f.page.title,
			url=f.page.url,
			description=meta.get('description'),
			category=meta.get('category'),
			cuisine=meta.get('cuisine'),
			total_minutes=total_minutes(meta),
		))
	context['recipes'] = sorted(recipes, key=lambda r: (r['title'] or '').lower())
	return context
