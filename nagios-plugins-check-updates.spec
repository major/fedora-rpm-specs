%define plugin check_updates
%define nagiospluginsdir %{_libdir}/nagios/plugins

# No binaries in this package
%define debug_package %{nil}

Name:          nagios-plugins-check-updates
Version:       1.8.5
Release:       2%{?dist}
Summary:       A Nagios plugin to check if Red Hat or Fedora system is up-to-date

License:       GPL-3.0-or-later
URL:           https://github.com/matteocorti/check_updates
Source:        https://github.com/matteocorti/check_updates/releases/download/v%{version}/check_updates-%{version}.tar.gz


BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl(Carp)
BuildRequires: perl(English)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(lib)
BuildRequires: perl(Module::Install)
BuildRequires: perl(Monitoring::Plugin)
BuildRequires: perl(Monitoring::Plugin::Getopt)
BuildRequires: perl(Monitoring::Plugin::Threshold)
BuildRequires: perl(POSIX)
BuildRequires: perl(Readonly)
BuildRequires: perl(strict)
BuildRequires: perl(Test::More)
BuildRequires: perl(vars)
BuildRequires: perl(warnings)

Requires:      nagios-plugins
Requires:      which
# Yum security plugin:
#   Fedora >= 19         : yum-plugin-security (is now provided by the yum package)
#   Fedora <= 18         : yum-plugin-security (yum-utils subpackage; also provides yum-security)
#   Red Hat Enterprise 6 : yum-plugin-security (yum-utils subpackage; also provides yum-security)
#   Red Hat Enterprise 5 : yum-security (yum-utils subpackage)
#   Red Hat Enterprise 8+:

%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?fedora} && 0%{?fedora} < 31)
Requires:      yum-plugin-security
%endif

Requires:      perl(Monitoring::Plugin)

Obsoletes:     check_updates < 1.4.11

%description
%{summary}.


%prep
%setup -q -n %{plugin}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor \
    INSTALLSCRIPT=%{nagiospluginsdir} \
    INSTALLVENDORSCRIPT=%{nagiospluginsdir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name "*.pod" -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} %{buildroot}/*

%check
make test


%files
%license COPYING COPYRIGHT
%doc AUTHORS Changes NEWS README.md
%{nagiospluginsdir}/*
%{_mandir}/man1/*.1*


%changelog
* Sat Sep 10 2022 Carl George <carl@george.computer> - 1.8.5-2
- Fix license handling

* Sat Jul 30 2022 Sean Mottles <seanmottles@posteo.net> - 1.8.5-1
- Update version to support AlmaLinux and Rocky Linux
- Skip the kernel checks if the kernel is not installed with RPM

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 02 2020 Martin Jackson <mhjacks@swbell.net> - 1.7.10-1
- new version

* Tue Mar 31 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.7.9-2
- Specify all perl dependencies for tests

* Thu Feb 27 2020 Martin Jackson <mhjacks@swbell.net> - 1.7.9-1
- Update to latest release, fix bz#1808156; remove bundled lib fixup

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Piotr Popieluch <piotr1212@gmail.com> - 1.7.8-2
- Remove bundled libraries

* Sat Jan 18 2020 Piotr Popieluch <piotr1212@gmail.com> - 1.7.8-1
- Update to 1.7.8
- Add version to Obsoletes:

* Mon Dec 2  2019 Martin Jackson <mhjacks@swbell.net> - 1.6.23-4
- Conditionalize yum Requires

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 29 2018 Piotr Popieluch <piotr1212@gmail.com> - 1.6.23-1
- Add Module::Install to BR to fix rhbz#1583366

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan  5 2017 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 1.6.19-1
- Update to 1.6.19.

* Sat Sep  3 2016 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 1.6.18-2
- Add missing requirement: perl(Monitoring::Plugin)

* Wed Jun  1 2016 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 1.6.18-1
- Update to 1.6.18.

* Sun May 29 2016 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 1.6.17-1
- Update to 1.6.17.

* Mon Apr 18 2016 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 1.6.16-1
- Update to 1.6.16.

* Sun Feb 07 2016 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 1.6.15-1
- Update to 1.6.15.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 28 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 1.6.12-2
- Upstream project moved to github
- Upstream is now using git instead of subversion
- Version 1.6.12 tarball in github has slightly different content

* Sat Sep 19 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 1.6.12-1
- Update to 1.6.12.
- Initial support for DNF.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Feb 16 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 1.6.10-1
- Update to 1.6.10.
- It now requires perl(Monitoring::Plugin).

* Tue Feb 10 2015 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 1.6.9-1
- Update to 1.6.9.
- No longer requires perl(Sort::Versions).
- Ship the version.pm file from check-updates 1.6.7 (temporary).

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 23 2014 Jose Pedro Oliveira <jose.p.oliveira.oss at gmail.com> - 1.6.7-1
- Update to 1.6.7.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 11 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.6-1
- Update to 1.6.6.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.5-1
- Update to 1.6.5.

* Wed Jun 19 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.4-1
- Update to 1.6.4.

* Sat May 25 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.3-2
- Fedora 19: yum-plugin-security is now provided by the yum package
  (and the yum-security virtual provide was dropped) (#967225).

* Wed May 15 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.3-1
- Update to 1.6.3.

* Sat Mar 30 2013 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.2-1
- Update to 1.6.2.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.1-1
- Update to 1.6.1.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.6.0-1
- Update to 1.6.0.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec  5 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.5.2-1
- Update to 1.5.2.

* Sat Dec  3 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.5.1-1
- Update to 1.5.1.

* Tue Oct  4 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.5.0-1
- Update to 1.5.0.

* Wed May 25 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.14-1
- Update to 1.4.14.

* Tue May 24 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.13-1
- Update to 1.4.13.
- Fixes a build problem in EPEL5 (test script failure).

* Tue May 24 2011 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.12-1
- Update to 1.4.12.
- Upstream added a test suite.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 18 2010 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.11-1
- Update to 1.4.11.

* Mon Nov  1 2010 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.9-1
- Update to 1.4.9 (solves the EPEL5 build problem).

* Sun Oct 31 2010 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.8-1
- Update to 1.4.8 (license clarification).

* Thu Feb 18 2010 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.7-1
- Update to 1.4.7.

* Thu Dec 10 2009 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4.6-1
- First build for Fedora and EPEL.

# vim:set ai ts=4 sw=4 sts=4 et:
