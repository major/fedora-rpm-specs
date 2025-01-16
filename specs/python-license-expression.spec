Name:           python-license-expression
Version:        30.4.1
Release:        %autorelease
Summary:        Library to parse, compare, simplify and normalize license expressions

# `irc-notify.py` in the tarball is licensed under GPL, but not re-distributed
License:        Apache-2.0
URL:            https://github.com/nexB/license-expression
Source:         %url/archive/v%{version}/license-expression-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinxcontrib-apidoc)
BuildRequires:  python3dist(sphinx-rtd-theme)

%global common_description %{expand:
This module defines a mini language to parse, validate, simplify, normalize and
compare license expressions using a boolean logic engine.

This supports SPDX license expressions and also accepts other license naming
conventions and license identifiers aliases to resolve and normalize licenses.

Using boolean logic, license expressions can be tested for equality,
containment, equivalence and can be normalized or simplified.}

%description %{common_description}

%package -n python3-license-expression
Summary:        %{summary}

%description -n python3-license-expression %{common_description}

%package -n python-license-expression-doc
Summary:        Documentation for python-license-expression
# BSD-2-Clause: Sphinx javascript
# MIT: jquery
License:        Apache-2.0 AND BSD-2-Clause AND MIT
BuildArch:      noarch
Requires:       python3-license-expression = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       bundled(js-sphinx_javascript_frameworks_compat)
Provides:       bundled(js-doctools)
Provides:       bundled(js-jquery)
Provides:       bundled(js-language_data)
Provides:       bundled(js-searchtools)

%description -n python-license-expression-doc
%{common_description}

This package is providing the documentation for license-expression.

%prep
%autosetup -p1 -n license-expression-%{version}
sed -i 's|\(fallback_version = "\)[^"]*|\1%{version}|' pyproject.toml
sed -i 's|setuptools_scm\[toml\]|setuptools_scm|' pyproject.toml
sed -i 's|setuptools_scm\[toml\]|setuptools_scm|' setup.cfg
sed -i '/sphinx_reredirects/d' setup.cfg
sed -i '/sphinx_reredirects/d' docs/source/conf.py
sed -i '/sphinx_rtd_dark_mode/d' docs/source/conf.py
sed -i '/sphinx_copybutton/d' docs/source/conf.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
sphinx-build-3 -b html docs/source html
# remove the sphinx-build-3 leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files license_expression

%check
%pytest

%files -n python3-license-expression -f %{pyproject_files}
%doc AUTHORS.rst CHANGELOG.rst CODE_OF_CONDUCT.rst README.rst

%files -n python-license-expression-doc
%doc html

%changelog
%autochangelog
