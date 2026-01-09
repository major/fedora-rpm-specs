Name:           R-munsell
Version:        %R_rpm_version 0.5.1
Release:        %autorelease
Summary:        Utilities for Using Munsell Colours

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides easy access to, and manipulation of, the Munsell colours.
Provides a mapping between Munsell's original notation (e.g. "5R 5/10")
and hexadecimal strings suitable for use directly in R graphics. Also
provides utilities to explore slices through the Munsell colour tree, to
transform Munsell colours and display colour palettes.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
