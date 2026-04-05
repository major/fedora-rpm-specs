%global giturl  https://codeberg.org/pybtex/pybtex

Name:           python-pybtex
Version:        0.26.1
Release:        %autorelease
Summary:        BibTeX-compatible bibliography processor written in Python

License:        MIT
URL:            https://pybtex.org/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}.tar.gz#/pybtex-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(generate_buildrequires): -x doc,test
BuildOption(install): -l pybtex

BuildRequires:  make
BuildRequires:  pytest
BuildRequires:  python3-docs
BuildRequires:  python3-sphinx

%global common_desc %{expand:Pybtex is a BibTeX-compatible bibliography processor written in Python.
Pybtex aims to be 100%% compatible with BibTeX.  It accepts the same command
line options, fully supports BibTeX’s .bst styles and produces byte-identical
output.

Additionally:
- Pybtex is Unicode-aware.
- Pybtex supports bibliography formats other than BibTeX.
- It is possible to write formatting styles in Python.
- As a bonus, Pythonic styles can produce HTML, Markdown and other markup
  besides the usual LaTeX.
Pybtex also includes a Python API for managing bibliographies from Python.}

%description
%common_desc

%package -n python3-pybtex
Summary:        BibTeX-compatible bibliography processor written in Python

%description -n python3-pybtex
%common_desc

%package doc
# The content is MIT.  Other licenses are due to files copied in by Sphinx.
# _static/basic.css: BSD-2-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/sphinx_highlight.js: BSD-2-Clause
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        MIT AND BSD-2-Clause
Summary:        Documentation for python-pybtex

%description doc
Documentation for python-pybtex.

%prep
%autosetup -n pybtex

%generate_buildrequires -a
cd docs/pybtex_doctools
%pyproject_buildrequires

%conf
# Fix shebangs
%py3_shebang_fix docs/generate_manpages.py \
                 src/pybtex/charwidths/make_charwidths.py

# Use local objects.inv for intersphinx
sed -e 's|\("https://docs\.python\.org/3/", \)None|\1"%{_docdir}/python3-docs/html/objects.inv"|' \
    -i docs/source/conf.py

%build -a
# Convert the README
rst2html --no-datestamp README.rst README.html

# Make fake distinfo so we can use pybtex_doctools to build the man pages
cd docs/pybtex_doctools
doctoolsver=$(sed -n 's/version = "\(.*\)"/\1/p' pyproject.toml)
pythonver=$(sed -n 's/requires-python = "\(.*\)"/\1/p' pyproject.toml)
cd -
metadataver=$(sed -n 's/Metadata-Version: \(.*\)/\1/p' %{python3_sitelib}/pygments-*.dist-info/METADATA)
mkdir docs/pybtex_doctools/pybtex_doctools-0.1.0.dist-info
cd docs/pybtex_doctools/pybtex_doctools-0.1.0.dist-info
cat > entry_points.txt << EOF
[pygments.lexers]
bibtex-bst = pybtex_doctools.pygments:BSTLexer
bibtex-pybtex = pybtex_doctools.pygments:BibTeXLexer

[pygments.styles]
pybtex = pybtex_doctools.pygments:PybtexStyle
EOF
cat > METADATA << EOF
Metadata-Version: $metadataver
Name: pybtex_doctools
Version: $doctoolsver
Summary: Documentation utils for pybtex
Author-email: Andrey Golovizin <ag@sologoc.com>
Requires-Python: $pythonver
Requires-Dist: pygments
EOF
cd -

%install -a
# Build documentation
export PYTHONPATH=%{buildroot}%{python3_sitelib}:$PWD/docs/pybtex_doctools
make -C docs html man
rm -f docs/build/html/.buildinfo

mkdir -p %{buildroot}%{_mandir}/man1
cp -p docs/build/man/*.1 %{buildroot}%{_mandir}/man1
echo ".so man1/pybtex.1" > %{buildroot}%{_mandir}/man1/pybtex-convert.1
echo ".so man1/pybtex.1" > %{buildroot}%{_mandir}/man1/pybtex-format.1

%check
%pytest -v

%files -n python3-pybtex -f %{pyproject_files}
%doc README.html
%{_bindir}/pybtex*
%{_mandir}/man1/pybtex*

%files doc
%doc CHANGES docs/build/html

%changelog
%autochangelog
