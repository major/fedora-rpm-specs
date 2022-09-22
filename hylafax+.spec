%global faxspool    /var/spool/hylafax
%global _hardened_build 1
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
%global lockdir    /var/lock/lockdev
%else
%global lockdir    /var/lock
%endif

Summary:   An enterprise-strength fax server
Name:      hylafax+
Version:   7.0.6
Release:   1%{?dist}
License:   libtiff and BSD with advertising
URL:       http://hylafax.sourceforge.net

Source0:   http://downloads.sourceforge.net/hylafax/hylafax-%{version}.tar.gz
Source1:   hylafax+_rh.init
Source2:   hylafax+_daily.cron
Source3:   hylafax+_hourly.cron
Source4:   hylafax+_hfaxd_systemd.service
Source5:   hylafax+_faxq_systemd.service
Source6:   hylafax+_faxgetty_systemd.service
Source7:   hylafax+_sysconfig


Provides:    hylafax = %{version}-%{release}
Requires:    %{name}-client%{?_isa} = %{version}-%{release}

BuildRequires: libjpeg-devel, libtiff-devel, zlib-devel, pam-devel, openldap-devel, uucp, %{_bindir}/tiffcp
BuildRequires: openssl-devel
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: %{_sbindir}/sendmail, ghostscript, mgetty
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
BuildRequires: jbigkit-devel
%endif
%if 0%{?fedora} || 0%{?rhel} >= 7
BuildRequires: lcms2-devel
%else
BuildRequires: lcms-devel
%endif
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
BuildRequires: systemd-units
%endif
%if 0%{?fedora} >= 18 || 0%{?rhel} >= 7
BuildRequires: systemd
%endif
%if 0%{?fedora} >= 27 || 0%{?rhel} > 7
BuildRequires: urw-base35-fonts
Requires: urw-base35-fonts
%else
BuildRequires: ghostscript-fonts
Requires: ghostscript-fonts
%endif
Requires:    ghostscript, uucp, gawk, sharutils, mailx, crontabs, %{_bindir}/tiffcp, mgetty
Requires:    openssl
Conflicts:   mgetty-sendfax
Obsoletes:   hylafax < 5.5.2-1

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%else
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service
Requires(postun): /sbin/service
%endif

%description
HylaFAX(tm) is a enterprise-strength fax server supporting
Class 1 and 2 fax modems on UNIX systems. It provides spooling
services and numerous supporting fax management tools. 
The fax clients may reside on machines different from the server
and client implementations exist for a number of platforms including 
windows.

%package client
Summary:     Client programs for HylaFAX fax servers
Provides:    hylafax-client = %{version}-%{release}
Obsoletes:   hylafax-client < 5.5.2-1
Requires:    %{_sbindir}/sendmail, uucp

%description client
HylaFAX(tm) is a enterprise-strength fax server supporting
Class 1 and 2 fax modems on UNIX systems. This package provides
fax clients which may reside on machines different from the server.

%prep
%setup -q -n hylafax-%{version}

%build
# - Can't use the configure macro because HylaFAX configure script does
#   not understand the config options used by that macro
STRIP=':' \
./configure \
        --with-DIR_BIN=%{_bindir} \
        --with-DIR_SBIN=%{_sbindir} \
        --with-DIR_LIB=%{_libdir} \
        --with-DIR_LIBEXEC=%{_sbindir} \
        --with-DIR_LIBDATA=%{_sysconfdir}/hylafax \
        --with-DIR_LOCKS=%{lockdir} \
        --with-LIBDIR=%{_libdir} \
        --with-TIFFBIN=%{_bindir} \
        --with-DIR_MAN=%{_mandir} \
        --with-PATH_GSRIP=%{_bindir}/gs \
        --with-TIFFINC=-L%{_includedir} \
        --with-LIBTIFF="-ltiff" \
        --with-DIR_SPOOL=%{faxspool} \
        --with-AFM=no \
        --with-AWK=%{_bindir}/gawk \
        --with-PATH_VGETTY=/sbin/vgetty \
        --with-PATH_GETTY=/sbin/mgetty \
        --with-PAGESIZE=A4 \
        --with-PATH_DPSRIP=%{faxspool}/bin/ps2fax \
        --with-PATH_IMPRIP="" \
        --with-SYSVINIT=%{_initrddir}/hylafax+ \
        --with-INTERACTIVE=no

