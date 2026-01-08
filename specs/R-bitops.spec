Name:           R-bitops
Version:        %R_rpm_version 1.0-9
Release:        %autorelease
Summary:        Functions for Bitwise operations

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Functions for Bitwise operations on integer vectors.

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
