%global _hardened_build 1

Summary: DNSSEC key and zone management software
Name: opendnssec
Version: 2.1.14
Release: 2%{?dist}
License: BSD-2-Clause
Url: http://www.opendnssec.org/
Source0: https://dist.opendnssec.org/source/%{?prever:testing/}%{name}-%{version}%{?prever}.tar.gz
Source10: https://dist.opendnssec.org/source/%{?prever:testing/}%{name}-%{version}%{?prever}.tar.gz.sig
Source1: ods-enforcerd.service
Source2: ods-signerd.service
Source3: ods.sysconfig
Source4: conf.xml
Source5: tmpfiles-opendnssec.conf
Source6: opendnssec.cron
Source7: opendnssec-2.1.sqlite_convert.sql
Source8: opendnssec-2.1.sqlite_rpmversion.sql
Source9: %{name}-sysusers.conf
Patch1: 0001-Pass-right-remaining-buffer-size-in-hsm_hex_unparse-.patch
Patch2: opendnssec-configure-c99.patch
Patch3: opendnssec-2.1.14rc1-gcc14.patch
Patch4: opendnssec-c99-2.patch
Patch5: opendnssec-implicit-declarations.patch

Requires: opencryptoki, softhsm >= 2.5.0 , systemd-units
Requires: libxml2, libxslt sqlite
BuildRequires: make
BuildRequires:  gcc
BuildRequires: ldns-devel >= 1.6.12, sqlite-devel >= 3.0.0, openssl-devel
BuildRequires: libxml2-devel CUnit-devel, doxygen
# It tests for pkill/killall and would use /bin/false if not found
BuildRequires: procps-ng
BuildRequires: perl-interpreter
BuildRequires: libmicrohttpd-devel jansson-devel libyaml-devel

BuildRequires: systemd-units
Requires(pre): shadow-utils
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%if 0%{?prever:1}
# For building development snapshots
Buildrequires: autoconf, automake, libtool
%ifarch %{java_arches}
Buildrequires: java
%endif
%endif

%description
OpenDNSSEC was created as an open-source turn-key solution for DNSSEC.
It secures zone data just before it is published in an authoritative
name server. It requires a PKCS#11 crypto module library, such as softhsm

%prep
%setup -q -n %{name}-%{version}%{?prever}
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

