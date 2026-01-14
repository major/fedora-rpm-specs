Name:           R-udunits2
Version:        %R_rpm_version 0.13.2.2
Release:        %autorelease
Summary:        Udunits-2 Bindings for R

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  udunits2-devel

%description
Provides simple bindings to Unidata's udunits library.

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
