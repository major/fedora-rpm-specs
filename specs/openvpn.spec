%define _hardened_build 1

# LTO needs to be disabled to avoid issues on Fedora 34+ and
# EL-9 when linking the unit-test, which utilizes --wrap in
# the link process
%if 0%{?rhel} > 8 || 0%{?fedora} > 34
%global _lto_cflags %{nil}
%endif

%bcond_without dco

# pkcs11-helper on RHEL9 (v1.27.0) comes with a buggy pkcs11.h, so skip it
%if 0%{?rhel} == 9
%bcond_with pkcs11
%else
%bcond_without pkcs11
%endif

# Build conditionals
# tests_long - Enabled by default, enables long running tests in %%check
%bcond_without tests_long

Name:              openvpn
Version:           2.6.13
Release:           1%{?dist}
Summary:           A full-featured TLS VPN solution
URL:               https://community.openvpn.net/
Source0:           https://build.openvpn.net/downloads/releases/%{name}-%{version}.tar.gz
Source1:           https://build.openvpn.net/downloads/releases/%{name}-%{version}.tar.gz.asc
Source2:           roadwarrior-server.conf
Source3:           roadwarrior-client.conf
# Upstream signing key
Source10:          gpgkey-F554A3687412CFFEBDEFE0A312F5F7B42F2B01E7.gpg
Source11:          openvpn.rpmlintrc
Patch1:            0001-Change-the-default-cipher-to-AES-256-GCM-for-server-.patch
Patch2:            fedora-crypto-policy-compliance.patch
Patch50:           openvpn-2.4-change-tmpfiles-permissions.patch
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:           GPL-2.0-only
BuildRequires:     gnupg2
BuildRequires:     gcc
BuildRequires:     automake
BuildRequires:     autoconf
BuildRequires:     autoconf-archive
BuildRequires:     libcap-ng-devel
BuildRequires:     libtool
BuildRequires:     gettext
BuildRequires:     lzo-devel
BuildRequires:     lz4-devel
BuildRequires:     make
BuildRequires:     openssl-devel
%if %{with dco}
BuildRequires:     libnl3-devel
%endif
%if %{with pkcs11}
BuildRequires:     pkcs11-helper-devel >= 1.11
%endif
BuildRequires:     pam-devel
BuildRequires:     libselinux-devel
BuildRequires:     libcmocka-devel
BuildRequires:     systemd
BuildRequires:     systemd-devel

%{?systemd_requires}
Requires(pre):     /usr/sbin/useradd

%if %{with dco}
Recommends:        kmod-ovpn-dco >= 0.2
%endif

BuildRequires:  python3-docutils

# For the perl_default_filter macro
BuildRequires:     perl-macros

# Filter out the perl(Authen::PAM) dependency.
# No perl dependency is really needed at all.
%{?perl_default_filter}

%description
OpenVPN is a robust and highly flexible tunneling application that uses all
of the encryption, authentication, and certification features of the
OpenSSL library to securely tunnel IP networks over a single UDP or TCP
port.  It can use the Marcus Franz Xaver Johannes Oberhumers LZO library
for compression.

%package devel
Summary:           Development headers and examples for OpenVPN plug-ins

%description devel
OpenVPN can be extended through the --plugin option, which provides
possibilities to add specialized authentication, user accounting,
packet filtering and related features.  These plug-ins need to be
written in C and provides a more low-level and information rich access
to similar features as the various script-hooks.

%prep
gpgv2 --quiet --keyring %{SOURCE10} %{SOURCE1} %{SOURCE0}
%setup -q -n %{name}-%{version}
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 50 -p1

# %%doc items shouldn't be executable.
find contrib sample -type f -perm /100 \
    -exec chmod a-x {} \;

%build
%configure \
    --enable-silent-rules \
    --with-crypto-library=openssl \
    %{?with_pkcs11:--enable-pkcs11} \
    --enable-selinux \
    --enable-systemd \
    --enable-x509-alt-username \
    --enable-async-push \
    %{?with_dco:--enable-dco} \
    --docdir=%{_pkgdocdir} \
    SYSTEMD_UNIT_DIR=%{_unitdir} \
    TMPFILES_DIR=%{_tmpfilesdir}

%{__make} %{?_smp_mflags}


