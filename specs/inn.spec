%global _hardened_build 1

Summary: The InterNetNews system, an Usenet news server
Name: inn
Version: 2.7.3
Release: 4%{?dist}
# most files are under ISC, except:
# contrib/analyze-traffic.in: public-domain
# contrib/mm_ckpasswd: GPL-2.0-or-later
# contrib/nnrp.access2readers.conf.in: public-domain
# contrib/tunefeed.in: Perl
# control/perl-nocem.in: GPL
# control/pgpverify.in: BSD-4-Clause
# innd/tinyleaf.c: MIT
# innfeed/config_y.[ch]: GPL-3.0-or-later with Bison-exception-2.2 exception
# lib/hashtab.c: public-domain
# lib/md5.c: NTP
# lib/newsuser.c: public-domain
# lib/sd-daemon.c: FSFAP
# lib/vector.c: FSFAP
# include/inn/hashtab.h: public-domain
# include/inn/md5.h: NTP
# include/inn/newsuser.h: public-domain
# include/inn/tst.h: BSD-3-Clause
# include/inn/vector.h: FSFAP
# include/portable/sd-daemon.h: FSFAP
License: ISC AND BSD-3-Clause AND BSD-4-Clause AND FSFAP AND (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-3.0-or-later WITH Bison-exception-2.2 AND LicenseRef-Fedora-Public-Domain AND MIT AND NTP
URL: https://www.eyrie.org/~eagle/software/inn/
Source0: https://downloads.isc.org/isc/inn/inn-%{version}.tar.gz
Source1: https://downloads.isc.org/isc/inn/inn-%{version}.tar.gz.asc
Source2: inn-default-distributions
# gpg2 --recv-key 0xD73934B49674CF5CCD9AC2787D80315C5736DE75
# gpg2 --export --export-options export-minimal 0xD73934B49674CF5CCD9AC2787D80315C5736DE75
Source3: 0xD73934B49674CF5CCD9AC2787D80315C5736DE75.gpg
Source10: http://www.eyrie.org/~eagle/faqs/inn.html#/inn-faq-%{version}.html
Source20: innd.service
Source21: innd-expire.service
Source22: innd-expire.timer
Source23: innd-nntpsend.service
Source24: innd-nntpsend.timer
Source25: innd-rnews.service
Source26: innd-rnews.timer
Source30: inn.rsyslog
# Fedora-specific paths and configuration settings
Patch0: inn-fedora.patch
BuildRequires: autoconf
BuildRequires: byacc
BuildRequires: cyrus-sasl-devel
BuildRequires: e2fsprogs-devel
BuildRequires: flex
BuildRequires: gcc
BuildRequires: gdbm-devel
BuildRequires: krb5-devel
BuildRequires: libdb-devel
BuildRequires: libcanlock-devel
BuildRequires: libxcrypt-devel
BuildRequires: openssl
BuildRequires: openssl-devel
BuildRequires: pam-devel
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::Embed)
BuildRequires: perl(GD)
BuildRequires: perl(MIME::Parser)
BuildRequires: perl(subs)
BuildRequires: perl(Test::MinimumVersion)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Pod)
BuildRequires: python3-devel
BuildRequires: sqlite-devel
BuildRequires: systemd-rpm-macros
BuildRequires: wget
BuildRequires: zlib-devel
BuildRequires: %{_bindir}/gpgv2
BuildRequires: make
%if 0%{?fedora} || 0%{?rhel} >= 8
Recommends: perl(GD)
Recommends: perl(subs)
Recommends: uucp
%endif
Requires: bash >= 2.0
Requires: coreutils
Requires: grep
Requires: sed
Requires: wget
Requires(post): inews

# XXX white out bogus perl requirement for now
Provides: perl(::usr/lib/innshellvars.pl) = %{version}-%{release}


%description
INN (InterNetNews) is a complete system for serving Usenet news and/or
private newsfeeds. INN includes innd, an NNTP (NetNews Transfer Protocol)
server, and nnrpd, a news server that handles connections from news
readers.

Install the inn package if you need a complete system for posting,
injecting, relaying and serving Usenet news. You may also need to
install inn-devel, if you are going to use a separate program which
interfaces to INN, like newsgate or tin.

%package devel
Summary: The INN (InterNetNews) library
Requires: inn = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}

%description devel
The inn-devel package contains the INN (InterNetNews) library, which
several programs that interface with INN need in order to work (for
example, newsgate and tin).

If you are installing a program which must interface with the INN news
system, you should install inn-devel.

%package -n inews
Summary: Sends Usenet articles to a local news server for distribution

%description -n inews
The inews program is used by some news programs (for example, inn and
trn) to post Usenet news articles to local news servers.  Inews reads
an article from a file or standard input, adds headers, performs some
consistency checks and then sends the article to the local news server
specified in the inn.conf file.

Install inews if you need a program for posting Usenet articles to
local news servers.

%package libs
Summary: Libraries provided by INN

%description libs
This package contains dynamic libraries provided by INN project

%prep
gpgv2 --keyring %{S:3} %{S:1} %{S:0}
%autosetup -p1

# Create a sysusers.d config file
cat >inn.sysusers.conf <<EOF
g news 13
g uucp 14
u news 9 'News server user' /etc/news -
u uucp 10 'Uucp user' /var/spool/uucp -
EOF

%build
%configure \
  --disable-static \
  --enable-largefiles \
  --enable-reduced-depends \
  --enable-shared \
  --enable-uucp-rnews \
  --bindir=%{_libexecdir}/news \
  --exec-prefix=%{_libexecdir}/news \
  --sysconfdir=%{_sysconfdir}/news \
  --with-canlock \
  --with-db-dir=%{_sharedstatedir}/news \
  --with-http-dir=%{_sharedstatedir}/news/http \
  --with-libperl-dir=%{perl_vendorlib} \
  --with-log-dir=/var/log/news \
  --with-openssl \
  --with-perl \
  --with-pic \
  --with-python \
  --with-run-dir=/run/news \
  --with-sasl \
  --with-sendmail=/usr/sbin/sendmail \
  --with-spool-dir=/var/spool/news \
  --with-tmp-dir=%{_sharedstatedir}/news/tmp \
  --with-news-group=news \
  --with-news-master=news \
  --with-news-user=news \

# Don't hardcode rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_sharedstatedir}/news/http
%make_install

# -- Install man pages needed by suck et al.
mkdir -p $RPM_BUILD_ROOT%{_includedir}/inn

for f in system.h libinn.h storage.h options.h dbz.h
do
    install -p -m 0644 ./include/inn/$f $RPM_BUILD_ROOT%{_includedir}/inn
done

touch     $RPM_BUILD_ROOT%{_sharedstatedir}/news/subscriptions
chmod 644 $RPM_BUILD_ROOT%{_sharedstatedir}/news/subscriptions

install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sharedstatedir}/news/distributions

mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 0644 %{SOURCE20} $RPM_BUILD_ROOT%{_unitdir}

install -p -m 0644 %{SOURCE21} $RPM_BUILD_ROOT%{_unitdir}
install -p -m 0644 %{SOURCE22} $RPM_BUILD_ROOT%{_unitdir}

install -p -m 0644 %{SOURCE23} $RPM_BUILD_ROOT%{_unitdir}
install -p -m 0644 %{SOURCE24} $RPM_BUILD_ROOT%{_unitdir}

install -p -m 0644 %{SOURCE25} $RPM_BUILD_ROOT%{_unitdir}
install -p -m 0644 %{SOURCE26} $RPM_BUILD_ROOT%{_unitdir}

cp -p %{SOURCE10} FAQ.html

touch $RPM_BUILD_ROOT%{_sharedstatedir}/news/history
#LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/bin/makedbz -i \
# -f $RPM_BUILD_ROOT/var/lib/news/history
#chmod 644 $RPM_BUILD_ROOT/var/lib/news/*

cat > $RPM_BUILD_ROOT%{_sysconfdir}/news/.profile <<EOF
PATH=/bin:%{_bindir}:%{_libexecdir}/news
export PATH
EOF

#Fix perms in sample directory to avoid bogus dependencies
find samples -type f | xargs chmod a-x

# we get this from cleanfeed
rm -f $RPM_BUILD_ROOT%{_libexecdir}/news/filter/filter_innd.pl

mkdir -p $RPM_BUILD_ROOT%{_bindir}
ln -sf %{_libexecdir}/news/inews $RPM_BUILD_ROOT%{_bindir}/inews
ln -sf %{_libexecdir}/news/rnews $RPM_BUILD_ROOT%{_bindir}/rnews
# fix debuginfo extraction, permissions are set in files section, anyway
chmod u+w $RPM_BUILD_ROOT%{_libdir}/libinn{,hist,storage}.so.*
pushd $RPM_BUILD_ROOT%{_libexecdir}/news
chmod u+w \
          actsync \
          archive \
          auth/passwd/{auth_krb5,ckpasswd,radius} \
          auth/resolv/{domain,ident} \
          batcher \
          {buff,over}chan \
          buffindexed_d \
          convdate \
          ctlinnd \
          cvtbatch \
          expire{,over} \
          fastrm \
          gencancel \
          getlist \
          {grep,make,prune}history \
          imapfeed \
          inews \
          inn{bind,confval,d,df,feed,xbatch,xmit} \
          makedbz \
          ninpaths \
          nnrpd \
          nntpget \
          ovdb_{init,monitor,server,stat} \
          ovsqlite-server \
          ovsqlite-util \
          rnews{,.libexec/{de,en}code} \
          shlock \
          shrinkfile \
          sm \
          tdx-util \
          tinyleaf \

popd

# Remove unwanted files
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a

# Documentation is installed via rpm %%doc directive
rm -rf $RPM_BUILD_ROOT/usr/doc/

# Use tmpfiles.d to create /run/news
install -d $RPM_BUILD_ROOT%{_tmpfilesdir}
cat <<EOF >$RPM_BUILD_ROOT%{_tmpfilesdir}/inn.conf
D /run/news 0755 news news -
EOF
install -d -m 0755 $RPM_BUILD_ROOT/run/news

install -d %{buildroot}%{_presetdir}
cat <<EOF >%{buildroot}%{_presetdir}/80-inn.preset
enable innd-expire.timer
enable innd-nntpsend.timer
enable innd-rnews.timer
EOF

install -dm755 %{buildroot}%{_sysconfdir}/rsyslog.d
install -pm644 %{S:30} %{buildroot}%{_sysconfdir}/rsyslog.d/inn.conf

install -m0644 -D inn.sysusers.conf %{buildroot}%{_sysusersdir}/inn.conf

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make -C tests test

%global inn_units_with_restart innd.service innd-expire.timer innd-nntpsend.timer innd-rnews.timer
%global inn_units innd-expire.service innd-nntpsend.service innd-rnews.service


%post
su -m news -c '/usr/libexec/news/makedbz -i -o'

umask 002
touch /var/log/news/news.notice /var/log/news/news.crit /var/log/news/news.err
chown -R news:news /var/log/news*

%systemd_post %{inn_units_with_restart} %{inn_units}

%ldconfig_scriptlets libs

%preun
%systemd_preun %{inn_units_with_restart} %{inn_units}

if [ $1 = 0 ]; then
    if [ -f /var/lib/news/history.dir ]; then
       rm -f /var/lib/news/history.*
    fi
fi

%postun
%systemd_postun_with_restart %{inn_units}
%systemd_postun %{inn_units}

