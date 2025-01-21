%global sslcert %{_sysconfdir}/pki/%{name}/server.cert.pem
%global sslkey  %{_sysconfdir}/pki/%{name}/server.key.pem

%bcond_without  maxmind
%global pcre2   10.44

Summary:        Open Source IRC server
Name:           unrealircd
Version:        6.1.9.1
Release:        2%{?dist}
# UnrealIRCd declares itself as GPL-2.0-or-later as it's the common denominator for
# a GPL-1.0-or-later and GPL-2.0-or-later mixture, breakdown of other source codes:
# BSD-3-Clause: include/mempool.h and src/mempool.c
# ISC: src/openssl_hostname_validation.c
# LicenseRef-Fedora-Public-Domain: include/crypt_blowfish.h and src/crypt_blowfish.c
# MIT: include/openssl_hostname_validation.h
License:        GPL-1.0-or-later AND GPL-2.0-or-later AND BSD-3-Clause AND ISC AND LicenseRef-Fedora-Public-Domain AND MIT
URL:            https://www.unrealircd.org/
Source0:        https://www.unrealircd.org/downloads/%{name}-%{version}.tar.gz
Source1:        https://www.unrealircd.org/downloads/%{name}-%{version}.tar.gz.asc
Source2:        gpgkey-1D2D2B03A0B68ED11D68A24BA7A21B0A108FF4A9.gpg
Source3:        %{name}.service
Source4:        %{name}.tmpfilesd
Source5:        %{name}.sysusersd
# Apply Fedora system-wide crypto policy
Patch0:         unrealircd-6.0.6-crypto-policy.patch
# Disable GeoIP to avoid dependency to legacy GeoIP
Patch1:         unrealircd-6.1.8-geoip.patch
# Same options like in unrealircd(ctl) shell script
Patch2:         unrealircd-6.0.3-unrealircdctl.patch
BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  %{_bindir}/openssl
BuildRequires:  openssl-devel
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  pcre2-devel >= 10.36
%else
Provides:       bundled(pcre2) = %{pcre2}
%endif
BuildRequires:  libargon2-devel >= 20161029
BuildRequires:  libsodium-devel >= 1.0.16
BuildRequires:  c-ares-devel >= 1.6.0
BuildRequires:  jansson-devel >= 2.0.0
BuildRequires:  libcurl-devel
BuildRequires:  systemd-rpm-macros
Requires(post): %{_bindir}/openssl
%{?systemd_requires}
%{?sysusers_requires_compat}

%description
UnrealIRCd is an Open Source IRC server based on the branch of IRCu called
Dreamforge, formerly used by the DALnet IRC network. Since the beginning of
development on UnrealIRCd in May of 1999, it has become a highly advanced
IRCd with a strong focus on modularity, an advanced and highly configurable
configuration file. Key features include SSL/TLS, cloaking, advanced anti-
flood and anti-spam systems, swear filtering and module support.

%if %{with maxmind}
%package maxmind
Summary:        GeoIP module using MaxMind databases for UnrealIRCd
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  libmaxminddb-devel >= 1.4.3
%else
BuildRequires:  libmaxminddb-devel >= 1.2.0
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description maxmind
UnrealIRCd is an Open Source IRC server with a strong focus on modularity.

This package provides an UnrealIRCd module to support GeoIP using MaxMind's
GeoIP2 C library and databases.
%endif

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch -P0 -p1 -b .crypto-policy
touch -c -r doc/conf/examples/example.conf{.crypto-policy,}
%patch -P1 -p1 -b .geoip
touch -c -r doc/conf/modules.default.conf{.geoip,}
%patch -P2 -p1 -b .unrealircdctl

# Ensure the bundled PCRE2 tarball matches the version in this spec file
! tar tfz extras/pcre2.tar.gz | grep -E -m 1 -v '^pcre2-%{pcre2}/'

