%global commit e2971e45063f6b327ccedbf18e168bda6749155c
%global shortcommit %{sub %{commit} 1 7}
%global commitdate 20240522.0


Name:           steam-devices
Version:        1.0.0.100%{?commit:^git%{commitdate}.%{shortcommit}}
Release:        2%{?dist}
License:        MIT
Summary:        Device support for Steam-related hardware
Url:            https://github.com/ValveSoftware/steam-devices/
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  git-core
BuildRequires:  systemd-rpm-macros

%description
The Steam Controller features dual trackpads, HD haptic feedback, dual-stage
triggers, back grip buttons, and fully-customizable control schemes.
Steam VR is a full-features, 360° room-scale virtual reality experience

This package also provides support for many other third party devices, such
as gamepads and joysticks, that can be used by Wine, Lutris, Heroic, and
other non-steam games and game launchers.

%prep
%autosetup -n %{name}-%{?commit:%{commit}}%{!?commit:%{version}} -S git_am

%build

%install
mkdir -p %{buildroot}%{_udevrulesdir}
install -Dm0644 60-steam-input.rules %{buildroot}%{_udevrulesdir}/60-steam-input.rules
install -Dm0644 60-steam-vr.rules %{buildroot}%{_udevrulesdir}/60-steam-vr.rules

%files
%license LICENSE
%{_udevrulesdir}/60-steam-input.rules
%{_udevrulesdir}/60-steam-vr.rules

%changelog
* Sat Mar 15 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> - 1.0.0.100^git20240522.0.e2971e4-2
- Updated description to remove outdated information

* Fri Mar 7 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> 1.0.0.100^git20240522.0.e2971e4-1
- new package

