Name:           perl-Syntax-Feature-Loop
Version:        1.8.0
Release:        20%{?dist}
Summary:        Provides the loop BLOCK syntax for unconditional loops
# lib/Syntax/Feature/ppport.h:  GPL-1.0-or-later OR Artistic-1.0-Perl
# other files:                  CC0-1.0
License:        CC0-1.0 AND ( GPL-1.0-or-later OR Artistic-1.0-Perl )
URL:            https://metacpan.org/release/Syntax-Feature-Loop
Source0:        https://cpan.metacpan.org/authors/id/I/IK/IKEGAMI/Syntax-Feature-Loop-v%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(Devel::CallParser)
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Lexical::Sub)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(syntax) >= 0.004
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.22
Requires:       perl(Lexical::Sub)
Requires:       perl(syntax) >= 0.004

%{?perl_default_filter}

%description
Syntax::Feature::Loop is a lexically-scoped pragma that provides the loop
BLOCK syntax for unconditional loops.

%prep
%setup -q -n Syntax-Feature-Loop-v%{version}

%build
perl Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README.txt
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Syntax*
%{_mandir}/man3/*

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.0-19
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.0-16
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.0-13
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.0-10
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.0-7
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.0-4
- Perl 5.28 rebuild

* Mon Feb 19 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.0-3
- Add build-require gcc

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 09 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.8.0-1
- 1.8.0 bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-16
- Perl 5.26 rebuild

* Fri May 19 2017 Petr Pisar <ppisar@redhat.com> - 1.6.0-15
- Restore compatibility with Perl 5.26.0 (CPAN RT#121788)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-13
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-10
- Perl 5.22 rebuild

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.6.0-9
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 07 2013 Petr Pisar <ppisar@redhat.com> - 1.6.0-6
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 29 2012 Petr Pisar <ppisar@redhat.com> - 1.6.0-2
- Perl 5.16 rebuild

* Mon May 21 2012 Jitka Plesnikova <jplesnik@redhat.com> 1.6.0-1
- Specfile autogenerated by cpanspec 1.78.
