%{?mingw_package_header}

%global pkgname g2clib

Name:          mingw-%{pkgname}
Version:       2.3.0
Release:       2%{?dist}
Summary:       MinGW Windows g2clib library

BuildArch:     noarch
License:       LGPL-3.0-only
URL:           https://github.com/NOAA-EMC/NCEPLIBS-g2c
Source0:       https://github.com/NOAA-EMC/NCEPLIBS-g2c/archive/v%{version}/%{pkgname}-%{version}.tar.gz
# Add missing link libs
Patch0:        g2clib-linklibs-patch

BuildRequires: cmake

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-jasper
BuildRequires: mingw32-libpng
BuildRequires: mingw32-openjpeg

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-jasper
BuildRequires: mingw64-libpng
BuildRequires: mingw64-openjpeg


%description
MinGW Windows g2clib library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows g2clib library

%description -n mingw32-%{pkgname}
MinGW Windows g2clib library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows g2clib library

%description -n mingw64-%{pkgname}
MinGW Windows g2clib library.

%{?mingw_debug_package}


%prep
%autosetup -p1 -n NCEPLIBS-g2c-%{version}


%build
%mingw_cmake -DBUILD_STATIC_LIBS=OFF
%mingw_make_build


%install
%mingw_make_install


%files -n mingw32-%{pkgname}
%license LICENSE.md
%{mingw32_bindir}/g2c_compare.exe
%{mingw32_bindir}/g2c_degrib2.exe
%{mingw32_bindir}/g2c_index.exe
%{mingw32_bindir}/libg2c.dll
%{mingw32_libdir}/libg2c.dll.a
%{mingw32_libdir}/cmake/g2c/
%{mingw32_includedir}/grib2.h
%{mingw32_datadir}/g2c/

%files -n mingw64-%{pkgname}
%license LICENSE.md
%{mingw64_bindir}/g2c_compare.exe
%{mingw64_bindir}/g2c_degrib2.exe
%{mingw64_bindir}/g2c_index.exe
%{mingw64_bindir}/libg2c.dll
%{mingw64_libdir}/libg2c.dll.a
%{mingw64_libdir}/cmake/g2c/
%{mingw64_includedir}/grib2.h
%{mingw64_datadir}/g2c/


%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sun Nov 09 2025 Sandro Mani <manisandro@gmail.com> - 2.3.0-1
- Update to 2.3.0

* Fri Aug 08 2025 Sandro Mani <manisandro@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jul 17 2025 Sandro Mani <manisandro@gmail.com> - 1.6.3-14
- Set minimum cmake version

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 01 2023 Sandro Mani <manisandro@gmail.com> - 1.6.3-9
- Rebuild (jasper)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Sandro Mani <manisandro@gmail.com> - 1.6.3-5
- Rebuild (jasper)

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.6.3-4
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 09 2021 Sandro Mani <manisandro@gmail.com> - 1.6.3-1
- Update to 1.6.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan 09 2021 Sandro Mani <manisandro@gmail.com> - 1.6.2-1
- Update to 1.6.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Apr 20 2017 Sandro Mani <manisandro@gmail.com> - 1.6.0-1
- Update to 1.6.0

* Wed Jun 24 2015 Sandro Mani <manisandro@gmail.com> - 1.4.0-1
- Initial package
