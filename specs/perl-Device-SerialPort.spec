Name:           perl-Device-SerialPort
Version:        1.04
Release:        %autorelease
Summary:        Linux/POSIX emulation of Win32::SerialPort functions
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Device-SerialPort
Source0:        https://cpan.metacpan.org/authors/id/C/CO/COOK/Device-SerialPort-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
ExcludeArch:    %{ix86}

%description
This module provides an object-based user interface essentially identical
to the one provided by the Win32::SerialPort module.

%prep
%setup -q -n Device-SerialPort-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
                      TESTPORT=/dev/null
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

chmod -R u+rwX,go+rX,go-w $RPM_BUILD_ROOT/*

%check
# Can't do serial port tests in mock/build system
#make test

%files
%doc Changes README TODO
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Device*
%{_bindir}/modemtest
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
