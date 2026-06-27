%global srcname conda-libmamba-solver

%bcond tests 1

Name:           python-%{srcname}
Version:        26.4.2
Release:        %autorelease
Summary:        The libmamba based solver for conda

License:        BSD-3-Clause
URL:            https://github.com/conda/conda-libmamba-solver
Source:         %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  conda
BuildRequires:  conda-build
BuildRequires:  conda-tests
BuildRequires:  python3-conda-index
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-xprocess
%endif

%global _description %{expand:
conda-libmamba-solver is a new solver for the conda package manager which
uses the solver from the mamba project behind the scenes, while carefully
implementing conda's functionality and expected behaviors on top. The
library used by mamba to do the heavy-lifting is called libsolv.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}
sed -i -e '/tool.hatch.version/afallback-version = "%{version}"' pyproject.toml
sed -i -e '/doctest/d' -e '/reruns/d' pyproject.toml
# Re-enable libmambapy dependency removed in https://github.com/conda/conda-libmamba-solver/pull/641
sed -i -e '/libmambapy/s/#//' pyproject.toml
# Do not require pytest-codspeed (for uploading test results)
sed -i -e '/pytest-codspeed/d' tests/requirements.txt


%generate_buildrequires
# When not testing, we don't need runtime dependencies.
# Normally, we would still BuildRequire them to not accidentally
# build an uninstallabe package,
# but there is a runtime dependency loop with conda
%pyproject_buildrequires %{!?with_tests:-R}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files conda_libmamba_solver


