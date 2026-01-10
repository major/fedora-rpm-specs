Name:           R-gpx
Version:        %R_rpm_version 1.1.0
Release:        %autorelease
Summary:        Process GPX Files into R Data Structures

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Process open standard GPX files into data.frames
for further use and analysis in R.

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
