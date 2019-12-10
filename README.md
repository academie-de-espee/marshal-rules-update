# marshal-rules-update

Any changes commited to master will automatically be built & published here: [Latest version of this document](https://github.com/academie-de-espee/marshal-rules-update/releases)

## PREREQS
```
sudo apt install pandoc texlive-xetex
```

## Build instructions
```
pandoc -N -V "geometry:left=1.5cm,right=1.5cm,top=1cm,bottom=2cm" -H header.tex handbook.md --toc -o handbook.pdf
```
