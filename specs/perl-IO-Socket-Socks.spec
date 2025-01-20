Name:		perl-IO-Socket-Socks
Version:	0.74
Release:	23%{?dist}
Summary:	Provides a way to create socks (4 or 5) client or server
# See https://rt.cpan.org/Public/Bug/Display.html?id=44047 for license discussion
License:	LGPL-2.0-or-later
URL:		https://metacpan.org/release/IO-Socket-Socks
Source0:	https://www.cpan.org/modules/by-module/IO/IO-Socket-Socks-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant) >= 1.03
BuildRequires:	perl(Errno)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(IO::Socket::IP) >= 0.36
BuildRequires:	perl(overload)
BuildRequires:	perl(Socket) >= 1.94
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(base)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Time::HiRes)
# Dependencies
# IPv6 support requires perl(IO::Socket::IP) ≥ 0.36
Requires:	perl(constant) >= 1.03
Requires:	perl(IO::Socket::IP) >= 0.36
Requires:	perl(Socket) >= 1.94

%description
IO::Socket::Socks connects to a SOCKS proxy and tells it to open a connection
to a remote host/port when the object is created. The object you receive can be
used directly as a socket (with IO::Socket interface) for sending and receiving
data to and from the remote host. In addition to creating a socks client, this
module could be used to create a socks server.

%prep
%setup -q -n IO-Socket-Socks-%{version}

# Don't want executable documentation
chmod -c -x examples/*.pl

# Fix up shellbangs too
sed -i -e 's|^#!/usr/bin/env perl|#!/usr/bin/perl|' examples/*.pl

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
SOCKS_SLOW_TESTS=1 make test

%files
%doc Changes examples/ README
%{perl_vendorlib}/IO/
%{_mandir}/man3/IO::Socket::Socks.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec  4 2024 Paul Howarth <paul@city-fan.org> - 0.74-22
- Drop EL-7 support
- Use %%{make_build} and %%{make_install}
- Enable SOCKS_SLOW_TESTS
- Switch source URL from cpan.metacpan.org to www.cpan.org

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-15
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-12
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-9
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.74-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.74-3
- Perl 5.28 rebuild

* Mon Feb 19 2018 Paul Howarth <paul@city-fan.org> - 0.74-2
- Incorporate feedback from package review (#1546648)
  - Add version requirements for constant and Socket runtime dependencies
  - Add examples/ as documentation

* Fri Feb 16 2018 Paul Howarth <paul@city-fan.org> - 0.74-1
- Initial RPM version
