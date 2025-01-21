Name:           tlock
Version:        1.6
Release:        23%{?dist}
Summary:        Terminal lock

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://pjp.dgplug.org/tools/
Source0:        http://pjp.dgplug.org/tools/%{name}-%{version}.tar.gz
Patch0:         tlock-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  ncurses-devel pam-devel

%description
tlock is a small program intended to lock the terminal until the correct
password is supplied by the user. By default 'tlock' locks the terminal with
the user's login password.

%package        devel
Summary:        Development library for tlock
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains the header(.h) and library(.so) files required to build
applications using librpass library. librpass is used by, and distributed with
tlock program.

%prep
%autosetup -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir
rm -f $RPM_BUILD_ROOT/%{_libdir}/librpass.la

%files
%doc README COPYING
%_bindir/tlock
%_libdir/lib*.so.*
%_infodir/*
%_mandir/man1/*

%files devel
%doc README COPYING
%_includedir/readpass.h
%_libdir/lib*.so
%_mandir/man3/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6-22
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Florian Weimer <fweimer@redhat.com> - 1.6-17
- Fix missing prototype for crypt (pointer truncation) (#2160647)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.6-8
- Rebuilt for libcrypt.so.2 (#1666033)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.6-5
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 pjp <pjp@fedoraproject.org> - 1.6-1
- New release v1.6

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Oct 13 2013 pjp <pjp@fedoraproject.org> - 1.5-8
- Updated autoconf(1) scripts to version >= 2.69
   -> https://bugzilla.redhat.com/show_bug.cgi?id=926640

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 1.5-2
- Rebuilt for gcc bug 634757

* Sat Sep 25 2010 _pjp_ <pj.pandit@yahoo.co.in> - 1.5-1
- changed to lock terminal with user's login password by default.

* Sat Jul 26 2008 _pjp_ <pj.pandit@yahoo.co.in> - 1.4-2
- Fixed the share/info/dir menu entry of tlock.

* Sat Jul 12 2008 _pjp_ <pj.pandit@yahoo.co.in> - 1.4-1
- Fixed the `root># tlock -s' bug. Patch supplied by: Milos Jakubicek
  (xjakub@fi.muni.cz)

* Thu May 29 2008 _pjp_ <pj.pandit@yahoo.co.in> - 1.3-1
- The new tlock version 1.3 for the last change in the texinfo source.

* Thu May 29 2008 _pjp_ <pj.pandit@yahoo.co.in> - 1.2-3
- Removed `make distclean' from under clean section above.

* Wed May 28 2008 _pjp_ <pj.pandit@yahoo.co.in> - 1.2-2
- Removed the permission and summary capitalisation glitches.

* Mon May 12 2008 _pjp_ <pj.pandit@yahoo.co.in> - 1.2-1
- Did some minor changes to tlcok source and readpass manual. No new feature
  addition. I just removed some minor glitches from the tlock source.

* Mon May 12 2008 _pjp_ <pj.pandit@yahoo.co.in> - 1.1-6
- Fixed the Requires error in package-devel

* Tue May  6 2008 _pjp_ <pj.pandit@yahoo.co.in> - 1.1-5
- Fixed the dep errors revealed by rpmlint

* Tue May  6 2008 _pjp_ <pj.pandit@yahoo.co.in> - 1.1-4
- Added the package devel section, to create a tlock-devel subpackage

* Mon May  5 2008 _pjp_ <pj.pandit@yahoo.co.in> - 1.1-3
- Fixed errors revealed in the second review

* Sat May  3 2008 _pjp_ <pj.pandit@yahoo.co.in> - 1.1-2
- Fixed errors from the first review

* Fri May  2 2008 _pjp_ <pj.pandit@yahoo.co.in> - 1.1-1
- Initial RPM release of tlock-1.1
