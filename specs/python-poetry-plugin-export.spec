# To break circular dependency on poetry, when bootstrapping
# we don't BuildRequire runtime deps and we don't run tests.
%bcond bootstrap 0

Name:           python-poetry-plugin-export
Version:        1.9.0
Release:        %autorelease
Summary:        Poetry plugin to export the dependencies to various formats

# Compatibility with poetry 2.2.1
Patch:          https://github.com/python-poetry/poetry-plugin-export/commit/39ff1fb.patch

# SPDX
License:        MIT
URL:            https://python-poetry.org/
Source:         %{pypi_source poetry_plugin_export}

# Adapt tests to cosmetic changes caused by poetry-core.
# The changes in poetry.lock file were removed from the patch as they are not necessary and they were not applying cleanly.
# Also the changes in pyproject.toml are not relevant.
# Adapted from https://github.com/python-poetry/poetry-plugin-export/commit/16637f1.patch
Patch:          Adapt-tests-to-changes-in-poetry-core.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# Test dependencies are taken from [tool.poetry.dev-dependencies]
# in pyproject.toml file. poetry-plugin-export lists test dependencies
# in dependency groups instead of extras, since they are not extras
# pyproject-rpm-macros can't recognize them and we list them manually.
# They also mix in pre-commit and mypy and we don't need them.
%if %{without bootstrap}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-xdist
%endif

%global _description %{expand:
This package is a plugin that allows the export of locked packages to various
formats. This plugin provides the same features as the existing export command
of Poetry which it will eventually replace.
}

%description %_description

%package -n python3-poetry-plugin-export
Summary:        %{summary}

%description -n python3-poetry-plugin-export %_description


%prep
%autosetup -p1 -n poetry_plugin_export-%{version}


%generate_buildrequires
%pyproject_buildrequires %{?with_bootstrap: -R}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files poetry_plugin_export

%if %{without bootstrap}
%check
%pytest
%endif


%files -n python3-poetry-plugin-export -f %{pyproject_files}
%doc README.*
%license LICENSE


%changelog
%autochangelog
