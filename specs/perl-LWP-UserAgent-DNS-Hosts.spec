Name:           perl-LWP-UserAgent-DNS-Hosts
Version:        0.14
Release:        14%{?dist}
Summary:        Override LWP HTTP/HTTPS request's host like /etc/hosts

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/LWP-UserAgent-DNS-Hosts
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MASAKI/LWP-UserAgent-DNS-Hosts-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
# runtime
BuildRequires:  perl(parent)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Carp)
BuildRequires:  perl(LWP::Protocol)
BuildRequires:  perl(LWP::Protocol::http)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(Scope::Guard)
# tests:
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::UseAllModules)
BuildRequires:  perl(Test::Fake::HTTPD) >= 0.08
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(File::Temp)


%{?perl_default_filter}


%description
LWP::UserAgent::DNS::Hosts is a module to override HTTP/HTTPS request peer
addresses that uses LWP::UserAgent.  This module concept was got from
LWP::Protocol::PSGI.


%prep
%setup -q -n LWP-UserAgent-DNS-Hosts-%{version}


%build
%{__perl} Build.PL --installdirs=vendor
./Build


%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}


%check
./Build test


%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.14-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-6
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 Carl George <carl@george.computer> - 0.14-1
- Latest upstream rhbz#1869061

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Petr Pisar <ppisar@redhat.com> - 0.13-9
- Adjust to an updated crypto policy that disabled SHA1 (bug #1852230)

* Thu Jun 25 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.13-2
- Perl 5.28 rebuild

* Mon Feb 26 2018 Carl George <carl@george.computer> - 0.13-1
- Latest upstream

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.12-2
- Perl 5.26 rebuild

* Mon May 01 2017 Carl George <carl.george@rackspace.com> - 0.12-1
- Latest upstream

* Tue Apr 04 2017 Carl George <carl.george@rackspace.com> - 0.11-3
- Remove deprecated Group tag
- Fix typo

* Fri Mar 17 2017 Carl George <carl.george@rackspace.com> - 0.11-2
- Rebuild

* Fri Mar 17 2017 Carl George <carl.george@rackspace.com> - 0.11-1
- Latest upstream
- Set minimum version of Test::Fake::HTTPD to 0.08

* Fri Mar 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.10-1
- 0.10 bump; Upstream switched to Module::Build::Tiny flow

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 12 2016 Carl George <carl.george@rackspace.com> - 0.08-3
- Add more missing build requirements

* Mon Aug 08 2016 Carl George <carl.george@rackspace.com> - 0.08-2
- Add missing build requirements
- Remove bundled Module::Install libs

* Wed Aug 03 2016 Carl George <carl.george@rackspace.com> - 0.08-1
- Initial package
