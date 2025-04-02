# SystemTap support is disabled by default
%{!?sdt:%global sdt 0}

%if 0%{?rhel} >= 10
%bcond_with dhclient
%bcond_with dhcpd
%else
%bcond_without dhclient
%bcond_without dhcpd
%endif

# Where dhcp configuration files are stored
%global dhcpconfdir %{_sysconfdir}/dhcp

#global prever b1
%global patchver P1
%global DHCPVERSION %{version}%{?prever}%{?patchver:-%{patchver}}
# Bundled bind version
%global BINDVERSION 9.11.36

%global dhcp_EOL_text DHCP is no longer maintained by ISC. This package is provided on\
best effort basis to cover functionality that is not provided by Kea\
and should not be used on production systems.

Summary:  Dynamic host configuration protocol software
Name:     dhcp
Version:  4.4.3
Release:  %autorelease

# We want to get rid of DHCP in favour of Kea package, because ISC has announced
# the end of maintenance for ISC DHCP as of the end of 2022. No package depends
# on dhcp-server, but dhcp-client is still being used, so we keep it around as
# deprecated package. There is ongoing effort to replace it with other options:
# https://fedoraproject.org/wiki/Changes/dhclient_deprecation
Provides:  deprecated()

# NEVER CHANGE THE EPOCH on this package.  The previous maintainer (prior to
# dcantrell maintaining the package) made incorrect use of the epoch and
# that's why it is at 12 now.  It should have never been used, but it was.
# So we are stuck with it.
Epoch:    12
License:  ISC AND MPL-2.0
Url:      https://www.isc.org/dhcp/
Source0:  https://downloads.isc.org/isc/dhcp/%{DHCPVERSION}/dhcp-%{DHCPVERSION}.tar.gz
Source9:  https://downloads.isc.org/isc/dhcp/%{DHCPVERSION}/dhcp-%{DHCPVERSION}.tar.gz.asc
Source10: codesign2021.txt
Source1:  dhclient-script
Source2:  README.dhclient.d
Source3:  11-dhclient
Source5:  56dhclient
Source6:  dhcpd.service
Source7:  dhcpd6.service
Source8:  dhcrelay.service
Source11: dhcp.sysusers

Patch1: 0001-change-bug-url.patch
Patch2: 0002-additional-dhclient-options.patch
Patch3: 0003-Handle-releasing-interfaces-requested-by-sbin-ifup.patch
Patch4: 0004-Support-unicast-BOOTP-for-IBM-pSeries-systems-and-ma.patch
Patch5: 0005-Change-default-requested-options.patch
Patch6: 0006-Various-man-page-only-fixes.patch
Patch7: 0007-Change-paths-to-conform-to-our-standards.patch
Patch8: 0008-Make-sure-all-open-file-descriptors-are-closed-on-ex.patch
Patch9: 0009-Fix-garbage-in-format-string-error.patch
Patch10: 0010-Handle-null-timeout.patch
Patch11: 0011-Drop-unnecessary-capabilities.patch
Patch12: 0012-RFC-3442-Classless-Static-Route-Option-for-DHCPv4-51.patch
Patch13: 0013-DHCPv6-over-PPP-support-626514.patch
Patch14: 0014-IPoIB-support-660681.patch
Patch15: 0015-Add-GUID-DUID-to-dhcpd-logs-1064416.patch
Patch16: 0016-Turn-on-creating-sending-of-DUID.patch
Patch17: 0017-Send-unicast-request-release-via-correct-interface.patch
Patch18: 0018-No-subnet-declaration-for-iface-should-be-info-not-e.patch
Patch19: 0019-dhclient-write-DUID_LLT-even-in-stateless-mode-11563.patch
Patch20: 0020-Discover-all-hwaddress-for-xid-uniqueness.patch
Patch21: 0021-Load-leases-DB-in-non-replay-mode-only.patch
Patch22: 0022-dhclient-make-sure-link-local-address-is-ready-in-st.patch
Patch23: 0023-option-97-pxe-client-id.patch
Patch24: 0024-Detect-system-time-changes.patch
Patch25: 0025-bind-Detect-system-time-changes.patch
Patch26: 0026-Add-dhclient-5-B-option-description.patch
Patch27: 0027-Add-missed-sd-notify-patch-to-manage-dhcpd-with-syst.patch
Patch28: 0028-Use-system-getaddrinfo-for-dhcp.patch
Patch29: CVE-2021-25220.patch
Patch30: 0030-bind-configure-c99.patch
Patch31: 0031-Correct-declarations-of-ia_na_-no-match-and-ia_pd_-n.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make
BuildRequires: libtool
BuildRequires: openldap-devel
# --with-ldap-gssapi
BuildRequires: krb5-devel
BuildRequires: libcap-ng-devel
# https://fedorahosted.org/fpc/ticket/502#comment:3
BuildRequires: systemd systemd-devel
# dhcp-sd_notify.patch
BuildRequires: pkgconfig(libsystemd)
BuildRequires: gnupg2
%if ! 0%{?_module_build}
BuildRequires: doxygen
%endif
%if %{sdt}
BuildRequires: systemtap-sdt-devel
%global tapsetdir    /usr/share/systemtap/tapset
%endif
BuildRequires: systemd-rpm-macros

