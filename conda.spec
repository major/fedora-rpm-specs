%bcond_without tests

Name:           conda
Version:        23.11.0
Release:        %autorelease
Summary:        Cross-platform, Python-agnostic binary package manager

License:        BSD-3-Clause AND Apache-2.0 
# The conda code is BSD-3-Clause
# adapters/ftp.py is Apache-2.0

URL:            http://conda.pydata.org/docs/
Source0:        https://github.com/conda/conda/archive/%{version}/%{name}-%{version}.tar.gz
# bash completion script moved to a separate project
Source1:        https://raw.githubusercontent.com/tartansandal/conda-bash-completion/1.7/conda
Patch0:         conda_sys_prefix.patch
# Use main entry point for conda and re-add conda-env entry point, no need to run conda init
Patch1:         0001-Use-main-entry-point-for-conda-and-re-add-conda-env-.patch
# Use system cpuinfo
Patch3:         conda-cpuinfo.patch
# Fix tests on 32bit
# https://github.com/conda/conda/pull/9759
#Patch4:         conda-32bit.patch

Patch10004:     0004-Do-not-try-to-run-usr-bin-python.patch
Patch10005:     0005-Fix-failing-tests-in-test_api.py.patch
Patch10006:     0006-shell-assume-shell-plugins-are-in-etc.patch

BuildArch:      noarch

BuildRequires:  pkgconfig(bash-completion)
%global bash_completionsdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null || echo '/etc/bash_completion.d')
BuildRequires:  sed

Requires:       python%{python3_pkgversion}-conda = %{version}-%{release}
# Removed upstream in favour of calling "conda activate" in version 4.4.0
Obsoletes:      conda-activate < 4.4

%?python_enable_dependency_generator


%global _description %{expand:
Conda is a cross-platform, Python-agnostic binary package manager. It
is the package manager used by Anaconda installations, but it may be
used for other systems as well. Conda makes environments first-class
citizens, making it easy to create independent environments even for
C libraries. Conda is written entirely in Python.

The Fedora conda base environment is special.  Unlike a standard
anaconda install base environment it is essentially read-only.  You
can only use conda to create and manage new environments.}


%description %_description


%package tests
Summary:        conda tests

%description tests
Data for conda tests.  Set CONDA_TEST_DATA_DIR to
%{_datadir}/conda/tests/data.


%package -n python%{python3_pkgversion}-conda
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
# For tests
BuildRequires:  python-unversioned-command
BuildRequires:  python%{python3_pkgversion}-boto3
BuildRequires:  python%{python3_pkgversion}-flask
BuildRequires:  python%{python3_pkgversion}-jsonpatch
BuildRequires:  python%{python3_pkgversion}-pytest-mock
BuildRequires:  python%{python3_pkgversion}-pytest-rerunfailures
BuildRequires:  python%{python3_pkgversion}-pytest-timeout
BuildRequires:  python%{python3_pkgversion}-pytest-xprocess
BuildRequires:  python%{python3_pkgversion}-responses

# Some versions in conda/_vendor/vendor.txt
Provides:       bundled(python%{python3_pkgversion}-appdirs) = 1.2.0
Provides:       bundled(python%{python3_pkgversion}-auxlib) = 0.0.43
Provides:       bundled(python%{python3_pkgversion}-boltons) = 21.0.0

%{?python_provide:%python_provide python%{python3_pkgversion}-conda}

%description -n python%{python3_pkgversion}-conda %_description

%prep
%autosetup -p1

# Do not restrict upper bound of ruamel-yaml
sed -i -e '/ruamel.yaml/s/,<[0-9.]*//' pyproject.toml

# pytest-split/xdoctest not packaged, store-duration not needed
sed -i -e '/splitting-algorithm/d' -e '/store-durations/d' -e '/xdoctest/d' pyproject.toml

# delete interpreter line, the user can always call the file
# explicitly as python3 /usr/lib/python3.6/site-packages/conda/_vendor/appdirs.py
# or so.
sed -r -i '1 {/#![/]usr[/]bin[/]env/d}' conda/_vendor/appdirs.py

# Use Fedora's cpuinfo since it supports more arches
rm -r conda/_vendor/cpuinfo
sed -i -e '/^dependencies = /a\ \ "py-cpuinfo",' pyproject.toml

