# Generating shell completions requires shtab 1.11.0 or later,
# https://bugzilla.redhat.com/show_bug.cgi?id=2415592,
# https://src.fedoraproject.org/rpms/python-shtab/pull-request/2
%bcond completion 0

Name:           python-nodeenv
Version:        1.12.0
Release:        %autorelease
Summary:        Node.js virtual environment builder

License:        BSD-3-Clause
URL:            https://github.com/ekalinin/nodeenv
# The PyPI sdist does not contain tests, so we use the GitHub archive
Source:         %{url}/archive/%{version}/nodeenv-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  help2man

# We don’t use tox, because we would have to patch out linting and coverage
# analysis from tox.ini, and the rest of the dependencies in
# requirements-dev.txt are all for linting and coverage—except pytest, which we
# handle manually, because this is easier than filtering the requirements file.
#
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
BuildRequires:  python3dist(pytest)
# For integration tests:
BuildRequires:  /usr/bin/node

%global _description %{expand:
nodeenv (node.js virtual environment) is a tool to create isolated node.js
environments.

It creates an environment that has its own installation directories, that
doesn’t share libraries with other node.js virtual environments.

Also the new environment can be integrated with the environment which was built
by virtualenv (python).}

%description %{_description}


%package -n python3-nodeenv
Summary:        %{summary}

%description -n python3-nodeenv %{_description}


%pyproject_extras_subpkg --name python3-nodeenv certifi
%if %{with completion}
%pyproject_extras_subpkg --name python3-nodeenv completion
%endif


%prep
%autosetup -n nodeenv-%{version} -p1

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed --regexp-extended --in-place \
    "s@'coverage', 'run', '-p',@'%{python3}',@" tests/nodeenv_test.py

# Remove unwanted shebangs from files that will not have the executable bit set
sed --regexp-extended --in-place '1{/^#!/d}' nodeenv.py

# Upstream wants shtab >=1.11, but we can get by with older releases
# https://bugzilla.redhat.com/show_bug.cgi?id=2415592
sed --regexp-extended --in-place "s/(shtab)>=[^'\"]+/\\1/" setup.py


%generate_buildrequires
%pyproject_buildrequires --extras certifi%{?with_completion:,completion}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files --assert-license nodeenv

# Set up the environment to generate the man page and completions using the
# installed entry point. See %%{py3_test_envvars} on EPEL10+ and Fedora.
export PYTHONPATH='%{buildroot}%{python3_sitelib}'
export PYTHONDONTWRITEBYTECODE=1

# Generate the man page here, rather than in %%build, so that the executable
# script entry point is readily available.
install --directory '%{buildroot}%{_mandir}/man1'
help2man --no-info --output='%{buildroot}%{_mandir}/man1/nodeenv.1' \
    '%{buildroot}%{_bindir}/nodeenv'

%if %{with completions}
# From the message for
# https://github.com/ekalinin/nodeenv/commit/0fd263f58fd232b6b6a8e8def2401db885eb3d7d,
#
#   --print-completion SHELL prints a completion script for bash, zsh, fish or
#   PowerShell, made by shtab from the same parser that reads the command line.
#   shtab is an optional dependency, installed with the completion extra, and
#   only this flag imports it: without shtab the flag stays in --help and exits
#   with the pip command to run.
#
# Pre-generate and install the completion files.
while read -r shell target
do
  install --directory "%{buildroot}$(dirname "${target}")"
  '%{buildroot}%{_bindir}/nodeenv' --print-completion "${shell}" \
      > "%{buildroot}${target}"
done <<'EOF'
bash %{bash_completions_dir}/nodeenv
zsh %{zsh_completions_dir}/_nodeenv
fish %{fish_completions_dir}/nodeenv.fish
EOF
%endif


%check
# Requires network access:
k="${k-}${k+ and }not test_smoke"

%pytest -k "${k-}" --verbose


%files -n python3-nodeenv -f %{pyproject_files}
%doc README.rst
%lang(ru) %doc README.ru.rst
%doc CHANGES

%{_bindir}/nodeenv
%{_mandir}/man1/nodeenv.1*
%if %{with completions}
%{bash_completions_dir}/nodeenv
%{zsh_completions_dir}/_nodeenv
%{fish_completions_dir}/nodeenv.fish
%endif


%changelog
%autochangelog
