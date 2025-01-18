Summary:	Daemon for exposing ALSA sequencer applications in JACK MIDI system
Name:		a2jmidid
Version:	9
Release:	16%{?dist}
URL:		https://github.com/linuxaudio/a2jmidid
Source0:	https://github.com/linuxaudio/a2jmidid/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Backported from upstream
Patch0:		%{name}-man.patch
Patch1:		%{name}-portname.patch
Patch2:		%{name}-add-riscv64-support.patch

# a2jmidi_bridge.c and j2amidi_bridge.c are GPLv2+
# The rest is GPLv2
# Automatically converted from old format: GPLv2 and GPLv2+ - review is highly recommended.
License:	GPL-2.0-only AND GPL-2.0-or-later

BuildRequires:	alsa-lib-devel
BuildRequires:	dbus-devel
BuildRequires:	gcc
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	meson
Requires:	dbus
Requires:	python3

%description
a2jmidid is a project that aims to ease usage of legacy ALSA sequencer
applications, in a JACK MIDI enabled system. There are two ways to use legacy
ALSA sequencer applications in JACK MIDI system.

The first approach is to use automatic bridging. For every ALSA sequencer port
you get one JACK MIDI port. If ALSA sequencer port is both input and output
one, you get two JACK MIDI ports, one input and output.

The second approach is to static bridges. You start application that creates
one ALSA sequencer port and one JACK MIDI port. Such bridge is unidirectional.

%prep
%autosetup -p1

# Fix Python shebangs
sed -i 's|^#!/usr/bin/env python3|#!/usr/bin/python3|' a2j_control

%build
%meson
%meson_build

%install
%meson_install

%files
%doc AUTHORS.rst README.rst CHANGELOG.rst
%license LICENSE
%{_bindir}/a2j
%{_bindir}/%{name}
%{_bindir}/a2j_control
%{_bindir}/a2jmidi_bridge
%{_bindir}/j2amidi_bridge
%{_datadir}/dbus-1/services/org.gna.home.a2jmidid.service
%{_mandir}/man1/a2j*
%{_mandir}/man1/j2a*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 9-15
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 06 2023 Songsong Zhang <U2FsdGVkX1@gmail.com> - 9-11
- Add riscv64 patch from https://github.com/jackaudio/a2jmidid/pull/18

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Guido Aulisi <guido.aulisi@gmail.com> - 9-1
- Update to version 9
- New upstream

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 8-18
- Use Fedora link flags
- BR: gcc
- Moved license file to %%license
- Fix Python shebangs

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 8-16
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Orcan Ogetbil <oget [dot] fedora [at] gmail [dot] com> - 8-12
- Add patch to fix build on ppc64*

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Oct 26 2014 Peter Robinson <pbrobinson@fedoraproject.org> 8-8
- Add patch to fix ftbfs on aarch64

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 13 2013 Brendan Jones <brendan.jones.it@gmail.com> 8-3
- Release bump for F19

* Sat Sep 15 2012 Jørn Lomax <northlomax@gmail.com> - 8-2
- added patch for man pages

* Mon Jul 09 2012 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 8-1
- Update to 8.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 7-1
- Update to 7.
- Drop upstreamed patches.

* Fri Jul 16 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 6-3
- Fix license tag

* Wed May 19 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 6-2
- Fix DSO linking

* Sat Jan 30 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 6-1
- Update to 6

* Thu Nov 26 2009 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 5-1
- Initial Fedora package. Specfile borrowed from SuSE.

* Mon Jun 15 2009 Toni Graffy <toni@links2linux.de> - 5-0.pm.1
- update to 5
* Sun Aug 03 2008 Toni Graffy <toni@links2linux.de> - 4-0.pm.1
- update to 4
* Sat Oct 27 2007 Toni Graffy <toni@links2linux.de> - 2-0.pm.1
- update to 2
* Mon Aug 27 2007 Toni Graffy <toni@links2linux.de> - 1-0.pm.1
- Initial build 1
