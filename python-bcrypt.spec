%global modname bcrypt
%global sum     Modern password hashing for your software and your servers

Name:               python-bcrypt
Version:            4.0.1
Release:            1%{?dist}
Summary:            %{sum}

#crypt_blowfish code is in Public domain and all other code in ASL 2.0
License:            Apache-2.0 AND LicenseRef-Fedora-Public-Domain
URL:                http://pypi.python.org/pypi/bcrypt
Source0:            %pypi_source bcrypt


%description
%{sum}.


%package -n python3-%{modname}
Summary:            %{sum}
# LICENSE.dependencies contains a full license breakdown
License:            Apache-2.0 AND LicenseRef-Fedora-Public-Domain AND BSD-3-Clause AND MIT AND (Apache-2.0 OR MIT)
BuildRequires:      python3-devel
BuildRequires:      rust-packaging

%description -n python3-%{modname}
%{sum}.


%prep
%autosetup -n %{modname}-%{version} -p1
%cargo_prep
rm src/_bcrypt/Cargo.lock

%generate_buildrequires
%pyproject_buildrequires -t
(cd src/_bcrypt
%cargo_generate_buildrequires
)


%build
export RUSTFLAGS="%build_rustflags"
%pyproject_wheel

(cd src/_bcrypt
%cargo_license_summary
%{cargo_license} > ../../LICENSE.dependencies
)


%install
%pyproject_install
%pyproject_save_files bcrypt


%check
%tox


%files -n python%{python3_pkgversion}-%{modname} -f %{pyproject_files}
%doc README.rst
%license LICENSE LICENSE.dependencies


%changelog
* Wed Feb 08 2023 Sandro Mani <manisandro@gmail.com> - 4.0.1-1
- Update to 4.0.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jul 25 2022 Miro Hrončok <mhroncok@redhat.com> - 3.2.2-4
- Bump the obsoleted release of python3-py-bcrypt

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.2.2-2
- Rebuilt for Python 3.11

* Mon May 02 2022 Major Hayden <major@mhtx.net> - 3.2.2-1
- Update to 3.2.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Major Hayden <major@mhtx.net> - 3.2.0-1
- Update to 3.2.0

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 3.1.7-8
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.7-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 13 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.7-3
- Subpackage python2-bcrypt has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.7-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Tue Aug 20 2019 Pierre-Yves Chibon <pingou@pingoured.fr> - 3.1.7-1
- Update to 3.1.7

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.6-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Marc Dequènes (Duck) <duck@redhat.com> - 3.1.6-2
- Adaptations to build Python 3 on EPEL

* Fri Feb 08 2019 Alfredo Moralejo <amoralej@redhat.com> - 3.1.6-1
- Update to 3.1.6.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.4-5
- Rebuilt for Python 3.7

* Thu Apr 05 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 3.1.4-4
- Fix Requires for epel7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 21 2017 williamjmorenor@gmail.com - 3.1.4-2
- Update python2 requirements
- Enable tests in build

* Sat Oct 21 2017 williamjmorenor@gmail.com - 3.1.4-1
- Update to 3.1.4
  Upstream notes:
   - Fixed compilation with mingw and on illumos.

* Wed Aug 09 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.1.3-4
- Replace py-bcrypt.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 William Moreno <williamjmorenor@gmail.com> - 3.1.3-1
- Update to 3.1.3 upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 10 2017 William Moreno <williamjmorenor@gmail.com> - 3.1.2-1
- Update to v3.1.2

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 3.1.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jun 30 2016 William Moreno <williamjmorenor@gmail.com> - 3.1.0-1
- Update to bugfix release 3.1.0
- Add conflicts for the python3 subpackage

* Thu Jun 30 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 3.0.0-1
- Update to 3.0.0 (Fixes RHBZ#1351377)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.0.0-3
- Add conflicts to py-bcrypt since they both provide a bcrypt python module
- Fix macro that were using %%{module} instead of %%{modname}
- In fact the .so files must be executable, so ensure they are such

* Wed Jan 06 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.0.0-2
- Fix the license as the package has some Public Domain files
- Ensure the .so files are not executable

* Tue Jan 05 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.0.0-1
- initial package for Fedora
