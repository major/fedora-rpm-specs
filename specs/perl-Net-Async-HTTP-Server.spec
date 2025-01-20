Name:           perl-Net-Async-HTTP-Server
Version:        0.14
Release:        6%{?dist}
Summary:        Serve HTTP with IO::Async
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Net-Async-HTTP-Server
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Net-Async-HTTP-Server-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter perl-generators coreutils
BuildRequires:  perl(:VERSION) >= 5.14.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(IO::Async) >= 0.54
BuildRequires:  perl(IO::Async::Listener) >= 0.61
BuildRequires:  perl(IO::Async::Loop)
BuildRequires:  perl(IO::Async::SSL)
BuildRequires:  perl(IO::Async::Stream)
BuildRequires:  perl(IO::Async::Test)
BuildRequires:  perl(IO::Socket::UNIX)
BuildRequires:  perl(Metrics::Any) >= 0.05
BuildRequires:  perl(Module::Build) >= 0.4004
BuildRequires:  perl(Net::Async::HTTP)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test2::V0) >= 0.000147
BuildRequires:  perl(Test::Metrics::Any)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Refcount)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Recommends:     perl(IO::Async::SSL)
Recommends:     perl(IO::Socket::UNIX)

%description
This module allows a program to respond asynchronously to HTTP requests, as
part of a program based on IO::Async. An object in this class listens on a
single port and invokes the on_request callback or subclass method whenever
an HTTP request is received, allowing the program to respond to it.

%prep
%setup -q -n Net-Async-HTTP-Server-%{version}

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
%dir %{perl_vendorlib}/Net
%dir %{perl_vendorlib}/Net/Async
%dir %{perl_vendorlib}/Net/Async/HTTP
%{perl_vendorlib}/Net/Async/HTTP/Server*
%dir %{perl_vendorlib}/Plack
%dir %{perl_vendorlib}/Plack/Handler
%dir %{perl_vendorlib}/Plack/Handler/Net
%dir %{perl_vendorlib}/Plack/Handler/Net/Async
%dir %{perl_vendorlib}/Plack/Handler/Net/Async/HTTP
%{perl_vendorlib}/Plack/Handler/Net/Async/HTTP/Server.pm
%{_mandir}/man3/Net::Async::HTTP*
%{_mandir}/man3/Plack::Handler::Net::Async::HTTP*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Sep 21 2024 Chris Adams <linux@cmadams.net> 0.14-5
- make sure to own all the right directories

* Fri Mar 08 2024 Chris Adams <linux@cmadams.net> 0.14-4
- additional spec file cleanups

* Thu Feb 01 2024 Chris Adams <linux@cmadams.net> 0.14-3
- additional spec file cleanups

* Sat Jan 20 2024 Chris Adams <linux@cmadams.net> 0.14-2
- spec file cleanups

* Mon Nov 20 2023 Chris Adams <linux@cmadams.net> 0.14-1
- initial package
