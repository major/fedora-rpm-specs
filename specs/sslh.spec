# disable tests until perl-conf-libconfig is in Fedora
%global with_tests   0

Name:    sslh
Version: 2.3.1
Release: %autorelease
Summary: Applicative protocol(SSL/SSH) multiplexer
License: GPL-2.0-only
URL:     https://github.com/yrutschle/sslh
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  libev-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  perl(Pod::Man)

%if %{with_tests}
# Required for %%check
BuildRequires:  perl(IO::Socket::INET6)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Conf::Libconfig)
BuildRequires:  valgrind
BuildRequires:  psmisc
%endif

%description
sslh accepts connections on specified ports, and forwards them further
based on tests performed on the first data packet sent by the remote
client.

Probes for HTTP, SSL, SSH, OpenVPN, tinc, XMPP are implemented, and
any other protocol that can be tested using a regular expression, can
be recognized. A typical use case is to allow serving several services
on port 443 (e.g. to connect to ssh from inside a corporate firewall,
which almost never block port 443) while still serving HTTPS on that port.

Hence sslh acts as a protocol multiplexer, or a switchboard. Its name
comes from its original function to serve SSH and HTTPS on the same port.

%prep
%autosetup -p1

# Create a sysusers.d config file
cat >sslh.sysusers.conf <<EOF
u sslh - 'SSLH daemon' /dev/null -
EOF

%build
./genver.sh >version.h
%configure
%make_build USESYSTEMD=1

# Convert ChangeLog to UTF-8
iconv --from=ISO-8859-1 --to=UTF-8 ChangeLog > ChangeLog.conv && \
touch -r ChangeLog ChangeLog.conv && \
mv ChangeLog.conv ChangeLog

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_systemdgeneratordir}

install -p -m 0755 sslh-fork %{buildroot}%{_sbindir}/%{name}
install -p -m 0755 sslh-select %{buildroot}%{_sbindir}/%{name}-select
install -p -m 0755 sslh-ev %{buildroot}%{_sbindir}/%{name}-ev
install -p -m 0755 systemd-sslh-generator %{buildroot}%{_systemdgeneratordir}/systemd-sslh-generator

# Install configuration
install -p -m 0644 basic.cfg %{buildroot}%{_sysconfdir}/%{name}/%{name}.cfg

# Replace "nobody" with "sslh" in the default configuration
sed -i 's/user: "nobody";/user: "sslh";/g' %{buildroot}%{_sysconfdir}/%{name}/%{name}.cfg

# Install man page and set up redirects for the alternative engines
install -p -m 0644 sslh.8.gz %{buildroot}%{_mandir}/man8/
echo ".so man8/sslh.8" > %{buildroot}%{_mandir}/man8/sslh-select.8
echo ".so man8/sslh.8" > %{buildroot}%{_mandir}/man8/sslh-ev.8

# Install systemd service and socket units
cat > %{buildroot}%{_unitdir}/%{name}.service << 'EOF'
[Unit]
Description=SSL/SSH multiplexer
After=network.target
Documentation=man:sslh(8)

[Service]
EnvironmentFile=%{_sysconfdir}/sysconfig/%{name}
ExecStart=%{_sbindir}/%{name} --foreground $DAEMON_OPTS
KillMode=process
#Hardening
PrivateTmp=true
CapabilityBoundingSet=CAP_SETGID CAP_SETUID CAP_NET_BIND_SERVICE CAP_NET_ADMIN
ProtectSystem=full
ProtectHome=true
PrivateDevices=true

[Install]
WantedBy=multi-user.target
EOF

cat > %{buildroot}%{_unitdir}/%{name}.socket << 'EOF'
[Unit]
Description=Socket support for sslh
Before=sslh.service

[Socket]
FreeBind=true

[Install]
WantedBy=sockets.target
EOF

# Install systemd template units
cat > %{buildroot}%{_unitdir}/%{name}@.service << 'EOF'
[Unit]
Description=SSL/SSH multiplexer for %I
After=network.target
Documentation=man:sslh(8)

[Service]
EnvironmentFile=%{_sysconfdir}/sysconfig/%{name}
ExecStart=%{_sbindir}/%{name} -F%{_sysconfdir}/%{name}/%I.cfg --foreground $DAEMON_OPTS
KillMode=process
#Hardening
PrivateTmp=true
CapabilityBoundingSet=CAP_SETGID CAP_SETUID CAP_NET_BIND_SERVICE CAP_NET_ADMIN
ProtectSystem=full
ProtectHome=true
PrivateDevices=true

[Install]
WantedBy=multi-user.target
EOF

cat > %{buildroot}%{_unitdir}/%{name}-select@.service << 'EOF'
[Unit]
Description=SSL/SSH multiplexer (select engine) for %I
After=network.target
Documentation=man:sslh(8)

[Service]
EnvironmentFile=%{_sysconfdir}/sysconfig/%{name}
ExecStart=%{_sbindir}/%{name}-select -F%{_sysconfdir}/%{name}/%I.cfg --foreground $DAEMON_OPTS
KillMode=process
#Hardening
PrivateTmp=true
CapabilityBoundingSet=CAP_SETGID CAP_SETUID CAP_NET_BIND_SERVICE CAP_NET_ADMIN
ProtectSystem=full
ProtectHome=true
PrivateDevices=true

[Install]
WantedBy=multi-user.target
EOF

cat > %{buildroot}%{_sysconfdir}/sysconfig/%{name} << 'EOF'
#
# The options passed to the sslh binary can be provided here
# Defaults to passing the configuration file to the daemon
#
DAEMON_OPTS="-F%{_sysconfdir}/%{name}/%{name}.cfg"
EOF

install -m0644 -D sslh.sysusers.conf %{buildroot}%{_sysusersdir}/sslh.conf

%check
%if %{with_tests}
# Use right ip6 localhost for Fedora
sed -i 's/ip6-localhost/localhost6/g' t
# Build the binaries with gcc coverage enabled
%make_build test
%endif

%post
%systemd_post sslh.service

%preun
%systemd_preun sslh.service

%postun
%systemd_postun_with_restart sslh.service

%files
%doc README.md ChangeLog example.cfg
%license COPYING
%{_mandir}/man8/%{name}.8*
%{_mandir}/man8/%{name}-select.8*
%{_mandir}/man8/%{name}-ev.8*
%{_sbindir}/%{name}
%{_sbindir}/%{name}-select
%{_sbindir}/%{name}-ev
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}-select@.service
%{_systemdgeneratordir}/systemd-sslh-generator
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.cfg
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_sysusersdir}/sslh.conf

%changelog
%autochangelog