# can't use %{?_smp_mflags} because it breaks libfaxutil dso building
make OPTIMIZER="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

# install: make some dirs...
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/{cron.daily,cron.hourly} 
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/{hylafax,sysconfig}
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
mkdir -p -m 755 $RPM_BUILD_ROOT%{_unitdir}
%else
mkdir -p -m 755 $RPM_BUILD_ROOT%{_initrddir}
%endif
mkdir -p -m 755 $RPM_BUILD_ROOT%{_bindir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sbindir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_libdir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_mandir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{faxspool}/config

# install: binaries and man pages 
# FAXUSER, FAXGROUP, SYSUSER and SYSGROUP are set to the current user to
# avoid warnings about chown/chgrp if the user building the SRPM is not root; 
# they are set to the correct values with the RPM attr macro
make install -e \
        FAXUSER=`id -u` \
        FAXGROUP=`id -g` \
        SYSUSER=`id -u` \
        SYSGROUP=`id -g` \
        BIN=$RPM_BUILD_ROOT%{_bindir} \
        SBIN=$RPM_BUILD_ROOT%{_sbindir} \
        LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
        LIBDATA=$RPM_BUILD_ROOT%{_sysconfdir}/hylafax \
        LIBEXEC=$RPM_BUILD_ROOT%{_sbindir} \
        SPOOL=$RPM_BUILD_ROOT%{faxspool} \
        MAN=$RPM_BUILD_ROOT%{_mandir} \
        INSTALL_ROOT=$RPM_BUILD_ROOT

# install: remaining files
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_unitdir}/hylafax-hfaxd.service
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_unitdir}/hylafax-faxq.service
install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_unitdir}/hylafax-faxgetty@.service
%else
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/hylafax+
%endif
install -p -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/hylafax+
install -p -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/hylafax+
install -p -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly/hylafax+

# Prepare docdir by removing non-doc files
# Remove files that are not needed on Linux
rm -f $RPM_BUILD_ROOT%{_sbindir}/{faxsetup.irix,faxsetup.bsdi}
rm -f $RPM_BUILD_ROOT%{faxspool}/bin/{ps2fax.imp,ps2fax.dps}
rm -f $RPM_BUILD_ROOT%{faxspool}/etc/dpsprinter.ps

rm -f $RPM_BUILD_ROOT%{faxspool}/COPYRIGHT


%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
%post
if [ -e %{faxspool}/etc/setup.cache ] && [ ! -e %{_sysconfdir}/hylafax/setup.cache ]; then
    ln %{faxspool}/etc/setup.cache %{_sysconfdir}/hylafax/setup.cache
fi
if [ -e %{faxspool}/etc/setup.modem ] && [ ! -e %{_sysconfdir}/hylafax/setup.modem ]; then
    ln %{faxspool}/etc/setup.modem %{_sysconfdir}/hylafax/setup.modem
fi
/sbin/ldconfig
if [ 0$1 -eq 1 ]; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%post client -p /sbin/ldconfig

%preun
if [ 0$1 -eq 0 ]; then
    /bin/systemctl --no-reload disable hylafax-hfaxd.service > /dev/null 2>&1 || :
    /bin/systemctl stop hylafax-hfaxd.service > /dev/null 2>&1 || :
    /bin/systemctl --no-reload disable hylafax-faxq.service > /dev/null 2>&1 || :
    /bin/systemctl stop hylafax-faxq.service > /dev/null 2>&1 || :
fi

%postun
/sbin/ldconfig
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ 0$1 -ge 1 ]; then
    /bin/systemctl try-restart hylafax-hfaxd.service >/dev/null 2>&1 || :
    /bin/systemctl try-restart hylafax-faxq.service >/dev/null 2>&1 || :
fi

