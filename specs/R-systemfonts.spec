Name:           R-systemfonts
Version:        %R_rpm_version 1.3.1
Release:        %autorelease
Summary:        System Native Font Finding

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
Obsoletes:      %{name}-devel <= 1.3.1

%description
Provides system native access to the font catalogue. As font handling
varies between systems it is difficult to correctly locate installed fonts
across different operating systems. The 'systemfonts' package provides
bindings to the native libraries on Windows, macOS and Linux for finding
font files that can then be used further by e.g. graphic devices. The main
use is intended to be from compiled code but 'systemfonts' also provides
access from R.

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
