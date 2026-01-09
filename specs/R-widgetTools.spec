Name:           R-widgetTools
Version:        %R_rpm_version 1.88.0
Release:        %autorelease
Summary:        Bioconductor tools to support tcltk widgets

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{bioc_url}
Source:         %{bioc_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
This package contains tools to support the construction of tcltk widgets.
This library is part of the bioconductor (bioconductor.org) project

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