# Prevent re-running autoconf.
touch -r aclocal.m4 configure* m4/*

# bump default policy ZSK keysize to 2048
sed -i "s/1024/2048/" conf/kasp.xml.in

%build
export LDFLAGS="-Wl,-z,relro,-z,now -pie -specs=/usr/lib/rpm/redhat/redhat-hardened-ld"
export CFLAGS="$RPM_OPT_FLAGS -fPIE -pie -Wextra -Wformat -Wformat-nonliteral -Wformat-security"
export CXXFLAGS="$RPM_OPT_FLAGS -fPIE -pie -Wformat-nonliteral -Wformat-security"
%if 0%{?prever:1}
# for development snapshots
autoreconf
%endif
%configure --with-ldns=%{_libdir}
%make_build

%check
# Requires sample db not shipped with upstream
# make check

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}%{_localstatedir}/opendnssec/{tmp,signed,signconf,enforcer}
install -d -m 0755 %{buildroot}%{_initrddir} %{buildroot}%{_sysconfdir}/cron.d/
install -m 0644 %{SOURCE6} %{buildroot}/%{_sysconfdir}/cron.d/opendnssec
rm -f %{buildroot}/%{_sysconfdir}/opendnssec/*.sample
install -d -m 0755 %{buildroot}/%{_sysconfdir}/sysconfig
install -d -m 0755 %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/
install -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/
install -m 0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/sysconfig/ods
install -m 0644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/opendnssec/
install -D %{SOURCE9} %{buildroot}%{_sysusersdir}/%{name}.conf
mkdir -p %{buildroot}%{_tmpfilesdir}/
install -m 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/opendnssec.conf
mkdir -p %{buildroot}%{_localstatedir}/run/opendnssec
mkdir -p %{buildroot}%{_datadir}/opendnssec/
cp -a enforcer/utils %{buildroot}%{_datadir}/opendnssec/migration
cp -a enforcer/src/db/schema.* %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/
# fixup path for mysql/sqlite. Use our replacement sqlite_convert.sql to detect previous migration
cp -a %{SOURCE7} %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/sqlite_convert.sql
cp -a %{SOURCE8} %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/rpmversion.sql
sed -i "s:^SCHEMA=.*schema:SCHEMA=%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/schema:" %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/convert_sqlite
sed -i "s:find_problematic_zones.sql:%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/find_problematic_zones.sql:g" %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/convert_sqlite
sed -i "s:^SCHEMA=.*schema:SCHEMA=%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/schema:" %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/convert_mysql
sed -i "s:find_problematic_zones.sql:%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/find_problematic_zones.sql:g" %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/convert_mysql
sed -i "s:sqlite_convert.sql:%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/sqlite_convert.sql:g" %{buildroot}%{_datadir}/opendnssec/migration/1.4-2.0_db_convert/convert_sqlite


%files
%{_unitdir}/ods-enforcerd.service
%{_unitdir}/ods-signerd.service
%config(noreplace) %{_tmpfilesdir}/opendnssec.conf
%attr(0770,root,ods) %dir %{_sysconfdir}/opendnssec
%attr(0770,root,ods) %dir %{_localstatedir}/opendnssec
%attr(0770,root,ods) %dir %{_localstatedir}/opendnssec/tmp
%attr(0775,root,ods) %dir %{_localstatedir}/opendnssec/signed
%attr(0770,root,ods) %dir %{_localstatedir}/opendnssec/signconf
%attr(0770,root,ods) %dir %{_localstatedir}/opendnssec/enforcer
%attr(0660,root,ods) %config(noreplace) %{_sysconfdir}/opendnssec/*.xml
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/ods
%attr(0770,root,ods) %dir %{_localstatedir}/run/opendnssec
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cron.d/opendnssec
%doc NEWS README.md
%license LICENSE
%{_mandir}/*/*
%{_sbindir}/*
%{_bindir}/*
%attr(0755,root,root) %dir %{_datadir}/opendnssec
%{_datadir}/opendnssec/*
%{_sysusersdir}/%{name}.conf

%pre

%sysusers_create_package %{name} %{SOURCE9}

%post
# Initialise a slot on the softhsm on first install
if [ "$1" -eq 1 ]; then
   %{_sbindir}/runuser -u ods -- %{_bindir}/softhsm2-util --init-token \
                --free --label "OpenDNSSEC" --pin 1234 --so-pin 1234
   if [ ! -s %{_localstatedir}/opendnssec/kasp.db ]; then
      echo y | %{_sbindir}/ods-enforcer-db-setup
      %{_bindir}/sqlite3 -batch %{_localstatedir}/opendnssec/kasp.db < %{_datadir}/opendnssec/migration/1.4-2.0_db_convert/rpmversion.sql
   fi

elif [ -z "$(%{_bindir}/sqlite3 %{_localstatedir}/opendnssec/kasp.db 'select * from rpm_migration;')" ]; then
   # Migrate version 1.4 db to version 2.1 db
   if [ -e %{_localstatedir}/opendnssec/rpm-migration-in-progress ]; then
      echo "previous (partial?) migration found - human intervention is needed"
   else
      echo "opendnssec 1.4 database found, migrating to 2.x"
      touch %{_localstatedir}/opendnssec/rpm-migration-in-progress
      mv -n %{_localstatedir}/opendnssec/kasp.db %{_localstatedir}/opendnssec/kasp.db-1.4
      echo "migrating conf.xml from 1.4 to 2.1 schema"
      cp -n %{_sysconfdir}/opendnssec/conf.xml %{_sysconfdir}/opendnssec/conf.xml-1.4
      # fixup incompatibilities inflicted upon us by upstream :(
      sed -i "/<Interval>.*Interval>/d" %{_sysconfdir}/opendnssec/conf.xml
      echo "Converting kasp.db"
      ERR=""
      %{_datadir}/opendnssec/migration/1.4-2.0_db_convert/convert_sqlite -i %{_localstatedir}/opendnssec/kasp.db-1.4 -o %{_localstatedir}/opendnssec/kasp.db || ERR="convert_sqlite error"
      chown ods.ods %{_localstatedir}/opendnssec/kasp.db
      cp -n %{_sysconfdir}/opendnssec/zonelist.xml %{_localstatedir}/opendnssec/enforcer/zones.xml
      if [ -z "$ERR" ]; then
         echo "calling ods-migrate"
         ods-migrate || ERR="ods-migrate failed"
         if [ -z "$ERR" ]; then
            echo "opendnssec 1.4 to 2.x migration completed"
            rm %{_localstatedir}/opendnssec/rpm-migration-in-progress
         else
            echo "ods-migrate process failed - human intervention is needed"
         fi
      else
         echo "%{_localstatedir}/opendnssec/kasp.db conversion failed - not calling ods-migrate to complete migration. human intervention is needed"
      fi
   fi
fi

# in case we update any xml conf file
ods-enforcer update all >/dev/null 2>/dev/null ||:

%systemd_post ods-enforcerd.service
%systemd_post ods-signerd.service

%preun
%systemd_preun ods-enforcerd.service
%systemd_preun ods-signerd.service

%postun
%systemd_postun_with_restart ods-enforcerd.service
%systemd_postun_with_restart ods-signerd.service

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Tue Jan 21 2025 Rafel Jeffman <rjeffman@redhat.com> - 2.1.14-1
- Upstream release 2.1.14
- Use systemd-sysusers

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.14-0.4rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 22 2024 Richard W.M. Jones <rjones@redhat.com> - 2.1.14-0.3rc1
- Rebuild for Jansson 2.14
  (https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/3PYINSQGKQ4BB25NQUI2A2UCGGLAG5ND/)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.14-0.2rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 08 2024 Alexander Bokovoy <abokovoy@redhat.com> - 2.1.14-0.1rc1
- Upstream release 2.1.14RC1
- Fix build with gcc 14
- Resolves: rhbz#2261421

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb 24 2023 Florian Weimer <fweimer@redhat.com> - 2.1.10-6
- Port to C99

* Mon Jan 30 2023 Alexander Bokovoy <abokovoy@redhat.com> - 2.1.10-5
- Fix fortification issues leading to crash in FreeIPA setup
  Upstream PR: https://github.com/opendnssec/opendnssec/pull/842

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 François Cami <fcami@redhat.com> - 2.1.10-1
- Update to 2.1.10 (rhbz#2003250).

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.1.9-3
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 06 2021 François Cami <fcami@redhat.com> - 2.1.9-1
- Update to 2.1.9 (rhbz#1956561). Solves OPENDNSSEC-955 and OPENDNSSEC-956.
- Known issue: OPENDNSSEC-957: Signer daemon stops with failure exit code even when no error occured.

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.8-2
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Sat Feb 20 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.1.8-1
- Update to 2.1.8 (#1931143)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 19 10:13:50 PST 2020 awilliam@redhat.com - 2.1.7-3
- Rebuild for libldns soname bump

* Tue Dec  8 21:09:23 EST 2020 Paul Wouters <pwouters@redhat.com> - 2.1.7-2
- Resolves rhbz#1826233 ods-enforcerd.service should wait until socket is ready

* Fri Dec 04 2020 Alexander Bokovoy <abokovoy@redhat.com> - 2.1.7-1
- Upstream release 2.1.7

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 2.1.6-7
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Thu May 28 2020 Paul Wouters <pwouters@redhat.com> - 2.1.6-6
- Resolves: rhbz#1833718 ods-signerd.service missing .service

* Mon Apr 20 2020 Paul Wouters <pwouters@redhat.com> - 2.1.6-5
- Resolves: rhbz#1825812 AVC avc: denied { dac_override } for comm="ods-enforcerd

* Wed Mar 11 2020 Paul Wouters <pwouters@redhat.com> - 2.1.6-4
- Fix migration check to not attempt to check on first install with no db

* Tue Mar 03 2020 Alexander Bokovoy <abokovoy@redhat.com> - 2.1.6-3
- Create and manage /var/opendnssec/enforcer directory
- Resolves rhbz#1809492

* Wed Feb 19 2020 Paul Wouters <pwouters@redhat.com> - 2.1.6-2
- Update to 2.1.6 (major upgrade, supports migration from 1.4.x)
- gcc10 compile fixups
- Fix trying to use unversioned libsqlite3.so file

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 12 2017 Paul Wouters <pwouters@redhat.com> - 1.4.14-1
- Update to 1.4.14 as first steop to migrating to 2.x
- Resolves: rhbz#1413254 Move tmpfiles.d config to %%{_tmpfilesdir}, install LICENSE as %%license

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 08 2017 Tomas Hozza <thozza@redhat.com> - 1.4.9-5
- Fix FTBFS (#1424019) in order to rebuild against new ldns

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 18 2016 Paul Wouters <pwouters@redhat.com> - 1.4.9-3
- Resolves: rbz#1303965 upgrade to opendnssec-1.4.9-1.fc23 breaks old installations
- On initial install, after token init, also run ods-ksmutil setup

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Paul Wouters <pwouters@redhat.com> - 1.4.9-1
- Updated to 1.4.9
- Removed merged in patch

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Paul Wouters <pwouters@redhat.com> - 1.4.7-2
- Resolves rhbz#1219746 ods-signerd.service misplaced After= in section Service
- Resolves rhbz#1220443 OpenDNSSEC fails to initialise a slot in softhsm on first install

* Tue Dec 09 2014 Paul Wouters <pwouters@redhat.com> - 1.4.7-1
- Updated to 1.4.7 (fix zone update can get stuck, crash on retransfer cmd)

* Wed Oct 15 2014 Paul Wouters <pwouters@redhat.com> - 1.4.6-4
- Change /etc/opendnssec to be ods group writable

* Wed Oct 08 2014 Paul Wouters <pwouters@redhat.com> - 1.4.6-3
- Added Petr Spacek's patch that adds the config option <AllowExtraction/> (rhbz#1123354)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Paul Wouters <pwouters@redhat.com> - 1.4.6-1
- Updated to 1.4.6
- Removed incorporated patch upstream
- Remove Wants= from ods-signerd.service (rhbz#1098205)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Paul Wouters <pwouters@redhat.com> - 1.4.5-2
- Updated to 1.4.5
- Added patch for serial 0 bug in XFR adapter

* Tue Apr 01 2014 Paul Wouters <pwouters@redhat.com> - 1.4.4-3
- Add buildrequires for ods-kasp2html (rhbz#1073313)

* Sat Mar 29 2014 Paul Wouters <pwouters@redhat.com> - 1.4.4-2
- Add requires for ods-kasp2html (rhbz#1073313)

* Thu Mar 27 2014 Paul Wouters <pwouters@redhat.com> - 1.4.4-1
- Updated to 1.4.4 (compatibility with non RFC 5155 errata 3441)
- Change the default ZSK policy from 1024 to 2048 bit RSA keys
- Fix post to be quiet when upgrading opendnssec

* Thu Jan 09 2014 Paul Wouters <pwouters@redhat.com> - 1.4.3-1
- Updated to 1.4.3 (rhel#1048449) - minor bugfixes, minor feature enhancements
- rhel#1025985 OpenDNSSEC signer cannot be started due to a typo in service file

* Wed Sep 11 2013 Paul Wouters <pwouters@redhat.com> - 1.4.2-1
- Updated to 1.4.2, bugfix release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Paul Wouters <pwouters@redhat.com> - 1.4.1-1
- Updated to 1.4.1. NSEC3 handling and serial number handling fixes
- Add BuildRequire for systemd-units

* Sat May 11 2013 Paul Wouters <pwouters@redhat.com> - 1.4.0-1
- Updated to 1.4.0

* Fri Apr 12 2013 Paul Wouters <pwouters@redhat.com> - 1.4.20-0.8.rc3
- Updated to 1.4.0rc3
- Enabled hardened compile, full relzo/pie

* Fri Jan 25 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 1.4.0-0.7.rc2
- Updated to 1.4.0rc2, which includes svn r6952

* Fri Jan 18 2013 Patrick Uiterwijk <puiterwijk@gmail.com> - 1.4.0-0.6.rc1
- Updated to 1.4.0rc1
- Applied opendnssec-ksk-premature-retirement.patch (svn r6952)

* Tue Dec 18 2012 Paul Wouters <pwouters@redhat.com> - 1.4.0-0.5.b2
- Updated to 1.4.0b2
- All patches have been merged upstream
- cron job should be marked as config file

* Tue Oct 30 2012 Paul Wouters <pwouters@redhat.com> - 1.4.0-0.4.b1
- Added BuildRequires: procps-ng for bug OPENDNSSEC-345
- Change RRSIG inception offset to -2h to avoid possible
  daylight saving issues on resolvers
- Patch to prevent removal of occluded data

* Wed Sep 26 2012 Paul Wouters <pwouters@redhat.com> - 1.4.0-0.3.b1
- Just an EVR fix to the proper standard
- Cleanup of spec file
- Introduce new systemd-rpm macros (rhbz#850242)

* Wed Sep 12 2012 Paul Wouters <pwouters@redhat.com> - 1.4.0-0.b1.1
- Updated to 1.4.0b1
- Patch for NSEC3PARAM TTL
- Cron job to assist narrowing ods-enforcerd timing differences

* Wed Aug 29 2012 Paul Wouters <pwouters@redhat.com> - 1.4.0-0.a3.1
- Updated to 1.4.0a3
- Patch to more aggressively try to resign
- Patch to fix locking issue eating up cpu

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-0.a2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Paul Wouters <pwouters@redhat.com> - 1.4.0-0.a2.1
- Updated to 1.4.0a2
- ksm-utils patch for ods-ksmutil to die sooner when it can't lock
  the HSM.

* Wed May 16 2012 Paul Wouters <pwouters@redhat.com> - 1.4.0-0.a1.3
- Patch for crasher with deleted RRsets and NSEC3/OPTOUT chains

* Mon Mar 26 2012 Paul Wouters <pwouters@redhat.com> - 1.4.0-0.a1.2
- Added opendnssec LICENSE file from trunk (Thanks Jakob!)

* Mon Mar 26 2012 Paul Wouters <pwouters@redhat.com> - 1.4.0-0.a1.1
- Fix macros in comment
- Added missing -m to install target

* Sun Mar 25 2012 Paul Wouters <pwouters@redhat.com> - 1.4.0-0.a1
- The 1.4.x branch no longer needs ruby, as the auditor has been removed
- Added missing openssl-devel BuildRequire
- Comment out <SkipPublicKey/> so keys generated by ods can be used by bind

* Fri Feb 24 2012 Paul Wouters <pwouters@redhat.com> - 1.3.6-3
- Requires rubygem-soap4r when using ruby-1.9
- Don't ghost /var/run/opendnssec
- Converted initd to systemd

* Thu Nov 24 2011 root - 1.3.2-6
- Added rubygem-dnsruby requires as rpm does not pick it up automatically

* Tue Nov 22 2011 root - 1.3.2-5
- Added /var/opendnssec/signconf/ /as this temp dir is needed

* Mon Nov 21 2011 Paul Wouters <paul@xelerance.com> - 1.3.2-4
- Added /var/opendnssec/signed/ as this is the default output dir

* Sun Nov 20 2011 Paul Wouters <paul@xelerance.com> - 1.3.2-3
- Add ods user for opendnssec tasks
- Added initscripts and services for ods-signerd and ods-enforcerd
- Initialise OpenDNSSEC softhsm token on first install

* Wed Oct 05 2011 Paul Wouters <paul@xelerance.com> - 1.3.2-1
- Updated to 1.3.2
- Added dependancies on opencryptoki and softhsm
- Don't install duplicate unreadable .sample files
- Fix upstream conf.xml to point to actually used library paths

* Thu Mar  3 2011 Paul Wouters <paul@xelerance.com> - 1.2.0-1
- Initial package for Fedora
