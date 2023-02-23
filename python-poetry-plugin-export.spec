# To break circular dependency on poetry, when bootstrapping
# we don't BuildRequire runtime deps and we don't run tests.
%bcond bootstrap 0

Name:           python-poetry-plugin-export
Version:        1.3.0
Release:        2%{?dist}
Summary:        Poetry plugin to export the dependencies to various formats

License:        MIT
URL:            https://python-poetry.org/
Source:         %{pypi_source poetry_plugin_export}

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
* Mon Feb 20 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.3.0-2
- Update to 1.3.0 - without bootstrap

* Mon Feb 20 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 22 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.1.2-1
- Update to 1.1.2
- Fixes: rhbz#2140314

* Mon Oct 10 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.1.1-2
- Disable bootstrap

* Tue Oct 4 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.1.1-1
Initial package

