Name:           R-pingr
Version:        %R_rpm_version 2.0.5
Release:        %autorelease
Summary:        Check if a Remote Computer is Up

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Check if a remote computer is up. It can either just call the system ping
command, or check a specified TCP port.

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
