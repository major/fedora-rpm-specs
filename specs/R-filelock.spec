Name:           R-filelock
Version:        %R_rpm_version 1.0.3
Release:        %autorelease
Summary:        Portable File Locking

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Place an exclusive or shared lock on a file. It uses 'LockFile' on Windows and
'fcntl' locks on Unix-like systems.

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
