%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
%global with_desktop_vendor_tag 1
%else
%global with_desktop_vendor_tag 0
%endif

Summary:      Virtual MIDI keyboard
Name:         vkeybd
Version:      0.1.18d
Release:      30%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:      GPL-2.0-or-later
URL:          http://www.alsa-project.org/~iwai/alsa.html
Source0:      http://www.alsa-project.org/~iwai/vkeybd-0.1.18d.tar.bz2
Source1:      vkeybd.png
Source2:      vkeybd.desktop
Patch3:       vkeybd-no-OSS.patch
Patch4:	      vkeybd-tcl8.6.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires: tk-devel >= 1:8.6, tk-devel < 1:8.7
BuildRequires: lash-devel

BuildRequires: desktop-file-utils

Requires: tk >= 1:8.6, tk > 1:8.6, lash
Requires: hicolor-icon-theme

%description
This is a virtual keyboard for AWE, MIDI and ALSA drivers.
It's a simple fake of a MIDI keyboard on X-windows system.
Enjoy a music with your mouse and "computer" keyboard :-)

%prep
%setup -q -n vkeybd
%patch -P3 -p0
%patch -P4 -p0
sed -i -e 's|-Wall -O|$(RPM_OPT_FLAGS)|' Makefile

%build
make %{?_smp_mflags} USE_LADCCA=1 TCL_VERSION=8.6 PREFIX=%{_prefix}

%install
make USE_LADCCA=1 PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
make USE_LADCCA=1 PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install-man
chmod 644 $RPM_BUILD_ROOT/%{_mandir}/man1/*
chmod 755 $RPM_BUILD_ROOT/%{_datadir}/vkeybd/vkeybd.tcl

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/vkeybd.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
%if 0%{?with_desktop_vendor_tag}
  --vendor fedora            \
%endif
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  --add-category X-Fedora                       \
  %{SOURCE2}

%files
%doc README ChangeLog
%{_bindir}/vkeybd
%{_bindir}/sftovkb
%{_datadir}/vkeybd/
%{_mandir}/man1/*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/64x64/apps/vkeybd.png

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1.18d-29
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.18d-14
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18d-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18d-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18d-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 17 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.1.18d-7
- Update for tk8.6 (#1107101)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18d-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 0.1.18d-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18d-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Jon Ciesla <limburgher@gmail.com> - 0.1.18d-3
- Correctly macroize vendor tag handling.

* Wed Feb 13 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.1.18d-2
- Reisntate vendor for < f19

* Mon Feb 11 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.1.18d-1
- Update to 0.1.18d

* Sat Feb 09 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 0.1.17a-15
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.17a-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.17a-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.17a-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 23 2009 Orcan Ogetbil <oget[DOT]fedora[AT]gmail[DOT]com> - 0.1.17a-11
- Update desktop file according to F-12 FedoraStudio feature

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.17a-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.17a-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.1.17a-8
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.1.17a-7
- Autorebuild for GCC 4.3

* Sat Jan 05 2008 Marcela Maslanova <mmaslano@redhat.com> 0.1.17a-6
- Upgrade to tcl8.5. 

* Sun Oct 07 2007 Anthony Green <green@redhat.com> 0.1.17a-5
- Add -no-OSS patch.

* Sun Oct 07 2007 Anthony Green <green@redhat.com> 0.1.17a-4
- Rebuild for new lash.

* Mon Feb 19 2007 Anthony Green <green@redhat.com> 0.1.17a-3
- Track tcl/tk in rawhide.  Now using 1:8.4.

* Thu Feb 01 2007 Anthony Green <green@redhat.com> 0.1.17a-2
- Update tcl/tk dependency to 8.5.

* Thu Oct 19 2006 Anthony Green <green@redhat.com> 0.1.17a-1
- Update sources.
- Remove jack-audio-connection-kit dependency, which is implied by
  lash dependency.

* Mon Sep 25 2006 Anthony Green <green@redhat.com> 0.1.17-8
- Tweak vkeybd.desktop file.
- Package ChangeLog.
- Clean up %%files.
- Move Categories to .desktop file.
- More LADCCA to LASH patching.
- Fix man page permissions.

* Tue Sep 19 2006 Anthony Green <green@redhat.com> 0.1.17-7
- Remove Require(post,postun) for gtk2, as per the packaging
  guidelines.

* Tue Sep 19 2006 Anthony Green <green@redhat.com> 0.1.17-6
- Remove my COPYING file.
- Don't use update-desktop-database.
- Clean up BuildRequires.
- Install the icon in the hicolor tree.
- Require hicolor-icon-theme.
- Don't Require tcl, since tk does that.
- Collar tk version requirements.
- Make vkeybd.tcl executable.
- Require(post,postun) gtk2 for gtk-update-icon-cache.

* Thu Jun  1 2006 Anthony Green <green@redhat.com> 0.1.17-5
- Add dist tag to Release.
- Build with _smp_mflags.
- Add GPL license file (COPYING).

* Tue Apr 25 2006 Anthony Green <green@redhat.com> 0.1.17-4
- Add Fernando Lopez-Lezcano's icon and related changes.
- Clean up macro usage.

* Tue Apr 25 2006 Anthony Green <green@redhat.com> 0.1.17-3
- Build with RPM_OPT_FLAGS with vkeybd-CFLAGS.patch.

* Sat Apr 22 2006 Anthony Green <green@redhat.com> 0.1.17-2
- Build for Fedora Extras.
- Port from ladcca to lash.
- Update description.

* Mon Dec 27 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.17-1
- updated to 0.1.17
- spec file cleanup
* Mon May 10 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 
- added buildrequires, detect tcl version
* Tue Feb 24 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.15-1
- updated to 0.1.15
* Sat Jul 26 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.13a-1
- updated to 0.1.13a
- added menu entries
* Mon Dec 30 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 0.1.12-1
- Initial build.
