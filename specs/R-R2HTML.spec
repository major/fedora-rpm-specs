Name:           R-R2HTML
Version:        %R_rpm_version 2.3.4
Release:        %autorelease
Summary:        HTML Exportation for R Objects

License:        GPL-2.0-or-later
URL:            %cran_url
Source:         %cran_source

BuildArch:      noarch
BuildRequires:  R-devel

Provides:       bundled(asciimathml)
Provides:       bundled(activewidgets)

%description
Includes HTML function and methods to write in an HTML file. Thus, making
HTML reports is easy. Includes a function that allows redirection on the
fly, which appears to be very useful for teaching purpose, as the student
can keep a copy of the produced output to keep all that he did during the
course. Package comes with a vignette describing how to write HTML reports
for statistical analysis. Finally, a driver for 'Sweave' allows to parse
HTML flat files containing R code and to automatically write the
corresponding outputs (tables and graphs).

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
