Name:		glue-schema
Version:	2.1.0
Release:	6%{?dist}
Summary:	LDAP schema files for the GLUE 1.3 and GLUE 2.0 Schema
License:	Apache-2.0
URL:		https://github.com/EGI-Foundation/%{name}
Source:		https://github.com/EGI-Foundation/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make

%description
The GLUE specification is an information model for Grid entities such
as computing clusters and data storage facilities. As a conceptual
model, it is designed to be independent from the concrete data models
adopted for its implementation. The specification can be rendered to
several concrete data models such as XML Schema, LDAP Schema or SQL.

This package provides LDAP schema files for the GLUE 1.3 and GLUE 2.0 Schema.

%prep
%setup -q

%build 
# Nothing to build

%install
make install prefix=%{buildroot}

rm -rf %{buildroot}%{_docdir}
rm -rf %{buildroot}%{_licensedir}

%files
%dir %{_sysconfdir}/ldap
%dir %{_sysconfdir}/ldap/schema
%config(noreplace) %{_sysconfdir}/ldap/schema/*
%doc AUTHORS.md
%doc README.md
%license COPYRIGHT
%license LICENSE.txt

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.1.0-1
- Update to release 2.1.0
- Update License tag to SPDX standard

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 18 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.0.11-16
- New upstream location on github
- Drop doc sub-package

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.11-1
- Update to release 2.0.11

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 14 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.10-1
- Update to release 2.0.10

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 04 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.8-1
- Update to release 2.0.8

* Tue Aug 30 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.7-1
- Update to release 2.0.7

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 18 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.6-1
- Update to release 2.0.6
- Change license tag to ASL 2.0 to reflect upstream license change

* Thu Apr 08 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.4-2
- Add missing Group tag in doc subpackage

* Sun Apr 04 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.4-1
- Update to release 2.0.4
- Create doc subpackage containing the GLUE schema specification

* Thu Mar 25 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.3-3.448
- Use proper anonymous svn checkout instead of svnweb generated tarball

* Fri Feb 26 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.3-2.448
- Update (svn revision 448)

* Fri Feb 12 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.3-1
- Updated packaging

* Fri Jul 10 2009 Laurence Field <laurence.field@cern.ch> -  2.0.1-1
- First release
