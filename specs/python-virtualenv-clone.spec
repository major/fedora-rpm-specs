%global srcname virtualenv-clone

Name:             python-virtualenv-clone
Version:          0.5.7
Release:          13%{?dist}
Summary:          Script to clone Python virtual environments

License:          MIT
URL:              https://github.com/edwardgeorge/virtualenv-clone
# Use GitHub source archive rather than the one on PyPI since the latter omits
# the tests/ directory and tox.ini file.
Source0:          %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

# Allow the current Python version in tests
# Extend the hardcoded list of Python versions with sys.version_info
Patch:            https://github.com/edwardgeorge/virtualenv-clone/pull/76.patch

BuildArch:        noarch
BuildRequires:    python3-devel

%global _description %{expand:
A script for cloning a non-relocatable Python virtual environment.

Virtualenv provides a way to make a virtual environment relocatable which could
then be copied as we wanted. However, making a virtualenv relocatable this way
breaks the no-site-packages isolation of the virtualenv as well as other
aspects that come with relative paths and '/usr/bin/env' shebangs that may be
undesirable. Also, the '.pth' and '.egg-link' rewriting doesn't seem to work as
intended.

Virtualenv-clone attempts to overcome these issues and provide a way to easily
clone an existing virtualenv.}

%description %_description

%package -n python3-virtualenv-clone
Summary:          %{summary}
Requires:         python3-virtualenv

%description -n python3-virtualenv-clone %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files clonevirtualenv


%check
%tox


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license LICENSE
%{_bindir}/virtualenv-clone


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.5.7-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Karolina Surma <ksurma@redhat.com> - 0.5.7-7
- Allow Python 3.12 in tests

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.5.7-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.5.7-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 09 2021 Tadej Janež <tadej.j@nez.si> - 0.5.7-1
- Update to 0.5.7 release

* Wed Jul 28 2021 Tadej Janež <tadej.j@nez.si> - 0.5.6-1
- Update to 0.5.6 release

* Tue Jul 27 2021 Tadej Janež <tadej.j@nez.si> - 0.5.5-1
- Update to 0.5.5 release
- Update URL with project's GitHub home page
- Update Source0 to use the GitHub source archive
- Add LICENSE file
- Rewrite the SPEC file to use the new Python Packaging Guidelines:
  https://fedoraproject.org/wiki/Changes/PythonPackagingGuidelines202x
- Run package's tests in %%check
- Add support for Python 3.10
- Improve Summary's and Description's wording
- Add custom rpmlint config and ignore spurious spelling errors

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.5.4-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Tadej Janež <tadej.j@nez.si> - 0.5.4-1
- Update to 0.5.4 release
- Add explicit BuildRequires on python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.3-2
- Rebuilt for Python 3.8

* Wed Jul 31 2019 Tadej Janež <tadej.j@nez.si> - 0.5.3-1
- Update to 0.5.3 release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-13
- Drop the Python 2 package (#1661353)

* Fri Aug 24 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-12
- Only one /usr/bin/virtualenv-clone

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.6-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.6-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Ralph Bean <rbean@redhat.com> - 0.2.6-2
- Enable the python3 subpackage.
- Create a separate python2 subpackage and modernize macros.

* Mon Jun 29 2015 Ralph Bean <rbean@redhat.com> - 0.2.6-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Ralph Bean <rbean@redhat.com> - 0.2.4-1
- initial package for Fedora
