Name:           perl-VM-EC2
Version:        1.28
Release:        22%{?dist}
Summary:        Perl interface to Amazon EC2
# lib/VM/EC2.pm:    GPL+ or Artistic 2.0
# LICENSE:          GPL+ or Artistic 2.0
# DISCLAIMER.txt:   GPL+ or Artistic
# See <https://rt.cpan.org/Public/Bug/Display.html?id=104957>.
License:        (GPL+ or Artistic 2.0) and (GPL+ or Artistic)
URL:            https://metacpan.org/release/VM-EC2
Source0:        https://cpan.metacpan.org/authors/id/L/LD/LDS/VM-EC2-%{version}.tar.gz
# Fix a typo leading to unresolved dependencies, CPAN RT#104961
Patch0:         VM-EC2-1.28-Fix-a-typo-in-used-module-name.patch
BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(AnyEvent) >= 7.04
BuildRequires:  perl(AnyEvent::CacheDNS) >= 0.08
BuildRequires:  perl(AnyEvent::CondVar)
BuildRequires:  perl(AnyEvent::HTTP) >= 2.15
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::SHA) >= 5.47
BuildRequires:  perl(File::Basename)
# File::Find not used at tests
BuildRequires:  perl(File::Path) >= 2.08
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
# Getopt::Long not used at tests
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
# LWP::UserAgent version from LWP's version in META.json
# LWP::UserAgent 5.835 not used at tests
BuildRequires:  perl(MIME::Base64) >= 3.08
BuildRequires:  perl(overload)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
# Storable not used at tests
BuildRequires:  perl(String::Approx) >= 3.26
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::Simple) >= 2.18
# Tests:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       perl(AnyEvent) >= 7.04
Requires:       perl(AnyEvent::HTTP) >= 2.15
Requires:       perl(Digest::SHA) >= 5.47
Requires:       perl(File::Path) >= 2.08
# LWP::UserAgent version from LWP's version in META.json
Requires:       perl(LWP::UserAgent) >= 5.835
Requires:       perl(String::Approx) >= 3.26
Requires:       perl(XML::Simple) >= 2.18

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((AnyEvent|AnyEvent::HTTP|Digest::SHA|File::Path|LWP::UserAgent|String::Approx|XML::Simple)\\)$
# Filter under-specified provides
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(VM::EC2\\)$

%description
This is an interface to the 2014-05-01 version of the Amazon AWS API
(https://aws.amazon.com/ec2/). It was written provide access to the new tag
and metadata interface that is not currently supported by Net::Amazon::EC2, as
well as to provide developers with an extension mechanism for the API. This
library will also support the Open Stack open source cloud
(https://www.openstack.org/).

%prep
%setup -q -n VM-EC2-%{version}
%patch0 -p1

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test </dev/null

%files
%license DISCLAIMER.txt LICENSE
%doc Changes README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.28-21
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-19
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.28-18
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.28-15
- Perl 5.32 rebuild

* Fri Feb 07 2020 Petr Pisar <ppisar@redhat.com> - 1.28-14
- Update a description

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.28-11
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.28-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.28-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.28-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 04 2015 Petr Pisar <ppisar@redhat.com> 1.28-1
- Specfile autogenerated by cpanspec 1.78.
- Remove unused build-time dependencies
