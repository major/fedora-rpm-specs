# To break circular dependency on poetry, when bootstrapping
# we don't BuildRequire runtime deps and we don't run tests.
%bcond bootstrap 0

Name:           python-poetry-plugin-export
Version:        1.7.1
Release:        2%{?dist}
Summary:        Poetry plugin to export the dependencies to various formats

# SPDX
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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 08 2024 Charalampos Stratakis <cstratak@redhat.com> - 1.7.1-1
- Update to 1.7.1
- Fixes: rhbz#2269651

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.6.0-5
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.6.0-4
- Bootstrap for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 27 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.6.0-1
- Update to 1.6.0
- Fixes: rhbz#2247122

* Fri Sep 01 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.5.0-1
- Update to 1.5.0
- Fixes: rhbz#2232935

* Fri Aug 04 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.4.0-2
- Update to 1.4.0

* Fri Aug 04 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.4.0-1
- Update to 1.4.0 - with bootstrap

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 22 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.3.1-2
- Update to 1.3.1 - without bootstrap

* Thu May 11 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.3.1-1
- Update to 1.3.1

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

