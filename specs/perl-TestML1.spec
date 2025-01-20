# Run optional test
%bcond_without perl_TestML1_enables_optional_test

Name:           perl-TestML1
Version:        0.57
Release:        21%{?dist}
Summary:        Generic software testing meta language (version 1)
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/TestML1
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/TestML1-%{version}.tar.gz
# Adapt tests to YAML-LibYAML-0.81,
# <https://github.com/ingydotnet/testml1-pm/issues/1>
Patch0:         TestML1-0.57-Adjust-tests-to-YAML-LibYAML-0.81.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
# IO::All not used at tests
# Used Pegex::Parser is not versioned, depend on Pegex version
BuildRequires:  perl(Pegex) >= 0.30
BuildRequires:  perl(Pegex::Parser)
# Template::Toolkit::Simple not used at tests
BuildRequires:  perl(Test::Builder)
# Text::Diff not used at tests
# XXX not used at test-time
BuildRequires:  perl(YAML::XS)
# Tests:
BuildRequires:  perl(base)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::More)
# Test::Pod 1.41 not used
%if %{with perl_TestML1_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Capture::Tiny)
%endif
Requires:       perl(IO::All)
Requires:       perl(Pegex) >= 0.30
Requires:       perl(Template::Toolkit::Simple)
Requires:       perl(Text::Diff)
Requires:       perl(XXX)
Requires:       perl(YAML::XS)
Requires:       perl(warnings)

%description
TestML is a generic, programming language agnostic, meta language for writing
unit tests. The idea is that you can use the same test files in multiple
implementations of a given programming idea. Then you can be more certain that
your application written in, say, Python matches your Perl implementation.

In a nutshell you write a bunch of data tests that have inputs and expected
results. Using a simple syntax, you specify what functions the data must pass
through to produce the expected results. You use a bridge class to write the
data functions that pass the data through your application.

In Perl 5, TestML is the evolution of the Test::Base module. It has a superset
of Test:Base's goals. The data markup syntax is currently exactly the same as
Test::Base.

You may want to use perl-TestML instead that supports a new generation of
the meta language.


%prep
%setup -q -n TestML1-%{version}
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.57-20
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.57-13
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.57-10
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.57-7
- Perl 5.32 rebuild

* Thu Jan 30 2020 Petr Pisar <ppisar@redhat.com> - 0.57-6
- Adapt tests to YAML-LibYAML-0.81

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.57-3
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.57-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Petr Pisar <ppisar@redhat.com> 0.57-1
- Specfile autogenerated by cpanspec 1.78.
