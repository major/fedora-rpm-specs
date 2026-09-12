Name:		perl-Params-SomeUtil
Version:	1.11
Release:	1%{?dist}
Summary:	Simple, compact and correct param-checking functions
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Params-SomeUtil
Source0:	https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Params-SomeUtil-%{version}.tar.gz
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(:VERSION) >= 5.6
BuildRequires:	perl(Config)
BuildRequires:	perl(ExtUtils::CBuilder) >= 0.27
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:	perl(File::Spec) >= 0.80
BuildRequires:	perl(File::Temp)
# Module
BuildRequires:	perl(DynaLoader)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(overload)
BuildRequires:	perl(Scalar::Util) >= 1.18
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
# Test Suite
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(warnings)
# Dependencies
# (none)

# Sub _alt_hook in SomeUtil.pm has a fake provide for Params::Util 1.07,
# which really confuses the provides generator.
%global __provides_exclude ^(perl\\(Params::(Some)?Util\\))
Provides:	perl(Params::SomeUtil) = %{version}

%description
Params::SomeUtil provides a basic set of importable functions that makes
checking parameters much easier. This module is a fork of version 1.07 of
Params::Util with some additional bug fixes.

While they can be (and are) used in other contexts, the main point behind this
module is that the functions both Do What You Mean, and Do The Right Thing, so
they are most useful when you are getting params passed into your code from
someone and/or somewhere else and you can't really trust the quality.  Thus,
Params::SomeUtil is of most use at the edges of your API, where params and data
are coming in from outside your code.

The functions provided by Params::SomeUtil check in the most strictly correct
manner known, are documented as thoroughly as possible so their exact behavior
is clear, and heavily tested so make sure they are not fooled by weird data and
Really Bad Things.

%prep
%setup -q -n Params-SomeUtil-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
unset PERL_PARAMS_UTIL_PP
unset PERL_PARAMS_SOMEUTIL_PP
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/Params/
%{perl_vendorarch}/Params/
%{_mandir}/man3/Params::SomeUtil.3*

%changelog
* Fri Sep 11 2026 Paul Howarth <paul@city-fan.org> - 1.11-1
- Update to 1.11
  - Updated FSF address
  - Updated WHY section to document new differences with Params::Util; none of
    them are functional - three functions were added to a development release
- Incorporate feedback from package review (rhbz#2529191):
  - Bump required Scalar::Util version to 1.18
  - Require at least perl version 5.6 (Makefile.PL has require 5.00503)
  - Test::More version requirement left at 0.88 since tests use done_testing
  - Unset PERL_PARAMS_UTIL_PP and PERL_PARAMS_SOMEUTIL_PP environment variables
    in the %%check section to make the tests more reproducible
- BR: perl(ExtUtils::CBuilder) >= 0.27
- BR: perl(File::Spec) >= 0.80

* Sun Sep  6 2026 Paul Howarth <paul@city-fan.org> - 1.09-1
- Initial RPM version
