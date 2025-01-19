%global _hardened_build 1
%bcond_without pam
%bcond_without sqlite
%bcond_without db
%bcond_without ldap
%bcond_without mysql
%bcond_without postgresql
%if 0%{?rhel} && 0%{?rhel} == 6
%bcond_with systemd
%else
%bcond_without systemd
%endif

Summary:        OpenSource server implementation of the Jabber protocols
Name:           jabberd
Version:        2.6.1
Release:        30%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Source0:        https://github.com/jabberd2/jabberd2/releases/download/jabberd-%{version}/jabberd-%{version}.tar.xz
Source1:        README.fedora
Source2:        jabberd.init
Source3:        jabberd.sysconfig
Patch0:         jabberd-fedora-crypto-policy.patch
Patch1:         jabberd-fix-paths.patch
Patch2:         unbreak-autoreconf.patch
Patch3:         0001-configure.ac-adapt-to-openssl-1.1.patch
Patch4:         0002-authreg_ldapfull-adapt-to-openssl-1.1.patch
Patch5:         0003-sx-ssl.c-adapt-to-openssl-1.1.patch
Patch6:         0001-Fix-build-errors-with-MariaDB-10.2.patch
# rhbz1510642
Patch7:         181e736dcbb19c828266d88837f4343510b4d20e.patch
Patch8:         jabberd-c99.patch
URL:            http://jabberd2.org/
BuildRequires:  openssl-devel libidn-devel expat-devel
BuildRequires:  perl-generators
BuildRequires:  cppunit-devel
%if %{with systemd}
BuildRequires:          systemd-units
Requires(post):         systemd-units systemd-sysv
Requires(preun):        systemd-units
Requires(postun):       systemd-units
%else
Requires(post):         openssl chkconfig /sbin/service
Requires(pre):          shadow-utils
Requires(preun):        chkconfig shadow-utils /sbin/service
Requires(postun):       chkconfig /sbin/service
%endif
%if %{with pam}
BuildRequires:  pam-devel
%endif
%if %{with sqlite}
BuildRequires:  sqlite-devel
%endif
%if %{with db}
%if 0%{?fedora} >= 26
BuildRequires:  libdb-devel
%else
BuildRequires:  db4-devel
%endif
%endif
%if %{with ldap}
BuildRequires:  openldap-devel
%endif
%if %{with mysql}
%if 0%{?fedora} > 27
BuildRequires:  mariadb-connector-c-devel
%else
BuildRequires:  mysql-devel
%endif
%endif
%if %{with postgresql}
BuildRequires:  libpq-devel
%endif
BuildRequires:          libgsasl-devel udns-devel
BuildRequires:          http-parser-devel
BuildRequires:          autoconf libtool
BuildRequires: make
Requires(post):         openssl
Requires(pre):          shadow-utils
Requires(preun):        shadow-utils

%description
The jabberd project aims to provide an open-source server implementation of
the Jabber protocols for instant messaging and XML routing. The goal of this
project is to provide a scalable, reliable, efficient and extensible server
that provides a complete set of features and is up to date with the latest
protocol revisions.

jabberd2 is the next generation of the jabberd server. It has been
rewritten from the ground up to be scalable, architecturally sound, and to
support the latest protocol extensions coming out of the JSF.

This package defaults to use pam and sqlite.

%prep
%setup -q
# "Utilize system-wide crypto-policies" is only for F21+ (#1179229)
# therefore the patch is not applied on non Fedora builds
%if 0%{?fedora}
%patch -P0 -p1
%endif
%patch -P1 -p1
%if 0%{?fedora} >= 26
# With Fedora 26 openssl-1.1 was introduced. jabberd needs patches
# to work with openssl-1.1. These patches have been submitted upstream:
# https://github.com/jabberd2/jabberd2/pull/129
# The patches also work with older openssl versions.
# For now the patches are only applied for rawhide/f26 as long as upstream
# has not merged the patches.
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P7 -p1
%patch -P8 -p1
autoreconf --verbose --force --install
%endif
%patch -P6 -p1

%build
export CFLAGS="%{optflags}"
%configure \
        --sysconfdir=%{_sysconfdir}/%{name} \
        --localstatedir=%{_var}/lib \
%if %{with pam}
        --enable-pam \
%else
        --disable-pam \
%endif
%if %{with db}
        --enable-db \
