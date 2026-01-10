Name:           R-testthat
Version:        %R_rpm_version 3.3.1
Release:        %autorelease
Summary:        Unit Testing for R

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
A unit testing system designed to be fun, flexible, and easy to set up.

%prep
%autosetup -c
rm -f testthat/tests/testthat/test-expect-known.R # unconditional suggest, should be fixed

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
