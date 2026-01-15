Name:           R-reshape2
Version:        %R_rpm_version 1.4.5
Release:        %autorelease
Summary:        Flexibly Reshape Data: A Reboot of the Reshape Package

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Flexibly restructure and aggregate data using just two functions: melt and
'dcast' (or 'acast').

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
