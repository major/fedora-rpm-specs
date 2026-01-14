Name:           R-RColorBrewer
Version:        %R_rpm_version 1.1-3
Release:        %autorelease
Summary:        ColorBrewer Palettes

License:        Apache-2.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides color schemes for maps (and other graphics) designed by Cynthia
Brewer as described at http://colorbrewer2.org

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