# In _docdir we ship some perl scripts and module from contrib subdirectory.
# Because nothing under _docdir is allowed to "require" anything,
# prevent _docdir from being scanned. (#674058)
%global __requires_exclude_from ^%{_docdir}/.*$

%description
DHCP (Dynamic Host Configuration Protocol)

%{dhcp_EOL_text}

%if %{with dhcpd}
%package server
Summary: Provides the ISC DHCP server
Requires: %{name}-common = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-compat < 12:4.4.2-12.b1
Requires(post): coreutils grep sed
%{?sysusers_requires_compat}
%{?systemd_requires}
Provides: deprecated()

%description server
DHCP (Dynamic Host Configuration Protocol) is a protocol which allows
individual devices on an IP network to get their own network
configuration information (IP address, subnetmask, broadcast address,
etc.) from a DHCP server. The overall purpose of DHCP is to make it
easier to administer a large network.

This package provides the ISC DHCP server.

%{dhcp_EOL_text}
%endif

%package relay
Summary: Provides the ISC DHCP relay agent
Requires: %{name}-common = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-compat < 12:4.4.2-12.b1
Requires(post): grep sed
%{?systemd_requires}
Provides: deprecated()

%description relay
DHCP (Dynamic Host Configuration Protocol) is a protocol which allows
individual devices on an IP network to get their own network
configuration information (IP address, subnetmask, broadcast address,
etc.) from a DHCP server. The overall purpose of DHCP is to make it
easier to administer a large network.

This package provides the ISC DHCP relay agent.

%{dhcp_EOL_text}

%if %{with dhclient}
%package client
Summary: Provides the ISC DHCP client daemon and dhclient-script
Provides: dhclient = %{epoch}:%{version}-%{release}
Obsoletes: dhclient < %{epoch}:%{version}-%{release}
# dhclient-script requires:
Requires: coreutils gawk grep ipcalc iproute iputils sed systemd
Requires: %{name}-common = %{epoch}:%{version}-%{release}
# Old NetworkManager expects the dispatcher scripts in a different place
Conflicts: NetworkManager < 1.20
Provides: deprecated()

%description client
DHCP (Dynamic Host Configuration Protocol) is a protocol which allows
individual devices on an IP network to get their own network
configuration information (IP address, subnetmask, broadcast address,
etc.) from a DHCP server. The overall purpose of DHCP is to make it
easier to administer a large network.

This package provides the ISC DHCP client.

%{dhcp_EOL_text}
%endif

%package common
Summary: Common files used by ISC dhcp client, server and relay agent
BuildArch: noarch
Obsoletes: dhcp-libs < %{epoch}:%{version}
Provides: deprecated()

%description common
DHCP (Dynamic Host Configuration Protocol) is a protocol which allows
individual devices on an IP network to get their own network
configuration information (IP address, subnetmask, broadcast address,
etc.) from a DHCP server. The overall purpose of DHCP is to make it
easier to administer a large network.

This package provides common files used by dhcp and dhclient package.

%{dhcp_EOL_text}

%package libs-static
Summary: Shared libraries used by ISC dhcp client and server
Provides: %{name}-libs%{?_isa} =  %{epoch}:%{version}-%{release}
Provides: %{name}-libs =  %{epoch}:%{version}-%{release}
Provides: bundled(bind-export-libs) = %{BINDVERSION}
Provides: bundled(bind) = %{BINDVERSION}
Provides: deprecated()

