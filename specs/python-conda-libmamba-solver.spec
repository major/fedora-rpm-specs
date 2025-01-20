%global srcname conda-libmamba-solver

%bcond tests 1

Name:           python-%{srcname}
Version:        24.9.0
Release:        2%{?dist}
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
export CONDA_TEST_DATA_DIR=/usr/share/conda/tests/data
%pytest -v \
  --deselect=tests/test_channels.py::test_channel_matchspec \
  --deselect=tests/test_channels.py::test_channels_prefixdata \
  --deselect=tests/test_channels.py::test_channels_installed_unavailable \
  --deselect=tests/test_channels.py::test_http_server_auth_token_in_defaults \
  --deselect=tests/test_channels.py::test_local_spec \
  --deselect=tests/test_channels.py::test_mirrors_do_not_leak_channels\[_setup_channels_alias\] \
  --deselect=tests/test_channels.py::test_mirrors_do_not_leak_channels\[_setup_channels_custom\] \
  --deselect=tests/test_channels.py::test_jax_and_jaxlib \
  --deselect=tests/test_channels.py::test_encoding_file_paths \
  --deselect=tests/test_channels.py::test_conda_build_with_aliased_channels \
  --deselect=tests/test_channels.py::test_unknown_channels_do_not_crash \
  --deselect=tests/test_channels.py::test_use_cache_works_offline_fresh_install_keep \
  --deselect=tests/test_downstream.py::test_build_recipe\[jedi] \
  --deselect=tests/test_downstream.py::test_build_recipe\[multioutput] \
  --deselect=tests/test_downstream.py::test_build_recipe\[stackvana] \
  --deselect=tests/test_downstream.py::test_conda_lock \
  --deselect=tests/test_performance.py::test_a_warmup\[mambaforge.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_a_warmup\[mambaforge.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_update_python\[mambaforge.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_update_python\[mambaforge.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_install_python_update_deps\[mambaforge.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_install_python_update_deps\[mambaforge.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_update_all\[mambaforge.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_update_all\[mambaforge.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_a_warmup\[gvleobas.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_a_warmup\[gvleobas.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_update_python\[gvleobas.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_update_python\[gvleobas.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_install_python_update_deps\[gvleobas.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_install_python_update_deps\[gvleobas.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_update_all\[gvleobas.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_update_all\[gvleobas.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_a_warmup\[pangeo_ml_notebook.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_a_warmup\[pangeo_ml_notebook.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_update_python\[pangeo_ml_notebook.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_update_python\[pangeo_ml_notebook.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_install_python_update_deps\[pangeo_ml_notebook.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_install_python_update_deps\[pangeo_ml_notebook.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_update_all\[pangeo_ml_notebook.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_update_all\[pangeo_ml_notebook.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_a_warmup\[silverback9876.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_a_warmup\[silverback9876.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_update_python\[silverback9876.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_update_python\[silverback9876.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_install_python_update_deps\[silverback9876.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_install_python_update_deps\[silverback9876.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_update_all\[silverback9876.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_update_all\[silverback9876.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_a_warmup\[scipipe.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_a_warmup\[scipipe.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_update_python\[scipipe.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_update_python\[scipipe.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_install_python_update_deps\[scipipe.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_install_python_update_deps\[scipipe.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_update_all\[scipipe.linux-64.lock-libmamba] \
  --deselect=tests/test_performance.py::test_update_all\[scipipe.linux-64.lock-classic] \
  --deselect=tests/test_performance.py::test_install_vaex_from_conda_forge_and_defaults\[libmamba] \
  --deselect=tests/test_performance.py::test_install_vaex_from_conda_forge_and_defaults\[classic] \
  --deselect=tests/test_repoquery.py \
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
  --deselect=tests/test_state.py::test_create_requested_and_pinned \
  --deselect=tests/test_state.py::test_python_updates \
  --deselect=tests/test_workarounds.py::test_matchspec_star_version \
  --deselect=tests/test_workarounds.py::test_build_string_filters \
  --deselect='tests/test_workarounds.py::test_ctrl_c[Solving environment]'
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 18 2024 Orion Poplawski <orion@nwra.com> - 24.9.0-1
- Update to 24.9.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 23.11.1-5
- Bootstrap for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 20 2023 Karolina Surma <ksurma@redhat.com> - 23.11.1-2
- Conditionalize test run to avoid circular dependency on conda

* Sat Dec 02 2023 Orion Poplawski <orion@nwra.com> - 23.11.1-1
- Initial Fedora package
