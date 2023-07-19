%bcond_without tests

%global srcname platformdirs
%global common_description %{expand:
A small Python module for determining appropriate platform-specific dirs, e.g.
a "user data dir".}

Name:           python-%{srcname}
Version:        3.9.1
Release:        1%{?dist}
Summary:        Python module for determining appropriate platform-specific dirs
License:        MIT
URL:            https://github.com/platformdirs/platformdirs
Source0:        %pypi_source
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
# RHBZ#1712140, RHBZ#2076994
BuildRequires:  pyproject-rpm-macros >= 1.2.0


%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i '/^[[:blank:]]*"pytest-cov\b/d' pyproject.toml
sed -r -i '/^[[:blank:]]*"covdefaults\b/d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -w %{?with_tests:-x test}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%if %{with tests}
# Upstream uses tox, but we don’t use it, to avoid a build dependency loop
# platformdirs <- virtualenv <- tox
%pytest
%else
%pyproject_check_import
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
* Mon Jul 17 2023 Lumír Balhar <lbalhar@redhat.com> - 3.9.1-1
- Update to 3.9.1 (rhbz#2156775)

* Fri Jun 30 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 3.5.1-1
- Update to 3.5.1
- Fixes: rhbz#2156775

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.6.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 08 2022 Lumír Balhar <lbalhar@redhat.com> - 2.6.0-1
- Update to 2.6.0 (rhbz#2151438)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.5.2-2
- Rebuilt for Python 3.11

* Thu Apr 21 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 2.5.2-1
- Update to 2.5.2; accommodate upstream’s switch to hatchling build backend
- Add a build conditional for the tests

* Tue Mar 22 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 2.5.1-1
- Update to 2.5.1 (close RHBZ#2007878)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Dec 04 2021 Carl George <carl@george.computer> - 2.3.0-3
- Use "test" extra to generate buildrequires
- Run tests with %%pytest

* Tue Oct 26 2021 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-2
- Don't use tox during the build to avoid a build dependency loop

* Mon Aug 30 2021 Carl George <carl@george.computer> - 2.3.0-1
- Latest upstream
- Resolves: rhbz#1999337

* Sun Aug 01 2021 Carl George <carl@george.computer> - 2.2.0-1
- Latest upstream
- Resolves: rhbz#1985567

* Fri Jul 23 2021 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Let %%pyproject_buildrequires know we need appdirs

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 12 2021 Carl George <carl@george.computer> - 2.0.0-1
- Initial package rhbz#1981607
