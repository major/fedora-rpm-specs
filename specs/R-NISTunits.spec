Name:           R-NISTunits
Version:        %R_rpm_version 1.0.1
Release:        %autorelease
Summary:        Fundamental Physical Constants and Unit Conversions from NIST

License:        GPL-3.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Fundamental physical constants (Quantity, Value, Uncertainty, Unit) for SI
(International System of Units) and non-SI units, plus unit conversions. Based
on the data from NIST (National Institute of Standards and Technology, USA)

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
