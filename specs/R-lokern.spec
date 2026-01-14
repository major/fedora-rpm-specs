Name:           R-lokern
Version:        %R_rpm_version 1.1-12
Release:        %autorelease
Summary:        Kernel Regression Smoothing with Local or Global Plug-in Bandwidth

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Kernel regression smoothing with adaptive local or global plug-in bandwidth
selection.

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
