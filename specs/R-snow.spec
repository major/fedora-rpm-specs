Name:           R-snow
Version:        %R_rpm_version 0.4-4
Release:        %autorelease
Summary:        Simple Network of Workstations

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Support for simple parallel computing in R.

%prep
%autosetup -c
chmod -x snow/inst/RMPInode.R
rm -rf snow/inst/*.bat # do not need on Linux

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
