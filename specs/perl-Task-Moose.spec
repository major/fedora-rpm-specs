Name:           perl-Task-Moose
Version:        0.03
Release:        36%{?dist}
Summary:        Moose in a box
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Task-Moose
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOY/Task-Moose-%{version}.tar.gz
BuildArch:      noarch


BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install) >= 0.75
# Moose and Moose extentions are listed in Makefile.PL
BuildRequires:  perl(Moose) >= 0.92
BuildRequires:  perl(MooseX::StrictConstructor) >= 0.08
BuildRequires:  perl(MooseX::Params::Validate) >= 0.06
BuildRequires:  perl(MooseX::Role::TraitConstructor)
BuildRequires:  perl(MooseX::Traits)
BuildRequires:  perl(MooseX::Object::Pluggable)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(MooseX::GlobRef)
BuildRequires:  perl(MooseX::InsideOut)
BuildRequires:  perl(MooseX::Singleton) >= 0.20
BuildRequires:  perl(MooseX::NonMoose) >= 0.06
BuildRequires:  perl(MooseX::Declare)
BuildRequires:  perl(MooseX::Method::Signatures)
BuildRequires:  perl(MooseX::Types) >= 0.20
BuildRequires:  perl(MooseX::Types::Structured)
BuildRequires:  perl(MooseX::Types::Path::Class)
BuildRequires:  perl(MooseX::Types::Set::Object)
BuildRequires:  perl(MooseX::Types::DateTime)
BuildRequires:  perl(MooseX::Getopt)
BuildRequires:  perl(MooseX::ConfigFromFile)
BuildRequires:  perl(MooseX::SimpleConfig)
BuildRequires:  perl(MooseX::App::Cmd)
BuildRequires:  perl(MooseX::Role::Cmd)
BuildRequires:  perl(MooseX::LogDispatch)
BuildRequires:  perl(MooseX::LazyLogDispatch)
BuildRequires:  perl(MooseX::Log::Log4perl)
BuildRequires:  perl(MooseX::POE)
BuildRequires:  perl(MooseX::Workers)
BuildRequires:  perl(MooseX::Daemonize)
BuildRequires:  perl(MooseX::Param)
BuildRequires:  perl(MooseX::Iterator)
BuildRequires:  perl(MooseX::Clone)
BuildRequires:  perl(MooseX::Storage)
BuildRequires:  perl(Moose::Autobox)
BuildRequires:  perl(MooseX::ClassAttribute)
BuildRequires:  perl(MooseX::SemiAffordanceAccessor)
BuildRequires:  perl(namespace::autoclean) >= 0.09
BuildRequires:  perl(Pod::Coverage::Moose)
# Listed on Task::Moose man page
BuildRequires:  perl(TryCatch)
# Tests
BuildRequires:  perl(Test::More)

Requires:       perl(Moose) >= 0.92
# Make Moose Stricter
Requires:       perl(MooseX::StrictConstructor) >= 0.08
Requires:       perl(MooseX::Params::Validate) >= 0.06
# Traits / Roles
Requires:       perl(MooseX::Role::TraitConstructor)
Requires:       perl(MooseX::Traits)
Requires:       perl(MooseX::Object::Pluggable)
Requires:       perl(MooseX::Role::Parameterized)
# Instance Types
Requires:       perl(MooseX::GlobRef)
Requires:       perl(MooseX::InsideOut)
Requires:       perl(MooseX::Singleton) >= 0.20
Requires:       perl(MooseX::NonMoose) >= 0.06
# Declarative Syntax
Requires:       perl(MooseX::Declare)
Requires:       perl(MooseX::Method::Signatures)
Requires:       perl(TryCatch)
# Types
Requires:       perl(MooseX::Types) >= 0.20
Requires:       perl(MooseX::Types::Structured)
Requires:       perl(MooseX::Types::Path::Class)
Requires:       perl(MooseX::Types::Set::Object)
Requires:       perl(MooseX::Types::DateTime)
# Command Line Integration
Requires:       perl(MooseX::Getopt)
Requires:       perl(MooseX::ConfigFromFile)
Requires:       perl(MooseX::SimpleConfig)
Requires:       perl(MooseX::App::Cmd)
Requires:       perl(MooseX::Role::Cmd)
# Logging
Requires:       perl(MooseX::LogDispatch)
Requires:       perl(MooseX::LazyLogDispatch)
Requires:       perl(MooseX::Log::Log4perl)
# Async
Requires:       perl(MooseX::POE)
Requires:       perl(MooseX::Workers)
# Utility Roles
Requires:       perl(MooseX::Daemonize)
Requires:       perl(MooseX::Param)
Requires:       perl(MooseX::Iterator)
Requires:       perl(MooseX::Clone)
Requires:       perl(MooseX::Storage)
# Other Useful Extensions
Requires:       perl(Moose::Autobox)
Requires:       perl(MooseX::ClassAttribute)
Requires:       perl(MooseX::SemiAffordanceAccessor)
Requires:       perl(namespace::autoclean) >= 0.09
# Utilities
Requires:       perl(Pod::Coverage::Moose)


%description
This Task installs Moose and a number of Moose extensions.

%prep
%setup -q -n Task-Moose-%{version}
rm -r inc
sed -i -e '/^inc\// d' MANIFEST
find -type f -exec chmod -x {} +

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor </dev/null
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT 
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-29
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-26
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-23
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-20
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-17
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-14
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 30 2016 Petr Pisar <ppisar@redhat.com> - 0.03-12
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.03-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-9
- Perl 5.22 rebuild

* Mon Sep 01 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.03-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Aug 06 2013 Petr Pisar <ppisar@redhat.com> - 0.03-6
- Perl 5.18 rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 30 2012 Petr Pisar <ppisar@redhat.com> - 0.03-2
- Perl 5.16 rebuild

* Fri May 11 2012 Jitka Plesnikova <jplesnik@redhat.com> 0.03-1
- Initial release.
