%global srcname detect-secrets

%bcond check 1
%bcond gibberish 0

Name:           python-%{srcname}
Version:        1.5.0
Release:        %autorelease
Summary:        Detect secrets within a code base
License:        Apache-2.0
URL:            https://github.com/Yelp/detect-secrets
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

# https://bugzilla.redhat.com/show_bug.cgi?id=2296177
# Dependency python-pyahocorasick does not support big-endian platforms; we can
# only support the same architectures that it does (plus noarch). See:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_noarch_with_unported_dependencies
ExclusiveArch:  x86_64 %{arm64} ppc64le riscv64 noarch

BuildRequires:  help2man
BuildRequires:  python3-devel
BuildRequires:  sed

%global _description %{expand:
detect-secrets is an aptly named module for (surprise, surprise) detecting
secrets within a code base.

However, unlike other similar packages that solely focus on finding secrets,
this package is designed with the enterprise client in mind: providing a
backwards compatible, systematic means of:

* Preventing new secrets from entering the code base,
* Detecting if such preventions are explicitly bypassed, and
* Providing a checklist of secrets to roll, and migrate off to a more secure
  storage.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%pyproject_extras_subpkg -n python3-%{srcname} word_list

%if %{with gibberish}
%pyproject_extras_subpkg -n python3-%{srcname} gibberish
%endif

%prep
%autosetup -p1 -n %{srcname}-%{version}
# use relaxed build requirements instead of hard-coded ones
# this lets pyproject_buildrequires -t resolve deps correctly
sed -i -e 's/requirements-dev.txt/requirements-dev-minimal.txt/g' tox.ini
# drop linter requirements, see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# monotonic is only used in a benchmark script, not in the tests
sed -i \
    -e '/flake8/d' \
    -e '/tox-pip-extensions/d' \
    -e '/monotonic/d' \
    requirements-dev-minimal.txt
%if %{without gibberish}
sed -i -e '/gibberish-detector/d' requirements-dev-minimal.txt
%endif

%generate_buildrequires
%if %{with check}
%pyproject_buildrequires -t -x word_list
%else
%pyproject_buildrequires -x word_list
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l detect_secrets

install -dm755 %{buildroot}%{_mandir}/man1
export PYTHONPATH="$PYTHONPATH:%{buildroot}%{python3_sitelib}"
help2man --no-discard-stderr --no-info %{buildroot}%{_bindir}/%{srcname} -o %{buildroot}%{_mandir}/man1/%{srcname}.1

%check
%pyproject_check_import
%if %{with check}
# some tests require git and upstream git repo, others
# require an unpackaged dependency (gibberish-detector)
# see also https://github.com/Yelp/detect-secrets/issues/875
%pytest -k "not test_basic_usage \
        and not test_no_files_in_git_repo \
        and not test_scan_all_files \
        and not test_load_and_output \
        and not test_load_from_baseline \
        and not test_outputs_baseline_if_none_supplied \
        and not test_saves_to_baseline \
        and not test_works_from_different_directory \
        and not test_basic \
        and not test_verify_no_secret \
        and not test_verify_valid_secret \
        and not test_verify_invalid_secret \
        and not test_verify_keep_trying_until_found_something \
        and not test_potential_secret_constructed_correctly \
        and not test_no_verification_call_if_verification_filter_is_disabled \
        and not test_handle_verify_exception_gracefully \
        and not test_quit_if_baseline_is_changed_but_not_staged \
        and not test_baseline_filters_out_known_secrets \
        and not test_success \
        and not test_maintains_labelled_data \
        and not test_maintains_slim_mode \
        and not test_modifies_baseline \
        and not test_does_not_modify_slim_baseline \
        and not test_make_decisions \
        and not test_start_halfway \
        and not test_should_scan_specific_non_tracked_file \
        and not test_should_scan_tracked_files_in_directory \
        and not test_should_scan_all_files_in_directory_if_flag_is_provided \
        and not test_handles_each_path_separately \
        and not test_handles_multiple_directories \
        and not test_success \
        and not test_ignores_hex_strings \
        and not test_does_not_affect_private_keys \
        "
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md CONTRIBUTING.md CONTRIBUTORS.md README.md
%{_bindir}/%{srcname}
%{_bindir}/%{srcname}-hook
%{_mandir}/man1/%{srcname}.1*

%changelog
%autochangelog
