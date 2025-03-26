# -*- rpm-spec -*-

%define metacpan https://cpan.metacpan.org/authors/id/J/JV/JV
%define FullName Text-Layout

Name: perl-%{FullName}
Summary: Pango style text formatting
License: (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Artistic-2.0
Version: 0.039
Release: %autorelease
Source: %{metacpan}/%{FullName}-%{version}.tar.gz
Url: https://metacpan.org/release/%{FullName}

# It's all plain perl, nothing architecture dependent.
BuildArch: noarch

# This package would provide many (perl) modules, but these are
# not intended for general use.
%global __requires_exclude Text::Layout::Font(Config|Descriptor)
%global __provides_exclude_from /(Testing|Cairo|Pango|PDFAPI2|ImageElement|ElementRole)\\.pm$

Requires: perl(:VERSION) >= 5.26.0

Recommends: perl(PDF::API2) >= 2.036
Recommends: perl(HarfBuzz::Shaper) >= 0.026

BuildRequires: make
BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker) >= 7.24
BuildRequires: perl(Object::Pad) >= 0.78
BuildRequires: perl(File::Basename)
BuildRequires: perl(HarfBuzz::Shaper) >= 0.026
BuildRequires: perl(PDF::API2) >= 2.036
BuildRequires: perl(Test::More)
BuildRequires: perl(constant)
BuildRequires: perl(overload)
BuildRequires: perl(strict)
BuildRequires: perl(utf8)
BuildRequires: perl(warnings)
BuildRequires: perl-generators
BuildRequires: perl-interpreter

%description
Text::Layout provides methods for Pango style text formatting. Where
possible the methods have identical names and (near) identical
behavior as their Pango counterparts.

See https://developer.gnome.org/pango/stable/pango-Layout-Objects.html.

Text::Layout uses backend modules to render the marked up text.
Backends are included for PDF::API2 and PDF::Builder.

The package uses Text::Layout::FontConfig (included) to organize fonts
by description.

If module HarfBuzz::Shaper is installed, Text::Layout can use it for
text shaping.

%prep
%setup -q -n %{FullName}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%check
make test

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%files
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%autochangelog
