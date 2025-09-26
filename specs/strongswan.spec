%global _hardened_build 1
#%%define prerelease dr1

# pytho vici bindings cannot build without network, so temp. disabled
%bcond_with python3
%bcond_without perl
# checks fail for test_params_parse_rsa_pss
%bcond_with    check

%global forgeurl0 https://github.com/strongswan/strongswan

Name:           strongswan
Version:        6.0.2
Release:        %autorelease
Summary:        An OpenSource IPsec-based VPN and TNC solution
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.strongswan.org/
VCS:            git:%{forgeurl0}
Source0:        https://download.strongswan.org/strongswan-%{version}%{?prerelease}.tar.bz2
Source1:        https://download.strongswan.org/strongswan-%{version}%{?prerelease}.tar.bz2.sig
Source2:        https://download.strongswan.org/STRONGSWAN-RELEASE-PGP-KEY
Source3:        tmpfiles-strongswan.conf
# https://github.com/strongswan/strongswan/issues/1198  (also pinged upstream via email)
Patch1:         strongswan-5.9.7-error-no-format.patch
# Use isolation to prevent pip attempting to download during build
Patch2:         strongswan-6.0.2-no-isolation.patch
# Remove MD2, which causes test case failures due to fedora crypto policies
# https://github.com/strongswan/strongswan/commit/b3011e8e87a1fad1bfb026448fc37b80b7cfc007
Patch3:         strongswan-6.0.2-no-md5-b3011e8e.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  gmp-devel
BuildRequires:  libcurl-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
%if 0%{?fedora} >= 41
# https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine
BuildRequires:  openssl-devel-engine
%endif
BuildRequires:  sqlite-devel
BuildRequires:  gettext-devel
BuildRequires:  libxml2-devel
BuildRequires:  pam-devel
BuildRequires:  json-c-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  iptables-devel
BuildRequires:  libcap-devel
BuildRequires:  tpm2-tss-devel
Recommends:     tpm2-tools

%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-setuptools
BuildRequires:  python3-daemon
BuildRequires:  python3-pytest
%endif

%if %{with perl}
BuildRequires:  perl-devel perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
%endif

BuildRequires:  NetworkManager-libnm-devel
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
The strongSwan IPsec implementation supports both the IKEv1 and IKEv2 key
exchange protocols in conjunction with the native NETKEY IPsec stack of the
Linux kernel.

%package libipsec
Summary: Strongswan's libipsec backend
%description libipsec
The kernel-libipsec plugin provides an IPsec backend that works entirely
in userland, using TUN devices and its own IPsec implementation libipsec.

%package charon-nm
Summary:        NetworkManager plugin for Strongswan
Requires:       dbus
Obsoletes:      strongswan-NetworkManager < 0:5.0.4-5
Conflicts:      strongswan-NetworkManager < 0:5.0.4-5
Conflicts:      NetworkManager-strongswan < 1.4.2-1
%description charon-nm
NetworkManager plugin integrates a subset of Strongswan capabilities
to NetworkManager.

%package sqlite
Summary: SQLite support for strongSwan
Requires: strongswan = %{version}-%{release}
%description sqlite
The sqlite plugin adds an SQLite database backend to strongSwan.

%package tnc-imcvs
Summary: Trusted network connect (TNC)'s IMC/IMV functionality
Requires: strongswan = %{version}-%{release}
Requires: strongswan-sqlite = %{version}-%{release}
%description tnc-imcvs
This package provides Trusted Network Connect's (TNC) architecture support.
It includes support for TNC client and server (IF-TNCCS), IMC and IMV message
exchange (IF-M), interface between IMC/IMV and TNC client/server (IF-IMC
and IF-IMV). It also includes PTS based IMC/IMV for TPM based remote
attestation, SWID IMC/IMV, and OS IMC/IMV. It's IMC/IMV dynamic libraries
modules can be used by any third party TNC Client/Server implementation
possessing a standard IF-IMC/IMV interface. In addition, it implements
PT-TLS to support TNC over TLS.

%if %{with python3}
%package -n python3-vici
Summary: Strongswan Versatile IKE Configuration Interface python bindings
BuildArch: noarch
%description -n python3-vici
VICI is an attempt to improve the situation for system integrators by providing
a stable IPC interface, allowing external tools to query, configure
and control the IKE daemon.

The Versatile IKE Configuration Interface (VICI) python bindings provides module
for Strongswan runtime configuration from python applications.

%endif

%if %{with perl}
%package -n perl-vici
Summary: Strongswan Versatile IKE Configuration Interface perl bindings
BuildArch: noarch
%description -n perl-vici
VICI is an attempt to improve the situation for system integrators by providing
a stable IPC interface, allowing external tools to query, configure
and control the IKE daemon.

The Versatile IKE Configuration Interface (VICI) perl bindings provides module
for Strongswan runtime configuration from perl applications.
%endif

