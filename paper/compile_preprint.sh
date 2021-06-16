cat preprint.yml > preprint.md
tail -n +89 paper.md >> preprint.md
pandoc --filter pandoc-citeproc --bibliography=paper.bib \
    --variable papersize=a4paper -s preprint.md -o preprint.pdf \
    --lua-filter=/Users/kelly/.pandoc/scholarly-metadata.lua \
    --lua-filter=/Users/kelly/.pandoc/author-info-blocks.lua \
    --pdf-engine=xelatex -V geometry:margin=1in
rm preprint.md
