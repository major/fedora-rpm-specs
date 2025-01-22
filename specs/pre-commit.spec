%bcond check 1

Name:           pre-commit
Version:        4.1.0
Release:        %autorelease
Summary:        Framework for managing and maintaining multi-language pre-commit hooks

# SPDX
License:        MIT
URL:            https://pre-commit.com
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel

%if %{with check}
# All of the tests for the following require network access, so we can avoid
# pulling in these dependencies for now.
#
# BuildRequires:  R-core
# BuildRequires:  cabal-install
# BuildRequires:  conda
# BuildRequires:  dotnet-host
# BuildRequires:  dotnet-hostfxr-7.0
# BuildRequires:  dotnet-sdk-7.0
# BuildRequires:  ghc-compiler
# BuildRequires:  golang-bin
# BuildRequires:  julia

# These BR’s would enable a few extra tests, but are inconveniently
# ExclusiveArch. If we wanted to conditionalize BR’s based on build
# architecture, we would have to make *this* package arched.
#
# BuildRequires:  swift-lang

BuildRequires:  cargo
BuildRequires:  lua-devel
BuildRequires:  luarocks
BuildRequires:  nodejs
BuildRequires:  npm
BuildRequires:  perl-CPAN
BuildRequires:  ruby
BuildRequires:  rubygems

# Manually added to speed up the %%check section
BuildRequires:  python3dist(pytest-xdist)
%endif

%description
A framework for managing and maintaining multi-language pre-commit hooks.


%prep
%autosetup -p1 -S git
# Do not generate BR’s for coverage, linters, etc.:
sed -r '/^(covdefaults|coverage)\b/d' requirements-dev.txt |
  tee requirements-dev-filtered.txt


%generate_buildrequires
%pyproject_buildrequires -r %{?with_check:requirements-dev-filtered.txt}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pre_commit


