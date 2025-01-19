Summary:	Library (C API) for accessing CDDB servers
Name:		libcddb
Version:	1.3.2
Release:	45%{?dist}
License:	LGPL-2.0-or-later
URL:		http://libcddb.sourceforge.net/
Source0:	http://downloads.sourceforge.net/libcddb/%{name}-%{version}.tar.bz2
Patch0:		libcddb-1.3.0-multilib.patch
Patch1:		libcddb-1.3.2-rhbz770611.patch
Patch2:         pointer-types.patch
BuildRequires:  gcc
BuildRequires:	pkgconfig, libcdio-devel >= 0.67
BuildRequires: make

%description
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (e.g http://freedb.org/).


%package devel
Summary:	Development files for libcddb
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Libcddb is a library that implements the different protocols (CDDBP,
HTTP, SMTP) to access data on a CDDB server (e.g http://freedb.org/).
This package contains development files (static libraries, headers)
for libcddb.


%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p0
iconv -f ISO_8859-1 -t UTF-8 THANKS > THANKS.tmp
touch -r THANKS THANKS.tmp
mv THANKS.tmp THANKS
iconv -f ISO_8859-1 -t UTF-8 ChangeLog > ChangeLog.tmp
touch -r ChangeLog ChangeLog.tmp
mv ChangeLog.tmp ChangeLog


%build
%configure --disable-static
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS NEWS README THANKS ChangeLog TODO
%{_libdir}/libcddb.so.*
%{_bindir}/cddb_query

%files devel
%{_libdir}/libcddb.so
%{_includedir}/cddb
%{_libdir}/pkgconfig/libcddb.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 02 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.3.2-43
- SPDX license tag

* Thu Feb 01 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.3.2-42
- Patch for updated compiler flags.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 30 2020 Adrian Reber <adrian@lisas.de> 1.3.2-32
- Rebuilt for new libcdio (2.1.0)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Adrian Reber <adrian@lisas.de> 1.3.2-26
- Rebuilt for new libcdio (2.0.0)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Adrian Reber <adrian@lisas.de> 1.3.2-21
- Rebuilt for new libcdio (0.94)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.3.2-17
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Tue Nov 11 2014 Adrian Reber <adrian@lisas.de> 1.3.2-16
- Rebuilt for new libcdio

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 16 2013 Adrian Reber <adrian@lisas.de> 1.3.2-13
- Rebuilt for new libcdio
- Fix the rpmlint warnings

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 07 2013 Adrian Reber <adrian@lisas.de> 1.3.2-10
- Rebuilt for new libcdio

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 29 2011 Hans de Goede <hdegoede@redhat.com> - 1.3.2-7
- Fix DNS timeout handler causing an abort due to longjmp and
  FORTIFY_SOURCE from a signal handler not liking each other (rhbz#770611)

* Sun Nov 20 2011 Adrian Reber <adrian@lisas.de> 1.3.2-6
- Rebuilt for new libcdio

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 22 2010 Adrian Reber <adrian@lisas.de> 1.3.2-4
- Rebuilt for new libcdio

* Sun Jan 17 2010 Hans de Goede <hdegoede@redhat.com> - 1.3.2-3
- Drop static lib (#556063)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr  7 2009 Hans de Goede <hdegoede@redhat.com> 1.3.2-1
- New upstream release 1.3.2

* Mon Mar  9 2009 Hans de Goede <hdegoede@redhat.com> 1.3.1-1
- New upstream release 1.3.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 13 2009 Adrian Reber <adrian@lisas.de> 1.3.0-6
- Rebuild for new libcdio

* Tue Feb 19 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.0-5
- Fix Source0 URL

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.0-4
- Autorebuild for GCC 4.3

* Sun Oct 21 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.0-3
- Fix multilib conflict in version.h (bz 341971)

* Mon Aug 13 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.0-2
- Update License tag for new Licensing Guidelines compliance

* Fri Oct 27 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.3.0-1
- New upstream release 1.3.0

* Sun Oct  1 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.2-1
- New upstream release 1.2.2

* Sat Sep 23 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.1-5
- Rebuild for new libcdio

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.1-4
- FE6 Rebuild

* Sun Jul 23 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1.2.1-3
- Taking over as maintainer since Anvil has other priorities
- Long long due rebuild with new gcc for FC-5, it seems this may have already
  been done, since the last rebuild was of March 16 and the Rebuild Request
  bug of March 19? Rebuilding anyway to be sure (bug 185873)

* Thu Mar 16 2006 Dams <anvil[AT]livna.org> - 1.2.1-2.fc5
- Rebuild

* Tue Aug 23 2005 Dams <anvil[AT]livna.org> - 1.2.1
- Updated to 1.2.1

* Tue Jul 26 2005 Adrian Reber <adrian@lisas.de> - 1.2.0-3
- Rebuild against new libcdio (again)

* Tue Jul 26 2005 Dams <anvil[AT]livna.org> - 1.2.0-2
- Rebuild against new libcdio

* Tue Jul 26 2005 Dams <anvil[AT]livna.org> - 1.2.0-1
- Updated to 1.2.0

* Thu Jul 21 2005 Dams <anvil[AT]livna.org> - 1.1.0-1
- Updated to 1.1.0

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 1.0.2-2
- rebuild on all arches

* Wed May 11 2005 Dams <anvil[AT]livna.org> - 0:1.0.2-1.4
- Rebuilt for FC4

* Wed May 11 2005 Dams <anvil[AT]livna.org> - 0:1.0.2-1
- Added libcdio and pkgconfig buildreq
- Updated to 1.0.2
- Fixed URL in Source0

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Sat Jul  3 2004 Dams <anvil[AT]livna.org> 0:0.9.4-0.fdr.2
- added missing scriptlets
- Added URL in Source0
- Added additionnal files as doc

* Tue Mar  9 2004 Dams <anvil[AT]livna.org>
- Initial build.
