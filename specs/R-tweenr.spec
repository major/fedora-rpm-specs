Name:           R-tweenr
Version:        %R_rpm_version 2.0.3
Release:        %autorelease
Summary:        Interpolate Data for Smooth Animations

License:        MIT and WTFPL
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
In order to create smooth animation between states of data, tweening is
necessary. This package provides a range of functions for creating tweened
data that can be used as basis for animation. Furthermore it adds a number
of vectorized interpolaters for common R data types such as numeric, date
and colour.

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
