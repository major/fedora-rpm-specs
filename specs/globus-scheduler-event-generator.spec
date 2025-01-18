%global _hardened_build 1

%if %{?fedora}%{!?fedora:0} >= 25 || %{?rhel}%{!?rhel:0} >= 8
%global use_systemd 1
%else
%global use_systemd 0
%endif

Name:		globus-scheduler-event-generator
%global _name %(tr - _ <<< %{name})
Version:	6.5
Release:	9%{?dist}
Summary:	Grid Community Toolkit - Scheduler Event Generator

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source1:	%{name}@.service
Source2:	%{name}
Source8:	README
#		https://github.com/gridcf/gct/pull/223
Patch0:		0001-Handle-64-bit-time_t-on-32-bit-systems.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-xio-devel >= 3
BuildRequires:	globus-gram-protocol-devel >= 11
BuildRequires:	globus-xio-gsi-driver-devel >= 2
BuildRequires:	libtool-ltdl-devel
BuildRequires:	doxygen
%if %{use_systemd}
BuildRequires:	systemd
%endif
#		Additional requirements for make check
BuildRequires:	perl-interpreter
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Compare)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::More)

Requires:	globus-xio-gsi-driver%{?_isa} >= 2

%package progs
Summary:	Grid Community Toolkit - Scheduler Event Generator Programs
Requires:	%{name}%{?_isa} = %{version}-%{release}

%if %{use_systemd}
%{?systemd_requires}
%else
Requires(post):		chkconfig
Requires(preun):	chkconfig
Requires(preun):	initscripts
Requires(postun):	initscripts
%endif

%package devel
Summary:	Grid Community Toolkit - Scheduler Event Generator Development Files
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package doc
Summary:	Grid Community Toolkit - Scheduler Event Generator Documentation Files
BuildArch:	noarch

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Scheduler Event Generator

%description progs
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-progs package contains:
Scheduler Event Generator Programs

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
Scheduler Event Generator Development Files

%description doc
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-doc package contains:
Scheduler Event Generator Documentation Files

%prep
%setup -q -n %{_name}-%{version}
%patch -P0 -p5

%build
# Reduce overlinking
export LDFLAGS="-Wl,--as-needed -Wl,-z,defs %{?__global_ldflags}"

%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir} \
	   --with-initscript-config-path=%{_sysconfdir}/sysconfig/%{name} \
	   --with-lockfile-path=/run/lock/subsys/%{name}

# Reduce overlinking
sed 's!CC \(.*-shared\) !CC \\\${wl}--as-needed \1 !' -i libtool

%make_build

%install
%make_install

