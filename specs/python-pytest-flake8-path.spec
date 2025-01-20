%global srcname pytest-flake8-path

Name:           python-%{srcname}
Version:        1.5.0
Release:        6%{?dist}
Summary:        A pytest fixture for testing flake8 plugins

License:        MIT
URL:            https://github.com/adamchainz/pytest-flake8-path
Source0:        https://github.com/adamchainz/pytest-flake8-path/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description %{expand:
pytest-flake8-path is the successor to pytest-flake8dir. pytest-flake8dir was
based upon pytest’s tmpdir fixture, which returned a legacy py.path.local
object. Since version 3.9.0, pytest has provided the tmp_path fixture, which
returns a standard library pathlib.Path object. pytest-flake8-path is a
rewrite of pytest-flake8dir to use tmp_path instead of tmpdir.}

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires requirements/requirements.in


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pytest_flake8_path


%check
%pytest


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc HISTORY.rst README.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.5.0-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

*Fri Jul 21 2023 Scott K Logan <logans@cottsay.net> - 1.5.0-1
- Update to 1.5.0 (rhbz#2215680)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Python Maint <python-maint@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 21 2022 Scott K Logan <logans@cottsay.net> - 1.3.0-2
- Install test dependencies using pyproject_buildrequires

* Fri Nov 18 2022 Scott K Logan <logans@cottsay.net> - 1.3.0-1
- Initial package (rhbz#2144097)
