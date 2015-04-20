all: clean
	htlatex faif.tex "htlatex,xhtml,charset=utf-8,NoFonts,fonts" " -cunihtf -utf8"
	#python2.7 process_html.py
	pdflatex faif.tex
clean:
	rm -rf *.html
	rm -rf *.log
	rm -rf *.aux
	rm -rf faif.4ct	faif.4tc faif.cjk faif.css faif.dvi faif.ent faif.idv faif.idx faif.lg faif.out faif.pdf faif.tmp faif.toc faif.xref faif0x.png faif1x.png faif2x.png faif3x.png faif4x.png faif5x.png

