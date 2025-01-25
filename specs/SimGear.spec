Name:           SimGear
Version:        2020.3.19
Release:        7%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Summary:        Simulation library components
URL:            http://simgear.sourceforge.net
Source0:        https://sourceforge.net/projects/flightgear/files/release-2020.3/simgear-%{version}.tar.bz2
Patch1:         0001-remove-unneeded-header.patch
Patch2:         0002-check-to-be-sure-that-n-is-not-being-set-as-format-t.patch
Patch3:         0003-fix-support-for-aarch64.patch
Patch4:         0004-Fix-a-new-Clang-compile-failure-with-current-XCode.patch
Patch5:         0005-cppbind-check-I-O-rules-when-auto-constructing-an-SG.patch
BuildRequires:  gcc-c++
BuildRequires:  openal-soft-devel
BuildRequires:  OpenSceneGraph-devel >= 3.2.0
BuildRequires:  boost-devel >= 1.44.0
BuildRequires:  libXt-devel, libXext-devel
BuildRequires:  libXi-devel, libXmu-devel
BuildRequires:  zlib-devel, libjpeg-devel
BuildRequires:  expat-devel, xz-devel
BuildRequires:  cmake, mesa-libGLU-devel, mesa-libEGL-devel, libcurl-devel

%description
SimGear is a set of open-source libraries designed to be used as building
blocks for quickly assembling 3d simulations, games, and visualization
applications.

%package devel
Summary: Development libraries and headers for SimGear
Requires: %{name} = %{version}-%{release}
Requires: plib-devel, libjpeg-devel, zlib-devel, libGL-devel
Requires: libX11-devel, expat-devel

%description devel
Development headers and libraries for building applications against 
SimGear.

%prep
%setup -q -n simgear-%{version}
%patch -P2 -p1 -b .checkforn
%patch -P3 -p1 -b .aarch64
%patch -P4 -p1 -b .compile
%patch -P5 -p1 -b .cppbind

# makes rpmlint happy
find -name \*.cxx -o -name \*.hxx | xargs chmod -x

