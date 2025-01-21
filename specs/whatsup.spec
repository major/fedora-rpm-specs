%global libname libnodeupdown

# There is no opensm on 32-bit ARM, bugs #1484155, #1556539
# There is no libibcommon on s390, s390x
%ifnarch %{arm} s390 s390x
%global with_ib 1
%else
%global with_ib 0
%endif

Summary:       Node up/down detection utility
Name:          whatsup
Version:       1.14
Release:       48%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           https://computing.llnl.gov/linux/whatsup.html
Source0:       http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}-1/%{name}-%{version}.tar.gz
Source1:       %{name}-hostsfile
Source2:       %{name}-pingd.service
Patch0:        %{name}-%{version}-bug#1117251.patch
# Adjust to Autconf-2.71, bug #1999491,
# <https://savannah.gnu.org/support/index.php?110571>,
# <https://github.com/chaos/whatsup/pull/3>
Patch1:        %{name}-%{version}-Adjust-to-Autoconf-2.71.patch
BuildRequires: make
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker) expat-devel, libtool-ltdl-devel, libgenders-devel
BuildRequires: autoconf, automake, libtool
%if 0%{?fedora} > 15
BuildRequires: systemd-units
%endif
Requires:      %{libname} = %{version}-%{release}

%description
Whatsup is a cluster node up/down detection utility.

Whatsup can quickly calculate and output the up and down nodes of a cluster.
Whatsup allows some tools, such as Pdsh, to operate more quickly by
not operating on down nodes. Whatsup calculates the up and down nodes of a
cluster through one of several possible backend tools
and several optional cluster node databases.

%package -n    %{libname}-devel
Summary:       Development headers for %{libname}
Requires:      %{libname} = %{version}-%{release}
%description -n %{libname}-devel
development headers for %{libname}

%package -n    %{libname}
Summary:       A cluster node up/down detection library
%description -n %{libname}
A cluster node up/down detection library, with different backends

%package -n    %{libname}-backend-ganglia
Summary:       Ganglia backend for %{libname}
Requires:      %{libname} = %{version}-%{release}
BuildRequires: ganglia-devel
%description -n %{libname}-backend-ganglia
Ganglia backend module for %{libname}

%if %{with_ib}
%package -n    %{libname}-backend-openib
Summary:       Openib backend for %{libname}
BuildRequires: opensm-devel, libibcommon-devel, rdma-core-devel
Requires:      %{libname} = %{version}-%{release}
%description -n %{libname}-backend-openib
openib backend module for %{libname}
%endif

%package -n    %{libname}-backend-pingd
Summary:       Pingd backend for %{libname}
Requires:      %{libname} = %{version}-%{release}
Requires:      %{name}-pingd = %{version}-%{release}
%description -n %{libname}-backend-pingd
pingd backend module for %{libname}

%package -n    %{name}-pingd
Summary:       Pingd daemon for %{name}
Requires:      %{libname} = %{version}-%{release}
%if 0%{?fedora} > 15
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%else
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(preun): initscripts
Requires(postun): initscripts
%endif

%description -n %{name}-pingd
pingd daemon for %{name}

%package -n    perl-%{libname}
Summary:       Perl bindings for %{libname}
Requires:      %{libname} = %{version}-%{release}
%description -n perl-%{libname}
Perl bindings for %{libname}

%{?filter_setup:
%filter_provides_in %{perl_vendorarch}/.*\.so$
%filter_setup
}

%package -n    %{libname}-clusterlist-hostsfile
Summary:       Hostsfile clusterlist module for %{libname}
Requires:      %{libname} = %{version}-%{release}
%description -n %{libname}-clusterlist-hostsfile
Hostsfile clusterlist module for %{libname}

%package -n    %{libname}-clusterlist-genders
Summary:       Genders clusterlist module for %{libname}
Requires:      %{libname} = %{version}-%{release}
%description -n %{libname}-clusterlist-genders
Genders clusterlist module for %{libname}

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p1
%if 0%{?fedora} > 17
autoreconf -I config -f -i
%endif

%if 0%{?rhel} <= 6
cat << \EOF > %{name}-python-prov
#!/bin/sh
%{__python_provides} $* |\
sed -e '/.*Lib%{name}.so.*/d'
EOF

%global __python_provides %{_builddir}/%{name}-%{version}/%{name}-python-prov
chmod +x %{__python_provides}

cat << \EOF > %{name}-perl-prov
#!/bin/sh
%{__perl_provides} $* |\
sed -e '/.*Lib%{name}.so.*/d'
EOF

