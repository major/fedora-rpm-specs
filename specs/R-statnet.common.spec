Name:           R-statnet.common
Version:        %R_rpm_version 4.13.0
Release:        %autorelease
Summary:        Common R Scripts and Utilities Used by the Statnet Project Software

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Non-statistical utilities used by the software developed by the Statnet
Project. They may also be of use to others.

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
