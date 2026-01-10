Name:           R-bslib
Version:        %R_rpm_version 0.9.0
Release:        %autorelease
Summary:        Custom Bootstrap Sass Themes for shiny and rmarkdown

# Automatically converted from old format: MIT and BSD - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Simplifies custom CSS styling of both shiny and rmarkdown via Bootstrap Sass.
Supports both Bootstrap 3 and 4 as well as their various Bootswatch themes. An
interactive widget is also provided for previewing themes in real time.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
