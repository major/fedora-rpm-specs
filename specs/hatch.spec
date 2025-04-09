%bcond tests 1

Name:           hatch
Version:        1.14.1
Release:        %autorelease
Summary:        A modern project, package, and virtual env manager

%global tag hatch-v%{version}
%global archivename hatch-%{tag}

# The entire source is (SPDX) MIT. Apache-2.0 license text in the tests is used
# as a sample license text, not as a license for the source.
License:        MIT
URL:            https://github.com/pypa/hatch
Source0:        %{url}/archive/%{tag}/hatch-%{tag}.tar.gz

# Written for Fedora in groff_man(7) format based on --help output
Source100:      hatch.1
Source200:      hatch-build.1
Source300:      hatch-clean.1
Source400:      hatch-config.1
Source410:      hatch-config-explore.1
Source420:      hatch-config-find.1
Source430:      hatch-config-restore.1
Source440:      hatch-config-set.1
Source450:      hatch-config-show.1
Source460:      hatch-config-update.1
Source500:      hatch-dep.1
Source510:      hatch-dep-hash.1
Source520:      hatch-dep-show.1
Source521:      hatch-dep-show-requirements.1
Source522:      hatch-dep-show-table.1
Source600:      hatch-env.1
Source610:      hatch-env-create.1
Source620:      hatch-env-find.1
Source630:      hatch-env-prune.1
Source640:      hatch-env-remove.1
Source650:      hatch-env-run.1
Source660:      hatch-env-show.1
Source700:      hatch-new.1
Source800:      hatch-project.1
Source810:      hatch-project-metadata.1
Source900:      hatch-publish.1
Source1000:     hatch-run.1
Source1100:     hatch-shell.1
Source1200:     hatch-status.1
Source1300:     hatch-version.1
Source1400:     hatch-fmt.1
Source1500:     hatch-python.1
Source1510:     hatch-python-find.1
Source1520:     hatch-python-install.1
Source1530:     hatch-python-remove.1
Source1540:     hatch-python-show.1
Source1550:     hatch-python-update.1
Source1600:     hatch-self.1
Source1610:     hatch-self-report.1
Source1620:     hatch-self-restore.1
Source1630:     hatch-self-update.1
Source1700:     hatch-test.1

BuildSystem:            pyproject
BuildOption(install):   -l hatch
%if %{with tests}
BuildOption(generate_buildrequires): _envs.hatch-test.extra-dependencies.txt
%endif

# Add pytest.mark.requires_internet to a few more tests
# https://github.com/pypa/hatch/pull/1665
Patch:          %{url}/pull/1665.patch

BuildArch:      noarch

%if %{with tests}
# Upstream uses “hatch test” to run the tests, but this wants to use Python
# interpreters downloaded from the Internet
# (https://github.com/pypa/hatch/issues/1541), and there is less flexibility
# for skipping or ignoring tests than there is when we use pytest directly.
#
# Test dependencies are listed in src/hatch/env/internal/test.py:
# 'coverage-enable-subprocess==1.0', <-- linters/coverage
# 'coverage[toml]~=7.4', <-- linters/coverage
# 'pytest~=8.1',
# 'pytest-mock~=3.12',
# 'pytest-randomly~=3.15',
# 'pytest-rerunfailures~=14.0',
# 'pytest-xdist[psutil]~=3.5',
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-mock}
BuildRequires:  %{py3_dist pytest-randomly}
BuildRequires:  %{py3_dist pytest-rerunfailures}
BuildRequires:  %{py3_dist pytest-xdist[psutil]}
# For extracting the list of test “extra-dependencies” from hatch.toml:
BuildRequires:  tomcli
%endif

BuildRequires:  git-core
Requires:       git-core

%description
Hatch is a modern, extensible Python project manager.

Features:

  • Standardized build system with reproducible builds by default
  • Robust environment management with support for custom scripts and UV
  • Test execution with known best practices
  • Static analysis with sane defaults
  • Built-in Python script runner
  • Easy publishing to PyPI or other indices
  • Version management
  • Best practice project generation
  • Responsive CLI, ~2-3x faster than equivalent tools


%prep -a
# https://hatch.pypa.io/latest/config/environment/
tomcli get hatch.toml -F newline-list envs.hatch-test.extra-dependencies |
  tee _envs.hatch-test.extra-dependencies.txt


%install -a
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE100}' \
    '%{SOURCE200}' \
    '%{SOURCE300}' \
    '%{SOURCE400}' '%{SOURCE410}' '%{SOURCE420}' '%{SOURCE430}' \
      '%{SOURCE440}' '%{SOURCE450}' '%{SOURCE460}' \
    '%{SOURCE500}' '%{SOURCE510}' '%{SOURCE520}' '%{SOURCE521}' \
      '%{SOURCE522}' \
    '%{SOURCE600}' '%{SOURCE610}' '%{SOURCE620}' '%{SOURCE630}' \
      '%{SOURCE640}' '%{SOURCE650}' '%{SOURCE660}' \
    '%{SOURCE700}' \
    '%{SOURCE800}' '%{SOURCE810}' \
    '%{SOURCE900}' \
    '%{SOURCE1000}' \
    '%{SOURCE1100}' \
    '%{SOURCE1200}' \
    '%{SOURCE1300}' \
    '%{SOURCE1400}' \
    '%{SOURCE1500}' '%{SOURCE1510}' '%{SOURCE1520}' '%{SOURCE1530}' \
      '%{SOURCE1540}' '%{SOURCE1550}'


%check -a
%if %{with tests}
# These tests are actually for hatchling, and may fail due to small differences
# between the state of hatchling in the hatch release tag and in the latest
# actual hatchling release.
ignore="${ignore-} --ignore=tests/backend/"

# FAILED tests/cli/test/test_test.py::TestCustomScripts::test_single -
#   AssertionError: assert [call('test hatch-test.py3.12', shell=True)] ==
#   [call('test hatch-test.py3.13', shell=True)]
# This appears to be due to an expectation that the tests are run via “hatch
# test” on one of Hatch’s “standard” Python interpreters, rather than on the
# system Python.
k="${k-}${k+ and }not (TestCustomScripts and test_single)"

# https://github.com/pypa/hatch/issues/1670
# hatch.errors.PythonDistributionResolutionError: Could not find a default
# source for name='${param}' system='linux' arch='${arch}' abi='gnu' variant=''
#
# Since we cannot use %%ifarch in a noarch package, we skip tests that fail on
# *any* architecture, even if we happen to be building on an architecture where
# they pass. The largest set of failing distributions are, for ppc64le/s390x:
missing_dists='3.7 3.8 pypy2.7 pypy3.9 pypy3.10'
# For aarch64, missing_dists='3.7', and for x86_64, missing_dists=''.
for param in ${missing_dists}
do
  k="${k-}${k+ and }not test_custom_source[${param}]"
  # Requires network (but does fail when it is enabled)
  k="${k-}${k+ and }not test_installation[${param}]"
done
# Also, for ppc64le and s390x:
k="${k-}${k+ and }not (TestDistributionPaths and test_pypy_custom)"
k="${k-}${k+ and }not (TestDistributionVersions and test_pypy_custom)"

%pytest -k "${k-}" ${ignore-} -vv
%endif


%files -f %{pyproject_files}
%{_bindir}/hatch
%{_mandir}/man1/hatch.1*
%{_mandir}/man1/hatch-*.1*


%changelog
%autochangelog