%check
# Test Crypto:
./src/openvpn/openvpn --genkey --secret key
./src/openvpn/openvpn --cipher aes-128-cbc --test-crypto --secret key
./src/openvpn/openvpn --cipher aes-256-cbc --test-crypto --secret key
./src/openvpn/openvpn --cipher aes-128-gcm --test-crypto --secret key
./src/openvpn/openvpn --cipher aes-256-gcm --test-crypto --secret key

# Some of the unit tests does not run on RHEL-7
pushd tests/unit_tests
%{__make} %{?_smp_mflags} check
popd

%if %{with tests_long}
# Randomize ports for tests to avoid conflicts on the build servers.
cport=$[ 50000 + ($RANDOM % 15534) ]
sport=$[ $cport + 1 ]
sed -e 's/^\(rport\) .*$/\1 '$sport'/' \
    -e 's/^\(lport\) .*$/\1 '$cport'/' \
    < sample/sample-config-files/loopback-client \
    > %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u})-loopback-client
sed -e 's/^\(rport\) .*$/\1 '$cport'/' \
    -e 's/^\(lport\) .*$/\1 '$sport'/' \
    < sample/sample-config-files/loopback-server \
    > %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u})-loopback-server

pushd sample
# Test SSL/TLS negotiations (runs for 2 minutes):
../src/openvpn/openvpn --config \
    %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u})-loopback-client &
../src/openvpn/openvpn --config \
    %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u})-loopback-server
wait
popd

rm -f %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u})-loopback-client \
    %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u})-loopback-server
%endif

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' | xargs rm -f
mkdir -p -m 0750 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/client $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/server
cp %{SOURCE2} %{SOURCE3} sample/sample-config-files/

# Create some directories the OpenVPN package should own
mkdir -m 0750 -p $RPM_BUILD_ROOT%{_rundir}/%{name}-{client,server}
mkdir -m 0770 -p $RPM_BUILD_ROOT%{_sharedstatedir}/%{name}

# Package installs into %%{_pkgdocdir} directly
# Add various additional files
cp -a AUTHORS ChangeLog contrib sample distro/systemd/README.systemd $RPM_BUILD_ROOT%{_pkgdocdir}

# Fix incorrect she-bang on a python script
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_interpreter_invocation
sed -e "s|^#!/usr/bin/env.*python3$|#!%{python3} -%{py3_shebang_flags}|" \
    -i $RPM_BUILD_ROOT%{_pkgdocdir}/contrib/extract-crl/extractcrl.py

# Remove some files which does not really belong here
rm -f  $RPM_BUILD_ROOT%{_pkgdocdir}/sample/Makefile{,.in,.am}
rm -f  $RPM_BUILD_ROOT%{_pkgdocdir}/contrib/multilevel-init.patch
rm -rf $RPM_BUILD_ROOT%{_pkgdocdir}/sample/sample-keys


%pre
getent group openvpn &>/dev/null || groupadd -r openvpn
getent passwd openvpn &>/dev/null || \
    useradd -r -g openvpn -s /sbin/nologin -c OpenVPN \
        -d /etc/openvpn openvpn
exit 0

%post
for srv in `systemctl | awk '/openvpn-client@.*\.service/{print $1} /openvpn-server@.*\.service/{print $1}'`;
do
    %systemd_post $srv
done

%preun
for srv in `systemctl | awk '/openvpn-client@.*\.service/{print $1} /openvpn-server@.*\.service/{print $1}'`;
do
    %systemd_preun $srv
done

%postun
for srv in `systemctl | awk '/openvpn-client@.*\.service/{print $1} /openvpn-server@.*\.service/{print $1}'`;
do
    %systemd_postun_with_restart $srv
done

%files
%{_pkgdocdir}
%exclude %{_pkgdocdir}/README.mbedtls
%exclude %{_pkgdocdir}/sample/sample-plugins
%{_mandir}/man8/%{name}.8*
%{_mandir}/man5/%{name}-*.5*
%{_sbindir}/%{name}
%{_libdir}/%{name}/
%{_unitdir}/%{name}-client@.service
%{_unitdir}/%{name}-server@.service
%{_tmpfilesdir}/%{name}.conf
%config %dir %{_sysconfdir}/%{name}/
%config %dir %attr(-,-,openvpn) %{_sysconfdir}/%{name}/client
%config %dir %attr(-,-,openvpn) %{_sysconfdir}/%{name}/server
%attr(0770,openvpn,openvpn) %{_sharedstatedir}/%{name}
%dir %attr(0750,-,openvpn) %{_rundir}/openvpn-client
%dir %attr(0750,-,openvpn) %{_rundir}/openvpn-server

