Name:           perl-IO-Async-SSL
Version:        0.25
Release:        6%{?dist}
Summary:        Use SSL/TLS with IO::Async
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/IO-Async-SSL/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/IO-Async-SSL-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter perl-generators coreutils
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(Carp)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Future) >= 0.33
BuildRequires:  perl(IO::Async::Handle) >= 0.29
BuildRequires:  perl(IO::Async::Listener)
BuildRequires:  perl(IO::Async::Loop) >= 0.66
BuildRequires:  perl(IO::Async::OS)
BuildRequires:  perl(IO::Async::Protocol::Stream)
BuildRequires:  perl(IO::Async::Stream) >= 0.59
BuildRequires:  perl(IO::Async::Test) >= 0.68
BuildRequires:  perl(IO::Socket::SSL) >= 2.003
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::Identity)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  /usr/bin/openssl /usr/bin/socat

%description
This module extends existing IO::Async classes with extra methods to allow
the use of SSL or TLS-based connections using IO::Socket::SSL. It does not
directly provide any methods or functions of its own.

%prep
%setup -q -n IO-Async-SSL-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes examples README
%license LICENSE
%{perl_vendorlib}/IO/Async/SSL*
%{_mandir}/man3/IO::Async::SSL*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 08 2024 Chris Adams <linux@cmadams.net> 0.25-4
- additional spec file cleanups

* Thu Feb 01 2024 Chris Adams <linux@cmadams.net> 0.25-3
- additional spec file cleanups

* Sat Jan 20 2024 Chris Adams <linux@cmadams.net> 0.25-2
- spec file cleanups

* Mon Nov 20 2023 Chris Adams <linux@cmadams.net> 0.25-1
- initial package
