Name:           R-modelr
Version:        %R_rpm_version 0.1.11
Release:        %autorelease
Summary:        Modelling Functions that Work with the Pipe

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Functions for modelling that help you seamlessly integrate modelling into a
pipeline of data manipulation and visualisation.

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
