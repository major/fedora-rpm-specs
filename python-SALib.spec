%bcond tests 1

%global forgeurl https://github.com/SALib/SALib

Name:           python-SALib
Version:        1.4.7
Release:        %autorelease
Summary:        Tools for global sensitivity analysis

%forgemeta

License:        MIT
URL:            https://salib.readthedocs.io
Source:         %{forgesource}

# Remove a useless shebang line
# https://github.com/SALib/SALib/pull/592
Patch:          %{forgeurl}/pull/592.patch
# Remove bogus executable permissions
# https://github.com/SALib/SALib/pull/593
Patch:          %{forgeurl}/pull/593.patch

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  dos2unix
BuildRequires:  file

%global _description %{expand:
Python implementations of commonly used sensitivity analysis methods. Useful in
systems modeling to calculate the effects of model inputs or exogenous factors
on outputs of interest.}

%description %_description

%package -n python3-salib
Summary:        %{summary}

%py_provides python3-SALib

%description -n python3-salib %_description

%pyproject_extras_subpkg -n python3-salib distributed

%prep
%forgeautosetup -p1

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^([[:blank:]])(.*\bpytest-cov\b)/\1# \2/' pyproject.toml

# Correct end of line encodings. See:
#
# Standardize line terminations
# https://github.com/SALib/SALib/pull/591
find . -type f -exec file '{}' '+' |
  awk -F ':' '/CRLF/ { print $1 }' |
  xargs dos2unix --keepdate

%generate_buildrequires
%pyproject_buildrequires -x distributed %{?with_tests:-x test}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l SALib

%check
%if %{with tests}
%pytest
%endif

%files -n python3-salib -f %{pyproject_files}
%doc CHANGELOG.md
%doc CITATION.cff
%doc CITATIONS.rst
%doc FAQ.MD
%doc README-advanced.md
%doc README.rst
%{_bindir}/salib

%changelog
%autochangelog
