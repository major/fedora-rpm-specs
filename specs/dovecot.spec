%global __provides_exclude_from %{_docdir}
%global __requires_exclude_from %{_docdir}

Summary: Secure imap and pop3 server
Name: dovecot
Epoch: 1
Version: 2.4.2
%global prever %{nil}
Release: 5%{?dist}
#dovecot itself is MIT, a few sources are PD, pigeonhole is LGPLv2
License: MIT AND LGPL-2.1-only

URL: https://www.dovecot.org/
Source: https://www.dovecot.org/releases/2.4/%{name}-%{version}%{?prever}.tar.gz
Source1: dovecot.init
Source2: dovecot.pam
%global pigeonholever %{version}%{?prever}
Source8: https://pigeonhole.dovecot.org/releases/2.4/dovecot-pigeonhole-%{pigeonholever}.tar.gz
Source9: dovecot.sysconfig
Source10: dovecot.tmpfilesd

#our own
Source14: dovecot.conf.5
Source15: prestartscript
Source16: dovecot.sysusers

# 3x Fedora/RHEL specific
Patch1: dovecot-2.0-defaultconfig.patch
Patch2: dovecot-1.0.beta2-mkcert-permissions.patch
Patch3: dovecot-1.0.rc7-mkcert-paths.patch

#wait for network
Patch6: dovecot-2.1.10-waitonline.patch

Patch8: dovecot-2.2.20-initbysystemd.patch
Patch9: dovecot-2.2.22-systemd_w_protectsystem.patch
Patch15: dovecot-2.3.11-bigkey.patch

# do not use own implementation of HMAC, use OpenSSL for certification purposes
# not sent upstream as proper fix would use dovecot's lib-dcrypt but it introduces
# hard to break circular dependency between lib and lib-dcrypt
Patch16: dovecot-2.4.1-opensslhmac3.patch

# FTBFS
Patch17: dovecot-2.3.15-fixvalcond.patch
Patch18: dovecot-2.3.15-valbasherr.patch

# Fedora/RHEL specific, drop OTP which uses SHA1 so we dont use SHA1 for crypto purposes
Patch23: dovecot-2.4.1-nolibotp.patch
Patch24: dovecot-2.4.2-fixbuild.patch
# temporary workaround for s390x build test failure
# https://dovecot.org/mailman3/archives/list/dovecot@dovecot.org/thread/FZBVU55TK5332SMZSSDNWIVJCWGUAJQS/
Patch25: dovecot-2.4.2-ftbfs-workaround.patch

BuildRequires: gcc, gcc-c++, openssl-devel, pam-devel, zlib-devel, bzip2-devel, libcap-devel
BuildRequires: libtool, autoconf, automake, pkgconfig
BuildRequires: sqlite-devel
BuildRequires: libpq-devel
BuildRequires: mariadb-connector-c-devel
BuildRequires: libxcrypt-devel
BuildRequires: openldap-devel
BuildRequires: krb5-devel
BuildRequires: quota-devel
BuildRequires: xz-devel
BuildRequires: lz4-devel
BuildRequires: libzstd-devel
%if %{?rhel}0 == 0
BuildRequires: libsodium-devel
BuildRequires: lua-devel
BuildRequires: lua-json
%endif
BuildRequires: libicu-devel
%if %{?rhel}0 == 0
BuildRequires: libstemmer-devel
BuildRequires: xapian-core-devel
%endif
BuildRequires: multilib-rpm-config
BuildRequires: flex, bison
BuildRequires: perl-version
BuildRequires: systemd-devel
BuildRequires: systemd-rpm-macros

# gettext-devel is needed for running autoconf because of the
# presence of AM_ICONV
BuildRequires: gettext-devel

# Explicit Runtime Requirements for executalbe
Requires: openssl >= 0.9.7f-4

# Package includes an initscript service file, needs to require initscripts package
Requires(pre): shadow-utils
Requires: systemd
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%global ssldir %{_sysconfdir}/pki/%{name}

BuildRequires: libcurl-devel expat-devel
BuildRequires: make

%if 0%{?fedora} > 39
# as per https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
%endif

%global restart_flag /run/%{name}/%{name}-restart-after-rpm-install

%description
Dovecot is an IMAP server for Linux/UNIX-like systems, written with security 
primarily in mind.  It also contains a small POP3 server.  It supports mail 
in either of maildir or mbox formats.

The SQL drivers and authentication plug-ins are in their subpackages.

