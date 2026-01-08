Name:           R-polynom
Version:        %R_rpm_version 1.4-1
Release:        %autorelease
Summary:        A Class for Univariate Polynomial Manipulations

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A collection of functions to implement a class for univariate polynomial
manipulations.

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