%files
%license doc/GPL
%license LICENSE
%doc NEWS README* HACKING CONTRIBUTORS INSTALL FAQ.html
%doc doc/config-design doc/history-innfeed doc/sample-control
%doc doc/config-semantics doc/external-auth TODO doc/hook-python doc/config-syntax
%doc doc/hook-perl doc/history
%doc samples
%exclude %{_pkgdocdir}/samples/*.in*
%{_unitdir}/innd.service
%{_unitdir}/innd-expire.service
%{_unitdir}/innd-expire.timer
%{_unitdir}/innd-nntpsend.service
%{_unitdir}/innd-nntpsend.timer
%{_unitdir}/innd-rnews.service
%{_unitdir}/innd-rnews.timer
%{_presetdir}/80-inn.preset
%dir %{_sysconfdir}/rsyslog.d
%{_sysconfdir}/rsyslog.d/inn.conf
%{_mandir}/man1/c*.1.gz
%{_mandir}/man1/f*.1.gz
%{_mandir}/man1/g*.1.gz
%{_mandir}/man1/inn*.1.gz
%{_mandir}/man1/n*.1.gz
%{_mandir}/man1/p*.1.gz
%{_mandir}/man1/r*.1.gz
%{_mandir}/man1/s*.1.gz
%{_mandir}/man3/INN::Config.3pm*
%{_mandir}/man3/INN::Utils::Shlock.3pm*
%{_mandir}/man3/libinn_uwildmat.3*
%{_mandir}/man[58]/*
%defattr(-,news,news,-)
# tmpfile.d files
%{_tmpfilesdir}/inn.conf
%dir /run/news
# /etc/news config files
%dir %{_sysconfdir}/news
%config(noreplace) %{_sysconfdir}/news/send-uucp.cf
%config(noreplace) %{_sysconfdir}/news/actsync.cfg
%config(noreplace) %{_sysconfdir}/news/motd.innd.sample
%config(noreplace) %{_sysconfdir}/news/motd.nnrpd.sample
%config(noreplace) %{_sysconfdir}/news/expire.ctl
%config(noreplace) %{_sysconfdir}/news/actsync.ign
%config(noreplace) %{_sysconfdir}/news/innreport.conf
%config(noreplace) %{_sysconfdir}/news/distrib.pats
%config(noreplace) %{_sysconfdir}/news/buffindexed.conf
%config(noreplace) %{_sysconfdir}/news/innwatch.ctl
%config(noreplace) %{_sysconfdir}/news/nntpsend.ctl
%config(noreplace) %{_sysconfdir}/news/innfeed.conf
%config(noreplace) %{_sysconfdir}/news/nnrpd.track
%config(noreplace) %{_sysconfdir}/news/control.ctl.local
%config(noreplace) %{_sysconfdir}/news/storage.conf
%config(noreplace) %{_sysconfdir}/news/moderators
%config(noreplace) %{_sysconfdir}/news/news2mail.cf
%config(noreplace) %{_sysconfdir}/news/cycbuff.conf
%config(noreplace) %{_sysconfdir}/news/subscriptions
%config(noreplace) %{_sysconfdir}/news/control.ctl
%config(noreplace) %{_sysconfdir}/news/localgroups
%config(noreplace) %{_sysconfdir}/news/.profile
%config(noreplace) %{_sysconfdir}/news/nocem.ctl
%config(noreplace) %{_sysconfdir}/news/incoming.conf
%config(noreplace) %{_sysconfdir}/news/inn-radius.conf
%config(noreplace) %attr(0660,news,news) %{_sysconfdir}/news/inn-secrets.conf
%config(noreplace) %{_sysconfdir}/news/ovdb.conf
%config(noreplace) %{_sysconfdir}/news/ovsqlite.conf
%config(noreplace) %{_sysconfdir}/news/newsfeeds
%config(noreplace) %{_sysconfdir}/news/readers.conf
%config(noreplace) %{_sysconfdir}/news/distributions

%dir %{_sharedstatedir}/news
%config(noreplace) %{_sharedstatedir}/news/active.times
%config(noreplace) %{_sharedstatedir}/news/distributions
%config(noreplace) %{_sharedstatedir}/news/newsgroups
%config(noreplace) %{_sharedstatedir}/news/active
%config(noreplace) %{_sharedstatedir}/news/subscriptions
%config(noreplace) %{_sharedstatedir}/news/history

%config(noreplace) %{_sysconfdir}/news/innshellvars.pl.local
%config(noreplace) %{_sysconfdir}/news/innshellvars.local
%config(noreplace) %{_sysconfdir}/news/innshellvars.tcl.local

%defattr(0755,root,news,0755)
%{_bindir}/rnews
%dir %{_libexecdir}/news
%{_libexecdir}/news/controlbatch
%attr(4510,root,news) %{_libexecdir}/news/innbind
%{_libexecdir}/news/delayer
%{_libexecdir}/news/docheckgroups
%{_libexecdir}/news/imapfeed
%{_libexecdir}/news/actmerge
%{_libexecdir}/news/ovdb_server
%{_libexecdir}/news/ovsqlite-server
%{_libexecdir}/news/ovsqlite-util
%{_libexecdir}/news/gencancel
%{_libexecdir}/news/ninpaths
%{_libexecdir}/news/mod-active
%{_libexecdir}/news/news2mail
%{_libexecdir}/news/innconfval
%{_libexecdir}/news/shlock
%{_libexecdir}/news/nnrpd
%{_libexecdir}/news/controlchan
%{_libexecdir}/news/procbatch
%{_libexecdir}/news/expire
%{_libexecdir}/news/convdate
%{_libexecdir}/news/pullnews
%{_libexecdir}/news/archive
%{_libexecdir}/news/cnfsstat
%{_libexecdir}/news/grephistory
%{_libexecdir}/news/send-ihave
%{_libexecdir}/news/tinyleaf
%{_libexecdir}/news/cvtbatch
%{_libexecdir}/news/expirerm
%{_libexecdir}/news/rc.news
%attr(4550,uucp,news) %{_libexecdir}/news/rnews
%{_libexecdir}/news/innxmit
%{_libexecdir}/news/actsyncd
%{_libexecdir}/news/shrinkfile
%{_libexecdir}/news/makedbz
%{_libexecdir}/news/actsync
%{_libexecdir}/news/pgpverify
%{_libexecdir}/news/inndf
%{_libexecdir}/news/scanlogs
%{_libexecdir}/news/simpleftp
%{_libexecdir}/news/ovdb_init
%{_libexecdir}/news/ctlinnd
%{_libexecdir}/news/innstat
%{_libexecdir}/news/send-uucp
%{_libexecdir}/news/buffchan
%{_libexecdir}/news/perl-nocem
%{_libexecdir}/news/scanspool
%{_libexecdir}/news/expireover
%{_libexecdir}/news/batcher
%{_libexecdir}/news/fastrm
%{_libexecdir}/news/innmail
%{_libexecdir}/news/innxbatch
%{_libexecdir}/news/buffindexed_d
%{_libexecdir}/news/nntpget
%{_libexecdir}/news/cnfsheadconf
%{_libexecdir}/news/ovdb_stat
%{_libexecdir}/news/prunehistory
%{_libexecdir}/news/innreport
%attr(0644,root,news) %{_libexecdir}/news/innreport_inn.pm
%attr(0644,root,news) %{_libexecdir}/news/innreport-display.conf
%{_libexecdir}/news/getlist
%{_libexecdir}/news/innd
%{_libexecdir}/news/innupgrade
%{_libexecdir}/news/news.daily
%{_libexecdir}/news/sm
%{_libexecdir}/news/innwatch
%{_libexecdir}/news/inncheck
%{_libexecdir}/news/writelog
%{_libexecdir}/news/tdx-util
%{_libexecdir}/news/tally.control
%{_libexecdir}/news/overchan
%{_libexecdir}/news/sendinpaths
%{_libexecdir}/news/makehistory
%{_libexecdir}/news/nntpsend
%{_libexecdir}/news/mailpost
%{_libexecdir}/news/innfeed
%{_libexecdir}/news/ovdb_monitor
%{_libexecdir}/news/sendxbatches

%define filterdir %{_libexecdir}/news/filter
%dir %{filterdir}
%{filterdir}/filter_nnrpd.pl
%{filterdir}/nnrpd_access.pl
%{filterdir}/startup_innd.pl
%{filterdir}/nnrpd_auth.py*
%{filterdir}/nnrpd_access.py*
%{filterdir}/nnrpd_auth.pl
%{filterdir}/INN.py*
%{filterdir}/nnrpd.py*
%{filterdir}/filter_innd.py*
%{filterdir}/nnrpd_dynamic.py*

%define authdir %{_libexecdir}/news/auth
%dir %{authdir}

%define passwddir %{authdir}/passwd
%dir %{passwddir}
%{passwddir}/auth_krb5
%{passwddir}/ckpasswd
%{passwddir}/radius

%define resolvdir %{authdir}/resolv
%dir %{resolvdir}
%{resolvdir}/domain
%{resolvdir}/ident

%define controldir %{_libexecdir}/news/control
%dir %{controldir}
%{controldir}/ihave.pl
%{controldir}/sendme.pl
%{controldir}/checkgroups.pl
%{controldir}/newgroup.pl
%{controldir}/rmgroup.pl

%define rnewsdir %{_libexecdir}/news/rnews.libexec
%dir %{rnewsdir}
%{rnewsdir}/encode
%{rnewsdir}/gunbatch
%{rnewsdir}/decode
%{rnewsdir}/bunbatch
%{rnewsdir}/c7unbatch

%{_libexecdir}/news/innshellvars.pl
%{_libexecdir}/news/innshellvars
%{_libexecdir}/news/innshellvars.tcl

%attr(0775,root,news) %dir %{_sharedstatedir}/news/http
%{_sharedstatedir}/news/http/innreport.css

%dir %{perl_vendorlib}/INN
%{perl_vendorlib}/INN/Config.pm
%{perl_vendorlib}/INN/Utils/Shlock.pm
%{perl_vendorlib}/INN/ovsqlite_client.pm

%defattr(-,news,news,-)
%dir /var/spool/news
%dir /var/spool/news/archive
%dir /var/spool/news/articles
%attr(0775,news,news) %dir /var/spool/news/incoming
%attr(0775,news,news) %dir /var/spool/news/incoming/bad
%dir /var/spool/news/innfeed
%dir /var/spool/news/outgoing
%dir /var/spool/news/overview
%dir /var/log/news/OLD
%dir %{_sharedstatedir}/news/tmp

%files libs
%{_libdir}/libinn.so.9{,.*}
%{_libdir}/libinnhist.so.3{,.*}
%{_libdir}/libinnstorage.so.3{,.*}

%files devel
%{_includedir}/inn
%{_libdir}/libinn.so
%{_libdir}/libinnhist.so
%{_libdir}/libinnstorage.so
%{_mandir}/man3/*
%exclude %{_mandir}/man3/INN::Config.3pm*
%exclude %{_mandir}/man3/INN::Utils::Shlock.3pm*
%exclude %{_mandir}/man3/libinn_uwildmat.3*

%files -n inews
%config(noreplace) %attr(-,news,news) %{_sysconfdir}/news/inn.conf
%config(noreplace) %attr(-,news,news) %{_sysconfdir}/news/passwd.nntp
%{_bindir}/inews
%attr(0755,root,root) %{_libexecdir}/news/inews
%{_mandir}/man1/inews*
%{_sysusersdir}/inn.conf

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul 07 2025 Jitka Plesnikova <jplesnik@redhat.com> - 2.7.3-3
- Perl 5.42 rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 2.7.3-2
- Rebuilt for Python 3.14

* Tue May 27 2025 Dominik Mierzejewski <dominik@greysector.net> - 2.7.3-1
- update to 2.7.3 (resolves rhbz#2368556)
- enable canlock support
- add missing test dependency

* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.7.2-4
- Add sysusers.d config file to allow rpm to create users/groups automatically

* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 2.7.2-3
- Add explicit BR: libxcrypt-devel

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 13 2024 Dominik Mierzejewski <dominik@greysector.net> - 2.7.2-1
- update to 2.7.2 (#2293907)

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.7.1-10
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Jitka Plesnikova <jplesnik@redhat.com> - 2.7.1-8
- Perl 5.40 rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.7.1-7
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 2.7.1-3
- Perl 5.38 rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.7.1-2
- Rebuilt for Python 3.12

* Tue May 16 2023 Dominik Mierzejewski <dominik@greysector.net> - 2.7.1-1
- update to 2.7.1 (#2203869)
- re-enable parallel build

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Dominik Mierzejewski <dominik@greysector.net> - 2.7.0-3
- add missing dependency on perl-subs (for innupgrade and its tests)
  fixes rhbz#2155167

* Thu Nov 17 2022 Dominik Mierzejewski <dominik@greysector.net> - 2.7.0-2
- drop duplicate inn-secrets.conf from inews package

* Mon Nov 07 2022 Dominik Mierzejewski <dominik@greysector.net> - 2.7.0-1
- update to 2.7.0 (#2107592)
- update files list (API and ABI break)
- enable SQLite support
- disable parallel build again

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Dominik Mierzejewski <dominik@greysector.net> - 2.6.5-1
- update to 2.6.5 (#2058851)
- drop obsolete patch
- point to /run/news in tmpfiles.d drop-in
- re-enable parallel build

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.6.4-13
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.4-12
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 21 2021 Dominik Mierzejewski <rpm@greysector.net> - 2.6.4-10
- fix building using parallel make (#1558586)

* Wed Sep 29 2021 Dominik Mierzejewski <rpm@greysector.net> - 2.6.4-9
- drop uucp from BuildRequires (not required for build) and make it a weak dep

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.6.4-8
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.6.4-6
- Rebuilt for Python 3.10

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.4-5
- Perl 5.34 rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.6.4-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Thu Feb 18 2021 Dominik Mierzejewski <rpm@greysector.net> - 2.6.4-3
- use a config drop-in instead of modifying rsyslog.conf in a trigger scriptlet
- switch to HTTPS URLs for sources

* Tue Feb 16 2021 Dominik Mierzejewski <rpm@greysector.net> - 2.6.4-2
- backport upstream patch to fix util/inndf test on ppc64le
- drop obsolete patch (-pie is used for all programs by default now)
- move some man pages to the main package
- exclude internal header files and templates
- inews requires passwd.nntp to be present, move it to inews subpackage

* Sun Feb 14 2021 Dominik Mierzejewski <rpm@greysector.net> - 2.6.4-1
- update to 2.6.4
- drop obsolete patch

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Dominik Mierzejewski <rpm@greysector.net> - 2.6.3-10
- add missing build dependencies (enable zlib and gdbm)
- minimize shared library deps as recommended by upstream
- add missing test dependencies and run testsuite
- follow current guidelines for systemd units packaging
- drop Patch6 (upstream says it's formally incorrect)
- drop Patch7 (doesn't seem to fix any warnings)
- merge Patch14 and Patch17 into Patch1

* Wed Sep 09 2020 Petr Viktorin <pviktori@redhat.com> - 2.6.3-9
- Switch BuildRequires to python3
- enable embedded python support (Dominik Mierzejewski)
- drop unused variable causing GCC10 compilation error (Dominik Mierzejewski)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.3-7
- Perl 5.32 rebuild

* Sun Jun 21 2020 Dominik Mierzejewski <rpm@greysector.net> - 2.6.3-6
- switch from db4 to libdb (#1838599)

* Fri Jan 31 2020 Dominik Mierzejewski <rpm@greysector.net> - 2.6.3-5
- add missing dependency on wget
- use HTTPS in URL

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.3-2
- Perl 5.30 rebuild

* Fri Feb 22 2019 Dominik Mierzejewski <rpm@greysector.net> - 2.6.3-1
- update to 2.6.3 release (#1674441)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.6.2-4
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.2-2
- Perl 5.28 rebuild

* Sat Jun 23 2018 Dominik Mierzejewski <rpm@greysector.net> - 2.6.2-1
- update to 2.6.2 release (#1557980)
- check GPG signature of the tarball

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.6.1-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.6.1-9
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.1-6
- Perl 5.26 rebuild

* Fri Feb 17 2017 Than Ngo <than@redhat.com> - 2.6.1-5
- disable parallel build temporary as it breaks by mass rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Dominik Mierzejewski <rpm@greysector.net> - 2.6.1-3
- add missing BR: for perl modules GD and MIME::Parser
- perl(GD) is optional at runtime
- drop obsolete configure options
- drop ancient and obsolete compilation flags
- re-enable parallel make builds
- fix debuginfo extraction
- fix warning: %%defattr doesn't define directory mode...

* Thu Jan 26 2017 Dominik Mierzejewski <rpm@greysector.net> - 2.6.1-2
- make sure uucp user exists when installing inn (rnews)
- make sure news user exists when installing inews

* Wed Jan 25 2017 Dominik Mierzejewski <rpm@greysector.net> - 2.6.1-1
- update to 2.6.1 release (#1403810)
- drop obsolete patches
- bring back the patch to build suid binaries as PIE

* Fri Nov 25 2016 Petr Pisar <ppisar@redhat.com> - 2.6.0-5
- Support OpenSSL 1.1.0 (bug #1387660)

* Sat Jul 02 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.6.0-4
- drop executable bits from systemd service and timer units (#1301180)

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.0-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Dominik Mierzejewski <rpm@greysector.net> - 2.6.0-1
- update to 2.6.0 release
- update homepage URL
- drop obsolete patches
- fix typos in systemd service descriptions (#1278241)
- point INN FAQ "source" to its upstream URL
- enable SSL (#1282236) and SASL support
- fix innxmit processes getting killed prematurely (#1274857)
- depend on systemd instead of -units (#850159)
- fix /usr/libexec/news/auth files listed twice

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-0.rc1.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.6.0-0.rc1.1.1
- Perl 5.22 rebuild

* Thu May 07 2015 Dan Horák <dan[at]danny.cz> - 2.6.0-0.rc1.1
- workaround ssize_t detection

* Tue Apr 21 2015 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.0-0.rc1
- New upstream release

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.5.4-3
- Perl 5.20 rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 15 2014 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.4-1
- New upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jan  4 2014 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.3-18
- User systemd scriptlets rpm macros for timers

* Thu Jan  2 2014 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.3-17
- Add a delay for the systemd timers on boot
- Avoid warning when stopping timers during update
- Stricter Req. in inn-devel subpackage

* Sun Dec 29 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.3-16
- Additional rework on the systemd timer files

* Sun Dec 29 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.3-15
- Rework ystemd timer handling (#1046960)

* Sat Dec 14 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.3-14
- Fix typo in innd-nntpsend.service (#1043126)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.5.3-12
- Perl 5.18 rebuild

* Tue May 28 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.3-11
- Fix typos in the posix patch (hint from upstream)

* Tue May 21 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.3-10
- Building package with PIE flags (#965502)
- Fix issue with recent pod2man releases

* Sun Feb 24 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.3-9
- Fix name conflict with libradius

* Fri Jan 25 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.3-8
- Timer service units have to been enabled also

* Wed Jan 23 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.3-7
- Using of %%{_tmpfilesdir} instaead of %%{_sysconfdir}/tmpfiles.d/
- Disable SMP build due an SMP-related issue
- Rework for the systemd timers. They will been enabled and started after install

* Tue Jan 22 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.3-6
- Fix some issues with the systemd timer units

* Wed Jan 16 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.3-5
- Migrating from cron to systemd timer
- Change %%doc %%dir into %%doc

* Fri Oct  5 2012 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.3-4
- Introduction of systemd rpm macros

* Tue Sep 11 2012 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.3-3
- New release is SMP compilant

* Tue Sep 11 2012 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.3-2
- Remove inn-2.5.2-hdr.patch

* Thu Sep 06 2012 Ondrej Vasik <ovasik@redhat.com> - 2.5.3-1
- new upstream release 2.5.3

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 2.5.2-22
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 15 2011 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.2-20
- Redirect both STDOUT and STDERR on cron.hourly

* Sun Nov 13 2011 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.2-19
- Avoid useless messages in cron.hourly (#753581)

* Wed Oct  5 2011 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.2-18
- Unghosting /var/run/news

* Wed Oct  5 2011 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.2-17
- Use tmpfiles.d to create /var/run/news
- Clean up SPEC file 

* Mon Sep 19 2011 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.2-16
- Set PATH for user news to more resticted values

* Mon Sep 19 2011 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.2-15
- Move wrong place assigments in innd.service file

* Thu Sep  1 2011 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.2-14
- Rewrite systemd.service file
- Allow login to news user account

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 2.5.2-13
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 2.5.2-12
- Perl mass rebuild

* Wed Jul 13 2011 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.2-11
- Add Condition to /etc/news/inn.conf in innd.service

* Tue Jul  5 2011 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.2-10
- Fix typo in start-inn

* Sun Jun 26 2011 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.2-9
- Initial migration to native systemd support

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.5.2-8
- Perl mass rebuild

* Tue May 31 2011 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.2-7
- Change /var/run/news to /run/news

* Mon May 30 2011 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.2-6
- Create /var/run/news in innd.init (#708627)
- This release is not SMP compilant

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.2-4
- Rebuild for python-2.7 (#623322)
- Fix SMP issue in frontends

* Wed Jul 14 2010 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.2-3
- /var/run/news ghosted tmpfs

* Tue Jul  6 2010 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.2-2
- Try to fix a smp issue on innfeed/Makefile

* Mon Jun 28 2010 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.2-1
- New upstream release

* Wed Jun 2 2010 Nikola Pajkovsky <npajkovs@redhat.com> - 2.5.1-5
- Resolves: #597799 - Two typos in /etc/init.d/inn, three typos in /etc/cron.*/inn* in F13
- Resolves: #596580 - Migration from /usr/lib/news/bin to /usr/libexec/news is not complete
- Resolves: #604473 - wrong permissions on /usr/share/doc/inn-2.5.1(Jochen@herr-schmitt.de)
- add patch inn-2.5.1-config-path.patch
- add BuildRequires: flex (Jochen@herr-schmitt.de)

