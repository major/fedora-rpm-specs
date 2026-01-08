Name:           R-expm
Version:        %R_rpm_version 1.0-0
Release:        %autorelease
Summary:        Computation of the matrix exponential and related quantities

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Efficient calculation of the exponential of a matrix. The package
contains an R interface and a C API that package authors can use.

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
