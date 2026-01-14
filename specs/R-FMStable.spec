Name:           R-FMStable
Version:        %R_rpm_version 0.1-4
Release:        %autorelease
Summary:        Finite Moment Stable Distributions

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
This package implements some basic procedures for dealing with log
maximally skew stable distributions, which are also called finite moment
log stable distributions.

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
