# Run at least the handwritten tests?
%bcond tests 1
%bcond minimal_tests 1
# The full tests fail, and should probably be removed upstream:
# https://github.com/brendanarnold/py-fortranformat/issues/35
# https://github.com/brendanarnold/py-fortranformat/issues/32
%bcond full_tests 0

Name:           python-fortranformat
Version:        2.0.3
Release:        %{autorelease}
Summary:        FORTRAN format interpreter for Python

License:        MIT
URL:            https://github.com/brendanarnold/py-fortranformat
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#./python-fortranformat-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%if %{with minimal_tests} || %{with full_tests}
BuildRequires:  make
%endif
%if %{with full_tests}
BuildRequires:  gcc-gfortran
%endif
%endif

%global _description %{expand:
Generates text from a Python list of variables or will read a line of text
into Python variables according to the FORTRAN format statement passed.
}

%description %_description

%package -n python3-fortranformat
Summary:        %{summary}

%description -n python3-fortranformat %_description


%prep
%autosetup -p1 -n py-fortranformat-%{version}
sed -r -i 's@\bpython\b@%{python3}@' Makefile


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
%if %{with tests}
%if %{with minimal_tests} || %{with full_tests}
%make_build buildtests
%endif
%if %{with full_tests}
# This takes a long time!
%make_build compilertests
%endif
%endif


%install
%pyproject_install
%pyproject_save_files -l fortranformat -L


%check
%pyproject_check_import fortranformat
%if %{with tests}
%if %{without full_tests} && %{without minimal_tests}
# At least run the hand-written tests:
%pytest tests/handwritten
%endif
%if %{with minimal_tests}
%py3_test_envvars %make_build runminimaltests
%endif
%if %{with full_tests}
%py3_test_envvars %make_build runtests
%endif
%endif


%files -n python3-fortranformat -f %{pyproject_files}
%doc README.*
%doc CHANGELOG.md
%license LICENSE

%changelog
%autochangelog
