Name:           R-lambda.r
Version:        %R_rpm_version 1.2.4
Release:        %autorelease
Summary:        Modeling data with functional programming

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
A language extension to efficiently write functional programs in R. Syntax
extensions include multi-part function definitions, pattern matching,
guard statements, built-in (optional) type safety.

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
