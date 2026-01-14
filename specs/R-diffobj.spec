Name:           R-diffobj
Version:        %R_rpm_version 0.3.6
Release:        %autorelease
Summary:        Diffs for R Objects

License:        GPL-2.0-only OR GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Generate a colorized diff of two R objects for an intuitive visualization
of their differences.

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
