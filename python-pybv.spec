# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
%bcond doc_pdf 1

Name:           python-pybv
Version:        0.7.5
Release:        %autorelease
Summary:        A lightweight I/O utility for the BrainVision data format

License:        BSD-3-Clause
URL:            https://pybv.readthedocs.io/en/stable/
# A filtered source archive, obtained by (see Source1):
#
#   ./get_source %%{version}
#
# is required because specification/ contains a PDF file,
# BrainVisionCoreDataFormat_1-0.pdf, with unclear license terms.
#
# The unfiltered base source URL would be:
#
# https://github.com/bids-standard/pybv/archive/v%%{version}/pybv-%%{version}.tar.gz
#
# We have asked upstream to stop distributing the specification/ directory in
# PyPI sdists: https://github.com/bids-standard/pybv/pull/106
Source0:        pybv-%{version}-filtered.tar.xz
Source1:        get_source

# Replace deprecated mne.utils.requires_version
# https://github.com/bids-standard/pybv/pull/105
Patch:          https://github.com/bids-standard/pybv/pull/105.patch

# Fix version quote handling
# This is a partial backport of:
# https://github.com/bids-standard/pybv/commit/11b47b7a5a21230c1d7fd208e27bbd3ae721cc28
Patch:          0001-Fix-version-quote-handling.patch

BuildArch:      noarch
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

%if %{with doc_pdf}
# Extra dependencies for building PDF instead of HTML
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  /usr/bin/xindy
BuildRequires:  tex-xetex-bin
%endif

%global common_description %{expand:
pybv is a lightweight I/O utility for the BrainVision data format.

The BrainVision data format is a recommended data format for use in the Brain
Imaging Data Structure.}

%description %{common_description}


%package -n python3-pybv
Summary:        %{summary}

%description -n python3-pybv %{common_description}


%pyproject_extras_subpkg -n python3-pybv export


%package        doc
Summary:        Documentation for python-pybv

%description    doc %{common_description}


%prep
%autosetup -n pybv-%{version} -p1

# Filter unwanted dev dependencies:
#
# - linters
# - coverage analysis and other unnecessary pytest plugins
# - formatters etc.
# - documentation dependencies (if building docs is disabled)
#
# See also:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r \
    -e 's/^(check-manifest|flake8(-.*)?|pycodestyle|pre-commit)\b/# &/' \
    -e 's/^(pytest-(cov|sugar))/# &/' \
    -e 's/^(black|isort)/# &/' \
    %{?!with_doc_pdf:-e 's/^(sphinx(-(copybutton))?|numpydoc)\b/# &/'} \
    requirements-dev.txt | tee requirements-dev-filtered.txt

cat >>docs/conf.py <<'EOF'
# We can’t resolve intersphinx mapping URLs in an offline build.
intersphinx_mapping.clear()
EOF
# Since pdflatex cannot handle Unicode inputs in general:
echo "latex_engine = 'xelatex'" >> docs/conf.py


%generate_buildrequires
%pyproject_buildrequires -x export -r requirements-dev-filtered.txt


%build
%pyproject_wheel
%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/_build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files -l pybv


%check
%{pytest}


%files -n python3-pybv -f %{pyproject_files}


%files doc
%license LICENSE
%doc CITATION.cff
%doc README.rst
# The changelog is included in the PDF documentation, but it’s useful to
# package it as a text file too.
%doc docs/changelog.rst

%if %{with doc_pdf}
%doc docs/_build/latex/pybv.pdf
%endif


%changelog
%autochangelog
