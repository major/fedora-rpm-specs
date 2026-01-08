Name:           R-fortunes
Version:        %R_rpm_version 1.5-4
Release:        %autorelease
Summary:        R Fortunes

# Automatically converted from old format: GPLv2 or GPLv3 - review is highly recommended.
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A collection of fortunes from the R community.

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
