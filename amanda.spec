%if 0%{?rhel} >= 9
%bcond_with gnuplot
%else
%bcond_without gnuplot
%endif

%define _libexecdir %{_libdir}
%define defconfig DailySet1
%define indexserver amandahost
%define tapeserver %{indexserver}
%define amanda_user amandabackup
%define amanda_group disk

%global _hardened_build 1

Summary:       A network-capable tape backup solution
Name:          amanda
Version:       3.5.3
Release:       3%{?dist}
Source:        https://github.com/zmanda/amanda/archive/tag-community-%{version}/amanda-%{version}.tar.gz
Source1:       amanda.crontab
Source4:       disklist
Source8:       amandahosts
Source9:       amanda.socket
Source10:      amanda@.service
Source11:      activate-devpay.1.gz
Source12:      killpgrp.8
Source13:      amanda-udp.socket
Source14:      amanda-udp.service
Source15:      kamanda.socket
Source16:      kamanda@.service
Patch1:        amanda-3.1.1-xattrs.patch
Patch2:        amanda-3.1.1-tcpport.patch
Patch3:        amanda-3.2.0-config-dir.patch
# Don't mention xinetd files in amserverconfig (#1460763)
Patch4:        amanda-3.4.5-no-xinetd.patch
# Support tirpc
Patch5:        patch-tirpc

# Specify the location or the xfs housekeeping directory
# https://bugzilla.redhat.com/show_bug.cgi?id=1671117
Patch6:        patch-xfsrestore-housekeeping
Patch7: amanda-configure-c99.patch

License:       BSD-3-Clause AND GPL-3.0-or-later AND GPL-2.0-or-later AND GPL-2.0-only
URL:           http://www.amanda.org
BuildRequires: automake autoconf libtool
BuildRequires: xfsdump
%if %{with gnuplot}
BuildRequires: gnuplot
%endif
BuildRequires: cups samba-client tar grep
BuildRequires: gcc-c++ readline-devel libtirpc-devel
BuildRequires: krb5-devel rsh openssh-clients
BuildRequires: mtx mt-st
BuildRequires: perl-devel perl-generators perl(ExtUtils::Embed) perl(Test::Simple)
BuildRequires: glib2-devel openssl-devel swig bison flex
BuildRequires: libcurl-devel procps-ng systemd
BuildRequires: make
BuildRequires: rpcgen
Requires:      grep tar /usr/bin/mail
Requires:      amanda-libs%{?_isa} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
%{?systemd_requires}

%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Math::BigInt\\)

# Filter bogus libArchive.so() etc. Provides, this is intentional rpm-build
# feature, bug #1309664
%global __provides_exclude_from %{?__provides_exclude_from:%{__provides_exclude_from}|}^%{perl_vendorarch}/auto/.*\\.so$

#exclude Dancer2 module
%global __requires_exclude ^perl\\(Dancer2\\)

%description
AMANDA, the Advanced Maryland Automatic Network Disk Archiver, is a
backup system that allows the administrator of a LAN to set up a
single master backup server to back up multiple hosts to one or more
tape drives or disk files.  AMANDA uses native dump and/or GNU tar
facilities and can back up a large number of workstations running
multiple versions of Unix.  Newer versions of AMANDA (including this
version) can use SAMBA to back up Microsoft(TM) Windows95/NT hosts.
The amanda package contains the core AMANDA programs and will need to
be installed on both AMANDA clients and AMANDA servers.  Note that you
will have to install the amanda-client and/or amanda-server packages as
well.

%package libs
Summary:       Amanda libraries
Requires:      grep

%description libs
This package contains basic Amanda libraries, which are used by all
Amanda programs.

%package client
Summary:       The client component of the AMANDA tape backup system
Requires:      grep
Requires(pre): amanda = %{version}-%{release}
Requires:      amanda-libs%{?_isa} = %{version}-%{release}

%description client
The Amanda-client package should be installed on any machine that will
be backed up by AMANDA (including the server if it also needs to be
backed up).  You will also need to install the amanda package on each
AMANDA client machine.

%package server
Summary:       The server side of the AMANDA tape backup system
Requires:      grep
Requires:      perl(Amanda::DB) perl(Amanda::Recovery) perl(Amanda::Service)
Requires(pre): amanda = %{version}-%{release}
Requires:      amanda-libs%{?_isa} = %{version}-%{release}

%description server
The amanda-server package should be installed on the AMANDA server,
the machine attached to the device(s) (such as a tape drive) where backups
will be written. You will also need to install the amanda package on
the AMANDA server machine.  And, if the server is also to be backed up, the
server also needs to have the amanda-client package installed.

%prep
%autosetup -p1 -n %{name}-tag-community-%{version}

%build
./autogen

export MAILER=/usr/bin/mail CFLAGS="$RPM_OPT_FLAGS -fPIE" LDFLAGS="$RPM_LD_FLAGS -pie"
%configure --enable-shared \
           --disable-rpath \
           --disable-static \
           --disable-dependency-tracking \
           --disable-installperms \
           --with-amdatadir=%{_localstatedir}/lib/amanda \
           --with-amlibdir=%{_libdir} \
           --with-amperldir=%{perl_vendorarch} \
           --with-index-server=%{indexserver} \
           --with-tape-server=%{tapeserver} \
           --with-config=%{defconfig} \
           --with-gnutar-listdir=%{_localstatedir}/lib/amanda/gnutar-lists \
           --with-smbclient=%{_bindir}/smbclient \
           --with-amandates=%{_localstatedir}/lib/amanda/amandates \
           --with-amandahosts \
           --with-user=%amanda_user \
           --with-group=%amanda_group \
           --with-tmpdir=/var/log/amanda \
           --with-gnutar=/bin/tar \
%if %{without gnuplot}
           --without-gnuplot \
%endif
           --with-ssh-security \
           --with-rsh-security \
           --with-bsdtcp-security \
           --with-bsdudp-security \
           --with-krb5-security

pushd perl
make maintainer-clean-am
popd

%make_build


%install
%make_install BINARY_OWNER=%(id -un) SETUID_GROUP=%(id -gn)

