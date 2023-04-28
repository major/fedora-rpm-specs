
# include rapper here (or in raptor2 packaging)
%if 0%{?fedora} < 16
%global rapper 1
%endif

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Summary:       Raptor RDF Parser Toolkit for Redland
Name:          raptor
Version:       1.4.21
Release:       40%{?dist}

License:       LGPLv2+ or ASL 2.0
URL:           http://librdf.org/raptor/
Source:        http://download.librdf.org/source/raptor-%{version}.tar.gz
# Make the raptor-config file multilib friendly (RHBZ#477342)
Patch0:        raptor-config-multilib.patch
Patch1:        raptor-1.4.21-CVE-2012-0037.patch

BuildRequires: make
BuildRequires: automake
BuildRequires: libtool
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: curl-devel
BuildRequires: gtk-doc

## upstream patches
Patch100: raptor-1.4.21-curl.patch
Patch101: raptor-1.4.21-CVE-2017-18926.patch
Patch102: raptor-configure-c99.patch

%description
Raptor is the RDF Parser Toolkit for Redland that provides
a set of standalone RDF parsers, generating triples from RDF/XML
or N-Triples.

%package devel
Summary: Libraries, includes etc to develop with Raptor RDF parser library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Libraries, includes etc to develop with Raptor RDF parser library.
It provides a set of standalone RDF parsers, generating triples from
RDF/XML or N-Triples.

%prep
%setup -q
%patch0 -p1 -b .multilib
%patch1 -p1 -b .CVE-2012-0037
%patch100 -p1 -b .curl
%patch101 -p1 -b .CVE-2017-18926
%patch102 -p1

# Fix encoding
iconv -f ISO-8859-1 -t UTF8 NEWS > NEWS.tmp
touch -r NEWS NEWS.tmp
mv -f NEWS.tmp NEWS

autoreconf -i
# hack to nuke rpaths (not needed if doing autoreconf above)
#if "%{_libdir}" != "/usr/lib"
%if 0
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
%endif

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install

# unpackaged files
rm -fv ${RPM_BUILD_ROOT}%{_libdir}/lib*.la
%if ! 0%{?rapper}
rm -fv  $RPM_BUILD_ROOT%{_bindir}/rapper
rm -fv $RPM_BUILD_ROOT%{_mandir}/man1/rapper.1*
%endif

%check
make test


%ldconfig_scriptlets

%files
%doc AUTHORS COPYING COPYING.LIB ChangeLog LICENSE-2.0.txt LICENSE.html
%doc LICENSE.txt  NEWS NEWS.html NOTICE README README.html RELEASE.html
%{_libdir}/libraptor.so.1*
%if 0%{?rapper}
%{_bindir}/rapper
%{_mandir}/man1/rapper.1*
%endif

%files devel
%{_mandir}/man1/raptor-config.1*
%{_mandir}/man3/libraptor.3*
%doc %{_datadir}/gtk-doc/html/raptor/
%{_libdir}/libraptor.so
%{_libdir}/pkgconfig/raptor.pc
%{_includedir}/raptor.h
%{_bindir}/raptor-config

%changelog
* Wed Apr 26 2023 Florian Weimer <fweimer@redhat.com> - 1.4.21-40
- Port configure script to C99

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.21-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.21-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.21-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.21-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 25 2021 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.21-35
- Fixed FTBFS with autoconf-2.71
  Resolves: rhbz#1943104

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.21-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.21-33
- Defuzzified patches
- Fixed buffer overflows due to an error in calculating the maximum
  nspace declarations
  Resolves: CVE-2017-18926

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.21-32
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.21-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.21-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.21-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.21-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.21-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.21-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.21-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.21-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.21-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.21-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.21-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.21-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.21-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 17 2013 Rex Dieter <rdieter@fedoraproject.org> 1.4.21-18
- .spec cleanup

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.21-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.21-16
- Added aarch64 support
  Resolves: rhbz#926427

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.21-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 20 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.21-14
- Enabled internal testsuite

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.21-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Jaroslav Škarvada <jskarvad@redhat.com> - 1.4.21-12
- Fixed XML entity expansion that could lead to information disclosure (CVE-2012-0037)
  Resolves: rhbz#805941

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jul 31 2011 Rex Dieter <rdieter@fedoraproject.org> 1.4.21-10
- omit rapper, include in raptor2 instead (f16+)
- upstream patch to fix build against newer libcurl

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 14 2010 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.4.21-1
- New bugfix release

