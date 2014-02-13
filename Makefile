all: clean
	htlatex faif-1.0.tex
	python2.7 process_html.py
	pdflatex faif-1.0.tex
clean:
	rm -rf *.html
	rm -rf *.log
	rm -rf *.aux
