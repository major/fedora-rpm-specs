# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc 1

Name:           python-docx
Version:        1.0.1
Release:        %autorelease
Summary:        Create and modify Word documents with Python

# SPDX
License:        MIT
URL:            https://python-docx.readthedocs.io/en/latest/
# We MUST use the PyPI tarball; the GitHub tarball includes material under ref/
# (PDFs of ISO/IEC standards) for which redistribution may be prohibited.
Source0:        %{pypi_source python-docx}
# Include requirements files in PyPI sdist
# https://github.com/python-openxml/python-docx/pull/1259
Source1:        https://github.com/python-openxml/python-docx/raw/v%{version}/requirements.txt
Source2:        https://github.com/python-openxml/python-docx/raw/v%{version}/requirements-test.txt

# Add build backend in pyproject.toml
# https://github.com/python-openxml/python-docx/pull/1258
Patch:          https://github.com/python-openxml/python-docx/pull/1258.patch

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  dos2unix

# Extra dependencies for documentation
%if %{with doc}
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


%if %{with doc}
%package        doc
Summary:        Documentation for python-docx

%description    doc %{common_description}
%endif


%prep
%autosetup -p1

cp -p '%{SOURCE1}' '%{SOURCE2}' .

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^(ruff)\b/# &/' requirements-test.txt

# We don’t want to package https://github.com/armstrong/armstrong_sphinx (and
# shouldn’t use the bundled copy), so we just switch the documentation theme
# from “armstrong” to the built-in “alabaster”. The result seems similarly
# useful, without the bundling.
rm -rvf docs/_themes
sed -r -i 's/armstrong/alabaster/' docs/conf.py

# Drop intersphinx mappings, since we can’t download remote inventories and
# can’t easily produce working hyperlinks from inventories in local
# documentation packages.
echo 'intersphinx_mapping.clear()' >> docs/conf.py

# Fix a stray CRLF-terminated reStructuredText file:
dos2unix --keepdate docs/dev/analysis/features/table/cell-merge.rst


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel

%if %{with doc}
PYTHONPATH="${PWD}/src" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
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
%if %{without doc}
%doc HISTORY.rst README.md
%endif


%if %{with doc}
%files doc
%license LICENSE
%doc HISTORY.rst README.md
%doc docs/.build/latex/python-docx.pdf
%endif


%changelog
%autochangelog
