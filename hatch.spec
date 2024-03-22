%bcond tests 1
# These tests are really for python-hatchling; they are more likely than other
# tests to fail when the version of hatchling is compatible but does not
# exactly match the version of hatchling that existed in the shared git
# repository at the time of this Hatch release. Furthermore, it may be
# redundant to run these here if we run them in the python-hatchling build.
%bcond backend_tests 1

Name:           hatch
Version:        1.9.4
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

# Fix test that fails for openSUSE and other re-distributors
# https://github.com/pypa/hatch/pull/1177
#
# Missing patch for TestErrors.test_resolution_error in hatch 1.9.2
# https://github.com/pypa/hatch/issues/1214
Patch:          %{url}/pull/1177.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
# For extracting the list of test dependencies from hatch.toml:
BuildRequires:  tomcli
%if %{with backend_tests}
# A number of tests in TestBuildBootstrap require cargo.
BuildRequires:  cargo
%endif
%endif

BuildRequires:  git-core
Requires:       git-core

%description
Hatch is a modern, extensible Python project manager.

Features:

  • Standardized build system with reproducible builds by default
  • Robust environment management with support for custom scripts
  • Easy publishing to PyPI or other sources
  • Version management
  • Configurable project generation with sane defaults
  • Responsive CLI, ~2-3x faster than equivalent tools


%prep
%autosetup -n %{archivename} -p1

# https://hatch.pypa.io/latest/config/environment/
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli get hatch.toml -F newline-list envs.default.dependencies |
  sed -r 's/^(pytest-cov|cover)/# &/' | tee _env.default.txt


%generate_buildrequires
%if %{with tests}
%pyproject_buildrequires _env.default.txt
%else
%pyproject_buildrequires
%endif


%build
%pyproject_wheel

# The Markdown documentation is meant to be built with mkdocs. The HTML result
# is unsuitable for packaging due to various bundled and pre-minified
# JavaScript and CSS. See https://bugzilla.redhat.com/show_bug.cgi?id=2006555
# for discussion of similar problems with Sphinx and Doxygen. We therefore do
# not build or install the documentation.


%install
%pyproject_install
%pyproject_save_files -l hatch

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


%check
%if %{with tests}
%if %{with backend_tests}
# Without this, we end up with several test failures related to zip timestamps.
unset SOURCE_DATE_EPOCH
%else
ignore="${ignore-} --ignore=tests/backend/"
%endif

%pytest -k "${k-}" ${ignore-} -v
%else
%pyproject_check_import
%endif


%files -f %{pyproject_files}
%{_bindir}/hatch
%{_mandir}/man1/hatch.1*
%{_mandir}/man1/hatch-*.1*


%changelog
%autochangelog
