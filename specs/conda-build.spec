%bcond_without tests

Name:           conda-build
Version:        25.11.1
Release:        %autorelease
Summary:        Commands and tools for building conda packages
# version.py is BSD-2-Clause
License:        BSD-3-Clause AND BSD-2-Clause
URL:            https://github.com/conda/conda-build
Source0:        https://github.com/conda/conda-build/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
Requires:       python%{python3_pkgversion}-conda-build = %{version}-%{release}

%global _description %{expand:
You can easily build your own packages for conda, and upload them to
anaconda.org, a free service for hosting packages for conda, as well as other
package managers. To build a package, create a recipe. See
http://github.com/conda/conda-recipes for many example recipes, and
http://conda.pydata.org/docs/build.html for documentation on how to build
recipes.

To upload to anaconda.org, create an account. Then, install the
anaconda-client and login

$ conda install anaconda-client
$ anaconda login

Then, after you build your recipe

$ conda build <recipe-dir>

you will be prompted to upload to anaconda.org.

To add your anaconda.org channel, or the channel of others to conda so that
conda install will find and install their packages, run

$ conda config --add channels https://conda.anaconda.org/username

(replacing username with the user name of the person whose channel you want to
add).}

%description %_description

%package -n python%{python3_pkgversion}-conda-build
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
# For tests
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-mock
BuildRequires:  python%{python3_pkgversion}-conda-index
BuildRequires:  python%{python3_pkgversion}-flaky
# For docs
BuildRequires:  python%{python3_pkgversion}-myst-parser
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-conda-sphinx-theme
BuildRequires:  conda
BuildRequires:  /usr/bin/hostname
BuildRequires:  /usr/bin/git
BuildRequires:  /usr/bin/python

%description -n python%{python3_pkgversion}-conda-build %_description

%prep
%autosetup -p1
# lief is not yet packaged and is not a hard dependency
sed -i -e '/lief/d' pyproject.toml
# Unpackaged and unneeded test deps
sed -i -E -e '/^(py-lief|python|python-libarchive-c|ripgrep)( .*)?$/d' tests/requirements.txt
# pytz isn't used but referenced in deps
sed -i -e '/pytz/d' recipe/meta.yaml pyproject.toml tests/requirements.txt
# do not run coverage/xdoctest in pytest
sed -i -E -e '/--(no-)?cov/d' -e '/xdoctest/d' pyproject.toml
# Not needed for man pages
sed -i -E -e '/linkify/d' -e '/sphinx_(design|sitemap)/d' docs/source/conf.py


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:tests/requirements.txt}


%build
%pyproject_wheel
make -C docs man


