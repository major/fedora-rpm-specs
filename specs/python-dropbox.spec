%global pypi_name dropbox
Name:           python-%{pypi_name}
Version:        12.0.2
Release:        4%{?dist}
Summary:        Official Dropbox REST API Client
License:        MIT

URL:            https://www.dropbox.com/developers/core/sdks
Source0:        %pypi_source
Patch0:         unpin-pytest-runner.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest-runner

%description
A Python library for Dropbox's HTTP-based Core and Datastore APIs.

%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-requests
Requires:       python3-six
Requires:       python3-urllib3

%description -n python3-%{pypi_name}
A Python library for Dropbox's HTTP-based Core and Datastore APIs.

%prep
%setup -q -n %{pypi_name}-%{version}

%patch -P 0 -p0

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 12.0.2-2
- Rebuilt for Python 3.13

* Mon Jun 03 2024 Gwyn Ciesla <gwync@protonmail.com> - 12.0.2-1
- 12.0.2

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.36.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 11.36.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.36.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 11.36.2-2
- Rebuilt for Python 3.12

* Tue Jun 13 2023 Gwyn Ciesla <gwync@protonmail.com> - 11.36.2-1
- 11.36.2

* Tue Apr 25 2023 Gwyn Ciesla <gwync@protonmail.com> - 11.36.0-5
- Fix FTBFS, patch macros.

* Thu Mar 09 2023 Gwyn Ciesla <gwync@protonmail.com> - 11.36.0-4
- Fix glob, move to pyprject macros.

* Wed Mar 08 2023 Gwyn Ciesla <gwync@protonmail.com> - 11.36.0-3
- migrated to SPDX license

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 11.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 10 2022 Gwyn Ciesla <gwync@protonmail.com> - 11.36.0-1
- 11.36.0

* Wed Oct 12 2022 Gwyn Ciesla <gwync@protonmail.com> - 11.35.0-1
- 11.35.0

* Tue Sep 06 2022 Gwyn Ciesla <gwync@protonmail.com> - 11.34.0-1
- 11.34.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.33.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 13 2022 Gwyn Ciesla <gwync@protonmail.com> - 11.33.0-1
- 11.33.0

* Wed Jul 06 2022 Gwyn Ciesla <gwync@protonmail.com> - 11.32.0-1
- 11.32.0

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 11.31.0-2
- Rebuilt for Python 3.11

* Thu May 19 2022 Gwyn Ciesla <gwync@protonmail.com> - 11.31.0-1
- 11.31.0

* Tue Apr 26 2022 Gwyn Ciesla <gwync@protonmail.com> - 11.30.0-1
- 11.30.0

* Tue Apr 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 11.29.0-1
- 11.29.0

* Thu Mar 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 11.28.0-1
- 11.28.0

* Thu Feb 03 2022 Gwyn Ciesla <gwync@protonmail.com> - 11.27.0-1
- 11.27.0

* Thu Jan 27 2022 Gwyn Ciesla <gwync@protonmail.com> - 11.26.0-1
- 11.26.0

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 30 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.25.0-1
- 11.25.0

* Thu Nov 18 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.24.0-1
- 11.24.0

* Thu Nov 04 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.23.0-1
- 11.23.0

* Fri Oct 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.22.0-1
- 11.22.0

* Thu Sep 30 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.21.0-1
- 11.21.0

* Thu Sep 23 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.20.0-1
- 11.20.0

* Wed Sep 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.19.0-1
- 11.19.0

* Thu Aug 26 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.18.0-1
- 11.18.0

* Wed Aug 18 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.17.0-1
- 11.17.0

* Thu Aug 12 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.16.0-1
- 11.16.0

* Thu Jul 29 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.15.0-1
- 11.15.0

* Wed Jul 21 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.14.0-1
- 11.14.0

* Wed Jul 14 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.13.3-1
- 11.13.3

* Thu Jul 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 1.13.2-1
- 11.13.2

* Fri Jul 02 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.13.1-1
- 11.13.1

* Thu Jul 01 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.13.0-1
- 11.13.0

* Wed Jun 23 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.12.0-1
- 11.12.0

* Thu Jun 17 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.11.0-1
- 11.11.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 11.10.0-2
- Rebuilt for Python 3.10

* Thu May 27 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.10.0-1
- 11.10.0

* Fri May 14 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.9.0-1
- 11.9.0

* Fri May 07 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.8.0-1
- 11.8.0

* Wed Apr 14 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.7.0-1
- 11.7.0

* Thu Apr 08 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.6.0-1
- 11.6.0

* Thu Mar 25 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.5.0-1
- 11.5.0

* Tue Mar 09 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.4.1-1
- 11.4.1

