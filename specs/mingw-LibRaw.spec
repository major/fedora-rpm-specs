%{?mingw_package_header}

%global pkgname LibRaw

Name:          mingw-%{pkgname}
Version:       0.21.3
Release:       2%{?dist}
Summary:       Library for reading RAW files obtained from digital photo cameras

# LibRaw base package is dual licensed (actually triple licensed LGPLv2+, CDDL, LibRaw Software License)
# LibRaw-%%{version}/internal/dcb_demosaicing.c is BSD (3 clause)
License:       BSD-3-Clause AND (CDDL-1.0 OR LGPL-2.1-only)
BuildArch:     noarch
URL:           http://www.libraw.org
Source0:       http://www.libraw.org/data/%{pkgname}-%{version}.tar.gz
# Add missing -lwsock32
Patch0:        LibRaw_wsock32.patch
# Replace obsolete configure.ac macros
Patch1:        LibRaw_obsolete-macros.patch

BuildRequires: make
BuildRequires: autoconf automake libtool

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-lcms2
BuildRequires: mingw32-jasper

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-lcms2
BuildRequires: mingw64-jasper

Provides: bundled(dcraw)


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
%{summary}.


%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
%{summary}.


%package -n mingw32-%{pkgname}-tools
Summary:       Tools for the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-tools
%{summary}.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
%{summary}.


%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
%{summary}.


%package -n mingw64-%{pkgname}-tools
Summary:       Tools for the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-tools
%{summary}.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}

# Remove executable bit on license files
chmod -x LICENSE.CDDL
chmod -x LICENSE.LGPL


%build
autoreconf -ifv
%mingw_configure --enable-jasper --enable-lcms CPPFLAGS=-DLIBRAW_NODLL
%mingw_make_build


%install
%mingw_make_install

# Delete *.la files
find %{buildroot} -name '*.la' -delete

# Install doc through %%doc
rm -rf %{buildroot}%{mingw32_datadir}
rm -rf %{buildroot}%{mingw64_datadir}


