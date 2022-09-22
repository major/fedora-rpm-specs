%if 0%{?rhel} && 0%{?rhel} <= 7
%bcond_with python3
%if 0%{?rhel} <= 6
%{!?python2_version: %global python2_version %(%{__python2} -c "import sys; sys.stdout.write(sys.version[:3])")}
%{!?_licensedir:%global license %%doc}
%endif
%else
%bcond_without python3
%endif

%if 0%{?fedora} && 0%{?fedora} >= 30
%bcond_with python2
%else
%bcond_without python2
%endif

%bcond_without tests

%global srcname dockerfile-parse
%global modname %(n=%{srcname}; echo ${n//-/_})

Name:           python-%{srcname}
Version:        1.1.0
Release:        13%{?dist}

Summary:        Python library for Dockerfile manipulation
License:        BSD
URL:            https://github.com/DBuildService/dockerfile-parse
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%if %{with python2}
%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}
BuildRequires:  python2-devel
BuildRequires:  python2-six
%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:  python-setuptools
BuildRequires:  pytest
%else
BuildRequires:  python2-setuptools
BuildRequires:  python2-pytest
%endif
Requires:  python2-six

%description -n python2-%{srcname}
%{summary}.

Python 2 version.
%endif # python2 pkg

%if %{with python3}
%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-six
%endif
Requires:  python3-six

%description -n python3-%{srcname}
%{summary}.

Python 3 version.
%endif #python3 pkg

%prep
%setup -q -n %{srcname}-%{version}


%build
%if %{with python2}
%py2_build
%endif # python2
%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif #python2
%if %{with python3}
%py3_install
%endif

%if %{with tests}
%check
export LANG=C.UTF-8
%if %{with python2}
py.test-%{python2_version} -v tests
%endif # python2
%if %{with python3}
py.test-%{python3_version} -v tests
%endif # python3
%endif

%if %{with python2}
%files -n python2-%{srcname}
%license LICENSE
%doc README.md
%{python2_sitelib}/%{modname}-*.egg-info/
%{python2_sitelib}/%{modname}/
%endif

%if %{with python3}
%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{modname}-*.egg-info/
%{python3_sitelib}/%{modname}/
%endif

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.1.0-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.0-9
- Rebuilt for Python 3.10

* Mon Mar 08 2021 David Kirwan <dkirwan@redhat.com> - 1.1.0
- Updated python-dockerfile-parse to 1.1.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.13-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.13-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.0.13-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 12 2019 Athos Ribeiro <athoscr@fedoraproject.org> - 0.0.13-1
- New upstream release 0.0.13
- Require six for RHEL builds
- Do not build python2 packages for Fedora >= 30

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Tim Waugh <twaugh@redhat.com> - 0.0.11-3
- Require six

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Tim Waugh <twaugh@redhat.com> - 0.0.11-1
- New upstream release 0.0.11

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.0.10-2
- Rebuilt for Python 3.7

* Thu Apr 19 2018 Tomas Tomecek <ttomecek@redhat.com> - 0.0.10-1
- New upstream release 0.0.10

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 05 2017 Tomas Tomecek <ttomecek@redhat.com> - 0.0.7-1
- new upstream release: 0.0.7

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.0.5-8
- Rebuild for Python 3.6

* Tue Dec 06 2016 Adam Miller <maxamillion@fedoraproject.org> - 0.0.5-7
- Patch to handle inheriting parent Dockerfile ENVs

* Wed Sep 07 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.5-6
- Modernize spec
- Trivial fixes

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Nov 06 2015 Jiri Popelka <jpopelka@redhat.com> - 0.0.5-2
- %%check section

* Mon Sep 21 2015 Jiri Popelka <jpopelka@redhat.com> - 0.0.5-1
- 0.0.5

* Thu Aug 27 2015 Jiri Popelka <jpopelka@redhat.com> - 0.0.4-1
- 0.0.4

* Tue Jun 30 2015 Jiri Popelka <jpopelka@redhat.com> - 0.0.3-2
- define macros for RHEL-6

* Fri Jun 26 2015 Jiri Popelka <jpopelka@redhat.com> - 0.0.3-1
- 0.0.3

* Fri Jun 26 2015 Jiri Popelka <jpopelka@redhat.com> - 0.0.2-1
- 0.0.2

* Thu Jun 18 2015 Jiri Popelka <jpopelka@redhat.com> - 0.0.1-1
- initial release
