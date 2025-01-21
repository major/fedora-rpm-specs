Name:    soundtracker
Version: 1.0.4
Release: 5%{?dist}

Summary: Sound module composer/player

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:   GPL-2.0-or-later
URL:       http://www.soundtracker.org/
Source0:   http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Patch0:    soundtracker-1.0.2.1-else.patch

BuildRequires: autoconf
BuildRequires: gcc
BuildRequires: gtk2-devel >= 2.24
BuildRequires: libsndfile-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: SDL-devel
BuildRequires: libxml2-devel >= 2.6.0

%description
Soundtracker is a module tracker for the X Window System similar to
the DOS program `FastTracker'. Soundtracker is based on the XM file
format. The user interface makes use of GTK2.

%prep
%setup -q
%patch -P 0 -p1

%build
%configure
%make_build

%install
%make_install
%find_lang soundtracker

%files -f soundtracker.lang
%license COPYING
%doc AUTHORS FAQ NEWS README TODO
%{_bindir}/%{name}
%{_bindir}/%{name}_convert_config
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/extensions/
%dir %{_datadir}/%{name}/extensions/sample-editor/
%{_datadir}/%{name}/*.*
%{_datadir}/%{name}/extensions/sample-editor/sox.menu
%{_datadir}/appdata/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1*
%{_datadir}/pixmaps/%{name}-icon.png

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul  26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.4-4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 12 2023 Peter Hanecak <hany@hany.sk> - 1.0.4-1
- Update to 1.0.4
- Build now requires also libxml2-devel
- Update of patch macro syntax

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jan 29 2023 Peter Hanecak <hany@hany.sk> - 1.0.3-1
- Update to 1.0.3

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan  9 2022 Peter Hanecak <hany@hany.sk> - 1.0.2.1-2
- Fixed compilation on s390x

* Sun Jan  9 2022 Peter Hanecak <hany@hany.sk> - 1.0.2.1-1
- Update to 1.0.2.1
- Build now requires also pulseaudio-libs-devel

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep  6 2020 Peter Hanecak <hany@hany.sk> - 1.0.1-1
- Update to 1.0.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 25 2020 Peter Hanecak <hany@hany.sk> - 1.0.0.1-1
- Update to GTK2-based 1.0.0.1, latest stable release
- Small clean-up of the spec file

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 06 2015 Jaromir Capik <jcapik@redhat.com> - 0.6.8-23
- Adding OSS auto-load in th %%post and modules-load.d (#1245940)
- Fixing bogus dates in the changelog

* Thu Jul 23 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.6.8-22
- Add MimeTypes to desktop file, remove deprecated Categories and vendor
- Mark COPYING as %%license

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 04 2013 Jaromir Capik <jcapik@redhat.com> - 0.6.8-17
- aarch64 support (#926556)
- spec cleaning

* Sun Feb 24 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.6.8-16
- Desktop files must retain the vendor tag in Fedora < 19.  They are only
  allowed to get rid of it in Fedora 19 and later.  This makes it so that we're
  only breaking user customization of menus when they upgrade to Fedora 19.

* Mon Feb 11 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.6.8-15
- Correct desktop file error

* Mon Feb 11 2013 Brendan Jones <brendan.jones.it@gmail.com> 0.6.8-14
- Remove vendor from desktop file

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Feb 12 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.6.8-11
- Add soundtracker-0.6.8-channel-mute-w-o-gdk-pixbuf.patch

* Sat Feb 12 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.6.8-10
- Update spec file comments
- Stop using gdk-pixbuf
- Explicitly link with -ldl

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.6.8-6
- fix license tag

* Fri Aug 29 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.6.8-5
- Actually use no-setuid patch, which fixes rawhide FTBFS issue.

* Sat May 31 2008 Hans Ulrich Niedermann <hun@n-dimensional.de> - 0.6.8-4
- Disable ALSA support. Upstream requires alsa 0.4 or 0.5 API, F9 has 1.0

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.8-3
- Autorebuild for GCC 4.3

* Sun Sep 10 2006 Callum Lerwick <seg@haxxed.com> - 0.6.8-2
- --disable-asm breaks x86_64 builds.

* Sun Aug 13 2006 Callum Lerwick <seg@haxxed.com> - 0.6.8-1
- New upstream version.
- Enable SDL driver, this indirectly gives ALSA support, however it is rather
  unstable so we can't kill off the OSS driver just yet.
- Compiling with jack support crashes on startup, even if the jack driver is
  not enabled.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.6.7-5
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 0.6.7-4
- rebuilt

* Wed Nov 10 2004 Michael Schwendt <mschwendt[AT]users.sf.net> - 0:0.6.7-3
- BR gettext-devel

* Mon Feb 2 2004 Nils O. Selåsdal <NOS@Utel.no> - 0:0.6.7-0.fdr.2
- 0.6.7.0.fdr.1 was not  based on latest -pre rpm. Fixes build errors.

* Thu Jan 29 2004 Nils O. Selåsdal <NOS@Utel.no> - 0:0.6.7-0.fdr.1
- 0.6.7 release

* Mon Nov 17 2003 Nils O. Selåsdal <NOS@Utel.no> - 0:0.6.7-0.fdr.0.4.pre6
- Revert soundtracker-mkinstalldirs.patch to patch provided by Michael Schwendt,
  Now builds on RH9 again.

* Fri Nov 14 2003 Nils O. Selåsdal <NOS@Utel.no>  - 0:0.6.7-0.fdr.0.3.pre6
- add soundtracker-mkinstalldirs.patch that prevents po/Makefile.in.in from
  doing funny things. Now builds on FC1.

* Sat Aug 30 2003 Nils O. Selåsdal <NOS@Utel.no> - 0:0.6.7-0.fdr.0.2.pre6
- Remove old and painful changelogs from doc,
- Don't use macros for commands run within the .spec file
- Disable jack support.

* Thu Aug 28 2003 Nils O. Selåsdal <NOS@Utel.no> - 0:0.6.7-0.fdr.0.1.pre6
- Correct package version
- Add missing BuildRequires. Explicit disable features we don't want(alsa,asm),
- Remove ABOUT-NLS from documentation
- Place .desktop file in external source, use correct .desktop category.

* Wed Aug 27 2003 Nils O. Selåsdal <NOS@Utel.no> - 0:0.6.7-0.fdr.1.pre6
- Initial RPM release for Fedora
- Rework Makefile.am's to work with recent autotools and to not
  install setuid root
