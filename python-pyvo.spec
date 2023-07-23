# For release builds set to 1, for snapshots set to 0
%global relbuild 1 

%if !0%{?relbuild}
%global commit 3fa56a6406ddd7aee0e735aa5ba8b02d11a48780
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20170411
%global git_ver -git%{gitdate}.%{shortcommit}
%global git_rel .git%{gitdate}.%{shortcommit}
%endif # !0%%{?relbuild}

%global srcname pyvo

%global sum Access to remote data and services of the Virtual observatory (VO) using Python
%global desc                                                             \
PyVO is a package providing access to remote data and services of the    \
Virtual Observatory (VO) using Python.                                   \
                                                                         \
The pyvo module currently provides these main capabilities:              \
* Find archives that provide particular data of a particular type and/or \
  relates to a particular topic                                          \
* Search an archive for datasets of a particular type                    \
* Do simple searches on catalogs or databases                            \
* Get information about an object via its name                   

Name:           python-%{srcname}
Version:        1.4.1
Release:        3%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://github.com/astropy/%{srcname}
%if 0%{?relbuild}
Source0:        %{pypi_source} 
%else  # 0%%{?relbuild}
Source0:        %{url}/archive/%{commit}.tar.gz#/%{srcname}-%{version}%{?git_ver}.tar.gz
%endif # 0%%{?relbuild}

BuildArch:      noarch

BuildRequires:  python3-astropy
BuildRequires:  python3-dateutil
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-requests
BuildRequires:  python3-six
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
# Needed to generate docs
BuildRequires:  python3-numpydoc
BuildRequires:  python3-sphinx

Provides:       python3-pyvo-doc = %{version}-%{release}
Obsoletes:      python3-pyvo-doc = %{version}-%{release}

%description
%{desc}

%package -n python3-%{srcname}
Summary:        %{sum}
Requires:       astropy-tools
Requires:       python3-astropy
Requires:       python3-dateutil
Requires:       python3-requests
Requires:       python3-six
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}

%prep
%if 0%{?relbuild}
%autosetup -n %{srcname}-%{version} -p 1
%else  # 0%%{?relbuild}
%autosetup -n %{srcname}-%{commit} -p 1
%endif # 0%%{?relbuild}
sed -i -e 's|mimeparse|python-mimeparse|' setup.cfg


%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license licenses/LICENSE.rst
%doc CHANGES.rst README.rst
%{python3_sitelib}/*


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul  7 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.1-2
- Drop BR: python3-astropy-helpers, no longer used

* Mon Mar 27 2023 Christian Dersch <lupinix@fedoraproject.org> - 1.4.1-1
- new version

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 26 2022 Christian Dersch <lupinix@fedoraproject.org> - 1.4-1
- Update to version 1.4

* Wed Sep 14 2022 Christian Dersch <lupinix@fedoraproject.org> - 1.3-1
- Update to version 1.3

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 26 2021 Christian Dersch <lupinix@fedoraproject.org> - 1.2-1
- new version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Christian Dersch <lupinix@fedoraproject.org> - 1.1-1
- new version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Christian Dersch <lupinix@fedoraproject.org> - 1.0-1
- new version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.3-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul 20 2019 Kevin Fenzi <kevin@scrye.com> - 0.9.3-2
- Fix requires for python-mimeparse instead of just mimeparse

* Fri May 31 2019 Christian Dersch <lupinix@fedoraproject.org> - 0.9.3-1
- new version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 19 2018 Christian Dersch <lupinix.fedora@gmail.com> - 0.9.2-1
- new version

* Tue Oct 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.9.1-2
- drop python2 subpackage (#1634584)

* Tue Oct 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.9.1-1
- new version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Christian Dersch <lupinix@mailbox.org> - 0.8.1-3
- Fix build with Python 3.7

* Fri Jul 06 2018 Christian Dersch <lupinix.fedora@gmail.com> - 0.8.1-2
- Rebuild for Python 3.7

* Wed Jun 27 2018 Christian Dersch <lupinix@fedoraproject.org> - 0.8.1-1
- new version

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8-2
- Rebuilt for Python 3.7

* Fri Jun 08 2018 Christian Dersch <lupinix.fedora@gmail.com> - 0.8-1
- new version

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 0.6.1-4
- rebuilt

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Christian Dersch <lupinix@mailbox.org> - 0.6.1-1
- new version

* Tue Apr 11 2017 Christian Dersch <lupinix@mailbox.org> - 0.6.0-1.git20170411.3fa56a6
- new version

* Thu Feb 09 2017 Christian Dersch <lupinix@mailbox.org> - 0.5.2-1
- new version

* Tue Jan 17 2017 Christian Dersch <lupinix@mailbox.org> - 0.5.0.1-1
- new version

* Mon Jan 16 2017 Christian Dersch <lupinix@mailbox.org> - 0.5.0-1
- new version

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-3.20161020git823b14a
- Rebuild for Python 3.6

* Sun Dec 04 2016 Christian Dersch <lupinix@mailbox.org> - 0.4.1-2.20161020git823b14a
- Added -doc subpackage
- Added missing requirement for requests

* Mon Oct 31 2016 Christian Dersch <lupinix@mailbox.org> - 0.4.1-1
- new version

* Wed Oct  5 2016 Christian Dersch <lupinix@mailbox.org> - 0.0-0.1.2016100570090d6
- Initial package

