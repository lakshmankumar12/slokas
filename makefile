
srcdir=$(PWD)/src
outfile := sooktas.pdf
infile := sooktas.tex
basename := $(patsubst %.pdf,%,$(outfile))

all:
	( cd $(srcdir) && rm $(outfile) && \
	docker run --rm -v $(srcdir):/data moss_xelatex_fonts xelatex -interaction=batchmode -no-pdf-info -jobname=$(basename) -output-directory=./ $(infile) ) || true
	test -f $(srcdir)/$(outfile)
