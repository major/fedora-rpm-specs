Name:           R-reticulate
Version:        %R_rpm_version 1.44.1
Release:        %autorelease
Summary:        R Interface to 'Python'

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(scipy)
Requires:       python3

%description
Interface to Python modules, classes, and functions. When calling into Python,
R data types are automatically converted to their equivalent Python types. When
values are returned from Python to R they are converted back to R types.

%prep
%autosetup -c
sed -i 's/# skip_if_offline/skip/' \
    reticulate/tests/testthat/test-python-source.R

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%py_byte_compile %{python3} %{buildroot}%{_R_libdir}/reticulate/python/rpytools
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
