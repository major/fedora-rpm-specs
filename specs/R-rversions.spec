Name:           R-rversions
Version:        %R_rpm_version 3.0.0
Release:        %autorelease
Summary:        Query 'R' Versions, Including 'r-release' and 'r-oldrel'

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Query the main 'R' 'SVN' repository to find the versions 'r-release' and
'r-oldrel' refer to, and also all previous 'R' versions and their release
dates.

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
