Name:           R-lazyeval
Version:        %R_rpm_version 0.2.2
Release:        %autorelease
Summary:        Lazy (Non-Standard) Evaluation

License:        GPL-3.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
An alternative approach to non-standard evaluation using formulas.
Provides a full implementation of LISP style 'quasiquotation', making it
easier to generate code with other code.

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
