%{!?lua_version: %global lua_version %{lua: print(string.sub(_VERSION, 5))}}

%global sslcert    %{_sysconfdir}/pki/%{name}/localhost.crt
%global sslkey     %{_sysconfdir}/pki/%{name}/localhost.key

Summary:           Flexible communications server for Jabber/XMPP
Name:              prosody
Version:           0.12.4
Release:           6%{?dist}
License:           MIT
URL:               https://prosody.im/
Source0:           https://prosody.im/downloads/source/%{name}-%{version}.tar.gz
Source1:           https://prosody.im/downloads/source/%{name}-%{version}.tar.gz.asc
Source2:           https://keys.openpgp.org/vks/v1/by-fingerprint/3E52119EF853C59678DBBF6BADED9A77B67AD329
Source3:           prosody.service
Source4:           prosody.logrotate
Source5:           prosody.tmpfilesd
Source6:           prosody.sysusersd
Source7:           prosody-localhost.cfg.lua
Source8:           prosody-example.com.cfg.lua
Patch0:            prosody-0.12.3-config.patch
BuildRequires:     gnupg2
BuildRequires:     gcc
BuildRequires:     make
BuildRequires:     libicu-devel
BuildRequires:     openssl-devel
BuildRequires:     lua
BuildRequires:     lua-devel
BuildRequires:     systemd-rpm-macros
Requires:          %{_bindir}/openssl
Requires(post):    %{_bindir}/openssl
Requires:          lua(abi) = %{lua_version}
Requires:          lua-filesystem
Requires:          lua-expat
Requires:          lua-socket
Requires:          lua-sec
Recommends:        lua-unbound
Recommends:        lua-readline
%{?systemd_requires}
%{?sysusers_requires_compat}

# Testsuite in %%check
BuildRequires:     lua-filesystem
BuildRequires:     lua-expat
BuildRequires:     lua-socket
BuildRequires:     lua-sec
BuildRequires:     lua-unbound
BuildRequires:     %{_bindir}/openssl
BuildRequires:     %{_sbindir}/ss

%description
Prosody is a flexible communications server for Jabber/XMPP written in Lua.
It aims to be easy to use, and light on resources. For developers it aims
to be easy to extend and give a flexible system on which to rapidly develop
added functionality, or prototype new protocols.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%patch -P0 -p1 -b .config

%build
./configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --idn-library=icu \
  --add-cflags="$RPM_OPT_FLAGS" \
  --add-ldflags="$RPM_LD_FLAGS" \
  --no-example-certs
%make_build

# Make prosody-migrator
%make_build -C tools/migration

%install
mkdir -p $RPM_BUILD_ROOT{%{_sysconfdir}/pki,%{_localstatedir}/{lib,log}/%{name}}/
%make_install

# Install prosody-migrator
%make_install -C tools/migration

# Install ejabberd2prosody
install -p -m 0755 tools/ejabberd2prosody.lua $RPM_BUILD_ROOT%{_bindir}/ejabberd2prosody
sed -e 's@;../?.lua@;%{_libdir}/%{name}/util/?.lua;%{_libdir}/%{name}/?.lua;@' \
  -i $RPM_BUILD_ROOT%{_bindir}/ejabberd2prosody
touch -c -r tools/ejabberd2prosody.lua $RPM_BUILD_ROOT%{_bindir}/ejabberd2prosody
install -p -m 0644 tools/erlparse.lua $RPM_BUILD_ROOT%{_libdir}/%{name}/util/

# Move certificates directory and symlink it
mv -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/certs/ $RPM_BUILD_ROOT%{_sysconfdir}/pki/%{name}/
ln -s ../pki/%{name}/ $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/certs

# Install systemd unit files and tmpfiles
install -D -p -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE4} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}
install -D -p -m 0644 %{SOURCE5} $RPM_BUILD_ROOT%{_tmpfilesdir}/%{name}.conf
install -D -p -m 0644 %{SOURCE6} $RPM_BUILD_ROOT%{_sysusersdir}/%{name}.conf
mkdir -p $RPM_BUILD_ROOT/run/%{name}/

# Keep configuration file timestamp
touch -c -r prosody.cfg.lua.dist.config $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/prosody.cfg.lua

# Install virtual host configuration
install -D -p -m 0644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/conf.d/localhost.cfg.lua
install -D -p -m 0644 %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/conf.d/example.com.cfg.lua

