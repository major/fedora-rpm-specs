%global _docdir_fmt %{name}
%global giturl  https://github.com/sphinx-doc/sphinx-autobuild

Name:           python-sphinx-autobuild
Version:        2024.10.03
Release:        %autorelease
Summary:        Autobuild a Sphinx directory when a change is detected

License:        MIT
URL:            https://sphinx-autobuild.readthedocs.io/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/sphinx-autobuild-%{version}.tar.gz
# Fix --help invocations
Patch:          %{giturl}/pull/199.patch

BuildArch:      noarch

BuildRequires:  help2man
BuildRequires:  python3-devel

%description
Rebuild Sphinx documentation on changes, with live-reload in the browser.

%package     -n python3-sphinx-autobuild
Summary:        Autobuild a Sphinx directory when a change is detected

%description -n python3-sphinx-autobuild
Rebuild Sphinx documentation on changes, with live-reload in the browser.

%package        doc
# The content is MIT.  Other licenses are due to files copied in by Sphinx.
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
License:        MIT AND BSD-2-Clause AND BSD-3-Clause
Summary:        Documentation for sphinx-autobuild

%description    doc
Documentation for sphinx-autobuild.

%prep
%autosetup -n sphinx-autobuild-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel
rst2html --no-datestamp NEWS.rst NEWS.html
rst2html --no-datestamp README.rst README.html

# Build the documentation
mkdir html
sphinx-build -b html docs html
rm -rf html/{.buildinfo,.doctrees}

%install
%pyproject_install
%pyproject_save_files -L sphinx_autobuild

# Install a man page
mkdir -p %{buildroot}%{_mandir}/man1
%{py3_test_envvars} help2man -N %{buildroot}%{_bindir}/sphinx-autobuild \
  -n 'Autobuild a Sphinx directory when a change is detected' \
  > %{buildroot}%{_mandir}/man1/sphinx-autobuild.1

%check
%pytest -v

%files -n python3-sphinx-autobuild -f %{pyproject_files}
%doc AUTHORS.rst NEWS.html README.html
%license LICENSE.rst
%{_bindir}/sphinx-autobuild
%{_mandir}/man1/sphinx-autobuild.1*

%files doc
%doc html

%changelog
%autochangelog
