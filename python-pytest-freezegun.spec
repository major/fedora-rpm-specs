Name:           python-pytest-freezegun
Version:        0.4.2
Release:        7%{?dist}
Summary:        Wrap pytest tests with fixtures in freeze_time

License:        MIT
URL:            https://github.com/ktosiek/pytest-freezegun
Source0:        %{url}/archive/%{version}/pytest-freezegun-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

%global _description %{expand:
This is a pytest plugin that let you wrap tests with fixtures in freeze_time.

Features:

- Freeze time in both the test and fixtures
- Access the freezer when you need it}

%description %_description


%package -n python3-pytest-freezegun
Summary:        %{summary}

%description -n python3-pytest-freezegun %_description


%prep
%autosetup -p1 -n pytest-freezegun-%{version}


%generate_buildrequires
# tox config contains coverage, so we'll execute pytest directly instead
# since this a pytest plugin, pytetst is a runtime dependency anyway
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytest_freezegun


%check
%pytest -v


%files -n python3-pytest-freezegun -f %{pyproject_files}
%doc README.rst CHANGELOG.md
%license LICENSE


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.2-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.2-2
- Rebuilt for Python 3.10

* Tue May 18 2021 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-1
- Initial RPM package
- Fixes rhbz#1961793
