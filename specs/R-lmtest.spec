Name:           R-lmtest
Version:        %R_rpm_version 0.9-40
Release:        %autorelease
Summary:        Testing Linear Regression Models for R

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
A collection of tests, data sets and examples for diagnostic checking in
linear regression models in R.

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
