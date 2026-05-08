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
Version:        4.53.1
Release:        %autorelease
Summary:        Virtualenv-based automation of test activities

License:        MIT
URL:            https://tox.readthedocs.io/
Source:         %{pypi_source tox}

# Remove usage of devpi-process.
# Remove coverage options.
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
BuildRequires:  /usr/bin/man
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
Recommends:     python3.9
%endif
# Instead of adding new Pythons here, add `Supplements: tox` to them, see:
# https://lists.fedoraproject.org/archives/list/python-devel@lists.fedoraproject.org/thread/NVVUXSVSPFQOWIGBE2JNI67HEO7R63ZQ/

# Enable completions by default
Recommends:     (tox+completion if (bash-completion or fish or zsh))

%py_provides    python3-tox

%description -n tox %_description


%prep
%autosetup -p1 -n tox-%{version}

# Upstream updates dependencies too aggressively
# see https://github.com/tox-dev/tox/pull/2843#discussion_r1065028356
# First, carefully adjust the pins of build and runtime dependencies,
# then remove all the >= specifiers from tests deps, whatever they are,
# finally, remove undesired test dependencies.
sed -ri -e 's/"(filelock|platformdirs|pyproject-api|cachetools|hatch-vcs)>=.*/"\1",/g' \
        -e 's/"(hatchling)>=.*/"\1>=1.13",/g' \
        -e 's/"(pluggy)>=.*/"\1>=1.5",/g' \
        -e '/^test = \[/,/^\]/ { s/>=[^;"]+// }' \
        -e '/^test = \[/,/^\]/ { /"(covdefaults|coverage|detect-test-pollution|devpi-process|diff-cover|pytest-cov)[;"]/d }' \
    pyproject.toml

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_buildrequires -r %{?with_tests:-g test} -x completion


%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tox

for shell in bash fish zsh; do
  register-python-argcomplete --shell $shell tox > tox.$shell
done
# The bash-completion package has tox already, we use the .bash suffix,
# see https://github.com/scop/bash-completion/issues/1628#issuecomment-4380971779
install -Dpm 0644 tox.bash %{buildroot}%{bash_completions_dir}/tox.bash
install -Dpm 0644 tox.fish %{buildroot}%{fish_completions_dir}/tox.fish
install -Dpm 0644 tox.zsh  %{buildroot}%{zsh_completions_dir}/_tox


%if %{with tests}
%check
# A macro that returns a version of the installed Python package, as an RPM v-string, defaults to v"0"
%define pyversion() v"%(%{python3} -c 'import importlib.metadata as im; print(im.version("%{1}"))' 2>/dev/null || echo 0)"

# Skipped tests use internal virtualenv functionality to
# download wheels which does not work with "bundled" version of wheel in
# the Fedora's virtualenv patch.
k="${k-}${k+ and }not test_virtualenv_flipped_settings"
k="${k-}${k+ and }not test_virtualenv_env_ignored_if_set"
k="${k-}${k+ and }not test_virtualenv_env_used_if_not_set"

# https://github.com/tox-dev/tox/commit/698f1dd663
# The tests fail with setuptools < 70.1
%if %{pyversion setuptools} < v"70.1"
k="${k-}${k+ and }not test_result_json_sequential"
k="${k-}${k+ and }not test_setuptools_package"
k="${k-}${k+ and }not test_skip_develop_mode"
k="${k-}${k+ and }not test_tox_install_pkg_sdist"
%endif

# The following tests either need internet connection or installed tox
# so we only run them on the CI.
%if %{without ci_tests}
k="${k-}${k+ and }not test_build_wheel_external"
k="${k-}${k+ and }not keyboard_interrupt"
k="${k-}${k+ and }not test_call_as_module"
k="${k-}${k+ and }not test_call_as_exe"
k="${k-}${k+ and }not test_run_installpkg_targz"
k="${k-}${k+ and }not test_pyproject_installpkg_pep517_envs"
k="${k-}${k+ and }not test_pylock_install_integration"
k="${k-}${k+ and }not test_interrupt_post_commands"
k="${k-}${k+ and }not test_second_interrupt_stops_post_commands"
%endif

%pytest -v -n auto -k "${k-}" --run-integration
%endif


%files -n tox -f %{pyproject_files}
%{_bindir}/tox
%{_mandir}/man1/tox.1*

%pyproject_extras_subpkg -n tox completion
%{bash_completions_dir}/tox.bash
%{fish_completions_dir}/tox.fish
%{zsh_completions_dir}/_tox


%changelog
%autochangelog
