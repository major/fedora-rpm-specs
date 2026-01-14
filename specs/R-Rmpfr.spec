Name:           R-Rmpfr
Version:        %R_rpm_version 1.1-2
Release:        %autorelease
Summary:        R MPFR - Multiple Precision Floating-Point Reliable

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  gmp-devel
BuildRequires:  mpfr-devel

%description
Arithmetic (via S4 classes and methods) for arbitrary precision floating
point numbers, including transcendental ("special") functions.  To this
end, the package interfaces to the 'LGPL' licensed 'MPFR' (Multiple
Precision Floating-Point Reliable) Library which itself is based on the
'GMP' (GNU Multiple Precision) Library.

%prep
%autosetup -c
rm -f Rmpfr/tests/special-*.R # unconditional suggest, should be fixed

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
