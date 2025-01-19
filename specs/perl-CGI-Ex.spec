Name:           perl-CGI-Ex
Version:        2.55
Release:        5%{?dist}
Summary:        CGI utility suite - makes powerful application writing fun and easy
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/CGI-Ex
Source0:        https://cpan.metacpan.org/authors/id/R/RH/RHANDOM/CGI-Ex-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(CGI)
BuildRequires:  perl(Config::IniHash)
BuildRequires:  perl(Crypt::Blowfish)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Taint::Runtime)
BuildRequires:  perl(Template::Alloy) >= 1.016
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Tie::Handle)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML)

%{?perl_default_filter}

%description
CGI::Ex provides a suite of utilities to make writing CGI scripts more
enjoyable. Although they can all be used separately, the main functionality
of each of the modules is best represented in the CGI::Ex::App module.
CGI::Ex::App takes CGI application building to the next step. CGI::Ex::App
is not quite a framework (which normally includes pre-built HTML) instead
CGI::Ex::App is an extended application flow that dramatically reduces CGI
build time in most cases. It does so using as little magic as possible. See
CGI::Ex::App.

%prep
%setup -q -n CGI-Ex-%{version}

# make rpmlint happy :)
find samples/ -type f -exec chmod -c -x {} \;
rm -f samples/app/app1/INSTALL
/usr/bin/perl -pi -e 's|^#!perl|#!/usr/bin/perl|' t/1_validate_14_untaint.t

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}

%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README samples/ t/
%license LICENSE
%{perl_vendorlib}/CGI*
%{_mandir}/man3/CGI*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.55-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.55-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.55-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 14 2024 Emmanuel Seyman <emmanuel@seyman.fr> - 2.55-1
- Update to 2.55
- Migrate to SPDX license

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.54-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.54-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.54-2
- Perl 5.36 rebuild

* Sun Mar 13 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 2.54-1
- Update to 2.54

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.50-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.50-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.50-4
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.50-1
- Update to 2.50

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.49-4
- Perl 5.32 rebuild

* Tue Mar 24 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.49-3
- Add perl(blib) for tests

* Sun Mar 08 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.49-2
- Use correct Source URL

* Sun Mar 08 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 2.49-1
- Update to 2.49
- Use /usr/bin/perl instead of %%{__perl}
- Use %%{make_install} instead of "make pure_install"
- Use %%{make_build} instead of make
- Use %%license tag

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.48-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.48-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.48-1
- Update to 2.48

* Sun Aug 19 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.47-1
- Update to 2.47

* Sun Jul 29 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.46-1
- Update to 2.46

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.45-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jul 28 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 2.45-1
- Update to 2.45
- Drop upstreamed patches

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.44-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.44-6
- Perl 5.26 rebuild

* Thu May 25 2017 Petr Pisar <ppisar@redhat.com> - 2.44-5
- Restore compatibility with Perl 5.26.0 (CPAN RT#121889)
- Adapt to changes in JSON-2.93 (CPAN RT#121893)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.44-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.44-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 09 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 2.44-1
- Update to 2.44

* Fri Oct 02 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 2.43-1
- Updaye to 2.43

* Tue Aug 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.42-4
- Specify all dependencies

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.42-2
- Perl 5.22 rebuild

* Sun Feb 15 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 2.42-1
- Update to 2.42
- Drop Group tag
- Tighten file listing
- Spec file cleanup

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.38-7
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.38-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.38-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 2.38-2
- Perl 5.16 rebuild

* Sat Mar 03 2012 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 2.38-1
- Update to 2.38
- Clean up spec file
- Add perl default filter

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jul 20 2011 Petr Sabata <contyk@redhat.com> - 2.32-4
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.32-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sun Aug 08 2010 Iain Arnell <iarnell@gmail.com> 2.32-1
- update to latest upstream version

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.27-4
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.27-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 02 2009 Chris Weyl <cweyl@alumni.drew.edu> 2.27-1
- update to 2.27

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 26 2008 Chris Weyl <cweyl@alumni.drew.edu> 2.24-1
- update to 2.24

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.21-2
- rebuild for new perl

* Mon Nov 05 2007 Chris Weyl <cweyl@alumni.drew.edu> 2.21-1
- update to 2.21
- license tag: GPL -> GPL+

* Thu May 31 2007 Chris Weyl <cweyl@alumni.drew.edu> 2.13-1
- update to 2.13

* Sun May 13 2007 Chris Weyl <cweyl@alumni.drew.edu> 2.12-1
- update to 2.12

* Wed May 09 2007 Chris Weyl <cweyl@alumni.drew.edu> 2.11-1
- update to 2.11
- add split br's

* Mon Apr 30 2007 Chris Weyl <cweyl@alumni.drew.edu> 2.10-2
- bump

* Sat Apr 28 2007 Chris Weyl <cweyl@alumni.drew.edu> 2.10-1
- add perl(Hash::Case) as a BR
- update to 2.10

* Wed Apr 18 2007 Chris Weyl <cweyl@alumni.drew.edu> 2.09-2
- add additional BR's

* Sat Apr 07 2007 Chris Weyl <cweyl@alumni.drew.edu> 2.09-1
- Specfile autogenerated by cpanspec 1.70.
