Name:           perl-ExtUtils-LibBuilder
Version:        0.09
Release:        %autorelease
Summary:        Perl library to build C libraries and programs
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ExtUtils-LibBuilder
Source0:        https://cpan.metacpan.org/authors/id/A/AM/AMBS/ExtUtils-LibBuilder-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.23
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(Test::More)

%description
Some Perl modules need to ship C libraries together with their Perl code.
Although there are mechanisms to compile and link (or glue) C code in your
Perl programs, there was not a clear method to compile standard,
self-contained C libraries.  This module helps in that task.

%prep
%setup -q -n ExtUtils-LibBuilder-%{version}

%build
perl Build.PL installdirs=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
