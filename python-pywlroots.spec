Name:           python-pywlroots
# There is a newer version but I am packaging this as a dependency for Qtile
# which requires pywlroots>=0.15.24,<0.16.0
Version:        0.15.24
Release:        5%{?dist}
Summary:        Python binding to the wlroots library using cffi
License:        NCSA

URL:            https://github.com/flacjacket/pywlroots
Source:         %{pypi_source pywlroots}

BuildRequires: python3-devel
BuildRequires: python3-pytest
BuildRequires: gcc
BuildRequires: wlroots0.15-devel

Requires:  wlroots0.15


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
