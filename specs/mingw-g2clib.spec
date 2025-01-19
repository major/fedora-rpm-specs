%{?mingw_package_header}

%global pkgname g2clib

Name:          mingw-%{pkgname}
Version:       1.6.3
Release:       13%{?dist}
Summary:       MinGW Windows g2clib library

BuildArch:     noarch
License:       LicenseRef-Fedora-Public-Domain
URL:           http://www.nco.ncep.noaa.gov/pmb/codes/GRIB2/
Source0:       http://www.nco.ncep.noaa.gov/pmb/codes/GRIB2/%{pkgname}-%{version}.tar
Source1:       g2clib-msg.txt
Source2:       CMakeLists.txt
# Patch to fix up type detection and printf arguments on 64-bit machines
Patch0:        g2clib-64bit.patch
# Patch to remove multiple definitions of templates
Patch1:        g2clib-templates.patch
# Patch from Wesley Ebisuzaki <wesley.ebisuzaki@noaa.gov> to fix sigfault
# if simunpack() is called with 0 values to unpack
Patch2:        g2clib-simunpack.patch
# Patch from degrib - appears to fix projection issues
Patch3:        g2clib-degrib.patch
# Allow to override ar
Patch4:        g2clib-ar.patch
# Add declspec attributes
Patch5:        g2clib-declspec.patch
# Fix build against jasper2
Patch6:        g2clib-jasper2.patch
# Fix conflicting declarations
Patch7:        g2clib-conflicting-declarations.patch
# Fix implicit function declaration
Patch8:        g2clib-implicit-function-declaration.patch


BuildRequires: make
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-jasper
BuildRequires: mingw32-libpng

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-jasper
BuildRequires: mingw64-libpng

BuildRequires: cmake


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
%autosetup -p1 -n %{pkgname}-%{version}

chmod a-x *.h *.c README CHANGES grib2c.doc makefile
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .


%build
%mingw_cmake
%mingw_make_build


%install
%mingw_make_install


%files -n mingw32-%{pkgname}
%license g2clib-msg.txt
%{mingw32_bindir}/libgrib2c.dll
%{mingw32_libdir}/libgrib2c.dll.a
%{mingw32_includedir}/grib2.h
%{mingw32_includedir}/drstemplates.h
%{mingw32_includedir}/gridtemplates.h
%{mingw32_includedir}/pdstemplates.h

%files -n mingw64-%{pkgname}
%license g2clib-msg.txt
%{mingw64_bindir}/libgrib2c.dll
%{mingw64_libdir}/libgrib2c.dll.a
%{mingw64_includedir}/grib2.h
%{mingw64_includedir}/drstemplates.h
%{mingw64_includedir}/gridtemplates.h
%{mingw64_includedir}/pdstemplates.h


%changelog
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
