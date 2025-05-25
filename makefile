
srcdir=$(PWD)/src
outfile := sooktas.pdf
infile := sooktas.tex
basename := $(patsubst %.pdf,%,$(outfile))

sooktas:
	( cd $(srcdir) && rm $(outfile) && \
	docker run --rm -v $(srcdir):/data moss_xelatex_fonts xelatex -interaction=batchmode -no-pdf-info -jobname=$(basename) -output-directory=./ $(infile) ) || true
	test -f $(srcdir)/$(outfile)

mahanyasam_outfile := mahanyasam.pdf
mahanyasam_infile := mahanyasam.tex
mahanyasam_basename := $(patsubst %.pdf,%,$(mahanyasam_outfile))

mahanyasam:
	( cd $(srcdir) && rm -f $(mahanyasam_outfile) && \
		docker run --rm -v $(srcdir):/data moss_xelatex_fonts xelatex -interaction=batchmode -no-pdf-info -jobname=$(mahanyasam_basename) -output-directory=./ $(mahanyasam_infile) ) || true
	test -f $(srcdir)/$(mahanyasam_outfile)

clean:
	rm -f src/*log src/*aux
