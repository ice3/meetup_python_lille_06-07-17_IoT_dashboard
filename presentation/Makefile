REVEAL_DIR_JS = ./reveal.js/js
REVEAL_DIR_CSS = ./reveal.js/css
COPY_FILES = $(REVEAL_DIR_CSS)/reveal.min.css $(REVEAL_DIR_JS)/reveal.min.js

reveal.js:
	wget -N https://github.com/hakimel/reveal.js/archive/master.tar.gz
	tar xzvf master.tar.gz
	mv reveal.js-master reveal.js
	rm master.tar.gz

index.html: slides.md
	pandoc -t revealjs -s --slide-level=2 -o index.html $<

$(REVEAL_DIR_CSS)/reveal.min.css: $(REVEAL_DIR_CSS)/reveal.css
	cp $< $@

$(REVEAL_DIR_JS)/reveal.min.js: $(REVEAL_DIR_JS)/reveal.js
	cp $< $@

all: index.html $(COPY_FILES)
	python -m SimpleHTTPServer

clean:
	rm -f master.tar.gz
	rm -rf reveal.js
	rm -f index.html
	rm -f myslides.html
	rm -f .reveal.dl
