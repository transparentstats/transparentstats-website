# Transparent statistics in HCI

This repo contains docs and the website for the transparent statistics in HCI group.

- [web/](web/): The root directory of [transparentstatistics.org](http://transparentstatistics.org/).
  Files in this directory use a hacked-together setup that I (Matt) use for my own website and don't
  expect others to want to deal with. 
  
  If you do want to deal with it, `build.py` compiles `css/main.less` into `css/main.css`
  and takes the files ending in `-less.html` and translates them into files ending in `.html`, rewriting
  their CSS links to use `css/main.css` instead of `css/main.less`. The `-less.html` files can be used
  in development without compilation (they use a javascript LESS compiler in-browser), and the `.html`
  files are used in production. Apologies for the terrible.
    
- [papers/](papers/): Papers and abstracts
