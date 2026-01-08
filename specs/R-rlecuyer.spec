Name:           R-rlecuyer
Version:        %R_rpm_version 0.3-8
Release:        %autorelease
Summary:        R interface to RNG with multiple streams

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Provides an interface to the C implementation of the random number 
generator with multiple independent streams developed by L'Ecuyer 
et al (2002). The main purpose of this package is to enable the 
use of this random number generator in parallel R applications.  

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
