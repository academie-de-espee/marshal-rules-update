# marshal-rules-update

To get the base form markdown:

```
    pdftohtml ./Atlantian\ Book\ of\ Policy\ 2017-02-01.pdf -stdout -enc UTF-8 -nodrm -noframes | pandoc -f html --wrap=none -t markdown | tail -n 4478 | head -n 2831 > handbook.md
    python convert.py handbook.md > temp && mv temp handbook.md
```

To get PDF from current markdown:

```
    pandoc -N -V "geometry:left=1.5cm,right=1.5cm,top=1cm,bottom=2cm" -H header.tex handbook.md --toc -o handbook.pdf
```


# PREREQS
```
sudo apt install pandoc texlive-xetex
```

