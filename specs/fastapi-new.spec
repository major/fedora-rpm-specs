# Run tests that require network access for added confidence? We can only do
# this in a local mock build with --enable-network or in COPR.
%bcond network_tests 0

Name:           fastapi-new
Version:        0.0.4
Release:        %autorelease
Summary:        Create a new FastAPI project in one command

License:        MIT
URL:            https://github.com/fastapi/fastapi-new
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Written for Fedora in groff_man(7) format based on --help output
Source10:       fastapi-new.1

# Downstream-only: patch out coverage from script test
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          0001-Downstream-only-patch-out-coverage-from-script-test.patch
# Downstream-only: Drop spurious runtime dependency on prek
#
# This was added in 36321c1a and removed again in (unreleased) ed53c59f.
# This patch should therefore only be needed until the next upstream release.
Patch:          0001-Drop-spurious-runtime-dependency-on-prek.patch

BuildSystem:            pyproject
BuildOption(install):   -L fastapi_new

BuildArch:      noarch

%py_provides python3-fastapi-new

# Since requirements-tests.txt contains overly-strict version bounds and
# unwanted linting/coverage/typechecking/formatting dependencies
# (https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters),
# and the dev extra also includes unwanted dependencies, we just list the few
# test dependencies we *do* want manually.
BuildRequires:  %{py3_dist pytest} >= 8

# As described in README.md, uv is required; however, there is no dependency on
# python3-uv, only an expectation that the uv executable is in PATH.
BuildRequires:  uv
Requires:       uv

%global common_description %{expand:
Create a new FastAPI project in one command. ✨}

%description %{common_description}


%install -a
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE10}'

install -d \
    '%{buildroot}%{bash_completions_dir}' \
    '%{buildroot}%{zsh_completions_dir}' \
    '%{buildroot}%{fish_completions_dir}'
export PYTHONPATH='%{buildroot}%{python3_sitelib}'
export _TYPER_COMPLETE_TEST_DISABLE_SHELL_DETECTION=1
'%{buildroot}%{_bindir}/fastapi-new' --show-completion bash \
    > '%{buildroot}%{bash_completions_dir}/fastapi-new'
'%{buildroot}%{_bindir}/fastapi-new' --show-completion zsh \
    > '%{buildroot}%{zsh_completions_dir}/_fastapi-new'
'%{buildroot}%{_bindir}/fastapi-new' --show-completion fish \
    > '%{buildroot}%{fish_completions_dir}/fastapi-new.fish'


%check -a
%if %{without network_tests}
k="${k-}${k+ and }not test_creates_project_successfully"
k="${k-}${k+ and }not test_creates_project_with_python_version"
k="${k-}${k+ and }not test_validates_template_file_contents"
k="${k-}${k+ and }not test_initializes_in_current_directory"
k="${k-}${k+ and }not test_passes_single_digit_python_version_to_uv"
k="${k-}${k+ and }not test_creates_project_without_python_flag"
k="${k-}${k+ and }not test_file_write_failure"
%endif

%pytest -k "${k-}" -v


%files -f %{pyproject_files}
%license LICENSE
%doc README.md
%doc release-notes.md

# This package provides its own fastapi-new executable entry point; it also
# adds a “fastapi cloud” command to the fastapi CLI (entry point in
# python3-fastapi; separate package fastapi-cli also relevant). The man page
# integrates with those in python3-fastapi.
%{_bindir}/fastapi-new
%{_mandir}/man1/fastapi-new.1*
%{bash_completions_dir}/fastapi-new
%{zsh_completions_dir}/_fastapi-new
%{fish_completions_dir}/fastapi-new.fish


%changelog
%autochangelog
