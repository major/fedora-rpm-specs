Name:           R-RcppDate
Version:        %R_rpm_version 0.0.6
Release:        %autorelease
Summary:        'date' C++ Header Library for Date and Time Functionality

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 0.0.6

# This does not appear to be the same version as in Fedora, but I'm not sure
# what version exactly.
# https://github.com/eddelbuettel/rcppdate/issues/2
Provides:       bundled(date)

%description
A header-only C++ library is provided with support for dates, time zones,
ISO weeks, Julian dates, and Islamic dates. 'date' offers extensive date
and time functionality for the C++11, C++14 and C++17 standards and was
written by Howard Hinnant and released under the MIT license. A slightly
modified version has been accepted (along with 'tz.h') as part of C++20.
This package regroups all header files from the upstream repository by
Howard Hinnant so that other R packages can use them in their C++ code. At
present, few of the types have explicit 'Rcpp' wrappers though these may be
added as needed.

%prep
%autosetup -c

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