* Sat Dec 12 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.4.20-1
- New version.

* Thu Oct 29 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 1.4.18-5
- Fix multilib conflict (RHBZ#477342)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 01 2009 Rex Dieter <rdieter@fedoraproject.org> 1.4.18-3
- nuke rpaths
- touchup %%files
- -devel: omit dup'd %%doc's included in main pkg

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 08 2008 Anthony Green <green@redhat.com> 1.4.18-1
- Update sources.

* Sat Feb 9 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 1.4.16-2
- Rebuild for GCC 4.3.

* Fri Oct 12 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 1.4.16-1
- Update to 1.4.16 (for Soprano 2, also lots of bugfixes).
- Specify LGPL version in License tag.
- Update URLs.

* Mon Feb 26 2007 Anthony Green <green@redhat.com> 1.4.14-3
- Update sources.

* Tue Feb 13 2007 Anthony Green <green@redhat.com> 1.4.14-2
- Upgrade to 1.4.14.
- Remove pkgconfig and config patches.

* Fri Nov 3 2006 Anthony Green <green@redhat.com> 1.4.9-6
- Rebuild for new libcurl.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 1.4.9-5
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 19 2006 Anthony Green <green@redhat.com> 1.4.9-4
- Fix release tag.

* Mon Sep 18 2006 Anthony Green <green@redhat.com> 1.4.9-3.1
- Rebuild.

* Mon Sep  4 2006 Anthony Green <green@redhat.com> 1.4.9-3
- BuildRequire pkgconfig in the devel package.

* Sun May  7 2006 Anthony Green <green@redhat.com> 1.4.9-2
- Move libraptor man page to devel package.
- Update sources to 1.4.9.

* Wed Apr 26 2006 Anthony Green <green@redhat.com> 1.4.8-5
- Add raptor-1.4.8-config.patch from Michael Schwendt.
- Remove some Requires from the devel package.

* Sun Apr 23 2006 Anthony Green <green@redhat.com> 1.4.8-4
- Add raptor-1.4.8-pkgconfig.patch from Michael Schwendt.

* Sun Apr 23 2006 Anthony Green <green@redhat.com> 1.4.8-3
- Many spec file fixes from Michael Schwendt.
- Add many Requires to the -devel package.

* Tue Apr 18 2006 Anthony Green <green@redhat.com> 1.4.8-1
- Upgrade sources.  
- Install with DESTDIR.
- Build for Fedora Extras.

* Fri Nov  7 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 1.0.0-1
- build for Planet CCRMA, clean up spec file

* Thu Apr 17 2003 Dave Beckett <Dave.Beckett@bristol.ac.uk>

- Added pkgconfig raptor.pc, raptor-config
- Requires curl

* Mon Jan 13 2003 Dave Beckett <Dave.Beckett@bristol.ac.uk>

- rdfdump now rapper

* Thu Jan  9 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- built for planet ccrma
- one file conflicts with rdfdump in the nasm-rdoff package, so rename
  the binary to rdf-rdfdump for now. Maybe we should make this a
  "Conflict:" with nasm-rdoff and leave the file as is...

* Fri Dec 20 2002 Dave Beckett <Dave.Beckett@bristol.ac.uk>

- Updated to have two RPMs for raptor and raptor-devel.  Depend on
  libxml2 as XML parser.
