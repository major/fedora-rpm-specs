%if %{?fedora}%{!?fedora:0} >= 25 || %{?rhel}%{!?rhel:0} >= 8
%global use_systemd 1
%else
%global use_systemd 0
%endif

%if %{?fedora}%{!?fedora:0} >= 36 || %{?rhel}%{!?rhel:0} >= 9
%global use_mdb 1
%else
%global use_mdb 0
%endif

Name:		bdii
Version:	6.0.3
Release:	3%{?dist}
Summary:	The Berkeley Database Information Index (BDII)

License:	Apache-2.0
URL:		https://github.com/EGI-Federation/bdii
Source:		%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	make
BuildRequires:	python3-devel
%if %{use_systemd}
BuildRequires:	systemd-rpm-macros
%endif

Requires:	openldap-clients
Requires:	openldap-servers
Requires:	glue-schema >= 2.0.10
Requires:	logrotate

Requires(post):		/usr/bin/mkpasswd
%if %{use_systemd}
%{?systemd_requires}
%else
Requires(post):		chkconfig
Requires(preun):	chkconfig
Requires(preun):	initscripts
Requires(postun):	initscripts
%endif

%if %{?fedora}%{!?fedora:0} >= 23 || %{?rhel}%{!?rhel:0} >= 8
Requires(post):		policycoreutils-python-utils
Requires(postun):	policycoreutils-python-utils
%else
Requires(post):		policycoreutils-python
Requires(postun):	policycoreutils-python
%endif

%description
The Berkeley Database Information Index (BDII) consists of a standard
LDAP database which is updated by an external process. The update process
obtains LDIF from a number of sources and merges them. It then compares
this to the contents of the database and creates an LDIF file of the
differences. This is then used to update the database.

%prep
%setup -q
%if %{use_mdb}
# Use mdb on recent systems
patch -p1 -f < 0001-Use-mdb-slapd-backend.patch
%endif

%build

%install
make install prefix=%{buildroot}

# Don't use /usr/bin/env shebang
sed 's!%{_bindir}/env .*!%{__python3}!' -i %{buildroot}%{_sbindir}/bdii-update

%if %{use_systemd}
rm %{buildroot}%{_initrddir}/%{name}
mkdir -p %{buildroot}%{_unitdir}
install -m 644 -p etc/systemd/bdii.service etc/systemd/bdii-slapd.service %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p etc/systemd/bdii-slapd-start %{buildroot}%{_datadir}/%{name}
%endif

rm -rf %{buildroot}%{_docdir}/%{name}

%if %{use_systemd}
%pre
# Remove old init config when systemd is used
/sbin/chkconfig --del %{name} >/dev/null 2>&1 || :
%endif

%post
sed "s/\(rootpw *\)secret/\1$(mkpasswd -s 0 | tr '/' 'x')/" \
    -i %{_sysconfdir}/%{name}/bdii-slapd.conf \
       %{_sysconfdir}/%{name}/bdii-top-slapd.conf

%if %{use_systemd}
%systemd_post %{name}.service
%else
/sbin/chkconfig --add %{name}
%endif

semanage port -a -t ldap_port_t -p tcp 2170 2>/dev/null || :
semanage fcontext -a -t slapd_db_t "%{_localstatedir}/lib/%{name}/db(/.*)?" 2>/dev/null || :
semanage fcontext -a -t slapd_var_run_t "%{_localstatedir}/run/%{name}/db(/.*)?" 2>/dev/null || :
# Remove selinux labels for old bdii var dir
semanage fcontext -d -t slapd_db_t "%{_localstatedir}/run/%{name}(/.*)?" 2>/dev/null || :

%preun
%if %{use_systemd}
%systemd_preun %{name}.service
%else
if [ $1 -eq 0 ]; then
  service %{name} stop > /dev/null 2>&1
  /sbin/chkconfig --del %{name}
fi
%endif

%postun
%if %{use_systemd}
%systemd_postun_with_restart %{name}.service
%else
if [ $1 -ge 1 ]; then
  service %{name} condrestart > /dev/null 2>&1
fi
%endif

if [ $1 -eq 0 ]; then
  semanage port -d -t ldap_port_t -p tcp 2170 2>/dev/null || :
  semanage fcontext -d -t slapd_db_t "%{_localstatedir}/lib/%{name}/db(/.*)?" 2>/dev/null || :
  semanage fcontext -d -t slapd_var_run_t "%{_localstatedir}/run/%{name}/db(/.*)?" 2>/dev/null || :
fi

%files
%attr(-,ldap,ldap) %{_localstatedir}/lib/%{name}
%attr(-,ldap,ldap) %{_localstatedir}/log/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/DB_CONFIG
%config(noreplace) %{_sysconfdir}/%{name}/DB_CONFIG_top
%config(noreplace) %{_sysconfdir}/%{name}/bdii.conf
%config(noreplace) %{_sysconfdir}/%{name}/BDII.schema
%attr(-,ldap,ldap) %config %{_sysconfdir}/%{name}/bdii-slapd.conf
%attr(-,ldap,ldap) %config %{_sysconfdir}/%{name}/bdii-top-slapd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%if %{use_systemd}
%{_unitdir}/bdii.service
%{_unitdir}/bdii-slapd.service
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/bdii-slapd-start
%else
%{_initrddir}/%{name}
%endif
%{_sbindir}/bdii-update
%{_mandir}/man1/bdii-update.1*
%doc AUTHORS.md README.md
%license COPYRIGHT LICENSE.txt

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 28 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.0.3-1
- Version 6.0.3

