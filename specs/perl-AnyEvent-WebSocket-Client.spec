Name:           perl-AnyEvent-WebSocket-Client
Version:        0.55
Release:        8%{?dist}
Summary:        WebSocket client for AnyEvent
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/AnyEvent-WebSocket-Client
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/AnyEvent-WebSocket-Client-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make perl-interpreter perl-generators coreutils
BuildRequires:  perl(:VERSION) >= 5.008
BuildRequires:  perl(AE)
BuildRequires:  perl(AnyEvent) >= 7.13
BuildRequires:  perl(AnyEvent::Connector) >= 0.03
BuildRequires:  perl(AnyEvent::Handle)
BuildRequires:  perl(AnyEvent::Socket)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildConflicts: perl(Crypt::Random::Source) < 0.08
BuildRequires:  perl(Devel::Cycle)
BuildRequires:  perl(EV)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Mojo::Server::Daemon)
BuildRequires:  perl(Mojolicious)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Moo) >= 2.0
BuildRequires:  perl(Net::SSLeay) >= 1.33
BuildRequires:  perl(PerlX::Maybe) >= 0.003
BuildRequires:  perl(PerlX::Maybe::XS)
BuildRequires:  perl(Protocol::WebSocket) >= 0.20
BuildRequires:  perl(Protocol::WebSocket::Frame)
BuildRequires:  perl(Protocol::WebSocket::Handshake::Client)
BuildRequires:  perl(Protocol::WebSocket::Handshake::Server)
BuildRequires:  perl(Protocol::WebSocket::Request)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test2::API) >= 1.302015
BuildRequires:  perl(Test2::Require) >= 0.000121
BuildRequires:  perl(Test2::Require::Module) >= 0.000121
BuildRequires:  perl(Test2::V0) >= 0.000121
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(URI) >= 1.53
BuildRequires:  perl(URI::ws)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# some runtime deps are missed
Requires:       perl(AnyEvent::Connector)
Requires:       perl(URI)
Requires:       perl(URI::ws)
Recommends:     perl(PerlX::Maybe::XS)

%description
This class provides an interface to interact with a web server that
provides services via the WebSocket protocol in an AnyEvent context.
It uses Protocol::WebSocket rather than reinventing the wheel. You
could use AnyEvent and Protocol::WebSocket directly if you wanted
finer grain control, but if that is not necessary then this class may
save you some time.

%prep
%setup -q -n AnyEvent-WebSocket-Client-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
unset PERL_AE_WS_C_TEST_PROXY_URL PERL_AE_WS_C_TEST_PROXY_ON ANYEVENT_WEBSOCKET_TEST_SKIP_SSL
make test

%files
%doc Changes README example
%license LICENSE
%{perl_vendorlib}/AnyEvent/WebSocket
%{_mandir}/man3/AnyEvent::WebSocket*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 28 2024 Joe Orton <jorton@redhat.com> - 0.55-6
- require URI::ws

* Thu May 16 2024 Chris Adams <linux@cmadams.net> 0.55-5
- additional spec file cleanups

* Fri Mar 08 2024 Chris Adams <linux@cmadams.net> 0.55-4
- additional spec file cleanups

* Thu Feb 01 2024 Chris Adams <linux@cmadams.net> 0.55-3
- additional spec file cleanups

* Sat Jan 20 2024 Chris Adams <linux@cmadams.net> 0.55-2
- spec file cleanups

* Mon Nov 20 2023 Chris Adams <linux@cmadams.net> 0.55-1
- initial package
