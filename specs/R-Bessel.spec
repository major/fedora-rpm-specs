Name:           R-Bessel
Version:        %R_rpm_version 0.7-0
Release:        %autorelease
Summary:        Computations and Approximations for Bessel Functions

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Computations for Bessel function for complex, real and partly 'mpfr'
(arbitrary precision) numbers; notably interfacing TOMS 644;
approximations for large arguments, experiments, etc.

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
