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
Version:       3.5.4
Release:       %autorelease
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
Patch8: amanda-c99.patch

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
BuildRequires: libxslt docbook-dtds docbook-style-xsl
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
           --enable-manpage-build \
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
%autochangelog
