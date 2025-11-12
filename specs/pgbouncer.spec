# Tests fail on i686:
%ifarch %{ix86}
%bcond tests 0
%else
%bcond tests 0
%endif

Name:		pgbouncer
Version:	1.25.0
Release:	%autorelease
Summary:	Lightweight connection pooler for PostgreSQL
License:	ISC and BSD-2-Clause
URL:		https://www.pgbouncer.org

Source0:	%{url}/downloads/files/%{version}/%{name}-%{version}.tar.gz
Source3:	%{name}.logrotate
Source4:	%{name}.service
Source6:	%{name}.pam

Patch0:		%{name}-ini.patch

BuildRequires:	c-ares-devel >= 1.11
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	pandoc
BuildRequires:	pkgconfig(libevent)
# For Fedora and EL9+ systemd-rpm-macros would be enough:
BuildRequires:	systemd-devel


%if %{with tests}
# Test dependencies:
BuildRequires:  openssl
BuildRequires:  postgresql-contrib
BuildRequires:  postgresql-server
BuildRequires:  python3dist(filelock)
BuildRequires:  python3dist(psycopg)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(pytest-xdist)
%endif

Requires:	systemd
Requires:	logrotate
Requires:	python3-psycopg2
Requires:	c-ares >= 1.11

%description
pgbouncer is a lightweight connection pooler for PostgreSQL and uses libevent
for low-level socket handling.

%prep
%autosetup -p0

sed -i -e 's|/usr/bin/env python.*|%__python3|g' etc/mkauth.py

# Create a sysusers.d config file
cat >pgbouncer.sysusers.conf <<EOF
u pgbouncer - 'PgBouncer Server' - -
EOF

%build
# Building with systemd flag tries to enable notify support:
%configure \
	--enable-debug \
	--with-cares \
	--with-ldap \
	--with-pam \
	--with-systemd

%make_build V=1

%install
%make_install

# Configuration
install -p -d %{buildroot}%{_sysconfdir}/%{name}/
install -p -m 640 etc/%{name}.ini %{buildroot}%{_sysconfdir}/%{name}
install -p -m 600 etc/userlist.txt %{buildroot}%{_sysconfdir}/%{name}
install -p -m 700 etc/mkauth.py %{buildroot}%{_sysconfdir}/%{name}/

# Install pam configuration file
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
install -p -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/pam.d/%{name}

# Temporary folder
mkdir -p %{buildroot}%{_rundir}/%{name}

# Log folder
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}

# systemd unit
install -d %{buildroot}%{_unitdir}
install -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}.service

# tmpfiles.d configuration
mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/%{name}.conf <<EOF
d %{_rundir}/%{name} 0755 %{name} %{name} -
EOF

# logrotate file
install -p -d %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Let RPM pick up docs in the files section
rm -fr %{buildroot}%{_docdir}/%{name}

install -m0644 -D pgbouncer.sysusers.conf %{buildroot}%{_sysusersdir}/pgbouncer.conf

%if %{with tests}
%check
# Parallel tests fail (make check), run them sequentially:
pytest
%endif

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYRIGHT
%doc NEWS.md README.md doc/*.md
%{_bindir}/%{name}
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/mkauth.py*
%config(noreplace) %attr(600,%{name},%{name}) %{_sysconfdir}/%{name}/%{name}.ini
%config(noreplace) %attr(600,%{name},%{name}) %{_sysconfdir}/%{name}/userlist.txt
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%{_mandir}/man1/%{name}.*
%{_mandir}/man5/%{name}.*
%attr(700,%{name},%{name}) %{_localstatedir}/log/%{name}

%attr(755,%{name},%{name}) %dir %{_rundir}/%{name}
%ghost %{_rundir}/%{name}/%{name}.pid
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service
%{_sysusersdir}/pgbouncer.conf

%changelog
%autochangelog
