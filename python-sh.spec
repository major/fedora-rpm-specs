%global common_description %{expand:
sh is a full-fledged subprocess replacement for Python that allows you to call
any program as if it were a function.  sh is not a collection of system
commands implemented in Python.}

Name:           python-sh
Version:        2.0.6
Release:        %autorelease
Summary:        Python subprocess replacement
License:        MIT
URL:            https://sh.readthedocs.io/
Source:         %{pypi_source sh}
BuildArch:      noarch
BuildRequires:  python3-devel
# Several tests run the python command.
BuildRequires:  python-unversioned-command


%description %{common_description}


%package -n python3-sh
Summary:        %{summary}


%description -n python3-sh %{common_description}


%prep
%autosetup -p 1 -n sh-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files sh


%check
# The tests expect sh.py and sh_test.py to be in the same directory.
# https://github.com/amoffat/sh/blob/2.0.6/tests/Dockerfile#L47
# https://github.com/amoffat/sh/blob/2.0.6/tox.ini#L14
mv tests/sh_test.py .

# https://github.com/amoffat/sh/commit/bfb2bc97635f694de3e5234dcec08d604f0d880f
export SH_TESTS_RUNNING=1

# Normally we should run the tests with %%{py3_test_envvars}, but some tests
# fail if we modify PYTHONPATH.
# https://github.com/amoffat/sh/issues/692

# Run tests with both poll and select.
# https://github.com/amoffat/sh/commit/e8737f82585bc39a3bc079c5fa7054c973148e3d
SH_TESTS_USE_SELECT=0 %{python3} sh_test.py
SH_TESTS_USE_SELECT=1 %{python3} sh_test.py


%files -n python3-sh -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst CHANGELOG.md MIGRATION.md


%changelog
%autochangelog
