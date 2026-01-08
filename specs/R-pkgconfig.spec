Name:           R-pkgconfig
Version:        %R_rpm_version 2.0.3
Release:        %autorelease
Summary:        Private Configuration for 'R' Packages

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Set configuration options on a per-package basis. Options set by a given
package only apply to that package, other packages are unaffected.

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
