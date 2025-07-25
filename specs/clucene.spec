
%global git_long  e8e3d20f20da5ee3e37d347207b01890829a5475
%global git_short e8e3d20
%global snap 20130812

# rpmdev-bumpspec / releng automation compatible
%global baserelease 52

Summary:	A C++ port of Lucene
Name:		clucene
Version:	2.3.3.4
Release:	%{baserelease}.%{snap}.%{git_short}git%{?dist}
# Automatically converted from old format: LGPLv2+ or ASL 2.0 - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+ OR Apache-2.0
URL:		http://www.sourceforge.net/projects/clucene
%if 0%{?snap}
#  git archive e8e3d20f20da5ee3e37d347207b01890829a5475 --prefix=clucene-core-2.3.3.4/ | xz -9 > ../clucene-core-2.3.3.4-e8e3d20.tar.xz
Source0:	clucene-core-2.3.3.4-%{git_short}.tar.xz

%else
Source0:	http://downloads.sourceforge.net/clucene/clucene-core-%{version}.tar.gz
%endif

BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	gawk
BuildRequires:	gcc-c++
BuildRequires:	zlib-devel
BuildRequires: make

## upstreamable patches
# include LUCENE_SYS_INCLUDES in pkgconfig --cflags output
# https://bugzilla.redhat.com/748196
# and
# https://sourceforge.net/tracker/?func=detail&aid=3461512&group_id=80013&atid=558446
# pkgconfig file is missing clucene-shared
Patch50: clucene-core-2.3.3.4-pkgconfig.patch
# https://bugzilla.redhat.com/794795
# https://sourceforge.net/tracker/index.php?func=detail&aid=3392466&group_id=80013&atid=558446
# contribs-lib is not built and installed even with config
Patch51: clucene-core-2.3.3.4-install_contribs_lib.patch  
# Don't install CLuceneConfig.cmake twice
Patch52: clucene-core-2.3.3.4-CLuceneConfig.patch
# Fix tests for undefined usleep
Patch53: clucene-core-2.3.3.4-usleep.patch
# Upstream at <https://sourceforge.net/p/clucene/bugs/232/> "Patches for
# TestIndexSearcher failures":
Patch54: 0001-Make-sure-to-return-value-from-non-void-function.patch
Patch55: 0002-Avoid-deadlock-in-TestIndexSearcher.patch
# Upstream at <https://sourceforge.net/p/clucene/code/merge-requests/3/> "Fix
# missing #include <time.h>":
Patch56: 0001-Fix-missing-include-time.h.patch

