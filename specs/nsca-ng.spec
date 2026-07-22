Name:           nsca-ng
Version:        1.7
Release:        %autorelease
Summary:        Add-on for transferring check results (and other commands) to Nagios or Icinga
License:        LicenseRef-Callaway-BSD
URL:            https://nsca-ng.org
Source:         https://github.com/weiss/nsca-ng/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libbsd-devel
BuildRequires:  libconfuse-devel
BuildRequires:  libev-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  systemd-devel

%description
%{summary}.

%package client
Summary:        %{SUMMARY} (client)
Conflicts:      nsca-client

%description client
%{summary}.

%package server
Summary:        %{SUMMARY} (server)
Requires:       user(nagios)

%description server
%{summary}.

%prep
%autosetup
# Bundled stuff
sed -i -e "/lib\/ev\/libev.m4/d" m4/ev.m4
sed -r -i -e "/lib\/(ev|pidfile)\/Makefile/d" configure.ac
sed -r -i -e "/^MAYBE_(EV|PIDFILE)/d" lib/Makefile.am
rm -vr lib/{pidfile,ev}

%build
autoreconf -vfi
%configure \
  --enable-client \
  --enable-server \
  --with-ev=external \
  %{nil}
%make_build

%install
%make_install
install -Dpm0644 -t %{buildroot}%{_unitdir} etc/nsca-ng.{service,socket}

%check
%make_build check

%post server
%systemd_post nsca-ng.service nsca-ng.socket

%preun server
%systemd_preun nsca-ng.service nsca-ng.socket

%postun server
%systemd_postun_with_restart nsca-ng.service nsca-ng.socket

%files client
%license COPYING
%doc README NEWS PROTOCOL
%{_sbindir}/send_nsca
%{_mandir}/man8/send_nsca.8*
%config(noreplace) %{_sysconfdir}/send_nsca.cfg
%{_mandir}/man5/send_nsca.cfg.5*

%files server
%license COPYING
%doc README NEWS PROTOCOL
%{_unitdir}/nsca-ng.{socket,service}
%{_sbindir}/nsca-ng
%{_mandir}/man8/nsca-ng.8*
%attr(0640,nagios,nagios) %config(noreplace) %{_sysconfdir}/nsca-ng.cfg
%{_mandir}/man5/nsca-ng.cfg.5*

%changelog
%autochangelog
