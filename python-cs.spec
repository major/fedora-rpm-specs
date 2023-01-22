Name:           python-cs
Version:        3.0.0
Release:        8%{?dist}
Summary:        A simple, yet powerful CloudStack API client for python and the command-line

License:        BSD
URL:            https://github.com/exoscale/cs
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Checking manifest in tox is not possible, since check-manifest relies on VCS
Patch0:         python-cs-3.0.0-tox-skip-check-manifest.patch

BuildArch:      noarch

%global _description %{expand:
A simple, yet powerful CloudStack API client for python and the command-line.

* Async support.
* All present and future CloudStack API calls and parameters are supported.
* Syntax highlight in the command-line client if Pygments is installed.}

%description %_description

%package -n python3-cs
Summary:        %{summary}

BuildRequires:  python3-devel
# Test dependencies:
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(pytest-cache)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest)
# clearsilver also wants to install the cs executable, the upstream is dead,
# Fedora package is probably used by someone, python3-cs is modern, and conflicts are unlikely.
Conflicts: clearsilver

%description -n python3-cs %_description

%pyproject_extras_subpkg -n python3-cs async highlight

%prep
%autosetup -p1 -n cs-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files cs


%check
%tox


%files -n python3-cs -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/cs


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.0.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Roman Inflianskas <rominf@aiven.io> - 3.0.0-4
- Fix summary
* Fri Oct 29 2021 Roman Inflianskas <rominf@aiven.io> - 3.0.0-3
- Return cs binary back, add the package clearsilver to conflicts
* Wed Oct 27 2021 Roman Inflianskas <rominf@aiven.io> - 3.0.0-2
- Remove cs binary because it is provided by the package clearsilver
* Mon Oct 25 2021 Roman Inflianskas <rominf@aiven.io> - 3.0.0-1
- Initial package
