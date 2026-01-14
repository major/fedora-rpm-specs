Name:           R-gsl
Version:        %R_rpm_version 2.1-9
Release:        %autorelease
Summary:        Wrapper for the Gnu Scientific Library

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel
BuildRequires:  gsl-devel >= 2.1

%description
An R wrapper for some of the functionality of the Gnu Scientific Library.

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
