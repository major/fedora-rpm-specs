Name:           R-glue
Version:        %R_rpm_version 1.8.0
Release:        %autorelease
Summary:        Interpreted String Literals

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
An implementation of interpreted string literals, inspired by Python's
Literal String Interpolation <https://www.python.org/dev/peps/pep-0498/>
and Docstrings <https://www.python.org/dev/peps/pep-0257/> and Julia's
Triple-Quoted String Literals
<https://docs.julialang.org/en/v1.3/manual/strings/#Triple-Quoted-String-Literals-1>.

%prep
%autosetup -c
rm -f glue/tests/testthat/test-vctrs.R # unconditional suggest, should be fixed

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
