Name:           perl-MooX-Options
Version:        4.103
Release:        23%{?dist}
Summary:        Explicit Options eXtension for Object Class
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooX-Options
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/MooX-Options-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Record)
BuildRequires:  perl(Getopt::Long) >= 2.43
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.099
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo) >= 1.003
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::ConfigFromFile::Role)
BuildRequires:  perl(MooX::Locale::Passthrough)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Class) >= 0.32
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strictures) >= 2
BuildRequires:  perl(Text::LineFold)
# Optional run-time:
BuildRequires:  perl(Term::Size::Any)
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Mo) >= 0.36
BuildRequires:  perl(Mo::coerce)
BuildRequires:  perl(Mo::default)
BuildRequires:  perl(Mo::required)
BuildRequires:  perl(Moose)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Role::Tiny::With)
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Test::Trap)
# Optional tests:
# English not used
BuildRequires:  perl(MooX::Cmd) >= 0.007
BuildRequires:  perl(MooX::Locale::TextDomain::OO)
BuildRequires:  perl(Locale::TextDomain::OO::Lexicon::Hash)
Requires:       perl(Data::Record)
Requires:       perl(JSON::MaybeXS)
Requires:       perl(Moo) >= 1.003
Requires:       perl(Moo::Role)
Requires:       perl(MooX::ConfigFromFile::Role)
Requires:       perl(MooX::Locale::TextDomain::OO)
Requires:       perl(MRO::Compat)
Requires:       perl(Path::Class) >= 0.32
Requires:       perl(Pod::Usage)
Requires:       perl(Regexp::Common)
Requires:       perl(Text::LineFold)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Getopt::Long::Descriptive|Moo::Role)\\)$

%description
Create a command line tool with your Mo, Moo, Moose objects.

%prep
%setup -q -n MooX-Options-%{version}
chmod -c -x lib/MooX/Options.pm

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes etc README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.103-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 4.103-22
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.103-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.103-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.103-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.103-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.103-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.103-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 4.103-15
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.103-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.103-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 4.103-12
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.103-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.103-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 4.103-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.103-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.103-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.103-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.103-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.103-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.103-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.103-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 25 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.103-1
- 4.103 bump

* Thu Aug 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.101-1
- 4.101 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.100-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.100-1
- 4.100 bump

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.023-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.023-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 25 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.023-1
- 4.023 bump

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.022-4
- Perl 5.24 rebuild

* Fri May 06 2016 Petr Pisar <ppisar@redhat.com> - 4.022-3
- Add run-time dependency on Text::LineFold (bug #1307852)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.022-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 4.022-1
- 4.022 bump

* Fri Jul 17 2015 Petr Pisar <ppisar@redhat.com> - 4.018-1
- Update to 4.018 (thankt to Emmanuel Seyman)
- Clean up spec file

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.015-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 4.015-2
- Perl 5.22 rebuild

* Sat Jan 24 2015 David Dick <ddick@cpan.org> - 4.015-1
- Generate warning when missing required params

* Wed Nov 26 2014 David Dick <ddick@cpan.org> - 4.013-1
- Adding autorange support

* Tue Oct 14 2014 David Dick <ddick@cpan.org> - 4.012-2
- Added missing dependency Text::LineFold

* Tue Oct 14 2014 David Dick <ddick@cpan.org> - 4.012-1
- Upgrade to 4.012

* Tue Sep 09 2014 Jitka Plesnikova <jplesnik@redhat.com> - 4.009-2
- Perl 5.20 mass

* Wed Aug 27 2014 David Dick <ddick@cpan.org> - 4.009-1
- Initial release
