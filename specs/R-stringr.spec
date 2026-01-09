Name:           R-stringr
Version:        %R_rpm_version 1.6.0
Release:        %autorelease
Summary:        Simple, Consistent Wrappers for Common String Operations

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A consistent, simple and easy to use set of wrappers around the fantastic
'stringi' package. All function and argument names (and positions) are
consistent, all functions deal with "NA"'s and zero length vectors in the
same way, and the output from one function is easy to feed into the input
of another.

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
