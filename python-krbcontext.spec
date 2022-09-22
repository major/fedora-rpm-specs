%global src_name krbcontext

Summary: A Kerberos context manager
Name: python-%{src_name}
Version: 0.10
Release: 12%{?dist}
Source0: https://files.pythonhosted.org/packages/source/k/%{src_name}/%{src_name}-%{version}.tar.gz
License: GPLv3
Url: https://github.com/krbcontext/python-krbcontext
BuildArch: noarch

%description
krbcontext provides a Kerberos context that you can put code inside, which
requires a valid ticket in credential cache.

krbcontext is able to initialize credential cache automatically on behalf
of you according to the options you specify. It can initialize with keytab or a
regular user's Kerberos name and password.

You can use krbcontext as a context manager with with statement, or
call API directly to check credential cache and even initialize by yourself.

# Build Python 2 package for Fedora and only for RHEL7

%if 0%{?fedora}
%package -n python3-%{src_name}
Summary: A Kerberos context manager

BuildRequires: python3-setuptools
BuildRequires: python3-devel
BuildRequires: python3-gssapi
# For running test
BuildRequires: python3-mock
BuildRequires: python3-pytest
#BuildRequires: python3-pytest-cov

Requires: python3-gssapi
%{?python_provide:%python_provide python%{python3_pkgversion}-%{src_name}}

%description -n python3-%{src_name}
krbcontext provides a Kerberos context that you can put code inside, which
requires a valid ticket in credential cache.

krbcontext is able to initialize credential cache automatically on behalf
of you according to the options you specify. It can initialize with keytab or a
regular user's Kerberos name and password.

You can use krbcontext as a context manager with with statement, or
call API directly to check credential cache and even initialize by yourself.

%endif
# end of Python 3 package

%prep
%setup -q -n %{src_name}-%{version}

%build

%if 0%{?fedora}
%py3_build
%endif

%install

%if 0%{?fedora}
%py3_install
%endif

%check

%if 0%{?fedora}
PYTHONPATH=. py.test-%{python3_version} test/
%endif

%if 0%{?fedora}
%files -n python3-%{src_name}
%doc README.rst CHANGELOG.rst docs/
%license LICENSE
%{python3_sitelib}/krbcontext/
%{python3_sitelib}/krbcontext-%{version}-*.egg-info
%endif

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.10-11
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.10-8
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10-2
- Rebuilt for Python 3.8

* Sat Aug 03 2019 Chenxiong Qi <cqi@redhat.com> - 0.10-1
- Build release 0.10

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 2019 Chenxiong Qi <cqi@redhat.com> - 0.9-1
- Build release version 0.9

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8-7
- Subpackage python2-krbcontext has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8-5
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 07 2017 Chenxiong Qi <qcxhome@gmail.com> - 0.8-2
- Remove flake8 from BuildRequires

* Tue Sep 05 2017 Chenxiong Qi <qcxhome@gmail.com> - 0.8-1
- Fix SPEC (Chenxiong Qi)
- Use __future__.absolute_import (Chenxiong Qi)
- Fix and enhance maintanence scripts (Chenxiong Qi)

* Wed Aug 30 2017 Chenxiong Qi <qcxhome@gmail.com> - 0.7-1
- Remove unused meta info (Chenxiong Qi)
- Fix init_with_keytab and tests (Chenxiong Qi)
- Add script for publishing packages (Chenxiong Qi)
- Refine make release script (Chenxiong Qi)

* Sun Aug 27 2017 Chenxiong Qi <qcxhome@gmail.com> - 0.6-1
- Fix reading package info (Chenxiong Qi)

* Sat Aug 26 2017 Chenxiong Qi <qcxhome@gmail.com> - 0.5-1
- Add script for making release (Chenxiong Qi)
- Add distcheck to Makefile (Chenxiong Qi)
- Refine doc settings (Chenxiong Qi)
- Easy to set project info (Chenxiong Qi)
- Bump version to 4.0 in doc (Chenxiong Qi)

* Sat Aug 26 2017 Chenxiong Qi <qcxhome@gmail.com> - 0.4-1
- Migrate to python-gssapi
- Compatible with Python 3

* Thu Mar 13 2014 Chenxiong Qi <cqi@redhat.com> - 0.3.3-1
- Change README.txt to README.rst
- Fix: logic error of KRB5CCNAME maintenance during initialization
- Fix testcase of getting default credential cache

* Fri Jan 18 2013 Chenxiong Qi <cqi@redhat.com> - 0.3.1-1
- Thread-safe credentials cache initialization

* Thu Jan 10 2013 Chenxiong Qi <cqi@redhat.com> - 0.3.0-1
- Lazy initialization of credential cache.
- Refactor all code
- Rewrite all unittest
- Improve SPEC
- Improve configuration of Python package distribution
- Update documentation

* Mon Jul 30 2012 Chenxiong Qi <cqi@redhat.com> - 0.2-1
- Initial package