# TODO: make also ruby-vici


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n %{name}-%{version}%{?prerelease} -p1

%build
# only for snapshots
export ACLOCAL_PATH=/usr/share/gettext/m4:$ACLOCAL_PATH
autoreconf -fiv

# --with-ipsecdir moves internal commands to /usr/libexec/strongswan
# --bindir moves 'pki' command to /usr/libexec/strongswan
# See: http://wiki.strongswan.org/issues/552
# too broken to enable:    --enable-sha3 --enable-rdrand --enable-connmark --enable-forecast
%configure --disable-static \
    --with-ipsec-script=strongswan \
    --sysconfdir=%{_sysconfdir}/strongswan \
    --with-ipsecdir=%{_libexecdir}/strongswan \
    --bindir=%{_libexecdir}/strongswan \
    --with-ipseclibdir=%{_libdir}/strongswan \
    --with-piddir=%{_rundir}/strongswan \
    --with-nm-ca-dir=%{_sysconfdir}/strongswan/ipsec.d/cacerts/ \
    --enable-bypass-lan \
    --enable-tss-tss2 \
    --enable-nm \
    --enable-systemd \
    --enable-openssl \
    --enable-unity \
    --enable-ctr \
    --enable-ccm \
    --enable-gcm \
    --enable-chapoly \
    --enable-md4 \
    --enable-gcrypt \
    --enable-newhope \
    --enable-xauth-eap \
    --enable-xauth-pam \
    --enable-xauth-noauth \
    --enable-eap-identity \
    --enable-eap-md5 \
    --enable-eap-gtc \
    --enable-eap-tls \
    --enable-eap-ttls \
    --enable-eap-peap \
    --enable-eap-mschapv2 \
    --enable-eap-tnc \
    --enable-eap-sim \
    --enable-eap-sim-file \
    --enable-eap-aka \
    --enable-eap-aka-3gpp \
    --enable-eap-aka-3gpp2 \
    --enable-eap-dynamic \
    --enable-eap-radius \
    --enable-ext-auth \
    --enable-ipseckey \
    --enable-pkcs11 \
    --enable-tpm \
    --enable-farp \
    --enable-dhcp \
    --enable-ha \
    --enable-led \
    --enable-sql \
    --enable-sqlite \
    --enable-tnc-ifmap \
    --enable-tnc-pdp \
    --enable-tnc-imc \
    --enable-tnc-imv \
    --enable-tnccs-20 \
    --enable-tnccs-11 \
    --enable-tnccs-dynamic \
    --enable-imc-test \
    --enable-imv-test \
    --enable-imc-scanner \
    --enable-imv-scanner  \
    --enable-imc-attestation \
    --enable-imv-attestation \
    --enable-imv-os \
    --enable-imc-os \
    --enable-imc-swima \
    --enable-imv-swima \
    --enable-imc-hcd \
    --enable-imv-hcd \
    --enable-curl \
    --enable-cmd \
    --enable-acert \
    --enable-vici \
    --enable-swanctl \
    --enable-duplicheck \
    --enable-selinux \
    --enable-stroke \
%ifarch x86_64 %{ix86}
    --enable-aesni \
%endif
%if %{with python3}
    PYTHON=%{python3} --enable-python-wheels \
%endif
%if %{with perl}
    --enable-perl-cpan \
%endif
%if %{with check}
    --enable-test-vectors \
%endif
    --enable-kernel-libipsec \
    --with-capabilities=libcap \
    CPPFLAGS="-DSTARTER_ALLOW_NON_ROOT"

# disable certain plugins in the daemon configuration by default
for p in bypass-lan; do
    echo -e "\ncharon.plugins.${p}.load := no" >> conf/plugins/${p}.opt
done

# ensure manual page is regenerated with local configuration
rm -f src/ipsec/_ipsec.8

%make_build

pushd src/libcharon/plugins/vici

%if %{with python3}
  pushd python
    %make_build
    sed -e "s,/var/run/charon.vici,%{_rundir}/strongswan/charon.vici," -i vici/session.py
    #py3_build
  popd
%endif

%if %{with perl}
  pushd perl/Vici-Session/
    perl Makefile.PL INSTALLDIRS=vendor
    %make_build
  popd
%endif

popd

%install
%make_install


pushd src/libcharon/plugins/vici
%if %{with python3}
  pushd python
    # TODO: --enable-python-eggs breaks our previous build. Do it now
    # propose better way to upstream
    %pyproject_wheel
    %pyproject_install
  popd
%endif
%if %{with perl}
  %make_install -C perl/Vici-Session
  rm -f %{buildroot}{%{perl_archlib}/perllocal.pod,%{perl_vendorarch}/auto/Vici/Session/.packlist}