%if %{with check}
%check
# For general discusson on test failures building distribution packages, see:
# https://github.com/pre-commit/pre-commit/issues/1183,
# https://github.com/pre-commit/pre-commit/issues/1202
#
# Require network access:
# See https://github.com/pre-commit/pre-commit/issues/1202
k="${k-}${k+ and }not test_additional_dependencies_roll_forward"
k="${k-}${k+ and }not test_additional_golang_dependencies_installed"
k="${k-}${k+ and }not test_additional_node_dependencies_installed"
k="${k-}${k+ and }not test_additional_ruby_dependencies_installed"
k="${k-}${k+ and }not test_additional_rust_cli_dependencies_installed"
k="${k-}${k+ and }not test_additional_rust_lib_dependencies_installed"
k="${k-}${k+ and }not test_automatic_toolchain_switching"
k="${k-}${k+ and }not test_automatic_toolchain_switching_go_fmt"
k="${k-}${k+ and }not test_conda_additional_deps"
k="${k-}${k+ and }not test_conda_hook"
k="${k-}${k+ and }not test_conda_language"
k="${k-}${k+ and }not test_conda_with_additional_dependencies_hook"
k="${k-}${k+ and }not test_control_c_control_c_on_install"
k="${k-}${k+ and }not test_dotnet_combo_proj1"
k="${k-}${k+ and }not test_dotnet_combo_proj2"
k="${k-}${k+ and }not test_dotnet_csproj"
k="${k-}${k+ and }not test_dotnet_csproj_prefix"
k="${k-}${k+ and }not test_dotnet_hook"
k="${k-}${k+ and }not test_dotnet_sln"
k="${k-}${k+ and }not test_during_commit_all"
k="${k-}${k+ and }not test_golang_default_version"
k="${k-}${k+ and }not test_golang_hook"
k="${k-}${k+ and }not test_golang_hook_still_works_when_gobin_is_set"
k="${k-}${k+ and }not test_golang_infer_go_version_default"
k="${k-}${k+ and }not test_golang_system"
k="${k-}${k+ and }not test_golang_system_hook"
k="${k-}${k+ and }not test_golang_versioned"
k="${k-}${k+ and }not test_golang_versioned_hook"
k="${k-}${k+ and }not test_golang_with_recursive_submodule"
k="${k-}${k+ and }not test_health_check_after_downgrade"
k="${k-}${k+ and }not test_health_check_healthy"
k="${k-}${k+ and }not test_health_check_without_version"
k="${k-}${k+ and }not test_healthy_default_creator"
k="${k-}${k+ and }not test_healthy_venv_creator"
k="${k-}${k+ and }not test_install_ruby_with_version"
k="${k-}${k+ and }not test_installs_rust_missing_rustup"
k="${k-}${k+ and }not test_installs_with_bootstrapped_rustup"
k="${k-}${k+ and }not test_installs_with_existing_rustup"
k="${k-}${k+ and }not test_installs_without_links_outside_env"
k="${k-}${k+ and }not test_invalidated_virtualenv"
k="${k-}${k+ and }not test_julia_hook"
k="${k-}${k+ and }not test_julia_hook_additional_deps"
k="${k-}${k+ and }not test_julia_hook_args"
k="${k-}${k+ and }not test_julia_hook_manifest"
k="${k-}${k+ and }not test_julia_repo_local"
k="${k-}${k+ and }not test_language_versioned_python_hook"
k="${k-}${k+ and }not test_local_conda_additional_dependencies"
k="${k-}${k+ and }not test_local_golang_additional_dependencies"
k="${k-}${k+ and }not test_local_golang_additional_deps"
k="${k-}${k+ and }not test_local_lua_additional_dependencies"
k="${k-}${k+ and }not test_local_perl_additional_dependencies"
k="${k-}${k+ and }not test_local_python_repo"
k="${k-}${k+ and }not test_local_rust_additional_dependencies"
k="${k-}${k+ and }not test_lua_additional_dependencies"
k="${k-}${k+ and }not test_node_additional_deps"
k="${k-}${k+ and }not test_node_hook_versions"
k="${k-}${k+ and }not test_perl_additional_dependencies"
k="${k-}${k+ and }not test_python_hook_weird_setup_cfg"
k="${k-}${k+ and }not test_python_venv_deprecation"
k="${k-}${k+ and }not test_r_hook"
k="${k-}${k+ and }not test_r_inline"
k="${k-}${k+ and }not test_r_inline_hook"
k="${k-}${k+ and }not test_r_local_with_additional_dependencies_hook"
k="${k-}${k+ and }not test_r_with_additional_dependencies_hook"
k="${k-}${k+ and }not test_really_long_file_paths"
k="${k-}${k+ and }not test_reinstall"
k="${k-}${k+ and }not test_repository_state_compatibility[v1]"
k="${k-}${k+ and }not test_repository_state_compatibility[v2]"
k="${k-}${k+ and }not test_ruby_additional_deps"
k="${k-}${k+ and }not test_ruby_hook_default"
k="${k-}${k+ and }not test_ruby_hook_language_version"
k="${k-}${k+ and }not test_ruby_with_bundle_disable_shared_gems"
k="${k-}${k+ and }not test_run_a_node_hook_default_version"
k="${k-}${k+ and }not test_run_dep"
k="${k-}${k+ and }not test_run_example_executable"
k="${k-}${k+ and }not test_run_lib_additional_dependencies"
k="${k-}${k+ and }not test_run_ruby_hook_with_disable_shared_gems"
k="${k-}${k+ and }not test_run_versioned_node_hook"
k="${k-}${k+ and }not test_run_versioned_ruby_hook"
k="${k-}${k+ and }not test_rust_cli_additional_dependencies"
k="${k-}${k+ and }not test_simple_python_hook"
k="${k-}${k+ and }not test_simple_python_hook_default_version"
k="${k-}${k+ and }not test_unhealthy_old_virtualenv"
k="${k-}${k+ and }not test_unhealthy_python_goes_missing"
k="${k-}${k+ and }not test_unhealthy_system_version_changes"
k="${k-}${k+ and }not test_unhealthy_then_replaced"
k="${k-}${k+ and }not test_unhealthy_unexpected_pyvenv"
k="${k-}${k+ and }not test_unhealthy_with_version_change"
# Fails in koji but not in mock (Executable `ruby_hook` not found)
k="${k-}${k+ and }not test_ruby_hook_system"
# Requires rustup (not packaged), and would require network access even if
# rustup were available:
k="${k-}${k+ and }not test_language_version_with_rustup"
# Requires coursier (not packaged):
k="${k-}${k+ and }not test_coursier_hook"
k="${k-}${k+ and }not test_coursier_hook_additional_dependencies"
k="${k-}${k+ and }not test_error_if_no_deps_or_channel"
# Requires dart (not packaged):
k="${k-}${k+ and }not test_dart"
k="${k-}${k+ and }not test_dart_additional_deps"
k="${k-}${k+ and }not test_dart_additional_deps_versioned"
k="${k-}${k+ and }not test_dart_hook"
k="${k-}${k+ and }not test_local_dart_additional_dependencies"
k="${k-}${k+ and }not test_local_dart_additional_dependencies_versioned"
# Requires swift-lang, which we have chosen not to BuildRequire; see comments
# earlier in the spec file:
k="${k-}${k+ and }not test_swift_language"
# Requires docker (not packaged)
k="${k-}${k+ and }not test_docker_hook"
k="${k-}${k+ and }not test_docker_image_color_tty"
k="${k-}${k+ and }not test_docker_image_hook_via_args"
k="${k-}${k+ and }not test_docker_image_hook_via_entrypoint"
k="${k-}${k+ and }not test_docker_image_no_color_no_tty"
# Does not work under (i.e., respect) an “external” PYTHONPATH
k="${k-}${k+ and }not test_installed_from_venv"
# Fails in koji but not local mock (hook exits with code 1, no useful output)
k="${k-}${k+ and }not test_run_a_ruby_hook"
%pytest -v -k "${k-}" -n %{_smp_build_ncpus}
%endif


%files -f %{pyproject_files}
%doc README.md CHANGELOG.md CONTRIBUTING.md
%{_bindir}/pre-commit


%changelog
%autochangelog
