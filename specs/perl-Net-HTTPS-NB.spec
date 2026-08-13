Name:           perl-Net-HTTPS-NB
Version:        0.16
Release:        %{autorelease}
Summary:        Non-blocking HTTPS client for Perl
URL:            https://metacpan.org/dist/Net-HTTPS-NB
Source0:        https://cpan.metacpan.org/authors/id/O/OL/OLEG/Net-HTTPS-NB-%{version}.tar.gz

# "This library is free software; you can redistribute it and/or modify
# it under the same terms as Perl itself."
# https://github.com/olegwtf/p5-Net-HTTPS-NB/issues/3
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

BuildArch:      noarch
BuildRequires:  /usr/bin/chmod
BuildRequires:  make
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(IO::Socket::SSL) >= 0.98
BuildRequires:  perl(Net::HTTP)
BuildRequires:  perl(Net::HTTPS)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

%{?perl_default_filter}

%description
Same interface as Net::HTTPS but it will never try multiple reads when the
read_response_headers() or read_entity_body() methods are invoked. In addition
allows non-blocking connect.


%prep
%autosetup -n Net-HTTPS-NB-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%license Artistic
%license Copying
%doc Changes
%doc README
%doc examples/google_multi.pl
%{_mandir}/man3/Net::HTTPS::NB.3pm*
%dir %{perl_vendorlib}/Net/HTTPS
%{perl_vendorlib}/Net/HTTPS/NB.pm


%changelog
%{autochangelog}
