Name:           R-gdata
Version:        %R_rpm_version 3.0.1
Release:        %autorelease
Summary:        Various R Programming Tools for Data Manipulation

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Various R programming tools for data manipulation, including:
  - medical unit conversions,
  - combining objects,
  - character vector operations,
  - factor manipulation,
  - obtaining information about R objects,
  - manipulating MS-Excel formatted files,
  - generating fixed-width format files,
  - extricating components of date & time objects,
  - operations on columns of data frames,
  - matrix operations,
  - operations on vectors,
  - operations on data frames,
  - value of last evaluated expression, and
  - wrapper for 'sample' that ensures consistent behavior for both scalar and
    vector arguments.

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
