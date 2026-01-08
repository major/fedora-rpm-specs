Name:           R-ps
Version:        %R_rpm_version 1.9.1
Release:        %autorelease
Summary:        List, Query, Manipulate System Processes

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
List, query and manipulate all system processes, on 'Windows', 'Linux' and
'macOS'.

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
