Name:           R-rappdirs
Version:        %R_rpm_version 0.3.3
Release:        %autorelease
Summary:        Application Directories: Determine Where to Save Data, Caches, and Logs

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
An easy way to determine which directories on the users computer you should
use to save data, caches and logs. A port of Python's 'Appdirs'
(<https://github.com/ActiveState/appdirs>) to R.

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
