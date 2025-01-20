Name:           python-colored
Version:        2.2.4
Release:        6%{?dist}
Summary:        Library for color and formatting in terminal

License:        MIT
URL:            https://gitlab.com/dslackw/colored
Source:         https://gitlab.com/dslackw/colored/-/archive/%{version}/colored-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Very simple Python library for color and formatting in terminal.
Collection of color codes and names for 256 color terminal setups.}

%description %_description

%package -n python3-colored
Summary:        %{summary}

%description -n python3-colored %_description


%prep
%autosetup -p1 -n colored-%{version}
# remove shebangs
sed -i '/#!\/usr\/bin\/env python/d' colored/*.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files colored


%check
# tests from upstream appear to be incomplete and/or things that must be run manually.
%pyproject_check_import colored


%files -n python3-colored -f %{pyproject_files}
%doc README.* CHANGES.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.2.4-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 04 2024 Jonathan Wright <jonathan@almalinux.org> - 2.2.4-1
- Update to 2.2.4 rhbz#2255262

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Jonathan Wright <jonathan@almalinux.org> - 2.2.3-1
- Update to 2.2.3 rhbz#2222443

* Tue Jun 27 2023 Python Maint <python-maint@redhat.com> - 2.2.2-2
- Rebuilt for Python 3.12

* Mon Jun 26 2023 Jonathan Wright <jonathan@almalinux.org> - 2.2.2-1
- Update to 2.2.2 rhbz#2215743

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.4.4-2
- Rebuilt for Python 3.12

* Thu Jan 12 2023 Jonathan Wright <jonathan@almalinux.org> - 1.4.4-1
- Initial package build
