# Documentation can no longer be built in Fedora due to missing python modules:
# ablog, myst-nb, sphinx-togglebutton
# This also means that doctests cannot be run.
%bcond_with docs

Name:           python-pydata-sphinx-theme
Version:        0.14.2
Release:        1%{?dist}
Summary:        Bootstrap-based Sphinx theme from the PyData community

# This project is BSD-3-Clause.
# The bundled bootstrap JavaScript library is MIT.
License:        BSD-3-Clause and MIT
BuildArch:      noarch
URL:            https://pydata-sphinx-theme.readthedocs.io/
Source0:        https://github.com/pydata/pydata-sphinx-theme/archive/v%{version}/pydata-sphinx-theme-%{version}.tar.gz
# Source1 and Source2 created with ./prepare_vendor.sh
Source1:        pydata-sphinx-theme-%{version}-vendor.tar.xz
Source2:        pydata-sphinx-theme-%{version}-vendor-licenses.txt
%if %{with docs}
# Generating image files requires network access.  Instead, we scrape these from
# https://pydata-sphinx-theme.readthedocs.io/en/latest/_images.  See
# docs/_static/gallery.yaml for a list of images to download.
Source3:        pydata-gallery.tar.xz
%endif
# Fedora-only patch: unbundle the fontawesome fonts
Patch0:         %{name}-fontawesome.patch

BuildRequires:  fontawesome-fonts-all
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  nodejs-devel
BuildRequires:  nodejs-npm
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest-regressions}
BuildRequires:  yarnpkg

Provides:       bundled(js-bootstrap) = 5.3.2

%if %{without docs}
Obsoletes:      %{name}-doc < 0.13.0-1
%endif

%global _description %{expand:
This package contains a Sphinx extension for creating document components
optimized for HTML+CSS.

- The panels directive creates panels of content in a grid layout,
  utilizing both the Bootstrap 4 grid system, and cards layout.

- The link-button directive creates a clickable button, linking to a URL
  or reference, and can also be used to make an entire panel clickable.

- The dropdown directive creates content that can be toggled.

- The tabbed directive creates tabbed content.

- opticon and fa (fontawesome) roles allow for inline icons to be added.

See https://pydata-sphinx-theme.readthedocs.io/ for documentation.}

%description %_description

%package     -n python3-pydata-sphinx-theme
Summary:        Bootstrap-based Sphinx theme from the PyData community
Requires:       fontawesome-fonts-all

%description -n python3-pydata-sphinx-theme %_description

%if %{with docs}
%package        doc
Summary:        Documentation for pydata-sphinx-theme

%description    doc
Documentation for pydata-sphinx-theme.
%endif

%prep
%autosetup -n pydata-sphinx-theme-%{version} -p1 -a1
cp -p %{SOURCE2} .

%if %{with docs}
%setup -n pydata-sphinx-theme-%{version} -q -T -D -a 3

# Point to the local switcher instead of the inaccessible one on the web
sed -i 's,https://pydata-sphinx-theme\.readthedocs\.io/en/latest/,,' docs/conf.py
%endif

# Substitute the installed nodejs version for the requested version
sed -i 's,^\(node-version = \)".*",\1"%{nodejs_version}",' pyproject.toml

%generate_buildrequires
%if %{with docs}
%pyproject_buildrequires -x test,doc
%else
%pyproject_buildrequires -x test
%endif

%build
export YARN_CACHE_FOLDER="$PWD/.package-cache"
yarn install --offline
nodeenv --node=system --prebuilt --clean-src $PWD/.nodeenv

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pydata_sphinx_theme
sed -i '/\.gitignore/d' %{pyproject_files}
rm %{buildroot}%{python3_sitelib}/pydata_sphinx_theme/theme/pydata_sphinx_theme/static/.gitignore

%if %{with docs}
# We need an installed tree before documentation building works properly
cd docs
%{py3_test_envvars} sphinx-build -a . _build
rm _build/.buildinfo
cd -
%endif

%check
# Sphinx 7.1.2 does not have the translation the translation test looks for
%pytest -k 'not test_translations'

%files -n python3-pydata-sphinx-theme -f %{pyproject_files}
%doc README.md

%if %{with docs}
%files doc
%doc docs/_build/*
%license LICENSE
%endif

%changelog
* Wed Oct 25 2023 Jerry James <loganjerry@gmail.com> - 0.14.2-1
- Version 0.14.2

* Wed Sep 20 2023 Jerry James <loganjerry@gmail.com> - 0.14.1-1
- Version 0.14.1

* Fri Sep 15 2023 Jerry James <loganjerry@gmail.com> - 0.14.0-1
- Version 0.14.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 0.13.3-2
- Rebuilt for Python 3.12

* Thu Mar 30 2023 Jerry James <loganjerry@gmail.com> - 0.13.3-1
- Version 0.13.3
- Stop building documentation due to missing dependencies
- Dynamically generate python BuildRequires
- The node header tarball is no longer needed

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan  6 2023 Jerry James <loganjerry@gmail.com> - 0.9.0-2
- Fix unexpanded macros in the doc subpackage
- Convert License tag to SPDX

* Tue Aug  2 2022 Jerry James <loganjerry@gmail.com> - 0.9.0-1
- Version 0.9.0 (fixes rhbz#2105307)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Python Maint <python-maint@redhat.com> - 0.8.1-3
- Rebuilt for Python 3.11

* Fri May 13 2022 Jerry James <loganjerry@gmail.com> - 0.8.1-2
- Bring back the doc subpackage

* Tue Apr 12 2022 Jerry James <loganjerry@gmail.com> - 0.8.1-1
- Version 0.8.1
- Drop the doc subpackage due to missing dependencies
- Use yarn to install vendored JavaScript

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 11 2021 Jerry James <loganjerry@gmail.com> - 0.7.2-1
- Version 0.7.2

* Sat Oct  2 2021 Jerry James <loganjerry@gmail.com> - 0.7.1-1
- Version 0.7.1
- Drop upstreamed -sphinx4.1 and -docutils patches

* Wed Sep 22 2021 Jerry James <loganjerry@gmail.com> - 0.6.3-2
- Add upstream -docutils patch to fix FTI (bz 2006934)

* Tue Jul 13 2021 Jerry James <loganjerry@gmail.com> - 0.6.3-1
- Initial RPM
