%global snapshot 1
%global OWNER TLINDEN
%global PROJECT Crypt--PWSafe3
%global commit 002b0f0462a990b64c004a14151257273d637599
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20220227

Name:           perl-Crypt-PWSafe3
Version:        1.23%{?snapshot:~%{commitdate}git%{shortcommit}}
Release:        10%{?dist}
Summary:        Read and write Passwordsafe v3 files
License:        Artistic-2.0
URL:            https://metacpan.org/release/Crypt-PWSafe3
%if 0%{?snapshot}
Source0:        https://github.com/%{OWNER}/%{PROJECT}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-PWSafe3-%{version}.tar.gz
%endif
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(Bytes::Random::Secure)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Carp::Heavy)
BuildRequires:  perl(Config)
BuildRequires:  perl(Crypt::CBC) >= 2.3
BuildRequires:  perl(Crypt::ECB) >= 1.45
BuildRequires:  perl(Crypt::Twofish) >= 2.14
BuildRequires:  perl(Data::Dumper)
# Data::UUID 1.217 rounded two 2 digits
BuildRequires:  perl(Data::UUID) >= 1.22
BuildRequires:  perl(Digest::HMAC) >= 1
BuildRequires:  perl(Digest::SHA) >= 1
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Test::More)
Requires:       perl(Bytes::Random::Secure)
Requires:       perl(Crypt::CBC) >= 2.3
Requires:       perl(Crypt::ECB) >= 1.45
Requires:       perl(Crypt::Twofish) >= 2.14
# Data::UUID 1.217 rounded two 2 digits
Requires:       perl(Data::UUID) >= 1.22
Requires:       perl(Digest::HMAC) >= 1
Requires:       perl(Digest::SHA) >= 1

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:__requires_exclude|}^perl\\(Crypt::CBC\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Crypt::ECB\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Crypt::Random\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Crypt::Twofish\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Data::UUID\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Digest::HMAC\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Digest::SHA\\)$

%description
Crypt::PWSafe3 provides read and write access to password database files
created by Password Safe V3 (and up) available at <http://passwordsafe.sf.net>.

%prep
%if 0%{?snapshot}
%autosetup -n %{PROJECT}-%{commit}
%else
%autosetup -p1 -n Crypt-PWSafe3-%{version}
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc CHANGELOG README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.23~20220227git002b0f0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.23~20220227git002b0f0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Apr 20 2024 Miroslav Suchý <msuchy@redhat.com> - 1.23~20220227git002b0f0-8
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.23~20220227git002b0f0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.23~20220227git002b0f0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.23~20220227git002b0f0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.23~20220227git002b0f0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.23~20220227git002b0f0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.23~20220227git002b0f0-2
- Perl 5.36 rebuild

* Tue Mar 01 2022 Charles R. Anderson <cra@alum.wpi.edu> - 1.23~20220227git002b0f0-1
- update to git HEAD 1.23 prerelease to fix FTBFS rhbz#1939424 upstream issue #12
- BR coreutils

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-18
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-15
- Perl 5.32 rebuild

* Fri May 29 2020 Charles R. Anderson <cra@wpi.edu> - 1.22-14
- patch to remove hard dep on Crypt::Random, allowing Bytes::Random::Secure to be used instead

* Wed May 20 2020 Charles R. Anderson <cra@wpi.edu> - 1.22-13
- use versioned BR for perl(ExtUtils::MakeMaker)

* Thu May 14 2020 Charles R. Anderson <cra@wpi.edu> - 1.22-12
- Use latest perl packaging best practices

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Orion Poplawski <orion@cora.nwra.com> - 1.22-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 24 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.22-1
- 1.22 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.21-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 14 2015 Petr Pisar <ppisar@redhat.com> - 1.21-1
- 1.21 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.16-2
- Perl 5.22 rebuild

* Fri Feb 13 2015 David Dick <ddick@cpan.org> - 1.16-1
- Initial release
