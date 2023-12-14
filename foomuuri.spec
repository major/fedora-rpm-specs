Name:           foomuuri
Version:        0.22
Release:        1%{?dist}
Summary:        Multizone bidirectional nftables firewall
License:        GPL-2.0-or-later
URL:            https://github.com/FoobarOy/foomuuri
Source0:        https://github.com/FoobarOy/foomuuri/archive/v%{version}/foomuuri-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
%if (%{defined fedora} || %{defined epel})
BuildRequires:  pylint
BuildRequires:  python3-dbus
BuildRequires:  python3-flake8
BuildRequires:  python3-gobject
BuildRequires:  python3-pycodestyle
BuildRequires:  python3-requests
BuildRequires:  python3-systemd
%endif
BuildRequires:  systemd-rpm-macros
Requires:       nftables
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-requests
Requires:       python3-systemd
Recommends:     fping
Recommends:     (foomuuri-firewalld if NetworkManager)
%{?systemd_requires}


%description
Foomuuri is a firewall generator for nftables based on the concept of zones.
It is suitable for all systems from personal machines to corporate firewalls,
and supports advanced features such as a rich rule language, IPv4/IPv6 rule
splitting, dynamic DNS lookups, a D-Bus API and FirewallD emulation for
NetworkManager's zone support.


%package firewalld
Summary:        FirewallD emulation configuration files for Foomuuri
BuildArch:      noarch
Requires:       %{name} = %{version}


%description firewalld
Foomuuri is a firewall generator for nftables based on the concept of zones.
It is suitable for all systems from personal machines to corporate firewalls,
and supports advanced features such as a rich rule language, IPv4/IPv6 rule
splitting, dynamic DNS lookups, a D-Bus API and FirewallD emulation for
NetworkManager's zone support.

This optional package provides FirewallD D-Bus emulation for Foomuuri,
allowing dynamically assign interfaces to Foomuuri zones via NetworkManager.


%prep
%autosetup -p1


%build


%install
make install DESTDIR=%{buildroot}


%if (%{defined fedora} || %{defined epel})
%check
make test
%endif


%post
%systemd_post foomuuri.service foomuuri-dbus.service foomuuri-iplist.timer foomuuri-iplist.service foomuuri-monitor.service foomuuri-resolve.timer foomuuri-resolve.service
%tmpfiles_create foomuuri.conf


%preun
%systemd_preun foomuuri.service foomuuri-dbus.service foomuuri-iplist.timer foomuuri-iplist.service foomuuri-monitor.service foomuuri-resolve.timer foomuuri-resolve.service


%postun
%systemd_postun foomuuri.service foomuuri-iplist.service foomuuri-resolve.service
if [ $1 -ge 1 ]; then
    systemctl reload-or-try-restart foomuuri.service > /dev/null 2>&1 || :
fi
%systemd_postun_with_restart foomuuri-dbus.service foomuuri-monitor.service foomuuri-iplist.timer foomuuri-resolve.timer


%files
%license COPYING
%doc README.md CHANGELOG.md
%doc %{_mandir}/man8/foomuuri.8*
%attr(0750, root, adm) %dir %{_sysconfdir}/foomuuri
%{_sbindir}/foomuuri
%{_sysctldir}/50-foomuuri.conf
%dir %{_datadir}/foomuuri
%{_datadir}/foomuuri/default.services.conf
%{_datadir}/foomuuri/static.nft
%{_unitdir}/foomuuri.service
%{_unitdir}/foomuuri-dbus.service
%{_unitdir}/foomuuri-iplist.service
%{_unitdir}/foomuuri-iplist.timer
%{_unitdir}/foomuuri-monitor.service
%{_unitdir}/foomuuri-resolve.service
%{_unitdir}/foomuuri-resolve.timer
%{_tmpfilesdir}/foomuuri.conf
%ghost %dir %{_rundir}/foomuuri
%attr(0700, root, root) %dir %{_sharedstatedir}/foomuuri
%{_datadir}/dbus-1/system.d/fi.foobar.Foomuuri1.conf


%files firewalld
%{_datadir}/dbus-1/system.d/fi.foobar.Foomuuri-FirewallD.conf
%{_datadir}/foomuuri/dbus-firewalld.conf


%changelog
* Tue Dec 12 2023 Kim B. Heino <b@bbbs.net> - 0.22-1
- Upgrade to 0.22

* Fri Oct 06 2023 Kim B. Heino <b@bbbs.net> - 0.21-1
- Upgrade to 0.21

* Wed Sep 27 2023 Kim B. Heino <b@bbbs.net> - 0.20-4
- Upgrade to snapshot 5bccb4d

* Thu Sep 21 2023 Kim B. Heino <b@bbbs.net> - 0.20-3
- Upgrade to snapshot dcb332c

* Mon Sep 18 2023 Kim B. Heino <b@bbbs.net> - 0.20-2
- Upgrade to snapshot 34816cc

* Tue Aug 15 2023 Kim B. Heino <b@bbbs.net> - 0.20-1
- Upgrade to 0.20

* Mon Jul 31 2023 Kim B. Heino <b@bbbs.net> - 0.19-2
- Upgrade to snapshot 6b4eb23

* Fri May 19 2023 Kim B. Heino <b@bbbs.net> - 0.19-1
- Upgrade to 0.19

* Thu May 04 2023 Kim B. Heino <b@bbbs.net> - 0.18-3
- Upgrade to snapshot 07cf534

* Tue May 02 2023 Kim B. Heino <b@bbbs.net> - 0.18-2
- Upgrade to snapshot 0d0f101

* Tue Apr 18 2023 Kim B. Heino <b@bbbs.net> - 0.18-1
- Upgrade to 0.18

* Fri Mar 31 2023 Kim B. Heino <b@bbbs.net> - 0.17-1
- Upgrade to 0.17

* Mon Mar 13 2023 Kim B. Heino <b@bbbs.net> - 0.16-2
- Upgrade to snapshot b901a8b

* Mon Feb 27 2023 Kim B. Heino <b@bbbs.net> - 0.16-1
- Initial version
