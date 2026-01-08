Name:           R-RODBC
Version:        %R_rpm_version 1.3-26.1
Release:        %autorelease
Summary:        An ODBC database interface for R

# Automatically converted from old format: GPLv2 or GPLv3 - review is highly recommended.
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  unixODBC-devel

%description
An ODBC database interface for R.

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