# Use system versions
rm -r conda/_vendor/{distro.py,frozendict}
find conda -name \*.py | xargs sed -i -e 's/^\( *\)from .*_vendor\.\(\(distro\|frozendict\).*\) import/\1from \2 import/'
sed -i -e '/^dependencies = /a\ \ "distro",' pyproject.toml
sed -i -e '/^dependencies = /a\ \ "frozendict",' pyproject.toml

# Unpackaged - use vendored version
sed -i -e '/"boltons *>/d' pyproject.toml

# Unpackaged - really only applicable for macOS/Windows?
sed -i -e '/"truststore *>/d' pyproject.toml

%ifnarch x86_64
# Tests on 32-bit
cp -a tests/data/conda_format_repo/linux-{64,32}
sed -i -e s/linux-64/linux-32/ tests/data/conda_format_repo/linux-32/*json
# Tests on non-x86_64
cp -a tests/data/conda_format_repo/{linux-64,%{python3_platform}}
sed -i -e s/linux-64/%{python3_platform}/ tests/data/conda_format_repo/%{python3_platform}/*json
%endif

# Do not run coverage in pytest
sed -i -e '/"--cov/d' pyproject.toml

%generate_buildrequires
# When not testing, we don't need runtime dependencies.
# Normally, we would still BuildRequire them to not accidentally build an uninstallable package,
# but there is a runtime dependency loop with python3-conda-libmamba-solver.
%pyproject_buildrequires %{!?with_tests:-R}

%build
%pyproject_wheel

%install
%pyproject_install
%py3_shebang_fix %{buildroot}%{python3_sitelib}/conda/shell/bin/conda
%pyproject_save_files conda*

mkdir -p %{buildroot}%{_sysconfdir}/conda/condarc.d
mkdir -p %{buildroot}%{_datadir}/conda/condarc.d
cat >%{buildroot}%{_datadir}/conda/condarc.d/defaults.yaml <<EOF
pkgs_dirs:
 - /var/cache/conda/pkgs
 - ~/.conda/pkgs
EOF

mv %{buildroot}%{python3_sitelib}/tests %{buildroot}%{_datadir}/conda/
cp -rp tests/data %{buildroot}%{_datadir}/conda/tests/

mkdir -p %{buildroot}%{_localstatedir}/cache/conda/pkgs/cache

# install does not create the directory on EL7
install -m 0644 -Dt %{buildroot}/etc/profile.d/ conda/shell/etc/profile.d/conda.{sh,csh}
sed -r -i -e '1i [ -z "$CONDA_EXE" ] && CONDA_EXE=%{_bindir}/conda' \
          -e '/PATH=.*condabin/s|PATH=|[ -d $(dirname "$CONDA_EXE")/condabin ] \&\& PATH=|' %{buildroot}/etc/profile.d/conda.sh
sed -r -i -e '1i set _CONDA_EXE=%{_bindir}/conda\nset _CONDA_ROOT=' \
          -e 's/CONDA_PFX=.*/CONDA_PFX=/' %{buildroot}/etc/profile.d/conda.csh
install -m 0644 -Dt %{buildroot}%{_datadir}/fish/vendor_conf.d/ conda/shell/etc/fish/conf.d/conda.fish
sed -r -i -e '1i set -gx CONDA_EXE "/usr/bin/conda"\nset _CONDA_ROOT "/usr"\nset _CONDA_EXE "/usr/bin/conda"\nset -gx CONDA_PYTHON_EXE "/usr/bin/python3"' \
          %{buildroot}%{_datadir}/fish/vendor_conf.d/conda.fish

# Install bash completion script
install -m 0644 -Dt %{buildroot}%{bash_completionsdir}/ %SOURCE1


%check
%if %{with tests}
export PATH=%{buildroot}%{_bindir}:$PATH
PYTHONPATH=%{buildroot}%{python3_sitelib} conda info

# Integration tests generally require network, so skip them.

# TestJson.test_list does not recognize /usr as a conda environment
# These fail on koji with PackageNotFound errors likely due to network issues
# test_cli.py::TestRun.test_run_returns_int
# test_cli.py::TestRun.test_run_returns_nonzero_errorlevel
# test_cli.py::TestRun.test_run_returns_zero_errorlevel