# expat covers most of the files in simgear/xml, except for the custom ones (easyxml.*))
rm -rf simgear/xml/*.h simgear/xml/*.c

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DENABLE_TESTS=OFF \
    -DSIMGEAR_SHARED=ON \
    -DSYSTEM_EXPAT=ON

%cmake_build

%install
%cmake_install

# These two headers have a useless conditional when they're not internal.
# This cleans them up.
cd $RPM_BUILD_ROOT%{_includedir}/simgear/
patch -p2 < %{PATCH1}

%ldconfig_scriptlets

%files
%doc AUTHORS NEWS
%license COPYING
%{_libdir}/libSimGearCore.so.%{version}
%{_libdir}/libSimGearScene.so.%{version}

%files devel
%{_includedir}/simgear/
%{_libdir}/libSimGearCore.so
%{_libdir}/libSimGearScene.so
%{_libdir}/cmake/SimGear

%changelog
* Thu Jan 23 2025 Fabrice Bellet <fabrice@bellet.info> - 2020.3.19-7
- cppbind: check I/O rules when auto-constructing an SGPath

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2020.3.19-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 21 2023 Fabrice Bellet <fabrice@bellet.info> - 2020.3.19-1
- new upstream release

* Tue Mar 21 2023 Fabrice Bellet <fabrice@bellet.info> - 2020.3.18-1
- new upstream release
- Fix a new Clang compile failure with current XCode

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Fabrice Bellet <fabrice@bellet.info> - 2020.3.17-1
- new upstream release

* Thu Oct 20 2022 Fabrice Bellet <fabrice@bellet.info> - 2020.3.16-1
- new upstream release

* Mon Oct 03 2022 Fabrice Bellet <fabrice@bellet.info> - 2020.3.14-1
- new upstream release

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 31 2022 Fabrice Bellet <fabrice@bellet.info> - 2020.3.13-1
- new upstream release

* Fri Feb 04 2022 Fabrice Bellet <fabrice@bellet.info> - 2020.3.12-1
- new upstream release

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 15 2021 Sandro Mani <manisandro@gmail.com> - 2020.3.11-2
- Rebuild (OpenSceneGraph)

* Wed Sep 01 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.11-1
- new upstream release

* Mon Jul 26 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.10-1
- new upstream release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.9-1
- new upstream release

* Tue Mar 30 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.8-1
- new upstream release

* Mon Mar 22 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.7-1
- new upstream release

* Mon Jan 25 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.6-1
- new upstream release

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.5-1
- new upstream release

* Tue Dec 01 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.3.4-1
- new upstream release

* Sun Nov 29 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.3.3-1
- new upstream release

* Mon Nov 09 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.3.2-1
- new upstream release

* Thu Oct 29 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.3.1-1
- new upstream release

* Mon Jul 27 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.1.3-3
- use latest cmake macros

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.1.3-1
- new upstream release

* Sat May 23 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.1.2-1
- new upstream release

* Tue May 12 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.1.1-1
- new upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Fabrice Bellet <fabrice@bellet.info> - 2019.1.1-3
- remove BR freealut-devel

* Thu Sep 05 2019 Fabrice Bellet <fabrice@bellet.info> - 2019.1.1-2
- rebuild

* Mon Jul 29 2019 Fabrice Bellet <fabrice@bellet.info> - 2019.1.1-1
- new upstream release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fabrice Bellet <fabrice@bellet.info> - 2018.3.2-2
- fix for boost 1.69

* Thu Jan 31 2019 Fabrice Bellet <fabrice@bellet.info> - 2018.3.2-1
- new upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Fabrice Bellet <fabrice@bellet.info> - 2018.3.1-1
- new upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Fabrice Bellet <fabrice@bellet.info> - 2018.2.2-1
- new upstream release

* Wed May 23 2018 Tom Callaway <spot@fedoraproject.org> - 2018.2.1-1
- new upstream release

* Sun Apr 08 2018 Fabrice Bellet <fabrice@bellet.info> - 2018.1.1-1
- new upstream release

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017.3.1-3
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.3.1-1
- new upstream release

* Thu Sep 21 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 2017.2.1-5
- Rebuild against OSG-3.4.1.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 2017.2.1-2
- Rebuilt for Boost 1.64

* Mon May 22 2017 Tom Callaway <spot@fedoraproject.org> - 2017.2.1-1
- update to 2017.2.1

* Wed Apr 05 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.1.3-1
- new upstream release

* Fri Mar 03 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.1.2-1
- new upstream release

* Thu Feb 23 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.1.1-1
- new upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 2016.4.4-2
- Rebuilt for Boost 1.63

* Fri Jan 06 2017 Fabrice Bellet <fabrice@bellet.info> - 2016.4.4-1
- new upstream release

* Tue Dec 06 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.4.3-1
- new upstream release

* Fri Nov 25 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.4.2-1
- new upstream release

* Mon Nov 21 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.4.1-1
- new upstream release

* Wed Sep 14 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-2
- new upstream release

* Thu May 19 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.2.1-2
- add missing BR libcurl-devel

* Thu May 19 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.2.1-1
- new upstream release

* Mon May  9 2016 Tom Callaway <spot@fedoraproject.org> - 2016.1.2-1
- update to 2016.1.2

* Fri Feb 19 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.1.1-1
- new upstream release

* Sun Feb 14 2016 Fabrice Bellet <fabrice@bellet.info> - 3.7.0-5
- math: 'void getMaxSubdiv' does not make any sense

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 3.7.0-3
- Rebuilt for Boost 1.60

* Fri Sep 11 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.7.0-2
- Rebuild against OSG-3.4.0.

* Thu Sep 10 2015 Tom Callaway <spot@fedoraproject.org> - 3.7.0-1
- update to 3.7.0

* Thu Sep 10 2015 Tom Callaway <spot@fedoraproject.org> - 3.6.0-1
- update to 3.6.0

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 3.4.0-6
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 3.4.0-4
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.4.0-2
- Rebuild for Gcc-5.0.1 (FTBFS, RHBZ#1212686).
- Modernize spec.
- Add %%license.

* Wed Mar 11 2015 Fabrice Bellet <fabrice@bellet.info> - 3.4.0-1
- new upstream release
- drop the JPEG_FACTORY build option

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> 3.2.0-6
- rebuild (gcc5)

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 3.2.0-5
- Rebuild for boost 1.57.0

* Fri Dec 26 2014 Fabrice Bellet <fabrice@bellet.info> - 3.2.0-4
- revert "GroundLightManager: don't use smart pointers in ReferencedSingleton"

* Mon Nov 03 2014 Fabrice Bellet <fabrice@bellet.info> - 3.2.0-3
- GroundLightManager: don't use smart pointers in ReferencedSingleton

* Mon Nov 03 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.2.0-2
- Rebuild for RHBZ #1158669.

* Fri Oct 17 2014 Fabrice Bellet <fabrice@bellet.info> - 3.2.0-1
- new upstream release

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 30 2014 Peter Robinson <pbrobinson@fedoraproject.org> 3.0.0-5
- Minor patch to build on aarch64

* Thu Jul 10 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.0.0-4
- Rebuild against OSG-3.2.1.

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 3.0.0-2
- Rebuild for boost 1.55.0

* Fri Feb 21 2014 Fabrice Bellet <fabrice@bellet.info> - 3.0.0-1
- new upstream release

* Sun Sep 22 2013 Fabrice Bellet <fabrice@bellet.info> - 2.12.0-1
- new upstream release

* Thu Aug 15 2013 Ralf Corsépius <corsepiu@fedoraproject.org> 2.10.0-4
- Rebuild against OSG-3.2.0.
- Add 0005-SimGear-2.10.0-OSG-3.2.0.patch.

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 2.10.0-2
- Rebuild for boost 1.54.0

* Mon Feb 18 2013 Fabrice Bellet <fabrice@bellet.info> - 2.10.0-1
- new upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 2.8.0-3
- rebuild due to "jpeg8-ABI" feature drop

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 2.8.0-2
- rebuild against new libjpeg

* Tue Sep 11 2012 Fabrice Bellet <fabrice@bellet.info> 2.8.0-1
- new upstream release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 29 2012 Tom Callaway <spot@fedoraproject.org> 2.6.0-2
- check to be sure that %%n is not being set as format type (CVE-2012-2090)

* Tue Feb 28 2012 Fabrice Bellet <fabrice@bellet.info> 2.6.0-1
- new upstream release

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-4
- Rebuilt for c++ ABI breakage

* Mon Jan 16 2012 Tom Callaway <spot@fedoraproject.org> - 2.4.0-3
- fix boost compile issue in rawhide
- fix gcc 4.7 compile issue in rawhide

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 05 2011 Fabrice Bellet <fabrice@bellet.info> 2.4.0-1
- new upstream release

* Tue Jun 14 2011 Ralf Corsépius <corsepiu@fedoraproject.org> 2.0.0-6
- Rebuild against OSG-2.8.5.

* Wed Apr 20 2011 Tom Callaway <spot@fedoraproject.org> 2.0.0-5
- nuke old bundled copy of expat, use system expat (resolves 691934)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 02 2010 Ralf Corsépius <corsepiu@fedoraproject.org> 2.0.0-3
- Rebuild against OSG-2.8.3.

* Fri Jun 18 2010 Dan Horák <dan[at]danny.cz> 2.0.0-2
- include s390/s390x in the more-arches patch

* Fri Feb 26 2010 Fabrice Bellet <fabrice@bellet.info> 2.0.0-1
- New upstream release

* Sun Feb 14 2010 Fabrice Bellet <fabrice@bellet.info> 1.9.1-10
- Fix FTBFS (bz#564682)

* Sun Nov 29 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.1-9
- Fix osgParticle dependency (bz#542132)

* Sun Aug 16 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.1-8
- Switch to openal-soft

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 14 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.1-6
- Fix header file installed twice

* Mon May 11 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.1-5
- Rebuilt to fix bz#498584

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Hans de Goede <hdegoede@redhat.com> 1.9.1-3
- Remove rpath on x86_64

* Sun Feb 15 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.1-2
- Rebuild for newer OSG
- gcc44 compilation fix

* Tue Feb 03 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.1-1
- New upstream release

* Tue Jan 06 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.0-1
- New upstream release

* Wed Sep 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.0.0-5
- fix SimGear-0.3.10-notabbed_value_test.patch to apply without fuzz

* Tue May 13 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.0-4
- Rebuild for new plib

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.0-3
- Autorebuild for GCC 4.3

* Mon Jan  7 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.0-2
- Fix timestamp.hxx to not require the (not installed) simgear_config.h header

* Sun Jan  6 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.0-1
- Update to new upstream release 1.0.0
- Port various patches to 1.0.0

* Wed Oct 03 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.11-0.2.pre1.2
- enable alpha (bz 303161)

* Mon Aug 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.11-0.2.pre1.1
- rebuild for ppc32

* Fri Aug  3 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.11-0.3.pre1
- Update License tag for new Licensing Guidelines compliance

* Wed Jun 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.11-0.2.pre1
- fix ppc defines in conditional to be more complete

* Wed Jun 27 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.11-0.1.pre1
- bump to 0.3.11-0.1.pre1
- fix BZ 245320

* Fri Mar 30 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 0.3.10-4
- link with -release %%{version} libtool flag instead of -version, so that we
  get unique soname's for each upstream release. (Upstream gives 0 ABI
  guarantees)
- fix many undefined-non-weak-symbol's, some still remain though, see bz 208678
- work around the "thesky" bug, see bz 208678

* Wed Oct 18 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.10-3
- patch out the config internal header calls (not packaged)
- use generic libGL-devel Requires

* Tue Oct  3 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.10-2
- patch in some shared libraries

* Fri Sep 29 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.10-1
- bump to 0.3.10, fix BuildRequires

* Wed Sep  7 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.3.8-1
- initial package for Fedora Extras
