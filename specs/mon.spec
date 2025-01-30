# TODO: Split monitors and alerts into subpackages
#       they drag in way too many dependencies

%global moncgi_version 1.52
%global fixlib sed 's,/usr/lib,%{_libdir},g'

Name:           mon
Summary:        General-purpose resource monitoring system
Version:        1.2.0
Release:        41%{?dist}
License:        GPL-2.0-or-later
URL:            http://www.kernel.org/software/mon/

Source0:        ftp://ftp.kernel.org/pub/software/admin/mon/mon-%{version}.tar.bz2
Source1:        ftp://ftp.kernel.org/pub/software/admin/mon/contrib/cgi-bin/mon.cgi/mon.cgi-%{moncgi_version}.tar.bz2
Source2:        ftp://ftp.kernel.org/pub/software/admin/mon/contrib/all-alerts.tar.bz2

Source3:        mon.cf
Source4:        mon.service
Source5:        userfile

Patch0:         mon-1.2.0-perl.patch
Patch1:         mon-1.2.0-uucp.patch
# Use libtirpc instead of rpc/rpc.h from glibc, bug #1675405
Patch2:         mon-1.2.0-Port-to-libtirpc.patch
Patch3:         mon-1.2.0-fix_signal.patch

Requires:       perl(Authen::PAM)
Requires:       iputils
Requires:       fping
Requires:       traceroute
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  dos2unix
BuildRequires:  perl-generators
# pkgconfig(libtirpc) for Port-to-libtirpc.patch, bug #1675405,
# <https://sourceforge.net/p/mon/patches/11/>
BuildRequires:  pkgconfig(libtirpc)
BuildRequires:  systemd-units


%description
Mon is a general-purpose resource monitoring system.  It can be used
to monitor network service availability, server problems,
environmental conditions (i.e., the temperature in a room) or other
things. Mon can be used to test the condition and/or to trigger an
action upon failure of the condition.  Mon keeps the testing and
action-taking tasks as separate, stand-alone programs.

Mon is very extensible.  Monitors and alerts are not a part of mon, but
the distribution comes with a handful of them to get you started. This
means that if a new service needs monitoring, or if a new alert is
required, the mon server will not need to be changed.


%prep
%setup -q -a 1 -a 2
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

# Filter out unwanted requires
cat << \EOF > %{name}-req
#!/bin/sh
%{__perl_requires} $* |\
sed -e '
        /perl(Math::TrulyRandom)/d
        /perl(Net::hostent)/d
'
EOF

%define __perl_requires %{_builddir}/%{name}-%{version}/%{name}-req
chmod +x %{__perl_requires}


%build
for F in CHANGES doc/README.syslog.monitor
do
        iconv -f ISO-8859-1 -t UTF-8 $F >tmp
        touch --reference $F tmp
        mv tmp $F
done

dos2unix -q -k alerts/sms/sms.alert

make %{?_smp_mflags} -C mon.d \
        CFLAGS="%{optflags} -DUSE_VENDOR_CF_PATH=1"


%install
install -d -m0755 %{buildroot}%{_bindir}             \
        %{buildroot}%{_mandir}/man{1,8}/             \
        %{buildroot}%{_libdir}/mon/{alert.d,mon.d}/  \
        %{buildroot}%{_sysconfdir}/mon/              \
        %{buildroot}%{_unitdir}                    \
        %{buildroot}%{_localstatedir}/www/cgi-bin/   \
        %{buildroot}%{_localstatedir}/lib/mon/{log.d,state.d}/

install -p -m0755 mon clients/moncmd clients/monshow clients/skymon/skymon %{buildroot}%{_bindir}
install -p -m0644 doc/*.1 %{buildroot}%{_mandir}/man1/
install -p -m0644 doc/*.8 %{buildroot}%{_mandir}/man8/

install -p -m0755 mon.d/*.wrap mon.d/*.monitor %{buildroot}%{_libdir}/mon/mon.d/
install -p -m0755 alert.d/* %{buildroot}%{_libdir}/mon/alert.d/
install -p -m0755 alerts/*/*.alert %{buildroot}%{_libdir}/mon/alert.d/

install -d %{buildroot}%{_sysconfdir}/mon
%{fixlib} etc/auth.cf >%{buildroot}%{_sysconfdir}/mon/auth.cf
%{fixlib} %{SOURCE3} >%{buildroot}%{_sysconfdir}/mon/mon.cf
install -Dp -m0644 %{SOURCE4} %{buildroot}%{_unitdir}/mon.service
install -Dp -m0600 %{SOURCE5} %{buildroot}%{_sysconfdir}/mon/userfile

