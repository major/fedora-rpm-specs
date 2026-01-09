Name:           R-reshape
Version:        %R_rpm_version 0.8.10
Release:        %autorelease
Summary:        Flexibly Reshape Data

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Flexibly restructure and aggregate data using just two functions: melt and
cast.

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
