Name:           perl-Devel-StackTrace-Extract
Version:        1.000000
Release:        3%{?dist}
Summary:        Extract a stack trace from an exception object
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Devel-StackTrace-Extract
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MAXMIND/Devel-StackTrace-Extract-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Devel::StackTrace::Frame)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(warnings)
# Tests
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(Mojo::Exception)
BuildRequires:  perl(Moose::Exception)
BuildRequires:  perl(StackTrace::Auto)
BuildRequires:  perl(Throwable::Error)


%description
It's popular to store stack traces in objects that are thrown as
exceptions, but, this being Perl, there's more than one way to do it. This
module provides a simple interface to attempt to extract the stack trace
from various well known exception classes that are on the CPAN.

%prep
%setup -q -n Devel-StackTrace-Extract-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/Devel/
%{_mandir}/man3/Devel::StackTrace::Extract.3pm*

%changelog
* Thu Jun 29 2023 Xavier Bachelot <xavier@bachelot.org> 1.000000-3
- More review fixes

* Wed Jun 28 2023 Xavier Bachelot <xavier@bachelot.org> 1.000000-2
- Review fixes

* Tue Jun 27 2023 Xavier Bachelot <xavier@bachelot.org> 1.000000-1
- Initial spec file
