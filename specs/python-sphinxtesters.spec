Name:           python-sphinxtesters
Version:        0.2.4
Release:        %autorelease
Summary:        Utilities for testing Sphinx extensions

# The code is BSD-2-Clause.  Other licenses are due to files copied in by
# Sphinx.
# _static/alabaster.css: BSD-3-Clause
# _static/basic.css: BSD-2-Clause
# _static/custom.css: BSD-3-Clause
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
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://github.com/matthew-brett/sphinxtesters
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/sphinxtesters-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(generate_buildrequires): -x doc,test
BuildOption(install): -l sphinxtesters

%description
This package contains utilities for testing Sphinx extensions.

%package -n     python3-sphinxtesters
Summary:        Utilities for testing Sphinx extensions
Requires:       %{py3_dist sphinx}

%description -n python3-sphinxtesters
This package contains utilities for testing Sphinx extensions.

%prep
%autosetup -n sphinxtesters-%{version} -p1

%build -a
rst2html --no-datestamp README.rst README.html
PYTHONPATH=$PWD sphinx-build doc build
rm -fr build/.{buildinfo,doctrees,nojekyll}

%check
%pytest -v

%files -n python3-sphinxtesters -f %{pyproject_files}
%doc README.html build

%changelog
%autochangelog
