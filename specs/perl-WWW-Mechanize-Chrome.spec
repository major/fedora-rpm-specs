# tests are having issues that appear to be due to Chrome/Chromium, so
# don't run them by default
%bcond do_tests 0
%bcond debug_tests 0
# some tests require Internet access, don't enable by default
%bcond network_tests 0

Name:           perl-WWW-Mechanize-Chrome
Version:        0.73
Release:        5%{?dist}
Summary:        Automate the Chrome browser
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/WWW-Mechanize-Chrome

# perl-WWW-Mechanize-Chrome contains copyrighted web pages without a
# distributable license.  Use this script to remove the pages and the
# test that uses them.  Download the upstream tarball and run this
# script in the same directory:
# sh ./WWW-Mechanize-Chrome-generate-tarball.sh $VERSION
#Source0:        https://cpan.metacpan.org/authors/id/C/CO/CORION/WWW-Mechanize-Chrome-%%{version}.tar.gz
Source0:        WWW-Mechanize-Chrome-%{version}-nocopyright.tar.gz
Source1:        WWW-Mechanize-Chrome-generate-tarball.sh

BuildArch:      noarch
BuildRequires:  make perl-interpreter perl-generators coreutils
BuildRequires:  perl(:VERSION) >= 5.20
BuildRequires:  perl(Exporter) >= 5
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Future) >= 0.35
BuildRequires:  perl(Future::HTTP) >= 0.06
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTML::Selector::XPath)
BuildRequires:  perl(Imager)
BuildRequires:  perl(Image::Info)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Moo) >= 2
BuildRequires:  perl(MooX::Role::EventEmitter)
BuildRequires:  perl(Net::Async::WebSocket::Client) >= 0.12
BuildRequires:  perl(Object::Import)
BuildRequires:  perl(PerlX::Maybe)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::HTTP::LocalServer) >= 0.71
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::Without::Module)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(URI::ws)
BuildRequires:  perl(WWW::Mechanize::Link)
BuildRequires:  perl(experimental) >= 0.031
BuildRequires:  perl(strict)
%if %{with do_tests}
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::Future)
BuildRequires:  perl(AnyEvent::WebSocket::Client)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dump)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Glob)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Filter::signatures)
BuildRequires:  perl(Future::Mojo)
BuildRequires:  perl(Future::Utils)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(IO::Async::Loop)
BuildRequires:  perl(IO::Async::Stream)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Mojo::IOLoop::Stream)
BuildRequires:  perl(Mojo::UserAgent)
BuildRequires:  perl(Pod::Markdown)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(feature)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(parent)
BuildRequires:  perl(stable) >= 0.031
BuildRequires:  perl(warnings)
BuildRequires:  chromium
%endif

# some runtime deps are missed
Requires:       perl(Cwd)
Requires:       perl(HTTP::Cookies)
Requires:       perl(Imager)
Requires:       perl(Log::Log4perl)

%description
Like WWW::Mechanize, this module automates web browsing with a Perl object.
Fetching and rendering of web pages is delegated to the Chrome (or
Chromium) browser by starting an instance of the browser and controlling it
with Chrome DevTools.

%prep
%setup -q -n WWW-Mechanize-Chrome-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%if %{without do_tests}
exit 0
%endif

export CHROME_BIN=%{_bindir}/chromium-browser
# make sure some environment variables that can alter behavior are not set
unset \
    DISPLAY \
    WWW_MECHANIZE_CHROME_TRANSPORT \
    WWW_MECHANIZE_CHROME_CONNECTION_STYLE \
    TEST_LOG_LEVEL \
    TEST_WWW_MECHANIZE_CHROME_INSTANCE \
    TEST_WWW_MECHANIZE_CHROME_VERSIONS
%if %{with debug_tests}
export TEST_LOG_LEVEL=debug
%endif

# skip tests that use the Internet
%if %{without network_tests}
for tst in \
    t/50-mech-content-nonhtml.t \
    t/62-networkstatus.t \
    ; do
        echo 'use Test::More skip_all => "no network access"' > $tst
done
%endif

make test

%files
%doc Changes README examples
# note: files all say perl_5 which is GPLv1/Artistic but file is Artistic-2
# https://github.com/Corion/WWW-Mechanize-Chrome/issues/80
#license LICENSE
%{perl_vendorlib}/Chrome
%{perl_vendorlib}/HTTP/Cookies/Chrome*
%{perl_vendorlib}/WWW/Mechanize/Chrome*
%{_mandir}/man3/Chrome*
%{_mandir}/man3/HTTP::Cookies::Chrome*
%{_mandir}/man3/WWW::Mechanize::Chrome*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Chris Adams <linux@cmadams.net> 0.73-3
- tests run Chromium headless, so don't need X virtual framebuffer
- make tests conditional, due to being as much a a test of Chrome as of
  the module (and there's an issue with Chrome right now as of 125/126)

* Mon May 27 2024 Chris Adams <linux@cmadams.net> 0.73-2
- remove copyrighted webpages from tests

* Sun May 19 2024 Chris Adams <linux@cmadams.net> 0.73-1
- new version

* Fri Mar 08 2024 Chris Adams <linux@cmadams.net> 0.72-4
- additional spec file cleanups

* Thu Feb 01 2024 Chris Adams <linux@cmadams.net> 0.72-3
- additional spec file cleanups

* Sat Jan 20 2024 Chris Adams <linux@cmadams.net> 0.72-2
- spec file cleanups

* Sat Nov 25 2023 Chris Adams <linux@cmadams.net> 0.72-1
- initial package
