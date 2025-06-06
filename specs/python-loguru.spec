%bcond tests 1

Name:           python-loguru
Version:        0.7.3
Release:        %autorelease
Summary:        Python logging made (stupidly) simple

License:        MIT
URL:            https://github.com/Delgan/loguru
# The GitHub archive contains CHANGELOG.rst, which the PyPI sdist lacks.
Source:         %{url}/archive/%{version}/loguru-%{version}.tar.gz

# Fix deprecation warning raised by tests with Python 3.14
# https://github.com/Delgan/loguru/pull/1298
# Cherry-picked to 0.7.3
Patch:          0001-Fix-deprecation-warning-raised-by-tests-with-Python-.patch

BuildArch:      noarch

BuildSystem:            pyproject
BuildOption(install):   -l loguru

# The dev extra pins exact versions and includes unwanted coverage tools etc.
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters), 
# and developer tools, so we enumerate test dependencies manually:
BuildRequires:  %{py3_dist colorama}
BuildRequires:  %{py3_dist freezegun}
BuildRequires:  %{py3_dist pytest}

# Normally we should not depend on typecheckers or linters, but the test that
# uses mypy is simply confirming that the stub file is valid and usable. That
# seems OK. Alternatively, we could pass --ignore=tests/test_type_hinting.py to
# %%pytest.
BuildRequires:  %{py3_dist mypy}

%global common_description %{expand:
Loguru is a library which aims to bring enjoyable logging in Python.}

%description %{common_description}


%package -n     python3-loguru
Summary:        %{summary}

%description -n python3-loguru %{common_description}


%prep
%autosetup -n loguru-%{version} -p1


%check -a
%if %{with tests}
# Make sure we don’t run the detailed typing tests; see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
ignore="${ignore-} --ignore=tests/typesafety/test_logger.yml"

%if v"0%{?python3_version}" >= v"3.14"
# Python 3.14.0a6: a few new regressions
# https://github.com/Delgan/loguru/issues/1331
k="${k-}${k+ and }not test_exception_others[recursion_error]"
k="${k-}${k+ and }not test_exception_modern[type_hints-minimum_python_version0]"
%endif

%pytest ${ignore-} -k "${k-}" -rs
%endif


%files -n python3-loguru -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.md


%changelog
%autochangelog
