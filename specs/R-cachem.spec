Name:           R-cachem
Version:        %R_rpm_version 1.1.0
Release:        %autorelease
Summary:        Cache R Objects with Automatic Pruning

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  R-devel

%description
Key-value stores with automatic pruning. Caches can limit either their total
size or the age of the oldest object (or both), automatically pruning objects
to maintain the constraints.

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