install -Dp -m0755 mon.cgi-%{moncgi_version}/mon.cgi %{buildroot}%{_localstatedir}/www/cgi-bin/mon.cgi

# Fix permissions in examples documentation files
chmod -x mon.cgi-1.52/mon.cgi                   \
        clients/skymon/skymon                   \
        mon.cgi-1.52/util/moncgi-appsecret.pl   \
        doc/README.snmpdiskspace.monitor        \
        utils/cf-to-hosts                       \
        clients/batch-example                   \
        utils/syslog.monitor

# Fix library path in examples
%{fixlib} -i etc/*.cf


%post
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi


%preun
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable mon.service > /dev/null 2>&1 || :
    /bin/systemctl stop mon.service > /dev/null 2>&1 || :
fi


%postun
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart mon.service >/dev/null 2>&1 || :
fi

%triggerun -- mon < 1.2.0-10
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply mon
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save mon >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del mon >/dev/null 2>&1 || :
/bin/systemctl try-restart mon.service >/dev/null 2>&1 || :


%files
%license COPYING COPYRIGHT
%doc CHANGES CREDITS README TODO doc/README.*
%doc KNOWN-PROBLEMS utils/ VERSION
%doc alerts/*/*.README mon.cgi-1.52/
%doc clients/{skymon,batch-example} etc/*.cf etc/example.m4 etc/example.monshowrc
%config(noreplace) %{_sysconfdir}/mon/
%{_unitdir}/*
%{_mandir}/man?/*
%{_localstatedir}/www/cgi-bin/mon.cgi
%{_bindir}/*
%{_localstatedir}/lib/mon/
%dir %{_libdir}/mon
%{_libdir}/mon/alert.d
%dir %{_libdir}/mon/mon.d
%{_libdir}/mon/mon.d/*.monitor
%attr(2755, root, uucp) %{_libdir}/mon/mon.d/dialin.monitor.wrap

# These packages are not in EPEL
%if 0%{?rhel} <= 5
# perl(Expect)
%exclude %{_libdir}/mon/mon.d/dialin.monitor
# perl(Authen::Radius)
%exclude %{_libdir}/mon/mon.d/radius.monitor
%endif

# These are not in Fedora either
# perl(AOL::TOC)
%exclude %{_libdir}/mon/alert.d/aim.alert
# perl(Filesys::DiskSpace)
%exclude %{_libdir}/mon/mon.d/freespace.monitor


%changelog
* Tue Jan 28 2025 Michal Josef Špaček <mspacek@redhat.com> - 1.2.0-41
- Fix incompatible pointer type (rhbz#2340877)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 21 2022 Michal Josef Špaček <mspacek@redhat.com> - 1.2.0-34
- Update license to SPDX format
- Use %license macro

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 10 2019 Petr Pisar <ppisar@redhat.com> - 1.2.0-26
- Use libtirpc instead of rpc/rpc.h from glibc (bug #1675405)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 1.2.0-15
- Bulk sad and useless attempt at consistent SPEC file formatting

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
- BR: systemd-units for %%{_unitdir} macro definition

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.2.0-13
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 18 2012 Jon Ciesla <limburgher@gmail.com> - 1.2.0-10
- Migrate to systemd, BZ 789890.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-8
- Rebuilt for glibc bug#747377

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Apr 21 2010 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 1.2.0-6
- Add missing dependencies (#584281)
- Fix path to libdir for 64-bits

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 1.2.0-3
- Remove AOL::TOC
- Add most of shipped monitors (GDC #581)

* Sun Jul 13 2008 Lubomir Rintel (GoodData) <lubo.rintel@gooddata.com> - 1.2.0-2
- Refactor a bit, to fit Fedora customs and guidelines
- Fix use of optflags
- Fix file encodings
- Do not start service by default
- Remove unneeded requires
- Fix file modes

* Wed Jun 27 2007 Dag Wieers <dag@wieers.com> - 1.2.0-1 - 4303+/dries
- Updated to release 1.2.0.

* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 0.99.2-1
- Fixed problems with perl-modules.

* Fri Jan 09 2004 Dag Wieers <dag@wieers.com> - 0.99.2-0
- Initial package. (using DAR)
