# Perform optional tests
%bcond_without perl_Inline_CPP_enables_optional_test

Name:           perl-Inline-CPP
Version:        0.80
Release:        19%{?dist}
Summary:        Write Perl subroutines and classes in C++
License:        Artistic-2.0
URL:            https://metacpan.org/release/Inline-CPP
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAVIDO/Inline-CPP-%{version}.tar.gz
# Do not ask questions at build time
Patch0:         Inline-CPP-0.79-Non-interactive-Makefile.PL.patch
# Install into archicture specific path because of stored C++ compiler flags,
# CPAN RT#122557
Patch1:         Inline-CPP-0.79-Install-into-architecture-specific-path.patch
# This is a full-arch package because it stores arch-specific C++ options,
# CPAN RT#122557
%global debug_package %{nil}
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::CppGuess) >= 0.15
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.04
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Perl header files included into generated code
BuildRequires:  perl-devel
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Inline::C) >= 0.80
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Inline) >= 0.82
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 1.001009
%if %{with perl_Inline_CPP_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Inline::Filters)
%endif
Requires:       gcc-c++(%{__isa})
# Perl header files included into generated code
Requires:       perl-devel(%{__isa})
Requires:       perl(Inline::C) >= 0.80

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Inline::C\\)$

%description
The Inline::CPP Perl module allows you to put C++ source code directly "inline"
in a Perl script or module. You code classes or functions in C++, and you
can use them as if they were written in Perl.

%prep
%setup -q -n Inline-CPP-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 0.80-17
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.80-11
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.80-8
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.80-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.80-2
- Perl 5.30 rebuild

* Tue Apr 23 2019 Petr Pisar <ppisar@redhat.com> - 0.80-1
- 0.80 bump

* Wed Apr 03 2019 Petr Pisar <ppisar@redhat.com> - 0.79-1
- 0.79 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 19 2018 Petr Pisar <ppisar@redhat.com> - 0.75-1
- 0.75 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-5
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Petr Pisar <ppisar@redhat.com> 0.74-1
- Specfile autogenerated by cpanspec 1.78.
