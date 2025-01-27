# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as substitute.
%bcond doc_pdf 1

%global forgeurl https://github.com/holgern/pyedflib

%global _description %{expand:
pyEDFlib is a python library to read/write EDF+/BDF+ files based on EDFlib.
EDF means European Data Format and was firstly published Kemp1992. 
In 2003, an improved version of the file protocol named EDF+ has 
been published and can be found at Kemp2003.}

Name:           python-pyedflib
Version:        0.1.39
Release:        %autorelease
Summary:        Python library to read/write EDF+/BDF+ files, based on EDFlib
%forgemeta
# The entire source is BSD-3-Clause, except:
#   BSD-2-Clause: pyedflib/_extensions/edf.pxi
License:        BSD-3-Clause AND BSD-2-Clause
URL:            %forgeurl
Source:         %forgesource

# https://bugzilla.redhat.com/show_bug.cgi?id=2027046
ExcludeArch:    s390x

# Uses a forked copy of EDFlib (https://gitlab.com/Teuniz/EDFlib)
# https://github.com/holgern/pyedflib/issues/149
# Version number: pyedflib/_extensions/c/edflib.c, EDFLIB_VERSION
%global edflib_version 1.17
Provides:       bundled(edflib) = %{edflib_version}

%description %_description

%package -n python3-pyedflib
Summary:        %{summary}

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist toml-adapt}
BuildRequires:  %{py3_dist pytest}

%description -n python3-pyedflib %_description

%package doc
Summary:        Documentation and examples for pyedflib
BuildArch:      noarch

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(numpydoc)
%endif

# Required by some demos/examples:
Suggests:       python3dist(matplotlib)
Suggests:       python3dist(scipy)

%description doc
%{summary}.

%prep
%autosetup -p1 -n pyedflib-%{version}
# Avoid “too deeply nested” error generating LaTeX from Sphinx:
# https://github.com/sphinx-doc/sphinx/issues/777
cat >> doc/source/conf.py <<'EOF'
latex_elements = {
  'preamble': r'\usepackage{enumitem}\setlistdepth{99}',
}
EOF

# Remove shebangs from demos. The find-then-modify pattern keeps us from
# discarding mtimes on sources that do not need modification.
find demo -type f -exec \
    gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r -t sed -r -i '1{/^#!/d}'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}/build/lib.%{python3_platform}-cpython-%{python3_version_nodots}" \
    %make_build -C doc latex SPHINXOPTS='%{?_smp_mflags}'
%make_build -C doc/build/latex LATEXMKOPTS='-quiet'
%endif

%install
%pyproject_install
%pyproject_save_files -l pyedflib

%check
%pytest
# Make sure we are still indicating the correct bundled edflib version:
grep -E "^#define[[:blank:]]+EDFLIB_VERSION[[:blank:]]+\($(
  echo '%{edflib_version}' | tr -d '.'
)\)[[:blank:]]*\$" 'pyedflib/_extensions/c/edflib.c'

%files -n python3-pyedflib -f %{pyproject_files}
%doc README.rst

%files doc
%license LICENSE
%if %{with doc_pdf}
%doc doc/build/latex/PyEDFlib.pdf
%endif
%doc demo

%changelog
%autochangelog