%global __perl_provides %{_builddir}/%{name}-%{version}/%{name}-perl-prov
chmod +x %{__perl_provides}
%endif


%build
%configure \
    --disable-static \
    --with-perl-extensions \
    --with-perl-vendor-arch \
    --with-perl-destdir="%{buildroot}"
make %{?_smpflags}

%install
DESTDIR=%{buildroot} make install

%if 0%{?fedora} > 15
mkdir -vp %{buildroot}%{_unitdir}
install -m 644 -p %{SOURCE2} %{buildroot}%{_unitdir}/
rm -rf %{buildroot}%{_initrddir}
%endif

chmod -x %{buildroot}%{_sysconfdir}/nodeupdown.conf
chmod -x %{buildroot}%{_sysconfdir}/pingd.conf

# for whatsup-pingd
install -m 644 -p %{SOURCE1} %{buildroot}%{_sysconfdir}/hostsfile

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name "*.bs" -exec rm -f {} \;
find %{buildroot} -type f -name "*.la" -exec rm -f {} \;

%{_fixperms} %{buildroot}/*
touch %{buildroot}%{_sysconfdir}/hostsfile

%ldconfig_scriptlets -n %{libname}

%post -n %{name}-pingd
%if 0%{?fedora} > 15
%if 0%{?fedora} > 17
%systemd_post whatsup-pingd.service
%else
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%endif
%else
# EPEL thing
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /sbin/chkconfig --add whatsup-pingd
fi
%endif

%preun -n %{name}-pingd
%if 0%{?fedora} > 15
%if 0%{?fedora} > 17
%systemd_preun whatsup-pingd.service
%else
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable whatsup-pingd.service > /dev/null 2>&1 || :
    /bin/systemctl stop whatsup-pingd.service > /dev/null 2>&1 || :
fi
%endif
%else
# EPEL thing
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /sbin/service whatsup-pingd stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del whatsup-pingd >/dev/null 2>&1 || :
fi
%endif

%postun -n %{name}-pingd
%if 0%{?fedora} > 15
%if 0%{?fedora} > 17
%systemd_postun_with_restart whatsup-pingd.service
%else
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart whatsup-pingd.service >/dev/null 2>&1 || :
fi
%endif
%else
#EPEL thing
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /sbin/service whatsup-pingd condrestart
fi
%endif

%if 0%{?fedora} > 15
%triggerun -n %{name}-pingd -- whatsup-pingd < 1.12-6
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply whatsup-pingd
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save whatsup-pingd >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del whatsup-pingd >/dev/null 2>&1 || :
/bin/systemctl try-restart whatsup-pingd.service >/dev/null 2>&1 || :
%endif

%files
%doc AUTHORS COPYING DISCLAIMER NEWS README ChangeLog
%{_bindir}/whatsdown
%{_bindir}/whatsup
%{_mandir}/man1/*

%files -n perl-%{libname}
%doc COPYING
%{_mandir}/man3/Libnodeupdown.3*
%{_mandir}/man3/Nodeupdown.3*
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/

%files -n %{name}-pingd
%doc COPYING
%if 0%{?fedora} > 15
%{_unitdir}/%{name}-pingd.service
%else
%{_sysconfdir}/rc.d/init.d/%{name}-pingd
%endif
%{_sbindir}/pingd
%dir %{_libdir}/pingd
%{_libdir}/pingd/pingd_clusterlist_hostsfile.so
%{_libdir}/pingd/pingd_clusterlist_genders.so
%config(noreplace) %{_sysconfdir}/hostsfile
%{_mandir}/man5/pingd.conf.5*
%{_mandir}/man8/pingd.8*
%config(noreplace) %{_sysconfdir}/pingd.conf

%files -n %{libname}-devel
%doc COPYING
%{_includedir}/nodeupdown.h
%dir %{_includedir}/nodeupdown
%{_includedir}/nodeupdown/*.h
%{_libdir}/libnodeupdown*.so
%{_mandir}/man3/nodeupdown*

%files -n %{libname}
%doc COPYING
%{_libdir}/libnodeupdown*.so.*
%dir %{_libdir}/nodeupdown
%{_mandir}/man3/libnodeupdown.3*
%{_mandir}/man5/nodeupdown.conf.5*
%config(noreplace) %{_sysconfdir}/nodeupdown.conf

%files -n %{libname}-backend-ganglia
%doc COPYING
%{_libdir}/nodeupdown/nodeupdown_backend_ganglia.so

%if %{with_ib}
%files -n %{libname}-backend-openib
%doc COPYING
%{_libdir}/nodeupdown/nodeupdown_backend_openib.so
%endif

%files -n %{libname}-backend-pingd
%doc COPYING
%{_libdir}/nodeupdown/nodeupdown_backend_pingd.so

%files -n %{libname}-clusterlist-genders
%doc COPYING
%{_libdir}/nodeupdown/nodeupdown_clusterlist_genders.so

%files -n %{libname}-clusterlist-hostsfile
%doc COPYING
%{_libdir}/nodeupdown/nodeupdown_clusterlist_hostsfile.so
%config(noreplace) %{_sysconfdir}/hostsfile


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.14-47
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-45
- Perl 5.40 rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-42
- Perl 5.38 rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-39
- Perl 5.36 rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 26 2021 Petr Pisar <ppisar@redhat.com> - 1.14-37
- Adjust to Autconf-2.71 (bug #1999491)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-35
- Perl 5.34 rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.14-34
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-31
- Perl 5.32 rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-28
- Perl 5.30 rebuild

* Fri May 03 2019 Petr Pisar <ppisar@redhat.com> - 1.14-27
- Disable InfiniBand support on 32-bit ARM architectures (bug #1556539)

* Mon Apr 22 2019 Björn Esser <besser82@fedoraproject.org> - 1.14-26
- rebuilt(opensm)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-23
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.14-19
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-18
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-16
- Perl 5.24 rebuild

* Wed Apr 20 2016 Michal Schmidt <mschmidt@redhat.com> - 1.14-15
- Rebuild for new opensm.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-12
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.14-11
- Perl 5.20 rebuild

* Wed Aug 20 2014 Kevin Fenzi <kevin@scrye.com> - 1.14-10
- Rebuild for rpm bug 1131892

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.14-5
- Perl 5.18 rebuild

* Tue Mar 26 2013 David Brown <david.brown@pnnl.gov> - 1.14-4
- only do the autoreconf for fedora 17+

* Tue Mar 26 2013 David Brown <david.brown@pnnl.gov> - 1.14-3
- added autoreconf to fix bug #926718
- added autoconf, automake, libtool to build depends just to be safe

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 David Brown <david.brown@pnnl.gov> - 1.14-1
- New upstream version of whatsup
- added libtool-ltdl-devel build deps
- added genders build deps and sub packages

* Mon Sep 10 2012 David Brown <david.brown@pnnl.gov> - 1.13-6
- get the damn macro right for postun

* Mon Sep 10 2012 David Brown <david.brown@pnnl.gov> - 1.13-5
- add systemd macros to post postun preun

* Thu Aug 9 2012 David Brown <david.brown@pnnl.gov> - 1.13-4
- add dependancies for EPEL 5/6 service and chkconfig
- fixes bug #844900

* Wed Aug 1 2012 David Brown <david.brown@pnnl.gov> - 1.13-3
- fix issues with restarting services on EPEL 5/6

* Sun Jul 29 2012 David Brown <david.brown@pnnl.gov> - 1.13-2
- fixed logic for systemd dependancies on EPEL 5/6

* Tue Jul 24 2012 David Brown <david.brown@pnnl.gov> - 1.13-1
- New Upstream Release
- Made one spec file to rule them all ... at least el5 el6 f17 f16

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.12-9
- Perl 5.16 rebuild

* Tue Mar 13 2012 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.12-8
- Rebuild for new opensm

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 23 2011 Tom Callaway <spot@fedoraproject.org> - 1.12-6
- convert to systemd

* Tue Aug 02 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.12-5
- Rebuild for new opensm

* Mon Jul 25 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.12-4
- Rebuild for new libopensm

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.12-3
- Perl mass rebuild

* Thu Mar 10 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.12-2
- Install into vendorarch instead of sitearch

* Mon Mar 07 2011 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.12-1
- Upstream released new version
- Link against system-provided expat (#652981)
- Fixes FTBFS (#661001)
- Drop patch for incorrect open which was merged upstream

* Thu Sep 30 2010 Dan Horák <dan[at]danny.cz> 1.10-2
- no InfiniBand on s390(x)

* Thu Jun 24 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.10-1
- Upstream released new version

* Fri May 07 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.9-6
- Mass rebuild with perl-5.12.0

* Wed Mar 10 2010 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.9-5
- Rebuild to pick up new opensm

* Mon Dec 21 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.9-4
- Rebuild to pick up new opensm

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.9-3
- rebuild against perl 5.10.1

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 07 2009 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.9-1
- Upstream released new version
- Add openib backend
- Move clusterlist_hostsfile to separate module.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 14 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.8-1
- Upstream release new version

* Fri Apr 25 2008 Ruben Kerkhof <ruben@rubenkerkhof.com> 1.7-1
- Initial import



