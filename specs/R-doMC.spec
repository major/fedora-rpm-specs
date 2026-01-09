Name:           R-doMC
Version:        %R_rpm_version 1.3.8
Release:        %autorelease
Summary:        Foreach Parallel Adaptor for 'parallel'

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides a parallel backend for the %%dopar%% function using the multicore
functionality of the parallel package.

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
