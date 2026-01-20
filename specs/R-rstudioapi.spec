Name:           R-rstudioapi
Version:        %R_rpm_version 0.18.0
Release:        %autorelease
Summary:        Safely Access the RStudio API

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Access the RStudio API (if available) and provide informative error
messages when it's not.

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