mkdir -p $RPM_BUILD_ROOT/etc/amanda
mkdir -p $RPM_BUILD_ROOT/var/log/amanda/amandad
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/amanda
install -m 600 %SOURCE8 $RPM_BUILD_ROOT%{_localstatedir}/lib/amanda/.amandahosts
install -p -m 644 -D %{SOURCE9} %{buildroot}%{_unitdir}/amanda.socket
install -p -m 644 -D %{SOURCE10} %{buildroot}%{_unitdir}/amanda@.service
install -p -m 644 -D %{SOURCE13} %{buildroot}%{_unitdir}/amanda-udp.socket
install -p -m 644 -D %{SOURCE14} %{buildroot}%{_unitdir}/amanda-udp.service
install -p -m 644 -D %{SOURCE15} %{buildroot}%{_unitdir}/kamanda.socket
install -p -m 644 -D %{SOURCE16} %{buildroot}%{_unitdir}/kamanda@.service
install -D %{SOURCE11}  %{buildroot}/%{_mandir}/man1/activate-devpay.1.gz
install -D %{SOURCE12}  %{buildroot}/%{_mandir}/man8/killpgrp.8
install -m 644 %{buildroot}/etc/amanda/amanda-security.conf %{buildroot}/etc/amanda-security.conf
ln -s %{_libexecdir}/amanda/amandad $RPM_BUILD_ROOT%{_sbindir}/amandad
ln -s amrecover.8.gz $RPM_BUILD_ROOT%{_mandir}/man8/amoldrecover.8

pushd ${RPM_BUILD_ROOT}
  mv .%{_localstatedir}/lib/amanda/example .%{_sysconfdir}/amanda/%defconfig
  cp ${RPM_SOURCE_DIR}/amanda.crontab .%{_sysconfdir}/amanda/crontab.sample
  cp ${RPM_SOURCE_DIR}/disklist .%{_sysconfdir}/amanda/%defconfig
  cp ${RPM_SOURCE_DIR}/disklist .%{_sysconfdir}/amanda/%defconfig
  rm -f .%{_sysconfdir}/amanda/%defconfig/xinetd*
  rm -f .%{_sysconfdir}/amanda/%defconfig/inetd*

  mkdir -p .%{_localstatedir}/lib/amanda/gnutar-lists
  mkdir -p .%{_localstatedir}/lib/amanda/%defconfig/index
  touch .%{_localstatedir}/lib/amanda/amandates
popd
rm -rf $RPM_BUILD_ROOT/usr/share/amanda
find $RPM_BUILD_ROOT -name \*.la | xargs rm

%check
make check

%pre
/usr/sbin/useradd -M -N -g %amanda_group -o -r -d %{_localstatedir}/lib/amanda -s /bin/bash \
        -c "Amanda user" -u 33 %amanda_user >/dev/null 2>&1 || :
/usr/bin/gpasswd -a %amanda_user tape >/dev/null 2>&1 || :

%post
%{?ldconfig}
%systemd_post amanda.socket amanda-udp.socket kamanda.socket

%preun
%systemd_preun amanda.socket amanda-udp.socket kamanda.socket

%postun
%{?ldconfig}
%systemd_postun_with_restart amanda.socket amanda-udp.socket kamanda.socket

%ldconfig_scriptlets client
%ldconfig_scriptlets server

%files
%license COPYRIGHT COPYRIGHT.BSD
%doc ChangeLog NEWS README.md ReleaseNotes
%{_unitdir}/amanda@.service
%{_unitdir}/amanda.socket
%{_unitdir}/amanda-udp.service
%{_unitdir}/amanda-udp.socket
%{_unitdir}/kamanda@.service
%{_unitdir}/kamanda.socket

%dir %{_libexecdir}/amanda
%{_libexecdir}/amanda/amandad
%{_libexecdir}/amanda/amanda-sh-lib.sh
%attr(4750,root,%amanda_group) %{_libexecdir}/amanda/ambind
%{_libexecdir}/amanda/amndmjob
%if %{with gnuplot}
%{_libexecdir}/amanda/amcat.awk
%{_libexecdir}/amanda/amplot.awk
%{_libexecdir}/amanda/amplot.g
%{_libexecdir}/amanda/amplot.gp
%endif
%{_libexecdir}/amanda/ndmjob

%{_sbindir}/amandad
%{_sbindir}/amaespipe
%{_sbindir}/amarchiver
%{_sbindir}/amcrypt
%{_sbindir}/amcrypt-ossl
%{_sbindir}/amcrypt-ossl-asym
%{_sbindir}/amcryptsimple
%{_sbindir}/amgetconf
%{_sbindir}/amgpgcrypt
%if %{with gnuplot}
%{_sbindir}/amplot
%endif
%{_sbindir}/amssl

%{perl_vendorarch}/Amanda/
%{perl_vendorarch}/auto/Amanda/

%{_mandir}/man5/amanda-archive-format.5*
%{_mandir}/man7/amanda-compatibility.7*
%{_mandir}/man5/amanda.conf*
%{_mandir}/man7/amanda-auth.7*
%{_mandir}/man7/amanda-match.7*
%{_mandir}/man7/amanda-scripts.7*
%{_mandir}/man8/amanda.8*
%{_mandir}/man8/amarchiver.8*
%if %{with gnuplot}
%{_mandir}/man8/amplot.8*
%endif
%{_mandir}/man8/script-email.8*
%{_mandir}/man8/amaespipe.8*
%{_mandir}/man8/amcrypt-ossl-asym.8*
%{_mandir}/man8/amcrypt-ossl.8*
%{_mandir}/man8/amcryptsimple.8*
%{_mandir}/man8/amcrypt.8*
%{_mandir}/man8/amgpgcrypt.8*
%{_mandir}/man8/amgetconf.8*
%{_mandir}/man8/amcleanupdisk.8*
%{_mandir}/man7/amanda-auth-ssl.7.*
%{_mandir}/man8/amssl.8.*

%dir %{_sysconfdir}/amanda/
%dir %{_sysconfdir}/amanda/%defconfig

%attr(-,%amanda_user,%amanda_group)     %dir %{_localstatedir}/lib/amanda/
%attr(600,%amanda_user,%amanda_group)   %config(noreplace) %{_localstatedir}/lib/amanda/.amandahosts
%attr(02770,%amanda_user,%amanda_group) %dir /var/log/amanda
%attr(02770,%amanda_user,%amanda_group) %dir /var/log/amanda/amandad

%files libs
%{_libdir}/libamdevice*.so
%{_libdir}/libamserver*.so
%{_libdir}/libamclient*.so
%{_libdir}/libamanda-*.so
%{_libdir}/libamanda.so
%{_libdir}/libamandad*.so
%{_libdir}/libamar*.so
%{_libdir}/libamglue*.so
%{_libdir}/libamxfer*.so
%{_libdir}/libndmjob*.so
%{_libdir}/libndmlib*.so

%files server
%{_libexecdir}/amanda/amdumpd
%{_libexecdir}/amanda/amcheck-device
%{_libexecdir}/amanda/amidxtaped
%{_libexecdir}/amanda/amindexd
%{_libexecdir}/amanda/amlogroll
%{_libexecdir}/amanda/amtrmidx
%{_libexecdir}/amanda/amtrmlog
%{_libexecdir}/amanda/driver
%{_libexecdir}/amanda/amadmin_perl
%{_libexecdir}/amanda/ambackupd
%{_libexecdir}/amanda/rest-server/
%{_libexecdir}/amanda/dumper
%{_libexecdir}/amanda/chunker
%{_libexecdir}/amanda/planner
%{_libexecdir}/amanda/taper

