%bcond tests 1

Name:           python-wcwidth
Version:        0.9.2
Release:        %autorelease
Summary:        Measures number of Terminal column cells of wide-character codes

# The original code was derived from wcwidth.c under an HPND license
License:        MIT AND HPND-Markus-Kuhn
URL:            https://github.com/jquast/wcwidth
Source:         %{pypi_source wcwidth}


%description
This API is mainly for Terminal Emulator implementors, or those writing programs
that expect to interpreted by a terminal emulator and wish to determine the
printable width of a string on a Terminal.

%package -n     python3-wcwidth
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  gcc
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%description -n python3-wcwidth
This API is mainly for Terminal Emulator implementors, or those writing programs
that expect to interpreted by a terminal emulator and wish to determine the
printable width of a string on a Terminal.

%prep
%autosetup -p1 -n wcwidth-%{version}
# skip coverage checks
sed -i -e 's|--cov[^[:space:]]*||g' tox.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l wcwidth

%check
%pyproject_check_import
%if %{with tests}
export PYTHONSAFEPATH=1
%pytest -v --import-mode=importlib tests
%endif
# Check to make sure C extension loads
%{py3_test_envvars} %{python3} -c "import wcwidth; assert wcwidth.HAS_C_EXTENSION"

%files -n python3-wcwidth -f %{pyproject_files}
%doc docs/*.rst

%changelog
%autochangelog
