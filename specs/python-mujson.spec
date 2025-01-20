%global common_description %{expand:
mujson lets python libraries make use of the most performant JSON functions
available at import time.  It is small, and does not itself implement any
encoding or decoding functionality.}

Name:           python-mujson
Version:        1.4
Release:        15%{?dist}
Summary:        Use the fastest JSON functions available at import time
License:        MIT
URL:            https://github.com/mattgiles/mujson
# PyPI tarball is missing license
# https://github.com/mattgiles/mujson/issues/8
Source:         %{url}/archive/%{version}/mujson-%{version}.tar.gz
BuildArch:      noarch


%description %{common_description}


%package -n python3-mujson
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-mujson %{common_description}


%prep
%autosetup -n mujson-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files mujson


%check
%pyproject_check_import


%files -n python3-mujson -f %{pyproject_files}
%doc README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.4-13
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 30 2023 Carl George <carlwgeorge@fedoraproject.org> - 1.4-10
- Convert to pyproject macros
- Validated license as SPDX identifier

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.4-8
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4-2
- Rebuilt for Python 3.10

* Tue Apr 13 2021 Carl George <carl@george.computer> - 1.4-1
- Initial package rhbz#1948882
