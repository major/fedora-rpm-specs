Name:           R-bindrcpp
Version:        %R_rpm_version 0.2.3
Release:        %autorelease
Summary:        An 'Rcpp' Interface to Active Bindings

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 0.2.3

%description
Provides an easy way to fill an environment with active bindings that call
a C++ function.

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
