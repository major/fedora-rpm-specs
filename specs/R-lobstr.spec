Name:           R-lobstr
Version:        %R_rpm_version 1.1.3
Release:        %autorelease
Summary:        Visualize R Data Structures with Trees

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
A set of tools for inspecting and understanding R data structures inspired by
str(). Includes ast() for visualizing abstract syntax trees, ref() for showing
shared references, cst() for showing call stack trees, and obj_size() for
computing object sizes.

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
