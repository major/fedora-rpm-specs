%{?mingw_package_header}

%global pkgname quazip

Name:          mingw-%{pkgname}
Version:       1.4
Release:       6%{?dist}
Summary:       MinGW Windows %{pkgname} library

BuildArch:     noarch
# Following files are zlib licensed:
#  - quazip/unzip.c
#  - quazip/unzip.h
#  - quazip/zip.c
#  - quazip/zip.h
# Rest is LGPLv2 with a static linking exception, see COPYING
License:       ( LGPL-2.1-or-later WITH Qwt-exception-1.0 ) AND Zlib
URL:           https://stachenov.github.io/quazip/
Source:        https://github.com/stachenov/quazip/archive/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires: make
BuildRequires: cmake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-qt5-qtbase
BuildRequires: mingw32-qt6-qtbase
BuildRequires: mingw32-qt6-qt5compat
BuildRequires: mingw32-libzip

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-qt5-qtbase
BuildRequires: mingw64-qt6-qtbase
BuildRequires: mingw64-qt6-qt5compat
BuildRequires: mingw64-libzip

%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}-qt5
Summary:       MinGW Windows Qt5 %{pkgname} library
Obsoletes:     mingw32-%{pkgname}-qt5-static

%description -n mingw32-%{pkgname}-qt5
MinGW Windows Qt5 %{pkgname} library.

%package -n mingw32-%{pkgname}-qt6
Summary:       MinGW Windows Qt6 %{pkgname} library

%description -n mingw32-%{pkgname}-qt6
MinGW Windows Qt6 %{pkgname} library.


%package -n mingw64-%{pkgname}-qt5
Summary:       MinGW Windows Qt5 %{pkgname} library
Obsoletes:     mingw64-%{pkgname}-qt5-static

%description -n mingw64-%{pkgname}-qt5
MinGW Windows Qt5 %{pkgname} library.


%package -n mingw64-%{pkgname}-qt6
Summary:       MinGW Windows Qt6 %{pkgname} library

%description -n mingw64-%{pkgname}-qt6
MinGW Windows Qt6 %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2"
mkdir build_qt5
pushd build_qt5
%mingw_cmake -DQUAZIP_QT_MAJOR_VERSION=5 -DQT_INCLUDE_DIRS_NO_SYSTEM=ON ../..
%mingw_make_build
popd

mkdir build_qt6
pushd build_qt6
%mingw_cmake -DQUAZIP_QT_MAJOR_VERSION=6 -DQT_INCLUDE_DIRS_NO_SYSTEM=ON ../..
%mingw_make_build
popd


%install
pushd build_qt5
%mingw_make_install
popd

pushd build_qt6
%mingw_make_install
popd


%files -n mingw32-%{pkgname}-qt5
%license COPYING
%{mingw32_bindir}/libquazip1-qt5.dll
%{mingw32_includedir}/QuaZip-Qt5-%{version}/
%{mingw32_libdir}/libquazip1-qt5.dll.a
%{mingw32_libdir}/pkgconfig/quazip1-qt5.pc
%{mingw32_libdir}/cmake/QuaZip-Qt5-%{version}/

%files -n mingw32-%{pkgname}-qt6
%license COPYING
%{mingw32_bindir}/libquazip1-qt6.dll
%{mingw32_includedir}/QuaZip-Qt6-%{version}/
%{mingw32_libdir}/libquazip1-qt6.dll.a
%{mingw32_libdir}/pkgconfig/quazip1-qt6.pc
%{mingw32_libdir}/cmake/QuaZip-Qt6-%{version}/

%files -n mingw64-%{pkgname}-qt5
%license COPYING
%{mingw64_bindir}/libquazip1-qt5.dll
%{mingw64_includedir}/QuaZip-Qt5-%{version}/
%{mingw64_libdir}/libquazip1-qt5.dll.a
%{mingw64_libdir}/pkgconfig/quazip1-qt5.pc
%{mingw64_libdir}/cmake/QuaZip-Qt5-%{version}/

%files -n mingw64-%{pkgname}-qt6
%license COPYING
%{mingw64_bindir}/libquazip1-qt6.dll
%{mingw64_includedir}/QuaZip-Qt6-%{version}/
%{mingw64_libdir}/libquazip1-qt6.dll.a
%{mingw64_libdir}/pkgconfig/quazip1-qt6.pc
%{mingw64_libdir}/cmake/QuaZip-Qt6-%{version}/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 05 2023 Sandro Mani <manisandro@gmail.com> - 1.4-1
- Update to 1.4

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 20 2022 Sandro Mani <manisandro@gmail.com> - 1.3-1
- Update to 1.3

* Tue Feb 08 2022 Sandro Mani <manisandro@gmail.com> - 1.2-3
- Add -qt6 subpackage

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Sandro Mani <manisandro@gmail.com> - 1.2-1
- Update to 1.2

* Fri Aug 20 2021 Sandro Mani <manisandro@gmail.com> - 1.1-1
- Update to 1.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.7.6-4
- Rebuild (Changes/Mingw32GccDwarf2)
- Drop Qt4 build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Sandro Mani <manisandro@gmail.com> - 0.7.6-1
- Update to 0.7.6

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Sandro Mani <manisandro@gmail.com> - 0.7.3-5
- Fix cmake module install location

* Wed Sep 06 2017 Sandro Mani <manisandro@gmail.com> - 0.7.3-4
- Fix license

* Fri Aug 25 2017 Sandro Mani <manisandro@gmail.com> - 0.7.3-3
- Fix FindQuaZip5.cmake

* Thu Aug 10 2017 Sandro Mani <manisandro@gmail.com> - 0.7.3-2
- Align build with native package

* Thu Apr 20 2017 Sandro Mani <manisandro@gmail.com> - 0.7.3-1
- Update to 0.7.3

* Tue Jan 17 2017 Sandro Mani <manisandro@gmail.com> - 0.7.2-1
- Update to 0.7.2

* Fri Nov 01 2013 Sandro Mani <manisandro@gmail.com> - 0.5.1-1
- Initial package
