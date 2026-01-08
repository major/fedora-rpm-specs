Name:           R-highlight
Version:        %R_rpm_version 0.5.2
Release:        %autorelease
Summary:	    R Syntax Highlighter

License:	    GPL-3.0-or-later
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Syntax highlighter for R code based on the results of the R parser.
Rendering in HTML and latex markup. Custom Sweave driver performing
syntax highlighting of R code chunks.

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
