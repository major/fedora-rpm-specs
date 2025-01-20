Name:           python-pywayland
Version:        0.4.17
Release:        4%{?dist}
Summary:        Python bindings for the libwayland library written in pure Python

# The python-pywayland project is licensed under the Apache-2.0 license,
# except for the following files:
#
# ISC License:
# pywayland/protocol/ext_session_lock_v1/*.py
#
# NTP License:
# pywayland/protocol/text_input_unstable_v3/*.py
License:        Apache-2.0 AND ISC AND NTP

URL:            https://github.com/flacjacket/pywayland/
Source:         %{pypi_source pywayland}

BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%global _description %{expand:
PyWayland provides a wrapper to the libwayland library using the CFFI library
to provide access to the Wayland library calls and written in pure Python.}


%description %_description

%package -n     python3-pywayland
Summary:        %{summary}

%description -n python3-pywayland %_description


%prep
%autosetup -p1 -n pywayland-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
# There is a scary-looking deprecation warning, already reported to upstream
# https://github.com/flacjacket/pywayland/issues/44
%python3 pywayland/ffi_build.py
%python3 -m pywayland.scanner --with-protocols


%install
%pyproject_install
%pyproject_save_files pywayland


%check
%pyproject_check_import -t
mkdir tmp
export XDG_RUNTIME_DIR="$PWD/tmp"
%pytest


%files -n python3-pywayland -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/pywayland-scanner


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.17-2
- Rebuilt for Python 3.13

* Thu May 23 2024 Jakub Kadlcik <frostyx@email.cz> - 0.4.17-1
- New upstream version

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Jakub Kadlcik <frostyx@email.cz> - 0.4.15-3
- License breakdown
- Run unit tests
- Install license and doc files
- Build _ffi.abi3.so

* Sat Jul 22 2023 Jakub Kadlcik <frostyx@email.cz> - 0.4.15-2
- Remove wildcard from pyproject_save_files

* Sat Jul 22 2023 Jakub Kadlcik <frostyx@email.cz> - 0.4.15-1
- New upstream version

* Sun Jan 01 2023 Jakub Kadlcik <frostyx@email.cz> - 0.4.14-1
- New upstream version

* Tue Jun 14 2022 Jakub Kadlcik <frostyx@email.cz> - 0.4.12-1
- Initial package
