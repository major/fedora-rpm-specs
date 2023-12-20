# Run slow tests? In this case, “slow” is just a few minutes.
%bcond slow_tests 1

Name:           python-py27hash
Version:        1.1.0
Release:        %autorelease
Summary:        Python 2.7 hashing and iteration in Python 3+

# SPDX
License:        MIT
URL:            https://github.com/neuml/py27hash
# The GitHub tarball contains tests; the PyPI sdist does not.
Source:         %{url}/archive/v%{version}/py27hash-%{version}.tar.gz

# Since the package previously had an arch-dependent failure, we build on all
# platforms (the base package is not noarch) to flush out any similar issues.
# However, we produce only a noarch binary package. Since there is no compiled
# code, there is no debug package.
%global debug_package %{nil}

BuildRequires:  python3-devel

%global common_description %{expand:
This package helps ease the migration from Python 2 to 3 for applications that
depend on the old hash/iteration order of sets/dicts. Even when setting
PYTHONHASHSEED=0, the hash (and default iteration order) will still be
different as the hashing algorithm changed in Python 3. This package allows
Python 2.7 hashing and set/dict iteration.}

%description %{common_description}


%package -n python3-py27hash
Summary:        %{summary}

BuildArch:      noarch

%description -n python3-py27hash %{common_description}


%prep
%autosetup -n py27hash-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l py27hash


%check
# See scripts/tests.sh, which we have here slightly modified for our purposes:
SRC_DIR='%{buildroot}%{python3_sitelib}'
TEST_DIR="${PWD}/test/python"

# The %%{py3_test_envvars} macro adds to the PATH we set here. For PYTHONPATH,
# when it finds it already set, it does not override or adjust it.
export PYTHONPATH="${SRC_DIR}:${TEST_DIR}"
export PATH="${TEST_DIR}:${PATH}"
export SKIPSLOW='%{?!with_slow_tests:skipslow}'
%{py3_test_envvars} %{python3} -m unittest discover -v -s "${TEST_DIR}"


%files -n python3-py27hash -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
