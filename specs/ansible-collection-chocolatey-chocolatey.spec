Name:           ansible-collection-chocolatey-chocolatey
Version:        1.5.3
Release:        2%{?dist}
Summary:        Ansible collection for Chocolatey

License:        GPL-3.0-or-later
URL:            %{ansible_collection_url chocolatey chocolatey}
Source:         https://github.com/chocolatey/chocolatey-ansible/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ansible-packaging

BuildArch:      noarch

%description
The collection includes the modules required to configure Chocolatey, as well
as manage packages on Windows using Chocolatey.

%prep
%autosetup -n chocolatey-ansible-%{version}
find -type f ! -executable -name '*.py' -print -exec sed -i -e '1{\@^#!.*@d}' '{}' +
sed -i -e 's/{{ REPLACE_VERSION }}/%{version}/' chocolatey/galaxy.yml
cat >> chocolatey/galaxy.yml << EOF
build_ignore:
  # Remove unnecessary development files from the built package.
  - tests
  - azure-pipelines.yml
  - .gitignore
  # Licenses and docs are installed with %%doc and %%license
  - LICENSE
  - README.md
EOF

%build
cd chocolatey
%ansible_collection_build

%install
cd chocolatey
%ansible_collection_install

# No unit tests

%files -f %{ansible_collection_filelist}
%license LICENSE
%doc README.md

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 08 2024 Orion Poplawski <orion@nwra.com> - 1.5.3-1
- Update to 1.5.3

* Sun Sep 29 2024 Orion Poplawski <orion@nwra.com> - 1.5.2-1
- Update to 1.5.2

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 15 2023 Orion Poplawski <orion@nwra.com> - 1.5.1-1
- Update to 1.5.1

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 16 2022 Orion Poplawski <orion@nwra.com> - 1.4.0-1
- Update to 1.4.0
- Use current ansible collection packaging style
- Use SPDX License tag

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Orion Poplawski <orion@nwra.com> - 1.3.0-1
- Update to 1.3.0

* Fri Feb 11 2022 Orion Poplawski <orion@nwra.com> - 1.2.0-1
- Update to 1.2.0

* Sat Jan 29 2022 Maxwell G <gotmax@e.email> - 1.1.0-3
- Switch to ansible-packaging.

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 02 2021 Orion Poplawski <orion@nwra.com> - 1.1.0-1
- Update to 1.1.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 12 2021 Orion Poplawski <orion@nwra.com> - 1.0.2-1
- Initial package
