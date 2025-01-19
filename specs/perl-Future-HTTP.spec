# some tests require Internet access, don't enable by default
%bcond network_tests 0

Name:           perl-Future-HTTP
Version:        0.17
Release:        3%{?dist}
Summary:        HTTP client with a Future API
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Future-HTTP
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CORION/Future-HTTP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make perl-interpreter perl-generators coreutils
BuildRequires:  perl(:VERSION) >= 5.20
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Future)
BuildRequires:  perl(AnyEvent::HTTP)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Future) >= 0.49
BuildRequires:  perl(Future::Mojo) >= 1.003
BuildRequires:  perl(HTTP::Request) >= 6.07
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(HTTP::Tiny::Paranoid) >= 0.07
BuildRequires:  perl(IO::Async::Future) >= 0.802
BuildRequires:  perl(IO::Async::Loop)
BuildRequires:  perl(IO::Uncompress::Bunzip2)
BuildRequires:  perl(IO::Uncompress::Gunzip)
BuildRequires:  perl(IO::Uncompress::Inflate)
BuildRequires:  perl(IO::Uncompress::RawInflate)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::QuotedPrint)
BuildRequires:  perl(Mojo::UserAgent)
BuildRequires:  perl(Mojolicious)
BuildRequires:  perl(Moo) >= 2
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Net::Async::HTTP)
BuildRequires:  perl(Pod::Markdown)
BuildRequires:  perl(Test::HTTP::LocalServer)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(URI)
BuildRequires:  perl(experimental) >= 0.031
BuildRequires:  perl(feature)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# some runtime deps are missed
Requires:       perl(Fcntl)
Requires:       perl(IO::Async::Loop)
Requires:       perl(IO::Uncompress::Bunzip2)
Requires:       perl(IO::Uncompress::Gunzip)
Requires:       perl(IO::Uncompress::Inflate)
Requires:       perl(IO::Uncompress::RawInflate)
Requires:       perl(MIME::Base64)
Requires:       perl(MIME::QuotedPrint)
Requires:       perl(warnings)
# version some requires:
Requires:       perl(HTTP::Request) >= 6.07
%global __requires_exclude ^perl\\(HTTP::Request\\)$

%description
This module is a wrapper combining Future with the API provided by
AnyEvent::HTTP. The backend used for the HTTP protocols depends on
whether one of the event loops is loaded.

%prep
%setup -q -n Future-HTTP-%{version}
%if %{without network_tests}
rm t/01-http-tiny-paranoid.t
%endif
perl -pi -e 's/\r//' Changes

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
# note: files all say perl_5 which is GPLv1/Artistic but file is Artistic-2
# https://rt.cpan.org/Ticket/Display.html?id=152217
#license LICENSE
%{perl_vendorlib}/Future/HTTP*
%{_mandir}/man3/Future::HTTP*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 16 2024 Chris Adams <linux@cmadams.net> 0.17-1
- new upstream release, tweaks versions required

* Wed Apr 03 2024 Chris Adams <linux@cmadams.net> 0.16-5
- additional spec file cleanups

* Fri Mar 08 2024 Chris Adams <linux@cmadams.net> 0.16-4
- additional spec file cleanups

* Thu Feb 01 2024 Chris Adams <linux@cmadams.net> 0.16-3
- additional spec file cleanups

* Sat Jan 20 2024 Chris Adams <linux@cmadams.net> 0.16-2
- spec file cleanups

* Mon Nov 20 2023 Chris Adams <linux@cmadams.net> 0.16-1
- initial package
