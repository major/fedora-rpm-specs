Name:           perl-Net-Async-HTTP
Version:        0.49
Release:        7%{?dist}
Summary:        Use HTTP with IO::Async
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Net-Async-HTTP
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/Net-Async-HTTP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter perl-generators coreutils
BuildRequires:  perl(:VERSION) >= 5.14.0
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Bzip2) >= 2.10
BuildRequires:  perl(Compress::Raw::Zlib) >= 2.057
BuildRequires:  perl(Errno)
BuildRequires:  perl(Future) >= 0.28
BuildRequires:  perl(Future::Utils) >= 0.16
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(IO::Async::Loop) >= 0.59
BuildRequires:  perl(IO::Async::Notifier)
BuildRequires:  perl(IO::Async::SSL) >= 0.12
BuildRequires:  perl(IO::Async::Stream) >= 0.59
BuildRequires:  perl(IO::Async::Test)
BuildRequires:  perl(IO::Async::Timer::Countdown)
BuildRequires:  perl(List::Util) >= 1.29
BuildRequires:  perl(Metrics::Any) >= 0.05
BuildRequires:  perl(Module::Build)
%if !0%{?perl_bootstrap}
BuildRequires:  perl(Net::Async::HTTP::Server)
%endif
BuildRequires:  perl(Net::Async::SOCKS)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Socket) >= 2.010
BuildRequires:  perl(Struct::Dumb) >= 0.07
BuildRequires:  perl(Test2::V0) >= 0.000147
BuildRequires:  perl(Test::Metrics::Any)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# some optional runtime deps
Recommends:     perl(Compress::Bzip2) >= 2.010
Recommends:     perl(Compress::Raw::Zlib) >= 2.057
Recommends:     perl(IO::Async::SSL) >= 0.12
Recommends:     perl(Net::Async::SOCKS) >= 0.003

%description
This object class implements an asynchronous HTTP user agent. It sends
requests to servers, returning Future instances to yield responses when
they are received. The object supports multiple concurrent connections to
servers, and allows multiple requests in the pipeline to any one
connection. Normally, only one such object will be needed per program to
support any number of requests.

%prep
%setup -q -n Net-Async-HTTP-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}/*

%check
unset NET_ASYNC_HTTP_MAXCONNS
./Build test

%files
%doc Changes examples README
%license LICENSE
%{perl_vendorlib}/Net/Async/HTTP*
%{_mandir}/man3/Net::Async::HTTP*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.49-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 29 2024 Chris Adams <linux@cmadams.net> 0.49-6
- perl-Net-Async-HTTP-Server is in repo now, so remove forced bootstrap mode

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.49-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 08 2024 Chris Adams <linux@cmadams.net> 0.49-4
- additional spec file cleanups

* Thu Feb 01 2024 Chris Adams <linux@cmadams.net> 0.49-3
- additional spec file cleanups

* Sat Jan 20 2024 Chris Adams <linux@cmadams.net> 0.49-2
- spec file cleanups

* Mon Nov 20 2023 Chris Adams <linux@cmadams.net> 0.49-1
- initial package
