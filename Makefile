all: clean
	htlatex faif-2.0.tex
	python2.7 process_html.py
clean:
	rm -rf *.html
	rm -rf *.log
	rm -rf *.aux
