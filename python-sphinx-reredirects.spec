Name:           python-sphinx-reredirects
Version:        0.1.1
Release:        2%{?dist}
Summary:        Handle redirects for moved pages in Sphinx documentation

License:        BSD-3-Clause
URL:            https://documatt.gitlab.io/sphinx-reredirects/
Source0:        https://gitlab.com/documatt/sphinx-reredirects/-/archive/v%{version}/sphinx-reredirects-v%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist sphinx-documatt-theme}

%global _description %{expand:
Sphinx-reredirects is the extension for Sphinx documentation projects
that handles redirects for moved pages.  It generates HTML pages with
meta refresh redirects to the new page location to prevent 404 errors if
you rename or move your documents.}

%description %_description

%package     -n python3-sphinx-reredirects
Summary:        Handle redirects for moved pages in Sphinx documentation

%description -n python3-sphinx-reredirects %_description

%package        doc
Summary:        Documentation for %{name}
# This project is BSD-3-Clause.  The Javascript and CSS bundled with the
# documentation has the following licenses:
# _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# _static/basic.css: BSD-2-Clause
# _static/css: MIT
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/img: MIT
# _static/jquery*.js: MIT
# _static/js: MIT
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/underscore*.js: MIT
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        BSD-3-Clause AND BSD-2-Clause AND MIT

%description    doc
Documentation for %{name}.

%prep
%autosetup -n sphinx-reredirects-v%{version}

# Do not pin to specific package versions
sed -i 's/pytest==/pytest>=/;s/sphinx==/sphinx>=/' tox.ini test-requirements.txt

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

# Build documentation
PYTHONPATH=$PWD sphinx-build -b html docs html
rm -rf html/{.buildinfo,.doctrees}
rst2html --no-datestamp README.rst README.html

%install
%pyproject_install
%pyproject_save_files sphinx_reredirects

%check
%tox

%files -n python3-sphinx-reredirects -f %{pyproject_files}
%doc README.html

%files doc
%doc html
%license LICENSE

%changelog
* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 0.1.1-2
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 24 2022 Jerry James <loganjerry@gmail.com> - 0.1.1-1
- Initial RPM
