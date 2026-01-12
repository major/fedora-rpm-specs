Name:           R-RcppCCTZ
Version:        %R_rpm_version 0.2.14
Release:        %autorelease
Summary:        'Rcpp' Bindings for the 'CCTZ' Library

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  cctz-devel
Requires:       cctz-devel
Obsoletes:      %{name}-devel <= 0.2.13

%description
'Rcpp' Access to the 'CCTZ' timezone library is provided. 'CCTZ' is a C++
library for translating between absolute and civil times using the rules of a
time zone.

%prep
%autosetup -c
# Remove bundled cctz.
rm -r RcppCCTZ/inst/include/cctz
rm RcppCCTZ/src/time_zone_*.{cc,h}
rm RcppCCTZ/src/{civil_time_detail,zone_info_source}.cc
echo "PKG_LIBS = -lcctz" > RcppCCTZ/src/Makevars

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
