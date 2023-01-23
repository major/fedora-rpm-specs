Name:               studio-controls
Version:            2.1.0
Release:            7%{?dist}
Summary:            Studio control for audio devices
BuildArch:          noarch

# The entire source code is GPLv2+

License:            GPLv2+
URL:                https://launchpad.net/ubuntustudio-controls
Source:             https://github.com/ovenwerks/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:      desktop-file-utils
BuildRequires:      systemd-rpm-macros
Requires:           jack-audio-connection-kit
Requires:           jack-audio-connection-kit-dbus
Requires:           jack-audio-connection-kit-example-clients
Requires:           a2jmidid
Requires:           dbus-tools
Requires:           psmisc
Requires:           pulseaudio-utils
Requires:           pulseaudio-module-jack
Requires:           python3-dbus
Requires:           python3-gobject
Requires:           python3
Requires:           python3-alsaaudio
Requires:           python-jack-client
Requires:           zita-ajbridge
Requires:           qasmixer
Requires:           pavucontrol
Requires:           hicolor-icon-theme
Requires:           shared-mime-info
Requires:           kernel-tools
Requires:           polkit
Recommends:         Carla

%description
Studio Controls is a small application that enables/disables realtime privilege
for users and controls jackdbus. It allows Jackdbus to be run from session
start. It also will detect USB audio devices getting plugged in after session
start and optionally connect them to jackdbus as a client or switch them in as
jackdbus master.

%prep
%autosetup -p 1 -n studio-controls-%{version}

%build
#Intentionally blank

%install
cp -r etc %{buildroot} --preserve=mode,timestamps
cp -r usr %{buildroot} --preserve=mode,timestamps
rm -rf %{buildroot}/usr/lib/systemd/system/ondemand.service.d

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%post
%systemd_post studio-system.service
%systemd_user_post studio.service

%preun
%systemd_preun studio-system.service
%systemd_user_preun studio.service

%postun
%systemd_postun_with_restart studio-system.service

%files
%doc AUTHORS
%doc README
%doc ROADMAP
%license COPYING
%{_bindir}/autojack
%{_bindir}/convert-studio-controls
%{_bindir}/studio-controls
%{_sbindir}/studio-system
%{_prefix}/lib/systemd/studio
%{_unitdir}/studio-system.service
%exclude %{_userunitdir}/session-monitor.service
%{_userunitdir}/studio.service
%dir %{_userunitdir}/default.target.wants/
%{_userunitdir}/default.target.wants/studio.service
%exclude %{_userunitdir}/indicator-messages.service.wants/session-monitor.service
%{_datadir}/applications/studio-controls.desktop
%{_datadir}/studio-controls/
%{_datadir}/icons/hicolor/*/apps/studio-controls.*
%{_datadir}/man/man1/studio-controls.1.gz
%{_datadir}/man/man2/autojack.2.gz
%{_datadir}/man/man2/studio-system.2.gz
%{_datadir}/polkit-1/actions/com.studiocontrols.pkexec.studio-controls.policy
%config %{_sysconfdir}/acpi/studio.sh
%config %{_sysconfdir}/acpi/events/studio-plug
%config %{_sysconfdir}/acpi/events/studio-unplug

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.0-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Erich Eickmeyer <erich@ericheickmeyer.com> - 2.1.0-1
- New upstream release

* Tue Oct 06 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 2.0.9-1
- Fixed: Single-channel interfaces were not being dealt with correctly for
  pulse-jack bridges

* Mon Sep 21 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 2.0.8-1
- This a bugfix that accepts older versions of config files and coverts values
  to something useful

* Sat Sep 12 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 2.0.7-1
- "MONITOR" should never be 'none' but was sometimes so this forces it to a
  better value

* Wed Sep 09 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 2.0.6-1
- bugfix for variable used before initialized

* Fri Aug 07 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 2.0.5-1
- Add lockfile to autojack to prevent two instances running
- Add lockfile to studio-controls to prevent two instances running
- Depend on zita-ajbridge version 0.8.4 fixes
- Fix phones detection for USB phones when not plugged in
- Catch jack error messages so they don't alarm user
- studio-controls: Catch system signals to exit
- up autojack signal version

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 2.0.4-1
- Fix spelling mistake
- Fix wrong indent
- Add "NVidia" to HDMI names
- Add a readout of the configuration to logging

* Sat Jul 25 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 2.0.3-1
- Make sure to use default-device and not PCH everywhere
- Catch pulse connection port is integer
- no more support for older config file
- logging should have log level set at read config file
- autojack needs to import glob before using it - bug fix

* Thu Jul 23 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 2.0.1-1
- Use saved value for device instead index - bug fix
- Log file too long re-enable log rotate - bugfix
- Dynamicly set default audio device - bugfix
- Make sure bridges are created before connecting
- Check if headphone device exists before checking

* Tue Jul 21 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 2.0.0-1
- Add white glow to icon to increase visibilty
- Head phone detection for PCH devices added
- Force PCH devices to be at least 128 buffer in extra devices
- Remove old jackdbus settings file before starting jack
- Pulse connect port extended to all Physical ports
- Fixed extra devices that are not sub device 0 don't work
- Fixed Apply for input only
- USB units with sub devices other than 0 will now auto connect
- Added extra logging level for lots of output
- Added better method of finding device sample rate
- Added new depend: python3-alsaaudio
- Detect headphone plug state on startup
- Use direct alsa mixer manipulation
- Add manual headphone switching
- Add ability use outputs other than system:playback_1/2
- general code clean up
- Readded Firewire backend
- Added fixes for alsa firewire devices
- make sure extra devices work correctly with all backends

* Fri Jul 03 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.99.2+really1.99.1-1
- Downgrade for regression

* Thu Jun 25 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.99.2-1
- New version 1.99.2
- Add white glow to icon to increase visibilty
- Start work on head phone detection
- Force PCH devices to be at least 128 buffer in extra devices
- Remove old jackdbus settings file before starting jack

* Sun May 10 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.99.1-1
- New version 1.99.1, removes tablet interface code for now

* Thu May 07 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.99.0-1
- New version 1.99.0, removes Ubuntu branding from icon

* Tue May 05 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.12.5-1
- New version 1.12.5

* Sun Apr 12 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.12.4-1
- New verison 1.12.4

* Wed Mar 04 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.12.3-3
- Remove ondemand.service files, add studio-system.service system file

* Wed Mar 04 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.12.3-2
- Add missing systemd files

* Mon Mar 02 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.12.3-1
- Fix symbolic links (actually add them)

* Sun Mar 01 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.12.2-1
- Temporarily remove unused tablet configuration gui for wacom

* Sun Feb 23 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.12.1-1
- Fix for bad adduser call (should be usermod)

* Sat Feb 15 2020 Erich Eickmeyer <erich@ericheickmeyer.com> - 1.12-1
- Initial release for Fedora