%endif
popd
# prefix man pages
for i in %{buildroot}%{_mandir}/*/*; do
    if echo "$i" | grep -vq '/strongswan[^\/]*$'; then
        mv "$i" "`echo "$i" | sed -re 's|/([^/]+)$|/strongswan_\1|'`"
    fi
done
find %{buildroot} -type f -name '*.la' -delete
# delete unwanted library files - no consumers, so no -devel package
rm %{buildroot}%{_libdir}/strongswan/*.so
# fix config permissions
chmod 644 %{buildroot}%{_sysconfdir}/strongswan/strongswan.conf

# Create ipsec.d directory tree.
install -d -m 700 %{buildroot}%{_sysconfdir}/strongswan/ipsec.d
for i in aacerts acerts certs cacerts crls ocspcerts private reqs; do
    install -d -m 700 %{buildroot}%{_sysconfdir}/strongswan/ipsec.d/${i}
done
install -d -m 0700 %{buildroot}%{_rundir}/strongswan
install -D -m 0644 %{SOURCE3} %{buildroot}/%{_tmpfilesdir}/strongswan.conf
install -D -m 0644 %{SOURCE3} %{buildroot}/%{_tmpfilesdir}/strongswan-starter.conf

%check
%if %{with check}
  # Seen some tests hang. Ensure we do not block builder forever
  export TESTS_VERBOSITY=1
  timeout 600 %make_build check
%endif
%if %{with python}
  pushd src/libcharon/plugins/vici
    %pytest
  popd
%endif
:

%post
%systemd_post strongswan.service strongswan-starter.service

%preun
%systemd_preun strongswan.service strongswan-starter.service

%postun
%systemd_postun_with_restart strongswan.service strongswan-starter.service

%files
%doc README NEWS TODO ChangeLog
%license COPYING
%dir %attr(0755,root,root) %{_sysconfdir}/strongswan
%config(noreplace) %{_sysconfdir}/strongswan/*
%dir %{_libdir}/strongswan
%exclude %{_libdir}/strongswan/imcvs
%dir %{_libdir}/strongswan/plugins
%dir %{_libexecdir}/strongswan
%{_unitdir}/strongswan.service
%{_unitdir}/strongswan-starter.service
%{_sbindir}/charon-cmd
%{_sbindir}/charon-systemd
%{_sbindir}/strongswan
%{_sbindir}/swanctl
%{_libdir}/strongswan/*.so.*
%exclude %{_libdir}/strongswan/libimcv.so.*
%exclude %{_libdir}/strongswan/libtnccs.so.*
%exclude %{_libdir}/strongswan/libipsec.so.*
%{_libdir}/strongswan/plugins/*.so
%exclude %{_libdir}/strongswan/plugins/libstrongswan-sqlite.so
%exclude %{_libdir}/strongswan/plugins/libstrongswan-*tnc*.so
%exclude %{_libdir}/strongswan/plugins/libstrongswan-kernel-libipsec.so
%{_libexecdir}/strongswan/*
%exclude %{_libexecdir}/strongswan/attest
%exclude %{_libexecdir}/strongswan/pt-tls-client
%exclude %{_libexecdir}/strongswan/charon-nm
%exclude %dir %{_datadir}/strongswan/swidtag
%{_mandir}/man?/*.gz
%{_datadir}/strongswan/templates/config/
%{_datadir}/strongswan/templates/database/
%attr(0755,root,root) %dir %{_rundir}/strongswan
%attr(0644,root,root) %{_tmpfilesdir}/strongswan.conf
%attr(0644,root,root) %{_tmpfilesdir}/strongswan-starter.conf

%files sqlite
%{_libdir}/strongswan/plugins/libstrongswan-sqlite.so

%files tnc-imcvs
%{_sbindir}/sw-collector
%{_sbindir}/sec-updater
%dir %{_libdir}/strongswan/imcvs
%dir %{_libdir}/strongswan/plugins
%{_libdir}/strongswan/libimcv.so.*
%{_libdir}/strongswan/libtnccs.so.*
%{_libdir}/strongswan/plugins/libstrongswan-*tnc*.so
%{_libexecdir}/strongswan/attest
%{_libexecdir}/strongswan/pt-tls-client
%dir %{_datadir}/strongswan/swidtag
%{_datadir}/strongswan/swidtag/*.swidtag

%files libipsec
%{_libdir}/strongswan/libipsec.so.*
%{_libdir}/strongswan/plugins/libstrongswan-kernel-libipsec.so

%files charon-nm
%doc COPYING
%{_datadir}/dbus-1/system.d/nm-strongswan-service.conf
%{_libexecdir}/strongswan/charon-nm

%if %{with python3}
%files -n python3-vici
%license COPYING
%doc src/libcharon/plugins/vici/python/README.rst
%{python3_sitelib}/vici
%{python3_sitelib}/vici-%{version}.dist-info
%endif

%if %{with perl}
%license COPYING
%files -n perl-vici
%{perl_vendorlib}/Vici
%endif

%changelog
%autochangelog
