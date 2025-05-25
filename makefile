srcdir=$(PWD)/src

# Document definitions
DOCS := sooktas mahanyasam
sooktas_infile := sooktas.tex
mahanyasam_infile := mahanyasam.tex

# Generic function to build any document
define build_doc
	( cd $(srcdir) && rm -f $(1).pdf && \
		docker run --rm -v $(srcdir):/data moss_xelatex_fonts xelatex -interaction=batchmode -no-pdf-info -jobname=$(1) -output-directory=./ $(2) ) || true
	test -f $(srcdir)/$(1).pdf
endef

# Individual targets
sooktas:
	$(call build_doc,sooktas,$(sooktas_infile))

mahanyasam:
	$(call build_doc,mahanyasam,$(mahanyasam_infile))

# Build all documents
all: $(DOCS)

clean:
	rm -f src/*log src/*aux

.PHONY: sooktas mahanyasam all clean
