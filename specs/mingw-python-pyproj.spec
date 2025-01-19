%{?mingw_package_header}

%global pypi_name pyproj

Name:           mingw-python-%{pypi_name}
Summary:        MinGW Python %{pypi_name} library
Version:        3.7.0
Release:        2%{?dist}
BuildArch:      noarch

License:        MIT
Url:            https://github.com/jswhit/%{pypi_name}
Source0:        %{pypi_source %pypi_name}


BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-proj
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-build
BuildRequires:  mingw32-python3-Cython

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-proj
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-build
BuildRequires:  mingw64-python3-Cython


%description
MinGW Python %{pypi_name} library.


%package -n mingw32-python3-%{pypi_name}
Summary:       MinGW Python 3 %{pypi_name} library

%description -n mingw32-python3-%{pypi_name}
MinGW Python 3 %{pypi_name} library.


%package -n mingw64-python3-%{pypi_name}
Summary:       MinGW Python 3 %{pypi_name} library

%description -n mingw64-python3-%{pypi_name}
MinGW Python 3 %{pypi_name} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
(
export PROJ_DIR=%{mingw32_prefix}
export PROJ_INCDIR=%{mingw32_includedir}
export PROJ_LIBDIR=%{mingw32_libdir}
export PROJ_VERSION=`mingw32-pkg-config --modversion proj`
%mingw32_py3_build_wheel
)
(
export PROJ_DIR=%{mingw64_prefix}
export PROJ_INCDIR=%{mingw64_includedir}
export PROJ_LIBDIR=%{mingw64_libdir}
export PROJ_VERSION=`mingw64-pkg-config --modversion proj`
%mingw64_py3_build_wheel
)


%install
%mingw32_py3_install_wheel
%mingw64_py3_install_wheel


%files -n mingw32-python3-%{pypi_name}
%license LICENSE
%{mingw32_bindir}/pyproj
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/

%files -n mingw64-python3-%{pypi_name}
%license LICENSE
%{mingw64_bindir}/pyproj
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 03 2024 Sandro Mani <manisandro@gmail.com> - 3.7.0-1
- Update to 3.7.0

* Mon Sep 16 2024 Sandro Mani <manisandro@gmail.com> - 3.6.1-2
- Rebuild (proj)

* Sun Aug 04 2024 Sandro Mani <manisandro@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 05 2024 Sandro Mani <manisandro@gmail.com> - 3.6.0-6
- Rebuild (proj)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 03 2023 Sandro Mani <manisandro@gmail.com> - 3.6.0-3
- Rebuild (proj)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jun 18 2023 Sandro Mani <manisandro@gmail.com> - 3.6.0-1
- Update to 3.6.0

* Mon Apr 03 2023 Sandro Mani <manisandro@gmail.com> - 3.5.0-1
- Update to 3.5.0

* Sat Mar 04 2023 Sandro Mani <manisandro@gmail.com> - 3.4.1-3
- Rebuild (proj)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 30 2022 Sandro Mani <manisandro@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Wed Oct 12 2022 Sandro Mani <manisandro@gmail.com> - 3.4.0-2
- Switch to python3-build

* Tue Sep 13 2022 Sandro Mani <manisandro@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Sun Sep 04 2022 Sandro Mani <manisandro@gmail.com> - 3.3.1-3
- Rebuild (proj)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 03 2022 Sandro Mani <manisandro@gmail.com> - 3.3.1-1
- Update to 3.3.1

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 3.3.0-4
- Rebuild with mingw-gcc-12

* Wed Mar 09 2022 Sandro Mani <manisandro@gmail.com> - 3.3.0-3
- Rebuild for proj-9.0.0

* Sat Feb 19 2022 Sandro Mani <manisandro@gmail.com> - 3.3.0-2
- Fix spec filename
- Fix URL

* Fri Feb 11 2022 Sandro Mani <manisandro@gmail.com> - 3.3.0-1
- Initial package