%build
%if 0%{?rhel} == 8
# Bundling option for PCRE2 in UnrealIRCd itself is not really suitable for
# distribution packaging, thus build it first and pretend it as system one.
BUNDLED=$PWD/extras/pcre2
tar xfz extras/pcre2.tar.gz -C extras
cd extras/pcre2-%{pcre2}/
export CFLAGS="$RPM_OPT_FLAGS -fPIC"
%configure --enable-jit --enable-shared=no
%make_build
%make_install DESTDIR=$BUNDLED
cd $OLDPWD
sed \
  -e "s|^libdir=.*|libdir=$BUNDLED%{_libdir}|" \
  -e "s|^includedir=.*|includedir=$BUNDLED%{_includedir}|" \
  -i $BUNDLED%{_libdir}/pkgconfig/libpcre2-8.pc
export PKG_CONFIG_PATH="$BUNDLED%{_libdir}/pkgconfig"
%endif

# https://github.com/unrealircd/unrealircd/pull/183
%if %{with maxmind} && 0%{?rhel} == 8
sed -e 's|libmaxminddb >= 1.4.3|libmaxminddb >= 1.2.0|g' -i configure
%endif

# Mention new unrealircdctl tool rather than shell script
for file in src/{conf,ircd,misc,modulemanager,proc_io_server,unrealircdctl}.c doc/conf/examples/*.conf; do
  sed -e 's|\./unrealircd\([ "]\)|unrealircdctl\1|g' ${file} > ${file}.tmp
  touch -c -r ${file} ${file}.tmp && mv -f ${file}.tmp ${file}
done

%configure \
  --enable-ssl \
  --with-system-pcre2 \
  --with-system-argon2 \
  --with-system-sodium \
  --with-system-cares \
  --with-system-jansson \
  --enable-libcurl \
  %{?with_maxmind:--enable-libmaxminddb=yes} \
  --with-bindir=%{_bindir} \
  --with-scriptdir=unused \
  --with-confdir=%{_sysconfdir}/%{name} \
  --with-modulesdir=%{_libdir}/%{name} \
  --with-logdir=%{_localstatedir}/log/%{name} \
  --with-cachedir=%{_localstatedir}/cache/%{name} \
  --with-tmpdir=%{_localstatedir}/lib/%{name}/tmp \
  --with-datadir=%{_localstatedir}/lib/%{name} \
  --with-docdir=unused \
  --with-pidfile=%{_rundir}/%{name}/%{name}.pid \
  --with-controlfile=%{_rundir}/%{name}/%{name}.ctl \
  --with-permissions=0640 \
  --enable-dynamic-linking \
  --with-privatelibdir=no
%make_build

%install
%make_install

# Fix strange default permissions
chmod -R g+rX,o+rX $RPM_BUILD_ROOT

# Provide default configuration based on default example
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/{examples/example.conf,%{name}.conf}
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/examples/

# Remove module repository configuration (for module manager)
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/modules.sources.list

# Remove upgrade script intended only for source code users
rm -f $RPM_BUILD_ROOT%{_bindir}/unrealircd-upgrade-script

# Move tls directory and symlink it
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pki/
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/{%{name}/tls,pki/%{name}}/
ln -s ../pki/%{name}/ $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/tls
ln -sf ../tls/certs/ca-bundle.crt $RPM_BUILD_ROOT%{_sysconfdir}/pki/%{name}/curl-ca-bundle.crt

# Install systemd and tmpfiles files
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf
mkdir -p $RPM_BUILD_ROOT%{_rundir}/%{name}/

%pre
%sysusers_create_compat %{SOURCE5}

%post
%systemd_post %{name}.service

if [ ! -f %{sslkey} ]; then
  umask 077
  %{_bindir}/openssl genrsa 4096 > %{sslkey} 2> /dev/null
  chown root:%{name} %{sslkey}
  chmod 640 %{sslkey}
fi

if [ ! -f %{sslcert} ]; then
  FQDN=`hostname 2> /dev/null`
  if [ "x${FQDN}" = "x" ]; then
    FQDN=localhost.localdomain
  fi

  %{_bindir}/openssl req -new -key %{sslkey} -x509 -sha256 -days 365 -set_serial $RANDOM -out %{sslcert} \
    -subj "/C=--/ST=SomeState/L=SomeCity/O=SomeOrganization/OU=SomeOrganizationalUnit/CN=${FQDN}/emailAddress=root@${FQDN}"
  chmod 644 %{sslcert}
fi

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%doc doc/Authors doc/coding-guidelines doc/tao.of.irc
%doc README.md doc/RELEASE-NOTES.md
%dir %attr(0750,root,%{name}) %{_sysconfdir}/pki/%{name}/
%{_sysconfdir}/pki/%{name}/curl-ca-bundle.crt
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/*.conf
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/aliases/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/aliases/*.conf
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/help/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/help/*.conf
%{_sysconfdir}/%{name}/tls
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%{_bindir}/%{name}
%{_bindir}/unrealircdctl
%{_libdir}/%{name}/
%{?with_maxmind:%exclude %{_libdir}/%{name}/geoip_maxmind.so}
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/cache/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/tmp/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/log/%{name}/
%dir %attr(0755,%{name},%{name}) %{_rundir}/%{name}/

%if %{with maxmind}
%files maxmind
%{_libdir}/%{name}/geoip_maxmind.so
%endif

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 13 2024 Robert Scheck <robert@fedoraproject.org> 6.1.9.1-1
- Upgrade to 6.1.9.1 (#2327604)

* Tue Oct 22 2024 Richard W.M. Jones <rjones@redhat.com> - 6.1.8.1-2
- Rebuild for Jansson 2.14
  (https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/3PYINSQGKQ4BB25NQUI2A2UCGGLAG5ND/)

* Sat Oct 19 2024 Robert Scheck <robert@fedoraproject.org> 6.1.8.1-1
- Upgrade to 6.1.8.1 (#2319754)

* Sat Oct 12 2024 Robert Scheck <robert@fedoraproject.org> 6.1.8-1
- Upgrade to 6.1.8 (#2315105)

* Sat Sep 14 2024 Robert Scheck <robert@fedoraproject.org> 6.1.7.2-1
- Upgrade to 6.1.7.2 (#2297919)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 15 2024 Robert Scheck <robert@fedoraproject.org> 6.1.6-1
- Upgrade to 6.1.6 (#2290902)

* Sun May 12 2024 Robert Scheck <robert@fedoraproject.org> 6.1.5-1
- Upgrade to 6.1.5 (#2276377)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 16 2023 Robert Scheck <robert@fedoraproject.org> 6.1.4-1
- Upgrade to 6.1.4 (#2254828)

* Sat Dec 09 2023 Robert Scheck <robert@fedoraproject.org> 6.1.3-1
- Upgrade to 6.1.3 (#2252372)

* Sun Nov 05 2023 Robert Scheck <robert@fedoraproject.org> 6.1.2.3-2
- Build upstream's bundled recent PCRE2 version for RHEL 7 and 8

* Mon Oct 16 2023 Robert Scheck <robert@fedoraproject.org> 6.1.2.3-1
- Upgrade to 6.1.2.3 (#2238031)

* Sun Oct 08 2023 Robert Scheck <robert@fedoraproject.org> 6.1.2.2-1
- Upgrade to 6.1.2.2 (#2238031)

* Thu Oct 05 2023 Robert Scheck <robert@fedoraproject.org> 6.1.2.1-1
- Upgrade to 6.1.2.1 (#2238031)

* Thu Oct 05 2023 Robert Scheck <robert@fedoraproject.org> 6.1.2-1
- Upgrade to 6.1.2 (#2238031)

* Thu Oct 05 2023 Remi Collet <remi@remirepo.net> - 6.1.1.1-3
- rebuild for new libsodium

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Robert Scheck <robert@fedoraproject.org> 6.1.1.1-1
- Upgrade to 6.1.1.1 (#2215598)

* Wed Jun 14 2023 Robert Scheck <robert@fedoraproject.org> 6.1.1-1
- Upgrade to 6.1.1 (#2211354)

* Sat May 06 2023 Robert Scheck <robert@fedoraproject.org> 6.1.0-1
- Upgrade to 6.1.0 (#2185257)

* Sun Mar 26 2023 Robert Scheck <robert@fedoraproject.org> 6.0.7-1
- Upgrade to 6.0.7 (#2181536)

* Sat Feb 04 2023 Robert Scheck <robert@fedoraproject.org> 6.0.6-1
- Upgrade to 6.0.6 (#2166855)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Robert Scheck <robert@fedoraproject.org> 6.0.5-1
- Upgrade to 6.0.5 (#2151482)

* Sat Nov 19 2022 Robert Scheck <robert@fedoraproject.org> 6.0.4.2-1
- Upgrade to 6.0.4.2 (#2143921)

* Mon Aug 29 2022 Robert Scheck <robert@fedoraproject.org> 6.0.4.1-1
- Upgrade to 6.0.4.1 (#2122120)

* Fri Jul 29 2022 Robert Scheck <robert@fedoraproject.org> 6.0.4-3
- Added sysusers.d file to achieve user() and group() provides

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Robert Scheck <robert@fedoraproject.org> 6.0.4-1
- Upgrade to 6.0.4 (#2090417)

* Sat Apr 02 2022 Robert Scheck <robert@fedoraproject.org> 6.0.3-1
- Upgrade to 6.0.3 (#2071197)

* Mon Mar 21 2022 Robert Scheck <robert@fedoraproject.org> 6.0.2-1
- Upgrade to 6.0.2 (#2038245)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 31 2021 Robert Scheck <robert@fedoraproject.org> 6.0.1.1-1
- Upgrade to 6.0.1.1 (#2033813)

* Thu Dec 30 2021 Robert Scheck <robert@fedoraproject.org> 6.0.1-1
- Upgrade to 6.0.1 (#2033813)

* Wed Dec 29 2021 Robert Scheck <robert@fedoraproject.org> 6.0.0-1
- Upgrade to 6.0.0 (#2033813)

* Wed Dec 29 2021 Robert Scheck <robert@fedoraproject.org> 5.2.3-1
- Upgrade to 5.2.3

* Sun Oct 03 2021 Robert Scheck <robert@fedoraproject.org> 5.2.2-1
- Upgrade to 5.2.2 (#2010085)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 5.2.1.1-3
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Robert Scheck <robert@fedoraproject.org> 5.2.1.1-1
- Upgrade to 5.2.1.1 (#1978927 #c2)

* Fri Jul 09 2021 Robert Scheck <robert@fedoraproject.org> 5.2.1-1
- Upgrade to 5.2.1 (#1978927)

* Fri Jun 25 2021 Robert Scheck <robert@fedoraproject.org> 5.2.0.2-1
- Upgrade to 5.2.0.2 (#1976246)

* Wed Jun 16 2021 Robert Scheck <robert@fedoraproject.org> 5.2.0.1-1
- Upgrade to 5.2.0.1 (#1972543)

* Tue Jun 15 2021 Robert Scheck <robert@fedoraproject.org> 5.2.0-1
- Upgrade to 5.2.0 (#1967860)

* Fri Mar 26 2021 Robert Scheck <robert@fedoraproject.org> 5.0.9.1-1
- Upgrade to 5.0.9.1 (#1943492)

* Sun Mar 21 2021 Robert Scheck <robert@fedoraproject.org> 5.0.9-1
- Upgrade to 5.0.9 (#1938404)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.0.8-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 08 2021 Robert Scheck <robert@fedoraproject.org> 5.0.8-1
- Upgrade to 5.0.8 (#1911652)

* Sat Nov 07 2020 Robert Scheck <robert@fedoraproject.org> 5.0.7-2
- Remove build-time path from rpath (#1891370 #c1)
- Apply Fedora system-wide crypto policy (#1891370 #c1)
- License breakdown in spec file (#1891370 #c1)

* Sun Oct 18 2020 Robert Scheck <robert@fedoraproject.org> 5.0.7-1
- Upgrade to 5.0.7 (#1891370)

* Wed Apr 16 2008 Robert Scheck <robert@fedoraproject.org> 3.2.7-2
- Rebuild for openssl 0.9.8g and curl 7.18.0

* Thu Sep 06 2007 Robert Scheck <robert@fedoraproject.org> 3.2.7-1
- Upgrade to 3.2.7

* Sun Jun 10 2007 Robert Scheck <robert@fedoraproject.org> 3.2.6-2
- Rebuild for curl 7.16.2

* Sat Dec 23 2006 Robert Scheck <robert@fedoraproject.org> 3.2.6-1
- Upgrade to 3.2.6

* Sun Nov 05 2006 Robert Scheck <robert@fedoraproject.org> 3.2.5-2
- Enabled ziplinks and remote includes by linking zlib and curl

* Wed Nov 01 2006 Robert Scheck <robert@fedoraproject.org> 3.2.5-1
- Upgrade to 3.2.5 and rebuilt against glibc 2.5

* Sun May 07 2006 Robert Scheck <robert@fedoraproject.org> 3.2.4-3
- Added proxyscan 1.1 module for scanning open proxy servers (DNSBL,
  HTTP-CONNECT and -POST, Socks 4 and 5, Wingate and Cisco routers)

* Mon Mar 20 2006 Robert Scheck <robert@fedoraproject.org> 3.2.4-2
- Install Anope IRC Services aliases configuration files

* Thu Mar 16 2006 Robert Scheck <robert@fedoraproject.org> 3.2.4-1
- Upgrade to 3.2.4 and rebuilt against gcc 4.1 and glibc 2.4
- Re-added nocodes, privdeaf, ircops, sanick and timedbans modules
- Backported native cgiirc support from latest UnrealIRCd CVS

* Sat Oct 22 2005 Robert Scheck <robert@fedoraproject.org> 3.2.3-5
- Added timedbans 1.0 module to provide timebased channel bans
- Added cgiirc 1.7 module for hostname rewriting at CGI:IRC webchats
- Added cmdflood 1.8 module to limit the use of IRC commands
- Added chgswhois 1.3 module for easy changing SWHOIS information

* Sat Aug 27 2005 Robert Scheck <robert@fedoraproject.org> 3.2.3-4
- Added uline 1.13 module for allowing u:lined network admins
- Added netadmins 1.8 module for having unkillable netadmins
- Fixed IPv6 problem with gcc 4.0 in a sane way from UnrealIRCd CVS
- Added clones 1.8 module for displaying users with the same IP

* Sun Aug 21 2005 Robert Scheck <robert@fedoraproject.org> 3.2.3-3
- Added sanick 1.2 module for changing as IRC op a user's nickname
- Show nick!user@host of the person who set the topic, rather nick
- Added privdeaf 0.0.6 module for avoiding private messages/notices
- Added ircops 3.6 module for displaying a list of all IRC operators

* Tue Aug 09 2005 Robert Scheck <robert@fedoraproject.org> 3.2.3-2
- Added the nocodes 0.1 module for striping bold, underlined etc.
- Show the modes a channel has set in the /list output
- Rebuilt against gcc 4.0.1 and glibc 2.3.90

* Mon Mar 21 2005 Robert Scheck <robert@fedoraproject.org> 3.2.3-1
- Upgrade to 3.2.3 and rebuilt against gcc 4.0

* Sun Feb 06 2005 Robert Scheck <robert@fedoraproject.org> 3.2.2b-3
- Fixed system user creation and logging behaviour
- Adapted unrealircd.conf default configuration file

* Sun Jan 30 2005 Robert Scheck <robert@fedoraproject.org> 3.2.2b-2
- Fixed initscript

* Sun Jan 16 2005 Robert Scheck <robert@fedoraproject.org> 3.2.2b-1
- Upgrade to 3.2.2b

* Mon Nov 29 2004 Robert Scheck <robert@fedoraproject.org> 3.2.2-1
- Upgrade to 3.2.2
- Initial spec file for Red Hat Linux and Fedora Core