%check
%if %{with tests}
# Most tests require network access
# FileNotFoundError: [Errno 2] No such file or directory: 'conda-lock'
# tests/test_index.py::test_load_channel_repo_info_shards - uses pytest_codspeed
# tests/test_shards_subset.py - imports pytest_codspeed
export CONDA_TEST_DATA_DIR=/usr/share/conda/tests/data
%pytest -v \
  --ignore=tests/test_performance.py \
  --ignore=tests/test_shards_subset.py \
  --deselect=tests/test_channels.py::test_channel_matchspec \
  --deselect=tests/test_channels.py::test_channels_prefixdata \
  --deselect=tests/test_channels.py::test_channels_installed_unavailable \
  --deselect=tests/test_channels.py::test_conda_build_with_aliased_channels \
  --deselect=tests/test_channels.py::test_encoding_file_paths \
  --deselect=tests/test_channels.py::test_http_server_auth_token_in_defaults \
  --deselect=tests/test_channels.py::test_jax_and_jaxlib \
  --deselect=tests/test_channels.py::test_local_spec \
  --deselect=tests/test_channels.py::test_mirrors_do_not_leak_channels\[_setup_channels_alias] \
  --deselect=tests/test_channels.py::test_mirrors_do_not_leak_channels\[_setup_channels_custom] \
  --deselect=tests/test_channels.py::test_nameless_channel \
  --deselect=tests/test_channels.py::test_unknown_channels_do_not_crash \
  --deselect=tests/test_channels.py::test_use_cache_works_offline_fresh_install_keep \
  --deselect=tests/test_downstream.py::test_build_recipe\[jedi] \
  --deselect=tests/test_downstream.py::test_build_recipe\[multioutput] \
  --deselect=tests/test_downstream.py::test_build_recipe\[stackvana] \
  --deselect=tests/test_downstream.py::test_conda_lock \
  --deselect='tests/test_index.py::test_defaults_use_only_tar_bz2[CONDA_USE_ONLY_TAR_BZ2=true]' \
  --deselect='tests/test_index.py::test_defaults_use_only_tar_bz2[CONDA_USE_ONLY_TAR_BZ2=false]' \
  --deselect=tests/test_index.py::test_given_channels \
  --deselect=tests/test_index.py::test_load_channel_repo_info_shards \
  --deselect=tests/test_repoquery.py \
  --deselect=tests/test_shards.py::test_batch_retrieve_from_cache \
  --deselect=tests/test_shards.py::test_build_repodata_subset \
  --deselect=tests/test_shards.py::test_fetch_shards_channels \
  --deselect=tests/test_shards.py::test_fetch_shards_index_mark_unavailable[404] \
  --deselect=tests/test_shards.py::test_fetch_shards_index_mark_unavailable[405] \
  --deselect=tests/test_solver.py::test_ca_certificates_pins \
  --deselect=tests/test_solver.py::test_constraining_pin_and_requested \
  --deselect=tests/test_solver.py::test_defaults_specs_work \
  --deselect=tests/test_solver.py::test_determinism \
  --deselect=tests/test_solver.py::test_install_virtual_packages[__glibc] \
  --deselect=tests/test_solver.py::test_install_virtual_packages[__unix] \
  --deselect=tests/test_solver.py::test_install_virtual_packages[__linux] \
  --deselect=tests/test_solver.py::test_install_virtual_packages[__osx] \
  --deselect=tests/test_solver.py::test_install_virtual_packages[__win] \
  --deselect=tests/test_solver.py::test_track_features_recorded_correctly[True] \
  --deselect=tests/test_solver.py::test_track_features_recorded_correctly[False] \
  --deselect=tests/test_solver.py::test_locking_pins \
  --deselect=tests/test_solver.py::test_pinned_with_cli_build_string \
  --deselect=tests/test_solver.py::test_python_downgrade_reinstalls_noarch_packages \
  --deselect=tests/test_solver.py::test_too_aggressive_update_to_conda_forge_packages \
  --deselect=tests/test_solver.py::test_update_from_latest_not_downgrade \
  --deselect=tests/test_solver.py::test_python_update_should_not_uninstall_history \
  --deselect=tests/test_solver.py::test_python_downgrade_with_pins_removes_truststore \
  --deselect=tests/test_solver.py::test_urls_are_percent_decoded \
  --deselect=tests/test_solver.py::test_prune_existing_env \
  --deselect=tests/test_solver.py::test_prune_existing_env_dependencies_are_solved \
  --deselect=tests/test_solver.py::test_satisfied_skip_solve_matchspec \
  --deselect=tests/test_solver.py::test_shard_cache_multiple \
  --deselect=tests/test_solver.py::test_pytorch_gpu[pytorch] \
  --deselect='tests/test_solver.py::test_pytorch_gpu[pytorch>0]' \
  --deselect='tests/test_solver.py::test_pytorch_gpu[pytorch=2]' \
  --deselect=tests/test_solver.py::test_channel_subdir_set_correctly \
  --deselect=tests/test_solver.py::test_python_site_packages_path \
  --deselect=tests/test_solver_differences.py \
  --deselect=tests/test_solvers.py::test_python_downgrade_reinstalls_noarch_packages \
  --deselect=tests/test_solvers.py::test_defaults_specs_work \
  --deselect=tests/test_solvers.py::test_determinism \
  --deselect=tests/test_solvers.py::test_update_from_latest_not_downgrade \
  --deselect=tests/test_solvers.py::test_too_aggressive_update_to_conda_forge_packages \
  --deselect=tests/test_solvers.py::test_pinned_with_cli_build_string \
  --deselect=tests/test_solvers.py::test_constraining_pin_and_requested \
  --deselect=tests/test_solvers.py::test_locking_pins \
  --deselect=tests/test_solvers.py::test_ca_certificates_pins \
  --deselect=tests/test_solvers.py::test_python_update_should_not_uninstall_history \
  --deselect=tests/test_solvers.py::test_python_downgrade_with_pins_removes_truststore \
  --deselect=tests/test_channels.py::test_channel_ordering \
  --deselect=tests/test_state.py::test_create_requested_and_pinned \
  --deselect=tests/test_state.py::test_python_updates \
  --deselect=tests/test_workarounds.py::test_matchspec_star_version \
  --deselect=tests/test_workarounds.py::test_build_string_filters \
  --deselect=tests/test_workarounds.py::test_ctrl_c[Collecting\ package\ metadata-shards] \
  --deselect=tests/test_workarounds.py::test_ctrl_c[Collecting\ package\ metadata-noshards] \
  --deselect=tests/test_workarounds.py::test_ctrl_c[Solving\ environment] \
  --deselect=tests/test_workarounds.py::test_ctrl_c[Solving\ environment-noshards] \
  --deselect=tests/test_workarounds.py::test_ctrl_c[Solving\ environment-shards]
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.*

%changelog
%autochangelog
