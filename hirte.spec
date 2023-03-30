Name:       hirte
Version:    0.1.1
Release:    3%{?dist}
Summary:    A systemd service controller for multi-nodes environments
License:    GPL-2.0-or-later
URL:        https://github.com/containers/hirte
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  golang-github-cpuguy83-md2man

Requires:   systemd

%description
Hirte is a systemd service controller for multi-nodes environements with a
predefined number of nodes and with a focus on highly regulated environment
such as those requiring functional safety (for example in cars).

This package contains the controller and command line tool.

%post
%systemd_post hirte.service

%preun
%systemd_preun hirte.service

%postun
%systemd_postun_with_restart hirte.service

%files
%config(noreplace) %{_sysconfdir}/hirte/hirte.conf
%doc README.md
%doc README.developer.md
%license LICENSE
%{_bindir}/hirte
%{_datadir}/dbus-1/interfaces/org.containers.hirte.Job.xml
%{_datadir}/dbus-1/interfaces/org.containers.hirte.Manager.xml
%{_datadir}/dbus-1/interfaces/org.containers.hirte.Monitor.xml
%{_datadir}/dbus-1/interfaces/org.containers.hirte.Node.xml
%{_datadir}/hirte/config/hirte-default.conf
%{_mandir}/man1/hirte.*
%{_mandir}/man5/hirte.conf.*
%{_datadir}/dbus-1/system.d/org.containers.hirte.conf
%{_unitdir}/hirte.service
%{_unitdir}/hirte.socket

#--------------------------------------------------

%package agent
Summary:    Hirte service controller agent
Requires:   systemd

%description agent
Hirte is a systemd service controller for multi-nodes environements with a
predefined number of nodes and with a focus on highly regulated environment
such as those requiring functional safety (for example in cars).

This package contains the node agent.

%post agent
%systemd_post hirte-agent.service

%preun agent
%systemd_preun hirte-agent.service

%postun agent
%systemd_postun_with_restart hirte-agent.service

%files agent
%config(noreplace) %{_sysconfdir}/hirte/agent.conf
%doc README.md
%license LICENSE
%{_bindir}/hirte-agent
%{_datadir}/dbus-1/system.d/org.containers.hirte.Agent.conf
%{_datadir}/hirte-agent/config/hirte-default.conf
%{_mandir}/man1/hirte-agent.*
%{_mandir}/man5/hirte-agent.conf.*
%{_unitdir}/hirte-agent.service
%{_userunitdir}/hirte-agent.service

#--------------------------------------------------

%package ctl
Summary:  Hirte service controller command line tool
Requires: %{name} = %{version}-%{release}
Provides: hirtectl = %{version}-%{version}

%description ctl
Hirte is a systemd service controller for multi-nodes environements with a
predefined number of nodes and with a focus on highly regulated environment
such as those requiring functional safety (for example in cars).
This package contains the service controller command line tool.

%files ctl
%doc README.md
%license LICENSE
%{_bindir}/hirtectl
%{_mandir}/man1/hirtectl.*

#--------------------------------------------------

%prep
%autosetup

%build
%meson -Dapi_bus=system
%meson_build

%install
%meson_install

%check
%meson_test


%changelog
* Tue Mar 28 2023 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-3
- Drop the man page for hirtectl from the main hirte package

* Mon Mar 27 2023 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-2
- Remove hirtectl from the hirte package since it is now in its own subpackage

* Mon Mar 27 2023 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.1-1
- Update to 0.1.1
- Adjust Source0 to point to /archive/v<version>/hirte-<version>.tar.gz
- Adjust the location of dbus-1/system.d/org.containers.hirte.conf and
  bus-1/system.d/org.containers.hirte.Agent.conf so they are in _datadir
- Add the hirte-ctl subpackage (which provides hirtectl for convenience)

* Wed Mar 22 2023 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.0-5
- Adjust summary and description according to the changes made upstream

* Wed Mar 22 2023 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.0-4
- Fix the Source0 to point to a resolvable url
- Replace tabs with spaces

* Tue Mar 21 2023 Martin Perina <mperina@redhat.com> - 0.1.0-3
- Move the different files section near the different package definition

* Tue Mar 21 2023 Martin Perina <mperina@redhat.com> - 0.1.0-2
- Make rpmlint happier

* Tue Mar 21 2023 Martin Perina <mperina@redhat.com> - 0.1.0-1
- Initial release

