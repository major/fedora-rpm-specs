Name:           python-pybtex
Version:        0.25.1
Release:        %autorelease
Summary:        BibTeX-compatible bibliography processor written in Python

License:        MIT
URL:            https://pybtex.org/
VCS:            git:https://bitbucket.org/pybtex-devs/pybtex.git
Source:         %pypi_source pybtex

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(generate_buildrequires): -x doc,test
BuildOption(install): -l pybtex

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-docs

%global common_desc %{expand:
Pybtex is a BibTeX-compatible bibliography processor written in Python.
Pybtex aims to be 100%% compatible with BibTeX.  It accepts the same
command line options, fully supports BibTeX’s .bst styles and produces
byte-identical output.

Additionally:
- Pybtex is Unicode-aware.
- Pybtex supports bibliography formats other than BibTeX.
- It is possible to write formatting styles in Python.
- As a bonus, Pythonic styles can produce HTML, Markdown and other
  markup besides the usual LaTeX.
Pybtex also includes a Python API for managing bibliographies from Python.}

%description %common_desc

%package -n python3-pybtex
Summary:        BibTeX-compatible bibliography processor written in Python

%description -n python3-pybtex %common_desc

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
%autosetup -n pybtex-%{version}

%conf
# Remove useless shebang
sed -i '\@/usr/bin/env python@d' pybtex/cmdline.py

# Fix shebangs
%py3_shebang_fix docs/generate_manpages.py \
           pybtex/bibtex/runner.py \
           pybtex/charwidths/make_charwidths.py \
           pybtex/database/{convert,format}/__main__.py \
           pybtex/__main__.py \
           setup.py

# Use local objects.inv for intersphinx
sed -e "s|\('https://docs\.python\.org/3/', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" \
    -i docs/source/conf.py

%build -a
# Build documentation
# Workaround for pygments 2.13.  See bz 2127371.
cat >> pybtex.egg-info/entry_points.txt << EOF

[pygments.styles]
pybtex = pybtex_doctools.pygments:PybtexStyle

[pygments.lexers]
bibtex-pybtex = pybtex_doctools.pygments:BibTeXLexer
bst-pybtex = pybtex_doctools.pygments:BSTLexer
EOF

PYTHONPATH=$PWD:$PWD/build/lib:$PWD/docs/pybtex_doctools make -C docs html man
rm -f docs/build/html/.buildinfo

%install -a
mkdir -p %{buildroot}%{_mandir}/man1
cp -p docs/build/man/*.1 %{buildroot}%{_mandir}/man1
echo ".so man1/pybtex.1" > %{buildroot}%{_mandir}/man1/pybtex-convert.1
echo ".so man1/pybtex.1" > %{buildroot}%{_mandir}/man1/pybtex-format.1

pushd %{buildroot}%{python3_sitelib}
rm -fr custom_fixers tests
chmod a+x pybtex/bibtex/runner.py pybtex/charwidths/make_charwidths.py \
      pybtex/database/{convert,format}/__main__.py pybtex/__main__.py
popd

%check
%pytest -v

%files -n python3-pybtex -f %{pyproject_files}
%doc README
%{_bindir}/pybtex*
%{_mandir}/man1/pybtex*

%files doc
%doc CHANGES docs/build/html

%changelog
%autochangelog
