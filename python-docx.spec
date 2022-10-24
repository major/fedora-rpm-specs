# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond_without doc_pdf

Name:           python-docx
Version:        0.8.11
Release:        %autorelease
Summary:        Create and modify Word documents with Python

# SPDX
License:        MIT
URL:            https://python-docx.readthedocs.io/en/latest/
# We MUST use the PyPI tarball; the GitHub tarball includes material under ref/
# (PDFs of ISO/IEC standards) for which redistribution may be prohibited.
Source0:        %{pypi_source python-docx}

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  dos2unix

# Extra dependencies for documentation
%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
%endif
 
%global common_description %{expand:
A Python library for creating and updating Microsoft Word (.docx) files.}

%description %{common_description}


%package -n python3-docx
Summary:        %{summary}

%description -n python3-docx %{common_description}


%package        doc
Summary:        Documentation for python-docx

%description    doc %{common_description}


%prep
%autosetup

# We don’t want to package https://github.com/armstrong/armstrong_sphinx (and
# shouldn’t use the bundled copy), so we just switch the documentation theme
# from “armstrong” to the built-in “alabaster”. The result seems similarly
# useful, without the bundling.
rm -rf docs/_themes
sed -r -i 's@armstrong@alabaster@' docs/conf.py

# Drop intersphinx mappings, since we can’t download remote inventories and
# can’t easily produce working hyperlinks from inventories in local
# documentation packages.
echo 'intersphinx_mapping.clear()' >> docs/conf.py

# Fix a stray CRLF-terminated reStructuredText file:
dos2unix docs/dev/analysis/features/table/cell-merge.rst


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel

%if %{with doc_pdf}
%make_build -C docs latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C docs/.build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files docx


%check
%tox

# Fail the build if the tarball accidentally included ISO/IEC standards
# documents that should not have been redistributed. Note that removing these
# in %%prep would not have been good enough.
banned="$(find . -type f -name 'ISO*.pdf')"
if [ -n "${banned}" ]
then
  cat <<EOF
Source included ISO/IEC standards documents, which should not have been
redistributed:

${banned}
EOF
  exit 1
fi
if [ -e 'ref' ]
then
  cat <<EOF
Source had ref/ subdirectory, which has historically included content that
should not be redistributed.
EOF
  exit 1
fi


%files -n python3-docx -f %{pyproject_files}


%files doc
%license LICENSE
%doc HISTORY.rst
%doc README.rst
%if %{with doc_pdf}
%doc docs/.build/latex/python-docx.pdf
%endif


%changelog
%autochangelog
