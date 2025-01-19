Name:           perl-HTML-FormHandler
Version:        0.40068
Release:        24%{?dist}
Summary:        HTML forms using Moose
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/HTML-FormHandler
Source0:        https://cpan.metacpan.org/authors/id/G/GS/GSHANK/HTML-FormHandler-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(aliased)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Load) >= 0.06
BuildRequires:  perl(Config::Any)
BuildRequires:  perl(Crypt::Blowfish)
BuildRequires:  perl(Crypt::CBC)
BuildRequires:  perl(Data::Clone)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Strptime)
BuildRequires:  perl(Email::Valid)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(HTML::TreeBuilder) >= 3.23
BuildRequires:  perl(JSON::MaybeXS) >= 1.003003
BuildRequires:  perl(List::AllUtils)
BuildRequires:  perl(Locale::Maketext) >= 1.09
BuildRequires:  perl(Moose) >= 2.0007
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Getopt) >= 0.16
BuildRequires:  perl(MooseX::Types) >= 0.20
BuildRequires:  perl(MooseX::Types::Common)
BuildRequires:  perl(MooseX::Types::LoadableClass) >= 0.006
BuildRequires:  perl(namespace::autoclean) >= 0.09
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Memory::Cycle) >= 1.04
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(utf8)
Requires:       perl(Class::Load) >= 0.06
Requires:       perl(Locale::Maketext) >= 1.09
Requires:       perl(Moose) >= 2.0007
Requires:       perl(MooseX::Getopt) >= 0.16
Requires:       perl(MooseX::Types) >= 0.20
Requires:       perl(MooseX::Types::Common)
Requires:       perl(MooseX::Types::LoadableClass) >= 0.006
Requires:       perl(namespace::autoclean) >= 0.09

# hidden from Pause
Provides:       perl(HTML::FormHandler::Meta::Role) = %{version}
Provides:       perl(HTML::FormHandler::Model::CDBI) = %{version}
Provides:       perl(HTML::FormHandler::Params) = %{version}
Provides:       perl(HTML::FormHandler::Field::Repeatable::Instance) = %{version}

%{?perl_default_filter}

%description
HTML::FormHandler is a form handling class that validates HTML form data and,
for database forms, saves it to the database on validation. It has field
classes that can be used for creating a set of widgets and highly automatic
templates. There are two simple rendering roles plus a set of widget roles for
individual form and field classes. FormHandler is designed to make it easy to
produce alternative rendering modules.

%prep
%setup -q -n HTML-FormHandler-%{version}

find lib -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README TODO
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/HTML*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.40068-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.40068-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.40068-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.40068-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.40068-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.40068-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.40068-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.40068-17
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.40068-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.40068-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.40068-14
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.40068-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40068-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.40068-11
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.40068-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40068-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.40068-8
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.40068-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 25 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.40068-6
- Add version to the package Provides

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40068-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.40068-4
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.40068-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.40068-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Emmanuel Seyman <emmanuel@seyman.fr> - 0.40068-1
- Update to 0.40068

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.40067-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.40067-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 23 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.40067-1
- Update to 0.40067

* Sat Jul 23 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.40066-1
- Update to 0.40066

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.40065-2
- Perl 5.24 rebuild

* Thu Mar 31 2016 Emmanuel Seyman <emmanuel@seyman.fr> - 0.40065-1
- Update to 0.40065

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.40064-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 18 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.40064-1
- Update to 0.40064

* Sun Jul 12 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.40063-1
- Update to 0.40063

* Sun Jun 28 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.40062-1
- Update to 0.40062

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40059-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.40059-2
- Perl 5.22 rebuild

* Sun Mar 01 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.40058-1
- Update to 0.40058
- Use %%license macro

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.40057-2
- Perl 5.20 rebuild

* Wed Aug 06 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.40057-1
- 0.40057 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40020-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Petr Pisar <ppisar@redhat.com> - 0.40020-4
- Fix compound/basic.t test by floating year (bug #1084050)

* Sun Aug 04 2013 Petr Pisar <ppisar@redhat.com> - 0.40020-3
- Perl 5.18 rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40020-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Iain Arnell <iarnell@gmail.com> 0.40020-1
- update to latest upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40013-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 29 2012 Iain Arnell <iarnell@gmail.com> 0.40013-1
- update to latest upstream version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.40011-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 22 2012 Petr Pisar <ppisar@redhat.com> - 0.40011-2
- Perl 5.16 rebuild

* Sat Jun 09 2012 Iain Arnell <iarnell@gmail.com> 0.40011-1
- update to latest upstream version

* Mon Feb 20 2012 Iain Arnell <iarnell@gmail.com> 0.36003-1
- update to latest upstream version

* Sat Feb 04 2012 Iain Arnell <iarnell@gmail.com> 0.36002-1
- update to latest upstream version

* Wed Jan 25 2012 Iain Arnell <iarnell@gmail.com> 0.36001-1
- update to latest upstream version

* Mon Jan 23 2012 Iain Arnell <iarnell@gmail.com> 0.36000-1
- update to latest upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Oct 22 2011 Iain Arnell <iarnell@gmail.com> 0.35005-1
- update to latest upstream version

* Sun Oct 02 2011 Iain Arnell <iarnell@gmail.com> 0.35003-2
- fix explicit provides - should be
  HTML::FormHandler::Field::Repeatable::Instance, not
  HTML::FormHandler::Field::Compound.

* Fri Sep 30 2011 Iain Arnell <iarnell@gmail.com> 0.35003-1
- Specfile autogenerated by cpanspec 1.78.
