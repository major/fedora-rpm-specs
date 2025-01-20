Name:           perl-Menlo
Version:        1.9019
Release:        22%{?dist}
Summary:        A CPAN client
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Menlo
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Menlo-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Runtime
# BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Tiny) >= 1.001
BuildRequires:  perl(constant)
# BuildRequires:  perl(CPAN::Common::Index) >= 0.006
# BuildRequires:  perl(CPAN::Common::Index::Mirror)
# BuildRequires:  perl(CPAN::Meta) >= 2.132830
BuildRequires:  perl(CPAN::Meta::Requirements)
# BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Exporter)
# BuildRequires:  perl(ExtUtils::Config) >= 0.003
# BuildRequires:  perl(ExtUtils::Helpers) >= 1.020
# BuildRequires:  perl(ExtUtils::Install)
# BuildRequires:  perl(ExtUtils::InstallPaths) >= 0.002
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
# BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::Spec)
# BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Getopt::Long) >= 2.36
# BuildRequires:  perl(HTTP::Tiny) >= 0.054
# BuildRequires:  perl(HTTP::Tinyish) >= 0.04
# BuildRequires:  perl(IO::Uncompress::Gunzip)
# BuildRequires:  perl(JSON::PP) >= 2
# BuildRequires:  perl(parent)
# BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(String::ShellQuote)
# BuildRequires:  perl(TAP::Harness::Env)
# BuildRequires:  perl(Time::Local)
# BuildRequires:  perl(URI)
# Tests only
BuildRequires:  perl(Test::More)
Requires:       git
Requires:       perl(Class::Tiny) >= 1.001
Requires:       perl(CPAN::Common::Index) >= 0.006
Requires:       perl(CPAN::Meta) >= 2.132830
Requires:       perl(File::pushd)
Requires:       perl(HTTP::Tiny) >= 0.054
Requires:       perl(HTTP::Tinyish) >= 0.04
Requires:       perl(Pod::Man)
Requires:       perl(String::ShellQuote)
Requires:       perl(TAP::Harness::Env)

%{?perl_default_filter}

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(CPAN::Common::Index\\)$
%global __requires_exclude :%__requires_exclude|^perl\\(CPAN::Meta\\)$
%global __requires_exclude :%__requires_exclude|^perl\\(Class::Tiny\\)$
%global __requires_exclude :%__requires_exclude|^perl\\(HTTP::Tiny\\)$

%description
Menlo is a code name for cpanm 2.0, developed with the goal to
replace cpanm and its back-end with a more flexible, extensible and
easier to use APIs.

%prep
%setup -q -n Menlo-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9019-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9019-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9019-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9019-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9019-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9019-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.9019-16
- Update license to SPDX format and use %%make_* macros

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9019-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.9019-14
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9019-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9019-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.9019-11
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9019-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9019-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.9019-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9019-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9019-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.9019-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9019-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9019-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.9019-2
- Perl 5.28 rebuild

* Wed Apr 25 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.9019-1
- 1.9019 bump

* Mon Apr 23 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.9018-1
- 1.9018 bump

* Fri Apr 20 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.9011-1
- 1.9011 bump

* Fri Apr 20 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.9008-1
- 1.9008 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9005-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Petr Pisar <ppisar@redhat.com> - 1.9005-4
- Remove /usr/bin/env from shebang

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.9005-2
- Perl 5.26 rebuild

* Fri May 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.9005-1
- 1.9005 bump

* Mon Apr 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.9004-1
- 1.9004 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 07 2016 Petr Pisar <ppisar@redhat.com> - 1.9003-1
- 1.9003 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.9001-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 08 2015 Petr Šabata <contyk@redhat.com> 1.9001-1
- Initial packaging
