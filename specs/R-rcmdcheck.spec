Name:           R-rcmdcheck
Version:        %R_rpm_version 1.4.0
Release:        %autorelease
Summary:        Run 'R CMD check' from 'R' and Capture Results

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Run 'R CMD check' from 'R' and capture the results of the individual checks.
Supports running checks in the background, timeouts, pretty printing and
comparing check results.

%prep
%autosetup -c
# Fix test
sed -i 's/bad3, tempfile(), character()/bad3, tempfile(), "--no-build-vignettes"/' \
    rcmdcheck/tests/testthat/test-build.R

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