%files devel
%{_pkgdocdir}/sample/sample-plugins
%{_includedir}/openvpn-plugin.h
%{_includedir}/openvpn-msg.h


%changelog
* Thu Jan 16 2025 Frank Lichtenheld <frank@lichtenheld.com> - 2.6.13-1
- Update to upstream OpenVPN 2.6.13 (RHBZ#2338321)
- Remove RHEL 7 compat code

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6.12-2
- convert license to SPDX

* Thu Jul 18 2024 Frank Lichtenheld <frank@lichtenheld.com> - 2.6.12-1
- Update to upstream OpenVPN 2.6.12

* Fri Jul 12 2024 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.6.11-3
- Call useradd without full path

* Fri Jun 21 2024 Frank Lichtenheld <frank@lichtenheld.com> - 2.6.11-2
- Change /run directories from ghost to dir (RHBZ#2281686)

* Fri Jun 21 2024 Frank Lichtenheld <frank@lichtenheld.com> - 2.6.11-1
- Update to upstream OpenVPN 2.6.11
- Remove obsolete "beta release" qualifier from Summary

* Mon Feb 19 2024 David Sommerseth <davids@openvpn.net> - 2.6.9-1
- Update to upstream OpenVPN 2.6.9

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 20 2023 David Sommerseth <davids@openvpn.net> - 2.6.8-1
- Update to upstream OpenPVN 2.6.7
- Fixes a regression from 2.6.7 resulting in a SIGSEGV (GitHub#449)

* Thu Nov 9 2023 David Sommerseth <davids@openvpn.net> - 2.6.7-1
- Update to upstream OpenVPN 2.6.7
- Fixes CVE-2023-46849, CVE-2023-46850
- Fix false exit status on pre runtime scriptlet (Elkhan Mammadli <elkhan@almalinux.org>, RHBZ#2239722)
- Fix regression of systemctl scriptlet globbing issues (RHBZ#1887984); reintroduced in openvpn-2.6.0-1

* Mon Aug 21 2023 Frank Lichtenheld <frank@lichtenheld.com> - 2.6.6-1
- Update to upstream OpenVPN 2.6.6
- Fix "warning: %%patchN is deprecated"

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 David Sommerseth <davids@openvpn.net> - 2.6.5-1
- Update to upstream OpenVPN 2.6.5

* Fri Apr 21 2023 David Sommerseth <davids@openvpn.net> - 2.6.3-1
- Update to upstream OpenVPN 2.6.3
- Remove BF-CBC from the --data-ciphers list in openvpn-server@.service
- Add Recommends dependency to kmod-ovpn-dco (external Copr repo)

* Fri Mar 24 2023 David Sommerseth <davids@openvpn.net> -2.6.2-1
- Update to upstream OpenVPN 2.6.2

* Tue Mar 14 2023 David Sommerseth <davids@openvpn.net> -2.6.1-2
- Added patch to fix xkey related issues (rhbz#2177834)

* Mon Mar 13 2023 David Sommerseth <davids@openvpn.net> -2.6.1-1
- Update to upstream OpenVPN 2.6.1

* Thu Jan 26 2023 David Sommerseth <davids@openvpn.net> - 2.6.0-2
- Add missing fedora-crypto-policy-compliance.patch

* Thu Jan 26 2023 David Sommerseth <davids@openvpn.net> - 2.6.0-1
- Packaging of final openvpn-2.6.0 release

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 1 2022 David Sommerseth <davids@openvpn.net> - 2.5.8-1
- Update to upstream OpenVPN 2.5.8

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 David Sommerseth <davids@openvpn.net> - 2.5.7-2
- Added additional upstream patch resolving BF-CBC issues (to be removed with 2.5.8)
  https://patchwork.openvpn.net/patch/2504/
- Removed BF-CBC from the --data-ciphers list.  This is no longer available by default
  in OpenSSL 3.0

* Tue May 31 2022 David Sommerseth <davids@openvpn.net> - 2.5.7-1
- Update to upstream OpenVPN 2.5.7

* Wed Mar 16 2022 David Sommerseth <davids@openvpn.net> - 2.5.6-1
- Update to upstream OpenVPN 2.5.6
- Fixes CVE-2022-0547

* Thu Jan 27 2022 David Sommerseth <davids@openvpn.net> - 2.5.5-4
- Fix systemd related scriptlet error (#1887984)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
