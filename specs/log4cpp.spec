Name:           log4cpp
Version:        1.1.3
Release:        16%{?dist}
Summary:        C++ logging library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://sourceforge.net/projects/log4cpp/
Source0:        http://downloads.sourceforge.net/log4cpp/%{name}-%{version}.tar.gz
# Fix errors when compiling with gcc >= 4.3
Patch0:         log4cpp-1.0-gcc43.patch
# Don't put build cflags in .pc
Patch1:         log4cpp-1.0-remove-pc-cflags.patch
# Install docs into DESTDIR
Patch2:         log4cpp-1.0-fix-doc-dest.patch
# Don't try to build snprintf.c
Patch3:         log4cpp-1.0-no-snprintf.patch
# Version is actually 1.1.3
Patch4:         log4cpp-version-1.1.3.patch
Patch5:         03_aclocal_automake.diff
Patch6:         log4cpp-configure-c99.patch

BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  automake, autoconf, libtool
BuildRequires: make

%description
A library of C++ classes for flexible logging to files, syslog, IDSA and
other destinations. It is modeled after the Log for Java library
(http://www.log4j.org), staying as close to their API as is reasonable.

%package devel
Summary:        Header files, libraries and development man pages  %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if 0%{?el4}%{?el5}
Requires:       pkgconfig
%endif

%description devel
This package contains the header files, static libraries and development
man pages for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package doc
Summary:        Development documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description doc
This package contains the development documentation for %{name}.
If you like to documentation to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n log4cpp
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1 -b .no-snprintf
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
# Delete non-free (but freely distributable) file under Artistic 1.0
# just to be sure we're not using it.
rm -rf src/snprintf.c
#Convert line endings.
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mv %{buildroot}/usr/share/doc/log4cpp-%{version} rpmdocs
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%{_libdir}/liblog4cpp.so.5*
%doc ChangeLog COPYING

%files devel
%{_bindir}/log4cpp-config
%{_includedir}/log4cpp/
%{_libdir}/liblog4cpp.so
%{_libdir}/pkgconfig/log4cpp.pc
%{_datadir}/aclocal/log4cpp.m4
%{_mandir}/man3/log4cpp*

%files doc
%doc rpmdocs/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.3-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Florian Weimer <fweimer@redhat.com> - 1.1.3-9
- C99 compatibility fixes for the configure script

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 15 2022 Steve Traylen <steve.traylen@cern.ch> - 1.1.3-7
- Change autoconf call - do not understand

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Orion Poplawski <orion@nwra.com> - 1.1.3-1
- Update to 1.1.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Mar 23 2015 Steve Traylen <steve.traylen@cern.ch> - 1.1.1-1
- New upstream 1.1.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 19 2013 Steve Traylen <steve.traylen@cern.ch> - 1.1-1
- New upstream 1.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0-9
- Fix FTBFS

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 29 2011 Steve Traylen <steve.traylen@cern.ch> - 1.0-6
- Remove useless AUTHORS INSTALL NEWS README THANKS TODO
- Move API man pages to devel package.
- Move API html pages to a seperate -docs package.
- Explicit pkgconfig requires needed on el5 only.
- Remove .la and .a files in install rather than files section.
- Use buildroot rather than RPM_BUILD_ROOT everywhere.
- Add _isa tags to requires.
- Convert ChangeLog to utf8.
- Remove api/installdox for installing documentaion.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb  2 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-2
- Delete non-free (but freely distributable) snprintf.c under Artistic 1.0 
  just to be sure we're not using it.


* Mon Dec 15 2008 Jon McCann <jmccann@redhat.com> - 1.0-1
- Initial package
