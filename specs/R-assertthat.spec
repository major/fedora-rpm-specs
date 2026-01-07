Name:           R-assertthat
Version:        %R_rpm_version 0.2.1
Release:        %autorelease
Summary:        Easy Pre and Post Assertions

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
An extension to stopifnot() that makes it easy to declare the pre and post
conditions that you code should satisfy, while also producing friendly
error messages so that your users know what's gone wrong.

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
