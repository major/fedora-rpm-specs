# -*- rpm-spec -*-

%define metacpan https://cpan.metacpan.org/authors/id/J/JV/JV
%define FullName File-LoadLines

Name: perl-%{FullName}
Summary: Loads the contents of a text file into an array of lines
License: GPL-1.0-or-later OR Artistic-1.0-Perl
Version: 1.047
Release: %autorelease
Source: %{metacpan}/%{FullName}-%{version}.tar.gz
Url: https://metacpan.org/release/%{FullName}

# It's all plain perl, nothing architecture dependent.
BuildArch: noarch

Requires: perl(:VERSION) >= 5.10.1

BuildRequires: coreutils
BuildRequires: make
BuildRequires: perl(Carp)
BuildRequires: perl(Encode)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(LWP::Protocol::https)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(base)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter

%description
File-LoadLines provides an easy way to load the contents of a 
disk file or network resource into your program.

It can deliver the contents without touching (as a blob) but its most
useful purpose is to deliver the contents of text data into an array
of lines. Hence the name, File::LoadLines.

It automatically handles data encodings ASCII, Latin and UTF-8 text.
When the file has a BOM, it handles UTF-8, UTF-16 LE and BE, and
UTF-32 LE and BE.

Recognized line terminators are NL (Unix, Linux), CRLF (DOS, Windows)
and CR (Mac)

%prep
%setup -q -n %{FullName}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%check
make test VERBOSE=1

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%autochangelog
