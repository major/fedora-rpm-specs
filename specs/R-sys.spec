Name:           R-sys
Version:        %R_rpm_version 3.4.3
Release:        %autorelease
Summary:        Powerful and Reliable Tools for Running System Commands in R

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Drop-in replacements for the base system2() function with fine control and
consistent behavior across platforms. Supports clean interruption, timeout,
background tasks, and streaming STDIN / STDOUT / STDERR over binary or text
connections. Arguments on Windows automatically get encoded and quoted to work
on different locales.

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
