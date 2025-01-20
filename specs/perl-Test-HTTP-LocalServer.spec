Name:           perl-Test-HTTP-LocalServer
Version:        0.76
Release:        3%{?dist}
Summary:        Spawn a local HTTP server for testing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Test-HTTP-LocalServer/
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CORION/Test-HTTP-LocalServer-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make perl-interpreter perl-generators coreutils
BuildRequires:  perl(CGI)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTTP::Daemon) >= 6.05
BuildRequires:  perl(HTTP::Request::AsCGI)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Tiny)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::IP) >= 0.25
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Pod::Markdown)
BuildRequires:  perl(Socket)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# some runtime deps are missed
Requires:       perl(POSIX)
# - log-server is included but not .pm or executable
Requires:       perl(CGI)
Requires:       perl(Getopt::Long)
Requires:       perl(HTTP::Daemon)
Requires:       perl(HTTP::Request::AsCGI)
Requires:       perl(Socket)
Requires:       perl(Time::HiRes)
Requires:       perl(URI)
Requires:       perl(strict)

%description
This module implements a tiny web server suitable for running "live" tests
of HTTP clients against it. It also takes care of cleaning %%ENV from
settings that influence the use of a local proxy etc.

%prep
%setup -q -n Test-HTTP-LocalServer-%{version}
perl -pi -e 's/\r//' lib/Test/HTTP/cookie-server

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
# https://github.com/Corion/Test-HTTP-LocalServer/issues/7
#%license LICENSE
%{perl_vendorlib}/Test/HTTP/*
%{_mandir}/man3/Test::HTTP::LocalServer*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.76-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 08 2024 Chris Adams <linux@cmadams.net> 0.76-1
- update to new version
- additional spec file cleanups

* Thu Feb 01 2024 Chris Adams <linux@cmadams.net> 0.75-3
- additional spec file cleanups

* Sat Jan 20 2024 Chris Adams <linux@cmadams.net> 0.75-2
- spec file cleanups

* Mon Nov 20 2023 Chris Adams <linux@cmadams.net> 0.75-1
- initial package
