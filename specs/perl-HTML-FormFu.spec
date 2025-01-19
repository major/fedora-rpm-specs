Name:           perl-HTML-FormFu
Version:        2.07
Release:        20%{?dist}
Summary:        HTML Form Creation, Rendering and Validation Framework
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-FormFu
Source0:        https://cpan.metacpan.org/authors/id/C/CF/CFRANKS/HTML-FormFu-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(CGI) >= 3.37
BuildRequires:  perl(CGI::Simple)
BuildRequires:  perl(Class::Accessor::Chained::Fast)
BuildRequires:  perl(Class::MOP::Method)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Config::Any) >= 0.18
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Visitor) >= 0.26
BuildRequires:  perl(Data::Visitor::Callback)
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(DateTime) >= 0.38
BuildRequires:  perl(DateTime::Format::Builder) >= 0.80
BuildRequires:  perl(DateTime::Format::Natural)
BuildRequires:  perl(DateTime::Format::Strptime) >= 1.20
BuildRequires:  perl(DateTime::Locale) >= 0.45
BuildRequires:  perl(Email::Valid)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Fatal)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Hash::Flatten)
BuildRequires:  perl(HTML::Scrubber)
BuildRequires:  perl(HTML::TokeParser::Simple) >= 3.14
BuildRequires:  perl(HTTP::Headers) >= 1.64
BuildRequires:  perl(IO::File)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Locale::Maketext)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Moose) >= 1.00
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(MooseX::Aliases)
BuildRequires:  perl(MooseX::Attribute::Chained) >= 1.0.1
BuildRequires:  perl(MooseX::SetOnce)
BuildRequires:  perl(Number::Format)
BuildRequires:  perl(Path::Class::File)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Regexp::Assemble)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(YAML::XS) >= 0.32
BuildRequires:  sed
Requires:       perl(Captcha::reCAPTCHA) >= 0.93
Requires:       perl(Class::Accessor::Chained::Fast)
Requires:       perl(Config::Any) >= 0.18
Requires:       perl(Crypt::DES)
Requires:       perl(Data::Visitor) >= 0.26
Requires:       perl(Date::Calc)
Requires:       perl(DateTime) >= 0.38
Requires:       perl(DateTime::Format::Builder) >= 0.80
Requires:       perl(HTML::TokeParser::Simple) >= 3.14
Requires:       perl(HTTP::Headers) >= 1.64
Requires:       perl(Locale::Maketext)
Requires:       perl(MooseX::Attribute::Chained) >= 1.0.1
Requires:       perl(Template)
Requires:       perl(YAML::XS) >= 0.32

