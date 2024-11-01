Name:           perl-rdapper
Version:        1.04
Release:        1%{?dist}
Summary:        Simple console-based RDAP client
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/App-rdapper
# Upstream source repository is <https://github.com/gbxyz/rdapper>, renamed
# from <https://github.com/jodrell/rdapper> that was announced by the author
# at <https://www.ietf.org/mail-archive/web/weirds/current/msg01981.html>.
Source0:        https://cpan.metacpan.org/authors/id/G/GB/GBROWN/App-rdapper-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
# No tests, no run-time time dependencies used
# constant
# Getopt::Long
# JSON
# List::MoreUtils
# List::Util
# Net::ASN
# Net::DNS::Domain
# Net::IP
# Net::RDAP 0.26
# Net::RDAP::EPPStatusMap
# Pod::Usage
# Term::ANSIColor
# Term::Size
# Text::Wrap
# URI
# vars
# To support HTTPS
Requires:       perl(LWP::Protocol::https)

%description
"rdapper" is a simple RDAP client. It uses Net::RDAP to retrieve data about
internet resources (domain names, IP addresses, and autonomous systems) and
outputs the information in a human-readable format.

%prep
%autosetup -p1 -n App-rdapper-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README.md
%{_bindir}/rdapper
%dir %{perl_vendorlib}/App
%{perl_vendorlib}/App/rdapper.pm
%{_mandir}/man3/App::rdapper.*

%changelog
* Fri Oct 25 2024 Petr Pisar <ppisar@redhat.com> - 1.04-1
- 1.04 bump

* Fri Sep 27 2024 Petr Pisar <ppisar@redhat.com> - 1.03-1
- 1.03 bump

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.08-25
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-18
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-15
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.08-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.08-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jun 07 2016 Petr Pisar <ppisar@redhat.com> 0.08-1
- Specfile autogenerated by cpanspec 1.78.
