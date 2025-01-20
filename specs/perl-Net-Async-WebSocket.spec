Name:           perl-Net-Async-WebSocket
Version:        0.14
Release:        2%{?dist}
Summary:        Use WebSockets with IO::Async
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Net-Async-WebSocket
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Net-Async-WebSocket-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter perl-generators coreutils
BuildRequires:  perl(:VERSION) >= 5.14
BuildRequires:  perl(Carp)
BuildRequires:  perl(IO::Async::Listener) >= 0.61
BuildRequires:  perl(IO::Async::Loop)
BuildRequires:  perl(IO::Async::Notifier) >= 0.63
BuildRequires:  perl(IO::Async::OS)
BuildRequires:  perl(IO::Async::Stream) >= 0.34
BuildRequires:  perl(IO::Async::Test)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(Module::Build) >= 0.4004
BuildRequires:  perl(Protocol::WebSocket) >= 0.22
BuildRequires:  perl(Protocol::WebSocket::Frame)
BuildRequires:  perl(Protocol::WebSocket::Handshake::Client)
BuildRequires:  perl(Protocol::WebSocket::Handshake::Server)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::wss)
BuildRequires:  perl(base)
BuildRequires:  perl(meta) >= 0.008
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# some runtime deps are missed/are optional
Recommends:     perl(IO::Async::SSL)
Requires:       perl(Protocol::WebSocket) >= 0.22
Requires:       perl(URI::wss)
# version some deps
Requires:       perl(IO::Async::Listener) >= 0.61
Requires:       perl(IO::Async::Stream) >= 0.34
%global __requires_exclude ^perl\\(IO::Async::(Listener|Stream)\\)$

%description
This distribution provides modules that implement the WebSocket protocol,
and allows either servers or clients to be written based on IO::Async.

%prep
%setup -q -n Net-Async-WebSocket-%{version}

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
%{perl_vendorlib}/Net
%{_mandir}/man3/Net::Async::WebSocket*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Sep 21 2024 Chris Adams <linux@cmadams.net> 0.14-1
- update to new upstream release
- update dependencies to match

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 15 2024 Chris Adams <linux@cmadams.net> 0.13-5
- additional spec file cleanups

* Fri Mar 08 2024 Chris Adams <linux@cmadams.net> 0.13-4
- additional spec file cleanups

* Thu Feb 01 2024 Chris Adams <linux@cmadams.net> 0.13-3
- additional spec file cleanups

* Sat Jan 20 2024 Chris Adams <linux@cmadams.net> 0.13-2
- spec file cleanups

* Mon Nov 20 2023 Chris Adams <linux@cmadams.net> 0.13-1
- initial package