%{?perl_default_filter:
%filter_from_provides /perl(unicode/d
%filter_from_requires /perl(Catalyst/d; /perl(default/d; /perl(model_config)/d;
%perl_default_filter
}

%description
HTML::FormFu is a HTML form framework which aims to be as easy as possible
to use for basic web forms, but with the power and flexibility to do
anything else you might want to do (as long as it involves forms).

%prep
%setup -q -n HTML-FormFu-%{version}

find examples -type f | xargs chmod 644
find examples -type f | xargs sed -i -e 's/\r//'

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT/blib

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README examples
%{perl_vendorlib}/*
%{_bindir}/*.pl
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 2.07-19
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-12
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-9
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-6
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.07-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 23 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.07-1
- Update to 2.07

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.06-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.06-2
- Perl 5.28 rebuild

* Wed Apr 11 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 2.06-1
- Update to 2.06

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.05-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 09 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 2.05-1
- Update to 2.05
- Remove hacks and patchs related to Test::Aggregate (no longer used)

* Wed Jun 29 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 2.03-1
- Update to 2.03
- Remove tests that do mxchecks (koji doesn't allow network access)
- Pass NO_PACKLIST to Makefile.PL

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-8
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.01-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 02 2015 Petr Pisar <ppisar@redhat.com> - 2.01-6
- Do not use Test::Aggregate::Nested for tests because it's not available
  anymore (bug #1231204)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-4
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.01-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jun 01 2014 Emmanuel Seyman <emmanuel@seyman.fr> - 2.01-1
- Update to 2.01

* Fri Jan 03 2014 Iain Arnell <iarnell@gmail.com> 1.00-1
- update to latest upstream version

* Wed Aug 07 2013 Petr Pisar <ppisar@redhat.com> - 0.09010-4
- Locale::Maketext is needed at run-time

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.09010-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 11 2012 Iain Arnell <iarnell@gmail.com> 0.09010-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.09007-2
- Perl 5.16 rebuild

* Fri Feb 03 2012 Iain Arnell <iarnell@gmail.com> 0.09007-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.09005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 23 2011 Iain Arnell <iarnell@gmail.com> 0.09005-1
- update to latest upstream version

* Sun Aug 28 2011 Iain Arnell <iarnell@gmail.com> 0.09004-1
- update to latest upstream version

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.09003-2
- Perl mass rebuild

* Thu May 12 2011 Iain Arnell <iarnell@gmail.com> 0.09003-1
- update to latest upstream version

* Sat Apr 09 2011 Iain Arnell <iarnell@gmail.com> 0.09002-1
- update to latest upstream version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.08002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Sep 25 2010 Iain Arnell <iarnell@gmail.com> 0.08002-1
- update to latest upstream
- clean up spec for modern rpmbuild

* Tue Sep 07 2010 Iain Arnell <iarnell@gmail.com> 0.07003-1
- update to latest upstream version
- bump Captcha::reCAPTCHA requirement to 0.93

* Fri Jun 25 2010 Iain Arnell <iarnell@gmail.com> 0.07002-1
- update to latest upstream
- bump DateTime::Format::Strptime and DateTime::Locale BRs

* Fri Jun 18 2010 Iain Arnell <iarnell@gmail.com> 0.07001-3
- bump for build against perl-5.12

* Fri Jun 18 2010 Iain Arnell <iarnell@gmail.com> 0.07001-2
- doesn't BR perl(Regexp::Copy) any more

* Mon May 17 2010 Iain Arnell <iarnell@gmail.com> 0.07001-1
- update to latest upstream version
- re-enable tests
- tweak buildrequires

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.06001-2
- Mass rebuild with perl-5.12.0

* Mon Jan 11 2010 Iain Arnell <iarnell@gmail.com> 0.06001-1
- update to latest upstream version
- update requires

* Fri Dec 18 2009 Iain Arnell <iarnell@gmail.com> 0.05004-2
- fix silly typo in requires filtering

* Tue Dec 08 2009 Iain Arnell <iarnell@gmail.com> 0.05004-1
- update to latest upstream version
- use perl_default_filter

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.05001-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.05001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 07 2009 Iain Arnell <iarnell@gmail.com> 0.05001-1
- update to latest upstream version

* Wed May 27 2009 Iain Arnell <iarnell@gmail.com> 0.05000-1
- update to latest upstream
- R/BR Data::Visitor >= 0.23 to avoid Squirrel warnings

* Sun May 10 2009 Iain Arnell <iarnell@gmail.com> 0.04002-1
- update to latest upstream version

* Wed Apr 15 2009 Iain Arnell <iarnell@gmail.com> 0.04001-1
- update to latest upstream

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03007-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 08 2008 Iain Arnell <iarnell@gmail.com> 0.03007-1
- update to 030007

* Sat Dec 06 2008 Iain Arnell <iarnell@gmail.com> 0.03005-4
- remove wrongly detected requires (defaults and model_config)

* Sat Nov 29 2008 Iain Arnell <iarnell@gmail.com> 0.03005-3
- remove more unnecessary requires
- requires Exporter >= 5.57

* Sat Nov 29 2008 Iain Arnell <iarnell@gmail.com> 0.03005-2
- remove unnecessary explicit requires

* Wed Nov 26 2008 Iain Arnell <iarnell@gmail.com> 0.03005-1
- Specfile autogenerated by cpanspec 1.77.
