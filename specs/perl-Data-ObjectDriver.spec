Name:           perl-Data-ObjectDriver
Version:        0.23
Release:        2%{?dist}
Summary:        Simple, transparent data interface, with caching
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-ObjectDriver
Source0:        https://cpan.metacpan.org/authors/id/S/SI/SIXAPART/Data-ObjectDriver-%{version}.tar.gz

BuildArch:      noarch
# Build requirements
BuildRequires:  perl-generators
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Module::Build::Tiny)
# Test requirements
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(version)
# Runtime requirements
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Class::Data::Inheritable)
BuildRequires:  perl(Class::Trigger)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)

%{?perl_default_filter}
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}%{perl_vendorlib}/Data/ObjectDriver/Driver/DBD/Oracle.pm

%description
Data::ObjectDriver is an object relational mapper, meaning that it maps object-
oriented design concepts onto a relational database.

%prep
%setup -q -n Data-ObjectDriver-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}

%check
./Build test


%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 27 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 0.23-1
- Update to 0.23

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 0.22-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 05 2023 Emmanuel Seyman <emmanuel@seyman.fr> - 0.22-1
- Update to 0.22

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.21-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 01 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.21-1
- Update to 0.21

* Mon Sep 14 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.20-1
- Update to 0.20

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-2
- Perl 5.32 rebuild

* Sun Mar 08 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.19-1
- Update to 0.19
- Use /usr/bin/perl instead of %%{__perl}
- Use %%license tag

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.18-1
- Update to 0.18

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.17-2
- Perl 5.30 rebuild

* Sun Mar 17 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.17-1
- Update to 0.17

* Sun Mar 10 2019 Emmanuel Seyman <emmanuel@seyman.fr> - 0.16-1
- Update to 0.16

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.15-2
- Perl 5.26 rebuild

* Sun Apr 23 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.15-1
- Update to 0.15

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.14-1
- Update to 0.14, compatible with sqlite 3.10 (#1298821)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-2
- Perl 5.22 rebuild

* Sun May 24 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.13-1
- Update to 0.13

* Sun Apr 12 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.11-1
- Update to 0.11
- Switch to Minilla as a build-system

* Sun Jan 18 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.10-1
- Update to 0.10
- Drop upstreamed patch

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.09-13
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 23 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.09-11
- Add patch and bump EVR to rebuild

* Sun Mar 23 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 0.09-10
- Patch Data-ObjectDriver to handle the new sqlite error return format
- Fix incorrect dates in changelog

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 24 2013 Petr Pisar <ppisar@redhat.com> - 0.09-8
- Perl 5.18 rebuild
- Remove bundled Test::Builder (CPAN RT#87294)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 17 2012 Petr Pisar <ppisar@redhat.com> - 0.09-5
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Iain Arnell <iarnell@gmail.com> 0.09-3
- update filtering for rpm 4.9
- clean up spec for modern rpmbuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.09-2
- Perl mass rebuild

* Sun May 08 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.09-1
- Update to 0.09

* Sun Feb 13 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.08-3
- Add perl default filter
- Filter the Oracle stuff

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 07 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.08-1
- Update to 0.08

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.07-2
- Mass rebuild with perl-5.12.0

* Tue Mar 30 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 0.07-1
- Update to 0.07, dropping upstreamed patch

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.06-5
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 16 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.06-3
- Re-enable auto-Requires, for real this time
- Add DBD::SQLite to the BuildRequires
- Patch t/02-basic.t to pass on sqlite 3.5.9

* Wed Apr 15 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.06-2
- Re-enable auto-Requires
- Exclude DBD::Oracle from them

* Sat Apr 11 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.06-1
- Use Module::Install calls rather than ./Build.PL ones
- run tests in the check section
- clean up Requires
- Update to 0.06

* Mon Dec 29 2008 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 0.05-1
- Specfile autogenerated by cpanspec 1.77.
