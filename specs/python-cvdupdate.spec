%global pypi_name cvdupdate

Name:           python-%{pypi_name}
Version:        1.1.3
Release:        4%{?dist}
Summary:        ClamAV Private Database Mirror Updater Tool

License:        Apache-2.0
URL:            https://github.com/Cisco-Talos/cvdupdate
# pypi_source is missing fixtures
Source0:        %{url}/archive/%{pypi_name}-%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
A tool to download and update clamav databases and database patch files
for the purposes of hosting your own database mirror.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{pypi_name}-%{version}
sed -i -e '1{\@^#!@d}' cvdupdate/__main__.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
rm -r %{buildroot}%{python3_sitelib}/tests
%pyproject_save_files cvdupdate


%check
%pytest -v


%files -n python3-cvdupdate -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/cvd
%{_bindir}/cvdupdate


%changelog
* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 1.1.3-4
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 1.1.3-3
- Rebuilt for Python 3.14.0rc2 bytecode

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jul 20 2025 Orion Poplawski <orion@nwra.com> - 1.1.3-1
- Update to 1.1.3

* Sat Jul 19 2025 Python Maint <python-maint@redhat.com> - 1.1.2-2
- Rebuilt for Python 3.14

* Thu Jan 23 2025 Orion Poplawski <orion@nwra.com> - 1.1.2-1
- Update to 1.1.2

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Python Maint <python-maint@redhat.com> - 1.1.1-2
- Rebuilt for Python 3.13

* Mon Feb 27 2023 Orion Poplawski <orion@nwra.com> - 1.1.1-1
- Initial Fedora package
