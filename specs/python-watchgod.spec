%global srcname watchgod
%global common_description %{expand:
Simple, modern file watching and code reload in python.  watchgod is inspired
by watchdog, hence the name, but tries to fix some of the frustrations found
with watchdog.}


%bcond_without  tests


Name:           python-%{srcname}
Version:        0.8.2
Release:        11%{?dist}
Summary:        Simple, modern file watching and code reload
License:        MIT
URL:            https://github.com/samuelcolvin/watchgod
# PyPI tarball doesn't have tests
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-trio
%endif


%description -n python3-%{srcname} %{common_description}


%prep
# Upstream has renamed from watchgod to watchfiles.  This package will stay on
# the last version of the previous name, but the top level directory in the
# tarball from GitHub now shows the new name.
%autosetup -n watchfiles-%{version}

# If we don't set this, we end up with provides like:
# python3dist(watchgod) = 0~~dev0
sed -e 's/0.0.dev0/%{version}/' -i watchgod/version.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%if %{with tests}
%pytest -Wdefault -v
%else
%pyproject_check_import
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%{_bindir}/watchgod


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.8.2-9
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 0.8.2-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 28 2022 Carl George <carl@george.computer> - 0.8.2-2
- Set version in watchgod/version.py during build to avoid broken metadata

* Mon Jun 27 2022 Carl George <carl@george.computer> - 0.8.2-1
- Latest upstream, resolves rhbz#2063808
- Convert to pyproject macros
- Rebuild for Python 3.11, resolves rhbz#2099142

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.7-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7-2
- Rebuilt for Python 3.10

* Tue Mar 16 2021 Carl George <carl@george.computer> - 0.7-1
- Latest upstream
- Fixes: rhbz#1922631
- Fixes: rhbz#1928080

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Carl George <carl@george.computer> - 0.6-1
- Initial package
