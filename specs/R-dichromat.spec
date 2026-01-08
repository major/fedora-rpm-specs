Name:           R-dichromat
Version:        %R_rpm_version 2.0-0.1
Release:        %autorelease
Summary:        Color Schemes for Dichromats

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Collapse red-green or green-blue distinctions to simulate the effects of
different types of color-blindness.

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