%package pigeonhole
Requires: %{name} = %{epoch}:%{version}-%{release}
Summary: Sieve and managesieve plug-in for dovecot
License: MIT AND LGPL-2.1-only

%description pigeonhole
This package provides sieve and managesieve plug-in for dovecot LDA.

%package pgsql
Requires: %{name} = %{epoch}:%{version}-%{release}
Summary: Postgres SQL back end for dovecot
%description pgsql
This package provides the Postgres SQL back end for dovecot-auth etc.

%package mysql
Requires: %{name} = %{epoch}:%{version}-%{release}
Summary: MySQL back end for dovecot
%description mysql
This package provides the MySQL back end for dovecot-auth etc.

%package devel
Requires: %{name} = %{epoch}:%{version}-%{release}
Summary: Development files for dovecot
%description devel
This package provides the development files for dovecot.

%prep
%setup -q -n %{name}-%{version}%{?prever} -a 8

# standardize name, so we don't have to update patches and scripts
mv dovecot-pigeonhole-%{pigeonholever} dovecot-pigeonhole

%patch -P 1 -p2 -b .default-settings
%patch -P 2 -p1 -b .mkcert-permissions
%patch -P 3 -p1 -b .mkcert-paths
%patch -P 6 -p2 -b .waitonline
%patch -P 8 -p2 -b .initbysystemd
%patch -P 9 -p1 -b .systemd_w_protectsystem
%patch -P 15 -p1 -b .bigkey
%patch -P 16 -p2 -b .opensslhmac3
%patch -P 17 -p2 -b .fixvalcond
%patch -P 18 -p1 -b .valbasherr
%patch -P 23 -p2 -b .nolibotp
%patch -P 24 -p1 -b .fixbuild
%patch -P 25 -p1 -b .ftbfs-workaround
cp run-test-valgrind.supp dovecot-pigeonhole/
# valgrind would fail with shell wrapper
echo "testsuite" >dovecot-pigeonhole/run-test-valgrind.exclude

# drop OTP which uses SHA1 so we dont use SHA1 for crypto purposes
#rm -rf src/lib-otp
echo >src/auth/mech-otp-common.c
echo >src/auth/mech-otp-common.h
echo >src/auth/mech-otp.c
echo >src/lib-auth/password-scheme-otp.c
echo >src/lib-sasl/sasl-server-mech-otp.c
echo >src/lib-sasl/dsasl-client-mech-otp.c
pushd src/lib-otp
for f in *.c *.h
do
  echo >$f
done
popd

%build
#required for fdpass.c line 125,190: dereferencing type-punned pointer will break strict-aliasing rules
%global _hardened_build 1
export CFLAGS="%{__global_cflags} -fno-strict-aliasing -fstack-reuse=none"
export LDFLAGS="-Wl,-z,now -Wl,-z,relro %{?__global_ldflags}"
mkdir -p m4
if [ -d /usr/share/gettext/m4 ]
then
  #required for aarch64 support
  # point to gettext explicitely, autoreconf cant find iconv.m4 otherwise
  autoreconf -I . -I /usr/share/gettext/m4 
else
  autoreconf -I . -fiv #required for aarch64 support
fi

%configure                       \
    INSTALL_DATA="install -c -p -m644" \
    --with-rundir=%{_rundir}/%{name}   \
    --with-systemd               \
    --docdir=%{_docdir}/%{name}  \
    --disable-static             \
    --disable-rpath              \
    --with-nss                   \
    --with-shadow                \
    --with-pam                   \
    --with-gssapi=plugin         \
    --with-ldap=plugin           \
    --with-sql=plugin            \
    --with-pgsql                 \
    --with-mysql                 \
    --with-sqlite                \
    --with-zlib                  \
    --with-zstd                  \
    --with-libcap                \
    --with-icu                   \
%if %{?rhel}0 == 0
    --with-libstemmer            \
    --with-flatcurve             \
    --with-lua=plugin            \
%else
    --without-libstemmer         \
    --without-lua                \
%endif
    --without-lucene             \
    --without-exttextcat         \
    --with-ssl=openssl           \
    --with-ssldir=%{ssldir}      \
    --with-solr                  \
    --with-docs                  \
    systemdsystemunitdir=%{_unitdir}

sed -i 's|/etc/ssl|/etc/pki/dovecot|' doc/mkcert.sh # doc/example-config/conf.d/10-ssl.conf

%make_build

#pigeonhole
pushd dovecot-pigeonhole

