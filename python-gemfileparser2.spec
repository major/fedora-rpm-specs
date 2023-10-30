%global pypi_name gemfileparser2

Name:           python-%{pypi_name}
Version:        0.9.3
Release:        %autorelease
Summary:        Library to parse Rubygem gemspec

License:        GPL-3.0-or-later OR MIT
URL:            https://github.com/nexB/gemfileparser2
Source:         %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
# setup.cfg: fix invalid version spec
Patch:          6270a8805c7fb964e545a56ca8a92829d240a96a.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%global common_description %{expand:
gemfileparser2 parses Ruby Gemfile using Python with supports Ruby Gemfiles and
.gemspec files as well as Cocoapod .podspec files.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
# BSD-2-Clause: Sphinx javascript
# MIT: jquery
License:        (GPL-3.0-or-later OR MIT) AND BSD-2-Clause AND MIT
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
%py3_shebang_fix src/gemfileparser2.py

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
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS CHANGELOG.rst README.rst
%pycached %{python3_sitelib}/gemfileparser.py

%files -n python-%{pypi_name}-doc
%doc html

%changelog
%autochangelog
