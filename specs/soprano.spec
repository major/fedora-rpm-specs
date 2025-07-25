
%undefine __cmake_in_source_build

# undef or set to 0 to disable items for a faster build
%global apidocs 1
# upstream says tests busted, maybe to be fixed in some future point release
%global tests 1
%if 0%{?fedora} < 24 && 0%{?rhel} <= 7 
%global virtuoso 1
%endif

Summary: Qt wrapper API to different RDF storage solutions
Name:    soprano
Version: 2.9.4
Release: 37%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://quickgit.kde.org/?p=soprano.git
#URL:    http://sourceforge.net/projects/soprano

%if 0%{?snap:1}
# git clone git://anongit.kde.org/soprano ; cd soprano
# git archive --prefix=soprano-%{version}/ master | bzip2 > soprano-%{version}-%{snap}.tar.bz2
Source0: soprano-%{version}-%{snap}.tar.bz2
%else
Source0: http://downloads.sf.net/soprano/soprano-%{version}.tar.bz2
%endif

## upstreamable patches
Patch1: soprano-2.9.4-gcc6.patch

## upstream patches

BuildRequires: clucene-core-devel >= 0.9.20-2
BuildRequires: cmake
BuildRequires: kde4-macros(api)
BuildRequires: pkgconfig
BuildRequires: pkgconfig(raptor2)
BuildRequires: pkgconfig(rasqal) >= 0.9.22
BuildRequires: pkgconfig(redland)
BuildRequires: pkgconfig(QtDBus) pkgconfig(QtNetwork) pkgconfig(QtXml) 

%if 0%{?apidocs}
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: qt4-doc
%endif

%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}
## If/When backends are packaged separately
#Requires: soprano-backend
## otherwise,
Provides: soprano-backend = %{version}-%{release}
Provides: soprano-backend-redland =  %{version}-%{release}
%if 0%{?virtuoso}
Requires: redland-virtuoso
Provides: soprano-backend-virtuoso = %{version}-%{release}
## nepomuk upstream recommends this be in nepomuk-core, and strictly optional here -- rex
#Recommends: virtuoso-opensource
%endif

%description
%{summary}.

%package devel
Summary: Developer files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package backend-redland 
Summary: Redland backend for %{name}
Provides: %{name}-backend = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description backend-redland 
%{summary}.

%if 0%{?virtuoso}
%package backend-virtuoso
Summary: Virtuoso backend for %{name}
BuildRequires: libiodbc-devel
%if 0%{?tests}
BuildRequires: virtuoso-opensource
%endif
Provides: %{name}-backend = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
## not sure if  this is really needed -- rex
Requires: redland-virtuoso
## nepomuk upstream recommends this be in nepomuk-core, and strictly optional here -- rex
#Recommends: virtuoso-opensource
%description backend-virtuoso 
%{summary}.
%endif

%package apidocs
Summary: Soprano API documentation
Requires: kde-filesystem
BuildArch: noarch
%description apidocs
This package includes the Soprano API documentation in HTML
format for easy browsing.


%prep
%setup -q -n soprano-%{version}%{?pre:-%{pre}}

%patch -P1 -p1 -b .gcc6


%build
%cmake \
  -DDATA_INSTALL_DIR:PATH=%{_kde4_appsdir} \
  -DQT_DOC_DIR=%{?_qt4_docdir}%{!?_qt4_docdir:%(pkg-config --variable=docdir Qt)} \
  -DSOPRANO_BUILD_API_DOCS:BOOL=%{!?apidocs:0}%{?apidocs} \
  -DSOPRANO_BUILD_TESTS:BOOL=%{?tests:ON}%{!?tests:OFF} \
  -DSOPRANO_DISABLE_SESAME2_BACKEND:BOOL=ON \
  %{!?virtuoso:-DSOPRANO_DISABLE_VIRTUOSO_BACKEND:BOOL=ON}

%cmake_build


%install
%cmake_install

%if 0%{?apidocs}
mkdir -p %{buildroot}%{_kde4_docdir}/HTML/en
cp -a %{_vpath_builddir}/docs/html %{buildroot}%{_kde4_docdir}/HTML/en/soprano-apidocs
# spurious executables, pull in perl dep(s)
find %{buildroot}%{_kde4_docdir}/HTML/en/ -name 'installdox' -exec rm -fv {} ';'
%endif


%check
# verify pkg-config version (notoriously wrong in recent soprano releases)
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion soprano)" = "%{version}"
%if 0%{?tests:1}
export CTEST_OUTPUT_ON_FAILURE=1
# expect serveral failures, but we care mostly about virtuosobackendtest
time make -C %{_vpath_builddir} test ARGS="--timeout 300 --output-on-failure -R virtuosobackendtest" ||:
%endif


%ldconfig_scriptlets

