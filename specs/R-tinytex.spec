Name:           R-tinytex
Version:        %R_rpm_version 0.58
Release:        %autorelease
Summary:        Helper Functions to Install and Maintain TeX Live, and Compile LaTeX Documents

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Helper functions to install and maintain the 'LaTeX' distribution named
'TinyTeX' (<https://yihui.org/tinytex/>), a lightweight, cross-platform,
portable, and easy-to-maintain version of 'TeX Live'. This package also
contains helper functions to compile 'LaTeX' documents, and install missing
'LaTeX' packages automatically.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
