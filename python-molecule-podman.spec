Name: python-molecule-podman
Version: 2.0.3
Release: 3%{?dist}
Summary: Molecule Podman plugin
License: MIT

URL: https://github.com/ansible-community/molecule-podman
Source0: %{pypi_source molecule-podman}

BuildArch: noarch

BuildRequires: python3-devel


%description
Molecule Podman Plugin is designed to allow use podman containers for
provisioning test resources.


%package -n python3-molecule-podman
Summary: %summary


%description -n python3-molecule-podman
Molecule Podman Plugin is designed to allow use podman containers for
provisioning test resources.


%prep
%autosetup -n molecule-podman-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files molecule_podman


%check
%pyproject_check_import -e 'molecule_podman.test.*'


%files -n python3-molecule-podman -f %{pyproject_files}
%license LICENSE
%doc *.rst

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Maxwell G <gotmax@e.email> - 2.0.3-1
- Update to 2.0.3.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 1.0.1-1
- Update to version 1.0.1 (#2018838)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.3.0-1
- update to version 0.3.0

* Thu Oct 15 2020 Chedi Toueiti <chedi.toueiti@gmail.com> - 0.1-1
- initial package
