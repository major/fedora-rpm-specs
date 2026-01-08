Name:           R-measurements
Version:        %R_rpm_version 1.5.1
Release:        %autorelease
Summary:        Tools for Units of Measurement

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Collection of tools to make working with physical measurements easier. Convert
between metric and imperial units, or calculate a dimension's unknown value
from other dimensions' measurements.

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
