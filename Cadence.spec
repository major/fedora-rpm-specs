# Global variables for github repository
%global commit0 c146ff90efa5d7518421fa90a86c205ff6b84a84
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global pname cadence
%global commitdate 20210316

Name:    Cadence
Version: 1.0.0
Release: 0.24.%{commitdate}git%{shortcommit0}%{?dist}
Summary: A set of tools useful for audio production
# The entire source code is GPLv2+ except c++/jackbridge/ which is ISC License
# Following files are licensed under LGPLv2+
# data/pulse2jack/play+rec.pa
# data/pulse2jack/play.pa
# data/pulse2loopback/play+rec.pa
# data/pulse2loopback/play.pa
License: GPLv2+
URL:     https://github.com/falkTX/Cadence
Source0: https://github.com/falkTX/%{name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch0:  cadence_001_fedora_support.patch
Patch1:  cadence-desktop-patch
Patch2:  cadence-makefile.patch

BuildRequires: gcc gcc-c++
BuildRequires: python3-qt5-base
BuildRequires: qt5-qtbase-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: pulseaudio-module-jack
BuildRequires: python3-dbus
BuildRequires: a2jmidid
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: jack-audio-connection-kit-dbus
BuildRequires: jack_capture
BuildRequires: desktop-file-utils
BuildRequires: make
Requires:      hicolor-icon-theme
#Requires:      ladish
Requires:      python3-qt5
Requires:      jack_capture
Requires:      a2jmidid

%description
Here's a brief description of the main tools:

Cadence:
The main app. It performs system checks, manages JACK, calls other tools and
make system tweaks.

Cadence-JackMeter:
Digital peak meter for JACK.
It automatically connects itself to all application JACK output ports that are
also connected to the system output.

Cadence-JackSettings:
Simple and easy-to-use configure dialog for jackdbus.
It can configure JACK's driver and engine parameters, and it also supports
LADISH studios.

Cadence-Logs:
Small tool that shows JACK, A2J, LASH and LADISH logs in a multi-tab window.
The logs are viewed in a text box, making it easy to browse and extract status
messages using copy and paste commands.

Cadence-Render:
Tool to record (or 'render') a JACK project using jack-capture, controlled by
JACK Transport.
It supports a vast number of file types and can render in both realtime and
freewheel modes.

Cadence-XY Controller:
Simple XY widget that sends and receives data from Jack MIDI.
It can send data through specific channels and has a MIDI Keyboard too.

Catarina:
A Patchbay test app, created while the patchcanvas module was being developed.
It allows the user to experiment with the patchbay, without using ALSA, JACK or
LADISH. You can save & load patchbay configurations too.

Catia:
JACK Patchbay, with some neat features like A2J bridge support and JACK
Transport.
It's supposed to be as simple as possible (there's Claudia for advanced things),
so it can work nicely on Windows and Mac too.
Currently has ALSA-MIDI support in experimental stage (it doesn't automatically
refresh the canvas when changes happen externally).

Claudia:
LADISH frontend; just like Catia, but focused at session management through
LADISH.
It has a bit more features than the official LADISH GUI, with a nice preview of
the main canvas in the bottom-left.
It also implements the 'Claudia-Launcher' add-application style for LADISH.

Claudia-Launcher:
A multimedia application launcher with LADISH support.
It searches for installed packages (not binaries), and displays the respective
content as a launcher.
The content is got through an hardcoded database, created and/or modified to
suit the target distribution.
Currently supports Debian and ArchLinux based distros.

%prep
%autosetup -p 1 -n %{name}-%{commit0}

# remove windows stuff
rm -rf data/windows/

# Fix error: Empty %%files file debugsourcefiles.list
sed -i "s|-O0 -g|%{optflags}|" c++/Makefile.mk

%build
%{set_build_flags}
%make_build SKIP_STRIPPING=true DEBUG=true
  
%install
%make_install PREFIX=%{_prefix}

