Name:           R-sessioninfo
Version:        %R_rpm_version 1.2.3
Release:        %autorelease
Summary:        R Session Information

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Query and print information about the current R session. It is similar to
'utils::sessionInfo()', but includes more information about packages, and where
they were installed from.

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
