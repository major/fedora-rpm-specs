Name:           gpx-viewer
Version:        0.4.0
Release:        31%{?dist}
Summary:        A simple gpx viewer

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://edge.launchpad.net/gpx-viewer
Source0:        http://edge.launchpad.net/gpx-viewer/trunk/0.4.0/+download/%{name}-%{version}.tar.gz
Patch0:         gpx-viewer-0.4.0-gtk3-bugfix.patch

BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  libchamplain-devel
BuildRequires:  libchamplain-gtk-devel
BuildRequires:  vala-devel
BuildRequires:  libxml2-devel
BuildRequires:  libgdl-devel
BuildRequires:  unique-devel
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires: make
#BuildRequires:  autoconf libtool

Requires:       hicolor-icon-theme
Requires:       shared-mime-info


%description
GPX Viewer is a simple tool to visualize tracks and waypoints
stored in a gpx file.

It has the following features:
- Show multiple GPX files
- Height map
- Show waypoints and multiple tracks per gpx file
- Highlight selected track
- Show speed vs time graph
- Show distance, duration, average, moving average, max speed,
  moving time and gps points
- Zooming
- Smoothing of speed graph
- Playback of track
- Highlighting points in speed graph on map


%prep
%setup -q
%patch -P0 -p0 -b.gtk3-bugfix

%build
%configure --disable-database-updates
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mime/packages/gpx-viewer.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.0-30
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.0-14
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 01 2015 Christian Krause <chkr@fedoraproject.org> - 0.4.0-8
- Add patch to fix GTK3 compatibility problem (#1216202)

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 0.4.0-7
- update mime scriptlet

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 20 2014 Kalev Lember <kalevlember@gmail.com> - 0.4.0-4
- Rebuilt for cogl soname bump

* Mon Feb 10 2014 Peter Hutterer <peter.hutterer@redhat.com> - 0.4.0-3
- Rebuild for libevdev soname bump

* Wed Feb 05 2014 Kalev Lember <kalevlember@gmail.com> - 0.4.0-2
- Rebuilt for cogl soname bump

* Sun Dec 01 2013 Christian Krause <chkr@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0
- Remove upstreamed patches

* Sun Sep 22 2013 Christian Krause <chkr@fedoraproject.org> - 0.3.0-2
- Fix position of markers (for libchamplain >= 0.12.4)

* Fri Sep 20 2013 Christian Krause <chkr@fedoraproject.org> - 0.3.0-1
- Unretire gpx-viewer (#1008701)
- Update to 0.3.0
- Minor cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.2.0-6
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Oct  4 2010 Bill Nottingham <notting@redhat.com> - 0.2.0-3
- Fix build
- drop mesa-drivers-dri-experimental buildreq

* Mon Sep 06 2010 Fabian Affolter <fabian@bernewireless.net> -0.2.0-2
- Patch for configure is still needed

* Mon Sep 06 2010 Fabian Affolter <fabian@bernewireless.net> -0.2.0-1
- Changed URL to new project home
- Added new BRs
- Patches removed
- Updated to new upstream version 0.2.0

* Fri Jul 09 2010 Fabian Affolter <fabian@bernewireless.net> -0.1.2-3
- Rebuild for libchamplain

* Mon Mar 15 2010 Fabian Affolter <fabian@bernewireless.net> -0.1.2-2
- Added patch to fix DSOLinking (#565157)

* Wed Nov 18 2009 Fabian Affolter <fabian@bernewireless.net> - 0.1.2-1
- Updated to new upstream version 0.1.2

* Sat Oct 10 2009 Fabian Affolter <fabian@bernewireless.net> - 0.1.1-2
- Added patches to make it work with new libchamplain

* Wed Sep 09 2009 Fabian Affolter <fabian@bernewireless.net> - 0.1.1-1
- Updated to new upstream version 0.1.1

* Fri Aug 14 2009 Fabian Affolter <fabian@bernewireless.net> - 0.1.0-1
- Updated source URL
- Updated to new upstream version 0.1.0

* Thu Aug 06 2009 Fabian Affolter <fabian@bernewireless.net> - 0.0.7-2
- Fixed BR

* Mon Jul 07 2009 Fabian Affolter <fabian@bernewireless.net> - 0.0.7-1
- Updated to new upstream version 0.0.7

* Mon Jul 07 2009 Fabian Affolter <fabian@bernewireless.net> - 0.0.5-1
- Initial spec for Fedora
