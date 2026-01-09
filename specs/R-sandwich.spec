Name:           R-sandwich
Version:        %R_rpm_version 3.1-1
Release:        %autorelease
Summary:        Robust Covariance Matrix Estimators

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Model-robust standard error estimators for cross-sectional, time series
and longitudinal data.

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
