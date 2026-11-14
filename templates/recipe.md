---
# ──────────────────────────────────────────────────────────────────────────────
# NEW RECIPE TEMPLATE
# 1. Copy this file to docs/recipes/<short-name>.md  (e.g. docs/recipes/chicken-tacos.md)
#    The file name becomes the URL: dingo-meal-planner.com/recipes/chicken-tacos/
# 2. Fill in the fields below. Delete the example values. Lines starting with # are comments.
# 3. Preview with `.venv/bin/mkdocs serve`, then commit and push.
#
# The page AND the data Dingo imports are both built from these fields, so you
# only write the recipe once. Don't add a recipe in the Markdown body below.
#
# YAML tips: if a value contains a colon followed by a space (e.g. "Tip: stir"),
# or starts with a quote, [, {, &, * or #, wrap the whole value in double quotes.
# ──────────────────────────────────────────────────────────────────────────────

template: recipe.html            # leave as is

title: Weeknight Chicken Tacos   # recipe name in Dingo
description: Smoky, juicy chicken tacos on the table in 35 minutes.   # shown on the page, not imported

category: Dinner                 # Breakfast | Lunch | Dinner | Snack  (Dingo's default categories)
cuisine: Mexican                 # Dingo's "Style": American | BBQ | Italian | Indian | Mexican | Asian | Other

prep_minutes: 15                 # whole minutes
cook_minutes: 20
total_minutes:                   # leave blank to use prep + cook; fill in if there's resting/marinating time
servings: 4                      # shown on the page, not imported

image:                           # optional: put the photo in docs/assets/recipes/, then e.g. assets/recipes/chicken-tacos.jpg

# Ingredients: one per line, written as  QUANTITY  UNIT  ITEM
#   Units Dingo understands: tsp, Tbsp, cup, lb/lbs, oz, g, kg, ml, l, clove, can,
#   pinch, dash, slice, package, pint, quart (plurals and spelled-out forms are fine)
#   Quantities: 2, 1.5, 1/2, 1 1/2 or ½ all work.
#   Put sizes AFTER the unit:  "1 can (14 oz) diced tomatoes"  not  "1 (14 oz) can diced tomatoes"
#   No amount? Just the item:  "salt, to taste"
#   No unit? Quantity then item:  "2 limes"
ingredients:
  - 1 1/2 lbs boneless chicken thighs
  - 1 Tbsp chili powder
  - 1 tsp ground cumin
  - 2 cloves garlic, minced
  - 2 Tbsp olive oil
  - 8 small corn tortillas
  - 2 limes
  - salt, to taste

# Steps: in order. "name" is an optional short title for the step; "text" is required.
#   A step like "Preheat oven to 425°F" also fills in Dingo's Preheat field.
#   For a long step, use  text: >-  and continue on indented lines below it.
steps:
  - name: Season
    text: Toss the chicken with the chili powder, cumin, garlic, oil and a big pinch of salt.
  - text: Preheat oven to 425°F.
  - name: Roast
    text: Spread the chicken on a sheet pan and roast for 18 to 20 minutes, until cooked through.
  - name: Serve
    text: >-
      Slice the chicken, squeeze one lime over it, and serve in warm tortillas
      with the other lime cut into wedges.
---

<!-- Optional: anything written here shows under the steps as "Notes" on the web page
     (swaps, storage, tips). It isn't imported into Dingo. Delete this comment if unused. -->