* Mon Jun 17 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.0.2-1
- Version 6.0.2

* Thu May 16 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.0.1-1
- Version 6.0.1
- Backport fix for IPv6 support from upstream

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.0.0-1
- Version 6.0.0
- Drop previously backported patches
- Use python3 also for EPEL 7 (following upstream)
- Use systemd unit files from upstream

* Sun Dec 04 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.26-10
- Use mdb slapd backend (Fedors 36+, EPEL 9+)

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.26-8
- Update python3 patch with changes from upstream
- Update default paths (/var/run → /run, /var/lock → /run/lock)
- Update URL and Source tags

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 5.2.26-5
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.26-3
- Revert use of python3 for EPEL 7

* Wed Jan 06 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.26-2
- Use python3 also for EPEL 7 (following upstream)

* Tue Dec 01 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.26-1
- Version 5.2.26
- Update python3 patch
- Update systemd unit files

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 19 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.25-5
- Python 3 support (from upstream pull request)
- Use Python 3 for Fedora 31+ and EPEL 8+

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.25-3
- Use /usr/bin/mkpasswd instead of expect as Requires
  (mkpasswd is no longer provided by the expect rpm in Fedora 30+)

* Tue Apr 09 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.25-2
- Define __python2 if undefined

* Tue Apr 09 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.25-1
- Version 5.2.25
- Upstream project moved to github

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.23-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.23-11
- Don't use /usr/bin/python shebang
- Remove EPEL 5 conditionals

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.2.23-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 15 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.2.23-5
- Convert to systemd unit files (Fedora 25+)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jul 26 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.2.23-3
- Adapt to new policycoreutils packaging (Fedora 23+)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.2.23-1
- New upstream version 5.2.23

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 09 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.2.22-1
- New upstream version 5.2.22
- Do not hardcode run directory

* Tue Aug 13 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.2.21-1
- New upstream version 5.2.21

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.2.20-1
- New upstream version 5.2.20

* Thu Mar 14 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.2.17-2
- Don't use _libdir macro for noarch package

* Thu Mar 14 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.2.17-1
- New upstream version 5.2.17

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 15 2012 Laurence Field <Laurence.Field@cern.ch> - 5.2.13-1
- Included Fedora patches upstream.

* Fri Jul 20 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 5.2.12-1
- Fixed BDII_IPV6_SUPPORT after testing

* Wed Jul 18 2012 Maria Alandes <maria.alandes.pradillo@cern.ch> - 5.2.11-1
- BUG 95122: Created SLAPD_DB_DIR directoy with correct ownership if it doesn't exist
- BUG 95839: Added BDII_IPV6_SUPPORT

* Thu Mar 08 2012 Laurence Field <laurence.field@cern.ch> - 5.2.10-1
- New upstream version that includes a new DB_CONFIG

* Wed Feb 08 2012 Laurence Field <laurence.field@cern.ch> - 5.2.9-1
- Fixed /var/run packaging issue

* Wed Feb 08 2012 Laurence Field <laurence.field@cern.ch> - 5.2.8-1
- Fixed a base64 encoding issue and added /var/run/bdii to the package

* Tue Feb 07 2012 Laurence Field <laurence.field@cern.ch> - 5.2.7-1
- Performance improvements to reduce memory and disk usage

* Wed Jan 25 2012 Laurence Field <laurence.field@cern.ch> - 5.2.6-1
- New upstream version that includes fedora patches and fix for EGI RT 3235

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 04 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.2.5-1
- New upstream version 5.2.5

* Tue Jul 26 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.2.4-1
- New upstream version 5.2.4
- Drop patch accepted upstream: bdii-mdsvo.patch
- Move large files away from /var/run in order not to fill up /run partition

* Mon Jun 27 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.2.3-2
- Revert upstream hack that breaks ARC infosys

* Mon Jun 13 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.2.3-1
- New upstream version 5.2.3
- Drop patches accepted upstream: bdii-runuser.patch, bdii-context.patch,
  bdii-default.patch, bdii-shadowerr.patch, bdii-sysconfig.patch

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 01 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.1.13-1
- New upstream version 5.1.13
- Move restorecon from post sctiptlet to startup script in order to support
  /var/run on tmpfs

* Thu Sep 23 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.1.9-1
- New upstream version 5.1.9

* Thu Sep 02 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.1.8-1
- New upstream version 5.1.8

* Fri Jun 18 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.1.7-1
- New upstream version 5.1.7

* Sun May 23 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.1.5-1
- New upstream release 5.1.5
- Get rid of lsb initscript dependency

* Mon Apr 05 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.1.0-1
- New upstream verison 5.1.0
- Add SELinux context management to scriptlets

* Thu Mar 25 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.0.8-4.460
- Update (svn revision 460)
- Use proper anonymous svn checkout instead of svnweb generated tarball

* Fri Feb 26 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.0.8-3.443
- Update (svn revision 443)

* Wed Feb 24 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.0.8-2.436
- Update (svn revision 436)

* Mon Feb 08 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 5.0.8-1.375
- Initial package (svn revision 375)
