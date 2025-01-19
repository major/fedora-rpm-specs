Name:           perl-BZ-Client
Version:        4.4004
Release:        15%{?dist}
Summary:        A client for the Bugzilla web services API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/BZ-Client
Source0:        https://cpan.metacpan.org/authors/id/D/DJ/DJZORT/BZ-Client-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTTP::CookieJar)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(URI)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl(XML::Writer)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# testing requirements
BuildRequires:  perl(Clone)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(English)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(Text::Password::Pronounceable)
BuildRequires:  perl(lib)
BuildRequires:  perl(utf8)

%{?perl_default_filter}

%description
This module provides an interface to the Bugzilla web services API.

%prep
%setup -q -n BZ-Client-%{version}
chmod 644 Changes README LICENSE

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/BZ*
%{_mandir}/man3/BZ*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.4004-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4004-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 4.4004-13
- Remove not-needed BuildRequires (#2260475)
- Fix SPDX notation (#2260475)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4004-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4004-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4004-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 4.4004-9
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4004-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4004-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.4004-6
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4004-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.4004-3
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.4004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Gwyn Ciesla <gwync@protonmail.com> - 4.4004-1
- 4.4004

* Sun Sep 27 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 4.4003-1
- Update to 4.4003

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4002-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.4002-10
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.4002-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4002-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.4002-7
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.4002-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.4002-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.4002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.4002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 4.4002-1
- Update to 4.4002

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.4001-2
- Perl 5.26 rebuild

* Mon Feb 06 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 4.4001-1
- Update to 4.4001
- Drop upstreamed patch

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.072-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.072-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 18 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.072-1
- Update to 1.072

* Wed Sep 09 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.071-1
- Update to 1.071

* Sun Sep 06 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.070-1
- Update to 1.07
- Use %%license tag

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.061-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.061-2
- Perl 5.22 rebuild

* Sat Apr 25 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.061-1
- Update to 1.061

* Sun Apr 19 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.06-2
- Use correct upstream URL

* Sun Apr 19 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 1.06-1
- Update to 1.06
- Drop patch0 (upstreamed)
- Update patch1

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.04-12
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Petr Pisar <ppisar@redhat.com> - 1.04-10
- Fix test to expect random hash keys (bug #1084032)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Aug 01 2013 Petr Pisar <ppisar@redhat.com> - 1.04-8
- Perl 5.18 rebuild

* Mon Apr 01 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1.04-7
- Bump to rebuild

* Mon Apr 01 2013 Emmanuel Seyman <emmanuel@seyman.fr> - 1.04-6
- Include patch to handle bugzilla dates (#927999)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 1.04-3
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 24 2011 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.04-1
- Update to 1.04
- Clean up spec file
- Add perl default filter
- Add perl(DateTime) to the BuildRequires
- Add perl(DateTime::Format::ISO8601) to the BuildRequires

* Thu Jul 21 2011 Petr Sabata <contyk@redhat.com> - 1.03-6
- Perl mass rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 1.03-5
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.03-3
- 661697 rebuild for fixing problems with vendorach/lib

* Thu Apr 29 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.03-2
- Mass rebuild with perl-5.12.0

* Fri Feb 05 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 1.03-1
- Update to 1.03
- Fix file permissons

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.02-2
- rebuild against perl 5.10.1

* Tue Aug 11 2009 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> 1.02-1
- Specfile autogenerated by cpanspec 1.78.
