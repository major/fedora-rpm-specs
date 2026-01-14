Name:           R-unix
Version:        %R_rpm_version 1.5.9
Release:        %autorelease
Summary:        POSIX System Utilities

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Bindings to system utilities found in most Unix systems such as POSIX functions
which are not part of the Standard C Library.

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
