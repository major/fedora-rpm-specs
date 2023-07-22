Name:             ktechlab
Version:          0.50.0
Release:          4%{?dist}
Summary:          Development and simulation of micro-controllers and electronic circuits
License:          GPLv2

URL:              https://invent.kde.org/sdk/ktechlab
Source:           https://download.kde.org/unstable/ktechlab/%{name}-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automoc
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  gpsim-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-khtml-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kjs-devel
BuildRequires:  kf5-kparts-devel
BuildRequires:  kf5-ktexteditor-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-solid-devel
BuildRequires:  glib2-devel
BuildRequires:  make
BuildRequires:  phonon-devel
BuildRequires:  readline-devel

# Ktechlab requires gputils for PIC simulation.
Requires:       electronics-menu
Requires:       gputils
Requires:       sdcc

%description
KTechlab is a development and simulation environment for micro-controllers
and electronic circuits. KTechlab consists of several well-integrated
components: A circuit simulator, capable of simulating logic, linear devices
and some nonlinear devices. Integration with gpsim, allowing PICs to be
simulated in circuit. A schematic editor, which provides a rich real-time
feedback of the simulation. A flowchart editor, allowing PIC programs to be
constructed visually. MicroBASIC; a BASIC-like compiler for PICs, written as
a companion program to KTechlab. An embedded Kate part, which provides a
powerful editor for PIC programs. Integrated assembler and disassembler via
gpasm and gpdasm.

%prep
%autosetup


%build
%cmake -Wno-dev
%cmake_build


%install
%cmake_install


#fedora-specific : setting default path for sdcc
%{__mkdir} -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh << EOF
# setting default path for sdcc - fedora
export PATH=\$PATH:%{_libexecdir}/sdcc
EOF

# Fix absolute symlink
%{__rm} -f %{buildroot}%{_docdir}/HTML/en/%{name}/common

%find_lang %{name}

%post
source %{_sysconfdir}/profile.d/%{name}.sh

%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO
%doc %{_datadir}/doc/HTML/*/%{name}
%license COPYING
%{_bindir}/%{name}
%{_bindir}/microbe
%{_datadir}/config.kcfg/%{name}.kcfg
%{_datadir}/applications/org.kde.ktechlab.desktop
%{_datadir}/katepart5/syntax/microbe.xml
%{_datadir}/%{name}/*
%{_datadir}/kxmlgui5/%{name}/*
%{_datadir}/metainfo/org.kde.ktechlab.appdata.xml
%{_datadir}/mime/packages/ktechlab_mime.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_sysconfdir}/profile.d/%{name}.sh


%Changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.50.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.50.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.50.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 22 2022 Filipe Rosset <rosset.filipe@gmail.com> - 0.50.0-1
- Update to 0.50.0 fixes rhbz#1987629 and rhbz#1999456
- Lots of spec cleanups / modernization fixes rhbz#1885973

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Jeff Law <law@redhat.com> - 0.40.1-5
- Build UI headers first to avoid missing dependency problems

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 17 2019 Filipe Rosset <rosset.filipe@gmail.com> - 0.40.1-2
- initial commit to fix FTBFS on rawhide + spec cleanup
- upstream release 0.40.1 fixes rhbz #1604524
- fixes rhbz #1509726 and rhbz #1675239

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.70-27.20090304svn
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.70-26.20090304svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.70-25.20090304svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.70-24.20090304svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.70-23.20090304svn
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.70-22.20090304svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.70-21.20090304svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.3.70-20.20090304svn
- Add ktechlab-0.3.7-gcc7.patch (F26FTBFS, RHBZ#1423828).
- Add %%license.
- Fix bogus %%changelog date.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.70-19.20090304svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.3.70-18.20090304svn
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.70-17.20090304svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.70-16.20090304svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.3.70-15.20090304svn
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jun 18 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.3.70-13.20090304svn
- Update autotools patch for automake-1.14
- Fix FTBFS with gpsim-0.27 (#1107080)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.70-12.20090304svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 27 2013 Mat Booth <fedora@matbooth.co.uk> - 0.3.70-10.200900304svn
- Fix FTBFS bug #914120 caused by new automake.

* Tue Jun 28 2011 Mat Booth <fedora@matbooth.co.uk> - 0.3.70-5.200900304svn
- Fix FTBFS bug #715877 caused by new GCC strictness.

* Sat Sep 05 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3.70-3.200900304svn
- Fixed rawhide built

* Sat Sep 05 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3.70-2.200900304svn
- Fixed Bug 511578 -  FTBFS ktechlab-0.3.70-1.20090304svn.fc11
- Rebuilt to improve stability : gpsim-0.23

* Wed Mar 04 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3.70-1.200900304svn
- new svn checkout 238
- included patch from upstream, Julian Bäume, to build on gpsim 0.23

* Sat Jan 31 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3.69-11.20090131svn
- new svn checkout 175

* Mon Nov 03 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3.69-10.20081031svn
- added sdcc as Requires

* Sat Nov 01 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3.69-9.20081031svn
- fixed microcontrollers support
- fixed Bug 469126 -  ktechlab quits when attempting to add a component to a schematic

* Thu Jul 17 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.3.69-8
- fix gcc42 patch to actually apply (remove hunk already applied in 0.3.69)
- adapt Debian g++ 4.3 patch by Georges Khaznadar

* Mon Feb 25 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3.69-7
- fixed for KDE4

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.69-6
- Autorebuild for GCC 4.3

* Sat Sep 08 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3.69-5
- updated desktop file
- fixed missing icon of bar graph display
- disable rough oscilloscope

* Sat Aug 18 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3.69-4.20070626svn
- fixed conflict with alliance and changed license

* Mon Aug 13 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3.69-3.20070626svn
- added sdcc to path

* Tue Jun 26 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3.69-2.20070626svn
- dropped ktechlab-0.3-ppc-includes.patch (fix in upstream)

* Tue Jun 26 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3.69-1.20070626svn
- New svn snapshot

* Sun Jun 17 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3.69-1.20070617svn
- New svn snapshot

* Fri Apr 20 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3.6-2
- rebuild

* Wed Apr 18 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3.6-1
- New svn snapshot

* Wed Jan 03 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3-10 #development release
- New development snapshot - 20070103
- dropped ktechlab-check.patch

* Thu Dec 28 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3-9 #development release
- uncomment define CHECK in src/electronics/simulation/elementset.cpp

* Wed Dec 27 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3-8 #development release
- New development snapshot - 20061227

* Mon Dec 25 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3-7 #development release
- New development snapshot - Providing testing facilities to upstream
- dropped ktechlab-0.3-pic.patch
- package does not ship autom4te.cache anymore
- fixed missing make for src/math

* Wed Nov 22 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3-6
- Rebuilt due to new gpsim-devel release

* Fri Oct 13 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3-5
- Try to fix compilation on ppc.

* Mon Sep 25 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3-3
- Added gputils as requires

* Thu Sep 21 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3-2
- Removed gputils and gpsim as requires
- Removed autom4te.cache directory
- Owning %%{_datadir}/config.kcfg/
- Removed ldconfig from %%post and %%postun
- Removed gettext, libtool and autoconf as BR

* Fri Sep 15 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 0.3-1
- Initial package for Fedora Extras.
