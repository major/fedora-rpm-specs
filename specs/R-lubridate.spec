Name:           R-lubridate
Version:        %R_rpm_version 1.9.4
Release:        %autorelease
Summary:        Make dealing with dates a little easier

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Functions to work with date-times and time-spans: fast and user friendly
parsing of date-time data, extraction and updating of components of a date-time
(years, months, days, hours, minutes, and seconds), algebraic manipulation on
date-time and time-span objects. The 'lubridate' package has a consistent and
memorable syntax that makes working with dates easy and fun.

%prep
%autosetup -c
rm -f lubridate/inst/cctz.sh # dev stuff
rm -f lubridate/tests/testthat/test-vctrs.R # unconditional suggest, should be fixed

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