%files
%doc AUTHORS README TODO
%license COPYING*
%{_bindir}/sopranocmd
%{_bindir}/sopranod
%{_bindir}/onto2vocabularyclass
%{_libdir}/libsoprano.so.4*
%{_libdir}/libsopranoclient.so.1*
%{_libdir}/libsopranoindex.so.1*
%{_libdir}/libsopranoserver.so.1*
%dir %{_datadir}/soprano/
%dir %{_datadir}/soprano/plugins
%{_datadir}/soprano/plugins/*parser.desktop
%{_datadir}/soprano/plugins/*serializer.desktop
%{_datadir}/soprano/rules/
%dir %{_libdir}/soprano/
%{_libdir}/soprano/libsoprano_*parser.so
%{_libdir}/soprano/libsoprano_*serializer.so

#files backend-redland
%{_libdir}/soprano/libsoprano_redlandbackend.so
%{_datadir}/soprano/plugins/redlandbackend.desktop

%if 0%{?virtuoso}
#files backend-virtuoso
%{_libdir}/soprano/libsoprano_virtuosobackend.so
%{_datadir}/soprano/plugins/virtuosobackend.desktop
%endif

%files devel
%{_datadir}/dbus-1/interfaces/org.soprano.*.xml
%{_datadir}/soprano/cmake/
%{_libdir}/libsoprano*.so
%{_libdir}/pkgconfig/soprano.pc
%{_libdir}/pkgconfig/sopranoclient.pc
%{_libdir}/pkgconfig/sopranoindex.pc
%{_libdir}/pkgconfig/sopranoserver.pc
%{_includedir}/soprano/
%{_includedir}/Soprano/

%if 0%{?apidocs}
%files apidocs
%{_kde4_docdir}/HTML/en/soprano-apidocs/
%endif


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 07 2025 Alessandro Astone <ales.astone@gmail.com> - 2.9.4-35
- Fix build dependency on kde4 macros

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.9.4-34
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.9.4-25
- use new %%cmake macros

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-24
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.9.4-18
- Escape macros in %%changelog

* Tue Jan 30 2018 Karsten Hopp <karsten@redhat.com> - 2.9.4-17
- update conditional

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.9.4-14
- rebuild (#1336810), update URL

* Sun Feb 21 2016 Rex Dieter <rdieter@fedoraproject.org> 2.9.4-13
- make redland-virtuoso conditional on virtuoso support

* Sat Feb 20 2016 Rex Dieter <rdieter@fedoraproject.org> 2.9.4-12
- disable virtuoso support f24+

* Fri Feb 12 2016 Rex Dieter <rdieter@fedoraproject.org> 2.9.4-11
- cleanup, gcc6 fixes

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.4-9
- move xml dbus interface files to -devel

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.9.4-7
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 2.9.4-6
- rebuild (gcc5)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 13 2013 Rex Dieter <rdieter@fedoraproject.org> 2.9.4-3
- %%h%check: CMAKE_OUTPUT_ON_FAILURE

* Thu Oct 10 2013 Rex Dieter <rdieter@fedoraproject.org> 2.9.4-2
- %%check: make verbose (again)

* Wed Oct 09 2013 Rex Dieter <rdieter@fedoraproject.org> 2.9.4-1
- soprano-2.9.4

* Fri Aug 30 2013 Rex Dieter <rdieter@fedoraproject.org> 2.9.3-3
- %%check: run only virtuosobackendtest (verbosely)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 10 2013 Rex Dieter <rdieter@fedoraproject.org> 2.9.3-1
- soprano-2.9.3

* Fri May 10 2013 Rex Dieter <rdieter@fedoraproject.org> 2.9.2-1
- soprano-2.9.2

* Thu May 02 2013 Rex Dieter <rdieter@fedoraproject.org> 2.9.1-1
- soprano-2.9.1 (#891265)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 02 2013 Rex Dieter <rdieter@fedoraproject.org> - 2.9.0-1
- 2.9.0
- disable tests for now
- omit QT_NO_DEBUG_OUTPUT hack, handled properly now

* Mon Dec 24 2012 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-5
- backport some upstream fixes

* Fri Aug 10 2012 Rex Dieter <rdieter@fedoraproject.org> - 2.8.0-4
- move virtuoso dep to nepomuk-core
- remove .spec cruft

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 24 2012 Rex Dieter <rdieter@fedoraproject.org> 2.8.0-2
- rebuild

* Wed Jun 27 2012 Jaroslav Reznik <jreznik@redhat.com> 2.8.0-1
- soprano-2.8.0

* Fri Jun 08 2012 Rex Dieter <rdieter@fedoraproject.org> 2.7.57-1
- soprano-2.7.57

* Wed May 30 2012 Rex Dieter <rdieter@fedoraproject.org> 2.7.56-2
- restore SC / BC with a stub impl of tcpclient 

* Wed May 30 2012 Jaroslav Reznik <jreznik@redhat.com> 2.7.56-1
- soprano-2.7.56 beta 1 release

* Mon May 28 2012 Jaroslav Reznik <jreznik@redhat.com> 2.7.56-0.1.20120528
- soprano-2.7.56-20120528 snapshot

* Sat May 19 2012 Rex Dieter <rdieter@fedoraproject.org> 2.7.6-1
- 2.7.6

* Tue May 08 2012 Rex Dieter <rdieter@fedoraproject.org> 2.7.5-3
- use/rely-on Qt pkgconfig deps

* Wed Apr 18 2012 Jaroslav Reznik <jreznik@redhat.com> 2.7.5-2
- include 'installdox' script for el

* Tue Mar 06 2012 Rex Dieter <rdieter@fedoraproject.org> 2.7.5-1
- 2.7.5
- include our own 'installdox' script (doxygen-1.8+ no longer provides it)

* Sat Jan 14 2012 Rex Dieter <rdieter@fedoraproject.org> 2.7.4-3
- backport upstream gcc47 fix

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 03 2011 Rex Dieter <rdieter@fedoraproject.org> 2.7.4-1
- 2.7.4 (#759721)

* Tue Nov 01 2011 Rex Dieter <rdieter@fedoraproject.org> 2.7.3-1
- 2.7.3

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.2-3
- Rebuilt for glibc bug#747377

* Fri Oct 21 2011 Rex Dieter <rdieter@fedoraproject.org> 2.7.2-2
- unconditionally set -DQT_NO_DEBUG_OUTPUT

* Fri Oct 21 2011 Rex Dieter <rdieter@fedoraproject.org> 2.7.2-1
- soprano-2.7.2 (#747906)
- disable DEBUG for pre-rawhide builds (#746499) 

* Sun Sep 25 2011 Rex Dieter <rdieter@fedoraproject.org> 2.7.1-1
- soprano-2.7.1 is available (#741005)

* Thu Aug 04 2011 Rex Dieter <rdieter@fedoraproject.org> 2.7.0-1
- 2.7.0

* Mon Jul 25 2011 Rex Dieter <rdieter@fedoraproject.org> 2.6.52-2.20110723
- update raptor/rasqal deps

* Sat Jul 23 2011 Rex Dieter <rdieter@fedoraproject.org> 2.6.52-1.20110723
- soprano-2.6.52 20110723 snapshot

* Tue Jul 19 2011 Karsten Hopp <karsten@redhat.com> 2.6.51-0.3.20110602
- rebuild again, PPC picked up wrong dependencies

* Mon Jun 06 2011 Rex Dieter <rdieter@fedoraproject.org> 2.6.51-0.2.20110602
- rebuild (clucene)

* Thu Jun 02 2011 Rex Dieter <rdieter@fedoraproject.org> 2.6.51-0.1.20110602
- soprano-2.6.51 20110602 snapshot

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011 Rex Dieter <rdieter@fedoraproject.org> 2.6.0-1
- soprano-2.6.0

* Tue Jan 25 2011 Rex Dieter <rdieter@fedoraproject.org> 2.5.63-3
- rebuild (gcc)
- use upstreamable rpath fix

* Tue Nov 23 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.5.63-2
- soprano-2.5.63 (release)

* Sat Nov 20 2010 Rex Dieter <rdieter@fedoraproject.org> -  2.5.63-1.20101120
- soprano-2.5.63-20101120 snapshot

* Fri Sep 10 2010 Thomas Janssen <thomasj@fedoraproject.org> 2.5.2-1
- update to soprano 2.5.2

* Wed Sep 08 2010 Thomas Janssen <thomasj@fedoraproject.org> - 2.5.1-1
- soprano-2.5.1

* Mon Aug 23 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.5.0-2
- Requires: qt4 ...
- tighten subpkg pkg deps with %%{?_isa}

* Sat Aug 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.5.0-1
- soprano-2.5.0

* Sat Jul 24 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.64-3
- -apidocs: remove spurious perl dep, move to %%_kde4_docdir/HTML/en/

* Sat Jul 24 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.64-1
- soprano-2.4.64

* Thu Jun 10 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.63-3
- Requires: redland-virtuoso (f14+)

* Wed May 26 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.63-2
- soprano 2.4.63 (official)

* Fri May 21 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.63-1.20100521
- soprano 2.4.63 20100521 snapshot

* Sun Apr 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.3-2
- fix version, and test to %%check 

* Thu Apr 22 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.3-1
- soprano-2.4.3

* Sat Apr 17 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.2-1
- soprano-2.4.2

* Tue Mar 23 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.4.1-3
- disable debugging output (-DQT_NO_DEBUG_OUTPUT)

* Tue Mar 09 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.1-2
- fix version string in CMakeLists.txt

* Fri Mar 05 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.1-1
- soprano-2.4.1

* Thu Feb 11 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.0.1-1
- soprano-2.4.0.1

* Tue Feb 09 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.4.0-1
- soprano-2.4.0
- %%build: explictly %%{_cmake_skip_rpath}, need to poke on cmake to see why 
  %%{_libdir} is getting rpath'd here

* Sat Jan 30 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.3.73-0.1.20100130
- soprano-2.3.73 (20100130 snapshot)

* Sun Jan 03 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.3.70-3
- redland_version_check patch

* Sun Jan 03 2010 Rex Dieter <rdieter@fedoraproject.org> - 2.3.70-2
- rebuild (redland)

* Wed Dec 02 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.3.70-1
- soprano-2.3.70 (#543440)

* Wed Nov 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.3.68-0.1.20091118
- soprano-2.3.68 (20091118 snapshot)

* Mon Nov 02 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.3.67-0.1.20091102
- soprano-2.3.67 (20091102 snapshot)
- Provides: soprano-backend-virtuoso

* Tue Oct 20 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.3.65-0.2.20091020
- soprano-2.3.65 (20091020 snapshot)
- Requires: virtuoso-opensource

* Fri Oct 09 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.3.63-0.1.20091009
- soprano-2.3.63 (20091009 snapshot)

* Mon Sep 14 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.3.1-1
- soprano-2.3.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.3.0-1
- soprano-2.3.0
- upstream dropped virtuoso backend  ):

* Fri Jun 26 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.2.69-1
- soprano-2.2.69

* Tue Jun 09 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.2.67-2
- upstream soprano-2.2.67 tarball

* Wed Jun 03 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.2.67-1
- soprano-2.2.67, 20090603 snapshot from kdesupport 

* Wed May  6 2009 Rex Dieter <rdieter@fedoraproject.org> - 2.2.3-2
- %%files: drop ownership of %%_datadir/dbus-1.0/interfaces (#334681)
- %%files: track shlib sonames
- make -apidocs noarch

* Mon Mar  2 2009 Lukáš Tinkl <ltinkl@redhat.com> - 2.2.3-1
- update to 2.2.3, fix apidox building

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 29 2009 Lukáš Tinkl <ltinkl@redhat.com> 2.2.1-1
- update to 2.2.1

* Tue Jan 27 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.2-1
- update to 2.2

* Fri Jan 09 2009 Than Ngo <than@redhat.com> - 2.1.64-1
- update to 2.1.64 (2.2 beta 1)

* Sun Sep 28 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.1.1-1
- update to 2.1.1

* Tue Jul 22 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.1-1
- update to 2.1
- BR graphviz for apidocs

* Fri Jul 11 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.0.99-1
- update to 2.0.99 (2.1 RC 1)

* Thu May 1 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.0.98-1
- update to 2.0.98 (2.1 alpha 1)

* Thu Mar 6 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.0.3-2
- build apidocs and put them into an -apidocs subpackage (can be turned off)
- BR doxygen and qt4-doc when building apidocs

* Tue Mar 4 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.0.3-1
- update to 2.0.3 (bugfix release)

* Fri Feb 22 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.0.2-1
- update to 2.0.2 (bugfix release)
- drop glibc/open (missing mode) patch (fixed upstream)

* Sat Feb 9 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 2.0.0-2
- rebuild for GCC 4.3

* Mon Jan 07 2008 Than Ngo <than@redhat.com> 2.0.0-1
- 2.0.0

* Sun Dec 2 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 1.98.0-1
- soprano-1.98.0 (soprano 2 rc 1)
- update glibc/open patch

* Sat Nov 10 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.97.1-2
- glibc/open patch

* Sat Nov 10 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 1.97.1-1
- soprano-1.97.1 (soprano 2 beta 4)

* Fri Oct 26 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 1.95.0-3
- BR clucene-core-devel >= 0.9.20-2 to make sure we get a fixed package

* Fri Oct 26 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 1.95.0-2
- drop findclucene patch, fixed in clucene-0.9.20-2

* Tue Oct 16 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 1.95.0-1
- update to 1.95.0 (Soprano 2 beta 2)
- new BRs clucene-core-devel, raptor-devel >= 1.4.15
- now need redland-devel >= 1.0.6
- add patch to find CLucene (clucene-config.h is moved in the Fedora package)
- new Requires: pkg-config for -devel

* Wed Aug 22 2007 Rex Dieter <rdietr[AT]fedoraproject.org> 0.9.0-4
- respin (BuildID)

* Fri Aug 3 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 0.9.0-3
- specify LGPL version in License tag

* Sun Jul 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.0-2
- BR: cmake (doh)

* Wed Jun 27 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 0.9.0-1
- soprano-0.9.0
- first try

