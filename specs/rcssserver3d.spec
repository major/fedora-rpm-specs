Name:           rcssserver3d
Version:        0.7.6
Release:        7%{?dist}
Summary:        Robocup 3D Soccer Simulation Server

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://sourceforge.net/projects/simspark/
Source0:        http://downloads.sourceforge.net/simspark/%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires:  gcc gcc-c++ cmake boost-devel SDL-devel desktop-file-utils simspark-devel
BuildRequires:  ode-devel libGL-devel DevIL-devel freetype-devel libGLU-devel
BuildRequires:  tex(latex) ImageMagick qt5-qtbase-devel
BuildRequires:  tex(titlesec.sty) tex(wrapfig.sty) tex(subfigure.sty)

%description
The RoboCup Soccer Simulator is a research and educational tool for multi-agent
systems and artificial intelligence. It enables for two teams of 11 simulated
autonomous robotic players to play soccer (football).

This package contains the 3D version of the simulator.


%package        devel
Summary:        Header files and libraries for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       boost-devel ode-devel DevIL-devel
Requires:       libGL-devel libGLU-devel simspark-devel
BuildArch:      noarch

%description    devel
This package contains the header files for %{name}. If you like to develop
programs using %{name}, you will need to install %{name}-devel.

%package        doc
Summary:        Users manual for %{name}
BuildArch:      noarch

%description    doc
This package contains the user documentation
for %{name}. If you like to develop agents for %{name},
you will find %{name}-doc package useful.

%prep
%setup -q

%build
mkdir build
cd build
export CXXFLAGS="${CXXFLAGS:-%optflags} -std=gnu++98"
export CFLAGS="${CFLAGS:-%optflags}"
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLIBDIR:PATH=%{_lib} -DODE_CONFIG_EXEC=ode-double-config ..
make VERBOSE=1 %{?_smp_mflags}
make pdf
cp doc/users/user-manual.pdf ../doc/users/

%install
make -C build install DESTDIR=%{buildroot}

mkdir %{buildroot}/%{_datadir}/pixmaps/
cp -p data/logos/simspark.png %{buildroot}/%{_datadir}/pixmaps/

desktop-file-install \
  --dir=%{buildroot}/%{_datadir}/applications linux/%{name}.desktop

