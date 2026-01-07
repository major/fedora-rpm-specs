Name:           R-crayon
Version:        %R_rpm_version 1.5.3
Release:        %autorelease
Summary:        Colored Terminal Output

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Colored terminal output on terminals that support 'ANSI' color and highlight
codes. It also works in 'Emacs' 'ESS'. 'ANSI' color support is automatically
detected. Colors and highlighting can be combined and nested. New styles can
also be created easily. This package was inspired by the 'chalk'
'JavaScript' project.

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
