all: clean
	htlatex faif-1.0.tex
	python2.7 process_html.py
	pdflatex faif-1.0.tex
clean:
	rm -rf *.html
	rm -rf *.log
	rm -rf *.aux
	rm -rf faif-1.0.4ct	faif-1.0.4tc faif-1.0.cjk faif-1.0.css faif-1.0.dvi faif-1.0.ent faif-1.0.idv faif-1.0.idx faif-1.0.lg faif-1.0.out faif-1.0.pdf faif-1.0.tmp faif-1.0.toc faif-1.0.xref faif-1.00x.png faif-1.01x.png faif-1.02x.png faif-1.03x.png faif-1.04x.png faif-1.05x.png