mkdir package_docs
mv %{buildroot}/%{_datadir}/doc/%{name}/* package_docs/
rm -rf %{buildroot}/%{_datadir}/doc
rm -f package_docs/TODO

%files
%doc package_docs/*
%doc doc/TEXT_INSTEAD_OF_A_MANUAL.txt
%{_bindir}/*
# Notice: the package needs .so files for running so
# they can't be moved to -devel package
%{_libdir}/%{name}
%{_libdir}/guiplugin
%{_datadir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/*

%files devel
%{_includedir}/%{name}
%{_includedir}/guiplugin
%doc TODO

%files doc
%doc doc/users/user-manual.pdf
%doc package_docs/COPYING


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.7.6-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.7.6-1
- Update to version for RoboCup 2023

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 18 2022 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.7.4-4
- Fix Ruby 3 compatibility, closes rhbz#1997693

* Sun Jul 24 2022 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.4-3
- Rebuilt for Ode soname bump

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.7.4-1
- Update to latest upstream release: 0.7.4, closes fedora#2098437

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 0.7.3-3
- Rebuilt for Boost 1.76

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Apr 11 2021 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.7.3-1
- Update to latest upstream version: 0.7.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 0.7.1-11
- Rebuilt for Boost 1.75

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Jonathan Wakely <jwakely@redhat.com> - 0.7.1-9
- Rebuilt for Boost 1.73

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 2019 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.7.1-6
- Fix 'make doc' under F30

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.7.1-3
- Add gcc/gcc-c++ build dependency

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 root - 0.7.1-1
- Update to 0.7.1

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 0.7.0-5
- Rebuilt for Boost 1.66

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 0.7.0-2
- Rebuilt for Boost 1.64

* Fri Mar 24 2017 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.7.0-1
- New upstream version with new rules & new simulator control GUI

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 28 2017 Jonathan Wakely <jwakely@redhat.com> - 0.6.10-8
- Rebuilt for Boost 1.63

* Thu Mar 03 2016 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.6.10-7
- Fix compile error with GCC 6.0 (due to C++11 mode)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 0.6.10-5
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.6.10-4
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.10-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.6.10-2
- rebuild for Boost 1.58

* Tue Jul 14 2015 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.6.10-1
- Update to version 0.6.10

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.6.8.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jan 28 2015 Petr Machata <pmachata@redhat.com> - 0.6.8.1-3
- Rebuild for boost 1.57.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 04 2014 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.6.8.1-1
- Update to 0.6.8.1 with bug fixes for RoboCup 2014

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 31 2014 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.6.8-1
- Update to version 0.6.8

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 0.6.7-4
- rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 0.6.7-2
- Rebuild for boost 1.54.0

* Tue Jun 18 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.6.7-1
- Update to new upstream release: 0.6.7

* Wed May 01 2013 Jon Ciesla <limburgher@gmail.com> - 0.6.6-7
- Drop desktop vendor tag.

* Thu Feb 14 2013 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.6.6-6
- Fix Boost-1.53 compilation
- Add TeXLive style dependencies
- Fix boost system library link error

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.6.6-5
- Rebuild for Boost-1.53.0

* Tue Aug 21 2012 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.6.6-4
- Rebuild for Boost 1.50

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.6.6-2
- Add a patch to fix single-player kickoffs

* Tue May 22 2012 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.6.6-1
- Update to latest upstream version 0.6.6
- Remove some old .spec stuff (e.g. defattr's)

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-7
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 21 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.6.5-5
- Rebuild for the latest boost

* Mon Jun 20 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.6.5-4
- Add an upstream patch to fix rule enforcement code

* Sun May 15 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.6.5-3
- Add an upstream fix for goal counting

* Wed Apr 27 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.6.5-2
- Added a patch to use correct ODE flags

* Wed Apr 27 2011 Hedayat Vatankhah <hedayat.fwd+rpmchlog@gmail.com> - 0.6.5-1
- Updated to 0.6.5 release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 04 2010 Hedayat Vatankhah <hedayat@fedoraproject.org> - 0.6.4-2
- Rebuild for the new boost
- Added COPYING to -doc subpackage because of the new guidelines

* Wed Jun 09 2010 Hedayat Vatankhah <hedayat@fedoraproject.org> - 0.6.4-1
- New upstream version: 0.6.4
- Using rcssserver3d's own .desktop file

* Tue Jan 19 2010 Hedayat Vatankhah <hedayat@grad.com> - 0.6.3-1
- Updated to 0.6.3

* Thu Nov 05 2009 Hedayat Vatankhah <hedayat@grad.com> - 0.6.2-1
- Updated to 0.6.2

* Fri Aug 07 2009 Hedayat Vatankhah <hedayat@grad.com> - 0.6.1-7
- Enabled noarch sub-packages for doc and devel subpackages

* Sat Aug 01 2009 Hedayat Vatankhah <hedayat@grad.com> - 0.6.1-6
- Rebuilt against rawhide tetex

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 08 2009 Hedayat Vatankhah <hedayat@grad.com> 0.6.1-4
- Rebuild for boost-1.39

* Mon Mar 23 2009 Hedayat Vatankhah <hedayat@grad.com> 0.6.1-3
- Added missing requirements: ImageMagic and latex

* Mon Mar 23 2009 Hedayat Vatankhah <hedayat@grad.com> 0.6.1-2
- Rebuild because of a missing patch file in cvs!

* Mon Mar 23 2009 Hedayat Vatankhah <hedayat@grad.com> 0.6.1-1
- Updated to 0.6.1 version
- Using the new CMake build system

* Tue Mar 03 2009 Hedayat Vatankhah <hedayat@grad.com> 0.6-11
- Fixed the name of fonts package requirement to the new name

* Sun Mar 01 2009 Hedayat Vatankhah <hedayat@grad.com> 0.6-10
- Added patch for gcc 4.4 compatibility

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 28 2009 Hedayat Vatankhah <hedayat@grad.com> 0.6-8
- Fixed the year number in changelog documents (fixed in the previous commit).

* Wed Jan 14 2009 Hedayat Vatankhah <hedayat@grad.com> 0.6-7
- Removing VeraMono.ttf from the package because of new Fedora font guidelines.
- Adding dejavu-fonts-sans-mono as a requirement for VeraMono.ttf replacement.

* Fri Dec 19 2008 Petr Machata <pmachata@redhat.com> - 0.6-6
- Rebuild for boost-1.37.0.
- Add patch to convert make_shared(X) to X.lock()

* Mon Sep 29 2008 Hedayat Vatankhah <hedayat@grad.com> 0.6-5
- Rebuilding the package to use ODE 0.10.
- Added dInitODE patch for physicsserver.cpp

* Thu Aug 14 2008 Hedayat Vatankhah <hedayat@grad.com> 0.6-4
- Rebuilding the package because of new boost libraries.

* Wed Jul 02 2008 Hedayat Vatankhah <hedayat@grad.com> 0.6-3
- Added a patch to rename libtinyxml to libtinyxml_ex since it differs from libtinyxml

* Sat Jun 28 2008 Hedayat Vatankhah <hedayat@grad.com> 0.6-3
- Fixed Source0 URL
- Added a comment about Source1/2/3
- Replaced an incorrect path (/usr/bin) with the correct macro
- Changing "cp -r" commands in simspark makefiles with cp -pr

* Wed Jun 25 2008 Hedayat Vatankhah <hedayat@grad.com> 0.6-2
- Added missing dependencies for -devel subpackage

* Tue Jun 24 2008 Hedayat Vatankhah <hedayat@grad.com> 0.6-1
- fixed according to the Fedora package review process:
  - changed some requirements
  - removed -doc version
  - removed ld.so.conf.d/rcssserver3d.conf file in favour of rpath!!

* Mon Jun 23 2008 Hedayat Vatankhah <hedayat@grad.com> 0.6-1
- updated for 0.6 release

* Fri Jun 20 2008 Hedayat Vatankhah <hedayat@grad.com> 0.6-0.1.20080620cvs
- preparing for 0.6 release

* Thu Jun 12 2008 Hedayat Vatankhah <hedayat@grad.com> 0.5.9-1.20080611cvs
- removing rcssmonitor3D-lite
- update the package to use CVS version which contains Fedora packaging fixes
- added -doc subpackage
- added some documentation to -devel package

* Fri Jun 6 2008 Hedayat Vatankhah <hedayat@grad.com> 0.5.9-1
- added a patch to fix gcc43 compile errors and add --disable-rpath
  configure option. this patch is created using upstream CVS tree.s

* Thu Jun 5 2008 Hedayat Vatankhah <hedayat@grad.com> 0.5.9-1
- updated for 0.5.9 release
- preparing according to Fedora packaging guidelines:
  added -devel packages
  removed .la files from RPMs

* Thu Apr 17 2008 Hedayat Vatankhah <hedayat@grad.com> 0.5.7-2
- added some missing dependencies
- some cleanup
- changed to be more general. now it supports OpenSuse too (however it needs
  3rd party DevIL packages)
- removed RELEASE from doc files since it is not available in released versions

* Sun Apr 13 2008 Hedayat Vatankhah <hedayat@grad.com> 0.5.7-2
- updated an ugly wildcard! a little better.

* Fri Apr 11 2008 Hedayat Vatankhah <hedayat@grad.com> 0.5.7-2
- added ldconfig config file
- run ldconfig after install/uninstall
- some cleanup
- added subpackage rcssserver3d-rsgedit. TODO: file list should be expressed better
  this package will be built only when "--with wxWidgets" option is passed to rpmbuild

* Wed Apr 9 2008 Hedayat Vatankhah <hedayat@grad.com> 0.5.7-1
- added without-wxWidgets option to configure if availabe

* Thu Feb 28 2008 Hedayat Vatankhah <hedayat@grad.com> 0.5.7-1
- removed rcssserver3d-data as a requirement since the files are in the
  distribution now
- added libGLU stuff as requirements

* Wed Feb 27 2008 Hedayat Vatankhah <hedayat@grad.com> 0.5.7pre-1
- removed freeglut as a requirement since it is needed for rcssmonitor3d-lite only

* Thu Feb 14 2008 - Hedayat Vatankhah <hedayat@grad.com>
- Initial version
