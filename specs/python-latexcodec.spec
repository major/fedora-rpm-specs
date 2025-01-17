Name:           python-latexcodec
Version:        3.0.0
Release:        %autorelease
Summary:        Lexer and codec to work with LaTeX code in Python

License:        MIT
URL:            https://latexcodec.readthedocs.io/
VCS:            git:https://github.com/mcmtroffaes/latexcodec.git
BuildArch:      noarch
Source:         %pypi_source latexcodec
# Fix the build with python 3.13
# See https://github.com/mcmtroffaes/latexcodec/issues/98
Patch:          %{name}-python3.13.patch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist sphinx}

%description
This package contains a lexer and codec to work with LaTeX code in Python.

%package -n python3-latexcodec
Summary:        Lexer and codec to work with LaTeX code in Python

%description -n python3-latexcodec
This package contains a lexer and codec to work with LaTeX code in Python.

%package doc
# The content is MIT.  Other licenses are due to files copied in by Sphinx.
# _static/basic.css: BSD-2-Clause
# _static/classic.css: BSD-2-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/sidebar.js: BSD-2-Clause
# _static/sphinx_highlight.js: BSD-2-Clause
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        MIT AND BSD-2-Clause
Summary:        Documentation for %{name}

%description doc
Documentation for %{name}.

%prep
%autosetup -n latexcodec-%{version} -p1

%conf
# Update the sphinx theme name
sed -i 's/default/classic/' doc/conf.py

# Use local objects.inv for intersphinx
sed -i "s|\('http://docs\.python\.org/', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" doc/conf.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
PYTHONPATH=$PWD make -C doc html
rm -f doc/_build/html/.buildinfo
rst2html --no-datestamp LICENSE.rst LICENSE.html

%install
%pyproject_install
%pyproject_save_files -l latexcodec

%check
%pytest -v

%files -n python3-latexcodec -f %{pyproject_files}

%files doc
%license LICENSE.html
%doc doc/_build/html/*

%changelog
%autochangelog
