Name:           R-gmp
Version:        %R_rpm_version 0.7-5
Release:        %autorelease
Summary:        Multiple Precision Arithmetic

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  gmp-devel >= 4.2.3

%description
Multiple Precision Arithmetic (big integers and rationals, prime number
tests, matrix computation), "arithmetic without limitations" using the C
library GMP (GNU Multiple Precision Arithmetic).

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
