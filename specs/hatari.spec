Summary: An Atari ST/STE/TT/Falcon emulator suitable for playing games
Name: hatari
Version: 2.5.0
Release: 4%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://hatari.tuxfamily.org/
Source0: http://download.tuxfamily.org/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1: %{name}.appdata.xml

BuildRequires: gcc
BuildRequires: cmake
BuildRequires: SDL2-devel
BuildRequires: zlib-devel
BuildRequires: libpng-devel
BuildRequires: readline-devel
BuildRequires: portaudio-devel
BuildRequires: capstone-devel
BuildRequires: systemd-devel
BuildRequires: python3-devel
BuildRequires: python3-gobject
BuildRequires: gtk3
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils
Requires: hicolor-icon-theme
# Required by zip2st and atari-hd-image
Requires: unzip
Requires: mtools
Requires: dosfstools


%package ui
Summary: External user interface for Hatari
Requires: %{name} = %{version}-%{release}
Requires: python3
Requires: python3-gobject
Requires: gtk3
Requires: hicolor-icon-theme


%description
Hatari is an emulator for the Atari ST, STE, TT and Falcon computers.

The Atari ST was a 16/32 bit computer system which was first released 
by Atari in 1985. Using the Motorola 68000 CPU, it was a very popular 
computer having quite a lot of CPU power at that time.

Unlike most other open source ST emulators which try to give you a good
environment for running GEM applications, Hatari tries to emulate the hardware
as close as possible so that it is able to run most of the old Atari games
and demos.  Because of this, it may be somewhat slower than less accurate
emulators.


%description ui
Hatari UI is an out-of-process user interface for the Hatari emulator and its 
built-in debugger which can (optionally) embed the Hatari emulator window. 


%prep
%setup -q

# Fix interpreter
for pyfile in tools/atari-convert-dir.py tools/debugger/hatari_profile.py tools/hconsole/example.py tools/hconsole/hconsole.py python-ui/hatariui.py python-ui/gentypes.py python-ui/debugui.py
do
  sed -i '1s|/usr/bin/env python3|%{__python3}|' $pyfile
done


%build
%cmake \
  -DCMAKE_BUILD_TYPE:STRING=None \
  -DDOCDIR:PATH=%{_pkgdocdir} \
  -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build


%install
%cmake_install

# Install French man page
install -d -m 755 %{buildroot}%{_mandir}/fr/man1
install -p -m 644 doc/fr/hatari.1 %{buildroot}%{_mandir}/fr/man1

# Install AppData file
install -d -m 755 %{buildroot}%{_datadir}/metainfo
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo


%check
%ctest

# Validate desktop files
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/hatariui.desktop

# Validate AppData file
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml


