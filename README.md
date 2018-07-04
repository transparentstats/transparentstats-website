# Transparent statistics in HCI website

This repo contains the website for the transparent statistics in HCI group at [transparentstatistics.org](http://transparentstatistics.org/).

The website is created and served using [blogdown](https://bookdown.org/yihui/blogdown/). I recommend using RStudio to create and edit content. You can then use `blogdown::serve_site()` in R to preview the website locally. See the [blogdown documentation](https://bookdown.org/yihui/blogdown/) for more information.

The directories of interest are probably:

- [content/](content/): The directory containing most of the dynamic content. I
  recommend writing content as `.Rmd` files, which will be compiled into HTML when
  the website is built. **Do not edit HTML files directly in this folder.**

- [content/_index.Rmd](content/_index.Rmd): The source file for the home page.

- [content/blog/*.Rmd](content/blog/): The source files for blog posts.

- [static/](static/): The directory containing static content.

- [public/](public/): The directory output directory, into which the contents of `content/` (after being compiled)
  and the contents of `static/` are copited when the website is built. **Do not edit directly**.
  
- [old-web/](old-web/): The root directory of the old website. 
  Files in this directory use a hacked-together setup that I (Matt) use for my own website and don't
  expect others to want to deal with. 
  
  If you do want to deal with it, `build.py` compiles `css/main.less` into `css/main.css`
  and takes the files ending in `-less.html` and translates them into files ending in `.html`, rewriting
  their CSS links to use `css/main.css` instead of `css/main.less`. The `-less.html` files can be used
  in development without compilation (they use a javascript LESS compiler in-browser), and the `.html`
  files are used in production. Apologies for the terrible.