# Fix permissions for rpmlint
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/%{name}/util/*.so

# Fix incorrect end-of-line encoding
for file in doc/stanza.txt doc/session.txt doc/roster_format.txt; do
  sed -e 's/\r//g' ${file} > ${file}.eol
  touch -c -r ${file} ${file}.eol; mv -f ${file}.eol ${file}
done

%check
# Prepare test environment
mkdir -p tests/data/
cp -prf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/{*.cfg.lua,conf.d/} certs/ tests/
sed -e '/^log = {/,/}/d' -e '/^\(certificates\|pidfile\) =/d' -i tests/%{name}.cfg.lua  # Avoid 'duplicate option' warnings
echo 'certificates = "certs"' >> tests/%{name}.cfg.lua  # Relative to configuration
echo 'log = { "*console" }' >> tests/%{name}.cfg.lua  # Create no log files
echo 'pidfile = "'$(pwd)'/tests/prosody.pid"' >> tests/%{name}.cfg.lua  # Absolute path
echo 'unbound = { resolvconf = false, hoststxt = false }' >> tests/%{name}.cfg.lua  # Disable /etc/{resolv.conf,hosts} usage
echo 'admin_socket = "prosody.sock"' >> tests/%{name}.cfg.lua  # Avoid bind error for /run/prosody/prosody.sock
(. ./config.unix 2> /dev/null && sed -e "1s| lua\$| ${RUNWITH}|" -i %{name} %{name}ctl)
sed -e 's/^keysize=.*/keysize=4096/' -i tests/certs/{GNUmakefile,makefile}
make -C tests/certs localhost.crt
export LUA_PATH="$RPM_BUILD_ROOT%{_libdir}/%{name}/?.lua;;"
export LUA_CPATH="$RPM_BUILD_ROOT%{_libdir}/%{name}/?.so;;"
export PROSODY_CFGDIR="$(pwd)/tests"
export PROSODY_DATADIR="$(pwd)/tests/data"

# Run some common commands
./%{name}ctl about
./%{name}ctl start
./%{name}ctl status
for cnt in $(seq 1 5); do ss -lnpt | grep :5222 && ss -lnpt | grep :5269 && break || sleep 1; done
echo 'QUIT' | openssl s_client -connect localhost:5222 -starttls xmpp -name localhost -CAfile tests/certs/localhost.crt
echo 'QUIT' | openssl s_client -connect localhost:5269 -starttls xmpp-server -name localhost -CAfile tests/certs/localhost.crt
./%{name}ctl stop
echo -e 'Fish\nFish' | ./%{name}ctl adduser tux@localhost
ls -l tests/data/localhost/accounts/tux.dat
echo -e 'Penguin\nPenguin' | ./%{name}ctl passwd tux@localhost
./%{name}ctl deluser tux@localhost

%pre
%sysusers_create_compat %{SOURCE6}

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
  chmod 0644 %{sslcert}
