%global pypi_name debian-inspector
%global pypi_name_with_underscore %(echo "%{pypi_name}" | sed "s/-/_/g")

Name:           python-%{pypi_name}
Version:        31.1.1
Release:        %autorelease
Summary:        Library to parse Debian deb822-style control and copyright files

License:        Apache-2.0 AND BSD-3-Clause AND MIT
URL:            https://github.com/aboutcode-org/debian-inspector
Source:         %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(commoncode)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-reredirects)
BuildRequires:  python3dist(sphinxcontrib-apidoc)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  python3dist(sphinx-copybutton)

%global common_description %{expand:
Utilities to parse Debian package, copyright and control files

The Python package debian_inspector is a collection of utilities to parse
various Debian package manifests, machine readable copyright and control files
collectively known as the Debian 822 format (based on the RFC822 email format).}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
# BSD-2-Clause: Sphinx javascript
# MIT: jquery
License:        Apache-2.0 AND BSD-2-Clause AND MIT
BuildArch:      noarch
Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       bundled(js-sphinx_javascript_frameworks_compat)
Provides:       bundled(js-doctools)
Provides:       bundled(js-jquery)
Provides:       bundled(js-language_data)
Provides:       bundled(js-searchtools)

%description -n python-%{pypi_name}-doc
%{common_description}

This package is providing the documentation for %{pypi_name}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
sed -i 's|\(fallback_version = "\)[^"]*|\1%{version}|' pyproject.toml
sed -i  -e '/ABOUT/d' -e '/LICENSE/d' -e '/NOTICE/d' MANIFEST.in
# Disable Sphinx plugin that's not packaged in Fedora
sed -i '/sphinx_rtd_dark_mode/d' docs/source/conf.py

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
%pyproject_save_files %{pypi_name_with_underscore}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.rst CODE_OF_CONDUCT.rst README.rst

%files -n python-%{pypi_name}-doc
%doc html

%changelog
%autochangelog
