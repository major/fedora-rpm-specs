Name:           R-acepack
Version:        %R_rpm_version 1.6.3
Release:        %autorelease
Summary:        ACE and AVAS methods for choosing regression transformations

# Automatically converted from old format: Public Domain and MIT - review is highly recommended.
License:        LicenseRef-Callaway-Public-Domain AND LicenseRef-Callaway-MIT
URL:            %{cran_url}
Source:         %{cran_source}
Source:         ace-copyright.txt

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
ACE and AVAS (additivity and variance stabilization) are used to estimate 
transformations for regression.

%prep
%autosetup -c
mkdir -p acepack/inst
cp %{SOURCE1} acepack/inst/NOTICE.txt

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
