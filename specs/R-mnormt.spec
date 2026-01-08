Name:           R-mnormt
Version:        %R_rpm_version 2.1.1
Release:        %autorelease
Summary:        The Multivariate Normal and t Distributions

# Automatically converted from old format: GPLv2 or GPLv3 - review is highly recommended.
License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Functions are provided for computing the density and the distribution function
of d-dimensional normal and "t" random variables, possibly truncated (on one
side or two sides), and for generating random vectors sampled from these
distributions, except sampling from the truncated "t". Moments of arbitrary
order of a multivariate truncated normal are computed, and converted to
cumulants up to order 4. Probabilities are computed via non-Monte Carlo
methods; different routines are used in the case d=1, d=2, d=3, d>3, if d
denotes the dimensionality.

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