%if 0%{?fedora} < 26
        --with-extra-include-path=%{_includedir}/libdb4 \
%endif
%else
        --disable-db \
%endif
%if %{with mysql}
        --enable-mysql \
%if 0%{?fedora} > 27
        --with-extra-library-path=%{_libdir}/mariadb \
%else
        --with-extra-library-path=%{_libdir}/mysql \
%endif
%else
        --disable-mysql \
%endif
%if %{with ldap}
        --enable-ldap \
%else
        --disable-ldap \
%endif
%if %{with postgresql}
        --enable-pgsql \
%else
        --disable-pgsql \
%endif
%if %{with sqlite}
        --enable-sqlite \
%else
        --disable-sqlite \
%endif
        --enable-fs --enable-anon --enable-pipe --enable-ssl \
        --enable-websocket \
        --enable-debug

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# correct the script interpreter for perl scripts
sed -i "s|/usr/pkg/bin/perl|/usr/bin/env perl|" tools/*.pl

install -dpm 700 $RPM_BUILD_ROOT/%{_var}/lib/%{name}/{log,pid,db}
install -dpm 755 $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/
install -Dpm 644 tools/pam_jabberd $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/%{name}

install -dpm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/
# install any tool in tools/ to /usr/share/jabberd/, but skip Makefile-stuff
# and unneccessary scripts
install -dpm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/
for i in `ls tools`; do
    if [ $i == "Makefile" -o $i == "Makefile.am" -o $i == "Makefile.in" \
        -o $i == "jabberd.in" -o $i == "jabberd.rc" -o $i == "pam_jabberd" ]; then
        continue;
    fi

    sed -i "s|\r||g" tools/$i
    install -pm 755 tools/$i $RPM_BUILD_ROOT%{_datadir}/%{name}/
done

install -dpm 755 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/

%if ! %{with systemd}
rm -frv $RPM_BUILD_ROOT%{_prefix}/lib/systemd

install -Dpm 755 %{SOURCE2} $RPM_BUILD_ROOT%{_initrddir}/%{name}
install -Dpm 644 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}

sed -i -e "s,__BINDIR__,%{_bindir},g" \
       -e "s,__ETCDIR__,%{_sysconfdir}/%{name}/,g" \
       -e "s,__PIDDIR__,%{_var}/lib/%{name}/pid,g" \
       -e "s,__SYSCONF__,%{_sysconfdir}/sysconfig,g" \
          $RPM_BUILD_ROOT%{_initrddir}/%{name} \
          $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
%endif

# remove static libraries
find $RPM_BUILD_ROOT -name "*.la" -delete

# Remove Upstart configuration files, they are not needed for Fedora
rm -f $RPM_BUILD_ROOT/etc/jabberd/*.conf
rm -f $RPM_BUILD_ROOT/usr/etc/init/*.conf

#default authentication backend
#enable SSL certificate
#clients must do STARTTLS
#disable account registrations by default, because the default installation uses PAM
#set the realm to '' for a working authentication against PAM
sed -i -e ':a;N;$!ba' \
            -e 's,<module>mysql</module>,<module>pam</module>,g' \
            -e "s,register-enable='true'>,realm='' require-starttls='true' pemfile='/etc/%{name}/server.pem'>,g" \
                $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/c2s.xml

touch $RPM_BUILD_ROOT%{_sysconfdir}/jabberd/server.pem

# we have our own start script
rm -f $RPM_BUILD_ROOT%{_bindir}/jabberd

# we have our own start script
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/jabberd.cfg*

# README.fedora
cp %{SOURCE1} .



%pre
#creating jabber user
getent group jabber >/dev/null || groupadd -r jabber
getent passwd jabber >/dev/null || \
useradd -r -g jabber -d %{_var}/lib/%{name} -s /sbin/nologin \
        -c "Jabber Server" jabber
exit 0

%post
%if %{with systemd}
%systemd_post %{name}.service
if [ $1 -eq 1 ] ; then
        #replace default passwords, yet another hack
        export NEWPASS=$( dd if=/dev/urandom bs=20 count=1 2>/dev/null \
                                | sha1sum | awk '{print $1}' )
        cd %{_sysconfdir}/%{name}
        %{__sed} -i -f- router-users.xml router.xml <<END
s,<secret>secret</secret>,<secret>$NEWPASS</secret>,g
END
        %{__sed} -i -f- *.xml <<END
s,<pass>secret</pass>,<pass>$NEWPASS</pass>,g
END

fi

#create ssl certificate
cd %{_sysconfdir}/%{name}
if [ ! -s server.pem ]; then
 if [ -e %{_bindir}/make-dummy-cert ]; then
  # openssl-1.1 places the script in /usr
  %{___build_shell} %{_bindir}/make-dummy-cert
 else
  %{___build_shell} %{_sysconfdir}/pki/tls/certs/make-dummy-cert server.pem
 fi
 chown root.jabber server.pem
 chmod 640 server.pem
fi
%else
if [ "$1" -eq "1" ]; then
        /sbin/chkconfig --add %{name}
        #replace default passwords, yet another hack
        export NEWPASS=$( dd if=/dev/urandom bs=20 count=1 2>/dev/null \
                                | sha1sum | awk '{print $1}' )
        cd %{_sysconfdir}/%{name}
        %{__sed} -i -f- router-users.xml router.xml <<END
s,<secret>secret</secret>,<secret>$NEWPASS</secret>,g
END
        %{__sed} -i -f- *.xml <<END
s,<pass>secret</pass>,<pass>$NEWPASS</pass>,g
END

fi

#create ssl certificate
cd %{_sysconfdir}/%{name}
if [ ! -s server.pem ]; then
 %{___build_shell} %{_sysconfdir}/pki/tls/certs/make-dummy-cert server.pem
 chown root.jabber server.pem
 chmod 640 server.pem
fi
%endif

%preun
%if %{with systemd}
%systemd_preun %{name}.service
%else
if [ "$1" -eq "0" ]; then
        /sbin/service %{name} stop > /dev/null 2>&1
        /sbin/chkconfig --del %{name}
fi
%endif


%postun
%if %{with systemd}
%systemd_postun_with_restart %{name}.service

%triggerun -- jabberd < 2.2.14-3
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply jabberd
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save %{name} >/dev/null 2>&1 ||:

# If the package is allowed to autostart:
/bin/systemctl --no-reload enable %{name}.service >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del %{name} >/dev/null 2>&1 || :
/bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
%else
if [ "$1" -eq "1" ]; then
        /sbin/service %{name} condrestart > /dev/null 2>&1
fi
%endif


%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO README.fedora
%{_mandir}/man8/*
%{_bindir}/*
%if %{with systemd}
%{_unitdir}/*
%else
%{_initrddir}/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%endif
%{_libdir}/%{name}/
%attr(750, jabber, jabber) %dir %{_sysconfdir}/%{name}
%attr(750, jabber, jabber) %dir %{_sysconfdir}/%{name}/templates
%config(noreplace) %{_sysconfdir}/%{name}/server.pem
%attr(640, jabber, jabber) %config(noreplace) %{_sysconfdir}/%{name}/*xml*
%attr(640, jabber, jabber) %config(noreplace) %{_sysconfdir}/%{name}/templates/*xml*
%dir %{_datadir}/%{name}/
%attr(644,root,root) %{_datadir}/%{name}/*
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%attr(700, jabber, jabber) %{_var}/lib/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.6.1-29
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 12 2023 Arjun Shankar <arjun@redhat.com> - 2.6.1-24
- Port to C99 (#2186195)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.6.1-20
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.6.1-18
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 2.6.1-17
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.6.1-14
- Rebuild for http-parser 2.9.4

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.6.1-10
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.6.1-7
- Rebuilt for switch to libxcrypt

* Wed Nov 08 2017 Adrian Reber <adrian@lisas.de> - 2.6.1-6
- Fix crash with new openssl 1.1 support patch (Oleg Girko) (#1510642)

* Wed Sep 20 2017 Adrian Reber <adrian@lisas.de> - 2.6.1-5
- Switch to mariadb-connector-c-devel from mysql-devel for > f27 (#1493627)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Adrian Reber <adrian@lisas.de> - 2.6.1-2
- added patch to fix build errors with mariadb 10.2 (#1470036)

* Tue Jul 04 2017 Adrian Reber <adrian@lisas.de> - 2.6.1-1
- updated to 2.6.1 (security bugfix release)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Matěj Cepl <mcepl@redhat.com> - 2.5.0-1
- New upstream release.

* Tue Dec 20 2016 Adrian Reber <adrian@lisas.de> - 2.4.0-6
- Added patches to fix "segfaut in 'sm' component when blocking users" (#1406062)
- BR libdb-devel instead of db4-devel

* Fri Dec 02 2016 Adrian Reber <adrian@lisas.de> - 2.4.0-5
- Added patches to build against openssl-1.1 (only for >= 26)

* Tue Oct 04 2016 Matěj Cepl <mcepl@redhat.com> - 2.4.0-4
- Make spec alternatively working with RHEL-6 (no systemd).

* Tue Oct 04 2016 Adrian Reber <adrian@lisas.de> - 2.4.0-3
- Fixes "Enable websockets" (#1380958)

* Sat Jun 25 2016 Matěj Cepl <mcepl@redhat.com> - 2.4.0-2
- Use standard conditional macros in SPEC (#647101)
- Fix system paths (#857540)

* Mon May 23 2016 Adrian Reber <adrian@lisas.de> - 2.4.0-1
- updated to 2.4.0

* Sun Feb 28 2016 Adrian Reber <adrian@lisas.de> - 2.3.6-1
- updated to 2.3.6
- remove fix for "Version mismatch error."

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 31 2016 Adrian Reber <adrian@lisas.de> - 2.3.5-1
- updated to 2.3.5
- run autoreconf to fix libtool error

* Mon Nov 09 2015 Adrian Reber <adrian@lisas.de> - 2.3.4-1
- updated to 2.3.4

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 21 2015 Adrian Reber <adrian@lisas.de> - 2.3.3-5
- fix release number

* Tue Apr 14 2015 Adrian Reber <adrian@lisas.de> - 2.3.3-1
- updated to 2.3.3

* Thu Feb 26 2015 Adrian Reber <adrian@lisas.de> - 2.3.2-4
- fixes "Utilize system-wide crypto-policies" (#1179229) (thanks to Matěj Cepl)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Adrian Reber <adrian@lisas.de> - 2.3.2-1
- updated to 2.3.2
- dropped patches

* Tue Feb 18 2014 Adrian Reber <adrian@lisas.de> - 2.3.1-3
- upstreamed systemd unit files (Patch1)

* Wed Dec 04 2013 Adrian Reber <adrian@lisas.de> - 2.3.1-2
- fixes "Regression with jabberd 2.3.1 and postgresql" (#1036876)
  https://github.com/jabberd2/jabberd2/issues/48

* Thu Nov 28 2013 Adrian Reber <adrian@lisas.de> - 2.3.1-1
- updated to 2.3.1

* Fri Aug 23 2013 Adrian Reber <adrian@lisas.de> - 2.2.17-5
- enable _hardened_build (#954340)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.2.17-3
- Perl 5.18 rebuild

* Thu Jan 31 2013 Adrian Reber <adrian@lisas.de> - 2.2.17-2
- added README.fedora which describes what to change
  for authentication with PAM (#896575)

* Mon Aug 27 2012 Adrian Reber <adrian@lisas.de> - 2.2.17-1
- updated to 2.2.17
- removed all three patches which are now included

* Wed Aug 22 2012 Adrian Reber <adrian@lisas.de> - 2.2.16-5
- included patch for "Vulnerability in XMPP Server Dialback Implementations"
  http://xmpp.org/resources/security-notices/server-dialback/
- fixed "Introduce new systemd-rpm macros in jabberd spec file" (#850175)

* Tue Jul 24 2012 Adrian Reber <adrian@lisas.de> - 2.2.16-4
- added libdb4 include directory to include search path

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Adrian Reber <adrian@lisas.de> - 2.2.16-2
- added patch for "multiple calls of srand() with expat-2.1.0"
  https://github.com/Jabberd2/jabberd2/pull/5

* Sat May 05 2012 Adrian Reber <adrian@lisas.de> - 2.2.16-1
- updated to 2.2.16
- added patch 41884d9919.patch to build without debug

* Wed May 02 2012 Adrian Reber <adrian@lisas.de> - 2.2.15-1
- updated to 2.2.15

* Sat Mar 24 2012 Adrian Reber <adrian@lisas.de> - 2.2.14-3
- removed buildroot and clean section
- switched to systemd

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 01 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 2.2.14-1
- update to 2.2.14 (#700390, CVE-2011-1755)
- remove unneeded upstart configuration files

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 2.2.13-3
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Tue Mar 22 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 2.2.13-2
- rebuild against new libmysqlclient

* Wed Feb 23 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 2.2.13-1
- updated to 2.2.13

* Tue Feb 15 2011 Adrian Reber <adrian@lisas.de> - 2.2.12-1
- updated to 2.2.12

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 05 2011 Adrian Reber <adrian@lisas.de> - 2.2.11-7
- ported spec changes from f14 branch to devel branch
- fix "jabberd spec file puts server.pem in /etc instead of /etc/jabberd" (#667504)

* Wed Sep 29 2010 jkeating - 2.2.11-2
- Rebuilt for gcc bug 634757

* Sun Sep 12 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 2.2.11-1
- new upstream release
- fix script-without-shebang errors
- preserve timestamp of ChangeLog while converting to UTF8

* Thu Aug 12 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 2.2.10-1
- new upstream release jabberd 2.2.10
- add patch jabberd-fix-missing-reference-in-log_error.patch from upstream svn
- use %%{_mandir} macro for manpages
- create a new source file for the PAM info instead of writing it on the fly
- install all tools provided by upstream to /usr/share/jabberd/
- remove storage driver replacement, since 2.2.10 sqlite is the default
- remove dependency to gc-devel
- remove unneccessary defines for sysconfdir and don't use unneccessary macros
- remove static libraries
- fix a lot of rpmlint errors and warnings

* Wed Sep 16 2009 Tomas Mraz <tmraz@redhat.com> - 2.2.8-5
- use password-auth common PAM configuration instead of system-auth

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.2.8-4
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 19 2009 Adrian Reber <adrian@lisas.de> - 2.2.8-2
- updated to 2.2.8
- added patch to fix "router segfaults" (rhbz#497671)

* Tue Mar 31 2009 Bernie Innocenti <bernie@codewiz.org> - 2.2.7.1-2
- fix rhbz#349714: jabberd does not close its stdin/stdout/stderr

* Thu Feb 26 2009 Adrian Reber <adrian@lisas.de> - 2.2.7.1-1
- updated to 2.2.7.1
- "Workaround for buggy Java TLS implementation (affecting OpenFire and GTalk)"

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Adrian Reber <adrian@lisas.de> - 2.2.7-1
- updated to 2.2.7

* Mon Feb 16 2009 Adrian Reber <adrian@lisas.de> - 2.2.6-1
- updated to 2.2.6

* Tue Feb 03 2009 Adrian Reber <adrian@lisas.de> - 2.2.5-1
- updated to 2.2.5

* Fri Jan 23 2009 Bernie Innocenti <bernie@codewiz.org> - 2.2.4-2
- Replace /etc/sysconfig/jabberd on upgrade to drop obsolete daemons
- Rebuilt for new libmysqlclient

* Tue Oct 07 2008 Adrian Reber <adrian@lisas.de> - 2.2.4-1
- updated to 2.2.4
  (this version and pidgin 2.5.1 finally work together)

* Mon Feb 11 2008 Adrian Reber <adrian@lisas.de> - 2.1.23-1
- updated to 2.1.23

* Tue Jan 08 2008 Adrian Reber <adrian@lisas.de> - 2.1.21-1
- updated to 2.1.21

* Tue Jan 08 2008 Adrian Reber <adrian@lisas.de> - 2.1.20-1
- updated to 2.1.20

* Thu Dec 06 2007 Adrian Reber <adrian@lisas.de> - 2.1.19-1
- updated to 2.1.19
- this version might be config file incompatible to 2.0
  in certain cases
- for details please refer to the UPGRADE file

* Wed Dec 05 2007 Adrian Reber <adrian@lisas.de> - 2.0-0.s11.15
- rebuilt for new openssl and openldap

* Mon Aug 27 2007 Adrian Reber <adrian@lisas.de> - 2.0-0.s11.14
- applied patch to fix bz #175219
- removed config flag for startup script
- updated License
- added patch for new glibc open macro

* Tue Jun 12 2007 Thorsten Leemhuis <fedora [AT] leemhuis.info> - 2.0-0.s11.13
- rebuilt on behalf of Adrian

* Thu Dec 07 2006 Adrian Reber <adrian@lisas.de> - 2.0-0.s11.12
- rebuilt

* Tue Sep 12 2006 Adrian Reber <adrian@lisas.de> - 2.0-0.s11.11
- rebuilt

* Mon Aug 07 2006 Adrian Reber <adrian@lisas.de> - 2.0-0.s11.10
- changed pam file to use include
- added return value for status() function (bz #200996)

* Mon Apr 03 2006 Adrian Reber <adrian@lisas.de> - 2.0-0.s11.9
- updated to 2.0-0.s11

* Wed Feb 15 2006 Adrian Reber <adrian@lisas.de> - 2.0-0.s10.9
- rebuilt

* Sun Nov 27 2005 Adrian Reber <adrian@lisas.de> - 2.0-0.s10.8
- %%{_sysconfdir}/jabberd/server.pem was listed twice
- added /sbin/service dependency to %%post, %%postun and %%preun
- jabber user is not deleted to avoid unowned files

* Mon Oct 17 2005 Adrian Reber <adrian@lisas.de> - 2.0-0.s10.7
- updated to 2.0-0.s10

* Mon Aug 01 2005 Adrian Reber <adrian@lisas.de> - 2.0-0.s9.6
- updated to 2.0-0.s9.6

* Thu May 12 2005 Adrian Reber <adrian@lisas.de> - 2.0-0.s8.5
- updated to 2.0-0.s8.5
- using new location of make-dummy-cert

* Wed Mar 09 2005 Adrian Reber <adrian@lisas.de> - 2.0-0.s6.5
- removed Epoch: 0
- more Requires(...)
- typo
- changed db location to %%{_var}/lib/jabberd
- removed noreplace for start script
- make backends optional during build
- use -p with the install command
- combined some of the sed magic
- added a jabberd file in sysconfig to control if all daemons
  should be started
- don't suid c2s and add config option in sysconfig/jabberd
  to start c2s as root if required to authenticate against pam/shadow

* Tue Mar 08 2005 Adrian Reber <adrian@lisas.de> - 2.0-0.s6.4
- made password more random (/dev/random)
- replace password in the config without making it visible in ps
- enable ldap, mysql, postgresql backends
- remove dependency on perl during build
- make pam default authentication backend in c2s.xml
- make files in etc (640, jabber, jabber)
- enabled SSL certificate in c2s.xml
- enabled auto creation of accounts in sm.xml (necessary for usage with PAM)
- enabled require-startls

* Mon Mar 07 2005 Adrian Reber <adrian@lisas.de> - 2.0-0.s6.3
- changed startscript again

* Mon Mar 07 2005 Adrian Reber <adrian@lisas.de> - 2.0-0.s6.2
- changed startscript to support condrestart

* Mon Mar 07 2005 Adrian Reber <adrian@lisas.de> - 2.0-0.s6.1
- updated to 2.0s6

* Wed Nov 24 2004 Adrian Reber <adrian@lisas.de> - 0:2.0-0.fdr.16.s4
- updated to 2.0s4
- added jabberd-c2s-buffers.patch
  (http://jabberstudio.org/projects/jabberd2/bugs/view.php?id=4528)
- replace <driver>mysql</driver> with <driver>db</driver> in sm.xml

* Mon Jul 19 2004 Adrian Reber <adrian@lisas.de> - 0:2.0-0.fdr.15.s3
- add ||: at the end of the useradd line

* Mon Jul 19 2004 Adrian Reber <adrian@lisas.de> - 0:2.0-0.fdr.14.s3
- create jabber user in %%pre instead of in %%post
- remove -r from userdel

* Mon Jul 19 2004 Adrian Reber <adrian@lisas.de> - 0:2.0-0.fdr.13.s3
- s/jabberd2/%%{name}/
- replace another default password

* Fri Jul 16 2004 Adrian Reber <adrian@lisas.de> - 0:2.0-0.fdr.12.s3
- %%{_var}/jabberd is now owned be the package
- %%ghost-ing server.pem
- disable rm-ing %%{_var}/jabberd on uninstall

* Fri Jul 16 2004 Adrian Reber <adrian@lisas.de> - 0:2.0-0.fdr.11.s3
- using %%{_datadir}/ssl/certs/make-dummy-cert to
  create the certificate
- added -r to useradd
- added openssl to post-requires
- added libidn-devel and pam-devel as BuildRequires

* Mon Jul 12 2004 Adrian Reber <adrian@lisas.de> - 0:2.0-0.fdr.10.s3
- complete rewrite for fedora (I mean it)

* Tue May 18 2004 Tim Niemueller <tim@niemueller.de>
- Initial spec file
