%global forgeurl https://github.com/eeickmeyer/fedora-jam-audio-configuration

Name:           fedora-jam-audio-config
Version:        2.0.4
%global tag     %{version}
%forgemeta
Release:        1%{?dist}
Summary:        PipeWire-JACK audio configuration tool for Fedora Jam

BuildArch:      noarch

License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}
BuildRequires:  desktop-file-utils
BuildRequires:  systemd-rpm-macros
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  python3-devel
Requires:       grub2-common bash polkit systemd pipewire pipewire-utils pulseaudio-utils
Requires:       python3 >= 3.9
Requires:       (python3-gobject or python3-PyQt6)

%description
A Python application providing a graphical interface for configuring
PipeWire-JACK settings and GRUB kernel parameters to optimize a system
for low-latency audio performance on Fedora Jam. The GUI supports both
GTK (via PyGObject) and Qt (via PyQt6) backends, and includes systemd
user services to apply audio configuration automatically at login.

%prep
%autosetup -n %{archivename}

%build
%make_build -C po

%install
install -Dpm 0755 usr/bin/fedorajam-audio-config -t %{buildroot}%{_bindir}
install -Dpm 0755 usr/sbin/fedorajam-pwjack-config -t %{buildroot}%{_sbindir}
install -Dpm 0644 usr/lib/systemd/user/fedorajam-dummy-audio.service -t %{buildroot}%{_userunitdir}
install -Dpm 0644 usr/lib/systemd/user/fedorajam-pwconfig-start.service -t %{buildroot}%{_userunitdir}
install -Dpm 0644 usr/lib/systemd/user-preset/90_fedorajam-pwconfig-start.preset -t %{buildroot}%{_userpresetdir}
install -Dpm 0644 usr/share/applications/fedorajam-audio-config.desktop -t %{buildroot}%{_datadir}/applications
install -Dpm 0644 usr/share/man/man1/fedorajam-audio-config.1 -t %{buildroot}%{_mandir}/man1
install -Dpm 0644 usr/share/man/man1/fedorajam-pwjack-config.1 -t %{buildroot}%{_mandir}/man1

# Install Python application
install -d %{buildroot}%{_datadir}/fedorajam-audio-config
cp -pr usr/share/fedorajam-audio-config/* %{buildroot}%{_datadir}/fedorajam-audio-config/

# Install translations
%make_install -C po PREFIX=%{_datadir}/locale
%find_lang %{name} --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/fedorajam-audio-config.desktop
%{python3} -m py_compile usr/bin/fedorajam-audio-config
bash -n usr/sbin/fedorajam-pwjack-config
%{python3} -m py_compile usr/share/fedorajam-audio-config/__init__.py
%{python3} -m py_compile usr/share/fedorajam-audio-config/main.py
%{python3} -m py_compile usr/share/fedorajam-audio-config/i18n.py
%{python3} -m py_compile usr/share/fedorajam-audio-config/backend/__init__.py
%{python3} -m py_compile usr/share/fedorajam-audio-config/backend/audio_config.py
%{python3} -m py_compile usr/share/fedorajam-audio-config/ui/__init__.py
%{python3} -m py_compile usr/share/fedorajam-audio-config/ui/base.py
%{python3} -m py_compile usr/share/fedorajam-audio-config/ui/gtk_ui.py
%{python3} -m py_compile usr/share/fedorajam-audio-config/ui/qt_ui.py

%post
%systemd_user_post fedorajam-dummy-audio.service fedorajam-pwconfig-start.service
if ! [ -f %{_sysconfdir}/profile.d/fedorajam-pwjack.sh ]; then
   %{_sbindir}/fedorajam-pwjack-config 1024 48000
fi

%preun
%systemd_user_preun fedorajam-dummy-audio.service fedorajam-pwconfig-start.service
if [ "$1" -eq 0 ]; then
  if [ -f %{_sysconfdir}/profile.d/fedorajam-pwjack.sh ]; then
    %{__rm} -f %{_sysconfdir}/profile.d/fedorajam-pwjack.sh
  fi
  if [ -f %{_sysconfdir}/fedorajamboot.cfg ]; then
    %{__rm} -f %{_sysconfdir}/fedorajamboot.cfg
  fi
fi

%postun
%systemd_user_postun_with_restart fedorajam-dummy-audio.service fedorajam-pwconfig-start.service

%files -f %{name}.lang
%license COPYING
%{_bindir}/fedorajam-audio-config
%{_sbindir}/fedorajam-pwjack-config
%{_datadir}/fedorajam-audio-config/
%ghost %{_sysconfdir}/profile.d/fedorajam-pwjack.sh
%ghost %{_sysconfdir}/fedorajamboot.cfg
%{_userunitdir}/fedorajam-dummy-audio.service
%{_userunitdir}/fedorajam-pwconfig-start.service
%{_userpresetdir}/90_fedorajam-pwconfig-start.preset
%{_datadir}/applications/fedorajam-audio-config.desktop
%{_mandir}/man1/fedorajam-audio-config.1*
%{_mandir}/man1/fedorajam-pwjack-config.1*
%doc README.md

%changelog
* Sun Feb 22 2026 Erich Eickmeyer <erich@ericheickmeyer.com> 2.0.3-1
- Complete rewrite in Python

* Sat Jan 24 2026 Erich Eickmeyer <erich@ericheickmeyer.com> 1.2-1
- Update to version 1.2
- Fix for rpmlint warnings

* Wed Jan 14 2026 Erich Eickmeyer <erich@ericheickmeyer.com> 1.0-1
- Initial release
