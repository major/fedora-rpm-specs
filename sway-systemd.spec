Name:           sway-systemd
Version:        0.2.2
Release:        3%{?dist}
Summary:        Systemd integration for Sway session

License:        MIT
URL:            https://github.com/alebastr/sway-systemd
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros

Requires:       python3dist(dbus-next)
Requires:       python3dist(i3ipc)
Requires:       python3dist(psutil)
Requires:       python3dist(python-xlib)
Requires:       python3dist(tenacity)
Requires:       sway
Requires:       systemd
Recommends:     /usr/bin/dbus-update-activation-environment

%description
%{summary}.

The goal of this project is to provide a minimal set of configuration files
and scripts required for running Sway in a systemd environment.

This includes several areas of integration:
 - Propagate required variables to the systemd user session environment.
 - Define sway-session.target for starting user services.
 - Place GUI applications into a systemd scopes for systemd-oomd compatibility.

%prep
%autosetup


%build
%meson \
    -Dcgroups=enabled
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/sway/config.d/10-systemd-session.conf
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/session.sh
%{_userunitdir}/sway-session.target

%config(noreplace) %{_sysconfdir}/sway/config.d/10-systemd-cgroups.conf
%{_libexecdir}/%{name}/assign-cgroups.py

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 26 2022 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.2.2-1
- Update to 0.2.2

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 28 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.2.1-1
- Update to 0.2.1

* Mon Aug 09 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.2.0-1
- Update to 0.2.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 30 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2

* Wed Mar 10 2021 Aleksei Bavshin <alebastr@fedoraproject.org> - 0.1.1-1
- Initial import (#1932728)
