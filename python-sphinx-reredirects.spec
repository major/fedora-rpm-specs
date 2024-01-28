Name:           python-sphinx-reredirects
Version:        0.1.3
Release:        3%{?dist}
Summary:        Handle redirects for moved pages in Sphinx documentation

License:        BSD-3-Clause
URL:            https://documatt.com/sphinx-reredirects/
Source0:        https://github.com/documatt/sphinx-reredirects/archive/v%{version}/sphinx-reredirects-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Sphinx-reredirects is the extension for Sphinx documentation projects
that handles redirects for moved pages.  It generates HTML pages with
meta refresh redirects to the new page location to prevent 404 errors if
you rename or move your documents.}

%description %_description

%package     -n python3-sphinx-reredirects
Summary:        Handle redirects for moved pages in Sphinx documentation
# See https://pagure.io/packaging-committee/issue/1312.
# A duplicate python3-sphinx_reredirects was created that conflicts with this one.
# We Obsolete the duplicate and add Provides for python3-sphinx_reredirects to
# make this one easier to find.
%py_provides    python3-sphinx_reredirects
# Remove in Fedora 42+
Obsoletes:      python3-sphinx_reredirects < 0.1.2-3

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
%autosetup -n sphinx-reredirects-%{version}

# Do not pin to specific package versions
sed -i 's/==/>=/g' docs/requirements.txt test-requirements.txt tox.ini

%generate_buildrequires
%pyproject_buildrequires -t docs/requirements.txt

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
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Nov  3 2023 Jerry James <loganjerry@gmail.com> - 0.1.3-1
- Version 0.1.3
- New project URLs

* Mon Oct 16 2023 Maxwell G <maxwell@gtmx.me> - 0.1.2-4
- Obsolete duplicate python3-sphinx_reredirects package

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.1.2-2
- Rebuilt for Python 3.12

* Thu May 18 2023 Jerry James <loganjerry@gmail.com> - 0.1.2-1
- Version 0.1.2

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 0.1.1-2
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 24 2022 Jerry James <loganjerry@gmail.com> - 0.1.1-1
- Initial RPM
