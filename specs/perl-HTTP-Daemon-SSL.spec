Name:           perl-HTTP-Daemon-SSL
Version:        1.04
Release:        %autorelease
Summary:        Simple http server class with SSL support
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTTP-Daemon-SSL
Source0:        https://cpan.metacpan.org/modules/by-module/HTTP/HTTP-Daemon-SSL-%{version}.tar.gz
# Adapt tests to IO::Socket::SSL 1.80, CPAN RT#81932
Patch0:         HTTP-Daemon-SSL-1.04-Adapt-tests-to-IO-Socket-SSL-1.80.patch
# Do not test weak keys with OpenSSL 1.0.1, bug #1058728, CPAN RT#88998
Patch1:         HTTP-Daemon-SSL-1.04-Generate-keys-and-certificates-at-test-time.patch

BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Daemon) >= 1
BuildRequires:  perl(IO::Socket::SSL) >= 0.93
BuildRequires:  perl(IO::Socket::SSL::Utils)

Requires:       perl(HTTP::Daemon) >= 1
Requires:       perl(IO::Socket::SSL) >= 0.93

%description
Instances of the HTTP::Daemon::SSL class are HTTP/1.1 servers that listen
on a socket for incoming requests. The HTTP::Daemon::SSL is a sub-class of
IO::Socket::SSL, so you can perform socket operations directly on it too.

%prep
%setup -q -n HTTP-Daemon-SSL-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc BUGS Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/HTTP::Daemon::SSL.3pm*

%changelog
%autochangelog
