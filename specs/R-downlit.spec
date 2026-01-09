Name:           R-downlit
Version:        %R_rpm_version 0.4.5
Release:        %autorelease
Summary:        Syntax Highlighting and Automatic Linking

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Syntax highlighting of R code, specifically designed for the needs of RMarkdown
packages like pkgdown, hugodown, and bookdown. It includes linking of function
calls to their documentation on the web, and automatic translation of ANSI
escapes in output to the equivalent HTML.

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