%files
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
%{_mandir}/fr/man1/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/icons/hicolor/*/mimetypes/*
%{_datadir}/mime/packages/hatari.xml
%doc %{_pkgdocdir}
%license gpl.txt
%exclude %{_bindir}/hatariui
%exclude %{_datadir}/%{name}/hatariui
%exclude %{_datadir}/%{name}/hconsole
%exclude %{_mandir}/man1/hatariui.1*
%exclude %{_mandir}/man1/hconsole.1*
%exclude %{_pkgdocdir}/hatariui

%files ui
%{_bindir}/hatariui
%{_datadir}/%{name}/hatariui
%{_datadir}/%{name}/hconsole
%{_mandir}/man1/hatariui.1*
%{_mandir}/man1/hconsole.1*
%{_datadir}/applications/hatariui.desktop
%doc %{_pkgdocdir}/hatariui


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.5.0-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 22 2024 Andrea Musuruane <musuruan@gmail.com> - 2.5.0-1
- Updated to new upstream release

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 21 2022 Andrea Musuruane <musuruan@gmail.com> - 2.4.1-1
- Updated to new upstream release

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Andrea Musuruane <musuruan@gmail.com> - 2.4.0-1
- Updated to new upstream release

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 27 17:05:46 CET 2020 Andrea Musuruane <musuruan@gmail.com> - 2.3.1-1
- Updated to new upstream release

* Thu Aug 06 2020 Andrea Musuruane <musuruan@gmail.com> - 2.2.1-10
- Fixed FTBFS for F33 (BZ #1863844)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 02 2019 Andrea Musuruane <musuruan@gmail.com> - 2.2.1-5
- Enabled parallel build
- Enabled regression test suite

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.1-4
- Rebuild for readline 8.0

* Sat Feb 16 2019 Andrea Musuruane <musuruan@gmail.com> - 2.2.1-3
- Fixed Requires for gtk3 python UI

* Sat Feb 16 2019 Andrea Musuruane <musuruan@gmail.com> - 2.2.1-2
- pygtk2 still only support python2

* Sat Feb 16 2019 Andrea Musuruane <musuruan@gmail.com> - 2.2.1-1
- Updated to upstream 2.2.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Andrea Musuruane <musuruan@gmail.com> - 2.1.0-3
- Fix FTBFS for F29

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 Andrea Musuruane <musuruan@gmail.com> - 2.1.0-1
- Updated to upstream 2.1.0
- Used new AppData directory

* Wed Feb 21 2018 Andrea Musuruane <musuruan@gmail.com> - 2.0.0-12
- Added gcc dependency
- Spec file clean up

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.0-10
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Andrea Musuruane <musuruan@gmail.com> - 2.0.0-6
- Added a patch to fix X11 window embedding with SDL2

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.0.0-5
- Rebuild for readline 7.x

* Sat Dec 31 2016 Andrea Musuruane <musuruan@gmail.com> - 2.0.0-4
- Added a patch to support both hatari config file locations in hatariui
- Added a patch to support hatari v2.0 option changes in hatariui

* Tue Dec 20 2016 Dan Horák <dan[at]danny.cz> - 2.0.0-3
- Added a patch to compile under s390(x)

* Sat Dec 17 2016 Andrea Musuruane <musuruan@gmail.com> - 2.0.0-2
- Added a patch to compile under aarch64

* Sun Nov 27 2016 Andrea Musuruane <musuruan@gmail.com> - 2.0.0-1
- Updated to upstream 2.0.0
- Updated description

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Oct 18 2015 Andrea Musuruane <musuruan@gmail.com> 1.9.0-2
- Correctly marked license file

* Sat Oct 17 2015 Andrea Musuruane <musuruan@gmail.com> 1.9.0-1
- Updated to upstream 1.9.0
- Spec file cleanup

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.8.0-2
- Add an AppData file for the software center

* Wed Sep 24 2014 Andrea Musuruane <musuruan@gmail.com> 1.8.0-1
- Updated to upstream 1.8.0
- Dropped cleaning at the beginning of %%install
- Spec file cleanup

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Sep 13 2013 Andrea Musuruane <musuruan@gmail.com> 1.7.0-3
- Used unversioned docdir (BZ #993813)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 27 2013 Andrea Musuruane <musuruan@gmail.com> 1.7.0-1
- Updated to upstream 1.7.0
- Fixed vendor tag logic in a prettier way
- Dropped obsolete Group, Buildroot, %%clean and %%defattr

* Wed Apr 24 2013 Jon Ciesla <limburgher@gmail.com> - 1.6.2-4
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 05 2012 Andrea Musuruane <musuruan@gmail.com> 1.6.2-1
- updated to upstream 1.6.2

* Sat Jan 14 2012 Andrea Musuruane <musuruan@gmail.com> 1.6.1-1
- updated to upstream 1.6.1

* Fri Jan 06 2012 Andrea Musuruane <musuruan@gmail.com> 1.6.0-1
- updated upstream URL
- updated upstream Source0

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.5.0-2
- Rebuild for new libpng

* Sun Sep 25 2011 Andrea Musuruane <musuruan@gmail.com> 1.5.0-1
- updated to upstream 1.5.0
- added patches to include hatari window at hatariui startup (SF #18340)
- dropped Debian man pages now that hatari has its own

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 14 2010 Andrea Musuruane <musuruan@gmail.com> 1.4.0-4
- added license among docs

* Sun Nov 14 2010 Andrea Musuruane <musuruan@gmail.com> 1.4.0-3
- ui subpackage now requires the fully versioned base package
- more consistent macro usage

* Fri Nov 12 2010 Andrea Musuruane <musuruan@gmail.com> 1.4.0-2
- fixed Requires
- added manpages from Debian
- removed script extensions (.sh, .py) from scripts installed into /usr/bin
- macro usage is more consistent now

* Sun Jul 18 2010 Andrea Musuruane <musuruan@gmail.com> 1.4.0-1
- updated to upstream 1.4.0
- dropped README.tos now that emutos.txt is supplied

* Sat Mar 06 2010 Andrea Musuruane <musuruan@gmail.com> 1.3.1-2
- link against libm (BZ #564801)

* Sat Sep 12 2009 Andrea Musuruane <musuruan@gmail.com> 1.3.1-1
- updated to upstream 1.3.1

* Sat Aug 22 2009 Andrea Musuruane <musuruan@gmail.com> 1.3.0-1
- updated to upstream 1.3.0
- disabled new upstream python UI
- updated icon cache snippets
- used upstream Mac OS X icons
- preserved french man page timestamp

* Mon Aug 10 2009 Andrea Musuruane <musuruan@gmail.com> 1.2.0-4
- updated Source0 URL

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Andrea Musuruane <musuruan@gmail.com> 1.2.0-1
- updated to upstream 1.2.0
- dropped no longer needed hmsa tool patch
- updated upstream URL
- updated Source0 URL

* Sat Nov 29 2008 Andrea Musuruane <musuruan@gmail.com> 1.1.0-1
- updated to upstream 1.1.0

* Sat Apr 05 2008 Andrea Musuruane <musuruan@gmail.com> 1.0.1-1
- updated to upstream 1.0.1

* Mon Mar 17 2008 Andrea Musuruane <musuruan@gmail.com> 1.0.0-1
- updated to upstream 1.0.0
- removed icon extension from desktop file to match Icon Theme Specification

* Sun Feb 10 2008 Andrea Musuruane <musuruan@gmail.com> 0.95-5
- Rebuilt against gcc 4.3

* Sat Oct 06 2007 Andrea Musuruane <musuruan@gmail.com> 0.95-4
- Fixed doc/authors.txt file encoding
- Updated icon cache scriptlets to be compliant to new guidelines

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.95-3
- Rebuild for selinux ppc32 issue.

* Mon Aug 20 2007 Andrea Musuruane <musuruan@gmail.com> 0.95-2
- changed license due to new guidelines 
- removed %%{?dist} tag from changelog

* Sat Jun 23 2007 Andrea Musuruane <musuruan@gmail.com> 0.95-1
- updated to upstream 0.95
- updated description
- README.tos and hatari.desktop are no longer built in the spec file
- added new upstream hmsa tool
- added new upstream french man page
- updated icon cache scriptlets to be compliant to new guidelines
- cosmetic changes

* Sat Mar 17 2007 Andrea Musuruane <musuruan@gmail.com> 0.90-6
- dropped --add-category X-Fedora from desktop-file-install
- changed .desktop category to Game;Emulator;
- now using sed to fix makefile not to strip binaries during make install
- cosmetic changes to BR section

* Mon Oct 23 2006 Andrea Musuruane <musuruan@gmail.com> 0.90-5
- added a patch not to strip binaries during make install
- added hicolor-icon-theme to Requires

* Sat Oct 21 2006 Andrea Musuruane <musuruan@gmail.com> 0.90-4
- added README.tos to explain that Hatari is shipped with EmuTOS

* Fri Oct 20 2006 Andrea Musuruane <musuruan@gmail.com> 0.90-3
- new release for FE migration

* Sun Oct 08 2006 Andrea Musuruane <musuruan@gmail.com> 0.90-2
- replaced %%_mandir with %%{_mandir}
- full URL is now specified in the Source tag
- added .desktop file and icons

* Sat Sep 30 2006 Andrea Musuruane <musuruan@gmail.com> 0.90-1
- initial package


