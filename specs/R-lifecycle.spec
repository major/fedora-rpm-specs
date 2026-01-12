Name:           R-lifecycle
Version:        %R_rpm_version 1.0.5
Release:        %autorelease
Summary:        Manage the Life Cycle of your Package Functions

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Manage the life cycle of your exported functions with shared conventions,
documentation badges, and user-friendly deprecation warnings.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