# Remove libtool archives (.la files)
rm %{buildroot}%{_libdir}/*.la

# Remove start-up scripts
rm -rf %{buildroot}%{_sysconfdir}/init.d

# Install start-up scripts
%if %{use_systemd}
mkdir -p %{buildroot}%{_unitdir}
install -m 644 -p %{SOURCE1} %{buildroot}%{_unitdir}
%else
mkdir -p %{buildroot}%{_initddir}
install -p %{SOURCE2} %{buildroot}%{_initddir}
%endif

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

%check
%make_build check

%ldconfig_scriptlets

%if %{use_systemd}

%pre progs
# Remove old init config when systemd is used
/sbin/chkconfig --del %{name} > /dev/null 2>&1 || :

%post progs
if [ $1 -eq 1 ] ; then
    systemctl daemon-reload > /dev/null 2>&1 || :
fi

%preun progs
if [ $1 -eq 0 ] ; then
    for INSTANCE in `systemctl | grep %{name}@ | awk '{print $1;}'`; do
	systemctl --no-reload disable $INSTANCE > /dev/null 2>&1 || :
	systemctl stop $INSTANCE > /dev/null 2>&1 || :
    done
fi

%postun progs
if [ $1 -ge 1 ] ; then
    systemctl daemon-reload > /dev/null 2>&1 || :
    for INSTANCE in `systemctl | grep %{name}@ | awk '{print $1;}'`; do
	systemctl try-restart $INSTANCE > /dev/null 2>&1 || :
    done
fi

%else

%post progs
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add %{name}
fi

%preun progs
if [ $1 -eq 0 ]; then
    /sbin/chkconfig --del %{name}
    /sbin/service %{name} stop > /dev/null 2>&1 || :
fi

%postun progs
if [ $1 -ge 1 ]; then
    /sbin/service %{name} condrestart > /dev/null 2>&1 || :
fi

%endif

%files
%{_libdir}/libglobus_scheduler_event_generator.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%files progs
%{_sbindir}/globus-scheduler-event-generator
%{_sbindir}/globus-scheduler-event-generator-admin
%{_mandir}/man8/globus-scheduler-event-generator.8*
%{_mandir}/man8/globus-scheduler-event-generator-admin.8*
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%if %{use_systemd}
%{_unitdir}/%{name}@.service
%else
%{_initddir}/%{name}
%endif
%dir %{_sysconfdir}/globus
%dir %{_sysconfdir}/globus/scheduler-event-generator
%dir %{_sysconfdir}/globus/scheduler-event-generator/available

%files devel
%{_includedir}/globus/*
%{_libdir}/libglobus_scheduler_event_generator.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc %{_mandir}/man3/*
%dir %{_pkgdocdir}
%dir %{_pkgdocdir}/html
%doc %{_pkgdocdir}/html/*
%license GLOBUS_LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 29 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.5-8
- Handle 64 bit time_t on 32 bit systems

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 25 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.5-1
- New GCT release v6.2.20220524
- Drop patches included in the release

* Sat Mar 12 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.4-3
- Fix some compiler warnings

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 17 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.4-1
- Keep admin script in sync with init script

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.3-1
- Minor fixes to makefiles (6.2)
- Remove unused TESTS.pl script (6.3)
- Add BuildRequires perl-interpreter
- Add additional perl dependencies for tests
- Specfile updates
- Replace /var/run with /run in systemd unit file

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 10 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.1-4
- Add additional perl build dependencies due to perl package split

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.1-1
- Doxygen fixes

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.0-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.12-3
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir and _initddir macro definitions
  - Drop redundant Requires corresponding to autogenerated pkgconfig Requires
  - Don't clear the buildroot in the install section
  - Remove the clean section

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Sep 02 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.12-1
- GT6 update

* Sun Aug 14 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.11-4
- Convert to systemd unit file (Fedora 25+)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 08 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.11-1
- GT6 update

* Wed Feb 18 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.10-2
- Revert logfile location change

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.10-1
- Implement updated license packaging guidelines
- GT6 update (test fixes)

* Fri Dec 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.9-1
- GT6 update

* Thu Nov 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.8-1
- GT6 update
- Drop patch globus-scheduler-event-generator-manpages.patch (fixed upstream)

* Mon Oct 27 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.7-1
- GT6 update
- Drop patch globus-scheduler-event-generator-doxygen.patch (fixed upstream)
- Fix manpage typos

* Fri Sep 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.6-1
- Update to Globus Toolkit 6.0
- Drop GPT build system and GPT packaging metadata
- Enable checks
- Activate hardening flags

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 Brent Baude <baude@us.ibm.com> - 4.7-9
- Replace arch def of ppc64 with power64 macro for ppc64le enablement

* Thu Jan 09 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.7-8
- Fix logfile location

* Fri Dec 13 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.7-7
- Proper ownership of /etc/globus/scheduler-event-generator/available

* Sat Oct 26 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.7-6
- Remove obsolete workaround for broken RHEL 5 epstopdf

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.7-4
- Implement updated packaging guidelines

* Tue May 21 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.7-3
- Add aarch64 to the list of 64 bit platforms

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.7-1
- Update to Globus Toolkit 5.2.3

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 28 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.6-1
- Update to Globus Toolkit 5.2.1

* Tue Jan 24 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.4-2
- Fix broken links in README file

* Thu Dec 15 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.4-1
- Update to Globus Toolkit 5.2.0
- Drop patch globus-scheduler-event-generator.patch (fixed upstream)

* Mon Apr 25 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.1-4
- Add README file

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 23 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.1-2
- Update to Globus Toolkit 5.0.0

* Wed Jul 29 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.1-1
- Autogenerated
