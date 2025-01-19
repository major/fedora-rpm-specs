Name:           perl-Catalyst-View-TT
Summary:        Template Toolkit View Class
Version:        0.46
Release:        8%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Catalyst-View-TT-%{version}.tar.gz
URL:            https://metacpan.org/release/Catalyst-View-TT
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl(Catalyst) >= 5.70000
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Timer)
BuildRequires:  perl(Template::Provider::Encoding)
BuildRequires:  perl(Test::More)

Requires:       perl(Catalyst) >= 5.70000

%{?perl_default_filter}

%description
This is the Catalyst view base class for the Template Toolkit.

%prep
%setup -q -n Catalyst-View-TT-%{version}

find . -type f -exec chmod -x -c {} +

# silence rpmlint warnings
sed -i 's/\r//' t/lib/TestApp/Template/Any.pm

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README t/
%{perl_vendorlib}/Catalyst*
%{_mandir}/man3/Catalyst*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 0.46-7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Aug 14 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 0.46-1
- Update to 0.46
- Replace %%{__perl} with /usr/bin/perl

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.45-7
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.45-4
- Perl 5.34 rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 26 2020 Emmanuel Seyman <emmanuel@seyman.fr> - 0.45-1
- Update to 0.45
- Pass NO_PERLLOCAL=1 to Makefile.PL
- Use %%{make_install} instead of "make pure_install"
- Use %%{make_build} instead of make

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-14
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.44-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 09 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.44-1
- Update to 0.44

* Sun Aug 16 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.43-1
- Update to 0.43
- Do not generate the .packlist file

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.42-2
- Perl 5.22 rebuild

* Thu Jan 01 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.42-1
- Update to 0.42
- Tighten file listing
- Drop tests subpackage

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.41-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Petr Pisar <ppisar@redhat.com> - 0.41-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 01 2013 Iain Arnell <iarnell@gmail.com> 0.41-1
- update to latest upstream version

* Fri Feb 15 2013 Iain Arnell <iarnell@gmail.com> 0.40-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.39-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 0.39-2
- Perl 5.16 rebuild

* Sat May 12 2012 Iain Arnell <iarnell@gmail.com> 0.39-1
- update to latest upstream version

* Sat Feb 18 2012 Iain Arnell <iarnell@gmail.com> 0.38-1
- update to latest upstream version
- fix required Catalyst version
- drop unnecessary explicit requires

* Sun Jan 22 2012 Iain Arnell <iarnell@gmail.com> 0.37-3
- drop tests subpackage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 01 2011 Iain Arnell <iarnell@gmail.com> 0.37-1
- update to latest upstream version

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.36-2
- Perl mass rebuild

* Sun Mar 13 2011 Iain Arnell <iarnell@gmail.com> 0.36-1
- update to latest upstream version
- clean up spec for modern rpmbuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.34-2
- 661697 rebuild for fixing problems with vendorach/lib

* Sat Jul 17 2010 Iain Arnell <iarnell@gmail.com> 0.34-1
- update to latest upstream version
- BR perl(Template::Provider::Encoding)

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.32-2
- Mass rebuild with perl-5.12.0

* Sat Feb 20 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.32-1
- update by Fedora::App::MaintainerTools 0.003
- PERL_INSTALL_ROOT => DESTDIR
- dropped old BR on perl(Test::Pod)
- dropped old BR on perl(Test::Pod::Coverage)
- dropped old requires on perl(warnings)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.31-2
- rebuild against perl 5.10.1

* Sun Dec 06 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.31-1
- auto-update to 0.31 (by cpan-spec-update 0.01)

* Sat Sep 26 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.30-1
- update filtering
- auto-update to 0.30 (by cpan-spec-update 0.01)
- altered br on perl(Catalyst) (5.5 => 5.7)
- added a new br on perl(Class::Accessor) (version 0)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- added a new br on CPAN (inc::Module::AutoInstall found)
- altered req on perl(Catalyst) (0 => 5.7)
- added a new req on perl(Class::Accessor) (version 0)
- added a new req on perl(MRO::Compat) (version 0)
- added a new req on perl(Template) (version 0)
- added a new req on perl(Template::Timer) (version 0)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Feb 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.29-1
- update to 0.29

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 28 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.27-1
- update to 0.27

* Wed Mar 19 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.26-2
- bump

* Mon Mar 17 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.26-1
- Specfile autogenerated by cpanspec 1.74.
