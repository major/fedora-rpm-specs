Name:           podman-compose
Version:        1.5.0
Release:        2%{?dist}
Summary:        Run docker-compose.yml using podman
License:        GPL-2.0-only
URL:            https://github.com/containers/podman-compose
Source0:	https://github.com/containers/podman-compose/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pyyaml
Requires:       python%{python3_pkgversion}
Requires:       python%{python3_pkgversion}-pyyaml
Requires:       podman

%description
An implementation of docker-compose with podman backend.
The main objective of this project is to be able to run docker-compose.yml
unmodified and rootless.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
 
%install
%pyproject_install
%pyproject_save_files -l 'podman_compose*'

#Drop spurious shebang
sed -i /python3/d %{buildroot}%{python3_sitelib}/podman_compose.py

#Install bash completion
install -Dpm 0644 completion/bash/podman-compose -t %{buildroot}%{bash_completions_dir}


%files -f %{pyproject_files}
%doc README.md CONTRIBUTING.md docs/ examples
%{_bindir}/podman-compose
%{bash_completions_dir}/podman-compose

%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jul 07 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.5.0-1
- 1.5.0

* Fri Jun 06 2025 Python Maint <python-maint@redhat.com> - 1.4.1-2
- Rebuilt for Python 3.14

* Thu Jun 05 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.4.1-1
- 1.4.1

* Tue Jun 03 2025 Python Maint <python-maint@redhat.com> - 1.4.0-3
- Rebuilt for Python 3.14

* Thu May 22 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.4.0-2
- Ship bash completion

* Mon May 12 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.4.0-1
- 1.4.0

* Thu Jan 16 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.3.0-2
- Patch for environment bug.

* Tue Jan 07 2025 Gwyn Ciesla <gwync@protonmail.com> - 1.3.0-1
- 1.3.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 05 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.2.0-1
- 1.2.0

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.13

* Mon Apr 22 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.1.0-1
- 1.1.0

* Thu Feb 15 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.0.6-6
- Drop requirement on podman-plugins, no longer exists with podman >= 5.x

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.0.6-2
- Rebuilt for Python 3.12

* Tue Apr 11 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.0.6-1
- 1.0.6

* Wed Mar 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.0.3-8
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 01 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.0.3-6
- Env patch

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.3-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.0.3-2
- Requires podman-plugins, BZ 2038126.

* Wed Dec 29 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.0.3-1
- 1.0.3

* Tue Nov 23 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.1.8-1
- 0.1.8

* Sun Nov 14 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.1.7-8.git20211114
- Latest git to fix --dry-run issue.

* Thu Nov 11 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.1.7-7.git20211111
- Latest git to fix string substitution issue.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-6.git20210129
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.7-5.git20210129
- Rebuilt for Python 3.10

* Fri Jan 29 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.1.7-4.git20210129
- Update to latest git.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3.git20201120
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> 0.1.7-2.git20201120
- Change deps to be able to build in EPEL8

* Fri Nov 20 2020 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 0.1.7-1.git20201120
- update to the latest git HEAD

* Wed Jul 29 2020 Pavel Raiskup <praiskup@redhat.com> - 0.1.6-1.git20200615
- update to the latest git HEAD; namely to allow spawning privileged containers
  and to fix volume initialization

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5.git20191107
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-4.git20191107
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3.git20191107
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.1.5-2.git20191107
- Fix for service extension with the same name.

* Mon Oct 28 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.1.5-1.git20191030
- Initial build.
