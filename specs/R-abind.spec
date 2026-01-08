Name:           R-abind
Version:        %R_rpm_version 1.4-8
Release:        %autorelease
Summary:        Combine multi-dimensional arrays

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Combine multi-dimensional arrays. This is a generalization of cbind and rbind. 
Takes a sequence of vectors, matrices, or arrays and produces a single array 
of the same or higher dimension.

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
