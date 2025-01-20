Name:           perl-Net-Async-SOCKS
Version:        0.003
Release:        6%{?dist}
Summary:        Some degree of SOCKS5 proxy support in IO::Async
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Net-Async-SOCKS/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Net-Async-SOCKS-%{version}.tar.gz
Patch0:         Net-Async-SOCKS-0.003-noRefcount.patch
BuildArch:      noarch
BuildRequires:  make perl-interpreter perl-generators coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Future) >= 0.29
BuildRequires:  perl(IO::Async) >= 0.62
BuildRequires:  perl(IO::Async::Loop)
BuildRequires:  perl(IO::Async::Stream)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Protocol::SOCKS) >= 0.003
BuildRequires:  perl(Protocol::SOCKS::Client)
BuildRequires:  perl(Protocol::SOCKS::Constants)
BuildRequires:  perl(Test::CheckDeps) >= 0.010
BuildRequires:  perl(Test::Fatal) >= 0.010
BuildRequires:  perl(Test::HexString)
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(blib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
Currently provides a very basic implementation of SOCKS_connect:

%prep
%setup -q -n Net-Async-SOCKS-%{version}
# incorrectly tries to require Test::Refcount which is not used
%patch -P0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.003-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar 11 2024 Chris Adams <linux@cmadams.net> 0.003-4
- fix FTBFS by removing Test::Refcount check (rhbz#2268969)

* Thu Feb 01 2024 Chris Adams <linux@cmadams.net> 0.003-3
- additional spec file cleanups

* Sat Jan 20 2024 Chris Adams <linux@cmadams.net> 0.003-2
- spec file cleanups

* Mon Nov 20 2023 Chris Adams <linux@cmadams.net> 0.003-1
- initial package
