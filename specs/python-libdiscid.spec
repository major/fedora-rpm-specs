Name:           python-libdiscid
Version:        2.0.2
Release:        8%{?dist}
Summary:        Python bindings for libdiscid

License:        MIT
URL:            https://github.com/sebastinas/python-libdiscid
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libdiscid-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-sphinx

%description
python-libdiscid provides Python bindings for libdiscid. libdiscid's
main purpose is the calculation of identifiers for audio discs to use
for the MusicBrainz database.

%package -n python%{python3_pkgversion}-libdiscid
Summary:        Python 3 bindings for libdiscid
%{?python_provide:%python_provide python%{python3_pkgversion}-libdiscid}

%description -n python%{python3_pkgversion}-libdiscid
python%{python3_pkgversion}-libdiscid provides Python 3 bindings for libdiscid. libdiscid's
main purpose is the calculation of identifiers for audio discs to use
for the MusicBrainz database.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup
# for sphinx 6.1.3
sed -i 's/("http:\/\/musicbrainz.org\/doc\/%s", "")/("http:\/\/musicbrainz.org\/doc\/%s", "%s")/g' docs/conf.py


%build
%pyproject_wheel
PYTHONPATH="%{pyproject_build_lib}" sphinx-build-3 docs/ html
rm -rf html/.{doctrees,buildinfo}


%install
%pyproject_install
%pyproject_save_files libdiscid

%check
pushd libdiscid
PYTHONPATH=%{buildroot}%{python3_sitearch}/ %{python3} -m unittest discover -v
popd


%files -n python%{python3_pkgversion}-libdiscid -f %{pyproject_files}
%doc CHANGELOG.md README.md
%exclude %{python3_sitearch}/*libdiscid*/tests/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.2-6
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.0.2-2
- Rebuilt for Python 3.12

* Wed Apr 05 2023 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2 (rhbz #2139176 and #2180472)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 22 2022 Charalampos Stratakis <cstratak@redhat.com> - 2.0.1-3
- Convert to pyproject-rpm-macros
- Fixes FTBFS with setuptools >= 62.1
Resolves: rhbz#2097105

* Sun Jun 19 2022 Python Maint <python-maint@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.11

* Sun Jun 19 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1 (rhbz #1705476, #1771169 and #2097105)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.1-30
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.1-27
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-24
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-22
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-21
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-18
- Subpackage python2-libdiscid has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-16
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.1-14
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Matěj Cepl <mcepl@redhat.com> - 0.4.1-11
- All req. pkgs are in EPEL7, we can built python3 packages as well.

* Fri May 26 2017 Ville Skyttä <ville.skytta@iki.fi> - 0.4.1-10
- Run tests with -Wall

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov  4 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.4.1-5
- Apply upstream fix for Cython >= 0.23

* Thu Aug  6 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.4.1-4
- Spec cleanup per current Python guidelines; Python 2 package is now python2-*

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 11 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.4.1-2
- Build below source dir instead of in %%{py3dir}

* Thu Mar  5 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.4.1-1
- First build
