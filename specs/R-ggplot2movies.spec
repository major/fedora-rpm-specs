Name:           R-ggplot2movies
Version:        %R_rpm_version 0.0.1
Release:        %autorelease
Summary:        Movies Data

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A dataset about movies. This was previously contained in ggplot2, but has been
moved its own package to reduce the download size of ggplot2.

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
