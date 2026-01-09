Name:           R-multcomp
Version:        %R_rpm_version 1.4-29
Release:        %autorelease
Summary:        Simultaneous inference for general linear hypotheses R Package

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
This R package contains functions for simultaneous tests and confidence
intervals for general linear hypotheses in parametric models, including
linear, generalized linear, linear mixed effects, and survival models.

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
