%global	short_version	3.10

%undefine        _changelog_trimtime
%undefine   __brp_mangle_shebangs

Name:			xcircuit
Version:		%{short_version}.30
Release:		14%{?dist}
Summary:		Electronic circuit schematic drawing program

# Xw/		HPND unused
# asg/	non-free	unused
# flate.c	GPL-2.0-only	from acroformtool
# lib/tcl/matgen.tcl		GPL-2.0-or-later
# spiceparser/	GPL-2.0-or-later	unused
# utf8encodings.c	not-a-license https://gitlab.com/fedora/legal/fedora-license-data/-/issues/498
# xcircuit.c	GPL-2.0-or-later
# SPDX confirmed
License:		GPL-2.0-or-later AND GPL-2.0-only
URL:			http://opencircuitdesign.com/xcircuit

Source:		http://opencircuitdesign.com/xcircuit/archive/%{name}-%{version}.tgz
Source1:		%{name}.desktop
# http://opencircuitdesign.com/xcircuit/archive/xcircuit.xpm as 64x64
Source2:		%{name}.png

Patch0:		xcircuit-3.9.40-format-security.patch
Patch1:		xcircuit-c99.patch
# C23 fix, include math.h instead of declare atan2 internally
Patch2:		xcircuit-3.10.30-c23-math-include.patch

BuildRequires:	make
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	libgs-devel
BuildRequires:	libXpm-devel
BuildRequires:	libXt-devel
BuildRequires:	pkgconfig(tcl) <= 8.999
BuildRequires:	pkgconfig(tk) <= 8.999
BuildRequires:	zlib-devel
BuildRequires:	desktop-file-utils
BuildRequires:	ngspice

BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool

# Need check
Requires:		coreutils
Requires:		gtk2
Requires:		tk

# Special FEL Gnome/KDE menu structure
Requires:		electronics-menu

%description
Xcircuit is a general-purpose drawing program and also a specific-purpose
CAD program for circuit schematic drawing and schematic capture.

%prep
%setup -q
%patch -P0 -p1 -b .format
%patch -P1 -p1 -b .c99
%patch -P2 -p1 -b .c23

#439604: TCL 8.5.1
sed -i lib/tcl/tkcon.tcl \
	-e "s|package require -exact|package require|" 
sed -i Makefile.am \
	-e 's|/lib/|/%{_lib}/|'

autoreconf

sed -i Makefile.in -e 's|LD_RUN_PATH =|LD_RUN_PATH_DIE =|'
sed -i examples/xc_remote.sh -e 's|/usr/local/bin|%{_bindir}|'
chmod ugo-x lib/tcl/console.tcl

%build
export WISH=/usr/bin/wish

#01/08/09 Without --enable-asg \ because it's broken
%configure \
	--with-tcl=%{_libdir} \
	--with-tk=%{_libdir} \
	%{nil}
%make_build

%install
%make_install
make install-man mandir="%{buildroot}%{_mandir}"

