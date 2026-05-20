%global pkgname Net-DNSBL-Client

Summary:        Perl module with client code for querying multiple DNSBLs
Name:           perl-Net-DNSBL-Client
Version:        0.207
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/%{pkgname}
Source0:        https://cpan.metacpan.org/authors/id/D/DS/DSKOLL/%{pkgname}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Install)
BuildRequires:  perl(Net::DNS::Resolver)
# Tests
BuildRequires:  perl(Carp)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.82
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildArch:      noarch

%description
This Perl module is an easy-to-use library for looking up IP addresses
against multiple DNSBLs at once. It supports different types of DNSBLs:
Normal, meaning that any returned A record indicates a hit, match,
meaning that one of the returned A records must exactly match a given
IP address, mask, meaning that one of the returned A records must
evaluate to non-zero when bitwise-ANDed against a given IP address, or
txt meaning that TXT records should be looked up and returned (rather
than A records).

%prep
%setup -q -n %{pkgname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README
%{_bindir}/dnsblcheck
%{perl_vendorlib}/Net/
%{_mandir}/man1/dnsblcheck.1*
%{_mandir}/man3/Net::DNSBL::Client.3pm*

%changelog
* Sun Dec 14 2025 Robert Scheck <robert@fedoraproject.org> 0.207-1
- Upgrade to 0.207 (#2422114)
- Initial spec file for Fedora and Red Hat Enterprise Linux