%description libs-static
This package contains shared libraries used by ISC dhcp client and server

%{dhcp_EOL_text}

%package devel
Summary: Development headers and libraries for interfacing to the DHCP server
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Provides: deprecated()

%description devel
Header files and API documentation for using the ISC DHCP libraries.  The
libdhcpctl and libomapi static libraries are also included in this package.

%{dhcp_EOL_text}

%if ! 0%{?_module_build}
%package devel-doc
Summary: Developer's Guide for ISC DHCP
Requires: %{name}-libs = %{epoch}:%{version}-%{release}
BuildArch: noarch
Provides: deprecated()

%description devel-doc
This documentation is intended for developers, contributors and other
programmers that are interested in internal operation of the code.
This package contains doxygen-generated documentation.
%endif

%{dhcp_EOL_text}

%prep
%if 0%{?fedora}
%{gpgverify} --keyring='%{SOURCE10}' --signature='%{SOURCE9}' --data='%{SOURCE0}'
%endif
%setup -n dhcp-%{DHCPVERSION}
pushd bind
tar -xf bind.tar.gz
# Ensure we have correct bundled bind version specified.
ls -1 bind-%{BINDVERSION}
ln -s bind-%{BINDVERSION} bind
popd
%autopatch -p1 

# Update paths in all man pages
for page in client/dhclient.conf.5 client/dhclient.leases.5 \
            client/dhclient-script.8 client/dhclient.8 ; do
    sed -i -e 's|CLIENTBINDIR|%{_sbindir}|g' \
                -e 's|RUNDIR|%{_localstatedir}/run|g' \
                -e 's|DBDIR|%{_localstatedir}/lib/dhclient|g' \
                -e 's|ETCDIR|%{dhcpconfdir}|g' $page
done

for page in server/dhcpd.conf.5 server/dhcpd.leases.5 server/dhcpd.8 ; do
    sed -i -e 's|CLIENTBINDIR|%{_sbindir}|g' \
                -e 's|RUNDIR|%{_localstatedir}/run|g' \
                -e 's|DBDIR|%{_localstatedir}/lib/dhcpd|g' \
                -e 's|ETCDIR|%{dhcpconfdir}|g' $page
done

sed -i -e 's|/var/db/|%{_localstatedir}/lib/dhcpd/|g' contrib/dhcp-lease-list.pl

## FIXME drop unused bind components 

%build
#libtoolize --copy --force
autoreconf --verbose --force --install

CFLAGS="%{optflags} -fno-strict-aliasing -fcommon" \
%configure \
    --with-srv-lease-file=%{_localstatedir}/lib/dhcpd/dhcpd.leases \
    --with-srv6-lease-file=%{_localstatedir}/lib/dhcpd/dhcpd6.leases \
    --with-cli-lease-file=%{_localstatedir}/lib/dhclient/dhclient.leases \
    --with-cli6-lease-file=%{_localstatedir}/lib/dhclient/dhclient6.leases \
    --with-srv-pid-file=%{_localstatedir}/run/dhcpd.pid \
    --with-srv6-pid-file=%{_localstatedir}/run/dhcpd6.pid \
    --with-cli-pid-file=%{_localstatedir}/run/dhclient.pid \
    --with-cli6-pid-file=%{_localstatedir}/run/dhclient6.pid \
    --with-relay-pid-file=%{_localstatedir}/run/dhcrelay.pid \
    --with-ldap \
    --with-ldapcrypto \
    --with-ldap-gssapi \
    --enable-log-pid \
%if %{sdt}
    --enable-systemtap \
    --with-tapset-install-dir=%{tapsetdir} \
%endif
    --enable-paranoia --enable-early-chroot \
    --enable-binary-leases \
    --with-systemd
%make_build

%if ! 0%{?_module_build}
pushd doc
make %{?_smp_mflags} devel
popd
%endif

%install
%make_install

# We don't want example conf files in /etc
rm -f %{buildroot}%{_sysconfdir}/dhclient.conf.example
rm -f %{buildroot}%{_sysconfdir}/dhcpd.conf.example

%if %{with dhclient}
# dhclient-script
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_sbindir}/dhclient-script

# README.dhclient.d
install -p -m 0644 %{SOURCE2} .