rm -rf examples/win32
chmod -x examples/*

# They stay
#W: xcircuit hidden-file-or-dir examples/python/.xcircuitrc
#W: xcircuit hidden-file-or-dir examples/.xcircuitrc

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
install -cpm 0644 %{SOURCE2} \
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

sed -i '7 a\export TCLLIBPATH=%{_libdir}' %{buildroot}%{_bindir}/xcircuit

desktop-file-install \
	--vendor "" \
	--dir %{buildroot}%{_datadir}/applications \
	%{SOURCE1}

%files
%doc	CHANGES
%doc	README*
%doc	TODO
%doc	examples/
%license	COPYRIGHT

%{_bindir}/%{name}
%{_libdir}/%{name}-%{short_version}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_mandir}/man1/%{name}.1.*

%changelog
* Fri Jan 31 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.10.30-14
- Use tk8 explicitly

* Sun Jan 19 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.10.30-13
- Fix for C23, include header properly

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.30-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Apr 12 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.10.30-11
- SPDX migration

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.30-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.10.30-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 11 2023 Florian Weimer <fweimer@redhat.com> - 3.10.30-8
- Port to C99

* Tue Jan 24 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.10.30-7
- Rebuild for ghostscript 10

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.30-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.10.30-1
- 3.10.30

* Wed Sep 23 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.10.29-1
- 3.10.29

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul  2 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.10.28-1
- 3.10.28

* Tue May  5 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.10.24-1
- 3.10.24

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 12 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.10.12-1
- 3.10.12

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.10.10-1
- 3.10.10

* Tue May  8 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.10.9-1
- 3.10.9

* Fri Feb 16 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.10.8-1
- 3.10.8

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.10.4-3
- Remove obsolete scriptlets

* Tue Jan 16 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.10.4-2
- Adjust ghostscript BR for packaging change

* Thu Sep 28 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.10.4-1
- 3.10.4

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.68-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Fri Jul 28 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.68-1
- 3.9.68

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.67-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.67-1
- 3.9.67

* Fri Apr 14 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.66-1
- 3.9.66

* Fri Mar 31 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.65-1
- 3.9.65

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.61-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb  3 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.61-1
- 3.9.61

* Sun Dec 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.60-1
- 3.9.60

* Wed Nov 16 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.59-1
- 3.9.59

* Wed Nov  9 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.58-1
- 3.9.58

* Mon Oct 24 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.57-1
- 3.9.57

* Wed Oct 12 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.56-1
- 3.9.56

* Fri Aug 26 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.54-1
- 3.9.54

* Fri Jul 29 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.51-1
- 3.9.51

* Fri Jul 15 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.50-1
- 3.9.50

* Sat Jul  2 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.49-1
- 3.9.49

* Sat Jun 25 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.48-2
- Kill rpath
- Kill some rpmlint warnings

* Sat Jun 25 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.48-1
- 3.9.48

* Fri Jun 24 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.40-4
- Actually build with Tcl/Tk
- format-security.patch again needed

* Fri Jun 24 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.9.40-3
- Create debuginfo rpm correctly
- Minor spec file cleanup

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 17 2015 Eduardo Mayorga Téllez <mayorga@fedoraproject.org> - 3.9.40-1
- Update to 3.9.40
- Disable debuginfo package
- Remove xcircuit-3.7.57-Werror=format-security.patch

* Sat Oct 10 2015 Peter Robinson <pbrobinson@fedoraproject.org> 3.7.57-2
- Rebuild (ngspice and aarch64)

* Mon Jul 13 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.7.57-1
- Update to latest version from the 3.7 series (3.7.57).
- Fix F23FTBFS (RHBZ#1240082).
- Add %%license.
- Rework spec.
- Add xcircuit-3.7.57-Werror=format-security.patch.
- Remove remove-AM_C_PROTOTYPES.patch.
- Fix bogus %%changelog entries.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.44-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.44-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.44-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 3.7.44-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.44-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 27 2013 Mat Booth <fedora@matbooth.co.uk> - 3.7.44-7
- Fix invalid auto-generated dependency.

* Mon Feb 25 2013 Mat Booth <fedora@matbooth.co.uk> - 3.7.44-6
- Remove obsoleted macro for automake >= 1.12
- Fix FTBFS rhbz #914582

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.44-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Oct 20 2012 Peter Robinson <pbrobinson@fedoraproject.org> 3.7.44-1
- Update to new 3.7.44 stable release
- Cleanup spec

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.164-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.164-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.164-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 30 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 3.6.164-1
- new upstream stable release

* Sun Nov 15 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 3.6.163-1
- new upstream stable release 3.6.163

* Sat Aug 01 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 3.6.161-1
- new upstream release 3.6.161

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 15 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 3.4.30-1
- new upstream release

* Sun Apr 06 2008 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 3.4.28-1
- closed #440387
- new upstream release
- opting the FEL related menu structure
- fixed and closed #439604: TCL 8.5.1

* Fri Apr 04 2008 Trond Danielsen <trondd@fedoraproject.org> - 3.4.27-2
- Added fix for bug #440387.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.4.27-3
- Autorebuild for GCC 4.3

* Sat Jan  5 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 3.4.27-2
- Rebuild for new Tcl 8.5

* Sun Oct 21 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 3.4.27-1
- new upstream release
- added coreutils and gtk as requires: #339771

* Fri Aug 24 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 3.4.26-23
- mass rebuild for fedora 8 - ppc

* Sun Aug 12 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 3.4.26-22
- fix for x86_64

* Sun Aug 12 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 3.4.26-21
- dump release

* Wed Aug 08 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 3.4.26-20
- patch %%{name}-3.4-memset.patch: Found memset with swapped arguments

* Mon Feb 26 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 3.4.26-19
- Rebuilt for rawhide

* Wed Jan 31 2007 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 3.4.26-18
- Fixed presence in Gnome menu

* Wed Aug 30 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 3.4.26-17
- Rebuilt for FC6 devel

* Sun Aug 27 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 3.4.26-16
- Again.

* Sun Aug 27 2006 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 3.4.26-15
- Fix tk and tcl libdir.

* Sat Aug 26 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 3.4.26-13
- Minor fixes to build properly under x86_64

* Sat Aug 26 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 3.4.26-12
- Minor fixes to build properly under x86_64

* Sat Aug 26 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 3.4.26-11
- Minor fixes to build properly under x86_64

* Sat Aug 26 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 3.4.26-10
- Opted %%{_prefix}/lib* prior to %%{_libdir}

* Sat Aug 26 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 3.4.26-9
- Added --libdir=%%{_libdir} to solve build error on x86_64

* Sat Aug 26 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 3.4.26-8
- Use of %%{__cp} -p to keep timestamp

* Sat Aug 26 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 3.4.26-7
- Fixed mandir

* Sat Aug 26 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 3.4.26-6
- Dropped patch xcircuit-3.4.26-xpm-gif.patch
- Removed useless Windows related files

* Fri Aug 25 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 3.4.26-5
- Added libXpm-devel as BR to prevent "image type "xpm" doesn't exist" error

* Fri Aug 25 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 3.4.26-4
- Added libXt-devel and zlib-devel as BR

* Fri Aug 25 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 3.4.26-3
- Fixed xcircuit.desktop and removed unneccessary installation for manual
- Used update-desktop-database in %%post and %%postun
- patch for "image type "xpm" doesn't exist"

* Thu Aug 24 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 3.4.26-2
- Fixed xcircuit.desktop, xcircuit.png
- Minor fixes

* Wed Aug 23 2006 Chitlesh Goorah <chitlesh@fedoraproject.org> - 3.4.26-1
- Initial Package
