Name:           R-mAr
Version:        %R_rpm_version 1.2-0
Release:        %autorelease
Summary:        R module to evaluate functions for multivariate AutoRegressive analysis

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
R package:
An R add-on package for estimation of multivariate AR models through a
computationally-efficient stepwise least-squares algorithm (Neumaier
and Schneider, 2001); the procedure is of particular interest for
high-dimensional data without missing values such as geophysical
fields.

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
