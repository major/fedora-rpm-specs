Name:           R-quantities
Version:        %R_rpm_version 0.2.3
Release:        %autorelease
Summary:        Quantity Calculus for R Vectors

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Integration of the 'units' and 'errors' packages for a complete quantity
calculus system for R vectors, matrices and arrays, with automatic
propagation, conversion, derivation and simplification of magnitudes and
uncertainties.
Documentation about 'units' and 'errors' is provided in the papers by Pebesma,
Mailund & Hiebert (2016, <doi:10.32614/RJ-2016-061>) and by Ucar, Pebesma &
Azcorra (2018, <doi:10.32614/RJ-2018-075>), included in those packages as
ignettes; see 'citation("quantities")' for details.

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
