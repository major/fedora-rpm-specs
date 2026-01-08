Name:           R-waveslim
Version:        %R_rpm_version 1.8.4
Release:        %autorelease
Summary:        R module, Basic wavelet routines for 1,2 and 3-dimensional signal processing

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Basic wavelet routines for time series (1D), image (2D)
and array (3D) analysis.  The code provided here is based on
wavelet methodology developed in Percival and Walden (2000);
Gencay, Selcuk and Whitcher (2001); the dual-tree complex wavelet
transform (CWT) from Kingsbury (1999, 2001) as implemented by
Selesnick; and Hilbert wavelet pairs (Selesnick 2001, 2002).  All
figures in chapters 4-7 of GSW (2001) are reproducible using this
package and R code available at the book website(s) below.

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
