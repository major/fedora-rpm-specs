Summary: A DMARC milter and library
Name: opendmarc
Version: 1.4.2
Release: %autorelease
License: BSD-3-Clause AND Sendmail-Open-Source-1.1
URL: http://www.trusteddomain.org/opendmarc.html
Source: https://github.com/trusteddomainproject/OpenDMARC/archive/refs/tags/rel-opendmarc-1-4-2.tar.gz

# Patch for ticket 159 and 179
# fixes opendmarc-importstats script up for mysql
Patch01:   opendmarc-1.4.0-ticket159-179.patch

# improve mysql and support strict mode
# Unfortunately, this patchset no longer applies and there's changes, so it needs rebasing
# by someone who knows the code well.
# Patch03:   %%{name}.ticket193.patch

# Patch for non security bug cve-2024-25768
# https://github.com/trusteddomainproject/OpenDMARC/issues/256
Patch02: cve-2024-25768.patch

# gcc15 includes stricter check for header detection
Patch: 0001-Fix-gcc15-stricter-check-for-headers.patch

# Required for all versions
Requires: lib%{name}%{?_isa} = %{version}-%{release}
Requires(pre): shadow-utils
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make
BuildRequires: libbsd
BuildRequires: libbsd-devel
BuildRequires: libspf2-devel
BuildRequires: libtool
BuildRequires: openssl-devel
BuildRequires: perl-generators
BuildRequires: pkgconfig
BuildRequires: systemd-rpm-macros
BuildRequires: mariadb-connector-c-devel
BuildRequires: sendmail-milter-devel
Suggests: %{name}-tools%{?_isa} = %{version}-%{release}

%description
OpenDMARC (Domain-based Message Authentication, Reporting & Conformance)
provides an open source library that implements the DMARC verification
service plus a milter-based filter application that can plug in to any
milter-aware MTA, including sendmail, Postfix, or any other MTA that supports
the milter protocol.

The DMARC sender authentication system is still a draft standard, working
towards RFC status.

The database schema required for some functions is provided in
%{_datadir}/%{name}/db. The rddmarc tools are provided in
%{_datadir}/%{name}/contrib/rddmarc.

%package -n opendmarc-tools
Summary: Tools for opendmarc
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n opendmarc-tools
This package contains the util binaries for opendmarc, including:

- opendmarc-expire
- opendmarc-import
- opendmarc-importstats
- opendmarc-params
- opendmarc-reports

%package -n libopendmarc
Summary: An open source DMARC library

%description -n libopendmarc
This package contains the library files required for running services built
using libopendmarc.

%package -n libopendmarc-devel
Summary: Development files for libopendmarc
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description -n lib%{name}-devel
This package contains the static libraries, headers, and other support files
required for developing applications against libopendmarc.

%prep
%autosetup -p1 -n OpenDMARC-rel-opendmarc-1-4-2

%build
autoreconf -v -i
%configure \
  --with-sql-backend \
  --with-spf \
  --with-spf2-include=%{_prefix}/include/spf2 \
  --with-spf2-lib=%{_libdir}/
%make_build CFLAGS="%{optflags} -std=gnu17"

%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p -m 0755 %{buildroot}%{_sysconfdir}/%{name}

cat > %{buildroot}%{_sysconfdir}/sysconfig/%{name} << 'EOF'
# Set the necessary startup options
OPTIONS="-c %{_sysconfdir}/%{name}.conf"
EOF

install -d -m 0755 %{buildroot}%{_unitdir}
cat > %{buildroot}%{_unitdir}/%{name}.service <<EOF
[Unit]
Description=Domain-based Message Authentication, Reporting & Conformance (DMARC) Milter
Documentation=man:%{name}(8) man:%{name}.conf(5) man:%{name}-import(8) man:%{name}-reports(8) http://www.trusteddomain.org/%{name}/
After=network.target nss-lookup.target syslog.target

[Service]
Type=simple
RuntimeDirectory=%{name}
RuntimeDirectoryMode=0750
EnvironmentFile=-/etc/sysconfig/%{name}
ExecStart=/usr/sbin/%{name} -f \$OPTIONS
ExecReload=/bin/kill -USR1 \$MAINPID
Restart=on-failure
User=%{name}
Group=%{name}

[Install]
WantedBy=multi-user.target
EOF

