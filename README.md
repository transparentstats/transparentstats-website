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


## Edit a page
1. Clone this repository locally.
2. Open the Rproj project in RStudio. You may need to run `install.packages('blogdown')` the first time.
3. Open the Rmd file in `content/` or `content/blog/`
4. Save. And Click the "Knit" above the editor.
5. Click `Build Website` in the `Build` tab on the right.
6. Commit the changes to git and push to github.
7. You may need to do a PR and merge if you've forked the repo.


## Add a page

1. Clone this repository locally.
2. Open the Rproj project in RStudio. You may need to run `install.packages('blogdown')` the first time.
3. Add a new Rmd file to `content/` or `content/blog/`
4. For a blog post, make sure to copy the date format in the filename.
5. Copy the header content from one of the existing files, and add your content.
6. Save. And Click the "Knit" above the editor.
7. Click `Build Website` in the `Build` tab on the right.
8. Commit the changes to git and push to github.
9. You may need to do a PR and merge if you've forked the repo.

## Change the header links

See `config.toml`

## Deploying

The deployed version of the website is built automatically by Netlify based on the `master` branch of this repository on Github. Therefore, please do not push things to master that you haven't tested :).
