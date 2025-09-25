Name:               python-Mastodon
Version:            2.1.4
Release:            1%{?dist}
Summary:            Python wrapper for the Mastodon API


License:            MIT
URL:                https://github.com/halcy/Mastodon.py
Source:             %{url}/archive/v%{version}/Mastodon.py-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      tomcli

%description
%{summary}.

%package -n python3-Mastodon
Summary:            %{summary}

%description -n python3-Mastodon
%{summary}.

%pyproject_extras_subpkg -n python3-Mastodon webpush blurhash

%prep
%autosetup -n Mastodon.py-%{version}
# Not packaged, and not strictly required:
tomcli set pyproject.toml lists delitem project.optional-dependencies.test \
    pytest-retry
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
tomcli set pyproject.toml lists delitem project.optional-dependencies.test \
    pytest-cov
tomcli set pyproject.toml del tool.pytest.ini_options.addopts
# Avoid conflict of python3-magic with python3-file-magic, and it's not needed.
tomcli set pyproject.toml lists delitem project.dependencies 'python-magic ; platform_system!="Windows"'

%generate_buildrequires
%pyproject_buildrequires -x webpush,blurhash,test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mastodon

%check
#Disable tests until after 2.0.1
#%%pytest

%files -n python3-Mastodon -f %{pyproject_files}
%doc README.rst

%changelog
* Tue Sep 23 2025 Gwyn Ciesla <gwync@protonmail.com> - 2.1.4-1
- 2.1.4

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 2.1.3-2
- Rebuilt for Python 3.14.0rc3 bytecode

* Tue Sep 02 2025 Gwyn Ciesla <gwync@protonmail.com> - 2.1.3-1
- 2.1.3

* Wed Aug 20 2025 Gwyn Ciesla <gwync@protonmail.com> - 2.1.2-1
- 2.1.2

* Tue Aug 19 2025 Gwyn Ciesla <gwync@protonmail.com> - 2.1.1-1
- 2.1.1

* Mon Aug 18 2025 Gwyn Ciesla <gwync@protonmail.com> - 2.1.0-1
- 2.1.0

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 2.0.1-6
- Rebuilt for Python 3.14.0rc2 bytecode

* Wed Jul 30 2025 Gwyn Ciesla <gwync@protonmail.com> - 2.0.1-5
- Drop optional requirement on python3-magic

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Fri Jun 06 2025 Python Maint <python-maint@redhat.com> - 2.0.1-3
- Rebuilt for Python 3.14

* Mon May 26 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 2.0.1-2
- Use pytest instead of deprecated pytest-runner
- Actually run the tests
- Port to pyproject-rpm-macros and add extras metapackages
- Omit unwanted coverage-analysis dependencies

* Sun Mar 02 2025 Gwyn Ciesla <gwync@protonmail.com> - 2.0.1-1
- 2.0.1

* Mon Feb 17 2025 Gwyn Ciesla <gwync@protonmail.com> - 2.0.0-1
- 2.0.0

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 1.8.1-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 01 2023 Python Maint <python-maint@redhat.com> - 1.8.1-2
- Rebuilt for Python 3.12

* Mon Apr 24 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.8.1-1
- 1.8.1

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.8.0-3
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.8.0-1
- 1.8.0

* Mon Nov 28 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.7.0-1
- 1.7.0

* Mon Nov 21 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.6.3-1
- 1.6.3

* Thu Nov 17 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.6.1-1
- 1.6.1

* Mon Nov 07 2022 Gwyn Ciesla <gwync@protonmail.com> - 1.5.2-1
- 1.5.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.1-8
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.1-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-2
- Rebuilt for Python 3.9

* Mon Mar 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 1.5.1-1
- 1.5.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.5.0-1
- 1.5.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.6-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.6-2
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.6-1
- 1.4.6

* Mon Jun 24 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.5-1
- 1.4.5

* Wed Jun 12 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.3-2
- Patch out blurhash.

* Fri May 31 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.3-1
- 1.4.3

* Mon May 13 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.2-1
- 1.4.2

* Mon May 13 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.1-1
- 1.4.1

* Fri May 10 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.0-2
- Disable auto-deps.

* Mon Apr 29 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.0-1
- 1.4.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 28 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.3.1-2
- Fix broken deps.

* Thu Sep 13 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.3.1-1
- 1.3.1, drop Python2 per BZ 1627376.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.3.0-1
- 1.3.0
- Disabled Python 3 tests, failing in mock.

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-2
- Rebuilt for Python 3.7

* Fri Mar 09 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.2.2-1
- 1.2.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.1-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Dec 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.2.1-1
- 1.2.1, 2.1.0 compatibility.
- Disabled Python 2 tests, failing in mock.

* Tue Nov 21 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.1.2-1
- 1.1.2, full Mastodon 2.0.0 support.

* Mon Oct 16 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.1.1-2
- Fix macro usage for review.

* Fri Oct 13 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.1.1-1
- Initial package.
