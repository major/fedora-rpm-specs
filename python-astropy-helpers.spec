%global srcname astropy-helpers
%global sum Utilities for building and installing Astropy and Astropy affiliated packages

# Description for all subpackages
%global common_description                                                   \
This project provides a Python package, astropy_helpers, which includes many \
build, installation, and documentation-related tools used by the Astropy     \
project, but packaged separately for use by other projects that wish to      \
leverage this work. The motivation behind this package and details of its    \
implementation are in the accepted Astropy Proposal for Enhancement (APE) 4.

Name:           python-%{srcname}
Version:        4.0.1
Release:        12%{?dist}
Summary:        %{sum}

License:        BSD
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
# Workaround for python 3.12 change of imp module removal
Patch0:         astropy_helpers-py312-imp-deprecation.patch

BuildArch:      noarch
BuildRequires:  gcc gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-numpy
BuildRequires:  python3-sphinx
BuildRequires:  python3-pytest

%description
%{common_description}

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-numpy
Requires:       python3-setuptools
Requires:       python3-sphinx

%description -n python3-%{srcname}
%{common_description}


%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%py3_build

%install
%py3_install

%check
# Tests disabled for Python3 as they are not yet ported completely
# (they require the compiler module removed in Python 3)
#%%{__python3} setup.py test


%files -n python3-%{srcname}
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{python3_sitelib}/*

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul  7 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.1-11
- Workaround for python 3.12 change of imp module removal

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 4.0.1-10
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 4.0.1-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.0.1-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 17 2020 Christian Dersch <lupinix@fedoraproject.org> - 4.0.1-1
- new version

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 27 2019 Christian Dersch <lupinix@fedoraproject.org> - 3.2.2-1
- new version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Christian Dersch <lupinix@fedoraproject.org> - 3.1.1-1
- new version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Christian Dersch <lupinix@fedoraproject.org> - 3.0.2-1
- new version
- dorp python2 submodule (upstream does not support this anymore)

* Sun Jul 15 2018 Christian Dersch <lupinix@fedoraproject.org> - 2.0.4-4
- BuildRequires: gcc gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-2
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Christian Dersch <lupinix@mailbox.org> - 2.0.4-1
- new version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.2-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Oct 19 2017 Christian Dersch <lupinix@mailbox.org> - 2.0.2-1
- new version

* Sun Oct 08 2017 Christian Dersch <lupinix@mailbox.org> - 2.0.1-1
- new version

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 26 2016 Christian Dersch <lupinix@mailbox.org> - 1.3-1
- new version

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2-2
- Rebuild for Python 3.6

* Sun Sep 25 2016 Christian Dersch <lupinix@mailbox.org> - 1.2-1
- new version

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Mar 25 2016 Christian Dersch <lupinix@mailbox.org> - 1.1.2-1
- new version

* Sun Jan 10 2016 Christian Dersch <lupinix@mailbox.org> - 1.1.1-1
- Initial spec