fi

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYING
%doc AUTHORS CHANGES HACKERS README doc/*
%{_bindir}/%{name}
%{_bindir}/%{name}ctl
%{_bindir}/%{name}-migrator
%{_bindir}/ejabberd2prosody
%{_libdir}/%{name}/
%dir %attr(0750,root,%{name}) %{_sysconfdir}/pki/%{name}/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/pki/%{name}/*
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/*.cfg.lua
%dir %attr(0750,root,%{name}) %{_sysconfdir}/%{name}/conf.d/
%config(noreplace) %attr(0640,root,%{name}) %{_sysconfdir}/%{name}/conf.d/*.cfg.lua
%{_sysconfdir}/%{name}/certs
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/%{name}.conf
%{_tmpfilesdir}/%{name}.conf
%dir %attr(0755,%{name},%{name}) /run/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/lib/%{name}/
%dir %attr(0750,%{name},%{name}) %{_localstatedir}/log/%{name}/
%{_mandir}/man1/%{name}ctl.1*

%changelog
* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 0.12.4-6
- Rebuild for ICU 76

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 0.12.4-4
- Rebuild for ICU 74

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 13 2023 Robert Scheck <robert@fedoraproject.org> 0.12.4-1
- Upgrade to 0.12.4 (#2172143)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 0.12.3-2
- Rebuilt for ICU 73.2

* Fri Jun 02 2023 Robert Scheck <robert@fedoraproject.org> 0.12.3-1
- Upgrade to 0.12.3 (#2172143)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 0.12.2-2
- Rebuild for ICU 72

* Wed Dec 14 2022 Robert Scheck <robert@fedoraproject.org> 0.12.2-1
- Upgrade to 0.12.2 (#2153076)

* Sun Dec 11 2022 Robert Scheck <robert@fedoraproject.org> 0.12.1-1
- Upgrade to 0.12.1 (#2063943)

* Sun Aug 14 2022 Robert Scheck <robert@fedoraproject.org> 0.12.0-1
- Upgrade to 0.12.0 (#2063943)

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.11.13-4
- Rebuilt for ICU 71.1

* Sun Jul 31 2022 Robert Scheck <robert@fedoraproject.org> 0.11.13-3
- Added sysusers.d file to achieve user() and group() provides

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jan 25 2022 Robert Scheck <robert@fedoraproject.org> 0.11.13-1
- Upgrade to 0.11.13 (#2044449)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Robert Scheck <robert@fedoraproject.org> 0.11.12-1
- Upgrade to 0.11.12 (#2040350)

* Tue Dec 21 2021 Robert Scheck <robert@fedoraproject.org> 0.11.11-1
- Upgrade to 0.11.11 (#2034434)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.11.10-2
- Rebuilt with OpenSSL 3.0.0

* Tue Aug 03 2021 Robert Scheck <robert@fedoraproject.org> 0.11.10-1
- Upgrade to 0.11.10 (#1989535)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May 20 2021 Pete Walter <pwalter@fedoraproject.org> - 0.11.9-3
- Rebuild for ICU 69

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 0.11.9-2
- Rebuild for ICU 69

* Thu May 13 2021 Robert Scheck <robert@fedoraproject.org> 0.11.9-1
- Upgrade to 0.11.9 (#1960244, #1960332, #1960335, #1960340,
  #1960343, #1960349)

* Fri Apr 30 2021 Robert Scheck <robert@fedoraproject.org> 0.11.8-4
- Added upstream patch to avoid '-Wl,--as-needed' removing linking
  to libpthread when building with current libicu (#1954178)

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.11.8-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Fri Feb 26 2021 Robert Scheck <robert@fedoraproject.org> 0.11.8-2
- Added upstream patch to unbreak Lua 5.4 support (#1933063)
- Added %%check to run some common commands (as a small testsuite)

* Mon Feb 15 2021 Robert Scheck <robert@fedoraproject.org> 0.11.8-1
- Upgrade to 0.11.8 (#1928951)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 08 2020 Robert Scheck <robert@fedoraproject.org> 0.11.7-2
- Added upstream patches for better Lua 5.4 support (#1886456)

* Thu Oct 01 2020 Robert Scheck <robert@fedoraproject.org> 0.11.7-1
- Upgrade to 0.11.7 (#1877424)

* Wed Sep 09 2020 Robert Scheck <robert@fedoraproject.org> 0.11.6-1
- Upgrade to 0.11.6 (#1877424)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Tom Callaway <spot@fedoraproject.org> - 0.11.5-3
- fix build with lua 5.4

* Tue Jun 30 2020 Björn Esser <besser82@fedoraproject.org> - 0.11.5-2
- Rebuilt for Lua 5.4

* Mon Apr 06 2020 Robert Scheck <robert@fedoraproject.org> 0.11.5-1
- Upgrade to 0.11.5 (#1816855)

* Mon Feb 10 2020 Robert Scheck <robert@fedoraproject.org> 0.11.4-1
- Upgrade to 0.11.4 (#1792635)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 30 2019 Robert Scheck <robert@fedoraproject.org> 0.11.3-1
- Upgrade to 0.11.3 (#1756953)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Robert Scheck <robert@fedoraproject.org> 0.11.2-1
- Upgrade to 0.11.2

* Thu Nov 29 2018 Robert Scheck <robert@fedoraproject.org> 0.11.1-1
- Upgrade to 0.11.1

* Mon Nov 19 2018 Robert Scheck <robert@fedoraproject.org> 0.11.0-1
- Upgrade to 0.11.0

* Sun Aug 19 2018 Robert Scheck <robert@fedoraproject.org> 0.10.2-3
- Don't attempt to reload during logrotate if prosody is stopped

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Robert Scheck <robert@fedoraproject.org> 0.10.2-1
- Upgrade to 0.10.2 (#1584801)
- Changed log rotation from weekly/52 to local system defaults

* Tue May 15 2018 Robert Scheck <robert@fedoraproject.org> 0.10.1-1
- Upgrade to 0.10.1 (#1578371)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 27 2017 Robert Scheck <robert@fedoraproject.org> 0.10.0-1
- Upgrade to 0.10.0 (#1497877)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Robert Scheck <robert@fedoraproject.org> 0.9.12-1
- Upgrade to 0.9.12 (#1412102)

* Mon Nov 07 2016 Robert Scheck <robert@fedoraproject.org> 0.9.11-1
- Upgrade to 0.9.11 (#1391802)

* Sun Apr 17 2016 Robert Scheck <robert@fedoraproject.org> 0.9.10-3
- Added runtime requirement to %%{_bindir}/openssl (#1319227)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 27 2016 Robert Scheck <robert@fedoraproject.org> 0.9.10-1
- Upgrade to 0.9.10 (#1302463)

* Tue Jan 12 2016 Robert Scheck <robert@fedoraproject.org> 0.9.9-2
- Added upstream patch to open /dev/urandom read-only

* Fri Jan 08 2016 Robert Scheck <robert@fedoraproject.org> 0.9.9-1
- Upgrade to 0.9.9 (#1296983, #1296984)

* Sun Sep 27 2015 Robert Scheck <robert@fedoraproject.org> 0.9.8-6
- Fixed shebang for ejabberd2prosody
- Backported support for IPv6 DNS servers (#1256677)

* Sun Aug 23 2015 Robert Scheck <robert@fedoraproject.org> 0.9.8-5
- Start after network-online.target not network.target (#1256062)

* Wed Jul 15 2015 Robert Scheck <robert@fedoraproject.org> 0.9.8-4
- Change default CA paths to /etc/pki/tls/certs(/ca-bundle.crt)

* Wed Jul 01 2015 Robert Scheck <robert@fedoraproject.org> 0.9.8-3
- Fixed the wrong logrotate configuration to not use a wildcard

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 18 2015 Robert Scheck <robert@fedoraproject.org> 0.9.8-1
- Upgrade to 0.9.8 (#1152126)

* Sat Feb 14 2015 Robert Scheck <robert@fedoraproject.org> 0.9.7-1
- Upgrade to 0.9.7 (#985563, #1152126)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jun 03 2014 Jan Kaluza <jkaluza@redhat.com> - 0.9.4-2
- add missing lua-socket-compat dependency

* Fri May 30 2014 Jan Kaluza <jkaluza@redhat.com> - 0.9.4-1
- update to version 0.9.4
- build with luajit

* Wed Sep 11 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.1-1
- Update to 0.9.1

* Thu Aug 22 2013 Matěj Cepl <mcepl@redhat.com> - 0.9.0-1
- Final upstream release.

* Wed Aug 07 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.0-0.5.rc5
- Update to 0.9.0rc5

* Fri Jun 21 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.0-0.4.rc4
- Update to 0.9.0rc4

* Fri Jun 21 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.0-0.3.rc3
- Update to 0.9.0rc3

* Fri Jun 07 2013 Johan Cwiklinski <johan AT x-tnd DOT be> - 0.9.0-0.2.rc2
- Update to 0.9.0rc2

* Wed May 15 2013 Tom Callaway <spot@fedoraproject.org> - 0.9.0-0.1.beta1
- update to 0.9.0beta1, rebuild for lua 5.2

* Sat Apr 27 2013 Robert Scheck <robert@fedoraproject.org> - 0.8.2-9
- Apply wise permissions to %%{_sysconfdir}/%%{name} (#955384)
- Apply wise permissions to default SSL certificates (#955380)
- Do not ship %%{_sysconfdir}/%%{name}/certs by default (#955385)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Sep 27 2012 Johan Cwiklinski <johan At x-tnd DOt be> 0.8.2-7
- Use systemd-rpm macros, bz #850282

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 07 2012 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.2-5
- Missing rhel %%ifs
- Change the way SSL certificate is generated

* Sun May 06 2012 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.2-4
- ghost %%{_localstatedir}/run/%%{name}

* Sun May 06 2012 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.2-3
- Add missing requires
- Add rhel %%ifs

* Mon Mar 05 2012 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.2-2
- Switch to systemd for Fedora >= 15, keep sysv for EPEL builds
- Remove some macros that should not be used

* Thu Jun 23 2011 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.2-1.trashy
- 0.8.2

* Tue Jun 7 2011 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.1-1.trashy
- 0.8.1

* Sun May 8 2011 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.0-3.trashy
- tmpfiles.d configuration for F-15

* Sat Apr 16 2011 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.0-2.trashy
- Now requires lua-dbi

* Fri Apr 8 2011 Johan Cwiklinski <johan AT x-tnd DOT be> 0.8.0-1.trashy
- 0.8.0

* Sun Jan 23 2011 Johan Cwiklinski <johan AT x-tnd DOT be> 0.7.0-4.trashy
- Redefine _initddir and _sharedstatedir marcos for EL-5

* Sat Dec 11 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 0.7.0-3
- Apply ssl patch before sed on libdir; to avoid a patch context issue
  building on i686

* Sat Sep 11 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 0.7.0-2
- No longer ships default ssl certificates, generates one at install

* Wed Jul 14 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 0.7.0-1
- Update to 0.7.0

* Wed Apr 28 2010 Johan Cwiklinski <johan AT x-tnd DOT be> 0.6.2-1
- Update to 0.6.2

* Thu Dec 31 2009 Johan Cwiklinski <johan AT x-tnd DOT be> 0.6.1-1
- Initial packaging
