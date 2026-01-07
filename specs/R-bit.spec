Name:           R-bit
Version:        %R_rpm_version 4.6.0
Release:        %autorelease
Summary:        Classes and Methods for Fast Memory-Efficient Boolean Selections

# Automatically converted from old format: GPLv2 or GPLv3 - review is highly recommended.
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Provided are classes for boolean and skewed boolean vectors, fast boolean
methods, fast unique and non-unique integer sorting, fast set operations on
sorted and unsorted sets of integers, and foundations for ff (range index,
compression, chunked processing).

%prep
%autosetup -c
rm -f bit/tests/ff_tests.R # unconditional suggest, should be fixed

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
