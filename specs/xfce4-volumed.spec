# https://bugzilla.redhat.com/show_bug.cgi?id=541154
%global _hardened_build 1
%global upstreamname xfce4-volumed-pulse
%global minorversion 0.2

Name:           xfce4-volumed
Version:        0.2.3
Release:        36%{?dist}
Summary:        Daemon to add additional functionality to the volume keys of the keyboard
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://git.xfce.org/apps/xfce4-volumed-pulse/
Source0:        https://archive.xfce.org/src/apps/%{upstreamname}/%{minorversion}/%{upstreamname}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  xfconf-devel
BuildRequires:  libnotify-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk3-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  keybinder3-devel

Provides:       xfce4-volumed-pulse

%description
The xfce4-volumed adds additional functionality to the volume up/down and mute
keys of the keyboard. It makes the keys work without configuration and uses 
the XFCE 4 mixer's defined card and track for choosing which track to act on. 
The volume level is shown in a notification.

%prep
%setup -qn %{upstreamname}-%{version}
echo "Icon=multimedia-volume-control" >> data/%{name}.desktop


%build
%configure
%make_build


%install
%make_install
desktop-file-install \
  --add-category="Utility" \
  --dir=%{buildroot}/%{_datadir}/applications \
  %{buildroot}/%{_sysconfdir}/xdg/autostart/%{upstreamname}.desktop

# one launcher is enough, we don't want to have a daemon in the menu
rm -rf %{buildroot}/%{_datadir}/applications/


%files
%doc AUTHORS ChangeLog README THANKS
%license COPYING
/etc/xdg/autostart/%{upstreamname}.desktop
%{_bindir}/%{upstreamname}


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.2.3-35
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.3-26
- Fix FTBFS (drop BR on gstreamer)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-25
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 13 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.2.3-20
- Rebuild (xfce 4.13)
- Drop unneeded dependency on xfce4-mixer

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.2.3-1
- Bump to 0.2.3 and provides xfce4-volumed-pulse replacement for xfce4-volumed

* Wed Feb 14 2018 Filipe Rosset <rosset.filipe@gmail.com> - 0.1.13-15
- Spec cleanup / modernization

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.1.13-2
- Rebuild for new libpng

* Fri May 27 2011 Orion Poplawski <orion@cora.nwra.com> - 0.1.13-1
- Update to 0.1.13
- Drop libnotify patch fixed upstream
- Upstream now accepts CFLAGS environment variable in configure

* Sun Mar 06 2011 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.12-1
- Update to 0.1.12 (fixes #680111)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Nov 27 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.11-1
- Update to 0.1.11

* Sat Nov 06 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.10-2
- Fix for libnotify 0.7.0

* Wed Nov 03 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.10-1
- Update to 0.1.10 (#631199)
- Build requirements change: Require keybinder-devel instead of xcb-util-devel

* Tue Nov 17 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.8-1
- Update to 0.1.8

* Sun Nov 01 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.7-1
- Update to 0.1.7

* Wed Oct 28 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5

* Sat Sep 05 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.1.4-1
- Initial Fedora package
