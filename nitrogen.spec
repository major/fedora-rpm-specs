Name:           nitrogen
Version:        1.6.1
Release:        16%{?dist}
Summary:        Background browser and setter for X windows

# Code is GPLv2+ and zlib, icons are CC-BY-SA as described in COPYING
License:        GPLv2+ and zlib and CC-BY-SA
URL:            https://github.com/l3ib/%{name}/
Source:         https://github.com/l3ib/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:         appdata.patch
BuildRequires: make
BuildRequires:  gtkmm24-devel
BuildRequires:  libpng-devel
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  m4
BuildRequires:  libtool
BuildRequires:  gettext-devel
BuildRequires:  gcc-c++
Requires:       gtkmm24

%description
A background browser and setter for X windows that can be used in two
modes: browser and recall. It features Multihead and Xinerama awareness,
a recall mode to be used in start up scripts, uses the freedesktop.org
standard for thumbnails, can set the GNOME background, command line set
modes for use in scripts, inotify monitoring of browse directory, lazy
loading of thumbnails to conserve memory and an 'automatic' set mode
which determines the best mode to set an image based on its size.

%prep
%setup -q

%patch0

%build
autoreconf -fi

%configure --disable-dependency-tracking
# -lX11 is missing (DSO: https://fedoraproject.org/wiki/UnderstandingDSOLinkChange)
make %{?_smp_mflags} CFLAGS="%{optflags}" LDFLAGS="-lX11"

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files -f %{name}.lang
%doc COPYING NEWS README AUTHORS ChangeLog
%{_bindir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/icons/hicolor/16x16/actions/wallpaper-*.png
%{_datadir}/icons/hicolor/16x16/devices/video-display.png
%{_datadir}/icons/hicolor/16x16/mimetypes/image-x-generic.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 2019 James Wrigley <jamesnz@fedoraproject.org> - 1.6.1-8
- Added patch to fix some fields in the appdata file (and the install location)
- Fixed build error on rawhide by adding gcc-c++ as a BuildRequires

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.1-4
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 06 2017 James Wrigley <james@puiterwijk.org> - 1.6.1-1
- New upstream version, 1.6.1.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 James Wrigley <jwrigley7@gmail.com> - 1.6.0-1
- New upstream version, 1.6.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.5.2-15
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 9 2014 James Wrigley <jwrigley7@gmail.com> - 1.5.2-13
- Rolled back to the last stable release to fix bug in master.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-12.20140405git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 22 2014 James Wrigley <jwrigley7@gmail.com> - 1.5.2-11.20140405git
- Fixed compile bug on F19

* Sat Apr 5 2014 James Wrigley <jwrigley7@gmail.com> - 1.5.2-10.20140405git
- Rolled back by one commit to fix https://github.com/l3ib/nitrogen/issues/46

* Sun Feb 9 2014 James Wrigley <jwrigley7@gmail.com> - 1.5.2-9.20131218git
- Fixed issue with the .desktop file not being installed properly

* Thu Jan 30 2014 James Wrigley <jwrigley7@gmail.com> - 1.5.2-8.20131218git
- Updated autoconf version to 2.69, now using a git snapshot from 20131218

* Mon Sep 9 2013 James Wrigley <jwrigley7@gmail.com> - 1.5.2-7
- Un-orphaning package

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-4
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.5.2-2
- Rebuild for new libpng

* Fri Jul 01 2011 Sandro Mathys <red at fedoraproject.org> - 1.5.2-1
- New upstream version 1.5.2

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May 27 2010 Sandro Mathys <red at fedoraproject.org> - 1.5.1-3
- fixed missing libX11 BuildRequire

* Sat May 01 2010 Sandro Mathys <red at fedoraproject.org> - 1.5.1-2
- corrected license and improved the spec file a little

* Fri Feb 05 2010 Sandro Mathys <red at fedoraproject.org> - 1.5.1-1
- new version with fixed licensing and some bugfixes
- added desktop file and updating of the icon caches

* Thu Oct 22 2009 Sandro Mathys <red at fedoraproject.org> - 1.4-1
- initial build