# required for snapshot
[ -f configure ] || autoreconf -fiv
[ -f ChangeLog ] || echo "Pigeonhole ChangeLog is not available, yet" >ChangeLog

%configure                             \
    INSTALL_DATA="install -c -p -m644" \
    --disable-static                   \
    --with-dovecot=../                 \
    --without-unfinished-features

%make_build
popd

%install
rm -rf $RPM_BUILD_ROOT

%make_install

# move doc dir back to build dir so doc macro in files section can use it
mv $RPM_BUILD_ROOT/%{_docdir}/%{name} %{_builddir}/%{name}-%{version}%{?prever}/docinstall

# fix multilib issues
%multilib_fix_c_header --file %{_includedir}/dovecot/config.h

pushd dovecot-pigeonhole
%make_install

mv $RPM_BUILD_ROOT/%{_docdir}/%{name} $RPM_BUILD_ROOT/%{_docdir}/%{name}-pigeonhole

install -m 644 AUTHORS ChangeLog COPYING COPYING.LGPL INSTALL NEWS README $RPM_BUILD_ROOT/%{_docdir}/%{name}-pigeonhole
popd

install -p -D -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/dovecot

#install man pages
install -p -D -m 644 %{SOURCE14} $RPM_BUILD_ROOT%{_mandir}/man5/dovecot.conf.5

#install waitonline script
install -p -D -m 755 %{SOURCE15} $RPM_BUILD_ROOT%{_libexecdir}/dovecot/prestartscript

install -p -D -m 0644 %{SOURCE16} $RPM_BUILD_ROOT%{_sysusersdir}/dovecot.conf

# generate ghost .pem files
mkdir -p $RPM_BUILD_ROOT%{ssldir}/certs
mkdir -p $RPM_BUILD_ROOT%{ssldir}/private
touch $RPM_BUILD_ROOT%{ssldir}/certs/dovecot.pem
chmod 600 $RPM_BUILD_ROOT%{ssldir}/certs/dovecot.pem
touch $RPM_BUILD_ROOT%{ssldir}/private/dovecot.pem
chmod 600 $RPM_BUILD_ROOT%{ssldir}/private/dovecot.pem

install -p -D -m 644 %{SOURCE10} $RPM_BUILD_ROOT%{_tmpfilesdir}/dovecot.conf

mkdir -p $RPM_BUILD_ROOT/run/dovecot/{login,empty,token-login}

# Install dovecot configuration and dovecot-openssl.cnf
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/dovecot/conf.d
install -p -m 644 $RPM_BUILD_ROOT/%{_docdir}/%{name}-pigeonhole/example-config/conf.d/*.conf $RPM_BUILD_ROOT%{_sysconfdir}/dovecot/conf.d
install -p -m 644 $RPM_BUILD_ROOT/%{_docdir}/%{name}-pigeonhole/example-config/conf.d/*.conf.ext $RPM_BUILD_ROOT%{_sysconfdir}/dovecot/conf.d ||:
install -p -m 644 doc/dovecot-openssl.cnf $RPM_BUILD_ROOT%{ssldir}/dovecot-openssl.cnf

install -p -m755 doc/mkcert.sh $RPM_BUILD_ROOT%{_libexecdir}/%{name}/mkcert.sh

mkdir -p $RPM_BUILD_ROOT/var/lib/dovecot

#remove the libtool archives
find $RPM_BUILD_ROOT%{_libdir}/%{name}/ -name '*.la' | xargs rm -f

#remove what we don't want
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/dovecot/README
pushd docinstall
rm -f securecoding.txt thread-refs.txt
popd


%pre
%if 0%{?fedora} < 42
#dovecot uid and gid are reserved, see /usr/share/doc/setup-*/uidgid 
%sysusers_create_compat %{SOURCE16}
%endif

# do not let dovecot run during upgrade rhbz#134325
if [ "$1" = "2" ]; then
  rm -f %restart_flag
  /bin/systemctl is-active %{name}.service >/dev/null 2>&1 && touch %restart_flag ||:
  /bin/systemctl stop %{name}.service >/dev/null 2>&1
fi

%post
if [ $1 -eq 1 ]
then
  %systemd_post dovecot.service
fi

install -d -m 0755 -g dovecot -d /run/dovecot
install -d -m 0755 -d /run/dovecot/empty
install -d -m 0750 -g dovenull -d /run/dovecot/login
install -d -m 0750 -g dovenull -d /run/dovecot/token-login
[ -x /sbin/restorecon ] && /sbin/restorecon -R /run/dovecot ||:

