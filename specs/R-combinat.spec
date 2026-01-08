Name:           R-combinat
Version:        %R_rpm_version 0.0-8
Release:        %autorelease
Summary:        R routines for combinatorics

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
R routines for combinatorics

%prep
%autosetup -c
[ -f combinat/NAMESPACE ] || echo 'exportPattern("^[^\\.]")' > combinat/NAMESPACE

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