* Tue Jun 01 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.5.1-4
- Mass rebuild with perl-5.12.0

* Wed Dec 16 2009 Nikola Pajkovsky <npajkovs@redhta.com> - 2.5.1-3
- rebuild 
- chage licence and remove on rm -f
- drop patches inn-2.4.1.perl.patch and inn-2.4.5-dynlib.patch

* Fri Dec 11 2009 Nikola Pajkovsky <npajkovs@redhat.com> - 2.5.1-2
- #225901 - Merge Review: inn

* Tue Oct 13 2009 Jochen Schmitt <Jochen herr-schmitt de> - 2.5.1-1
- New upstream release

* Mon Sep 14 2009 Nikola Pajkovsky <npajkovs@redhat.com> - 2.5.0-5
- resolved: 511772 - inn/storage.h not self-contained, missing inn/options.h

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Nikola Pajkovsky <npajkovs@redhat.com> 2.5.0-3
- ugly sed script for file section was deleted and rewrite in classic style
- fix init script(does not start correctly and shutdown when pid does not exist when service run)

* Wed Jun 24 2009 Ondrej Vasik <ovasik@redhat.com> - 2.5.0-2
- add support for load average to makehistory(#276061)
- update faq, ship it in %%doc
- fix typo in filelist

* Tue Jun 09 2009 Ondrej Vasik <ovasik@redhat.com> - 2.5.0-1
- new upstream release 2.5.0
- remove applied and adjust modified patches

* Tue May 19 2009 Ondrej Vasik <ovasik@redhat.com> - 2.4.6-2
- reflect change in sasl_encode64 abi(null terminator) - #501452

* Wed Mar 11 2009 Ondrej Vasik <ovasik@redhat.com> - 2.4.6-1
- new bugfix upstream release 2.4.6
- no strict aliasing, remove pyo/.pyc filters files from list

* Wed Feb 25 2009 Ondrej Vasik <ovasik@redhat.com> - 2.4.5-10
- mark /usr/lib/news/lib/innshellvars* as noreplace,
  versioned provide for perl(::/usr/lib/innshellvars.pl)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Ondrej Vasik <ovasik@redhat.com> - 2.4.5-8
- create user/group news with reserved uidgid numbers

* Wed Jan 13 2009 Ondrej Vasik <ovasik@redhat.com> - 2.4.5-7
- fix upstream url

* Mon Dec  1 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.4.5-6
- Rebuild for Python 2.6

* Mon Dec 01 2008 Ondrej Vasik <ovasik@redhat.com> - 2.4.5-5
- do own /usr/include/inn in devel package (#473922)

* Tue Nov 25 2008 Ondrej Vasik <ovasik@redhat.com> - 2.4.5-4
- package summary tuning

* Fri Aug 29 2008 Ondrej Vasik <ovasik@redhat.com> - 2.4.5-3
- patch fuzz clean up

* Fri Jul  7 2008 Ondrej Vasik <ovasik@redhat.com> - 2.4.5-2
- do not use static libraries(changes by Jochen Schmitt,#453993)
- own all dirs spawned by inn package(#448088)

* Thu Jul  3 2008 Ondrej Vasik <ovasik@redhat.com> - 2.4.5-1
- new upstream release 2.4.5

* Tue Jun 17 2008 Ondrej Vasik <ovasik@redhat.com> - 2.4.4-3
- Add news user. fixes bug #437462
* Mon May 19 2008 Ondrej Vasik <ovasik@redhat.com> - 2.4.4-2
- add sparc arches to the list for -fPIC(Dennis Gilmore)

* Thu May 15 2008 Ondrej Vasik <ovasik@redhat.com> - 2.4.4-1
- new upstream release 2.4.4

* Thu Apr 24 2008 Ondrej Vasik <ovasik@redhat.com> - 2.4.3-14
- make /var/spool/news/incoming writable for news group
  (#426760)
- changes because of /sbin/nologin shell for news user

* Wed Apr  9 2008 Ondrej Vasik <ovasik@redhat.com> - 2.4.3-13
- few documentation changes because of /sbin/nologin shell 
  for news user (su - news -c <commmand> will not work in 
  that case ) #233738

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.4.3-12
- BuildRequires: perl(ExtUtils::Embed)

* Tue Mar 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.4.3-11
- add Requires for versioned perl (libperl.so)

* Mon Feb 11 2008 Ondrej Vasik <ovasik@redhat.com> 2.4.3-10
- again added trigger for sysklogd
- rebuild for gcc43

* Wed Jan 16 2008 Ondrej Vasik <ovasik@redhat.com> 2.4.3-9
- do not show annoying fatal log message when nonfatal error 
  eaddrinuse occured in rcreader
- use /etc/rsyslog.conf instead of /etc/syslog.conf

* Mon Jan 07 2008 Ondrej Vasik <ovasik@redhat.com> 2.4.3-8
- initscript changes - review changes caused errors while
  in stop() phase - not known variable NEWSBIN(#401241)
- added url, fixed License tag

* Tue Oct 02 2007 Ondrej Dvoracek <odvorace@redhat.com> 2.4.3-7
- initscript review (#246951)
- added buildrequires for perl-devel and python

* Tue Aug 29 2006 Martin Stransky <stransky@redhat.com> 2.4.3-6
- added dist tag
- added patch from #204371 - innd.init script should use 
  ctlinnd to stop the server

* Mon Jul 17 2006 Jesse Keating <jkeating@redhat.com> - 2.4.3-5
- rebuild

* Wed Jun 21 2006 Martin Stransky <stransky@redhat.com> 2.4.3-4
- enabled ipv6 support

* Wed Jun 07 2006 Karsten Hopp <karsten@redhat.de> 2.4.3-3
- add some buildrequirements (krb5-devel pam-devel e2fsprogs-devel)

* Sun May 28 2006 Martin Stransky <stransky@redhat.com> 2.4.3-2
- file conflicts for inn (#192689)
- added byacc to dependencies (#193402)

* Mon Mar 27 2006 Martin Stransky <stransky@redhat.com> 2.4.3-1
- new upstream

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.4.2-4.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.4.2-4.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Aug 02 2005 Karsten Hopp <karsten@redhat.de> 2.4.2-4
- rebuild with current rpm
- include .pyc and pyo files created by /usr/lib/rpm/brp-python-bytecompile

* Thu Apr  7 2005 Martin Stransky <stransky@redhat.com> 2.4.2-3
- add support for large files

* Mon Mar  7 2005 Martin Stransky <stransky@redhat.com>
- rebuilt

* Tue Jan 11 2005 Martin Stransky <stransky@redhat.com> 2.4.2-1
- fix file conflict between inews and inn packages (#51607)
- update to 2.4.2
- thanks to Jochen Schmitt <Jochen@herr-schmitt.de>

* Thu Dec 23 2004 Martin Stransky <stransky@redhat.com> 2.4.1-2
- fix array overflow / uninitialized pointer (#143592)

* Wed Dec 15 2004 Martin Stransky <stransky@redhat.com> 2.4.1-1
- diff patch (fix obsolete version of diff parameter) #137342
- posix/warnings patch #110825

* Mon Dec 13 2004 Martin Stransky <stransky@redhat.com> 2.4.1-1
- update to INN 2.4.1
- Thanks to Jochen Schmitt <Jochen@herr-schmitt.de>

* Tue Oct  5 2004 Thomas Woerner <twoerner@redhat.com> 2.3.5-11.1
- using runuser instead of su in cronjobs

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 17 2004 Thomas Woerner <twoerner@redhat.com> 2.3.5-10
- compiling server and suid programs PIE

* Tue Apr  6 2004 Thomas Woerner <twoerner@redhat.com> 2.3.5-9
- /etc/rc.d/init.d/innd is owned by root now (#119131)

* Mon Feb 23 2004 Tim Waugh <twaugh@redhat.com>
- Use ':' instead of '.' as separator for chown.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jan 29 2004 Thomas Woerner <twoerner@redhat.com> 2.3.5-7
- using db-4.2

* Mon Jul 14 2003 Chip Turner <cturner@redhat.com>
- rebuild for new perl 5.8.1

* Thu Jul 03 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- recompile for other thingy

* Wed Jun 11 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- link against db-4.1  #92420
- use correct optims settings from rpm  #92410
- install with other perms to allow debuginfo stripping #92412

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Apr 30 2003 Ellito Lee <sopwith@redhat.com> 2.3.5-2
- headusage patch for ppc64 etc.

* Sun Mar 30 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- 2.3.5 update

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jan 17 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to current bug-fix release

* Fri Jan 03 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- do not require cleanfeed  #80124

* Tue Dec 17 2002 Phil Knirsch <pknirsch@redhat.com> 2.3.3-9
- Fixed changelog entries containing percent sections.

* Tue Dec 03 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- do not link against -lelf

* Thu Nov  7 2002 Tim Powers <timp@redhat.com>
- rebuilt to fix unsatisfied dependencies
- pass _target_platform when configuring

* Tue Jul 23 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- fix cron scripts to use correct paths #69189
- add compat symlinks for rnews/inews into /usr/bin

* Thu Jul 18 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- make check if networking is up more robust in initscript
- move most apps into /usr/lib/news/bin for less namespace pollution

* Tue Jun 18 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- add some cvs patches
- crude hack to change LOCK_READ and LOCK_WRITE within INN source code

* Mon May 27 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to inn-2.3.3
- use db4

* Mon Apr 15 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- put /etc/news/inn.conf into the inews subpackage to make a smaller
  client side possible and require inews from the main inn rpm

* Mon Apr 08 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- startup and cron scripts unset LANG and LC_COLLATE to make
  inn more robust   (#60770)
- really link against db3
- inews requires inn #59852

* Thu Feb 28 2002 Elliot Lee <sopwith@redhat.com> 2.3.2-10
- Change db4-devel requirement to db3-devel.
- Use _smp_mflags

* Thu Jan 31 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- fix #59123

* Wed Jan 30 2002 Jeff Johnson <jbj@redhat.com>
- white out bogus perl requirement for now.
- don't include <db1/ndbm.h> to avoid linking with -ldb1.

* Sat Jan 26 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- change to db4

* Sun Jan 20 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- allow rebuilding by not using newer autoconf, adjust inn patches

* Tue Jul 24 2001 Tim Powers <timp@redhat.com>
- make inews owned by root, not the build system

* Tue Jul 24 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- fix badd attr() macro

* Sat Jul 21 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add build req

* Fri Jul 06 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- change perms on inews

* Tue Jun 19 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 2.3.2

* Wed Feb 14 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add startup script patch by kevin@labsysgrp.com #27421
- inews subpackage does not depend on inn anymore #24439
- fix reload and make some cleanups to the startup script #18076

* Wed Feb 07 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add a "exit 0" to the postun script

* Wed Jan 24 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 2.3.1
- do not use --enable-tagged-hash
- move tmp dir to /var/lib/news/tmp
- add more docu
- do not call "strip" directly
- remove some of the default files as the ones in INN are ok
- do not req /etc/init.d
- do not attempt an automatic update from previous versions as
  we have to deal with different storage methods
- prepare startup script for translations
- add minimal check into startup for a history file

* Mon Jan 22 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- innreport had wrong perms
- files for the cron-jobs must be owned by root:root

* Tue Aug 29 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- remove cleanfeed sources

* Mon Jul 24 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- fix some perms

* Mon Jul 24 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 2.2.3
- fixed many perms
- cleaned up complete build process

* Sat Jul 15 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jul 10 2000 Bill Nottingham <notting@redhat.com>
- add fix for the verifycancels problem fron Russ Allbery
- turn them off anyways
- fix perms on inews

* Sat Jul  8 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- prereq init.d

* Tue Jun 27 2000 Than Ngo <than@redhat.de>
- /etc/rc.d/init.d -> /etc/init.d
- fix initscript

* Sun Jun 25 2000 Matt Wilson <msw@redhat.com>
- defattr root

* Wed Jun 21 2000 Preston Brown <pbrown@redhat.com>
- fix up some issues with our new gcc compiler (patch 6)
- don't do chown in the install script so we can build as nonroot

* Mon Jun 19 2000 Preston Brown <pbrown@redhat.com>
- FHS mandir

* Tue May 23 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- add inn-2.2.2-rnews.patch which is also accepted in current cvs

* Mon May 22 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- fix stupid bug in rnews cronjob
- enable controlchan in default newsfeeds config
- run "rnews -U" hourly instead of daily

* Fri May 19 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- add bug-fix to batcher from cvs version
- "su news" before starting rnews from cron

* Mon Apr  3 2000 Bill Notttingham <notting@redhat.com>
- arrgh, there is no /usr/lib/news anymore. (#10536)
- pppatch ppport for ppproper ppperl

* Thu Mar 02 2000 Cristian Gafton <gafton@redhat.com>
- remove useless filter_innd.pl so that we will get the cleanfeed one
  instead

* Mon Feb  7 2000 Bill Nottingham <notting@redhat.com>
- handle compressed manpages
- other minor fixes

* Tue Dec 14 1999 Bill Nottingham <notting@redhat.com>
- update to 2.2.2

* Sun Aug 29 1999 Cristian Gafton <gafton@redhat.com>
- version 2.2.1 to fix security problems in previous inn versions
- add the faq back to the source rpm

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging

* Tue Jun 22 1999 Jeff Johnson <jbj@redhat.com>
- fix syntax error in reload (#3636).

* Fri Jun 18 1999 Bill Nottingham <notting@redhat.com>
- don't run by default

* Sun Jun 13 1999 Jeff Johnson <jbj@redhat.com>
- mark /var/lib/news/* as config(noreplace) (#3425)

* Thu Jun 10 1999 Dale Lovelace <dale@redhat.com>
- change su news to su - news (#3331)

* Wed Jun  2 1999 Jeff Johsnon <jbj@redhat.com>
- complete trn->inews->inn dependency (#2646)
- use f_bsize rather than f_frsize when computing blocks avail (#3154).
- increase client timeout to 30 mins (=1800) (#2833).
- add missing includes to inn-devel (#2904).

* Mon May 31 1999 Jeff Johnson <jbj@redhat.com>
- fix owner and permissions on /var/lib/news/.news.daily (#2354).

* Tue Mar 30 1999 Preston Brown <pbrown@redhat.com>
- fixed paths in cron jobs, check to see that innd is enabled

* Fri Mar 26 1999 Preston Brown <pbrown@redhat.com>
- path to makehistory corrected.

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- fixed permissions on rnews for uucp

* Fri Mar 19 1999 Preston Brown <pbrown@redhat.com>
- make sure init scripts get packaged up, fix other minor bugs
- major fixups to innd.conf for denial of service attacks, sanity, etc.
- make sure history gets rebuilt in an upgrade (added to post section)
- many thanks go out to mmchen@minn.net for these suggestions.

* Fri Feb 19 1999 Cristian Gafton <gafton@redhat.com>
- prereq all the stuff we need in the postinstall scripts

* Sat Feb  6 1999 Bill Nottingham <notting@redhat.com>
- strip -x bits from docs/samples (bogus dependencies)

* Thu Sep 03 1998 Cristian Gafton <gafton@redhat.com>
- updated to version 2.1

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- innd.init chkconfig entry was incorrect (problem #855)

* Tue Jun 30 1998 Jeff Johnson <jbj@redhat.com>
- susbsys name must be identical to script name (problem #700)

* Mon Jun 29 1998 Bryan C. Andregg <bandregg@redhat.com>
- fixed startinnfeed paths

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- enhanced initscript

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- fixed innfeed patched to be perl-version independent

* Wed Apr 15 1998 Bryan C. Andregg <bandregg@redhat.com>
- fixed sfnet.* entries in control.ctl

* Mon Apr 13 1998 Bryan C. Andregg <bandregg@redhat.com>
- moved cleanfeed to its own package

* Thu Apr 09 1998 Bryan C. Andregg <bandregg@redhat.com>
- added insync patches
- added cleanfeed
- added innfeed

* Thu Apr 09 1998 Cristian Gafton <gafton@redhat.com>
- abuse buildroot to simplify the file list
- built against Manhattan

* Tue Mar 24 1998 Bryan C. Andregg <bandregg@redhat.com>
- updated to inn 1.7.2
- Added REMEMBER_TRASH and Poison patch

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- updated to inn 1.7
- added chkconfig support to the initscripts
- orginally released as release 2, leving release 1 if a 4.2.x upgrade
  is ever necessary 
- don't start it in any runlevel (by default)
- added inndcomm.h

* Thu Oct 09 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Tue Aug 05 1997 Elliot Lee <sopwith@redhat.com>
- Applied the 1.5.1sec and 1.5.1sec2 patches
- Applied 3 more unoff patches.
- Removed insanity in /etc/cron.hourly/inn-cron-nntpsend, it now
  just runs nntpsend as news.

* Wed Apr 02 1997 Erik Troan <ewt@redhat.com>
- Patch from CERT for sh exploit.
- Changed /usr/ucb/compress reference to /usr/bin/compress

* Mon Mar 17 1997 Erik Troan <ewt@redhat.com>
- Removed inews.1 from main inn package (it's still in the inews packaeg)
- Fixed references to /usr/spoo in sendbatch
- added "-s -" to crosspost line in newsfeeds
- /var/lib/news/active.time is now created as news.news
- /etc/news/nnrp.access and /etc/news/nntpsend.ctl are mode 0440 
- included a better rc script which does a better job of shutting down news
- updated /etc/rc.d/rc.news output look like the rest of our initscripts
- hacked sendbatch df stuff to work on machines w/o a separate /var/spool/news

* Tue Mar 11 1997 Erik Troan <ewt@redhat.com>
- added chmod to make sure rnews is 755
- /etc/news/nnrp.access and /etc/news/nntpsend.ctl are news.news not root.news
  or root.root
- install an empty /var/lib/news/.news.daily as a config file
- added dbz/dbz.h as /usr/include/dbz.h
- added /usr/bin/inews link to /usr/lib/news/inews
- changed INEWS_PATH to DONT -- I'm not sure this is right though
- turned off MMAP_SYNC
- added a ton of man pages which were missing from the filelist
- increased CLIENT_TIMEOUT to (30 * 60)
- added a postinstall to create /var/lib/news/active.times if it doesn't
  already exist
- patched rc.news to start inn w/ -L flag
- pulled news.init into a separate source file rather then creating it through
  a patch
- added /etc/rc.d/rc5.d/S95news to the file list
- remove pid files from /var/lock/news/* on shutdown
- use /var/lock/subsys/news rather then /var/lock/subsys/inn or things
  don't shutdown properly

* Mon Mar 10 1997 Christian 'Dr. Disk' Hechelmann <drdisk@ds9.au.s.shuttle.de>
- changed devel package description to include tin.
- the devel package missed libinn.h
- moved libinn.3 man-page to the devel package
- moved changelog up
- in post some echo statements were messed up. if we put the redirection
  staements in a different line than the echo command we really should use
  a backslash to thell the shell :-)
- in install a chmod line referenced the same directory twice.
- changed inn-1.5.1-redhat.patch: The patch for news.daily had a side effect.
  as EXPIREOVERFLAGS was set to '-a', expireover would break if there were
  articles to be removed, as '-a' can't be used if '-z' is specified...
  Now there is a separate 'eval expireover -a' after the first eval. Dirty
  but works.

* Wed Feb 26 1997 Erik Troan <ewt@redhat.com>
- Added a /usr/bin/rnews symlink to /usr/lib/news/rnews as other programs like
  to use it.

* Tue Feb 25 1997 Elliot Lee <sopwith@cuc.edu>
- Fixed rnews path in /etc/cron.daily/inn-cron-rnews
- Added overview! and crosspost lines to /etc/news/newsfeeds
- Fixed nntpsend.ctl path in /usr/lib/news/bin/nntpsend, and set a saner
  nntpsend.ctl config file.
- Added automated inn.conf 'server: ' line creation in post
- Added misc. patches from ftp.isc.org/isc/inn/unoff-patches/1.5
- Removed -lelf from config.data LIBS
- Made RPM_OPT_FLAGS work.
- Bug in rpm meant that putting post after files made it not run. Moved
  post up.
- Added /etc/cron.hourly/inn-cron-nntpsend to send news every hour.
- Fixed most of the misc permissions/ownership stuff that inncheck
  complained about.

* Wed Feb 19 1997 Erik Troan <ewt@redhat.com>
- Incorporated changes from <drdisk@tilx01.ti.fht-esslingen.de> which fixed
  some paths and restored the cron jobs which disappeared in the 1.5.1
  switch. He also made the whole thing use a buildroot and added some files
  which were missing from the file list.
