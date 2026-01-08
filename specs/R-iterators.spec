Name:           R-iterators
Version:        %R_rpm_version 1.0.14
Release:        %autorelease
Summary:        Provides Iterator Construct

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Support for iterators, which allow a programmer to traverse through all the
elements of a vector, list, or other collection of data.

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
