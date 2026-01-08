Name:           R-rprojroot
Version:        %R_rpm_version 2.1.1
Release:        %autorelease
Summary:        Finding Files in Project Subdirectories

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Robust, reliable and flexible paths to files below a project root. The
'root' of a project is defined as a directory that matches a certain
criterion, e.g., it contains a certain regular file.

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
