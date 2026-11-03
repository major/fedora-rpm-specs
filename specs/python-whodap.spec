%global pypi_name whodap

%global pypi_description %{expand:
This RDAP module supports asyncio HTTP requests (httpx). It leverages the
SimpleNamespace type for cleaner RDAP Response traversal. Keeps the familiar
look of WHOIS via the to_whois_dict method for DNS lookups.}

Name: python-%{pypi_name}
Summary: Simple RDAP module for Python
License: MIT

Version: 0.2.1
Release: 1%{?dist}

URL: https://github.com/pogzyb/%{pypi_name}
Source0: %{URL}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

# Change dependency declarations from "==version" to ">=version"
Patch0: whodap-depver.patch

# Disable code coverage report generation
Patch1: whodap-no-cov.patch

# Disable tests that require internet access
Patch2: whodap-test-nonet.patch

BuildArch: noarch
BuildRequires: python3-devel

%description %pypi_description


%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %pypi_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{pypi_name}


%check
%tox


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md


%changelog
* Mon Oct 12 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.2.1-1
- Update to v0.2.1

* Fri Sep 11 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.1.16-1
- Initial packaging
