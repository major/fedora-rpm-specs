%global gittag 1.9.0
Name:           tlp
Version:        1.9.0
Release:        6%{?dist}
Summary:        Optimize laptop battery life
License:        GPL-2.0-or-later
URL:            https://linrunner.de/tlp
Source0:        https://github.com/linrunner/TLP/archive/%{gittag}.tar.gz#/%{name}-%{gittag}.tar.gz
Patch0:         0000-license-wrong-address.patch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  systemd
BuildRequires:  libappstream-glib

#The following requires are not detected:
Requires:       ethtool
Requires:       hdparm
Requires:       iw
Requires:       rfkill
Requires:       systemd
Requires:       udev
Requires:       usbutils
Requires:       pciutils
Recommends:     kernel-tools
Recommends:     smartmontools

#Note: Conflicts with laptop-mode-tools
#Makes sure laptop_mode isn't being used:
Conflicts:      %{_sbindir}/laptop_mode
BuildArch:      noarch

%description
TLP is a feature-rich command-line utility, saving laptop battery power
without the need to delve deeper into technical details.

TLP’s default settings are already optimized for battery life and implement
Powertop’s recommendations out of the box. Moreover TLP is highly
customizable to fulfill specific user requirements.

Settings are organized into two profiles, allowing to adjust between
savings and performance independently for battery (BAT) and AC operation.
In addition TLP can enable or disable Bluetooth, NFC, Wi-Fi and WWAN radio
devices on boot.

For ThinkPads and selected other laptops it provides a unified way
to configure charge thresholds and re-calibrate the battery.

%package rdw
Summary:        Radio device wizard for TLP
Requires:       NetworkManager >= 1.20
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description rdw
Radio device wizard is an add-on to TLP. It provides event based
switching of Bluetooth, NFC, Wi-Fi and WWAN radio devices on:
 - network connect/disconnect
 - dock/undock

%prep
%autosetup -p1 -n TLP-%{gittag}

%build
%make_build

%install
%make_install \
  TLP_SDSL=%{_unitdir}/../system-sleep \
  TLP_NO_INIT=1 \
  TLP_WITH_ELOGIND=0 \
  TLP_SYSD=%{_unitdir} \
  TLP_ULIB=%{_udevrulesdir}/.. \
  TLP_SBIN=%{_bindir}

#Install manpages:
make install-man DESTDIR=%{buildroot}
make install-man-rdw DESTDIR=%{buildroot}

%check
appstream-util validate-relax --nonet \
  %{buildroot}/%{_datadir}/metainfo/*.xml

%files
%config(noreplace) %{_sysconfdir}/tlp.conf
%config(noreplace) %{_sysconfdir}/tlp.d
%license LICENSE
%doc AUTHORS COPYING README.rst changelog
%{_bindir}/bluetooth
%{_bindir}/nfc
%{_bindir}/run-on-ac
%{_bindir}/run-on-bat
%{_bindir}/%{name}
%{_bindir}/%{name}-pd
%{_bindir}/%{name}-stat
%{_bindir}/%{name}ctl
%{_bindir}/wifi
%{_bindir}/wwan
%exclude %{_bindir}/tlp-rdw
%{_mandir}/man*/*
%exclude %{_mandir}/man*/tlp-rdw*
%{_datadir}/tlp
%{_udevrulesdir}/85-tlp.rules
%{_udevrulesdir}/../tlp-usb-udev
%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/*
%{_datadir}/fish/vendor_completions.d/*
%exclude %{_datadir}/bash-completion/completions/tlp-rdw
%exclude %{_datadir}/zsh/site-functions/_tlp-radio-device
%exclude %{_datadir}/zsh/site-functions/_tlp-rdw
%exclude %{_datadir}/fish/vendor_completions.d/tlp-rdw.fish
%{_unitdir}/*.service
%{_unitdir}/../system-sleep
%{_datadir}/metainfo/*.metainfo.xml
%{_sharedstatedir}/tlp
%{_datadir}/polkit-1/actions/tlp-pd.policy
%{_datadir}/dbus-1/system-services/net.hadess.PowerProfiles.service
%{_datadir}/dbus-1/system-services/org.freedesktop.UPower.PowerProfiles.service
%{_datadir}/dbus-1/system.d/net.hadess.PowerProfiles.conf
%{_datadir}/dbus-1/system.d/org.freedesktop.UPower.PowerProfiles.conf

%files rdw
%doc AUTHORS COPYING README.rst changelog
%{_bindir}/tlp-rdw
%{_mandir}/man*/tlp-rdw*
%{_prefix}/lib/NetworkManager/dispatcher.d/99tlp-rdw-nm
%{_udevrulesdir}/85-tlp-rdw.rules
%{_udevrulesdir}/../tlp-rdw-udev
%{_datadir}/bash-completion/completions/tlp-rdw
%{_datadir}/zsh/site-functions/_tlp-radio-device
%{_datadir}/zsh/site-functions/_tlp-rdw
%{_datadir}/fish/vendor_completions.d/tlp-rdw.fish

%post
%systemd_post tlp.service
if [ $1 -eq 2 ] ; then
    systemctl unmask systemd-rfkill.service
    systemctl unmask power-profiles-daemon.service
fi

%preun
%systemd_preun tlp.service

%postun
%systemd_postun_with_restart tlp.service

%changelog
%autochangelog
