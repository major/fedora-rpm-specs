%global pypi_name ftfy
%global github_name python-%{pypi_name}

Name:           python-%{pypi_name}
Version:        6.3.1
Release:        %autorelease
Summary:        Fixes mojibake and other glitches in Unicode text, after the fact

License:        Apache-2.0
URL:            https://github.com/rspeer/python-ftfy
Source:         %url/archive/v%{version}/%{github_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  poetry
BuildRequires:  python3-devel
BuildRequires:  python3dist(furo)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)

%global common_description %{expand:
ftfy fixes mojibake and other glitches in Unicode text, after the fact.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
# Main program: Apache-2.0
# BSD-2-Clause: Sphinx javascript
# MIT: jquery
License:        Apache-2.0 AND MIT AND BSD-2-Clause
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
%autosetup -p1 -n %{github_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
sphinx-build-3 -b html docs/ html
# remove the sphinx-build-3 leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}
rm -rfv %{buildroot}%{python3_sitelib}/*.md

%check
# Doesn't work in Mock
rm -rfv tests/test_cli.py
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{_bindir}/ftfy

%files -n python-%{pypi_name}-doc
%doc html
%license html/_static/scripts/furo.js.LICENSE.txt

%changelog
%autochangelog
