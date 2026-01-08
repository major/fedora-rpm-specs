Name:           R-magrittr
Version:        %R_rpm_version 2.0.4
Release:        %autorelease
Summary:        Provides a mechanism for chaining commands with a new forward-pipe operator

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Provides a mechanism for chaining commands with a new forward-pipe operator.
This operator will forward a value, or the result of an expression, into
the next function call/expression. There is flexible support for the type of
right-hand side expressions. For more information, see package vignette. To
quote Rene Magritte, "Ceci n'est pas un pipe."

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