# Empty directory for dhclient.d scripts
mkdir -p %{buildroot}%{dhcpconfdir}/dhclient.d

# NetworkManager dispatcher script
mkdir -p %{buildroot}%{_prefix}/lib/NetworkManager/dispatcher.d
install -p -m 0755 %{SOURCE3} %{buildroot}%{_prefix}/lib/NetworkManager/dispatcher.d

# pm-utils script to handle suspend/resume and dhclient leases
install -D -p -m 0755 %{SOURCE5} %{buildroot}%{_libdir}/pm-utils/sleep.d/56dhclient
%endif

# systemd unit files
mkdir -p %{buildroot}%{_unitdir}
%if %{with dhcpd}
install -m 644 %{SOURCE6} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE7} %{buildroot}%{_unitdir}
%endif
install -m 644 %{SOURCE8} %{buildroot}%{_unitdir}

# systemd-sysusers
install -p -D -m 0644 %{SOURCE11} %{buildroot}%{_sysusersdir}/dhcp.conf

%if %{with dhcpd}
# Start empty lease databases
mkdir -p %{buildroot}%{_localstatedir}/lib/dhcpd/
touch %{buildroot}%{_localstatedir}/lib/dhcpd/dhcpd.leases
touch %{buildroot}%{_localstatedir}/lib/dhcpd/dhcpd6.leases
%endif
%if %{with dhclient}
mkdir -p %{buildroot}%{_localstatedir}/lib/dhclient/
%endif

%if %{with dhcpd}
# default sysconfig file for dhcpd
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
cat <<EOF > %{buildroot}%{_sysconfdir}/sysconfig/dhcpd
# WARNING: This file is NOT used anymore.

# If you are here to restrict what interfaces should dhcpd listen on,
# be aware that dhcpd listens *only* on interfaces for which it finds subnet
# declaration in dhcpd.conf. It means that explicitly enumerating interfaces
# also on command line should not be required in most cases.

# If you still insist on adding some command line options,
# copy dhcpd.service from /lib/systemd/system to /etc/systemd/system and modify
# it there.
# https://fedoraproject.org/wiki/Systemd#How_do_I_customize_a_unit_file.2F_add_a_custom_unit_file.3F

# example:
# $ cp /usr/lib/systemd/system/dhcpd.service /etc/systemd/system/
# $ vi /etc/systemd/system/dhcpd.service
# $ ExecStart=/usr/sbin/dhcpd -f -cf /etc/dhcp/dhcpd.conf -user dhcpd -group dhcpd --no-pid <your_interface_name(s)>
# $ systemctl --system daemon-reload
# $ systemctl restart dhcpd.service
EOF
%endif

%if %{with dhcpd}
# Copy sample conf files into position (called by doc macro)
cp -p doc/examples/dhclient-dhcpv6.conf client/dhclient6.conf.example
cp -p doc/examples/dhcpd-dhcpv6.conf server/dhcpd6.conf.example
%endif

%if %{with dhclient}
cat << EOF > client/dhclient-enter-hooks
#!/bin/bash

# For dhclient/dhclient-script debugging.
# Copy this into /etc/dhcp/ and make it executable.
# Run 'dhclient -d <interface>' to see info passed from dhclient to dhclient-script.
# See also HOOKS section in dhclient-script(8) man page.

echo "interface: ${interface}"
echo "reason: ${reason}"

( set -o posix ; set ) | grep "old_"
( set -o posix ; set ) | grep "new_"
( set -o posix ; set ) | grep "alias_"
( set -o posix ; set ) | grep "requested_"
EOF
%endif

%if %{with dhcpd}
# Install default (empty) dhcpd.conf:
mkdir -p %{buildroot}%{dhcpconfdir}
cat << EOF > %{buildroot}%{dhcpconfdir}/dhcpd.conf
#
# DHCP Server Configuration file.
#   see /usr/share/doc/dhcp-server/dhcpd.conf.example
#   see dhcpd.conf(5) man page
#
EOF

# Install default (empty) dhcpd6.conf:
cat << EOF > %{buildroot}%{dhcpconfdir}/dhcpd6.conf
#
# DHCPv6 Server Configuration file.
#   see /usr/share/doc/dhcp-server/dhcpd6.conf.example
#   see dhcpd.conf(5) man page
#
EOF

