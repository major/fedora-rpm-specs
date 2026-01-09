Name:           R-zeallot
Version:        %R_rpm_version 0.2.0
Release:        %autorelease
Summary:        Multiple, Unpacking, and Destructuring Assignment

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Provides a %<-% operator to perform multiple, unpacking, and destructuring
assignment in R. The operator unpacks the right-hand side of an assignment into
multiple values and assigns these values to variables on the left-hand side of
the assignment.

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