%files -n mingw32-%{pkgname}
%license LICENSE.CDDL LICENSE.LGPL COPYRIGHT
%{mingw32_bindir}/libraw-23.dll
%{mingw32_bindir}/libraw_r-23.dll
%{mingw32_includedir}/libraw/
%{mingw32_libdir}/libraw.dll.a
%{mingw32_libdir}/libraw_r.dll.a
%{mingw32_libdir}/pkgconfig/libraw.pc
%{mingw32_libdir}/pkgconfig/libraw_r.pc

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libraw_r.a
%{mingw32_libdir}/libraw.a

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{pkgname}
%license LICENSE.CDDL LICENSE.LGPL COPYRIGHT
%{mingw64_bindir}/libraw-23.dll
%{mingw64_bindir}/libraw_r-23.dll
%{mingw64_includedir}/libraw/
%{mingw64_libdir}/libraw.dll.a
%{mingw64_libdir}/libraw_r.dll.a
%{mingw64_libdir}/pkgconfig/libraw.pc
%{mingw64_libdir}/pkgconfig/libraw_r.pc

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libraw_r.a
%{mingw64_libdir}/libraw.a

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/*.exe


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 23 2024 Sandro Mani <manisandro@gmail.com> - 0.21.3-1
- Update to 0.21.3

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 21 2023 Sandro Mani <manisandro@gmail.com> - 0.21.2-1
- Update to 0.21.2

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 10 2023 Sandro Mani <manisandro@gmail.com> - 0.21.1-3
- Backport patch for CVE-2023-1729

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Sandro Mani <manisandro@gmail.com> - 0.21.1-1
- Update to 0.21.1

* Fri Dec 30 2022 Sandro Mani <manisandro@gmail.com> - 0.21.0-1
- Update to 0.21.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 04 2022 Sandro Mani <manisandro@gmail.com> - 0.20.2-6
- Rebuild (jasper)

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.20.2-5
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Sandro Mani <manisandro@gmail.com> - 0.20.2-1
- Update to 0.20.2

* Wed Oct 14 2020 Sandro Mani <manisandro@gmail.com> - 0.20.1-1
- Update to 0.20.1

* Thu Jul 23 2020 Sandro Mani <manisandro@gmail.com> - 0.20.0-1
- Update to 0.20.0

* Mon Jul 13 2020 Sandro Mani <manisandro@gmail.com> - 0.19.5-4
- Backport patch for CVE-2020-15503

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.19.5-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Aug 22 2019 Sandro Mani <manisandro@gmail.com> - 0.19.5-1
- Update to 0.19.5

* Tue Aug 06 2019 Sandro Mani <manisandro@gmail.com> - 0.19.4-1
- Update to 0.19.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 08 2019 Sandro Mani <manisandro@gmail.com> - 0.19.3-1
- Update to 0.19.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 26 2018 Sandro Mani <manisandro@gmail.coM> - 0.19.2-1
- Update to 0.19.2

* Sat Nov 24 2018 Sandro Mani <manisandro@gmail.com> - 0.19.1-1
- Update to 0.19.1

* Thu Jul 19 2018 Sandro Mani <manisandro@gmail.com> - 0.19.0-1
- Update to 0.19.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Sandro Mani <manisandro@gmail.com> - 0.18.12-1
- Update to 0.18.12

* Tue May 15 2018 Sandro Mani <manisandro@gmail.com> - 0.18.11-1
- Update to 0.18.11

* Mon May 07 2018 Sandro Mani <manisandro@gmail.com> - 0.18.10-1
- Update to 0.18.10

* Wed Apr 25 2018 Sandro Mani <manisandro@gmail.com> - 0.18.9-1
- Update to 0.18.9

* Sun Feb 25 2018 Sandro Mani <manisandro@gmail.com> - 0.18.8-1
- Update to 0.18.8

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Sandro Mani <manisandro@gmail.com> - 0.18.7-1
- Update to 0.18.7

* Wed Dec 06 2017 Sandro Mani <manisandro@gmail.com> - 0.18.6-1
- Update to 0.18.6

* Fri Sep 22 2017 Sandro Mani <manisandro@gmail.com> - 0.18.5-1
- Update to 0.18.5

* Wed Sep 13 2017 Sandro Mani <manisandro@gmail.com> - 0.18.4-1
- Update to 0.18.4

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 0.18.3-1
- Update to 0.18.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 09 2017 Sandro Mani <manisandro@gmail.com> - 0.18.2-3
- Rebuild

* Sat Jul 01 2017 Sandro Mani <manisandro@gmail.com> - 0.18.2-2
- Rebuild

* Mon Mar 13 2017 Sandro Mani <manisandro@gmail.com> - 0.18.2-1
- Update to 0.18.2

* Mon Feb 13 2017 Sandro Mani <manisandro@gmail.com> - 0.18.1-1
- Update to 0.18.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 01 2017 Sandro Mani <manisandro@gmail.com> - 0.18.0-1
- Update to 0.18.0

* Wed Nov 23 2016 Michael Cronenworth <mike@cchtml.com> - 0.17.2-2
- Rebuilt for mingw-jasper update

* Thu May 19 2016 Sandro Mani <manisandro@gmail.com> - 0.17.2-1
- Update to 0.17.2

* Wed May 11 2016 Sandro Mani <manisandro@gmail.com> - 0.17.1-3
- Add dcraw_narrowing.patch to fix GCC6 FTBFS

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Sandro Mani <manisandro@gmail.com> - 0.17.1-1
- Update to 0.17.1

* Sat Aug 22 2015 Sandro Mani <manisandro@gmail.com> - 0.17.0-1
- Update to 0.17.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Sandro Mani <manisandro@gmail.com> - 0.16.2-1
- Update to 0.16.2

* Mon May 11 2015 Sandro Mani <manisandro@gmail.com> - 0.16.1-1
- Update to 0.16.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 22 2014 Sandro Mani <manisandro@gmail.com> - 0.16.0-1
- Update to 0.16.0

* Tue Jan 14 2014 Sandro Mani <manisandro@gmail.com> - 0.15.4-4
- Actually remove executable permissions from the problematic LICENSE files

* Mon Jan 13 2014 Sandro Mani <manisandro@gmail.com> - 0.15.4-3
- Add patch to replace obsolete configure.ac macros
- Remove executable permissions from LICENSE files

* Wed Jan 08 2014 Sandro Mani <manisandro@gmail.com> - 0.15.4-2
- Fix license

* Sat Dec 28 2013 Sandro Mani <manisandro@gmail.com> - 0.15.4-1
- Initial package
