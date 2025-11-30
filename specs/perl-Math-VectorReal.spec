%bcond check 1

Name:           perl-Math-VectorReal
Version:        1.02
Release:        %autorelease
Summary:        Module to handle 3D Vector Mathematics
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Math-VectorReal
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANTHONY/Math-VectorReal-%{version}.tar.gz
# fix tests
Patch0:         %{name}-tests.patch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
%if %{with check}
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Math::MatrixReal)
%endif
BuildArch:      noarch

%description
The Math::VectorReal package defines a 3D mathematical "vector", in a
way that is compatible with the previous CPAN module Math::MatrixReal.
However it provides a more vector oriented set of mathematical functions
and overload operators, to the MatrixReal package. For example the
normal perl string functions "x" and "." have been overloaded to allow
vector cross and dot product operations. Vector math formula thus looks
like vector math formula in perl programs using this package.

%prep
%autosetup -p1 -n Math-VectorReal-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" \
  NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} '%{buildroot}'/*
# do not include test scripts in the final package
rm -v %{buildroot}%{perl_vendorlib}/Math/{{matrix,vector}_test,synopsis}.pl

%if %{with check}
%check
make test
%endif

%files
%doc README
%dir %{perl_vendorlib}/Math
%{perl_vendorlib}/Math/VectorReal.pm
%{_mandir}/man3/Math::VectorReal.3pm.*

%changelog
%autochangelog
