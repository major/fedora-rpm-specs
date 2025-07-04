# This is built as an arched package, as its includes a cache as a Python
# pickle file which is apparently not an architecture-independent format (fails
# on s390x). Still, this needs does not produce any debug data.
%global debug_package %{nil}

Name:           scancode-toolkit
Version:        32.3.3
Release:        %autorelease
Summary:        Scan code and detect licenses, copyrights, and more

# Apache-2.0: main program
# CC-BY-4.0: ScanCode datasets for license detection
License:        Apache-2.0 AND CC-BY-4.0
URL:            https://scancode-toolkit.readthedocs.io/
VCS:            https://github.com/nexB/scancode-toolkit
Source:         %vcs/archive/v%{version}/%{name}-%{version}.tar.gz

Patch:          0001-tests-fix-pytest-traceback.patch
Patch:          0002-Replace-pkginfo2-with-pkginfo.patch

# scancode has dependencies that are not compatible with ix86
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-reredirects)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  tomcli

%global common_description %{expand:
ScanCode is an open-source tool to scan code and detect licenses, copyrights,
and more. It provides detailed information about discovered licenses,
copyrights, and other important details in various formats.}

%description %{common_description}

%package doc
Summary:        Documentation for python-%{name}
BuildArch:      noarch

%description doc
%{common_description}

This package is providing the documentation for %{name}.

%prep
%autosetup -p1
sed -i 's|\(fallback_version = "\)[^"]*|\1%{version}|' pyproject.toml
sed -i \
    -e '/doc8/d' \
    -e '/sphinx-rtd-dark-mode/d' \
    -e 's/Sphinx ==/Sphinx>=/' \
    -e 's|Beautifulsoup4\[chardet\]|Beautifulsoup4|' \
    -e '/sphinx-autobuild/d' \
setup.cfg
sed -i '/"sphinx_rtd_dark_mode"/d' docs/source/conf.py

%generate_buildrequires
%pyproject_buildrequires -x docs

%build
# NOTE: Upstream's wheels include the license cache as a Python pickle, so
# let's build that here. Without this file, scancode tries to write the cache
# to site-packages itself which it doesn't have permissions for.
# TODO: Upstream's approach to caching is problematic.
# It treats pickles as a portable data format and tries to write a new cache to
# site-packages if the cache is invalid or does not exist.
# See https://github.com/aboutcode-org/scancode-toolkit/issues/3497.
# This should be fixed to prefer a user-writable cache directory.
PYTHONPATH="$(pwd)/src" %{python3} -m licensedcode.reindex
test -f src/licensedcode/data/cache/license_index/index_cache
%pyproject_wheel

# generate html docs
sphinx-build-3 -b html docs/source html
# remove the sphinx-build-3 leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files scancode_config

%check
# https://github.com/nexB/scancode-toolkit/issues/3496
mkdir -p venv/bin
ln -s %{buildroot}%{_bindir}/scancode venv/bin/regen-package-docs
ln -s %{buildroot}%{_bindir}/scancode venv/bin/scancode
ln -s %{buildroot}%{_bindir}/scancode venv/bin/scancode-license-data
ln -s %{buildroot}%{_bindir}/scancode venv/bin/scancode-reindex-licenses
# The tests expect that the directory of each file is added to sys.path, but
# this doesn't happen in importlib mode, so do it manually.
tomcli set pyproject.toml arrays str \
    tool.pytest.ini_options.pythonpath 'tests/packagedcode' 'tests/cluecode'
# The tests expect to be run from a source checkout.
export PYTHONPATH="$(pwd)/src"

# we use system libmagic 5.45 while upstream uses 5.39
# real failures start at test_is_licensing_works \
# to be reported upstream but probably some different library version somewhere too
# test_about_files: inside the venv we don't use
# Use importlib mode because some test files have the same filenames.
%pytest -k "not test_json_pretty_print and not \
            test_jsonlines and not \
            test_json_compact and not \
            test_json_with_extracted_license_statements and not \
            test_yaml and not \
            test_end_to_end_scan_with_license_policy and not \
            test_scan_can_handle_weird_file_names and not \
            test_scan_can_run_from_other_directory and not \
            test_scan_produces_valid_yaml_with_extracted_license_statements and not \
            test_classify_with_package_data and not \
            test_consolidate_package and not \
            test_consolidate_package_files_should_not_be_considered_in_license_holder_consolidated_component and not \
            test_consolidate_component_package_from_json_can_run_twice and not \
            test_consolidate_component_package_from_live_scan and not \
            test_consolidate_package_always_include_own_manifest_file and not \
            test_consolidate_component_package_build_from_live_scan and not \
            test_end2end_todo_works_on_codebase_without_ambiguous_detections and not \
            test_is_licensing_works and not \
            test_parse_from_rb and not \
            test_parse_from_rb_dependency_requirement and not \
            test_scan_cli_works and not \
            test_scan_cli_works_package_only and not \
            test_package_command_scan_chef and not \
            test_package_scan_pypi_end_to_end and not \
            test_develop_with_parse and not \
            test_develop_with_parse_metadata and not \
            test_parse_with_eggfile and not \
            test_parse_with_unpacked_wheel_meta and not \
            test_parse_metadata_prefer_pkg_info_from_egg_info_from_command_line and not \
            test_parse_dependency_file_with_invalid_does_not_fail and not \
            test_recognize_rpmdb_sqlite and not \
            test_collect_installed_rpmdb_xmlish_from_rootfs and not \
            test_scan_system_package_end_to_end_installed_win_reg and not \
 test_consolidate_report_minority_origin_directory and not \
            test_about_files and not \
            test_scan_works_on_rust_binary_with_inspector and not \
            test_package_list_command and not \
            test_get_file_info_include_size and not \
            test_scan_cli_help" \
    --import-mode importlib -vv


%files -f %{pyproject_files}
%doc AUTHORS.rst CHANGELOG.rst CODE_OF_CONDUCT.rst
%doc CONTRIBUTING.rst README.rst ROADMAP.rst
%license NOTICE apache-2.0.LICENSE cc-by-4.0.LICENSE
%{_bindir}/regen-package-docs
%{_bindir}/scancode
%{_bindir}/scancode-license-data
%{_bindir}/scancode-reindex-licenses
%{python3_sitelib}/cluecode
%{python3_sitelib}/formattedcode
%{python3_sitelib}/licensedcode
%{python3_sitelib}/packagedcode
%{python3_sitelib}/scancode
%{python3_sitelib}/summarycode
%{python3_sitelib}/textcode

%files doc
%doc html
%license NOTICE apache-2.0.LICENSE cc-by-4.0.LICENSE

%changelog
%autochangelog