# test_ProgressiveFetchExtract_prefers_conda_v2_format, test_subdir_data_prefers_conda_to_tar_bz2,
# test_use_only_tar_bz2 fail in F31 koji, but not with mock --enablerepo=local. Let's disable
# them for now.
# tests/conda_env/test_create.py::test_create_update_remote_env_file requires network access
# tests/cli/test_conda_argparse.py::test_list_through_python_api does not recognize /usr as a conda environment
# tests/cli/test_main_{clean,info,list,list_reverse,rename}.py tests require network access
# tests/cli/test_main_notices.py::test_notices_appear_once_when_running_decorated_commands needs a conda_build fixture that we remove
# tests/cli/test_main_notices.py::test_notices_cannot_read_cache_files - TypeError: '<' not supported between instances of 'MagicMock' and 'int'
# tests/cli/test_main_run.py require /usr/bin/conda to be installed
# tests/cli/test_subcommands.py tests require network access
# tests/cli/test_subcommands.py::test_rename seems to need an active environment
# tests/test_misc.py::test_explicit_missing_cache_entries requires network access
# tests/core/test_initialize.py tries to unlink /usr/bin/python3 and fails when python is a release candidate
# tests/core/test_solve.py::test_cuda_fail_1 fails on non-x86_64
# tests/core/test_solve.py libmamba - some depsolving differences - TODO
# tests/core/test_solve.py libmamba - some depsolving differences - TODO
# tests/core/test_prefix_graph.py libmamba - some depsolving differences - TODO
# tests/trust/test_signature_verification.py requires conda_content_trust - not yet packaged
py.test-%{python3_version} -vv -m "not integration" \
    --deselect=tests/test_cli.py::TestJson::test_list \
    --deselect=tests/test_cli.py::test_run_returns_int \
    --deselect=tests/test_cli.py::test_run_returns_nonzero_errorlevel \
    --deselect=tests/test_cli.py::test_run_returns_zero_errorlevel \
    --deselect=tests/test_cli.py::test_run_readonly_env \
    --deselect=tests/test_misc.py::test_explicit_missing_cache_entries \
    --ignore=tests/conda_env/specs/test_binstar.py \
    --deselect=tests/conda_env/test_create.py::test_create_update_remote_env_file \
    --deselect='tests/cli/test_common.py::test_is_active_prefix[active_prefix-True]' \
    --deselect=tests/cli/test_conda_argparse.py::test_list_through_python_api \
    --deselect=tests/cli/test_main_clean.py \
    --deselect=tests/cli/test_main_info.py::test_info_conda_json \
    --deselect=tests/cli/test_main_list.py::test_list \
    --deselect=tests/cli/test_main_list.py::test_list_reverse \
    --deselect=tests/cli/test_main_notices.py::test_notices_appear_once_when_running_decorated_commands \
    --deselect=tests/cli/test_main_notices.py::test_notices_cannot_read_cache_files \
    --deselect=tests/cli/test_main_rename.py \
    --deselect=tests/cli/test_main_run.py \
    --deselect=tests/cli/test_subcommands.py::test_create[libmamba] \
    --deselect=tests/cli/test_subcommands.py::test_env_create \
    --deselect=tests/cli/test_subcommands.py::test_env_update \
    --deselect=tests/cli/test_subcommands.py::test_init \
    --deselect=tests/cli/test_subcommands.py::test_install \
    --deselect=tests/cli/test_subcommands.py::test_list \
    --deselect=tests/cli/test_subcommands.py::test_notices \
    --deselect=tests/cli/test_subcommands.py::test_remove_all_json[remove] \
    --deselect=tests/cli/test_subcommands.py::test_remove_all_json[uninstall] \
    --deselect=tests/cli/test_subcommands.py::test_rename \
    --deselect=tests/cli/test_subcommands.py::test_run \
    --deselect=tests/cli/test_subcommands.py::test_search \
    --deselect=tests/cli/test_subcommands.py::test_update[libmamba-update] \
    --deselect=tests/cli/test_subcommands.py::test_update[libmamba-upgrade] \
    --deselect=tests/cli/test_subcommands.py::test_update[update] \
    --deselect=tests/cli/test_subcommands.py::test_update[upgrade] \
    --deselect=tests/core/test_package_cache_data.py::test_ProgressiveFetchExtract_prefers_conda_v2_format \
    --deselect=tests/core/test_subdir_data.py::test_subdir_data_prefers_conda_to_tar_bz2 \
    --deselect=tests/core/test_subdir_data.py::test_use_only_tar_bz2 \
    --deselect=tests/core/test_initialize.py \
    --deselect=tests/core/test_solve.py::test_cuda_fail_1 \
    --deselect=tests/core/test_solve.py::test_conda_downgrade[libmamba] \
    --deselect=tests/core/test_solve.py::test_python2_update[libmamba] \
    --deselect=tests/core/test_solve.py::test_update_deps_2[libmamba] \
    --deselect=tests/core/test_solve.py::test_fast_update_with_update_modifier_not_set[libmamba] \
    --deselect=tests/core/test_solve.py::test_timestamps_1[libmamba] \
    --deselect=tests/core/test_solve.py::test_remove_with_constrained_dependencies[libmamba] \
    --deselect=tests/gateways/test_jlap.py::test_download_and_hash \
    --deselect=tests/gateways/test_jlap.py::test_jlap_fetch_ssl[True] \
    --deselect=tests/gateways/test_jlap.py::test_jlap_fetch_ssl[False] \
    --deselect=tests/test_plan.py::test_pinned_specs_conda_meta_pinned \
    --deselect=tests/test_plan.py::test_pinned_specs_condarc \
    --deselect=tests/test_plan.py::test_pinned_specs_all \
    --deselect=tests/cli/test_subcommands.py::test_compare[libmamba] \
    --deselect=tests/cli/test_subcommands.py::test_package[libmamba] \
    --deselect=tests/cli/test_subcommands.py::test_remove[libmamba-remove] \
    --deselect=tests/cli/test_subcommands.py::test_remove[libmamba-uninstall] \
    --deselect=tests/cli/test_subcommands.py::test_remove_all_json[libmamba-remove] \
    --deselect=tests/cli/test_subcommands.py::test_remove_all_json[libmamba-uninstall] \
    --deselect=tests/cli/test_subcommands.py::test_remove_all_json[classic-remove] \
    --deselect=tests/cli/test_subcommands.py::test_remove_all_json[classic-uninstall] \
    --deselect=tests/cli/test_subcommands.py::test_update[classic-update] \
    --deselect=tests/cli/test_subcommands.py::test_update[classic-upgrade] \
    --deselect=tests/cli/test_subcommands.py::test_env_remove[libmamba] \
    --deselect=tests/cli/test_subcommands.py::test_env_config_vars[libmamba] \
    --deselect=tests/core/test_subdir_data.py::test_subdir_data_coverage \
    --deselect=tests/models/test_prefix_graph.py::test_prefix_graph_1[libmamba] \
    --deselect=tests/models/test_prefix_graph.py::test_prefix_graph_2[libmamba] \
    --deselect=tests/models/test_prefix_graph.py::test_remove_youngest_descendant_nodes_with_specs[libmamba] \
    --deselect=tests/models/test_prefix_graph.py::test_deep_cyclical_dependency[libmamba] \
    --deselect=tests/plugins/subcommands/doctor/test_cli.py::test_conda_doctor_with_test_environment \
    --deselect=tests/core/test_prefix_data.py::test_get_environment_env_vars \
    --deselect=tests/core/test_prefix_data.py::test_set_unset_environment_env_vars \
    --deselect=tests/core/test_prefix_data.py::test_set_unset_environment_env_vars_no_exist \
    --ignore=tests/trust \
    conda tests
%endif

%files
%{_sysconfdir}/conda/
%{_bindir}/conda
%{_bindir}/conda-env
%{bash_completionsdir}/conda
# TODO - better ownership for fish/vendor_conf.d
%dir %{_datadir}/fish/vendor_conf.d
%{_datadir}/fish/vendor_conf.d/conda.fish
/etc/profile.d/conda.sh
/etc/profile.d/conda.csh

%files tests
%{_datadir}/conda/tests/

%files -n python%{python3_pkgversion}-conda -f %pyproject_files
%doc CHANGELOG.md README.md
%{_localstatedir}/cache/conda/
%dir %{_datadir}/conda/
%{_datadir}/conda/condarc.d/


%changelog
%autochangelog
