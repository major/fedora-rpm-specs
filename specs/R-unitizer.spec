Name:           R-unitizer
Version:        %R_rpm_version 1.4.23
Release:        %autorelease
Summary:        Interactive R Unit Tests

License:        GPL-2.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Simplifies regression tests by comparing objects produced by test code with
earlier versions of those same objects. If objects are unchanged the tests
pass, otherwise execution stops with error details. If in interactive mode,
tests can be reviewed through the provided interactive environment.

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
