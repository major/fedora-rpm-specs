Name:           R-mvtnorm
Version:        %R_rpm_version 1.3-3
Release:        %autorelease
Summary:        Multivariate normal and T distribution R Package

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 1.3.3

%description
This R package computes multivariate normal and t probabilities, quantiles
and densities.

%prep
%autosetup -c
rm -f mvtnorm/tests/regtest-aperm.R # unconditional suggest, should be fixed

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