* Fri Feb 19 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.3.0-1
- 11.3.0

* Wed Feb 10 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.2.0-1
- 11.2.0

* Tue Jan 26 2021 Gwyn Ciesla <gwync@protonmail.com> - 11.1.0-1
- 11.1.0

* Fri Dec 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 11.0.0-1
- 11.0.0

* Fri Dec 04 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.11.0-1
- 10.11.0

* Fri Nov 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.10.0-1
- 10.10.0

* Wed Nov 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.9.0-1
- 10.9.0

* Fri Oct 30 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.8.0-1
- 10.8.0

* Thu Oct 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.7.0-1
- 10.7.0

* Mon Oct 12 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.6.0-1
- 10.6.0

* Tue Oct 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.5.0-1
- 10.5.0

* Fri Aug 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.4.1-1
- 10.4.1

* Tue Aug 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.3.1-1
- 10.3.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.3.0-1
- 10.3.0

* Sun May 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.2.0-1
- 10.2.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 10.1.2-2
- Rebuilt for Python 3.9

* Thu May 07 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.1.2-1
- 10.1.2

* Tue Apr 21 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.1.1-1
- 10.1.1

* Thu Apr 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.1.0-1
- 10.1.0

* Thu Apr 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 10.0.0-1
- 10.0.0

* Fri Mar 20 2020 Gwyn Ciesla <gwync@protonmail.com> - 9.5.0-1
- 9.5.0.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 9.4.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 9.4.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Gwyn Ciesla <gwync@protonmail.com> - 9.4.0-2
- Drop Python 2.

* Fri Jun 14 2019 Gwyn Ciesla <gwync@protonmail.com> - 9.4.0-1
- 9.4.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Gwyn Ciesla <limburgher@gmail.com> - 9.3.0-1
- 9.3.0

* Fri Jul 13 2018 Miro Hrončok <mhroncok@redhat.com> - 9.0.0-1
- Update to 9.0.0 (#1600097)
- Reenable python3-dropbox

* Fri Jun 29 2018 Miro Hrončok <mhroncok@redhat.com> - 8.9.0-2
- Disable python3-dropbox with Python 3.7

* Wed May 23 2018 Charalampos Stratakis <cstratak@redhat.com> - 8.9.0-1
- Updated to 8.9.0 (#1535988)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Lumír Balhar <lbalhar@redhat.com> - 8.5.1-1
- Updated to 8.5.1 (#1528473)

* Mon Dec 04 2017 Charalampos Stratakis <cstratak@redhat.com> - 8.5.0-1
- Updated to 8.5.0 (#1503364)

* Fri Sep 15 2017 Charalampos Stratakis <cstratak@redhat.com> - 8.2.0-1
- Updated to 8.2.0 (#1493317)

* Fri Sep 15 2017 Charalampos Stratakis <cstratak@redhat.com> - 8.1.0-1
- Updated to 8.1.0 (#1450023)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 17 2017 Miro Hrončok <mhroncok@redhat.com> - 7.2.1-1
- Updated to 7.2.1 (#1361160)
- Updated to the new naming scheme

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 6.5.0-2
- Rebuild for Python 3.6

* Wed Jul 27 2016 Miro Hrončok <mhroncok@redhat.com> - 6.5.0-1
- Update to 6.5.0 (#1283806)

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.41-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 Miro Hrončok <mhroncok@redhat.com> - 3.41-3
- Update to 3.41 (#1258447)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.22-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Aug 28 2015 Miro Hrončok <mhroncok@redhat.com> - 3.22-1
- Update to 3.22 (#1256561)
- Remove %%check completely as it requires API tokens, etc.

* Sat Aug 15 2015 Stephen Gallagher <sgallagh@redhat.com> 2.2.0-3
- Disable tests to resolve FTBFS
- Performed as part of the Flock 2015 Package Cleanup Workshop

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep 24 2014 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-1
- Updated to 2.2.0 (#1145025)

* Sat Jun 07 2014 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-1
- Updated to 2.1.0 (#1104561)

* Wed May 14 2014 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-2
- Rebuilt for Python 3.4

* Wed May 14 2014 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-1
- Updated to 2.0.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Miro Hrončok <mhroncok@redhat.com> - 1.6-3
- Use source package from dropbox.org
- Added LICENSE
- chmod -x examples
- Added BR python-mock

* Wed Jul 10 2013 Miro Hrončok <mhroncok@redhat.com> - 1.6-2
- Removed duplicate BR python3-setuptools
- Delete bundled egg-info

* Mon Jul 08 2013 Miro Hrončok <mhroncok@redhat.com> - 1.6-1
- First package