%{_sbindir}/activate-devpay
%{_sbindir}/amaddclient
%{_sbindir}/amadmin
%{_sbindir}/amcleanup
%{_sbindir}/amcleanupdisk
%{_sbindir}/amdevcheck
%{_sbindir}/amdump
%{_sbindir}/amfetchdump
%{_sbindir}/amflush
%{_sbindir}/amcheck
%{_sbindir}/amcheckdb
%{_sbindir}/amcheckdump
%{_sbindir}/amlabel
%{_sbindir}/amoverview
%{_sbindir}/amreport
%{_sbindir}/amrestore
%{_sbindir}/amrmtape
%{_sbindir}/amserverconfig
%{_sbindir}/amservice
%{_sbindir}/amstatus
%{_sbindir}/amtape
%{_sbindir}/amtapetype
%{_sbindir}/amtoc
%{_sbindir}/amvault
%{_sbindir}/amanda-rest-server
%{_sbindir}/amreindex

%{_mandir}/man5/disklist.5*
%{_mandir}/man5/tapelist.5*
%{_mandir}/man5/amanda-command-file.5*
%{_mandir}/man7/amanda-devices.7*
%{_mandir}/man7/amanda-changers.7*
%{_mandir}/man7/amanda-interactivity.7*
%{_mandir}/man7/amanda-taperscan.7*
%{_mandir}/man8/amaddclient.8*
%{_mandir}/man8/amadmin.8*
%{_mandir}/man8/amcleanup.8*
%{_mandir}/man8/amdevcheck.8*
%{_mandir}/man8/amdump.8*
%{_mandir}/man8/amfetchdump.8*
%{_mandir}/man8/amflush.8*
%{_mandir}/man8/amcheckdb.8*
%{_mandir}/man8/amcheckdump.8*
%{_mandir}/man8/amcheck.8*
%{_mandir}/man8/amlabel.8*
%{_mandir}/man8/amoverview.8*
%{_mandir}/man8/amreport.8*
%{_mandir}/man8/amrestore.8*
%{_mandir}/man8/amrmtape.8*
%{_mandir}/man8/amserverconfig.8*
%{_mandir}/man8/amservice.8*
%{_mandir}/man8/amstatus.8*
%{_mandir}/man8/amtapetype.8*
%{_mandir}/man8/amtape.8*
%{_mandir}/man8/amtoc.8*
%{_mandir}/man8/amvault.8*
%{_mandir}/man8/amanda-rest-server.8.*
%{_mandir}/man8/amreindex.8.*
%{_mandir}/man1/activate-devpay.1*

