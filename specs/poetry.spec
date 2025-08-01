# To break circular dependency on poetry-plugin-export, when bootstrapping
# we don't BuildRequire runtime deps and we don't run tests.
%bcond bootstrap 0

%global common_description %{expand:
Poetry helps you declare, manage and install dependencies of Python
projects, ensuring you have the right stack everywhere.}

Name:           poetry
Summary:        Python dependency management and packaging made easy
Version:        2.1.3
Release:        %autorelease

# SPDX
License:        MIT

URL:            https://python-poetry.org/
Source0:        https://github.com/python-poetry/poetry/archive/%{version}/poetry-%{version}.tar.gz

# We don't ship embedded wheels in Fedora and they are being patched out
# from virtualenv (https://src.fedoraproject.org/rpms/python-virtualenv/blob/370bb9cf4e/f/rpm-wheels.patch#_110).
# Since poetry touches get_embedded_wheel() our patch breaks it as it
# retuns None instead of wheels.
# This temporary patch returns correct wheels by calling
# get_system_wheels_paths() from virtualenv.
# TODO get rid of this patch by talking to virtualenv and poetry upstream about a better solution.
Patch:          Patch-get_embedded_wheel-to-return-system-wheels-fro.patch

Patch:          https://github.com/python-poetry/poetry/pull/10397.patch

# Fix test_python_get_preferred_default for rc Python releases
Patch:          https://github.com/python-poetry/poetry/pull/10478.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# The tests deps are only defined as part of poetry.dev-dependencies together with tox, pre-commit etc.
%if %{without bootstrap}
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  /usr/bin/python
BuildRequires:  %py3_dist pytest
BuildRequires:  %py3_dist pytest-mock
BuildRequires:  %py3_dist pytest-xdist
BuildRequires:  %py3_dist httpretty
BuildRequires:  %py3_dist cachy
BuildRequires:  %py3_dist deepdiff
%endif

Requires:       python3-poetry = %{version}-%{release}

%description %{common_description}


%package -n     python3-poetry
Summary:        %{summary}
# Our patch only works with recent version of the virtualenv patch
Conflicts:      python3-virtualenv < 20.19.0-2
%description -n python3-poetry %{common_description}


%prep
%autosetup -p1
# Relax version constraint to allow older virtualenv we have in Fedora
# Downstream report: https://bugzilla.redhat.com/show_bug.cgi?id=2188155#c8 
sed -i 's/virtualenv = "^20.23.0"/virtualenv = ">=20.21.1"/' pyproject.toml
sed -i 's/jsonschema = ">=4.10.0,<4.18.0"/jsonschema = ">=4.10.0,<4.20.0"/' pyproject.toml
# Convert the SemVer bound on the version of keyring to a lower bound, since
# its major version increases frequently, usually without significant
# incompatibilities.
sed -i -r 's/(keyring = ")\^/\1>=/' pyproject.toml

# Allow newer version of dulwich, which has landed in Fedora
sed -i 's/dulwich = "^0.21.2"/dulwich = ">=0.21.2"/' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires %{?with_bootstrap: -R}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files poetry

export PYTHONPATH=%{buildroot}%{python3_sitelib}
for i in bash,bash-completion/completions,poetry fish,fish/vendor_completions.d,poetry.fish zsh,zsh/site-functions,_poetry; do IFS=","
    set -- $i
    mkdir -p %{buildroot}%{_datadir}/$2
    # poetry leaves references to the buildroot in the completion files -> remove them
    %{buildroot}%{_bindir}/poetry completions $1 | sed 's|%{buildroot}||g' > %{buildroot}%{_datadir}/$2/$3
done

%if %{without bootstrap}
%check
# test_isolated_env_install_discards_requirements_not_needed_by_env fails with python3.14
# upstream issue: https://github.com/python-poetry/poetry/issues/10306
%pytest -m "not network" \
        -k "not test_isolated_env_install_discards_requirements_not_needed_by_env"
%endif


%files
%{_bindir}/poetry
# The directories with shell completions are co-owned
%{_datadir}/bash-completion/
%{_datadir}/fish/
%{_datadir}/zsh/


%files -n python3-poetry -f %{pyproject_files}
%license LICENSE
%doc README.md

# this is co-owned by poetry-core but we require poetry-core, so we get rid of it
# the file and its pycache might not be bit by bit identical
%exclude %dir %{python3_sitelib}/poetry
%pycached %exclude %{python3_sitelib}/poetry/__init__.py



%changelog
%autochangelog
