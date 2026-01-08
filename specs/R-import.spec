Name:           R-import
Version:        %R_rpm_version 1.3.4
Release:        %autorelease
Summary:        An Import Mechanism for R

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Alternative mechanism for importing objects from packages and R modules.
The syntax allows for importing multiple objects with a single command in
an expressive way. The import package bridges some of the gap between using
library (or require) and direct (single-object) imports. Furthermore the
imported objects are not placed in the current environment.

%prep
%autosetup -c

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