%config(noreplace) %{_sysconfdir}/amanda/crontab.sample
%config(noreplace) %{_sysconfdir}/amanda/%defconfig/*
%exclude %{_sysconfdir}/amanda/%defconfig/amanda-client.conf
%exclude %{_sysconfdir}/amanda/%defconfig/amanda-client-postgresql.conf

%attr(-,%amanda_user,%amanda_group) %dir %{_localstatedir}/lib/amanda/%defconfig/
%attr(-,%amanda_user,%amanda_group) %dir %{_localstatedir}/lib/amanda/%defconfig/index
%attr(-,%amanda_user,%amanda_group) %dir %{_localstatedir}/lib/amanda/template.d
%attr(-,%amanda_user,%amanda_group) %config(noreplace) %{_localstatedir}/lib/amanda/template.d/*

%files client
%dir %{_libexecdir}/amanda/application/
%attr(4750,root,%amanda_group) %{_libexecdir}/amanda/application/ambsdtar
%attr(4750,root,%amanda_group) %{_libexecdir}/amanda/application/amgtar
%attr(4750,root,%amanda_group) %{_libexecdir}/amanda/application/amstar
%{_libexecdir}/amanda/application/amlog-script
%{_libexecdir}/amanda/application/ampgsql
%{_libexecdir}/amanda/application/amraw
%{_libexecdir}/amanda/application/amsamba
%{_libexecdir}/amanda/application/amsuntar
%{_libexecdir}/amanda/application/amzfs-sendrecv
%{_libexecdir}/amanda/application/amzfs-snapshot
%{_libexecdir}/amanda/application/script-email
%{_libexecdir}/amanda/application/amrandom
%{_libexecdir}/amanda/application/script-fail
%{_libexecdir}/amanda/restore
%{_libexecdir}/amanda/senddiscover

%attr(4750,root,%amanda_group) %{_libexecdir}/amanda/calcsize
%attr(4750,root,%amanda_group) %{_libexecdir}/amanda/killpgrp
%{_libexecdir}/amanda/noop
%{_libexecdir}/amanda/patch-system
%attr(4750,root,%amanda_group) %{_libexecdir}/amanda/rundump
%attr(4750,root,%amanda_group) %{_libexecdir}/amanda/runtar
%{_libexecdir}/amanda/selfcheck
%{_libexecdir}/amanda/sendbackup
%{_libexecdir}/amanda/sendsize
%{_libexecdir}/amanda/teecount

%{_sbindir}/amdump_client
%{_sbindir}/amoldrecover
%{_sbindir}/amrecover
%{_sbindir}/ambackup

%{_sysconfdir}/amanda/amanda-security.conf

%{_mandir}/man7/amanda-applications.7*
%{_mandir}/man8/amdump_client.8*
%{_mandir}/man5/amanda-client.conf.5*
%{_mandir}/man5/amanda-security.conf.5*
%{_mandir}/man8/ambsdtar.8*
%{_mandir}/man8/amgtar.8*
%{_mandir}/man8/ampgsql.8*
%{_mandir}/man8/amraw.8*
%{_mandir}/man8/amrecover.8*
%{_mandir}/man8/amoldrecover.8*
%{_mandir}/man8/amsamba.8*
%{_mandir}/man8/amstar.8*
%{_mandir}/man8/amsuntar.8*
%{_mandir}/man8/amzfs-sendrecv.8*
%{_mandir}/man8/amzfs-snapshot.8*
%{_mandir}/man8/killpgrp.8*
%{_mandir}/man8/ambackup.8.*

%config(noreplace) %{_sysconfdir}/amanda/%defconfig/amanda-client.conf
%config(noreplace) %{_sysconfdir}/amanda/%defconfig/amanda-client-postgresql.conf

%attr(-,%amanda_user,%amanda_group) %config(noreplace) %{_localstatedir}/lib/amanda/amandates
%attr(-,%amanda_user,%amanda_group) %{_localstatedir}/lib/amanda/gnutar-lists/
%attr(0644, root, root) %config(noreplace) %{_sysconfdir}/amanda-security.conf


%changelog
* Tue May 02 2023 Josef Ridky <jridky@redhat.com> - 3.5.3-3
- move to SPDX license format

* Fri Apr 14 2023 Florian Weimer <fweimer@redhat.com> - 3.5.3-2
- Port configure script to C99

* Thu Mar 16 2023 Orion Poplawski <orion@nwra.com> - 3.5.3-1
- Update to 3.5.3
- Fixes CVE-2022-37703 (bz#2126849) CVE-2022-37704 (bz#2168789) CVE-2022-37705 (bz#2168797)

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 30 2022 Orion Poplawski <orion@nwra.com> - 3.5.2-1
- Update to 3.5.2

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Jason L Tibbitts III <j@tib.bs> - 3.5.1-36
- Add patch to fix bug which caused a failing test.  Thanks to Peter Bieringer
  for the patch.

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.1-35
- Perl 5.36 rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 3.5.1-33
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.1-31
- Perl 5.34 rebuild

* Wed Mar 03 2021 Nikola Forró <nforro@redhat.com> - 3.5.1-30
- Use /usr/bin/mail as mailer

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.5.1-29
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Feb  9 2021 Pavel Cahyna <pcahyna@redhat.com> - 3.5.1-28
- Make the gnuplot dependency together with building of amplot optional.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jul 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-26
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.1-24
- Perl 5.32 rebuild

* Mon Feb 17 2020 Václav Doležal <vdolezal@redhat.com> - 3.5.1-23
- Drop support for 'dump' backend.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Václav Doležal <vdolezal@redhat.com> - 3.5.1-21
- Fix FTBFS caused by missing 'extern' on global variable (#1793391)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Orion Poplawski <orion@nwra.com> - 3.5.1-19
- Move ambind to amanda package (bug #1710147)

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.1-18
- Perl 5.30 rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.5.1-17
- Rebuild for readline 8.0

* Fri Feb 01 2019 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.5.1-16
- Add patch to specify xfsrestore housekeeping dir during index generation
  (#1671117)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 02 2018 Vaclav Dolezal <vdolezal@redhat.com> - 3.5.1-14
- modify permissions of /var/log/amanda/amandad directory due to SELinux issues

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 3.5.1-12
- Perl 5.28 rebuild

* Mon Apr 30 2018 Josef Ridky <jridky@redhat.com> - 3.5.1-11
- change /var/log/amanda directory permission due SELinux issues

* Thu Apr 12 2018 Josef Ridky <jridky@redhat.com> - 3.5.1-10
- remove perl(Dancer2) requirements

* Wed Feb 21 2018 Josef Ridky <jridky@redhat.com> - 3.5.1-9
- add RPM_LD_FLAGS to build section (#1547499)

* Thu Feb 15 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.5.1-8
- Fix embarrassing typo.

* Wed Feb 14 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.5.1-7
- Convert to ldconfig macros.

* Wed Feb 14 2018 Josef Ridky <jridky@redhat.com> - 3.5.1-6
- Remove Group tag

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.5.1-4
- Assign setuid permissions properly.

* Fri Jan 26 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.5.1-3
- Add patch to support tirpc and re-enable ndmp support.

* Thu Jan 25 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.5.1-2
- Use proper systemd package dependencies.
- Remove Obsoletes: for ancient amanda version.
- Remove obsolete Requires(post): dependencies.

* Mon Jan 08 2018 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.5.1-1
- Update to 3.5.1.
- Pass --without-ndmp and remove ndmp-related files until we can get the ndmp
  code to use libtirpc.

* Tue Nov 07 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.5-2
- Remove old crufty coreutils requires

* Thu Sep 28 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.5-1
- Update to 3.5.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.4.5-3
- Modify amserverconfig to not mention xinetd (#1460763)

* Fri Jun 09 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.5-2
- Perl 5.26 rebuild

* Thu Jun 08 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.4.5-1
- New upstream release 3.4.5.

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 3.4.4-2
- Perl 5.26 rebuild

* Wed May 03 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.4.4-1
- New upstream relase 3.4.4.

* Thu Mar 02 2017 Josef Ridky <jridky@redhat.com> - 3.4.3-1
- New upstream release 3.4.3 (#1428185)

* Wed Mar  1 2017 Josef Ridky <jridky@redhat.com> - 3.4.2-4
- Fix issue with local authentication (#1427775)

* Mon Feb 20 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.4.2-3
- Add patch from upstream to fix a segfault in planner.  Hopefully fixes
  https://bugzilla.redhat.com/show_bug.cgi?id=1423471

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.4.2-1
- Update to 3.4.2.
- Remove upstreamed patches.
- Add patch to allow builds on non-x86 arches.
- Move autogen call from %%prep to %%build.
- Remove some specfile cruft.
- Use %%license.

* Tue Jan 31 2017 Josef Ridky <jridky@redhat.com> - 3.4.1-4
- Fix warning with checking return value from setreuid in krb5-security.c (#1417828)

* Fri Jan 13 2017 Jason L Tibbitts III <tibbs@math.uh.edu> - 3.4.1-3
- Add patch to avoid breakage with RHEL5 clients.

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.4.1-2
- Rebuild for readline 7.x

* Tue Dec 06 2016 Josef Ridky <jridky@redhat.com> - 3.4.1-1
- New upstream release 3.4.1 (#1398045)

* Wed Nov 16 2016 Josef Ridky <jridky@redhat.com> - 3.4-5
- add BuildRequires dependency for dump and xfsdump - (#1395445)

* Thu Nov 10 2016 Josef Ridky <jridky@redhat.com> - 3.4-4
- Update amanda spec file (thanks Jason Tibbitts for optimalization) - (#1386434)

* Wed Oct 26 2016 Josef Ridky <jridky@redhat.com> - 3.4-3
- Upstream fix of broken dependencies

* Mon Oct 24 2016 Josef Ridky <jridky@redhat.com> - 3.4-2
- Add Requires for server package

* Wed Oct 19 2016 Josef Ridky <jridky@redhat.com> - 3.4-1
- New upstream release 3.4 (#1386434) - resolves (#1384065)

* Thu Aug 18 2016 Josef Ridky <jridky@redhat.com> - 3.3.9-3
- Add security configuration file into /etc folder (#1368021)

* Thu Aug  4 2016 Josef Ridky <jrikdy@redhat.com> - 3.3.9-2
- Fix Tie::StdHash permission problem (#1257686)

* Wed Jul 27 2016 Josef Ridky <jridky@redhat.com> - 3.3.9-1
- New upstream release 3.3.9 (#1360703)
- Remove Require(pre) from .spec file (unimportant here) (#1319129)

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 3.3.8-3
- Perl 5.24 rebuild

* Fri Mar 11 2016 Petr Pisar <ppisar@redhat.com> - 3.3.8-2
- Do not provide private libraries (bug #1309664)

* Tue Feb 09 2016 Petr Hracek <phracek@redhat.com> - 3.3.8-1
- New upstream release 3.3.8

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.7p1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Petr Hracek <phracek@redhat.com> - 3.3.7p1-1
- Update to 3.3.7p1 version
- fixed bug (#1225841)

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 3.3.6-11
- Perl 5.22 rebuild

* Fri Feb 27 2015 Petr Hracek <phracek@redhat.com> - 3.3.6-10
- Fix for Swig-3.0.5 (#1195297)

* Fri Nov 21 2014 Petr Hracek <phracek@redhat.com> - 3.3.6-9
- inlude unit files for systemd

* Fri Nov 21 2014 Petr Hracek <phracek@redhat.com> - 3.3.6-8
- add kamanda unit files (#1077642)

* Tue Nov 11 2014 Petr Hracek <phracek@redhat.com> - 3.3.6-7
- Resolves #1033896 Add amindexd as argument to amandad

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.3.6-6
- Perl 5.20 rebuild

* Wed Sep 03 2014 Petr Hracek <phracek@redhat.com> - 3.3.6-5
- FTBFS with perl 5.20 (#1134732)

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 3.3.6-4
- Perl 5.20 rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Petr Hracek <phracek@redhat.com> - 3.3.6-2
- amstatus perl script is broken due to misconfiguration of $PS (#1074216)

* Thu Jul 10 2014 Orion Poplawski <orion@cora.nwra.com> - 3.3.6-1
- Update to 3.3.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Orion Poplawski <orion@cora.nwra.com> - 3.3.5-1
- Update to 3.3.5
- Drop stdio patch, fixed upstream

* Tue Apr 08 2014 Petr Hracek <phracek@redhat.com> - 3.3.3-11
- Remove initscripts from dependencies (#1081399)

* Fri Jan 31 2014 Petr Hracek <phracek@redhat.com> - 3.3.3-10
- Fix: #1056675 systemd file incorrectly named (missing file in install section)

* Fri Jan 31 2014 Petr Hracek <phracek@redhat.com> - 3.3.3-9
- Fix: #1056675 systemd file incorrectly named

* Mon Oct 21 2013 Petr Hracek <phracek@redhat.com> - 3.3.3-8
- Moved all dynamic libraries to amanda-libs (#881128)
- Added dependencies to client and server on amanda-libs

* Mon Oct 21 2013 Petr Hracek <phracek@redhat.com> - 3.3.3-7
- package amanda-libs introduced because of multilib issue

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 3.3.3-5
- Perl 5.18 rebuild

* Tue Jul 16 2013 Petr Hracek <phracek@redhat.com> - 3.3.3-4
- Correct problem with man page killpgrp (#881128)

* Tue Jun 25 2013 Petr Hracek <phracek@redhat.com> - 3.3.3-3
- Remove dependency on dump in RHEL-7

* Tue Jun 18 2013 Petr Hracek <phracek@redhat.com> - 3.3.3-2
- Added systemd udp unit files

* Fri Mar 22 2013 Petr Hracek <phracek@redhat.com> - 3.3.3-1
- New upstream version
- Dependecy to /usr/sbin/service was removed.
 Instead of /usr/sbin/service systemd files are used.

* Thu Mar 21 2013 Petr Hracek <phracek@redhat.com> - 3.3.2-5
- Fix (#924326) Requires /sbin/service was changed to /usr/sbin/service

* Thu Jan 31 2013 Petr Hracek <phracek@redhat.com> - 3.3.2-4
- fix (#858703) add killpgrp(8) man page to the amanda-client package
    (killpgrp will be removed from man-pages package)
- Fix autogen for parallel tests.

* Thu Dec 06 2012 Lukáš Nykrýn <lnykryn@redhat.com> - 3.3.2-3
- Fix group ownership
- Add manpage for activate-devpay

* Tue Sep 18 2012 Petr Pisar <ppisar@redhat.com> - 3.3.2-2
- Do not provide perl(Math::BigInt) (bug #648321)

* Wed Aug 15 2012 Lukáš Nykrýn <lnykryn@redhat.com> - 3.3.2-1
- upgrade to new upstream release
- convert to systemd

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Petr Pisar <ppisar@redhat.com> - 3.3.1-2
- Perl 5.16 rebuild

* Wed Jun 20 2012 Lukáš Nykrýn <lnykryn@redhat.com> - 3.3.1-1
- upgrade to new upstream release

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 3.3.0-6
- Perl 5.16 rebuild

* Wed Apr 18 2012 Lukáš Nykrýn <lnykryn@redhat.com>> - 3.3.0-5
- Fix building issues with newer glib

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 28 2011 Lukáš Nykrýn <lnykryn@redhat.com> - 3.3.0-3
- fix #757618 - Use of qw(...) as parentheses is deprecated
- fix #752253 - Using functions in amanda-client which are provided by server

* Thu Jun 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 3.3.0-2
- Perl mass rebuild

* Wed Jun 08 2011 Jan Görig <jgorig@redhat.com> - 3.3.0-1
- upgrade to new upstream release
- uses bsdtcp authentication by default
- dropped amanda-3.1.1-bsd.patch
- modified example directory handling and dropped amanda-3.1.0-example.patch

* Wed May 4 2011 Jan Görig <jgorig@redhat.com> - 3.3.0-0.1.beta1
- update to new upstream beta release
- removed merged patch amanda-3.2.2-krb5-libs.patch

* Wed Apr 27 2011 Jan Görig <jgorig@redhat.com> - 3.2.2-2
- amgtar, amstar and amservice must have setuid flag (#697933)

* Wed Mar 16 2011 Jan Görig <jgorig@redhat.com> - 3.2.2-1
- upgrade to new upstream release
- removed merged patch amanda-3.1-amrestore.patch
- fixed build on system with amanda installed

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Jan Görig <jgorig@redhat.com> - 3.2.1-2
- fix #666968 - amrestore should restore one file when outputting to a pipe

* Wed Dec 15 2010 Jan Görig <jgorig@redhat.com> - 3.2.1-1
- upgrade to new upstream release
- removed unneeded patches

* Thu Nov 4 2010 Jan Görig <jgorig@redhat.com> - 3.2.0-1
- upgrade to new upstream release
- fixed build with new glib
- changed owner of the most files to root
- moved variable files from /etc/amanda to /var/lib/amanda
- spec cleanups
- fix #648321 - amanda rpm should not provide the perl(Math::BigInt)

* Thu Oct 7 2010 Jan Görig <jgorig@redhat.com> - 3.1.3-1
- upstream security update

* Wed Aug 18 2010 Jan Görig <jgorig@redhat.com> - 3.1.2-1
- upgraded to new upstream bugfix version

* Tue Aug 10 2010 Jan Görig <jgorig@redhat.com> - 3.1.1-2
- removed obsolete README-rpm
- modified client configuration to match xinetd one
- modified tcpport patch to include postgresql sample configuration

* Tue Aug 03 2010 Jan Görig <jgorig@redhat.com> - 3.1.1-1
- upgraded to new upstream bugfix version
- dropped old upgrade scriptlets
- spec cleanups
- created symlink to manpage for amoldrecover
- default configuration now backups extended attributes
- fix #610169 - fixed build flags
- fix #600552 - corrected amdatadir path, updated example patch

* Mon Jun 28 2010 Jan Görig <jgorig@redhat.com> - 3.1.0-1
- upgraded to new upstream version
- documentation moved to main package
- fixed license tag
- moved files from libexecdir to libdir to avoid multilib conflict
- moved files between subpackages
- updated path in xinetd config
- added -fPIE to CFLAGS and -pie to LDFLAGS
- removed unused patches
- removed obsolete devel subpackage

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.6.1p2-4
- Mass rebuild with perl-5.12.0

* Thu Apr 22 2010 Daniel Novotny <dnovotny@redhat.com> 2.6.1p2-3
- fix #584774 - PIE patch disabled in amanda 2.6.1p2-2

* Tue Feb 16 2010 Daniel Novotny <dnovotny@redhat.com> 2.6.1p2-2
- fix #564935 -  FTBFS amanda-2.6.1p2-1.fc13

* Thu Jan 21 2010 Daniel Novotny <dnovotny@redhat.com> 2.6.1p2-1
- upgrade to 2.6.1p2, drop upstreamed patches, rebase remaining patches

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 2.6.0p2-15
- rebuild against perl 5.10.1

* Thu Oct 15 2009 Daniel Novotny <dnovotny@redhat.com> 2.6.0p2-14
- add amanda user to group "tape" (#529159)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.6.0p2-13
- rebuilt with new openssl

* Tue Aug 04 2009 Daniel Novotny <dnovotny@redhat.com> 2.6.0p2-12
-fix #512534 -  amstatus outputs "Insecure dependency in printf ..."

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0p2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Daniel Novotny <dnovotny@redhat.com> 2.6.0p2-10
- fix #510961 -  FTBFS: amanda-2.6.0p2-9

* Fri Apr 24 2009 Daniel Novotny <dnovotny@redhat.com> 2.6.0p2-9
- fix #497488 -  amanda subpackages require only a specific version of amanda,
      not also release

* Tue Apr 14 2009 Daniel Novotny <dnovotny@redhat.com> 2.6.0p2-8
- fix #495724 (spec file fix, use "useradd -N" instead of "useradd -n")

* Wed Apr 08 2009 Daniel Novotny <dnovotny@redhat.com> 2.6.0p2-7
- the tcpport patch was lost after rebase, adding again
  (#448071, #462681)

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0p2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Tomas Mraz <tmraz@redhat.com> 2.6.0p2-5
- rebuild with new openssl

* Thu Nov 20 2008 Daniel Novotny <dnovotny@redhat.com> 2.6.0p2-4
  .usernameupdate extension changed to .rpmsave (#472349)

* Thu Oct 23 2008 Daniel Novotny <dnovotny@redhat.com> 2.6.0p2-3
- added trailing || : in the %%pre client script

* Fri Oct 10 2008 Orion Poplawski <orion@cora.nwra.com> 2.6.0p2-2
- Drop duplicated libamglue.so from -devel
- Update -pie patch
- Fix Source typo
- Move xinetd to main package - used by both client and server
- Move %%{_libexecdir}/amanda/amanda-sh-lib.sh to main package
- LIBEXECDIR is used in xinetd template
- Make calcsize setuid root

* Wed Oct 01 2008 Daniel Novotny 2.6.0p2-1
- Update to 2.6.0p2
- perl-ExtUtils-Embed added to BuildRequires
- perl patch dropped (upstreamed)
- library name change from libamglue.so.* to libamglue.so

* Thu Mar 27 2008 Orion Poplawski <orion@cora.nwra.com> 2.6.0-0.b3_20080314.1
- Update to 2.6.0b3_20080314
- New -lib patch that patches the autotool source files

* Tue Mar 11 2008 Orion Poplawski <orion@cora.nwra.com> 2.6.0-0.b3_20080310.1
- Update to 2.6.0b3_20080310
- Re-add updated pie patch, re-add autogen
- Update example patch to modify Makefile.am, leave template.d in
 /var/lib/amanda for now

* Wed Feb 20 2008 Orion Poplawski <orion@cora.nwra.com> 2.6.0-0.b2_20080220.1
- Update to 2.6.0b2-20080220
- Drop libdir patch, use --with-libdir instead
- Move perl modules to %%{perl_vendorarch} and add perl Requires

* Wed Feb 20 2008 Orion Poplawski <orion@cora.nwra.com> 2.6.0-0.b2
- Update to 2.6.0b2, drop upstreamed patches
- Update xattrs patch
- Add patches to fix install locations
- Add -fPIE/-pie to CFLAGS/LDFLAGS, drop pie patch
- Drop autotools BR
- Drop /usr/bin/Mail BR and specify mailer as /bin/mail
- Add %%check section
- Move /etc/amanda/amandates to /var/lib/amanda/amandates
- Remove ending . from summaries

* Mon Feb 18 2008 Radek Brich <rbrich@redhat.com> 2.5.2.p1-10
- do not require gnuplot by -server subpackage (bz#433101)

* Thu Nov 22 2007 Radek Brich <rbrich@redhat.com> 2.5.2.p1-9
- Change default amanda user name to 'amandabackup' (#124510).
  This should not break upgrades as config files are checked for
  old user name and updated.
- Add some explaining comments to .amandahosts (#153749)

* Tue Aug 28 2007 Radek Brich <rbrich@redhat.com> 2.5.2.p1-8
- rebuild

* Fri Aug 17 2007 Radek Brich <rbrich@redhat.com> 2.5.2.p1-7
- BuildRequires mtx and mt-st (#251690).

* Fri Aug 10 2007 Radek Brich <rbrich@redhat.com> 2.5.2.p1-6
- Included upstream patch for chg-multi.sh (#251316).

* Wed Aug 08 2007 Radek Brich <rbrich@redhat.com> 2.5.2.p1-5
- Added ssh and ncompress to BuildRequires (#250730).
- Removed some obsolete makes from build section.

* Thu Jul 12 2007 Radek Brich <rbrich@redhat.com> 2.5.2.p1-4
- Enable backing up ACL/SElinux xattrs with tar (#201916).
- Removed obsolete patches and sources.

* Mon Jun 25 2007 Radek Brich <rbrich@redhat.com> 2.5.2.p1-3
- Update -undefSymbols patch. All undefined symbols reported by
  'ldd -r' should now be fixed (#198178).

* Fri Jun 22 2007 Radek Brich <rbrich@redhat.com> 2.5.2.p1-2
- Fix undefined symbols in libamserver.so.
- Fix ./autogen so it automatically installs ylwrap (bug 224143).
- Run ./autogen in prep section (otherwise the -pie patch had no effect).
- Update -pie patch.

* Thu Jun 21 2007 Radek Brich <rbrich@redhat.com> 2.5.2.p1-1
- New upstream version.
- Client rpm now installs amanda-client.conf.
- Removed obsolete patches -bug18322 and -rsh.
- Clean up spec file (non-utf8 error and some warnings from rpmlint).

* Mon Feb 19 2007 Jay Fenlason <fenlason@redhat.com> 2.5.1p3-1%{?dist}
- Upgrade to new upstream release, now that 2.5.1 is somewhat stable.
- Note that this requires changing the xinetd configuration and amanda.conf
  because of the new authentication mechanism.
- -server subpackage does not require xinetd.
- -server scriptlets do not need to reload xinetd.

* Mon Sep 25 2006 Jay Fenlason <fenlason@redhat.com> 2.5.0p2-4
- Include my -dump_size patch to close
  bz#206129: Dump output size determined incorrectly
- Clean up the spec file, following some suggestions in
  bz#185659: amanda 2.5.0
- Use a tarball without the problematic contrib/sst directory.
- Include my new_gnutar (based on a patch by Orion Poplawski
  <orion@cora.nwra.com>) to work around changed incremental file format
  in newer (>1.15.1) versions of gnutar.
- include my -wildcards patch to turn on wildcards with new versions of tar.

* Tue Sep 5 2006 Jay Fenlason <fenlason@redhat.com> 2.5.0p2-3
- move libamclient-*.so to the base rpm, so that multilib support works.
  This fixes
  bz#205202 File conflicts

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.5.0p2-2.1
- rebuild

* Thu Jun 8 2006 Jay Fenlason <fenlason@redhat.com> 2.5.0p2-2
- New upstream version
- Make the BuildRequires on /usr/bin/Mail rather than mailx, because we
  don't really care where the Mail command comes from.
- include the amcheck_badtape patch by Paul Bijnens
  <paul.bijnens@xplanation.com> to fix a problem where amcheck doesn't
  realize the wrong tape is in the drive.
- include the error_msg patch from Jean-Louis Martineau <martineau@zmanda.com>
  to fix a double-free problem
- include the restore patch from Jean-Louis Martineau <martineau@zmanda.com>
  to fix an error in amrestore
- include a slightly modified form of the big_holding_disk patch from
  Andrej Filipcic <andrej.filipcic@ijs.si> to fix a problem with holding
  disks bigger than 4tb

* Mon May 22 2006 Jesse Keating <jkeating@redhat.com> 2.5.0-3
- Fix BuildReqs

* Fri Apr 7 2006 Jay Fenlason <fenlason@redhat.com> 2.5.0-2
- New upstream release: 2.5.0, with new features
- Do not include our own amanda.conf anymore, use the one from the
  tarball.
- Remove the static libraries.
- Update the -pie patch
- Turn on the new -with-ssh-security option.
- Change the mode of ~amanda/.amandahosts to 600, since 2.5.0 requires
  it.
- actually use the defconfig macro it this spec file.
- Change the name of the index server to "amandahost" from localhost.
  Users should ensure that "amandahost.their-domain" points to their
  Amanda server.
- Change amandahosts likewise.
- Add dependency on /usr/bin/Mail
- Ensure unversioned .so files are only in the -devel rpm.
- Remove DUMPER_DIR and the files in it, as nothing seems to actually
  use them.
- Include the -overflow patch from Jean-Louis Martineau
  <martineau@zmanda.com>

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.4.5p1-3.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.4.5p1-3.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Jay Fenlason <fenlason@redhat.com> 2.4.5p1-3
- Fix spec file to use %%{_localstatedir} instead of hardcoding /var/lib
- Add amanda_user and amanda_group defines, to make changing the username
  easier.
- Add a BuildRequires on /usr/bin/Mail

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 4 2005 Jay Fenlason <fenlason@redhat.com>
- New upstream release.

* Sun Jul 31 2005 Florian La Roche <laroche@redhat.com>
- make sure amanda builds with newest rpm

* Wed Apr 20 2005 Jay Fenlason <fenlason@redhat.com> 2.4.5-2
- New upstream release.  This obsoletes the -bug144052 patch.
- Reorg this spec file slightly to allow someone to specify
  index server, tape server and default configuration when
  rebuilding the rpms via something like
  'rpmbuild -ba --define "indexserver foo.fqdn.com" amanda.spec'
  This change suggested by Matt Hyclak <hyclak@math.ohiou.edu>.

* Tue Apr 5 2005 Jay Fenlason <fenlason@redhat.com> 2.4.4p4-4
- Add -bug144052 patch to close
  bz#144052 amverifyrun sometimes verifies the wrong tapes

* Tue Mar 8 2005 Jay Fenlason <fenlason@redhat.com> 2.4.4p4-3
- rebuild with gcc4

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> 2.4.4p4-2
- Rebuilt for new readline.

* Mon Oct 25 2004 Jay Fenlason <fenlason@redhat.com> 2.4.4p4-1
- New upstream version
- Turn on --disable-dependency-tracking to work around an automake bug.

* Mon Jun 28 2004 Jay Fenlason <fenlason@redhat.com> 2.4.4p3-1
- New upstream version

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Mar 19 2004 Jay Fenlason <fenlason@redhat.com> 2.4.4p2-3
- make a few more programs PIE by updating the amanda-2.4.4p2-pie.path

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jan 13 2004 Jay Fenlason <fenlason@redhat.com> 2.4.4p2-1
- New upstream version, includes the -sigchld and -client-utils
  patches.  Also includes a new chg-disk changer script and a new
  amqde "quick-and-dirty estimate" program (called from sendsize--not
  a user command.

* Wed Jul 23 2003 Jay Fenlason <fenlason@redhat.com> 2.4.4p1-1
- Merge from 2.4.4p1-0.3E

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 26 2003 Jay Fenlason <fenlason@redhat.com> 2.4.4-0
- New upstream version.

* Thu Feb 13 2003 Jay Fenlason <fenlason@redhat.com> 2.4.3-3
- Removed call to signal(SIGCHLD, SIG_IGN) which prevents wait...()
  from working on newer Red Hat systems.  This fixes bug #84092.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Dec 11 2002 Jay Fenlason <fenlason@redhat.com> 2.4.3-2
- Add spec file entry for /usr/lib/amanda so owner/group set
  correctly  Fixes bugs 74025 and 73379.

* Wed Nov 20 2002 Elliot Lee <sopwith@redhat.com> 2.4.3-1
- Update to version 2.4.3, rebuild
- Update patch for bug18322 to match

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Apr  2 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.4.2p2-7
- Don't strip explicitly
- Require samba-client instead of /usr/bin/smbclient

* Thu Feb 21 2002 Trond Eivind Glomsrød <teg@redhat.com> 2.4.2p2-6
- Rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Jul 13 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Build and install the "tapetype"  utility program, for
  tape size identification (#48745)

* Tue Jun 19 2001 Trond Eivind Glomsrød <teg@redhat.com>
- don't use %%configure, to make it build

* Mon Apr  9 2001 Bill Nottingham <notting@redhat.com>
- include ia64 again

* Wed Apr  4 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 2.4.2p2 - fixes problems with amrecover (#26567)
- made config files noreplace
- don't build on IA64 right now, amanda doesn't like
  the dump there: It segfaults.

* Fri Mar 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Add /usr/bin/smbclient to buildprereq (#31996), to
  avoid samba being built without such support

* Thu Feb 22 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Use %%{version} in source URL, and thus actually use
  2.4.2p1 instead of 2.4.2 (doh! # 28759)
- add patch to handle bogus /dev/root entries (#28759)

* Fri Feb 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 2.4.2p1 bugfix release
- move amandaixd and amidxtape to the server package (#28037)

* Wed Jan 31 2001 Trond Eivind Glomsrød <teg@redhat.com>
- move /etc/xinetd.d/amanda to the client subpackage (#25430)

* Tue Jan 30 2001 Trond Eivind Glomsrød <teg@redhat.com>
- don't have "chunksize -1" as the default, as it's no longer
  supported
- make it uid amanda, with home /var/lib/amada
  so programs can actually access it (#20510)
- make .amandahosts a config file (#18322)

* Tue Jan 23 2001 Trond Eivind Glomsrød <teg@redhat.com>
- 2.4.2
- make the UDP service "wait" (#23047)

* Tue Oct 10 2000 Jeff Johnson <jbj@redhat.com>
- build with shared libraries.
- add amanda-devel package to contain static libraries.
- update to 2.4.2-19991216-beta1 (#16818).
- sort out client-server file confusions (#17232).
- amandaidx-xinetd should have "wait = no" (#17551).
- /var/lib/amanda needs operator.disk ownership (17913).
- /etc/xinetd.d/amanda added to the amanda-server package (#18112).
- ignore socket error message (#18322).

* Sun Sep  3 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- do not include /etc/xinetd.d/amandaidx in the server rpm

* Mon Aug 21 2000 Trond Eivind Glomsrød <teg@redhat.com>
- only do reload of xinetd if xinetd is running (#16653)
- don't show output of reload command to STDOUT (#16653)
- don't use /usr/sbin/tcpd in amidx, xinetd is linked
  with tcp_wrappers
- prereq initscripts (fixes #14572 and duplicates)

* Tue Aug  1 2000 Bill Nottingham <notting@redhat.com>
- turn off amandaidx by default (#14937)
- fix some binary permissions (#14938)

* Tue Aug  1 2000 Matt Wilson <msw@redhat.com>
- added Prereq: /sbin/service xinetd to client and server subpackages

* Tue Jul 18 2000 Trond Eivind Glomsrød <teg@redhat.com>
- xinetd support

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Jeff Johnson <jbj@redhat.com>
- add prereqs for scriptlets, requires for common package.

* Sat Jun 10 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.
- move to 7.0 distro.

* Tue May 23 2000 Tim Powers <timp@redhat.com>
- built for 7.0
- man pages in /usr/share/man

* Thu Apr 27 2000 Tim Powers <timp@redhat.com>
- added usr/lib/amanda/chg-zd-mtx to the client RPM to fix bug #8282

* Wed Mar 8 2000 Tim Powers <timp@redhat.com>
- fixed files/dirs ending up in the wrong packages.
- last time it wasn't built with dump (doh!), this time it is. Now has a
  BuildRequires for dump.

* Thu Feb 10 2000 Tim Powers <timp@redhat.com>
- strip binaries

* Fri Jan 21 2000 TIm Powers <timp@redhat.com>
- added chown lines to post section

* Tue Jan 11 2000 Tim Powers <timp@redhat.com>
- make sure the man pages are gzipped in each subpackage, overriding the build
  system spec_install_post macro.
- using mega spec file changes from Marc Merlin <merlin_bts@valinux.com> since
  the package we were shipping in the past had some major issues (not in
  Marc's words ;)
- using Marc's added README and modified config files.
- adapted patches written by Alexandre Oliva <oliva@dcc.unicamp.br> from Marc
  Merlin's package so that the patch matches the source version (the patches
  are the glibc2.1 and glibc2.2 patches)

* Mon Jan 3 2000 Tim Powers <timp@redhat.com>
- fix so configure doesn't crap out (libtoolize --force)
- gzip man pages, strip binaries
- rebuilt for 6.2

* Thu Aug 5 1999 Tim Powers <timp@redhat.com>
- applied patch so that it reports the available holding disk space correctly

* Thu Jul 8 1999 Tim Powers <timp@redhat.com>
- added %%defattr lines
- rebuilt for 6.1

* Wed May 05 1999 Bill Nottingham <notting@redhat.com>
- update to 2.4.1p1

* Tue Oct 27 1998 Cristian Gafton <gafton@redhat.com>
- version 2.4.1

* Tue May 19 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to full 2.4.0 release

* Thu Feb 19 1998 Otto Hammersmith <otto@redhat.com>
- fixed group for -client and -server packages (Network->Networking)

* Wed Feb 11 1998 Otto Hammersmith <otto@redhat.com>
- updated to 2.4.0b6, fixes security hole among other things
  (as well as finally got the glibc patch in the main source.)

* Tue Jan 27 1998 Otto Hammersmith <otto@redhat.com>
- moved versionsuffix to client package to remove dependency of amanda on amanda-client

* Mon Jan 26 1998 Otto Hammersmith <otto@redhat.com>
- fixed libexec garbage.

* Wed Jan 21 1998 Otto Hammersmith <otto@redhat.com>
- split into three packages amanda, amanda-client, and amanda-server

* Fri Jan  9 1998 Otto Hammersmith <otto@redhat.com>
- updated to latest beta... builds much cleaner now.

* Thu Jan  8 1998 Otto Hammersmith <otto@redhat.com>
- created the package

