Name:           R-poLCA
Version:        %R_rpm_version 1.6.0.1
Release:        %autorelease
Summary:        Polytomous variable Latent Class Analysis

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Latent class analysis and latent class regression models for polytomous
outcome variables.  Also known as latent structure analysis.

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
