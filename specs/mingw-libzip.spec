%{?mingw_package_header}

%global pkgname libzip

Name:           mingw-%{pkgname}
Version:        1.11.2
Release:        2%{?dist}
Summary:        C library for reading, creating, and modifying zip archives

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
BuildArch:      noarch
URL:            http://www.nih.at/libzip/index.html
Source0:        http://www.nih.at/libzip/%{pkgname}-%{version}.tar.xz
# Add soversion suffix, as was the case previously with autotools build
Patch0:         libzip_cmake.patch

BuildRequires:  ninja-build
BuildRequires:  cmake
#BuildRequires: perl
#BuildRequires: libzip-tools

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-zlib >= 1.1.2

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-zlib >= 1.1.2


%description
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.


%package -n mingw32-%{pkgname}
Summary:        C library for reading, creating, and modifying zip archives

%description -n mingw32-%{pkgname}
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.


%package -n mingw64-%{pkgname}
Summary:        C library for reading, creating, and modifying zip archives

%description -n mingw64-%{pkgname}
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from
other zip archives. Changes made without closing the archive can be reverted.
The API is documented by man pages.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_cmake -G Ninja
%mingw_ninja


%install
%mingw_ninja_install

# Remove unused files
rm -r %{buildroot}%{mingw32_datadir}
rm -r %{buildroot}%{mingw64_datadir}


%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_bindir}/zipcmp.exe
%{mingw32_bindir}/zipmerge.exe
%{mingw32_bindir}/ziptool.exe
%{mingw32_bindir}/libzip-5.dll
%{mingw32_libdir}/libzip.dll.a
%{mingw32_libdir}/pkgconfig/libzip.pc
%{mingw32_libdir}/cmake/libzip/
%{mingw32_includedir}/zip.h
%{mingw32_includedir}/zipconf.h

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_bindir}/zipcmp.exe
%{mingw64_bindir}/zipmerge.exe
%{mingw64_bindir}/ziptool.exe
%{mingw64_bindir}/libzip-5.dll
%{mingw64_libdir}/libzip.dll.a
%{mingw64_libdir}/pkgconfig/libzip.pc
%{mingw64_libdir}/cmake/libzip/
%{mingw64_includedir}/zip.h
%{mingw64_includedir}/zipconf.h


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 04 2024 Sandro Mani <manisandro@gmail.com> - 1.11.2-1
- Update to 1.11.2

* Mon Sep 23 2024 Sandro Mani <manisandro@gmail.com> - 1.11.1-1
- Update to 1.11.1

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.10.1-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 25 2023 Sandro Mani <manisandro@gmail.com> - 1.10.1-1
- Update to 1.10.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Sandro Mani <manisandro@gmail.com> - 1.10.0-1
- Update to 1.10.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Sandro Mani <manisandro@gmail.com> - 1.9.2-1
- Update to 1.9.2

* Tue Jun 14 2022 Sandro Mani <manisandro@gmail.com> - 1.9.0-1
- Update to 1.9.0

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.8.0-4
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Sandro Mani <manisandro@gmail.com> - 1.8.0-1
- Update to 1.8.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Sandro Mani <manisandro@gmail.com> - 1.7.3-1
- Update to 1.7.3

* Wed Jul 15 2020 Sandro Mani <manisandro@gmail.com> - 1.7.2-1
- Update to 1.7.2

* Sun Jun 14 2020 Sandro Mani <manisandro@gmail.com> - 1.7.1-1
- Update to 1.7.1

* Mon Jun 08 2020 Sandro Mani <manisandro@gmail.com> - 1.7.0-1
- Update to 1.7.0

* Mon Feb 03 2020 Sandro Mani <manisandro@gmail.com> - 1.6.1-1
- Update to 1.6.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Sandro Mani <manisandro@gmail.com> - 1.6.0-1
- Update to 1.6.0

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.5.2-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 15 2019 Sandro Mani <manisandro@gmail.com> - 1.5.2-1
- Update to 1.5.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 12 2018 Sandro Mani <manisandro@gmail.com> - 1.5.1-1
- Update to 1.5.1

* Mon Mar 12 2018 Sandro Mani <manisandro@gmail.com> - 1.5.0-1
- Update to 1.5.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 31 2017 Sandro Mani <manisandro@gmail.com> - 1.4.0-1
- Update to 1.4.0

* Tue Nov 21 2017 Sandro Mani <manisandro@gmail.com> - 1.3.2-1
- Update to 1.3.2

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Thu Sep 07 2017 Sandro Mani <manisandro@gmail.com> - 1.2.0-4
- Backport upstream fix for CVE-2017-14107

* Wed Aug 23 2017 Sandro Mani <manisandro@gmail.com> - 1.2.0-3
- Backport upstream fix for CVE-2017-12858

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 28 2017 Sandro Mani <manisandro@gmail.com> - 1.2.0-1
- Update to 1.2.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 01 2016 Sandro Mani <manisandro@gmail.com> - 1.1.3-1
- Update to 1.1.3

* Sat Feb 20 2016 Sandro Mani <manisandro@gmail.com> - 1.1.2-1
- Update to 1.1.2

* Sat Feb 13 2016 Sandro Mani <manisandro@gmail.com> - 1.1.1-1
- Update to 1.1.1
- Fix pkg-config files

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Sandro Mani <manisandro@gmail.com> - 1.1-1
- Update to 1.1

* Mon Nov 09 2015 Sandro Mani <manisandro@gmail.com> - 1.0.1-3
- Build with cmake to include win32 specific API (#1279580)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Sandro Mani <manisandro@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Mon Mar 23 2015 Sandro Mani <manisandro@gmail.com> - 0.11.2-3
- CVE-2015-2331: integer overflow when processing ZIP archives (#1204676,#1204677)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 19 2013 Sandro Mani <manisandro@gmail.com> - 0.11.2-1
- Update to 0.11.2

* Tue Sep 17 2013 Sandro Mani <manisandro@gmail.com> - 0.11.1-3
- Link zipconf.h to include dir (fix rhbz#1008128)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.11.1-1
- Update to 0.11.1
- Use a more verbose filelist

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 03 2012 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.9-8
- Added target for mingw64

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 0.9-6
- Renamed the source package to mingw-libzip (#800932)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9-5
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 22 2009 David Ludlow <dave@adsllc.com> - 0.9-2
- Prevent owning a directory that is not mine to own

* Tue Dec 22 2009 David Ludlow <dave@adsllc.com> - 0.9-1
- Initial creation of mingw32 package
