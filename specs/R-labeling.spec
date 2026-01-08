Name:           R-labeling
Version:        %R_rpm_version 0.4.3
Release:        %autorelease
Summary:        Axis Labeling

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Functions which provide a range of axis labeling algorithms.

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
