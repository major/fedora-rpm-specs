Name:           R-vctrs
Version:        %R_rpm_version 0.6.5
Release:        %autorelease
Summary:        Vector Helpers

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}
# https://github.com/r-lib/vctrs/issues/1353
Patch:          0001-Skip-some-tests-on-big-endian-machines.patch

BuildRequires:  R-devel
Obsoletes:      %{name}-devel <= 0.6.5

%description
Defines new notions of prototype and size that are used to provide tools for
consistent and well-founded type-coercion and size-recycling, and are in turn
connected to ideas of type- and size-stability useful for analysing function
interfaces.

%prep
%autosetup -c -p1

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