%description
CLucene is a C++ port of the popular Apache Lucene search engine
(http://lucene.apache.org/java). 
CLucene aims to be a high-speed alternative to Java Lucene, its API is very
similar to that of the Java version. CLucene has recently been brought up to
date with Lucene 2.3.2. It contains most of the same functionality as the Java version.

%package core
Summary:	Core clucene module
Provides:	clucene = %{version}-%{release}
#Requires: %{name} = %{version}-%{release}
%description core
CLucene is a C++ port of the popular Apache Lucene search engine
(http://lucene.apache.org/java).
CLucene aims to be a high-speed alternative to Java Lucene, its API is very
similar to that of the Java version. CLucene has recently been brought up to
date with Lucene 2.3.2. It contains most of the same functionality as the Java version.

%package core-devel
Summary:	Headers for developing programs that will use %{name}
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
Requires:	%{name}-contribs-lib%{?_isa} = %{version}-%{release}
%description core-devel
This package contains the libraries and header files needed for
developing with clucene

%package contribs-lib
Summary:	Language specific text analyzers for %{name}
Requires:	%{name}-core%{?_isa} = %{version}-%{release}
%description contribs-lib
%{summary}.


%prep
%setup -n %{name}-core-%{version}

%patch -P50 -p1 -b .pkgconfig
%patch -P51 -p1 -b .install_contribs_lib
%patch -P52 -p1 -b .CLuceneConfig
%patch -P53 -p1 -b .usleep
%patch -P54 -p1 -b .return-value
%patch -P55 -p1 -b .avoid-deadlock
%patch -P56 -p1 -b .missing-include

# nuke bundled code
rm -rfv src/ext/{boost/,zlib/}


%build
%{cmake} \
  -DBUILD_CONTRIBS_LIB:BOOL=ON \
  -DLIB_DESTINATION:PATH=%{_libdir} \
  -DLUCENE_SYS_INCLUDES:PATH=%{_libdir}

%cmake_build


%install
%cmake_install


%check
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion libclucene-core)" = "%{version}"
# FIXME: make tests non-fatal for ppc and s390 (big endian 32 bit archs) until we have a proper fix
#ifnarch ppc s390
export CTEST_OUTPUT_ON_FAILURE=1
# needing the 'touch' here seems an odd workaroudn for missing dependency, race condition or cache requirement
touch src/test/CMakeLists.txt && \
make -C %{_target_platform} cl_test && \
time make -C %{_target_platform} test ARGS="--timeout 300 --output-on-failure" ||:
#endif

%ldconfig_scriptlets core

%files core
%doc AUTHORS ChangeLog README
%license APACHE.license COPYING LGPL.license
%{_libdir}/libclucene-core.so.1*
%{_libdir}/libclucene-core.so.%{version}
%{_libdir}/libclucene-shared.so.1*
%{_libdir}/libclucene-shared.so.%{version}

%ldconfig_scriptlets contribs-lib

%files contribs-lib
%{_libdir}/libclucene-contribs-lib.so.1*
%{_libdir}/libclucene-contribs-lib.so.%{version}

%files core-devel
%dir %{_libdir}/CLucene
%{_includedir}/CLucene/
%{_includedir}/CLucene.h
%{_libdir}/libclucene*.so
%{_libdir}/CLucene/clucene-config.h
%{_libdir}/CLucene/CLuceneConfig.cmake
%{_libdir}/pkgconfig/libclucene-core.pc


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-52.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-51.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.3.4-50.20130812.e8e3d20git
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-49.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-48.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-47.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-46.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-45.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 18 2022 Stephan Bergmann <sbergman@redhat.com> - 2.3.3.4-44.20130812.e8e3d20git
- Fix FTBFS (missing #include <time.h>)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-43.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-42.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-41.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-40.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-39.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.3.3.4-38.20130812.e8e3d20.git
- pull in some upstream fixes (PR, previous commit)
- use latest %%cmake macros
- s/define/global/

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 2.3.3.4-37.20130812.e8e3d20git
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-36.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-35.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-34.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-33.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.3.3.4-3220130812.e8e3d20git
- BR: gcc-c++, .spec cleanup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-31.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.3.3.4-30.20130812.e8e3d20git
- Switch to %%ldconfig_scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-29.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-28.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 2.3.3.4-27.20130812.e8e3d20git
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-26.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2.3.3.4-25.20130812.e8e3d20git
- Rebuilt for Boost 1.63

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-24.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 2.3.3.4-23.20130812.e8e3d20git
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.3.3.4-22.20130812.e8e3d20git
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3.4-21.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.3.3.4-20.20130812.e8e3d20git
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3.4-19.20130812.e8e3d20git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.3.4-18.20130812.e8e3d20git
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 2.3.3.4-17.20130812.e8e3d20git
- Rebuild for boost 1.57.0

* Thu Oct 09 2014 Rex Dieter <rdieter@fedoraproject.org> 2.3.3.4-16.20130812.e8e3d20git
- %%check: more love

* Thu Oct 09 2014 Rex Dieter <rdieter@fedoraproject.org> 2.3.3.4-15.20130812.e8e3d20git
- fix minor cmake macro syntax error

* Tue Oct 07 2014 Rex Dieter <rdieter@fedoraproject.org> - 2.3.3.4-14.20130812.e8e3d20git
- 20130812 git snapshot
- fix tests
- %%prep: explicitly delete bundled boost,zlib

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 2.3.3.4-11
- Rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 2.3.3.4-9
- Rebuild for boost 1.54.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Rex Dieter <rdieter@fedoraproject.org> 2.3.3.4-6
- contribs-lib is not built and installed even with config (#794795, upstream ID: 3392466)
- pkgconfig file is missing clucene-shared (upstream ID: 3461512)
- non-descriptive descripton (#757319)

* Sat Feb 25 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 2.3.3.4-5
- Temporarily disable make check as it fails on all arches

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 23 2011 Rex Dieter <rdieter@fedoraproject.org> 2.3.3.4-3
- include LUCENE_SYS_INCLUDES in pkgconfig --cflags output (#748196)

* Wed Jun 08 2011 Rex Dieter <rdieter@fedoraproject.org> 2.3.3.4-2
- cleanup cmake usage
- fix scriptlets
- track sonames

* Thu Jun 02 2011 Deji Akingunola <dakingun@gmail.com> - 2.3.3.4-1
- Update to version 2.3.3.4

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.21b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 08 2010 Deji Akingunola <dakingun@gmail.com> 0.9.21b-2
- Include the license text in the -core subpackage.

* Sun Jun 06 2010 Robert Scheck <robert@fedoraproject.org> 0.9.21b-1
- Update to 0.9.21b

* Wed Nov 04 2009 Dennis Gilmore <dennis@ausil.us> - 0.9.21-5
- disable 'make check on sparc64 along with ppc64 and s390x

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Karsten Hopp <karsten@redhat.com> 0.9.21-3
- bypass 'make check' on s390x, similar to ppc64

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Aug 27 2008 Deji Akingunola <dakingun@gmail.com> - 0.9.21-1
- Update to version 0.9.21

* Sun Feb 10 2008 Deji Akingunola <dakingun@gmail.com> - 0.9.20-4
- Rebuild for gcc43

* Wed Oct 25 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.20-3
- Fix a typo in the License field

* Wed Oct 25 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.20-2
- Fix multiarch conflicts (BZ #340891)
- Bypass 'make check' for ppc64, its failing two tests there

* Tue Aug 21 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.20-1
- Update to version 0.9.20

* Sat Aug 11 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.19-1
- Latest release update

* Fri Aug 03 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.16a-2
- License tag update

* Thu Feb 22 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.16a-2
- Add -contrib subpackage 

* Thu Dec 07 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.16a-1
- Update to latest stable release 
- Run make check during build

* Mon Nov 20 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.15-3
- Don't package APACHE.license since we've LGPL instead 
- Package documentation in devel subpackage

* Mon Nov 13 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.15-2
- Fix a bunch of issues with the spec (#215258)
- Moved the header file away from lib dir

* Sat Nov 04 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.15-1
- Initial packaging for Fedora Extras
