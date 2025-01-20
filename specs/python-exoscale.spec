Name:           python-exoscale
Version:        0.10.0
Release:        4%{?dist}
Summary:        Python bindings for Exoscale API

License:        ISC
URL:            https://exoscale.github.io/python-exoscale/
Source0:        https://github.com/exoscale/python-exoscale/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
The library to allow developers to use the Exoscale cloud platform API with
high-level Python bindings.}

%description %_description

%package -n python3-exoscale
Summary:        %{summary}

BuildRequires:  python3-devel
# Test dependencies:
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(requests-mock)
BuildRequires:  python3dist(setuptools)

%description -n python3-exoscale %_description

%prep
%autosetup -p1 -n python-exoscale-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files exoscale


%check
%pyproject_check_import
%pytest


%files -n python3-exoscale -f %{pyproject_files}
%doc README.md
%license LICENSE


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.10.0-2
- Rebuilt for Python 3.13

* Wed May 29 2024 Packit <hello@packit.dev> - 0.10.0-1
- Update to version 0.10.0
- Resolves: rhbz#2283818

* Thu May 02 2024 Packit <hello@packit.dev> - 0.9.1-1
- Update to version 0.9.1
- Resolves: rhbz#2277750

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Python Maint <python-maint@redhat.com> - 0.8.0-2
- Rebuilt for Python 3.12

* Thu May 25 2023 Roman Inflianskas <rominf@aiven.io> - 0.8.0-1
- Update to 0.8.0 (resolve rhbz#2203225)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.7.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 08 2021 Roman Inflianskas <rominf@aiven.io> - 0.7.1-1
- Initial package
