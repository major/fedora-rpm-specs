Name:           perl-VM-EC2
Version:        1.28
Release:        31%{?dist}
Summary:        Perl interface to Amazon EC2
# lib/VM/EC2.pm:    GPL-1.0-or-later OR Artistic-2.0
# LICENSE:          GPL-1.0-or-later OR Artistic-2.0
# DISCLAIMER.txt:   GPL-1.0-or-later OR Artistic-1.0-Perl
# See <https://rt.cpan.org/Public/Bug/Display.html?id=104957>.
License:        (GPL-1.0-or-later OR Artistic-2.0) AND (GPL-1.0-or-later OR Artistic-1.0-Perl)
URL:            https://metacpan.org/release/VM-EC2
Source0:        https://cpan.metacpan.org/authors/id/L/LD/LDS/VM-EC2-%{version}.tar.gz
# Fix a typo leading to unresolved dependencies, CPAN RT#104961
Patch0:         VM-EC2-1.28-Fix-a-typo-in-used-module-name.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
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
# Filter private modules
%global __requires_exclude %{__requires_exclude}|^perl\\(EC2TestSupport\\)
%global __provides_exclude %{__provides_exclude}|^perl\\(EC2TestSupport\\)

%description
This is an interface to the 2014-05-01 version of the Amazon AWS API
(https://aws.amazon.com/ec2/). It was written provide access to the new tag
and metadata interface that is not currently supported by Net::Amazon::EC2, as
well as to provide developers with an extension mechanism for the API. This
library will also support the Open Stack open source cloud
(https://www.openstack.org/).

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n VM-EC2-%{version}
# Help generators to recognize Perl scripts
for F in t/*.t; do
    perl -i -MConfig -ple 'print $Config{startperl} if $. == 1 && !s{\A#!\s*perl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)" </dev/null
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
./Build test </dev/null

%files
%license DISCLAIMER.txt LICENSE
%doc Changes README
%{_bindir}/migrate-ebs-image.pl
%{_bindir}/sync_to_snapshot.pl
%dir %{perl_vendorlib}/VM
%{perl_vendorlib}/VM/EC2
%{perl_vendorlib}/VM/EC2.pm
%{_mandir}/man1/migrate-ebs-image.pl.*
%{_mandir}/man3/VM::EC2.*
%{_mandir}/man3/VM::EC2::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 07 2024 Petr Pisar <ppisar@redhat.com> - 1.28-30
- Convert a License tag to SDPX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 15 2023 Petr Pisar <ppisar@redhat.com> - 1.28-24
- Package the tests

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.28-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

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
