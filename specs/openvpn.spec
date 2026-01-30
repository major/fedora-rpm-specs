%define _hardened_build 1

# LTO needs to be disabled to avoid issues when linking the unit-test,
# which utilizes --wrap in the link process
%global _lto_cflags %{nil}


#
# Build conditionals
#

# Build with OpenVPN Data Channel Offload (kernel) support?
%bcond_without dco

# Build with PKCS#11/SmartCard support?
%bcond_without pkcs11

# tests_long - Enabled by default, enables long running tests in %%check
%bcond_without tests_long

Name:              openvpn
Version:           2.7_rc6
Release:           1%{?dist}
Summary:           A full-featured TLS VPN solution
URL:               https://community.openvpn.net/
Source0:           https://build.openvpn.net/downloads/releases/%{name}-%{version}.tar.gz
Source1:           https://build.openvpn.net/downloads/releases/%{name}-%{version}.tar.gz.asc
Source2:           roadwarrior-server.conf
Source3:           roadwarrior-client.conf
# Upstream signing key
Source10:          gpgkey-F554A3687412CFFEBDEFE0A312F5F7B42F2B01E7.gpg
Patch1:            fedora-crypto-policy-compliance.patch
Patch50:           openvpn-2.4-change-tmpfiles-permissions.patch
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
BuildRequires:     openssl-devel >= 1.1.0
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
Requires(post):    /usr/bin/awk

%if %{with dco}
Recommends:        kmod-ovpn
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
%{gpgverify} --keyring='%{SOURCE10}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n %{name}-%{version}

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
    %{?!with_dco:--disable-dco} \
    --docdir=%{_pkgdocdir} \
    SYSTEMD_UNIT_DIR=%{_unitdir} \
    TMPFILES_DIR=%{_tmpfilesdir}

%{__make} %{?_smp_mflags}



%check
# Test Crypto:
./src/openvpn/openvpn --genkey secret key
./src/openvpn/openvpn --cipher aes-128-cbc --test-crypto --secret key --allow-deprecated-insecure-static-crypto
./src/openvpn/openvpn --cipher aes-256-cbc --test-crypto --secret key --allow-deprecated-insecure-static-crypto
./src/openvpn/openvpn --cipher aes-128-gcm --test-crypto --secret key --allow-deprecated-insecure-static-crypto
./src/openvpn/openvpn --cipher aes-256-gcm --test-crypto --secret key --allow-deprecated-insecure-static-crypto

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
%{__make} install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' | xargs rm -f
mkdir -p -m 0750 %{buildroot}/%{_sysconfdir}/%{name}/client %{buildroot}/%{_sysconfdir}/%{name}/server
cp %{SOURCE2} %{SOURCE3} sample/sample-config-files/

# Create some directories the OpenVPN package should own
mkdir -m 0750 -p %{buildroot}%{_rundir}/%{name}-{client,server}
mkdir -m 0770 -p %{buildroot}%{_sharedstatedir}/%{name}

# Create a sysusers.d config file
echo "u openvpn - 'OpenVPN' /etc/openvpn -" > %{name}.sysusers.conf
install -m0644 -D %{name}.sysusers.conf %{buildroot}%{_sysusersdir}/%{name}.conf

# Package installs into %%{_pkgdocdir} directly
# Add various additional files
cp -a AUTHORS ChangeLog contrib sample distro/systemd/README.systemd %{buildroot}%{_pkgdocdir}

# Fix incorrect she-bang on a python script
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_interpreter_invocation
sed -e "s|^#!/usr/bin/env.*python3$|#!%{python3} -%{py3_shebang_flags}|" \
    -i %{buildroot}%{_pkgdocdir}/contrib/extract-crl/extractcrl.py

# Remove some files which does not really belong here
rm -f  %{buildroot}%{_pkgdocdir}/sample/Makefile{,.in,.am}
rm -f  %{buildroot}%{_pkgdocdir}/sample/sample-plugins/Makefile{,.in,.am}
rm -rf %{buildroot}%{_pkgdocdir}/sample/sample-keys
rm -f  %{buildroot}%{_pkgdocdir}/contrib/multilevel-init.patch
rm -rf %{buildroot}%{_pkgdocdir}/contrib/vcpkg-*
rm -rf %{buildroot}%{_pkgdocdir}/contrib/cmake*


%pre

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
%license COPYING COPYRIGHT.GPL
%{_pkgdocdir}/
%exclude %{_pkgdocdir}/{COPYING,COPYRIGHT.GPL}
%exclude %{_pkgdocdir}/README.mbedtls
%exclude %{_pkgdocdir}/sample/sample-plugins
%{_mandir}/man8/%{name}.8*
%{_mandir}/man5/%{name}-*.5*
%{_sbindir}/%{name}
%{_libdir}/%{name}/
%{_libexecdir}/%{name}/
%{_unitdir}/%{name}-client@.service
%{_unitdir}/%{name}-server@.service
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/%{name}.conf
%config %dir %{_sysconfdir}/%{name}/
%config %dir %attr(-,-,openvpn) %{_sysconfdir}/%{name}/client
%config %dir %attr(-,-,openvpn) %{_sysconfdir}/%{name}/server
%attr(0770,openvpn,openvpn) %{_sharedstatedir}/%{name}
%dir %attr(0750,-,openvpn) %{_rundir}/openvpn-client
%dir %attr(0750,-,openvpn) %{_rundir}/openvpn-server

%files devel
%{_pkgdocdir}/sample/sample-plugins
%exclude %{_pkgdocdir}/sample/sample-{config-files,scripts,windows}
%{_includedir}/openvpn-plugin.h
%{_includedir}/openvpn-msg.h


%changelog
* Wed Jan 28 2026 Frank Lichtenheld <frank@lichtenheld.com> - 2.7_rc6
- Update to upstream 2.7_rc6 release

* Fri Jan 16 2026 Frank Lichtenheld <frank@lichtenheld.com> - 2.7_rc5
- Update to upstream 2.7_rc5 release

* Mon Dec 22 2025 Frank Lichtenheld <frank@lichtenheld.com> - 2.7_rc4
- Update to upstream 2.7_rc4 release

* Fri Nov 28 2025 Frank Lichtenheld <frank@lichtenheld.com> - 2.7_rc3
- Update to upstream 2.7_rc3 release

* Tue Nov 18 2025 Frank Lichtenheld <frank@lichtenheld.com> - 2.7_rc2
- Update to upstream 2.7_rc2 release

* Tue Oct 14 2025 Frank Lichtenheld <frank@lichtenheld.com> - 2.7_beta3
- Update to upstream 2.7_beta3 release

* Mon Oct 6 2025 David Sommerseth <dazo@eurephia.org> - 2.7_beta2-2
- Add missing sysusers.d/openvpn.conf configuration file
- Switch to using %%{gpgverify} macro

* Thu Sep 25 2025 Frank Lichtenheld <frank@lichtenheld.com> - 2.7_beta2
- Update to upstream 2.7_beta2 release

* Tue Sep 9 2025 David Sommerseth <dazo@eurephia.org> - 2.7_beta1
- Update to upstream 2.7_beta1 release

* Fri Aug 1 2025 Frank Lichtenheld <frank@lichtenheld.com>  - 2.7_alpha3
- Update to upstream 2.7_alpha3 release

* Mon Jun 23 2025 Frank Lichtenheld <frank@lichtenheld.com>  - 2.7_alpha2
- Update to upstream 2.7_alpha2 release

* Fri May 30 2025 Frank Lichtenheld <frank@lichtenheld.com>  - 2.7_alpha1
- Update to upstream 2.7_alpha1 release

