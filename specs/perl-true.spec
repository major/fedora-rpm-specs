Name:		perl-true
Version:	1.0.2
Release:	15%{?dist}
Summary:	Automatically return a true value when a file is required
License:	Artistic-2.0
URL:		https://metacpan.org/release/true
Source0:	http://cpan.metacpan.org/authors/id/C/CH/CHOCOLATE/true-v%{version}.tar.gz
# ============= Module Build ====================
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Config)
BuildRequires:	perl(ExtUtils::Depends) >= 0.304
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(File::Copy)
# ============= Module Runtime ==================
BuildRequires:	perl(B::Hooks::OP::Annotation) >= 0.44
BuildRequires:	perl(B::Hooks::OP::Check) >= 0.22
BuildRequires:	perl(Devel::StackTrace) >= 2.03
BuildRequires:	perl(strict)
BuildRequires:	perl(version) >= 0.77
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# ============= Test Suite ======================
BuildRequires:	perl(base)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(Function::Parameters) >= 2.001003
BuildRequires:	perl(lib)
BuildRequires:	perl(Moo) >= 2.003004
BuildRequires:	perl(Test::More)
# ============= Module Dependencies =============
# (none)

# Don't "provide" private Perl libs
%{?perl_default_filter}

%description
Perl's require built-in (and its use wrapper) requires the files it loads to
return a true value. This is usually accomplished by placing a single

	1;

statement at the end of included scripts or modules. It's not onerous to add
but it's a speed bump on the Perl novice's road to enlightenment. In addition,
it appears to be a non-sequitur to the uninitiated, leading some to attempt to
mitigate its appearance with a comment:

	1; # keep require happy
or:
	1; # Do not remove this line
or even:
	1; # Must end with this, because Perl is bogus.

This module packages this "return true" behavior so that it need not be
written explicitly. It can be used directly, but it is intended to be invoked
from the import method of a Modern::Perl-style module that enables modern Perl
features and conveniences and cleans up legacy Perl warts.

%prep
%setup -q -n true-v%{version}

%build
perl Makefile.PL \
	INSTALLDIRS=vendor \
	NO_PACKLIST=1 \
	NO_PERLLOCAL=1 \
	OPTIMIZE="%{optflags}"
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE.md
%doc Changes README
%{perl_vendorarch}/auto/true/
%{perl_vendorarch}/true.pm
%{perl_vendorarch}/true/
%{_mandir}/man3/true.3*
%{_mandir}/man3/true::VERSION.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 11 2024 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.2-13
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.2-9
- Perl 5.38 rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.2-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.2-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 11 2020 Paul Howarth <paul@city-fan.org> - 1.0.2-1
- Update to 1.0.2
  - Code clean-up
  - Update ppport.h from 3.44 → 3.62

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.1-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.1-2
- Perl 5.30 rebuild

* Tue Mar 12 2019 Paul Howarth <paul@city-fan.org> - 1.0.1-1
- Update to 1.0.1
  - Fix breakage when using Moo/Moose and Function::Parameters on perl < 5.24
    (CPAN RT#124745)
  - Add t/rt-124745.t
  - Update ppport.h from 3.19 → 3.44
- License changed from (GPL+ or Artistic) to Artistic 2.0
- Modernize spec using features from ExtUtils::MakeMaker ≥ 6.76

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-17
- Perl 5.28 rebuild

* Thu Feb 22 2018 Paul Howarth <paul@city-fan.org> - 0.18-16
- BR: gcc
- Drop legacy Group: tag

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-12
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-10
- Perl 5.24 rebuild

* Tue Apr 19 2016 Paul Howarth <paul@city-fan.org> - 0.18-9
- Fix FTBFS due to missing buildreq perl-devel
- Simplify find commands using -empty and -delete

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-6
- Perl 5.22 rebuild

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.18-5
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 19 2013 Paul Howarth <paul@city-fan.org> - 0.18-2
- Sanitize for Fedora submission

* Fri Aug 16 2013 Paul Howarth <paul@city-fan.org> - 0.18-1
- Initial RPM version
