Name:           python-xkbcommon
Version:        0.8
Release:        8%{?dist}
Summary:        Bindings for libxkbcommon using cffi

License:        MIT
URL:            https://github.com/sde1000/python-xkbcommon
Source:         %{pypi_source xkbcommon}

BuildRequires:  python3-devel
BuildRequires:  gcc
BuildRequires:  libxkbcommon-devel

Requires:  libxkbcommon


%global _description %{expand:
Python bindings for libxkbcommon using cffi.}


%description %_description

%package -n     python3-xkbcommon
Summary:        %{summary}

%description -n python3-xkbcommon %_description


%prep
%autosetup -p1 -n xkbcommon-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
%python3 xkbcommon/ffi_build.py


%install
%pyproject_install
%pyproject_save_files xkbcommon


%check
%pyproject_check_import -t
%{py3_test_envvars} %{python3} -m unittest


%files -n python3-xkbcommon -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.8-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Jakub Kadlcik <frostyx@email.cz> - 0.8-3
- Run unit tests
- Install license and doc files
- Build _ffi.abi3.so

* Sat Jul 22 2023 Jakub Kadlcik <frostyx@email.cz> - 0.8-2
- Remove wildcard from pyproject_save_files

* Sat Jul 22 2023 Jakub Kadlcik <frostyx@email.cz> - 0.8-1
- Update to a new upstream version

* Tue Jun 14 2022 Jakub Kadlcik <frostyx@email.cz> - 0.4-1
- Initial package
