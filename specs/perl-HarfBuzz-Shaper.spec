# -*- rpm-spec -*-

%define metacpan https://cpan.metacpan.org/authors/id/J/JV/JV
%define FullName HarfBuzz-Shaper

Name: perl-%{FullName}
Summary: Access to a small subset of the native HarfBuzz library
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License: GPL-1.0-or-later OR Artistic-1.0-Perl
Version: 0.033
Release: %autorelease
Source: %{metacpan}/%{FullName}-%{version}.tar.gz
Url: https://metacpan.org/release/%{FullName}


BuildRequires: coreutils findutils gcc make perl-devel
BuildRequires: harfbuzz-devel >= 1.7.7
BuildRequires: make
BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(Devel::CheckLib)
BuildRequires: perl(Encode)
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(Test::More)
BuildRequires: perl(XSLoader)
BuildRequires: perl(charnames)
BuildRequires: perl(lib)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter

%description
HarfBuzz::Shaper is a perl module that provides access to a small
subset of the native HarfBuzz library.

The subset is suitable for typesetting programs that need to deal with
complex languages like Devanagari.

This module is intended to be used with module L<Text::Layout>.

%prep
%setup -q -n %{FullName}-%{version}

%build
env INCHS=%{with hbinc} \
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test VERBOSE=1

%files
%doc Changes README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/HarfBuzz/Shaper.pm
%{_mandir}/man3/*

%changelog
%autochangelog
