Name:           R-repr
Version:        %R_rpm_version 1.1.7
Release:        %autorelease
Summary:        Serializable Representations

License:        GPL-3.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
String and binary representations of objects for several formats / mime
types.

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples

%files -f %{R_files}

%changelog
%autochangelog
