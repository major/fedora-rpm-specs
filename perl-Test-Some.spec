%define upstream_name Test-Some
Name:       perl-%{upstream_name}
Version:    0.2.1
Release:    8%{?dist}
License:    GPL+ or Artistic
Group:      Development/Libraries
Summary:    Run a subset of tests
Source:     https://cpan.metacpan.org/authors/id/Y/YA/YANICK/%{upstream_name}-%{version}.tar.gz
Url:        https://metacpan.org/release/%{upstream_name}
BuildArch:  noarch
Requires:   perl-interpreter
BuildRequires: coreutils
BuildRequires: make
BuildRequires: perl(:VERSION) >= 5.10.0
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Package::Stash)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More)
BuildRequires: perl(blib)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl-generators

%description
This module allows one to run a subset of the 'subtest' tests given in a test
file.

The module declaration takes a whitelist of the subtests we want to run.
Any subtest that doesn't match any of the whitelist items will be skipped
(or potentially bypassed).

The test files don't even need to be modified, as the module can also be
invoked from the command-line.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
%{make_build}

%install
%{make_install}

%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.2.1-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Shlomi Fish <shlomif@shlomifish.org> 0.2.1-1
- initial Fedora packaging
- generated with cpan2dist (CPANPLUS::Dist::Fedora version 0.2.2)
