Name:       burp
Summary:    A network-based backup and restore program
Version:    2.1.32
Release:    15%{?dist}
License:    AGPLv3 and BSD and GPLv2+ and LGPLv2+
URL:        http://burp.grke.org/
Source0:    https://github.com/grke/burp/archive/%{version}.tar.gz
Source1:    burp.init
Source2:    burp.service

BuildRequires:  libtool
BuildRequires:  librsync-devel
BuildRequires:  zlib-devel
BuildRequires:  openssl-devel
BuildRequires:  ncurses-devel
BuildRequires:  libacl-devel
BuildRequires:  uthash-devel
BuildRequires:  yajl-devel

%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildRequires:  systemd-units
%endif
BuildRequires: make


%description
Burp is a network backup and restore program, using client and server.
It uses librsync in order to save network traffic and to save on the
amount of space that is used by each backup.
It also uses VSS (Volume Shadow Copy Service) to make snapshots when
backing up Windows computers.

%package client
Summary:    burp backup client
Requires:   librsync >= 1.0
Provides:   burp = %{version}-%{release}
Provides:   burp-client = %{version}-%{release}

%description client
Burp is a network backup and restore program, using client and server.
It uses librsync in order to save network traffic and to save on the
amount of space that is used by each backup.
It also uses VSS (Volume Shadow Copy Service) to make snapshots when
backing up Windows computers.


%package doc
Summary:    Documentation and samples for Burp backup
%if 0%{?fedora} || 0%{?rhel} >= 6
BuildArch:  noarch
%endif

%description doc
Burp is a network backup and restore program, using client and server.
It uses librsync in order to save network traffic and to save on the
amount of space that is used by each backup.
It also uses VSS (Volume Shadow Copy Service) to make snapshots when
backing up Windows computers.


%package server
Summary:    burp backup server
Requires:   burp-client%{?_isa} = %{version}-%{release}
Requires:   openssl-perl
Provides:   burp-server = %{version}-%{release}
Provides:   bedup = %{version}-%{release}
Provides:   vss_strip = %{version}-%{release}

%description server
Burp is a network backup and restore program, using client and server.
It uses librsync in order to save network traffic and to save on the
amount of space that is used by each backup.
It also uses VSS (Volume Shadow Copy Service) to make snapshots when
backing up Windows computers.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -vif
%configure --sysconfdir=%{_sysconfdir}/burp --docdir=%{_defaultdocdir}/%{name}-%{version}
make %{?_smp_mflags}

%install
# "install-all" target: also install config files and scripts
make install-all DESTDIR=%{buildroot}

# service files (server)
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/
%else
mkdir -p %{buildroot}%{_initrddir}
install -p -m 0755 %{SOURCE1} %{buildroot}%{_initrddir}/%{name}
%endif

# -doc: add server scripts examples
%global mydocbuild %{buildroot}%{_defaultdocdir}/%{name}-%{version}
mkdir -p %{mydocbuild}/server/scripts
cp -p configs/server/cron.example %{mydocbuild}/server/.
cp -p configs/server/out_of_date_report_script \
      configs/server/offsite-backup \
      %{mydocbuild}/server/scripts/.

