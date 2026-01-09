Name:           R-zip
Version:        %R_rpm_version 2.3.3
Release:        %autorelease
Summary:        Cross-Platform 'zip' Compression

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Cross-Platform 'zip' Compression Library. A replacement for the 'zip'
function, that does not require any additional external tools on any
platform.

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
