Name:           R-praise
Version:        %R_rpm_version 1.0.0
Release:        %autorelease
Summary:        Praise Users

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Build friendly R packages that praise their users if they have done something
good, or they just need it to feel better.

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
