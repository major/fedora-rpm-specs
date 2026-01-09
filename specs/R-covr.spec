Name:           R-covr
Version:        %R_rpm_version 3.6.5
Release:        %autorelease
Summary:        Test Coverage for Packages

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

Provides:       bundled(xstatic-bootstrap-common) = 3.3.5
Provides:       bundled(js-highlight) = 6.2

%description
Track and report code coverage for your package and (optionally) upload the
results to a coverage service like 'Codecov' <https://codecov.io> or
'Coveralls' <https://coveralls.io>. Code coverage is a measure of the amount of
code being exercised by a set of tests. It is an indirect measure of test
quality and completeness. This package is compatible with any testing
methodology or framework and tracks coverage of both R code and compiled
C/C++/FORTRAN code.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
