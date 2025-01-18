Name:		globus-gram-audit
%global _name %(tr - _ <<< %{name})
Version:	5.1
Release:	9%{?dist}
Summary:	Grid Community Toolkit - GRAM Jobmanager Auditing

License:	Apache-2.0
URL:		https://github.com/gridcf/gct/
Source:		https://repo.gridcf.org/gct6/sources/%{_name}-%{version}.tar.gz
Source8:	README
BuildArch:	noarch

BuildRequires:	make
BuildRequires:	perl-generators

Requires:	crontabs
Requires:	perl(DBD::SQLite)

Requires(post):	perl(DBD::SQLite)
Requires(post):	perl(Globus::Core::Paths)

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
GRAM Jobmanager Auditing

%prep
%setup -q -n %{_name}-%{version}

%build
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/globus \
	   --docdir=%{_pkgdocdir}

%make_build

%install
%make_install

# Rename cron script
mv %{buildroot}%{_sysconfdir}/cron.hourly/globus-gram-audit.cron \
   %{buildroot}%{_sysconfdir}/cron.hourly/globus-gram-audit

# Install README file
install -m 644 -p %{SOURCE8} %{buildroot}%{_pkgdocdir}/README

# Remove license file from pkgdocdir
rm %{buildroot}%{_pkgdocdir}/GLOBUS_LICENSE

%post
if [ $1 -eq 1 ]; then
    globus-gram-audit --query 'select 1 from gram_audit_table' 2> /dev/null || \
    globus-gram-audit --create --quiet || :
fi

%files
%{_sbindir}/globus-gram-audit
%dir %{_datadir}/globus
%dir %{_datadir}/globus/gram-audit
%{_datadir}/globus/gram-audit/*.sql
%dir %{_localstatedir}/lib/globus
%dir %{_localstatedir}/lib/globus/gram-audit
%config(noreplace) %{_sysconfdir}/cron.hourly/globus-gram-audit
%dir %{_sysconfdir}/globus
%config(noreplace) %{_sysconfdir}/globus/gram-audit.conf
%doc %{_mandir}/man8/globus-gram-audit.8*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%license GLOBUS_LICENSE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.1-1
- Typo fixes

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.0-6
- Specfile updates

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.0-1
- Switch upstream to Grid Community Toolkit
- First Grid Community Toolkit release
- Add Requires on perl(DBD::SQLite)
- Create database in post scriptlet

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.6-3
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Don't clear the buildroot in the install section
  - Remove the clean section

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 04 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.6-1
- GT6 update: Updated man pages

* Sat Sep 03 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 4.5-1
- GT6 update

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.4-2
- Implement updated license packaging guidelines

* Thu Nov 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.4-1
- GT6 update
- Drop patch globus-gram-audit-macro.patch (fixed upstream)

* Sun Oct 19 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.3-2
- Remove unexpanded configure macro

* Fri Sep 12 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 4.3-1
- Update to Globus Toolkit 6.0
- Drop GPT build system and GPT packaging metadata

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Dec 13 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.2-8
- Proper ownership of /etc/globus and /var/lib/globus

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.2-6
- Implement updated packaging guidelines

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 3.2-5
- Perl 5.18 rebuild

* Thu May 23 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.2-4
- Specfile clean-up

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 07 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.2-2
- Specfile clean-up

* Sun Jul 22 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.2-1
- Update to Globus Toolkit 5.2.2
- Drop patch globus-gram-audit-check.patch (fixed upstream)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 08 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.1-3
- Don't mark cron script as config file

* Tue Jan 24 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.1-2
- Rename cron script
- Fix broken links in README file

* Fri Dec 16 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 3.1-1
- Autogenerated
