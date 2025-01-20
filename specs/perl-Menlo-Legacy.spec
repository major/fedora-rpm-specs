Name:           perl-Menlo-Legacy
Version:        1.9022
Release:        21%{?dist}
Summary:        Legacy internal and client support for Menlo
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Menlo-Legacy
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Menlo-Legacy-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
# BuildRequires:  perl(Archive::Tar)
# BuildRequires:  perl(Archive::Zip)
# BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
# BuildRequires:  perl(CPAN::Common::Index::LocalPackage)
# BuildRequires:  perl(CPAN::DistnameInfo)
# BuildRequires:  perl(CPAN::Meta)
# BuildRequires:  perl(CPAN::Meta::Check)
# BuildRequires:  perl(CPAN::Meta::Requirements)
# BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Cwd)
# BuildRequires:  perl(Digest::SHA)
# BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
# BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Path)
# BuildRequires:  perl(File::pushd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
# BuildRequires:  perl(HTTP::Tinyish)
# BuildRequires:  perl(JSON::PP)
# BuildRequires:  perl(local::lib)
BuildRequires:  perl(Menlo) >= 1.9018
# BuildRequires:  perl(Menlo::Builder::Static)
BuildRequires:  perl(Menlo::Dependency)
# BuildRequires:  perl(Menlo::Index::MetaCPAN)
# BuildRequires:  perl(Menlo::Index::MetaDB)
# BuildRequires:  perl(Menlo::Index::Mirror)
BuildRequires:  perl(Menlo::Util)
# BuildRequires:  perl(Module::CoreList)
# BuildRequires:  perl(Module::CPANfile)
# BuildRequires:  perl(Module::Metadata)
# BuildRequires:  perl(Module::Signature)
# BuildRequires:  perl(Parse::PMFile)
# BuildRequires:  perl(Safe)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(version) >= 0.9905
# BuildRequires:  perl(version::vpp)
# Tests
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Archive::Tar)
Requires:       perl(Archive::Zip)
Requires:       perl(Capture::Tiny)
Requires:       perl(CPAN::Common::Index::LocalPackage)
Requires:       perl(CPAN::DistnameInfo)
Requires:       perl(CPAN::Meta)
Requires:       perl(CPAN::Meta::Check)
Requires:       perl(CPAN::Meta::Requirements)
Requires:       perl(CPAN::Meta::YAML)
Requires:       perl(Digest::SHA)
Requires:       perl(ExtUtils::Manifest)
Requires:       perl(File::HomeDir)
Requires:       perl(File::pushd)
Requires:       perl(HTTP::Tinyish)
Requires:       perl(JSON::PP)
Requires:       perl(local::lib)
Requires:       perl(Menlo) >= 1.9018
Requires:       perl(Menlo::Builder::Static)
Requires:       perl(Menlo::Index::MetaCPAN)
Requires:       perl(Menlo::Index::MetaDB)
Requires:       perl(Menlo::Index::Mirror)
Requires:       perl(Module::CoreList)
Requires:       perl(Module::CPANfile)
Requires:       perl(Module::Metadata)
Requires:       perl(Module::Signature)
Requires:       perl(Parse::PMFile)
Requires:       perl(Safe)
Requires:       perl(version::vpp)
Conflicts:      perl-Menlo < 1.9019

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Menlo\\)$

%description
Menlo::Legacy is a package to install Menlo::CLI::Compat which is a
compatibility library that implements the classic version of cpanminus
internals and behavios. This is so that existing users of cpanm and API
clients such as Carton, Carmel and App::cpm) can rely on the stable
features and specific behaviors of cpanm.

%prep
%setup -q -n Menlo-Legacy-%{version}

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
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.9022-14
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.9022-11
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.9022-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 01 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.9022-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9022-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.9022-2
- Perl 5.28 rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.9022-1
- 1.9022 bump

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.9021-2
- Perl 5.28 rebuild

* Fri Apr 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.9021-1
- 1.9021 bump

* Wed Apr 25 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.9019-1
- Specfile autogenerated by cpanspec 1.78.