# -doc: add server config examples (excluding -client's ones)
mkdir -p %{mydocbuild}/server/config/autoupgrade
cp -p configs/server/autoupgrade/*.script %{mydocbuild}/server/config/autoupgrade/.
cp -pr %{buildroot}%{_sysconfdir}/burp/.  %{mydocbuild}/server/config/.
rmdir %{mydocbuild}/server/config/CA-client
rm %{mydocbuild}/server/config/burp.conf

# -doc: add client scripts and config examples
mkdir -p %{mydocbuild}/client
cp -p configs/client/cron.example \
      configs/client/zfs_script \
      %{buildroot}%{_sysconfdir}/burp/burp.conf \
      %{mydocbuild}/client/.

# -server: do not provide a (test)client
rm %{buildroot}%{_sysconfdir}/burp/clientconfdir/testclient

%files doc
%{_defaultdocdir}/%{name}-%{version}/


%files client
%defattr(-,root,root,-)
%doc README CHANGELOG DONATIONS TODO CONTRIBUTORS UPGRADING
%if 0%{?rhel} <= 6
    %doc LICENSE
%else
    %license LICENSE
%endif
%config(noreplace) %{_sysconfdir}/burp/burp.conf
%dir %{_sysconfdir}/burp/CA-client
%dir %{_sysconfdir}/burp
%{_sbindir}/burp
%{_sbindir}/burp_ca
%{_mandir}/man8/burp.8*
%{_mandir}/man8/burp_ca.8*


%files server
%{_datadir}/burp
%config(noreplace) %{_sysconfdir}/burp/CA.cnf
%config(noreplace) %{_sysconfdir}/burp/burp-server.conf
%config(noreplace) %{_sysconfdir}/burp/clientconfdir/incexc/example
%dir %{_sysconfdir}/burp/clientconfdir/incexc
%dir %{_sysconfdir}/burp/clientconfdir
%dir %{_localstatedir}/spool/burp %attr(750 root root)
%{_bindir}/vss_strip
%{_sbindir}/bsigs
%{_sbindir}/bedup
%{_sbindir}/bsparse
%{_mandir}/man8/vss_strip.8*
%{_mandir}/man8/bedup.8*
%{_mandir}/man8/bsigs.8*
%{_mandir}/man8/bsparse.8*
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
%{_unitdir}/burp.service
%else
%{_initrddir}/burp
%endif

%post server
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
%systemd_post burp.service
%else
/sbin/chkconfig --add %{name}
%endif

%preun server
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
%systemd_preun burp.service
%else
if [ $1 = 0 ]; then
  /sbin/service %{name} stop > /dev/null 2>&1
  /sbin/chkconfig --del %{name}
fi
%endif

%postun server
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
%systemd_postun_with_restart burp.service
%else
if [ $1 -eq 2 ]; then
    /sbin/service burp upgrade || :
fi
%endif


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.32-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.32-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.32-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.32-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 24 2021 Björn Esser <besser82@fedoraproject.org> - 2.1.32-11
- Rebuild(uthash)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.1.32-10
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.32-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.1.32-8
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.32-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 2.1.32-2
- Rebuilt for libcrypt.so.2 (#1666033)

* Mon Aug 06 2018 Andrew Niemantsverdriet <andrewniemants@gmail.com> - 2.2.8-1
- bumped to 2.2.8

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.40-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.40-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.4.40-7
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.40-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.40-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.4.40-3
- Add burp-1.4.40-narrowing.patch (F24FTBFS, RHBZ#1307363).

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jul 08 2015 Pierre Bourgin <pierre.bourgin@free.fr> - 1.4.40-1
- bumped to 1.4.40
- provides burp-{client,server} packages now.
- rewrite to match EPEL SPEC file (http://pkgs.fedoraproject.org/cgit/burp.git/tree/burp.spec)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 15 2015 Andrew Niemantsverdriet <andrewniemants@gmail.com> - 1.4.36.6
- Added two configuration files so they would not be overwritten on update

* Wed May 13 2015 Andrew Niemantsverdriet <andrewniemants@gmail.com> - 1.4.36.5
- Only use license with compatible operating systems
- Fixed typo _initrdir -> _initddir and made sure the file gets the correct name

* Wed May 13 2015 Andrew Niemantsverdriet <andrewniemants@gmail.com> - 1.4.36.4
- Made systemd-units a conditional BuildRequire

* Tue May 12 2015 Andrew Niemantsverdriet <andrewniemants@gmail.com> - 1.4.36-3
- Updated licence field

* Sat May 09 2015 Andrew Niemantsverdriet <andrewniemants@gmail.com> - 1.4.36-2
- Added systemd-units as a build require

* Sat May 09 2015 Andrew Niemantsverdriet <andrewniemants@gmail.com> - 1.4.36-1
- Updated to latest stable version

* Fri May 08 2015 Andrew Niemantsverdriet <andrewniemants@gmail.com> - 1.3.48-6
- Changed the build require from uthash to uthash-devel

* Tue Mar 17 2015 Andrew Niemantsverdriet <andrewniemants@gmail.com> - 1.3.48-5
- Fixed scriptlets to correctly handle systemd

* Tue Feb 17 2015 Andrew Niemantsverdriet <andrewniemants@gmail.com> - 1.3.48-4
- Added scriptlets to handle systemd

* Mon Feb 09 2015 Andrew Niemantsverdriet <andrewniemants@gmail.com> - 1.3.48-3
- Split BuildRequires into one per line
- Moved the LICENSE file to the license macro
- Fixed spacing issue

* Mon Feb 02 2015 Andrew Niemantsverdriet <andrewniemants@gmail.com> - 1.3.48-2
- removed clean section of spec file
- changed install and files to conform to packaging guideline

* Tue Nov 25 2014 Andrew Niemantsverdriet <andrewniemants@gmail.com> - 1.3.48-1
- Initial spec file