# Install dhcp.schema for LDAP configuration
install -D -p -m 0644 contrib/ldap/dhcp.schema %{buildroot}%{_sysconfdir}/openldap/schema/dhcp.schema
%endif

# Don't package libtool *.la files
find %{buildroot} -type f -name "*.la" -delete -print

%if %{without dhcpd}
rm -frv \
    %{buildroot}%{_sysusersdir}/dhcp.conf \
    %{buildroot}%{_sbindir}/dhcpd \
    %{buildroot}%{_bindir}/omshell \
    %{buildroot}%{_mandir}/man1/omshell.1 \
    %{buildroot}%{_mandir}/man3/dhcpctl.3 \
    %{buildroot}%{_mandir}/man3/omapi.3 \
    %{buildroot}%{_mandir}/man5/dhcpd.conf.5 \
    %{buildroot}%{_mandir}/man5/dhcpd.leases.5 \
    %{buildroot}%{_mandir}/man8/dhcpd.8 \
    %{buildroot}%{_includedir} \
    %{buildroot}/usr/lib64/libdhcp.a \
    %{buildroot}/usr/lib64/libdhcpctl.a \
    %{buildroot}/usr/lib64/libomapi.a \
    %{buildroot}/usr/lib/debug/usr/bin/omshell-*.debug \
    %{buildroot}/usr/lib/debug/usr/sbin/dhcpd-*.debug
%endif

%if %{without dhclient}
rm -fv \
    %{buildroot}%{_sbindir}/dhclient \
    %{buildroot}%{_mandir}/man5/dhclient.conf.5 \
    %{buildroot}%{_mandir}/man5/dhclient.leases.5 \
    %{buildroot}%{_mandir}/man8/dhclient-script.8 \
    %{buildroot}%{_mandir}/man8/dhclient.8 \
    %{buildroot}/usr/lib/debug/usr/sbin/dhclient-*.debug
%endif

%if %{with dhcpd}
%pre server
%sysusers_create_compat %{SOURCE11}

%post server
# Initial installation
%systemd_post dhcpd.service dhcpd6.service


for servicename in dhcpd dhcpd6; do
  etcservicefile=%{_sysconfdir}/systemd/system/${servicename}.service
  if [ -f ${etcservicefile} ]; then
    grep -q Type= ${etcservicefile} || sed -i '/\[Service\]/a Type=notify' ${etcservicefile}
    sed -i 's/After=network.target/Wants=network-online.target\nAfter=network-online.target/' ${etcservicefile}
  fi
done
exit 0
%endif

%post relay
# Initial installation
%systemd_post dhcrelay.service

for servicename in dhcrelay; do
  etcservicefile=%{_sysconfdir}/systemd/system/${servicename}.service
  if [ -f ${etcservicefile} ]; then
    grep -q Type= ${etcservicefile} || sed -i '/\[Service\]/a Type=notify' ${etcservicefile}
    sed -i 's/After=network.target/Wants=network-online.target\nAfter=network-online.target/' ${etcservicefile}
  fi
done
exit 0

%if %{with dhcpd}
%preun server
# Package removal, not upgrade
%systemd_preun dhcpd.service dhcpd6.service
%endif

%preun relay
# Package removal, not upgrade
%systemd_preun dhcrelay.service


%if %{with dhcpd}
%postun server
# Package upgrade, not uninstall
%systemd_postun_with_restart dhcpd.service dhcpd6.service
%endif

%postun relay
# Package upgrade, not uninstall
%systemd_postun_with_restart dhcrelay.service


%triggerun -- dhcp
# convert DHC*ARGS from /etc/sysconfig/dhc* to /etc/systemd/system/dhc*.service
%if %{with dhcpd}
SERVICE_NAMES="dhcpd dhcpd6 dhcrelay"
%else
SERVICE_NAMES="dhcrelay"
%endif
for servicename in ${SERVICE_NAMES}; do
  if [ -f %{_sysconfdir}/sysconfig/${servicename} ]; then
    # get DHCPDARGS/DHCRELAYARGS value from /etc/sysconfig/${servicename}
    source %{_sysconfdir}/sysconfig/${servicename}
    if [ "${servicename}" == "dhcrelay" ]; then
        args=$DHCRELAYARGS
    else
        args=$DHCPDARGS
    fi
    # value is non-empty (i.e. user modified) and there isn't a service unit yet
    if [ -n "${args}" -a ! -f %{_sysconfdir}/systemd/system/${servicename}.service ]; then
      # in $args replace / with \/ otherwise the next sed won't take it
      args=$(echo $args | sed 's/\//\\\//'g)
      # add $args to the end of ExecStart line
      sed -r -e "/ExecStart=/ s/$/ ${args}/" \
                < %{_unitdir}/${servicename}.service \
                > %{_sysconfdir}/systemd/system/${servicename}.service
    fi
  fi
