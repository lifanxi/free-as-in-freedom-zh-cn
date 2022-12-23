all: pdf html

html:
	htxelatex faif-2.0.tex
pdf:
	xelatex faif-2.0.tex
clean:
	rm -f *.html *.pdf
	rm -f *.log *.aux
	rm -f faif-2.0.4ct faif-2.0.4tc faif-2.0.css faif-2.0.dvi faif-2.0.ent faif-2.0.xref
	rm -f faif-2.0.fdb_latexmk faif-2.0.fls faif-2.0.idv faif-2.0.idx faif-2.0.ilg
	rm -f faif-2.0.ind faif-2.0.lg faif-2.0.out faif-2.0.tmp faif-2.0.toc faif-2.0.xdv