# E: non-executable-script /usr/share/cadence/src/cadence.py 644 /usr/bin/env python3
chmod a+x %{buildroot}%{_datadir}/%{pname}/src/*.py

# E: non-executable-script /usr/share/cadence/pulse2loopback/play+rec.pa 644 /usr/bin/pulseaudio -nF
chmod a+x %{buildroot}%{_datadir}/%{pname}/pulse2*/{play+rec,play,play+rec}.pa

# removing /usr/share/cadence/pulse2*/*.pa files removes the implicit /usr/bin/pulseaudio dependency
rm %{buildroot}%{_datadir}/%{pname}/pulse2*/*.pa

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md
%license COPYING
%{_bindir}/%{pname}
%{_bindir}/%{pname}-aloop-daemon
%{_bindir}/%{pname}-jackmeter
%{_bindir}/%{pname}-jacksettings
%{_bindir}/%{pname}-logs
%{_bindir}/%{pname}-pulse2jack
%{_bindir}/%{pname}-pulse2loopback
%{_bindir}/%{pname}-render
%{_bindir}/%{pname}-session-start
%{_bindir}/%{pname}-xycontroller
%{_bindir}/catarina
%{_bindir}/catia
%{_bindir}/claudia
%{_bindir}/claudia-launcher
%{_datadir}/applications/*.desktop
%dir %{_datadir}/%{pname}/
%{_datadir}/%{pname}/icons/claudia-hicolor/*/apps/*.png
%{_datadir}/%{pname}/icons/claudia-hicolor/index.theme
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
#%%{_datadir}/%%{pname}/pulse2*/*.pa
%{_datadir}/%{pname}/templates/*
%{_datadir}/%{pname}/src/*
%{_sysconfdir}/X11/Xsession.d/61-cadence-session-inject.sh
%config(noreplace) %{_sysconfdir}/xdg/autostart/cadence-session-start.desktop

%changelog
* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.24.20210316gitc146ff9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.23.20210316gitc146ff9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.22.20210316gitc146ff9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.21.20210316gitc146ff9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.20.20210316gitc146ff9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.19.20210316gitc146ff9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.18.20210316gitc146ff9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.17.20210316gitc146ff9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 14 2021 Scott Talbert <swt@techie.net> - 1.0.0-0.16.20210316gitc146ff9
- Replace python3-qt5-devel BD with python3-qt5-base (for pyuic5)

* Thu Apr 08 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-0.15.20210316gitc146ff9
- Update to 1.0.0-0.15.20210316gitc146ff9
- remove /usr/share/cadence/pulse2*/*.pa files removes the implicit /usr/bin/pulseaudio dependency 
  Fixes (RHBZ#1916362)

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.14.20200604gitc167f35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-0.13.20200604gitc167f35
- Update to 1.0.0-0.13.20200604gitc167f35

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.12.20200504git5787908
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-0.11.20200504git5787908
- Update to 1.0.0-0.11.20200504git5787908

* Fri Feb 07 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-0.10.20200103git9324d24
- Add %%make_build SKIP_STRIPPING=true DEBUG=true

* Fri Feb 07 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-0.9.20200103git9324d24
- Update to 1.0.0-0.9.20200103git9324d24

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.8.20191021git0642494
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-0.7.20191021git0642494
- Remove RR ladish due package is dead

* Wed Oct 30 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-0.6.20191021git0642494
- Update to 1.0.0-0.6.20191021git0642494

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.5.20180827git4a5f5b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.4.20180827git4a5f5b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-0.3.20180827git4a5f5b4
- Add RR hicolor-icon-theme
- Add comment which files are licensed under LGPLv2+
- Take ownership of dirs

* Thu Dec 13 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-0.2.20180827git4a5f5b4
- Use correct link for sources
- Use %%autosetup macro
- Use %%{set_build_flags}
- Use %%make_install PREFIX=%%{_prefix}
- List all files 

* Thu Dec 13 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-0.1.20180827git4a5f5b4
- Initial build
