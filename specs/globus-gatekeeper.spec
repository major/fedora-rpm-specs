%global _hardened_build 1

%if %{?fedora}%{!?fedora:0} >= 25 || %{?rhel}%{!?rhel:0} >= 8
%global use_systemd 1
%else
%global use_systemd 0
%endif

Name:		globus-gatekeeper
%global _name %(tr - _ <<< %{name})
Version:	11.4
Release:	8%{?dist}
Summary:	Grid Community Toolkit - Globus Gatekeeper

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source1:	%{name}.service
Source2:	%{name}
Source3:	%{name}.README
Source8:	README

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 15
BuildRequires:	globus-gss-assist-devel >= 8
BuildRequires:	globus-gssapi-gsi-devel >= 9
BuildRequires:	openssl-devel
%if %{use_systemd}
BuildRequires:	systemd
%endif

Requires:	logrotate

%if %{use_systemd}
%{?systemd_requires}
%else
Requires(post):		chkconfig
Requires(preun):	chkconfig
Requires(preun):	initscripts
Requires(postun):	initscripts
%endif

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Globus Gatekeeper

%prep
%setup -q -n %{_name}-%{version}

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

# Remove start-up script
rm -rf %{buildroot}%{_sysconfdir}/init.d

# Install start-up script
%if %{use_systemd}
mkdir -p %{buildroot}%{_unitdir}
install -m 644 -p %{SOURCE1} %{buildroot}%{_unitdir}
%else
mkdir -p %{buildroot}%{_initddir}
install -p %{SOURCE2} %{buildroot}%{_initddir}
%endif

# Install post installation instructions
install -m 644 -p %{SOURCE3} %{buildroot}%{_pkgdocdir}/README.Fedora

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

mkdir -p %{buildroot}%{_sysconfdir}/grid-services
mkdir -p %{buildroot}%{_sysconfdir}/grid-services/available

%if %{use_systemd}

%pre
# Remove old init config when systemd is used
/sbin/chkconfig --del %{name} > /dev/null 2>&1 || :

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%else

%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add %{name}
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service %{name} stop > /dev/null 2>&1 || :
    /sbin/chkconfig --del %{name}
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service %{name} condrestart > /dev/null 2>&1 || :
fi

%endif

%files
%{_sbindir}/globus-gatekeeper
%{_sbindir}/globus-k5
%if %{use_systemd}
%{_unitdir}/%{name}.service
%else
%{_initddir}/%{name}
%endif
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_sysconfdir}/grid-services
%dir %{_sysconfdir}/grid-services/available
%doc %{_mandir}/man8/globus-gatekeeper.8*
%doc %{_mandir}/man8/globus-k5.8*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%doc %{_pkgdocdir}/README.Fedora
%license GLOBUS_LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 11.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 25 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 11.4-1
- New GCT release v6.2.20220524
- Drop patches included in the release

* Sat Mar 12 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 11.3-11
- Fix some compiler warnings

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 11.3-9
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 11.3-7
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 11.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 11.3-5
- Specfile updates
- Replace /var/run with /run in systemd unit file
- Add logrotate dependency (fixes rpmlint error)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 11.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 11.3-1
- Remove obsolete acconfig.h file (11.1)
- Add AC_CONFIG_MACRO_DIR and ACLOCAL_AMFLAGS (11.3)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 11.0-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release
  - Fix make clean rule

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.12-3
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir and _initddir macro definitions
  - Don't clear the buildroot in the install section
  - Remove the clean section
  - Drop the globus-gatekeeper-openssl098.patch

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.12-1
- GT6 update: Updated man pages

* Thu Oct 13 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.11-2
- Rebuild for openssl 1.1.0 (Fedora 26)

* Fri Sep 02 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.11-1
- GT6 update

* Sun Aug 14 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 10.10-4
- Convert to systemd unit file (Fedora 25+)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 10.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 08 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.10-1
- GT6 update

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.9-2
- Implement updated license packaging guidelines

* Thu Nov 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.9-1
- GT6 update

* Sun Oct 26 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.8-1
- GT6 update

* Fri Sep 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 10.7-1
- Update to Globus Toolkit 6.0
- Drop GPT build system and GPT packaging metadata
- Activate hardening flags

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Brent Baude <baude@us.ibm.com> - 9.15-2
- Replace arch def of ppc64 with power64 macro for ppc64le enablement

* Thu Nov 07 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.15-1
- Update to Globus Toolkit 5.2.5
- Drop patch globus-gatekeeper-ac.patch (fixed upstream)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.14-5
- Implement updated packaging guidelines

* Tue May 21 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.14-4
- Add aarch64 to the list of 64 bit platforms
- Don't use AM_CONFIG_HEADER (automake 1.13)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 06 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.14-2
- Specfile clean-up

* Sun Jul 22 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.14-1
- Update to Globus Toolkit 5.2.2
- Drop patch globus-gatekeeper-porting.patch (fixed upstream)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Apr 28 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.11-1
- Update to Globus Toolkit 5.2.1
- Drop patch globus-gatekeeper-deps.patch (fixed upstream)

* Thu Feb 02 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.6-3
- Fix start-up script

* Wed Jan 18 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.6-2
- Portability fixes
- Fix broken links in README file

* Thu Dec 15 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 9.6-1
- Update to Globus Toolkit 5.2.0

* Mon Apr 25 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.7-4
- Add README file

* Tue Apr 19 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.7-3
- Add start-up script and README.Fedora file

* Mon Feb 28 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.7-2
- Fix typos in the setup patch

* Thu Feb 24 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.7-1
- Update to Globus Toolkit 5.0.3

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 17 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.5-2
- Simplify directory ownership

* Wed Apr 14 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.5-1
- Update to Globus Toolkit 5.0.1

* Sat Jan 23 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.3-1
- Update to Globus Toolkit 5.0.0

* Wed Jul 29 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.0-1
- Autogenerated