# Install and set some basic settings in the default config file
install -m 0644 %{name}/%{name}.conf.sample %{buildroot}%{_sysconfdir}/%{name}.conf

sed -i 's|^# AuthservID name |AuthservID HOSTNAME |' %{buildroot}%{_sysconfdir}/%{name}.conf
sed -i 's|^# HistoryFile /var/run/%{name}.dat|# HistoryFile %{_localstatedir}/spool/%{name}/%{name}.dat|' %{buildroot}%{_sysconfdir}/%{name}.conf
sed -i 's|^# Socket inet:8893@localhost|Socket local:%{_rundir}/%{name}/%{name}.sock|' %{buildroot}%{_sysconfdir}/%{name}.conf
sed -i 's|^# SoftwareHeader false|SoftwareHeader true|' %{buildroot}%{_sysconfdir}/%{name}.conf
sed -i 's|^# SPFIgnoreResults false|SPFIgnoreResults true|' %{buildroot}%{_sysconfdir}/%{name}.conf
sed -i 's|^# SPFSelfValidate false|SPFSelfValidate true|' %{buildroot}%{_sysconfdir}/%{name}.conf
sed -i 's|^# Syslog false|Syslog true|' %{buildroot}%{_sysconfdir}/%{name}.conf
sed -i 's|^# UMask 077|UMask 007|' %{buildroot}%{_sysconfdir}/%{name}.conf
sed -i 's|^# UserID %{name}|UserID %{name}:mail|' %{buildroot}%{_sysconfdir}/%{name}.conf
sed -i 's|/usr/local||' %{buildroot}%{_sysconfdir}/%{name}.conf

rm -rf %{buildroot}%{_prefix}/share/doc/%{name}
rm %{buildroot}%{_libdir}/*.{la,a}

mkdir -p %{buildroot}%{_includedir}/%{name}
install -m 0644 lib%{name}/dmarc.h %{buildroot}%{_includedir}/%{name}/

mkdir -p %{buildroot}%{_localstatedir}/spool/%{name}
mkdir -p %{buildroot}%{_rundir}/%{name}

# install db/ and contrib/ to datadir
mkdir -p %{buildroot}%{_datadir}/%{name}/contrib
cp -R db/ %{buildroot}%{_datadir}/%{name}
sed -i -e 's:/usr/local/bin/python:/usr/bin/python:' contrib/rddmarc/dmarcfail.py
cp -R contrib/rddmarc/ %{buildroot}%{_datadir}/%{name}/contrib
# not much point including the Makefiles
rm -f %{buildroot}%{_datadir}/%{name}/contrib/rddmarc/Makefile*
rm -f %{buildroot}%{_datadir}/%{name}/db/Makefile*

%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
	useradd -r -g %{name} -G mail -d %{_rundir}/%{name} -s /sbin/nologin \
	-c "OpenDMARC Milter" %{name}
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%ldconfig_scriptlets -n libopendmarc

%files
%license LICENSE LICENSE.Sendmail
%doc README RELEASE_NOTES
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_datadir}/%{name}
%{_sbindir}/opendmarc
%{_sbindir}/opendmarc-check
%{_mandir}/man5/opendmarc.conf.5*
%{_mandir}/man8/opendmarc.8*
%{_mandir}/man8/opendmarc-check.8*
%dir %attr(-,%{name},%{name}) %{_localstatedir}/spool/%{name}
%dir %attr(710,%{name},mail) %{_rundir}/%{name}
%dir %attr(-,%{name},%{name}) %{_sysconfdir}/%{name}
%attr(0644,root,root) %{_unitdir}/%{name}.service

%files -n opendmarc-tools
%{_sbindir}/opendmarc-expire
%{_sbindir}/opendmarc-import
%{_sbindir}/opendmarc-importstats
%{_sbindir}/opendmarc-params
%{_sbindir}/opendmarc-reports
%{_mandir}/man8/opendmarc-expire.8*
%{_mandir}/man8/opendmarc-import.8*
%{_mandir}/man8/opendmarc-importstats.8*
%{_mandir}/man8/opendmarc-params.8*
%{_mandir}/man8/opendmarc-reports.8*

%files -n libopendmarc
%{_libdir}/lib%{name}.so.*

%files -n libopendmarc-devel
%doc lib%{name}/docs/*.html
%{_includedir}/%{name}
%{_libdir}/*.so

%changelog
%autochangelog