%postun client -p /sbin/ldconfig

%else
%post
if [ -e %{faxspool}/etc/setup.cache ] && [ ! -e %{_sysconfdir}/hylafax/setup.cache ]; then
    ln %{faxspool}/etc/setup.cache %{_sysconfdir}/hylafax/setup.cache
fi
if [ -e %{faxspool}/etc/setup.modem ] && [ ! -e %{_sysconfdir}/hylafax/setup.modem ]; then
    ln %{faxspool}/etc/setup.modem %{_sysconfdir}/hylafax/setup.modem
fi
/sbin/ldconfig
if [ 0$1 -eq 1 ]; then
    /sbin/chkconfig --add hylafax+
fi

%post client -p /sbin/ldconfig

%preun
if [ 0$1 -eq 0 ]; then
    /sbin/chkconfig --del hylafax+
    /sbin/service hylafax+ stop >/dev/null 2>&1 || :
fi

%postun
/sbin/ldconfig
if [ 0$1 -ge 1 ]; then
    /sbin/service hylafax+ condrestart >/dev/null 2>&1 || :
fi

%postun client -p /sbin/ldconfig
%endif

%files
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
%{_unitdir}/hylafax-faxgetty@.service
%{_unitdir}/hylafax-hfaxd.service
%{_unitdir}/hylafax-faxq.service
%else
%{_initrddir}/hylafax+
%endif
%doc CHANGES CONTRIBUTORS COPYRIGHT README TODO VERSION
%{_libdir}/libfaxserver*
%{_mandir}/man5/doneq.5f.gz
%{_mandir}/man5/hosts.hfaxd.5f.gz
%{_mandir}/man5/hylafax-config.5f.gz
%{_mandir}/man5/hylafax-info.5f.gz
%{_mandir}/man5/hylafax-log.5f.gz
%{_mandir}/man5/hylafax-server.5f.gz
%{_mandir}/man5/hylafax-shutdown.5f.gz
%{_mandir}/man5/pagermap.5f.gz
%{_mandir}/man5/recvq.5f.gz
%{_mandir}/man5/sendq.5f.gz
%{_mandir}/man5/status.5f.gz
%{_mandir}/man5/tsi.5f.gz
%{_mandir}/man5/xferfaxlog.5f.gz
%{_mandir}/man8/choptest.8c.gz
%{_mandir}/man8/cqtest.8c.gz
%{_mandir}/man8/faxabort.8c.gz
%{_mandir}/man8/faxaddmodem.8c.gz
%{_mandir}/man8/faxadduser.8c.gz
%{_mandir}/man8/faxanswer.8c.gz
%{_mandir}/man8/faxconfig.8c.gz
%{_mandir}/man8/faxcron.8c.gz
%{_mandir}/man8/faxdeluser.8c.gz
%{_mandir}/man8/faxgetty.8c.gz
%{_mandir}/man8/faxlock.8c.gz
%{_mandir}/man8/faxmodem.8c.gz
%{_mandir}/man8/faxq.8c.gz
%{_mandir}/man8/faxqclean.8c.gz
%{_mandir}/man8/faxquit.8c.gz
%{_mandir}/man8/faxrcvd.8c.gz
%{_mandir}/man8/faxsend.8c.gz
%{_mandir}/man8/faxstate.8c.gz
%{_mandir}/man8/hfaxd.8c.gz
%{_mandir}/man8/jobcontrol.8c.gz
%{_mandir}/man8/mkcover.8c.gz
%{_mandir}/man8/notify.8c.gz
%{_mandir}/man8/pagesend.8c.gz
%{_mandir}/man8/pollrcvd.8c.gz
%{_mandir}/man8/ps2fax.8c.gz
%{_mandir}/man8/recvstats.8c.gz
%{_mandir}/man8/tagtest.8c.gz
%{_mandir}/man8/tsitest.8c.gz
%{_mandir}/man8/wedged.8c.gz
%{_mandir}/man8/xferfaxstats.8c.gz
%{_mandir}/man8/faxmsg.8c.gz
%{_mandir}/man8/hylafax.8c.gz
%{_mandir}/man8/lockname.8c.gz
%{_mandir}/man8/ondelay.8c.gz
%{_mandir}/man8/probemodem.8c.gz
%dir %{_sysconfdir}/hylafax
%config(noreplace) %{_sysconfdir}/hylafax/hfaxd.conf
%dir %{faxspool}/config
%dir %{faxspool}/dev
%{faxspool}/config/*
%{faxspool}/bin/dict/*
%{faxspool}/bin/auto-rotate.ps
%{faxspool}/etc/cover.templ
%{faxspool}/etc/lutRS18.pcf
%{faxspool}/etc/LiberationSans-25.pcf
%config(noreplace) %{_sysconfdir}/sysconfig/hylafax+
%defattr(755,root,root,-)
%{_sysconfdir}/cron.daily/hylafax+
%{_sysconfdir}/cron.hourly/hylafax+
%{_sbindir}/choptest
%{_sbindir}/cqtest
%{_sbindir}/faxabort
%{_sbindir}/faxaddmodem
%{_sbindir}/faxadduser
%{_sbindir}/faxanswer
%{_sbindir}/faxconfig
%{_sbindir}/faxcron
%{_sbindir}/faxdeluser
%{_sbindir}/faxgetty
%{_sbindir}/faxlock
%{_sbindir}/faxmodem
%{_sbindir}/faxmsg
%{_sbindir}/faxq
%{_sbindir}/faxqclean
%{_sbindir}/faxquit
%{_sbindir}/faxsend
%{_sbindir}/faxstate
%{_sbindir}/hfaxd
%{_sbindir}/hylafax
%{_sbindir}/lockname
%{_sbindir}/ondelay
%{_sbindir}/pagesend
%{_sbindir}/probemodem
%{_sbindir}/recvstats
%{_sbindir}/tagtest
%{_sbindir}/tsitest
%{_sbindir}/xferfaxstats
%{faxspool}/bin/archive
%{faxspool}/bin/dictionary
%{faxspool}/bin/faxrcvd
%{faxspool}/bin/mkcover
%{faxspool}/bin/notify
%{faxspool}/bin/pollrcvd
%{faxspool}/bin/qp-encode.awk
%{faxspool}/bin/rfc2047-encode.awk
%{faxspool}/bin/wedged
%defattr(-,uucp,uucp,-)
%dir %{faxspool}
%dir %{faxspool}/client
%dir %{faxspool}/etc
%dir %{faxspool}/info
%dir %{faxspool}/log
%dir %{faxspool}/recvq
%dir %{faxspool}/status
%config(noreplace) %{faxspool}/etc/xferfaxlog
%attr(700,uucp,uucp) %dir %{faxspool}/docq
%attr(700,uucp,uucp) %dir %{faxspool}/doneq
%attr(700,uucp,uucp) %dir %{faxspool}/archive
%attr(700,uucp,uucp) %dir %{faxspool}/sendq
%attr(700,uucp,uucp) %dir %{faxspool}/tmp
%attr(700,uucp,uucp) %dir %{faxspool}/pollq
%defattr(600,uucp,uucp,-)
%config(noreplace) %{faxspool}/etc/hosts.hfaxd

%files client
%doc CHANGES CONTRIBUTORS COPYRIGHT README TODO VERSION
%{_libdir}/libfaxutil*
%{_mandir}/man1/*
%{_mandir}/man5/dialrules.5f.gz
%{_mandir}/man5/pagesizes.5f.gz
%{_mandir}/man5/typerules.5f.gz
%{_mandir}/man8/dialtest.8c.gz
%{_mandir}/man8/faxinfo.8c.gz
%{_mandir}/man8/faxwatch.8c.gz
%{_mandir}/man8/faxsetup.8c.gz
%{_mandir}/man8/pdf2fax.8c.gz
%{_mandir}/man8/tiff2fax.8c.gz
%{_mandir}/man8/tiffcheck.8c.gz
%{_mandir}/man8/faxfetch.8c.gz
%{_mandir}/man8/faxsetup.linux.8c.gz
%{_mandir}/man8/typetest.8c.gz
%dir %{_sysconfdir}/hylafax
%dir %{_sysconfdir}/hylafax/faxmail
%dir %{_sysconfdir}/hylafax/faxmail/application
%dir %{_sysconfdir}/hylafax/faxmail/image
%config(noreplace) %{_sysconfdir}/hylafax/faxcover.ps
%config(noreplace) %{_sysconfdir}/hylafax/faxmail.ps
%config(noreplace) %{_sysconfdir}/hylafax/pagesizes
%config(noreplace) %{_sysconfdir}/hylafax/typerules
%{faxspool}/bin/genfontmap.ps
%config(noreplace) %{faxspool}/etc/dialrules*
%defattr(755,root,root,-)
%{_bindir}/*
%{_sbindir}/dialtest
%{_sbindir}/edit-faxcover
%{_sbindir}/faxfetch
%{_sbindir}/faxinfo
%{_sbindir}/faxsetup
%{_sbindir}/faxsetup.linux
%{_sbindir}/faxwatch
%{_sbindir}/textfmt
%{_sbindir}/tiffcheck
%{_sbindir}/typetest
%{faxspool}/bin/common-functions
%{faxspool}/bin/pcl2fax
%{faxspool}/bin/pdf2fax.gs
%{faxspool}/bin/ps2fax.gs
%{faxspool}/bin/tiff2fax
%{faxspool}/bin/tiff2pdf
%{_sysconfdir}/hylafax/faxmail/application/binary
%{_sysconfdir}/hylafax/faxmail/application/pdf
%{_sysconfdir}/hylafax/faxmail/application/octet-stream
%{_sysconfdir}/hylafax/faxmail/image/tiff
%defattr(-,uucp,uucp,-)
%dir %{faxspool}
%dir %{faxspool}/etc

%changelog
* Tue Jul 26 2022 Lee Howard <faxguy@howardsilvan.com> - 7.0.6-1
- update to 7.0.6

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 4 2022 Lee Howard <faxguy@howardsilvan.com> - 7.0.5-1
- update to 7.0.5

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 7.0.4-3
- Rebuilt with OpenSSL 3.0.0

* Fri Sep  3 2021 Lee Howard <faxguy@howardsilvan.com> - 7.0.4-2
- update to 7.0.4 release

* Sat Jul 24 2021 Lee Howard <faxguy@howardsilvan.com> - 7.0.4-1
- update to 7.0.4 prerelease to address build on F34

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 4 2020 Lee Howard <faxguy@howardsilvan.com> - 7.0.3-1
- update to 7.0.3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Lee Howard <faxguy@howardsilvan.com> - 7.0.2-1
- update to 7.0.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Lee Howard <faxguy@howardsilvan.com> - 7.0.1-1
- update to 7.0.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Lee Howard <faxguy@howardsilvan.com> - 7.0.0-1
- update to 7.0.0, add openssl dependencies

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 5.6.1-2
- Rebuilt for libcrypt.so.2 (#1666033)

* Tue Sep 18 2018 Lee Howard <faxguy@howardsilvan.com> - 5.6.1-1
- update to 5.6.1

* Mon Jul 16 2018 Lee Howard <faxguy@howardsilvan.com> - 5.6.0-1
- update to 5.6.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Lee Howard <faxguy@howardsilvan.com> - 5.5.9-8
  Add BuildRequires: gcc-c++ to adhere to packaging guidelines

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 5.5.9-6
- Rebuilt for switch to libxcrypt

* Thu Nov 16 2017 Lee Howard <faxguy@howardsilvan.com> - 5.5.9-5
- add Requires uucp for client package

* Thu Oct 12 2017 Lee Howard <faxguy@howardsilvan.com> - 5.5.9-4
- change dependencies from ghostscript-fonts to urw-base35-fonts for f28

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 Lee Howard <faxguy@howardsilvan.com> - 5.5.9-1
- update to 5.5.9 (unreleased SVN checkout) to fix gcc v7 build problem with 5.5.8-2 on f26

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 06 2016 Lee Howard <faxguy@howardsilvan.com> 5.5.8-1
- update to 5.5.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Lee Howard <faxguy@howardsilvan.com> 5.5.7-1
- update to 5.5.7
- add hylafax-faxgetty@.service
- allow sysconfig/hylafax+ to disable faxqclean from being run
- fix lockdir location for recent dist releases

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Apr 27 2015 Lee Howard <faxguy@howardsilvan.com> 5.5.6-1
- update to 5.5.6

* Sun Feb 22 2015 Robert Scheck <robert@fedoraproject.org> 5.5.5-5
- allow the package building for RHEL >= 7 with systemd support
- build using lcms2 on all Fedora branches and also RHEL >= 7
- add build requirements to sendmail(1), ghostscript and mgetty
- correct wrong day of the week in %%changelog to silence rpm
- correct permissions of %%{_sysconfdir}/sysconfig/hylafax+ file

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Aug 14 2014 Rex Dieter <rdieter@fedoraproject.org> 5.5.5-3
- rebuild (jbigkit)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Lee Howard <faxguy@howardsilvan.com> - 5.5.5-1
- update to 5.5.5

* Thu Apr 24 2014 Lee Howard <faxguy@howardsilvan.com> - 5.5.4-3
- add uucp dependency for build and install, bug 998737

* Sat Sep 14 2013 Lee Howard <faxguy@howardsilvan.com> - 5.5.4-2
- fix preun stop call to hylafax+ (and not hylafax)

* Tue Aug 06 2013 Lee Howard <faxguy@howardsilvan.com> - 5.5.4-1
- update to 5.5.4
- add _hardened_build 1 per https://bugzilla.redhat.com/show_bug.cgi?id=955168

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr 14 2013 Robert Scheck <robert@fedoraproject.org> 5.5.3-4
- ship hylafax+ initscript only in base, not in both packages

* Sat Apr 13 2013 Robert Scheck <robert@fedoraproject.org> 5.5.3-3
- ensure that hylafax+-client has same architecture like base
- obsolete hylafax-client packages in favor of hylafax+-client
- added option to disable daily faxcron like in other hylafax
- added %%{_sysconfdir}/sysconfig/hylafax+ also for RHEL 5 & 6
- use $HFAXD_OPTIONS in hylafax+ initscript on RHEL 5 and 6
- added $FAXQ_OPTIONS to hylafax+ initscript for RHEL 5 and 6

* Tue Feb 26 2013 Lee Howard <faxguy@howardsilvan.com> - 5.5.3-2
- add Group tag for client package

* Mon Feb 25 2013 Lee Howard <faxguy@howardsilvan.com> - 5.5.3-1
- update to 5.5.3
- break out client utilities into hylafax+-client package
- add sysconfig feature

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 5.5.2-8
- rebuild due to "jpeg8-ABI" feature drop

* Sat Dec 15 2012 Lee Howard <faxguy@howardsilvan.com> - 5.5.2-7
- make jbigkit-devel BuildRequires conditional for Fedora >= 16

* Tue Dec 11 2012 Lee Howard <faxguy@howardsilvan.com> - 5.5.2-6
- make dependency on systemd-units and system instead of /bin/systemctl
- modify systemd scriptlets
- use defattr to accomodate correct permissions for mock builds

* Sat Dec 8 2012 Lee Howard <faxguy@howardsilvan.com> - 5.5.2-5
- remove defattr from files
- rename patches and all but Source0 to hylafax+
- remove config(noreplace) from FIFO
- add /bin/systemctl build dependency for Fedora > 16

* Mon Dec 3 2012 Lee Howard <faxguy@howardsilvan.com> - 5.5.2-4
- add missing man pages

* Sun Nov 4 2012 Lee Howard <faxguy@howardsilvan.com> - 5.5.2-3
- spec optimizations
- clarify linkage in libfaxserver
- add systemd support

* Thu Nov 1 2012 Lee Howard <faxguy@howardsilvan.com> - 5.5.2-2
- change package name to hylafax+
- add Provides: hylafax

* Sat Oct 13 2012 Lee Howard <faxguy@howardsilvan.com> - 5.5.2-1
- update to 5.5.2

* Thu Jan 12 2012 Lee Howard <faxguy@howardsilvan.com> - 5.5.1-1
- update to 5.5.1

* Sat Dec 18 2010 Lee Howard <faxguy@howardsilvan.com> - 5.5.0-1
- update to 5.5.0

* Wed Oct 13 2010 Lee Howard <faxguy@howardsilvan.com> - 5.4.3-1
- update to 5.4.3

* Sun May 2 2010 Lee Howard <faxguy@howardsilvan.com> - 5.4.2-1
- update to 5.4.2

* Mon Feb 22 2010 Lee Howard <faxguy@howardsilvan.com> - 5.4.1-1
- update to 5.4.1

* Wed Dec 23 2009 Lee Howard <faxguy@howardsilvan.com> - 5.4.0-1
- update to 5.4.0
- add lcms-devel build dependency

* Sun Oct 25 2009 Lee Howard <faxguy@howardsilvan.com> - 5.3.0-1
- update to 5.3.0

* Sat Feb 28 2009 Lee Howard <faxguy@howardsilvan.com> - 5.2.9-1
- update to 5.2.9
- remove "Provides: hylafax"

* Sun Dec 21 2008 Lee Howard <faxguy@howardsilvan.com> - 5.2.8-1
- update to 5.2.8

* Mon Apr 28 2008 Lee Howard <faxguy@howardsilvan.com> - 5.2.4-3
- openldap-devel and pam-devel build dependencies

* Wed Apr 23 2008 Lee Howard <faxguy@howardsilvan.com> - 5.2.4-1
- update to 5.2.4

* Sat Mar 29 2008 Lee Howard <faxguy@howardsilvan.com> - 5.2.3-1
- update to 5.2.3

* Fri Jan 18 2008 Lee Howard <faxguy@howardsilvan.com> - 5.2.2-1
- make licensing BSD, initscript is not config, remove libtiff dependency

* Thu Nov 8 2007 Lee Howard <faxguy@howardsilvan.com> - 5.1.11-1
- add libtiff dependency

* Thu Aug 2 2007 Lee Howard <faxguy@howardsilvan.com> - 5.1.7-1
- update to 5.1.7

* Sat Jul 14 2007 Lee Howard <faxguy@howardsilvan.com> - 5.1.6-1
- accomodate MIMEConverter script location change

* Fri Mar 23 2007 Lee Howard <faxguy@howardsilvan.com> - 5.1.2-1
- made faxq's FIFO "noreplace" to keep upgrades from messing up a running faxq

* Thu Mar  8 2007 Lee Howard <faxguy@howardsilvan.com> - 5.1.1-1
- update to 5.1.1

* Thu Feb 22 2007 Lee Howard <faxguy@howardsilvan.com> - 5.1.0-1
- update to 5.1.0

* Thu Jan 11 2007 Lee Howard <faxguy@howardsilvan.com> - 5.0.4-1
- update to 5.0.4

* Mon Jan 1 2007 Lee Howard <faxguy@howardsilvan.com> - 5.0.3-1
- update to 5.0.3

* Wed Dec 13 2006 Lee Howard <faxguy@howardsilvan.com> - 5.0.2-1
- update to 5.0.2

* Wed Nov 1 2006 Lee Howard <faxguy@howardsilvan.com> - 5.0.0-1
- update to 5.0.0
- disable build of debuginfo package
- change ownership of config and dev to root,root
- move changelog to the end of the spec file

* Mon Sep 18 2006 Lee Howard <faxguy@howardsilvan.com> - 4.3.0.11-1
- update to 4.3.0.1

* Tue Apr 11 2006 Lee Howard <faxguy@howardsilvan.com> - 4.2.5.6-1
- update to 4.2.5.6

* Tue Apr 11 2006 Lee Howard <faxguy@howardsilvan.com> - 4.2.5.5-1
- initial 4.2.5.5 build
