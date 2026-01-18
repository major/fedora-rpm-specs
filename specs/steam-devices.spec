%global commit daf01bc7e1e3d65987ab0f6e2c93707170a686b3
%if 0%{?rhel} && 0%{?rhel} < 10
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%else
%global shortcommit %{sub %{commit} 1 7}
%endif
%global commitdate 20251216


Name:           steam-devices
Version:        1.0.0.101^git%{commitdate}.%{shortcommit}
Release:        6%{?dist}
License:        MIT
Summary:        Device support for Steam-related hardware
Url:            https://github.com/ValveSoftware/steam-devices/
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  systemd-rpm-macros

# Temporary workaround to obsolete and replace the equivalent i686 package in RPMFusion
# so we don't break current installs. Can be removed after a while.
Obsoletes:      steam-devices < %{version}-%{release}
Provides:       steam-devices = %{version}-%{release}

%description
This package contains the necessary permissions for gaming devices (such as
gamepads, joysticks and VR headsets) that can be used by Wine, Lutris, Heroic,
and other non-Steam games and game launchers.

%prep
%autosetup -n %{name}-%{commit} -S git_am

%install
install -Dpm0644 60-steam-input.rules %{buildroot}%{_udevrulesdir}/60-steam-input.rules
install -Dpm0644 60-steam-vr.rules %{buildroot}%{_udevrulesdir}/60-steam-vr.rules

%files
%license LICENSE
%{_udevrulesdir}/60-steam-input.rules
%{_udevrulesdir}/60-steam-vr.rules

%changelog
* Fri Jan 16 2026 Simone Caronni <negativo17@gmail.com> - 1.0.0.101^git20251216.daf01bc-6
- Update to latest snapshot.

* Wed Nov 26 2025 Simone Caronni <negativo17@gmail.com> - 1.0.0.101^git20251018.4d7e6c1-5
- Update to latest snapshot.

* Fri Oct 17 2025 Simone Caronni <negativo17@gmail.com> - 1.0.0.101^git20250927.d3f7cd6-4
- Update to latest snapshot.

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0.101^git20240522.e2971e4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Mar 18 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> - 1.0.0.101^git20240522.e2971e4-2
- Added Conditional to fix FTBFS on epel8 and epel9

* Mon Mar 17 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> - 1.0.0.101^git20240522.e2971e4-1
- Update to 1.0.0.101^git20240522.e2971e4-1

* Mon Mar 17 2025 Simone Caronni <negativo17@gmail.com> - 1.0.0.100^git20240522.e2971e4-4
- Small cosmetic changes.

* Mon Mar 17 2025 Simone Caronni <negativo17@gmail.com> - 1.0.0.100^git20240522.0.e2971e4-3
- Temporarily provide/obsolete RPMFusion's equivalent i686 package.

* Sat Mar 15 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> - 1.0.0.100^git20240522.0.e2971e4-2
- Updated description to remove outdated information

* Fri Mar 7 2025 Shawn W. Dunn <sfalken@cloverleaf-linux.org> 1.0.0.100^git20240522.0.e2971e4-1
- new package