%preun
if [ $1 = 0 ]; then
        /bin/systemctl disable dovecot.service dovecot.socket >/dev/null 2>&1 || :
        /bin/systemctl stop dovecot.service dovecot.socket >/dev/null 2>&1 || :
    rm -rf /run/dovecot
fi

%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

if [ "$1" -ge "1" -a -e %restart_flag ]; then
    /bin/systemctl start dovecot.service >/dev/null 2>&1 || :
rm -f %restart_flag
fi

%posttrans
# dovecot should be started again in %%postun, but it's not executed on reinstall
# if it was already started, restart_flag won't be here, so it's ok to test it again
if [ -e %restart_flag ]; then
    /bin/systemctl start dovecot.service >/dev/null 2>&1 || :
rm -f %restart_flag
fi

%check
%ifnarch aarch64
# some aarch64 tests timeout, skip for now
make check
cd dovecot-pigeonhole
# FIXME: make check will fail as it requires doveconf to be already installed at /usr/bin/doveconf
make check ||:
%endif

%files
%doc docinstall/* AUTHORS ChangeLog COPYING COPYING.LGPL COPYING.MIT INSTALL.md NEWS README.md SECURITY.md
%{_sbindir}/dovecot

%{_bindir}/doveadm
%{_bindir}/doveconf
%{_bindir}/dovecot-sysreport

%_tmpfilesdir/dovecot.conf
%{_sysusersdir}/dovecot.conf
%{_unitdir}/dovecot.service
%{_unitdir}/dovecot-init.service
%{_unitdir}/dovecot.socket

%dir %{_sysconfdir}/dovecot
%dir %{_sysconfdir}/dovecot/conf.d
%config(noreplace) %{_sysconfdir}/dovecot/dovecot.conf
%config(noreplace) %{_sysconfdir}/pam.d/dovecot
%config(noreplace) %{ssldir}/dovecot-openssl.cnf

%dir %{ssldir}
%dir %{ssldir}/certs
%dir %{ssldir}/private
%attr(0600,root,root) %ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{ssldir}/certs/dovecot.pem
%attr(0600,root,root) %ghost %config(missingok,noreplace) %verify(not md5 size mtime) %{ssldir}/private/dovecot.pem

%dir %{_libdir}/dovecot
%dir %{_libdir}/dovecot/auth
%dir %{_libdir}/dovecot/dict
%{_libdir}/dovecot/doveadm
%exclude %{_libdir}/dovecot/doveadm/*sieve*
%{_libdir}/dovecot/*.so.*
#these (*.so files) are plugins, not devel files
%{_libdir}/dovecot/*_plugin.so
%exclude %{_libdir}/dovecot/*_sieve_plugin.so
%{_libdir}/dovecot/auth/libauthdb_imap.so
%{_libdir}/dovecot/auth/libauthdb_ldap.so
%if %{?rhel}0 == 0
%{_libdir}/dovecot/auth/libauthdb_lua.so
%endif
%{_libdir}/dovecot/auth/libmech_gssapi.so
%{_libdir}/dovecot/auth/libmech_gss_spnego.so
%{_libdir}/dovecot/auth/libdriver_sqlite.so
%{_libdir}/dovecot/dict/libdriver_sqlite.so
%{_libdir}/dovecot/dict/libdict_ldap.so
%{_libdir}/dovecot/libdriver_sqlite.so
%{_libdir}/dovecot/libssl_iostream_openssl.so
%{_libdir}/dovecot/libfs_compress.so
%{_libdir}/dovecot/libfs_crypt.so
%{_libdir}/dovecot/libdcrypt_openssl.so
%{_libdir}/dovecot//var_expand_crypt.so

%dir %{_libdir}/dovecot/settings

%{_libexecdir}/%{name}
%exclude %{_libexecdir}/%{name}/managesieve*

%dir %attr(0755,root,dovecot) %ghost /run/dovecot
%attr(0750,root,dovenull) %ghost /run/dovecot/login
%attr(0750,root,dovenull) %ghost /run/dovecot/token-login
%attr(0755,root,root) %ghost /run/dovecot/empty

%attr(0750,dovecot,dovecot) /var/lib/dovecot

%{_datadir}/%{name}

%{_mandir}/man1/deliver.1*
%{_mandir}/man1/doveadm*.1*
%{_mandir}/man1/doveconf.1*
%{_mandir}/man1/dovecot*.1*
%{_mandir}/man5/dovecot.conf.5*
%{_mandir}/man7/doveadm-search-query.7*

%files devel
%{_includedir}/dovecot
%{_datadir}/aclocal/dovecot*.m4
%{_libdir}/dovecot/libdovecot*.so
%{_libdir}/dovecot/dovecot-config

%files pigeonhole
%{_bindir}/sieve-dump
%{_bindir}/sieve-filter
%{_bindir}/sieve-test
%{_bindir}/sievec
%config(noreplace) %{_sysconfdir}/dovecot/conf.d/20-managesieve.conf
%config(noreplace) %{_sysconfdir}/dovecot/conf.d/90-sieve.conf
%config(noreplace) %{_sysconfdir}/dovecot/conf.d/90-sieve-extprograms.conf

%{_docdir}/%{name}-pigeonhole

%{_libexecdir}/%{name}/managesieve
%{_libexecdir}/%{name}/managesieve-login

%{_libdir}/dovecot/doveadm/*sieve*
%{_libdir}/dovecot/*_sieve_plugin.so
%{_libdir}/dovecot/settings/libmanagesieve_*.so
%{_libdir}/dovecot/settings/libpigeonhole_*.so
%{_libdir}/dovecot/sieve/

%{_mandir}/man1/sieve-dump.1*
%{_mandir}/man1/sieve-filter.1*
%{_mandir}/man1/sieve-test.1*
%{_mandir}/man1/sievec.1*
%{_mandir}/man1/sieved.1*
%{_mandir}/man7/pigeonhole.7*

%files mysql
%{_libdir}/%{name}/libdriver_mysql.so
%{_libdir}/%{name}/auth/libdriver_mysql.so
%{_libdir}/%{name}/dict/libdriver_mysql.so

%files pgsql
%{_libdir}/%{name}/libdriver_pgsql.so
%{_libdir}/%{name}/auth/libdriver_pgsql.so
%{_libdir}/%{name}/dict/libdriver_pgsql.so

%changelog
* Tue Feb 03 2026 Michal Hlavinka <mhlavink@redhat.com> - 1:2.4.2-5
- add workaround for test failure

* Tue Jan 27 2026 Michal Hlavinka <mhlavink@redhat.com> - 1:2.4.2-4
- add /var/lib/dovecot to tmpfiles for image mode

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Sun Nov 30 2025 Michal Hlavinka <mhlavink@redhat.com> - 1:2.4.2-1
- updated to 2.4.2 (#2411846)

* Wed Nov 05 2025 Michal Hlavinka <mhlavink@redhat.com> - 1:2.4.1-8
- update patch for CVE-2025-30189

* Wed Oct 15 2025 Michal Hlavinka <mhlavink@redhat.com> - 1:2.4.1-7
- enable fts flatcurve

* Thu Oct 09 2025 Michal Hlavinka <mhlavink@redhat.com> - 1:2.4.1-6
- fix CVE-2025-30189: users would end up overwriting each other in cache (rhbz#2402122)

* Wed Aug 06 2025 František Zatloukal <fzatlouk@redhat.com> - 1:2.4.1-5
- Rebuilt for icu 77.1

* Wed Jul 30 2025 Michal Hlavinka <mhlavink@redhat.com> - 1:2.4.1-4
- fix compatibility with latest openssl (#2383209)

* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jun 24 2025 Michal Hlavinka <mhlavink@redhat.com> - 1:2.4.1-2
- fix dovecot 2.4 gssapi regression (rhbz#2374419)

* Tue Jun 03 2025 Michal Hlavinka <mhlavink@redhat.com> - 1:2.4.1-1
- updated to 2.4.1 release
- note: configuration is incompatible with 2.3.x version
- trim changelog
- revert previous change, only if-guard it

* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:2.3.21.1-6
- Drop call to %%sysusers_create_compat

* Wed Feb 05 2025 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.21.1-5
- fix sysusers config file name

* Wed Jan 29 2025 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.21.1-4
- fix ftbfs

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.21.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 02 2024 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.21.1-2
- pigeonhole updated to 0.5.21.1

* Mon Aug 19 2024 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.21.1-1
- updated to 2.3.21.1(2304907)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.21-8
- fix sieve crash when there are two missing optional scripts
- Do not use deprecated OpenSSL v3 ENGINE API
- Drop dependency on libstemmer on RHEL

* Tue Mar 26 2024 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.21-7
- drop i686 build as per https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 1:2.3.21-6
- Rebuild for ICU 74

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 24 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.21-3
- drop lucene to reduce dependency, use solr for fts instead

* Thu Oct 05 2023 Remi Collet <remi@remirepo.net> - 1:2.3.21-2
- rebuild for new libsodium

* Mon Sep 18 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.21-1
- updated to 2.3.21(2239134)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 1:2.3.20-5
- Rebuilt for ICU 73.2

* Wed Apr 26 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.20-4
- update license tag format (SPDX migration) for https://fedoraproject.org/wiki/Changes/SPDX_Licenses_Phase_1

* Tue Feb 14 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.20-3
- drop SHA1 OTP

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.20-1
- updated to 2.3.20, pigeonhole to 0.5.20

* Mon Jan 02 2023 Florian Weimer <fweimer@redhat.com> - 1:2.3.19.1-8
- Port configure script to C99

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 1:2.3.19.1-7
- Rebuild for ICU 72

* Tue Nov 08 2022 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.19.1-6
- use Wants=network-online.target instead of preexec nm-online (#2095949)

* Tue Oct 11 2022 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.19.1-5
- build with lua support (#2132420)

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 1:2.3.19.1-4
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.19.1-2
- fix possible privilege escalation when similar master and non-master passdbs are used

* Mon Jun 20 2022 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.19.1-1
- updated to 2.3.19.1

* Mon May 30 2022 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.19-1
- updated to 2.3.19, pigeonhole to 0.5.19

* Wed Feb 09 2022 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.18-1
- updated to 2.3.18, pigeonhole to 0.5.18

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 07 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.17.1-1
- dovecot updated to 2.3.17.1, pigeonhole to 0.5.17.1
- dsync: Add back accidentically removed parameters.
- lib-ssl-iostream: Fix assert-crash when OpenSSL returned syscall error
  without errno.
- dovecot, managesieve and sieve-tool failed to run if ssl_ca was too large.

* Tue Nov 02 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.17-1
- dovecot updated to 2.3.17, pigeonhole to 0.5.17

* Tue Sep 28 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.16-4
- reenable LTO

* Mon Sep 27 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.16-3
- fix OpenSSLv3 issues 2005884

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1:2.3.16-2
- Rebuilt with OpenSSL 3.0.0

* Fri Aug 20 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.16-1
- dovecot updated to 2.3.16, pigeonhole to 0.5.16
- fixes several regressions

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.15-1
- dovecot updated to 2.3.15, pigeonhole updated to 0.5.15
- CVE-2021-29157: Dovecot does not correctly escape kid and azp fields in
  JWT tokens. This may be used to supply attacker controlled keys to
  validate tokens, if attacker has local access.
- CVE-2021-33515: On-path attacker could have injected plaintext commands
  before STARTTLS negotiation that would be executed after STARTTLS
  finished with the client.
- Add TSLv1.3 support to min_protocols.
- Allow configuring ssl_cipher_suites. (for TLSv1.3+)

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 1:2.3.14-4
- Rebuild for ICU 69

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 1:2.3.14-3
- Rebuild for ICU 69

* Mon May 10 2021 Jeff Law <jlaw@tachyum.com> - 1:2.3.14-2
- Re-enable LTO

* Mon Mar 22 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.14-1
- dovecot updated to 2.3.14, pigeonhole to 0.5.14
- use OpenSSL's implementation of HMAC
- Remove autocreate, expire, snarf and mail-filter plugins.
- Remove cydir storage driver.
- Remove XZ/LZMA write support. Read support will be removed in future release.

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 1:2.3.13-7
- rebuild for libpq ABI fix rhbz#1908268

* Mon Feb 01 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.13-6
- use make macros

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.13-4
- fix multilib issues

* Mon Jan 18 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.13-3
- bump release and rebuild

* Thu Jan 07 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.13-2
- fix rundir location

* Wed Jan 06 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.13-1
- fix release number

* Mon Jan 04 2021 Michal Hlavinka <mhlavink@redhat.com> - 1:2.3.13-0
- dovecot updated to 2.3.13, pigeonhole to 0.5.13
- CVE-2020-24386: Specially crafted command can cause IMAP hibernate to
  allow logged in user to access other people's emails and filesystem
  information.
- Metric filter and global event filter variable syntax changed to a
  SQL-like format. 
- auth: Added new aliases for %%{variables}. Usage of the old ones is
  possible, but discouraged.
- auth: Removed RPA auth mechanism, SKEY auth mechanism, NTLM auth
  mechanism and related password schemes.
- auth: Removed passdb-sia, passdb-vpopmail and userdb-vpopmail.
- auth: Removed postfix postmap socket
