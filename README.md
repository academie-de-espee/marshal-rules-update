# marshal-rules-update

## PREREQS
```
sudo apt install pandoc texlive-xetex
```

## Build instructions
```
pandoc -N -V "geometry:left=1.5cm,right=1.5cm,top=1cm,bottom=2cm" -H header.tex handbook.md --toc -o handbook.pdf
```
