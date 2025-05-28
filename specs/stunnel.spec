# Do not generate provides for private libraries
%global __provides_exclude_from ^%{_libdir}/stunnel/.*$

%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with libwrap
%else
%bcond_without libwrap
%endif

%if 0%{?rhel} >= 10
%bcond openssl_engine 0
%else
%bcond openssl_engine 1
%endif

Summary: A TLS-encrypting socket wrapper
Name: stunnel
Version: 5.75
Release: %autorelease
License: GPL-2.0-or-later WITH stunnel-exception AND MIT
URL: https://www.stunnel.org/
Source0: https://www.stunnel.org/downloads/stunnel-%{version}.tar.gz
Source1: https://www.stunnel.org/downloads/stunnel-%{version}.tar.gz.asc
Source2: Certificate-Creation
Source3: sfinger.xinetd
Source4: stunnel-sfinger.conf
Source5: pop3-redirect.xinetd
Source6: stunnel-pop3s-client.conf
Source7: stunnel@.service
# Upstream release signing key
# Upstream source is https://www.stunnel.org/pgp.asc; using a local URL because
# the remote one makes packit source-git choke.
Source99: pgp.asc
# Apply patch stunnel-5.50-authpriv.patch
Patch0:   stunnel-5.50-authpriv.patch
# Apply patch stunnel-5.61-systemd-service.patch
Patch1:   stunnel-5.61-systemd-service.patch
# Use cipher configuration from crypto-policies
# 
# On Fedora, CentOS and RHEL, the system's crypto policies are the best
# source to determine which cipher suites to accept in TLS. On these
# platforms, OpenSSL supports the PROFILE=SYSTEM setting to use those
# policies. Change stunnel to default to this setting.
Patch3:   stunnel-5.69-system-ciphers.patch
# Use TLS version f/crypto-policies unless specified
# 
# Do not explicitly set the TLS version and rely on the defaults from
# crypto-policies unless a TLS minimum or maximum version are explicitly
# specified in the stunnel configuration.
Patch5:   stunnel-5.72-default-tls-version.patch
# Apply patch stunnel-5.56-curves-doc-update.patch
Patch6:   stunnel-5.56-curves-doc-update.patch
# util-linux is needed for rename
BuildRequires: make
BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: openssl-devel, pkgconfig, util-linux
%if %{with openssl_engine} && 0%{?fedora} >= 41
BuildRequires: openssl-devel-engine
%endif
BuildRequires: autoconf automake libtool
%if %{with libwrap}
Buildrequires: tcp_wrappers-devel
%endif
BuildRequires: /usr/bin/pod2man
BuildRequires: /usr/bin/pod2html
# build test requirements
BuildRequires: /usr/bin/nc, /usr/bin/lsof, /usr/bin/ps
BuildRequires: python3 python3-cryptography openssl
BuildRequires: systemd systemd-devel
%{?systemd_requires}

%description
Stunnel is a socket wrapper which can provide TLS/SSL
(Transport Layer Security/Secure Sockets Layer) support
to ordinary applications. For example, it can be used in
conjunction with imapd to create a TLS secure IMAP server.

%prep
%{gpgverify} --keyring='%{SOURCE99}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -S gendiff -p1

%build
#autoreconf -v
CFLAGS="$RPM_OPT_FLAGS -fPIC"; export CFLAGS
if pkg-config openssl ; then
	CFLAGS="$CFLAGS `pkg-config --cflags openssl`";
	LDFLAGS="`pkg-config --libs-only-L openssl`"; export LDFLAGS
fi

CPPFLAGS_NO_ENGINE=""
%if !%{with openssl_engine}
	CPPFLAGS_NO_ENGINE="-DOPENSSL_NO_ENGINE"
%endif
%configure --enable-fips --enable-ipv6 --with-ssl=%{_prefix} \
%if %{with libwrap}
--enable-libwrap \
%else
--disable-libwrap \
%endif
	--with-bashcompdir=%{_datadir}/bash-completion/completions \
	CPPFLAGS="-UPIDFILE -DPIDFILE='\"%{_localstatedir}/run/stunnel.pid\"' $CPPFLAGS_NO_ENGINE"
make V=1 LDADD="-pie -Wl,-z,defs,-z,relro,-z,now"

%install
make install DESTDIR=%{buildroot}
# Move the translated man pages to the right subdirectories, and strip off the
# language suffixes.
#for lang in fr pl ; do
for lang in pl ; do
	mkdir -p %{buildroot}/%{_mandir}/${lang}/man8
	mv %{buildroot}/%{_mandir}/man8/*.${lang}.8* %{buildroot}/%{_mandir}/${lang}/man8/
	rename ".${lang}" "" %{buildroot}/%{_mandir}/${lang}/man8/*
done
mkdir srpm-docs
cp %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} srpm-docs
mkdir -p %{buildroot}%{_unitdir}
cp %{buildroot}%{_datadir}/doc/stunnel/examples/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
cp %{SOURCE7} %{buildroot}%{_unitdir}/%{name}@.service

%check
if ! make test; then
	for i in tests/logs/*.log; do
		echo "$i":
		cat "$i"
	done
	exit 1
fi

%files
%{!?_licensedir:%global license %%doc}
%doc AUTHORS.md BUGS.md CREDITS.md PORTS.md README.md TODO.md
%doc tools/stunnel.conf-sample
%doc srpm-docs/*
%license COPY*
%lang(en) %doc doc/en/*
%lang(pl) %doc doc/pl/*
%{_bindir}/stunnel
%exclude %{_bindir}/stunnel3
%exclude %{_datadir}/doc/stunnel
%{_libdir}/stunnel
%exclude %{_libdir}/stunnel/libstunnel.la
%{_mandir}/man8/stunnel.8*
%lang(pl) %{_mandir}/pl/man8/stunnel.8*
%dir %{_sysconfdir}/%{name}
%exclude %{_sysconfdir}/stunnel/*
%{_unitdir}/%{name}*.service
%{_datadir}/bash-completion/completions/%{name}.bash

%post
/sbin/ldconfig
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
/sbin/ldconfig
%systemd_postun_with_restart %{name}.service

%changelog
%autochangelog
