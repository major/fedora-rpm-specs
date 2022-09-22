Name:           python-sphinx-design
Version:        0.3.0
Release:        1%{?dist}
Summary:        Sphinx extension for responsive web components

# This project is MIT, but bundles JSON glyphs
# - sphinx_design/compiled/material* is Apache-2.0
# - sphinx_design/compiled/octicon* is MIT
License:        MIT AND Apache-2.0
URL:            https://github.com/executablebooks/sphinx-design
Source0:        %{url}/archive/v%{version}/sphinx-design-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist flit-core}
BuildRequires:  %{py3_dist myst-parser}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-regressions}
BuildRequires:  %{py3_dist sphinx}
BuildRequires:  %{py3_dist wheel}

# The Fedora package does not contain JSON glyphs
Provides:       bundled(material-icons-fonts) = 4.0.0.c9e5528

# Octicons is not available from Fedora
# The upstream release tarball does not contain JSON glyphs
Provides:       bundled(octicons) = 16.1.1

%global _description %{expand:
This package contains a Sphinx extension for designing beautiful, view
size responsive web components.}

%description %_description

%package     -n python3-sphinx-design
Summary:        Sphinx extension for responsive web components

%description -n python3-sphinx-design %_description

%package        doc
Summary:        Documentation for %{name}
# This project is MIT.  The Javascript and CSS bundled with the documentation
# has the following licenses:
# - searchindex.js: MIT
# - _static/alabaster.css: BSD-3-Clause
# - _static/basic.css: BSD-2-Clause
# - _static/doctools.js: BSD-2-Clause
# - _static/jquery*.js: MIT
# - _static/language_data.js: BSD-2-Clause
# - _static/pygments.css: BSD-2-Clause
# - _static/searchtools.js: BSD-2-Clause
# - _static/underscore*.js: MIT
License:        MIT AND BSD-2-Clause AND BSD-3-Clause

%description    doc
Documentation for %{name}.

%prep
%autosetup -n sphinx-design-%{version}

%build
%pyproject_wheel

# Build documentation
PYTHONPATH=$PWD sphinx-build -b html docs html
rm -rf html/{.buildinfo,.doctrees}

%install
%pyproject_install
%pyproject_save_files sphinx_design

%check
%pytest

%files -n python3-sphinx-design -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE
%license sphinx_design/compiled/material-icons_LICENSE
%license sphinx_design/compiled/octicon_LICENSE

%files doc
%doc html
%license LICENSE

%changelog
* Tue Aug 23 2022 Jerry James <loganjerry@gmail.com> - 0.3.0-1
- Version 0.3.0

* Mon Aug  1 2022 Jerry James <loganjerry@gmail.com> - 0.2.0-5
- Use uppercase AND for SPDX conjunction

* Mon Aug  1 2022 Jerry James <loganjerry@gmail.com> - 0.2.0-4
- Rename the docs subpackage to doc

* Fri Jul 22 2022 Jerry James <loganjerry@gmail.com> - 0.2.0-3
- Fix more issues found on review

* Tue Jun 28 2022 Jerry James <loganjerry@gmail.com> - 0.2.0-2
- Address license issues found on review

* Tue Jun 21 2022 Jerry James <loganjerry@gmail.com> - 0.2.0-1
- Initial RPM