%install
%pyproject_install
%pyproject_save_files conda_build
mkdir -p %{buildroot}%{_mandir}/man1
cp -p docs/_build/man/*.1 %{buildroot}%{_mandir}/man1/

%check
%if %{with tests}
export PATH=%{buildroot}%{_bindir}:$PATH
# test_api_build.py - requires unpackaged binstar_client
# Most tests require network access to the anaconda repositories
# Needs an environment to test
# tests/test_post.py::test_menuinst_* - conda_build.environ.InvalidEnvironment: Unable to load environment /usr
# tests/test_api_render.py::test_get_output_file_paths_jinja2 - Requires GIT/CI env
# tests/test_api_render.py::test_noarch_with_no_platform_deps - fails in koji for an unknown reason
# tests/test_api_render.py::test_transitive_subpackage_dependency - nettwork
py.test-%{python3_version} -rs -vv -W ignore::DeprecationWarning -W ignore::PendingDeprecationWarning \
  --ignore tests/test_api_build.py --ignore tests/cli/test_main_skeleton.py \
  --deselect='tests/test_api_build_conda_v2.py::test_conda_pkg_format[None-.tar.bz2]' \
  --deselect='tests/test_api_build_conda_v2.py::test_conda_pkg_format[2-.conda]' \
  --deselect='tests/test_api_build_dll_package.py::test_recipe_build' \
  --deselect='tests/test_api_build_go_package.py::test_recipe_build' \
  --deselect='tests/test_api_convert.py::test_show_imports[package0-linux]' \
  --deselect='tests/test_api_convert.py::test_show_imports[package0-win]' \
  --deselect='tests/test_api_convert.py::test_show_imports[package0-osx]' \
  --deselect='tests/test_api_convert.py::test_no_imports_found[package0-linux]' \
  --deselect='tests/test_api_convert.py::test_no_imports_found[package0-win]' \
  --deselect='tests/test_api_convert.py::test_no_imports_found[package0-osx]' \
  --deselect='tests/test_api_convert.py::test_no_platform[package0-linux]' \
  --deselect='tests/test_api_convert.py::test_no_platform[package0-win]' \
  --deselect='tests/test_api_convert.py::test_no_platform[package0-osx]' \
  --deselect='tests/test_api_convert.py::test_c_extension_error[package0-linux]' \
  --deselect='tests/test_api_convert.py::test_c_extension_error[package0-win]' \
  --deselect='tests/test_api_convert.py::test_c_extension_error[package0-osx]' \
  --deselect='tests/test_api_convert.py::test_c_extension_conversion[package0-linux]' \
  --deselect='tests/test_api_convert.py::test_c_extension_conversion[package0-win]' \
  --deselect='tests/test_api_convert.py::test_c_extension_conversion[package0-osx]' \
  --deselect='tests/test_api_convert.py::test_convert_platform_to_others[package0-linux]' \
  --deselect='tests/test_api_convert.py::test_convert_platform_to_others[package0-win]' \
  --deselect='tests/test_api_convert.py::test_convert_platform_to_others[package0-osx]' \
  --deselect='tests/test_api_convert.py::test_convert_platform_to_others[package1-linux]' \
  --deselect='tests/test_api_convert.py::test_convert_platform_to_others[package1-win]' \
  --deselect='tests/test_api_convert.py::test_convert_platform_to_others[package1-osx]' \
  --deselect='tests/test_api_convert.py::test_convert_from_unix_to_win_creates_entry_points' \
  --deselect='tests/test_api_convert.py::test_convert_dependencies[package0-linux]' \
  --deselect='tests/test_api_convert.py::test_convert_dependencies[package0-win]' \
  --deselect='tests/test_api_convert.py::test_convert_dependencies[package0-osx]' \
  --deselect='tests/test_api_convert.py::test_convert_no_dependencies[package0-linux]' \
  --deselect='tests/test_api_convert.py::test_convert_no_dependencies[package0-win]' \
  --deselect='tests/test_api_convert.py::test_convert_no_dependencies[package0-osx]' \
  --deselect='tests/test_api_convert.py::test_skip_conversion[package0-linux]' \
  --deselect='tests/test_api_convert.py::test_skip_conversion[package0-win]' \
  --deselect='tests/test_api_convert.py::test_skip_conversion[package0-osx]' \
  --deselect='tests/test_api_convert.py::test_renaming_executables[package0-linux]' \
  --deselect='tests/test_api_convert.py::test_renaming_executables[package0-osx]' \
  --deselect='tests/test_api_debug.py::test_debug[outputs w/ invalid filtering]' \
  --deselect='tests/test_api_debug.py::test_debug[outputs w/ no filtering]' \
  --deselect='tests/test_api_debug.py::test_debug[outputs w/ valid filtering]' \
  --deselect='tests/test_api_debug.py::test_debug[recipe w/ config]' \
  --deselect='tests/test_api_debug.py::test_debug[tarball w/ config]' \
  --deselect='tests/test_api_debug.py::test_debug[recipe w/ path]' \
  --deselect='tests/test_api_debug.py::test_debug[tarball w/ path]' \
  --deselect='tests/test_api_inspect.py::test_check_recipe' \
  --deselect=tests/test_api_render.py::test_get_output_file_paths_jinja2 \
  --deselect='tests/test_api_render.py::test_hash_no_apply_to_custom_build_string' \
  --deselect='tests/test_api_render.py::test_host_entries_finalized' \
  --deselect='tests/test_api_render.py::test_merge_build_host_build_key' \
  --deselect='tests/test_api_render.py::test_merge_build_host_empty_host_section' \
  --deselect='tests/test_api_render.py::test_noarch_with_platform_deps' \
  --deselect='tests/test_api_render.py::test_output_without_jinja_does_not_download' \
  --deselect='tests/test_api_render.py::test_noarch_with_no_platform_deps' \
  --deselect='tests/test_api_render.py::test_pin_compatible_semver' \
  --deselect='tests/test_api_render.py::test_pin_depends' \
  --deselect='tests/test_api_render.py::test_render_need_download' \
  --deselect='tests/test_api_render.py::test_render_yaml_output' \
  --deselect='tests/test_api_render.py::test_resolved_packages_recipe' \
  --deselect='tests/test_api_render.py::test_run_exports_with_pin_compatible_in_subpackages' \
  --deselect='tests/test_api_render.py::test_transitive_subpackage_dependency' \
  --deselect='tests/test_api_skeleton_cpan.py::test_xs_needs_c_compiler' \
  --deselect='tests/test_api_skeleton_cran.py::test_cran_no_comments' \
  --deselect='tests/test_api_skeleton.py::test_sympy[with version]' \
  --deselect='tests/test_api_skeleton.py::test_sympy[with url]' \
  --deselect='tests/test_api_skeleton.py::test_get_package_metadata' \
  --deselect='tests/test_api_skeleton.py::test_pypi_with_setup_options' \
  --deselect='tests/test_api_skeleton.py::test_pypi_pin_numpy' \
  --deselect='tests/test_api_skeleton.py::test_pypi_version_sorting' \
  --deselect='tests/test_api_skeleton.py::test_pypi_with_entry_points' \
  --deselect='tests/test_api_skeleton.py::test_pypi_with_version_arg' \
  --deselect='tests/test_api_skeleton.py::test_pypi_with_extra_specs' \
  --deselect='tests/test_api_skeleton.py::test_pypi_with_version_inconsistency' \
  --deselect='tests/test_api_skeleton.py::test_pypi_with_basic_environment_markers' \
  --deselect='tests/test_api_skeleton.py::test_setuptools_test_requirements' \
  --deselect='tests/test_api_skeleton.py::test_pypi_section_order_preserved' \
  --deselect='tests/test_api_test.py::test_recipe_test' \
  --deselect='tests/test_api_test.py::test_package_test' \
  --deselect='tests/test_api_test.py::test_package_test_without_recipe_in_package' \
  --deselect='tests/test_api_test.py::test_package_with_jinja2_does_not_redownload_source' \
  --deselect='tests/test_api_test.py::test_api_extra_dep' \
  --deselect='tests/test_build.py::test_build_preserves_PATH' \
  --deselect='tests/test_build.py::test_rewrite_output' \
  --deselect='tests/test_conda_interface.py::test_get_installed_version' \
  --deselect='tests/test_cpan_skeleton.py::test_core_modules' \
  --deselect='tests/test_environ.py::test_environment_creation_preserves_PATH' \
  --deselect='tests/test_inspect.py::test_inspect_linkages' \
  --deselect='tests/test_inspect.py::test_inspect_objects' \
  --deselect='tests/test_inspect.py::test_channel_installable' \
  --deselect='tests/test_jinja_context.py::test_resolved_packages' \
  --deselect='tests/test_metadata.py::test_build_bootstrap_env_by_name' \
  --deselect='tests/test_metadata.py::test_build_bootstrap_env_by_path' \
  --deselect=tests/test_post.py::test_file_hash \
  --deselect=tests/test_post.py::test_menuinst_validation_ok \
  --deselect=tests/test_post.py::test_menuinst_validation_fails_bad_schema \
  --deselect=tests/test_post.py::test_menuinst_validation_fails_bad_json \
  --deselect='tests/test_post.py::test_postlink_script_in_output_explicit' \
  --deselect='tests/test_post.py::test_postlink_script_in_output_implicit' \
  --deselect='tests/test_post.py::test_pypi_installer_metadata' \
  --deselect=tests/test_post.py::test_rpath_symlink \
  --deselect='tests/test_published_examples.py::test_recipe_builds[building_jinja2_direct_env_vars]' \
  --deselect='tests/test_published_examples.py::test_recipe_builds[building_jinja2_setup_py_data]' \
  --deselect='tests/test_published_examples.py::test_recipe_builds[building_jinja2_environ]' \
  --deselect='tests/test_published_examples.py::test_skeleton_pypi' \
  --deselect='tests/test_source.py::test_multiple_different_sources' \
  --deselect='tests/test_source.py::test_git_repo_with_single_subdir_does_not_enter_subdir' \
  --deselect='tests/test_subpackages.py::test_autodetect_raises_on_invalid_extension' \
  --deselect='tests/test_subpackages.py::test_build_string_does_not_incorrectly_add_hash' \
  --deselect='tests/test_subpackages.py::test_circular_deps_cross' \
  --deselect='tests/test_subpackages.py::test_git_in_output_version' \
  --deselect='tests/test_subpackages.py::test_intradep_with_templated_output_name' \
  --deselect='tests/test_subpackages.py::test_multi_outputs_without_package_version' \
  --deselect='tests/test_subpackages.py::test_subpackage_recipes[noarch_subpackage]' \
  --deselect='tests/test_subpackages.py::test_subpackage_recipes[copying_files]' \
  --deselect='tests/test_subpackages.py::test_subpackage_recipes[script_install_files]' \
  --deselect='tests/test_subpackages.py::test_subpackage_recipes[python_test_dep]' \
  --deselect='tests/test_subpackages.py::test_subpackage_recipes[script_bash_windows]' \
  --deselect='tests/test_subpackages.py::test_subpackage_recipes[test_files_in_parent]' \
  --deselect='tests/test_subpackages.py::test_subpackage_recipes[test_files_copying]' \
  --deselect='tests/test_subpackages.py::test_subpackage_recipes[compose_run_requirements_from_subpackages]' \
  --deselect='tests/test_subpackages.py::test_subpackage_recipes[outputs_using_vars_defined_in_meta]' \
  --deselect='tests/test_subpackages.py::test_subpackage_recipes[split_packages_hash_resolution]' \
  --deselect='tests/test_subpackages.py::test_subpackage_recipes[script_autodetect_interpreter]' \
  --deselect='tests/test_subpackages.py::test_subpackage_recipes[jinja2_subpackage_name]' \
  --deselect='tests/test_subpackages.py::test_rm_rf_does_not_remove_relative_source_package_files' \
  --deselect='tests/test_subpackages.py::test_subpackage_independent_hash' \
  --deselect='tests/test_subpackages.py::test_run_exports_in_subpackage' \
  --deselect='tests/test_subpackages.py::test_subpackage_variant_override' \
  --deselect='tests/test_subpackages.py::test_intradependencies' \
  --deselect='tests/test_subpackages.py::test_about_metadata' \
  --deselect='tests/test_subpackages.py::test_toplevel_entry_points_do_not_apply_to_subpackages' \
  --deselect='tests/test_subpackages.py::test_subpackage_hash_inputs' \
  --deselect='tests/test_subpackages.py::test_overlapping_files' \
  --deselect='tests/test_subpackages.py::test_per_output_tests' \
  --deselect='tests/test_subpackages.py::test_per_output_tests_script' \
  --deselect='tests/test_subpackages.py::test_pin_compatible_in_outputs' \
  --deselect='tests/test_subpackages.py::test_subpackage_order_natural' \
  --deselect='tests/test_subpackages.py::test_subpackage_order_bad' \
  --deselect='tests/test_subpackages.py::test_subpackage_script_and_files' \
  --deselect='tests/test_subpackages.py::test_build_script_and_script_env' \
  --deselect='tests/test_subpackages.py::test_python_line_up_with_compiled_lib[_line_up_python_compiled_libs]' \
  --deselect='tests/test_subpackages.py::test_python_line_up_with_compiled_lib[_line_up_python_compiled_libs_top_level_same_name_output]' \
  --deselect='tests/test_subpackages.py::test_merge_build_host_applies_in_outputs' \
  --deselect='tests/test_subpackages.py::test_activation_in_output_scripts' \
  --deselect='tests/test_subpackages.py::test_loops_do_not_remove_earlier_packages' \
  --deselect='tests/test_variants.py::test_build_run_exports_act_on_host' \
  --deselect='tests/test_variants.py::test_different_git_vars' \
  --deselect='tests/test_variants.py::test_git_variables_with_variants' \
  --deselect='tests/test_variants.py::test_no_satisfiable_variants_raises_error' \
  --deselect='tests/test_variants.py::test_pinning_in_build_requirements' \
  --deselect='tests/test_variants.py::test_python_variants[yaml]' \
  --deselect='tests/test_variants.py::test_python_variants[dict]' \
  --deselect='tests/test_variants.py::test_ensure_valid_spec_on_run_and_test' \
  --deselect='tests/test_variants.py::test_serial_builds_have_independent_configs' \
  --deselect='tests/test_variants.py::test_numpy_used_variable_looping' \
  --deselect='tests/test_variants.py::test_inner_python_loop_with_output' \
  --deselect='tests/test_variants.py::test_top_level_finalized' \
  --deselect='tests/test_variants.py::test_variant_as_dependency_name' \
  --deselect='tests/test_variants.py::test_variant_subkeys_retained' \
  --deselect='tests/test_variants.py::test_variants_in_versions_with_setup_py_data' \
  --deselect='tests/cli/test_main_build.py::test_build_empty_sections' \
  --deselect='tests/cli/test_main_build.py::test_build_skip_existing' \
  --deselect='tests/cli/test_main_build.py::test_build_skip_existing_croot' \
  --deselect='tests/cli/test_main_build.py::test_relative_path_croot' \
  --deselect='tests/cli/test_main_build.py::test_relative_path_test_artifact' \
  --deselect='tests/cli/test_main_build.py::test_relative_path_test_recipe' \
  --deselect='tests/cli/test_main_build.py::test_build_add_channel' \
  --deselect='tests/cli/test_main_build.py::test_build_without_channel_fails' \
  --deselect='tests/cli/test_main_build.py::test_build_output_build_path' \
  --deselect='tests/cli/test_main_build.py::test_build_output_build_path_multiple_recipes' \
  --deselect='tests/cli/test_main_build.py::test_slash_in_recipe_arg_keeps_build_id' \
  --deselect='tests/cli/test_main_build.py::test_build_long_test_prefix_default_enabled' \
  --deselect='tests/cli/test_main_build.py::test_build_no_build_id' \
  --deselect='tests/cli/test_main_build.py::test_build_multiple_recipes' \
  --deselect='tests/cli/test_main_build.py::test_build_output_folder' \
  --deselect='tests/cli/test_main_build.py::test_build_source' \
  --deselect='tests/cli/test_main_build.py::test_purge' \
  --deselect='tests/cli/test_main_build.py::test_purge_all' \
  --deselect='tests/cli/test_main_build.py::test_no_filename_hash' \
  --deselect='tests/cli/test_main_build.py::test_no_force_upload' \
  --deselect='tests/cli/test_main_build.py::test_conda_py_no_period' \
  --deselect='tests/cli/test_main_build.py::test_package_test' \
  --deselect='tests/cli/test_main_build.py::test_activate_scripts_not_included' \
  --deselect='tests/cli/test_main_build.py::test_test_extra_dep' \
  --deselect='tests/cli/test_main_convert.py::test_convert' \
  --deselect='tests/cli/test_main_develop.py::test_develop' \
  --deselect='tests/cli/test_main_inspect.py::test_inspect_installable' \
  --deselect='tests/cli/test_main_inspect.py::test_inspect_linkages' \
  --deselect='tests/cli/test_main_inspect.py::test_inspect_objects' \
  --deselect='tests/cli/test_main_inspect.py::test_inspect_prefix_length' \
  --deselect='tests/cli/test_main_inspect.py::test_inspect_hash_input' \
  --deselect='tests/cli/test_main_metapackage.py::test_metapackage' \
  --deselect='tests/cli/test_main_metapackage.py::test_metapackage_build_number' \
  --deselect='tests/cli/test_main_metapackage.py::test_metapackage_build_string' \
  --deselect='tests/cli/test_main_metapackage.py::test_metapackage_metadata' \
  --deselect='tests/cli/test_main_render.py::test_render_add_channel' \
  --deselect='tests/cli/test_main_render.py::test_render_without_channel_fails' \
  --deselect='tests/cli/test_main_render.py::test_render_output_build_path' \
  --deselect='tests/cli/test_main_render.py::test_render_output_build_path_and_file' \
  --deselect='tests/cli/test_main_render.py::test_render_output_build_path_set_python' \
  --deselect='tests/cli/test_main_render.py::test_render_with_python_arg_reduces_subspace' \
  --deselect='tests/cli/test_main_render.py::test_render_with_python_arg_CLI_reduces_subspace' \
%endif


%files
%{_bindir}/conda-build
%{_bindir}/conda-convert
%{_bindir}/conda-debug
%{_bindir}/conda-develop
%{_bindir}/conda-inspect
%{_bindir}/conda-metapackage
%{_bindir}/conda-render
%{_bindir}/conda-skeleton
%{_mandir}/man1/conda-build.1*

%files -n python%{python3_pkgversion}-conda-build -f %pyproject_files
%doc CHANGELOG.md README.md


%changelog
%autochangelog
