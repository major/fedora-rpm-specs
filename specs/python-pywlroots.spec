Name:           python-pywlroots
Version:        0.17.0
Release:        4%{?dist}
Summary:        Python binding to the wlroots library using cffi
License:        NCSA

URL:            https://github.com/flacjacket/pywlroots
Source:         %{pypi_source pywlroots}

BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: gcc
BuildRequires: (pkgconfig(wlroots) >= 0.17.0 with pkgconfig(wlroots) < 0.18)


%global _description %{expand:
A Python binding to the wlroots library using cffi. The library uses pywayland
to provide the Wayland bindings and python-xkbcommon to provide wlroots
keyboard functionality.}


%description %_description

%package -n     python3-pywlroots
Summary:        %{summary}

%description -n python3-pywlroots %_description


%prep
%autosetup -p1 -n pywlroots-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
python3 wlroots/ffi_build.py


%install
%pyproject_install
%pyproject_save_files wlroots


%check
%pyproject_check_import -t
%pytest


%files -n python3-pywlroots -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.17.0-2
- Rebuilt for Python 3.13

* Thu May 23 2024 Jakub Kadlcik <frostyx@email.cz> - 0.17.0-1
- New upstream version

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Nov 04 2023 Jakub Kadlcik <frostyx@email.cz> - 0.16.4-1
- Downgrade to 0.16.4 for Qtile Wayland compatibility

* Tue Oct 10 2023 Jakub Kadlcik <frostyx@email.cz> - 0.16.6-1
- New upstream version

* Thu Sep 14 2023 Jakub Kadlcik <frostyx@email.cz> - 0.15.24-5
- Don't exclude wlroots/include/ Qtile needs it

* Thu Sep 14 2023 Jakub Kadlcik <frostyx@email.cz> - 0.15.24-4
- The upstream issue #125 resolved, the license is only NCSA

* Sun Jul 30 2023 Jakub Kadlcik <frostyx@email.cz> - 0.15.24-3
- License breakdown
- Install license and doc files
- Depend on the correct wlroots version
- Use pytest instead of unittest
- Specify pyproject_save_files

* Sat Jul 22 2023 Jakub Kadlcik <frostyx@email.cz> - 0.15.24-2
- We can use pyproject_buildrequires now, the RHBZ 2097535 is resolved

* Tue Dec 20 2022 Jakub Kadlcik <frostyx@email.cz> - 0.15.24-1
- New upstream version

* Tue Jun 14 2022 Jakub Kadlcik <frostyx@email.cz> - 0.15.17-1
- Initial package
