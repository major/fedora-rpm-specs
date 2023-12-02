Name:           python-textual
Version:        0.43.2
Release:        1%{?dist}
Summary:        TUI (Text User Interface) framework for Python
License:        MIT
URL:            https://github.com/Textualize/textual
Source0:        %{url}/archive/v%{version}/textual-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# Test dependencies:
BuildRequires:  pytest
BuildRequires:  python3-jinja2
BuildRequires:  python3-syrupy
BuildRequires:  python3-time-machine
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-aiohttp
BuildRequires:  python3-pytest-aiohttp

%global _description %{expand:
Textual is a TUI (Text User Interface) framework for Python inspired
by modern web development. Currently a Work in Progress.}

%description
%{_description}

%package -n python3-textual
Summary:        %{summary}

%description -n python3-textual
%{_description}

%package -n python3-textual-doc
Summary:        Docs and examples for python3-textual

%description -n python3-textual-doc
%{_description}

%prep
%autosetup -n textual-%{version}

%generate_buildrequires
%pyproject_buildrequires -r -x dev


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files textual


%check
# skip these tests until https://github.com/Textualize/pytest-textual-snapshot
# is packaged
rm -rf tests/snapshot_tests
%pytest -k "not test_textual_env_var and not test_register_language and not test_register_language_existing_language"


%files -n python3-textual -f %{pyproject_files}
%license LICENSE

%files -n python3-textual-doc
%license LICENSE
%doc README.md docs/ examples/


%changelog
* Thu Nov 30 2023 Jonathan Wright <jonathan@almalinux.org> - 0.43.2-1
- Update to 0.43.2 rhbz#2239239

* Fri Sep 15 2023 Jonathan Wright <jonathan@almalinux.org> - 0.37.0-1
- Update to 0.37.0 rhbz#2192888

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 28 2023 Jonathan Wright <jonathan@almalinux.org> - 0.22.3-1
- Update to 0.22.3 rhbz#2170877

* Sat Mar 25 2023 Jonathan Wright <jonathan@almalinux.org> - 0.16.0-1
- Update to 0.16.0 rhbz#2170877

* Wed Feb 15 2023 Jonathan Wright <jonathan@almalinux.org> - 0.10.0-1
- Update to 0.10.0 rhbz#2162484

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jul 31 2022 Jonathan Wright <jonathan@almalinux.org> - 0.1.18-1
- Initial package build
- rhbz#2121258
