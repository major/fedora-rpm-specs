%bcond bootstrap 0
# Many tests are enabled by default, unless bootstrapping
%bcond tests %{without bootstrap}
# However, some tests are disabled by default, becasue they require:
#  a) tested tox to be installed and/or
#  b) internet connection
# To run them, do the following:
#  1) Build --without ci_tests (the default) and optionally --without tests
#     (e.g. fedpkg mockbuild --without tests)
#  2) Install the built package
#     (e.g. mock install ./results_python-tox/.../tox-...rpm)
#  3) Build again --with ci_tests (and internet connection)
#     (e.g. fedpkg mockbuild --no-clean-all --enable-network --with ci_tests)
# The Fedora CI tests do this.
%bcond ci_tests 0

# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
# Fixes https://bugzilla.redhat.com/2057015
%undefine _py3_shebang_s

Name:           python-tox
Version:        4.24.1
Release:        %autorelease
Summary:        Virtualenv-based automation of test activities

License:        MIT
URL:            https://tox.readthedocs.io/
Source:         %{pypi_source tox}

# Remove dependency on devpi-process.
# Remove dependency on detect-test-pollution.
# Remove coverage-related dependencies.
# Adjust virtualenv environment variables to make it work with our patched virtualenv.
# Adjust setuptools-version specific ifs to check for setuptools version rather than Python version.
Patch:          fix-tests.patch

BuildArch:      noarch

BuildRequires:  python3-devel
# for dependency-groups support:
BuildRequires:  pyproject-rpm-macros >= 1.16

%if %{with tests}
BuildRequires:  /usr/bin/gcc
BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/pip
BuildRequires:  /usr/bin/pytest
BuildRequires:  /usr/bin/python
BuildRequires:  libffi-devel
# xdist is not used upstream, but we use it to speed up the %%check
BuildRequires:  python3-pytest-xdist
%if %{with ci_tests}
# The CI tests only work if the tested tox is installed :(
# This should technically be the same V-R, but the CI does not handle %%autorelease well
BuildRequires:  tox = %{version}
%endif
%endif

%global _description %{expand:
Tox as is a generic virtualenv management and test command line tool you
can use for:

 - checking your package installs correctly with different Python versions
   and interpreters
 - running your tests in each of the environments, configuring your test tool
   of choice
 - acting as a frontend to Continuous Integration servers, greatly reducing
   boilerplate and merging CI and shell-based testing.}

%description %_description


%package -n tox
Summary:        %{summary}

# Recommend "all the Pythons"
# Why? Tox exists to enable developers to test libraries against various Python
# versions, with just "dnf install tox" and a config file.
# See: https://developer.fedoraproject.org/tech/languages/python/python-installation.html#using-virtualenv
# Tox itself runs on the system python3 (i.e. %%{python3_version},
# however it launches other Python versions as subprocesses.
# It recommends all Python versions it supports. (This is an exception to
# the rule that Fedora packages may not require the alternative interpreters.)
%if 0%{?fedora}
%if 0%{?fedora} < 42
Recommends:     python3.8
%endif
Recommends:     python3.9
Recommends:     python3.10
Recommends:     pypy3-devel
%endif
Recommends:     python3-devel
# Instead of adding new Pythons here, add `Supplements: tox` to them, see:
# https://lists.fedoraproject.org/archives/list/python-devel@lists.fedoraproject.org/thread/NVVUXSVSPFQOWIGBE2JNI67HEO7R63ZQ/

%py_provides    python3-tox

%description -n tox %_description


%prep
%autosetup -p1 -n tox-%{version}

# Upstream updates dependencies too aggressively
# see https://github.com/tox-dev/tox/pull/2843#discussion_r1065028356
sed -ri -e 's/"(packaging|filelock|platformdirs|psutil|pyproject-api|pytest|pytest-mock|pytest-xdist|wheel|pluggy|distlib|cachetools|build\[virtualenv\]|setuptools|flaky)>=.*/"\1",/g' \
        -e 's/"(time-machine)>=[^;"]+/"\1/' \
        -e 's/"(virtualenv)>=.*/"\1>=20",/g' \
        -e 's/"(hatchling)>=.*/"\1>=1.13",/g' \
    pyproject.toml

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_buildrequires -r %{?with_tests:-g test}


%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tox


%if %{with tests}
%check
# Skipped tests use internal virtualenv functionality to
# download wheels which does not work with "bundled" version of wheel in
# the Fedora's virtualenv patch.
k="${k-}${k+ and }not test_virtualenv_flipped_settings"
k="${k-}${k+ and }not test_virtualenv_env_ignored_if_set"
k="${k-}${k+ and }not test_virtualenv_env_used_if_not_set"

# https://github.com/tox-dev/tox/issues/3290
%if v"0%{?python3_version}" >= v"3.13"
k="${k-}${k+ and }not test_str_convert_ok_py39"
%endif

# https://github.com/tox-dev/tox/commit/698f1dd663
# Until we have setuptools 70.1+ we skip those
k="${k-}${k+ and }not test_result_json_sequential"
k="${k-}${k+ and }not test_setuptools_package"
k="${k-}${k+ and }not test_skip_develop_mode"
k="${k-}${k+ and }not test_tox_install_pkg_sdist"

# The following tests either need internet connection or installed tox
# so we only run them on the CI.
%if %{without ci_tests}
k="${k-}${k+ and }not test_virtualenv_flipped_settings"
k="${k-}${k+ and }not test_virtualenv_env_ignored_if_set"
k="${k-}${k+ and }not test_virtualenv_env_used_if_not_set"
k="${k-}${k+ and }not test_build_wheel_external"
k="${k-}${k+ and }not keyboard_interrupt"
k="${k-}${k+ and }not test_call_as_module"
k="${k-}${k+ and }not test_call_as_exe"
k="${k-}${k+ and }not test_run_installpkg_targz"
%endif

%pytest -v -n auto -k "${k-}" --run-integration
%endif


%files -n tox -f %{pyproject_files}
%{_bindir}/tox


%changelog
%autochangelog
