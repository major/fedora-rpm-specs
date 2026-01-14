Name:           R-tmvnsim
Version:        %R_rpm_version 1.0-2
Release:        %autorelease
Summary:        Truncated Multivariate Normal Simulation

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Importance sampling from the truncated multivariate normal using the GHK
(Geweke-Hajivassiliou-Keane) simulator. Unlike Gibbs sampling which can get
stuck in one truncation sub-region depending on initial values, this package
allows truncation based on disjoint regions that are created by truncation of
absolute values. The GHK algorithm uses simple Cholesky transformation followed
by recursive simulation of univariate truncated normals hence there are also no
convergence issues. Importance sample is returned along with sampling weights,
based on which, one can calculate integrals over truncated regions for
multivariate normals.

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
