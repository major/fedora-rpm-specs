Name:           R-selectr
Version:        %R_rpm_version 0.5-1
Release:        %autorelease
Summary:        Translate CSS Selectors to XPath Expressions

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{cran_url}
Source:         %{cran_source}

BuildArch:      noarch
BuildRequires:  R-devel

%description
Translates a CSS3 selector into an equivalent XPath expression. This allows us
to use CSS selectors when working with the XML package as it can only evaluate
XPath expressions. Also provided are convenience functions useful for using CSS
selectors on XML nodes. This package is a port of the Python package
'cssselect' (<https://cssselect.readthedocs.io/>).

%prep
%autosetup -c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-examples \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
