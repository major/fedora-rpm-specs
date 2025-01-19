%{?mingw_package_header}

%global pkgname exiv2

Name:          mingw-%{pkgname}
Version:       0.27.7
Release:       2%{?dist}
Summary:       MinGW Windows %{pkgname} library
License:       GPL-2.0-or-later
BuildArch:     noarch
URL:           http://www.exiv2.org/
Source0:       https://github.com/Exiv2/%{pkgname}/archive/v%{version}/%{pkgname}-%{version}.tar.gz


BuildRequires: make
BuildRequires: cmake
BuildRequires: gettext

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-gettext
BuildRequires: mingw32-expat
BuildRequires: mingw32-win-iconv
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-gettext
BuildRequires: mingw64-expat
BuildRequires: mingw64-win-iconv
BuildRequires: mingw64-zlib


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_cmake \
  -DEXIV2_ENABLE_NLS:BOOL=ON \
  -DEXIV2_BUILD_SAMPLES:BOOL=OFF \
  -DCMAKE_NO_SYSTEM_FROM_IMPORTED=ON \
  -DICONV_ACCEPTS_CONST_INPUT=1

# Hack around double slashes install paths in generated po/cmake_install.cmake
# sed -i 's|//|/|g' build_win32/po/cmake_install.cmake
# sed -i 's|//|/|g' build_win64/po/cmake_install.cmake

%mingw_make_build


%install
%mingw_make_install
%mingw_find_lang exiv2

rm -f %{buildroot}%{mingw32_libdir}/pkgconfig/exiv2.lsm
rm -f %{buildroot}%{mingw32_datadir}/man/man1/exiv2.1
rm -f %{buildroot}%{mingw64_libdir}/pkgconfig/exiv2.lsm
rm -f %{buildroot}%{mingw64_datadir}/man/man1/exiv2.1



%files -n mingw32-%{pkgname} -f mingw32-%{pkgname}.lang
%license COPYING
%{mingw32_bindir}/exiv2.exe
%{mingw32_bindir}/libexiv2.dll
%{mingw32_libdir}/libexiv2.dll.a
%{mingw32_libdir}/libexiv2-xmp.a
%{mingw32_libdir}/cmake/exiv2/
%{mingw32_libdir}/pkgconfig/exiv2.pc
%{mingw32_includedir}/exiv2/


%files -n mingw64-%{pkgname} -f mingw64-%{pkgname}.lang
%license COPYING
%{mingw64_bindir}/exiv2.exe
%{mingw64_bindir}/libexiv2.dll
%{mingw64_libdir}/libexiv2.dll.a
%{mingw64_libdir}/libexiv2-xmp.a
%{mingw64_libdir}/cmake/exiv2/
%{mingw64_libdir}/pkgconfig/exiv2.pc
%{mingw64_includedir}/exiv2/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 04 2024 Sandro Mani <manisandro@gmail.com> - 0.27.7-1
- Update to 0.27.7

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 01 2023 Sandro Mani <manisandro@gmail.com> - 0.27.6-1
- Update to 0.27.6

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.27.5-3
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 23 2021 Sandro Mani <manisandro@gmail.com> - 0.27.5-1
- Update to 0.27.5

* Wed Aug 11 2021 Sandro Mani <mainsandro@gmail.com> - 0.27.4-3
- Backport patch for CVE-2021-37618
- Backport patch for CVE-2021-37619
- Backport patch for CVE-2021-37620
- Backport patch for CVE-2021-37621
- Backport patch for CVE-2021-37622
- Backport patch for CVE-2021-37623
- Backport patch for CVE-2021-32815
- Backport patch for CVE-2021-34334
- Backport patch for CVE-2021-37615 and CVE-2021-37615
- Backport patch for CVE-2021-34335

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 20 2021 Sandro Mani <manisandro@gmail.com> - 0.27.4-1
- Update to 0.27.4

* Wed May 26 2021 Sandro Mani <manisandro@gmail.com> - 0.27.3-6
- Backport patch for CVE-2021-32617, CVE-2021-29623

* Sat May 01 2021 Sandro Mani <manisandro@gmail.com> - 0.27.3-5
- Backport patch for CVE-2021-29470
- Backport patch for CVE-2021-29473

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:36:04 GMT 2020 Sandro Mani <manisandro@gmail.com> - 0.27.3-3
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 02 2020 Sandro Mani <manisandro@gmail.com> - 0.27.3-1
- Update to 0.27.3

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 0.27.2-4
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.27.2-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Mon Jul 29 2019 Sandro Mani <manisandro@gmail.com> - 0.27.2-1
- Update to 0.27.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Sandro Mani <manisandro@gmail.com> - 0.27.1-1
- Update to 0.27.1

* Wed Apr 17 2019 Sandro Mani <manisandro@gmail.com> - 0.27-4
- Fix build against mingw-win-iconv-0.0.8

* Tue Apr 02 2019 Sandro Mani <manisandro@gmail.com> - 0.27-3
- Backport fix for CVE-2018-2009{6,7,8,9}

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Sandro Mani <manisandro@gmail.com> - 0.27-1
- Update to 0.27

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jul 11 2017 Sandro Mani <manisandro@gmail.com> - 0.26-1
- Update to 0.26

* Tue Jan 17 2017 Sandro Mani <manisandro@gmail.com> - 0.25-1
- Initial package
