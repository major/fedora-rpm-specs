%global srcname watchdog

%global common_description %{expand: \
Python API and shell utilities to monitor file system events.

Works on 3.7+.}

Name:               python-%{srcname}
Version:            3.0.0
Release:            %autorelease
Summary:            File system events monitoring

License:            Apache-2.0
URL:                https://github.com/gorakhargosh/watchdog
Source0:            %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:          noarch

%description %{common_description}

%package -n python3-%{srcname}
Summary:            %{summary}

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-pytest
BuildRequires:      python3-pytest-cov
BuildRequires:      python3-pytest-rerunfailures
BuildRequires:      python3-pytest-timeout
BuildRequires:      python3-PyYAML

%description -n python3-%{srcname} %{common_description}


%prep
%autosetup -p1 -n %{srcname}-%{version}
# Remove all shebangs
find src -name "*.py" | xargs sed -i -e '/^#!\//, 1d'
# Remove +x of the README file
chmod -x README.rst

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
# test_unmount_watched_directory_filesystem,test_unmount_watched_directory_filesystem requires sudo and cannot work here.
%pytest -v -k 'not test_unmount_watched_directory_filesystem' -k 'not test_unmount_watched_directory_filesystem'


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/watchmedo*


%changelog
* Tue Aug 08 2023 Jonathan Steffan <jsteffan@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 2.1.9-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 29 2022 Julien Enselme <jujens@jujens.eu> - 2.1.9-1
- Update to 2.1.9

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.6-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 04 2021 Charalampos Stratakis <cstratak@redhat.com> - 2.1.6-1
- Update to 2.1.6
- Remove redundant python-argh dependency

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.10.2-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.2-2
- Rebuilt for Python 3.9

* Tue Feb 18 2020 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.10.2-1
- Update to the upstream release 0.10.2
- Use the pypi_source macro for Source0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-14
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-13
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-12
- Remove python2-watchdog

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-9
- Rebuilt for Python 3.7

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.3-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.3-4
- Rebuild for Python 3.6

* Mon Aug 15 2016 Julien Enselme <jujens@jujens.eu> - 0.8.3-3
- Add python-pytest-timeout to BR to launch tests

* Thu Aug 12 2016 Julien Enselme <jujens@jujens.eu> - 0.8.3-2
- Add python2-pathtools to BR (was two times in Requires)

* Thu Aug 11 2016 Julien Enselme <jujens@jujens.eu> - 0.8.3-1
- Update to 0.8.3
- Correct requires
- Update to follow new Python packaging guidelines
- Always build with Python 3

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 22 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.8.2-1
- Update to 0.8.2

* Fri Apr 25 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7.1-4
- Adjust the license tag to ASL2.0 and BSD and MIT

* Fri Apr 18 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7.1-3
- Adjust the check for Fedora/RHEL release number for the py3 package

* Fri Apr 18 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7.1-2
- Remove all shebang of the python files

* Fri Apr 18 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7.1-1
- initial package for Fedora