done

%if %{with dhcpd}
%files server
%doc server/dhcpd.conf.example server/dhcpd6.conf.example
%doc contrib/ldap/ contrib/dhcp-lease-list.pl
%attr(0750,root,root) %dir %{dhcpconfdir}
%attr(0755,dhcpd,dhcpd) %dir %{_localstatedir}/lib/dhcpd
%attr(0644,dhcpd,dhcpd) %verify(mode) %config(noreplace) %{_localstatedir}/lib/dhcpd/dhcpd.leases
%attr(0644,dhcpd,dhcpd) %verify(mode) %config(noreplace) %{_localstatedir}/lib/dhcpd/dhcpd6.leases
%config(noreplace) %{_sysconfdir}/sysconfig/dhcpd
%config(noreplace) %{dhcpconfdir}/dhcpd.conf
%config(noreplace) %{dhcpconfdir}/dhcpd6.conf
%dir %{_sysconfdir}/openldap/schema
%config(noreplace) %{_sysconfdir}/openldap/schema/dhcp.schema
%attr(0644,root,root)   %{_unitdir}/dhcpd.service
%attr(0644,root,root)   %{_unitdir}/dhcpd6.service
%{_sysusersdir}/dhcp.conf
%{_sbindir}/dhcpd
%{_bindir}/omshell
%attr(0644,root,root) %{_mandir}/man1/omshell.1.gz
%attr(0644,root,root) %{_mandir}/man5/dhcpd.conf.5.gz
%attr(0644,root,root) %{_mandir}/man5/dhcpd.leases.5.gz
%attr(0644,root,root) %{_mandir}/man8/dhcpd.8.gz
%if %{sdt}
%{tapsetdir}/*.stp
%endif
%endif

%files relay
%{_sbindir}/dhcrelay
%attr(0644,root,root) %{_unitdir}/dhcrelay.service
%attr(0644,root,root) %{_mandir}/man8/dhcrelay.8.gz

%if %{with dhclient}
%files client
%doc README.dhclient.d
%doc client/dhclient.conf.example client/dhclient6.conf.example client/dhclient-enter-hooks
%attr(0750,root,root) %dir %{dhcpconfdir}
%dir %{dhcpconfdir}/dhclient.d
%dir %{_localstatedir}/lib/dhclient
%dir %{_prefix}/lib/NetworkManager
%dir %{_prefix}/lib/NetworkManager/dispatcher.d
%{_prefix}/lib/NetworkManager/dispatcher.d/11-dhclient
%{_sbindir}/dhclient
%{_sbindir}/dhclient-script
%attr(0755,root,root) %{_libdir}/pm-utils/sleep.d/56dhclient
%attr(0644,root,root) %{_mandir}/man5/dhclient.conf.5.gz
%attr(0644,root,root) %{_mandir}/man5/dhclient.leases.5.gz
%attr(0644,root,root) %{_mandir}/man8/dhclient.8.gz
%attr(0644,root,root) %{_mandir}/man8/dhclient-script.8.gz
%endif

%files common
%{!?_licensedir:%global license %%doc}
%{license} LICENSE
%doc README RELNOTES doc/References.txt
%attr(0644,root,root) %{_mandir}/man5/dhcp-options.5.gz
%attr(0644,root,root) %{_mandir}/man5/dhcp-eval.5.gz

%if %{with dhcpd}
%files libs-static
%{_libdir}/libdhcp*.a
%{_libdir}/libomapi.a

%files devel
%doc doc/IANA-arp-parameters doc/api+protocol
%{_includedir}/dhcpctl
%{_includedir}/omapip
%attr(0644,root,root) %{_mandir}/man3/dhcpctl.3.gz
%attr(0644,root,root) %{_mandir}/man3/omapi.3.gz

%if ! 0%{?_module_build}
%files devel-doc
%doc doc/html/
%endif
%endif

%changelog
%autochangelog
