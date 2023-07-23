%global srcname lazr.smtptest
%global pkgname lazr-smtptest
%global summary Test framework for SMTP-based applications
%global _description \
This is LAZR smtptest, a framework for testing SMTP-based applications and \
libraries. It provides a real, live SMTP server that you can send messages \
to, and from which you can read those test messages. This can be used to   \
ensure proper operation of your applications which send email.

Name:           python-%{pkgname}
Version:        2.0.3
Release:        25%{?dist}
Summary:        %{summary}

License:        LGPLv3
URL:            https://launchpad.net/lazr.smtptest
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

# Make tests pass on machines with IPv6
Patch0:         %{name}-ipv6.patch
Patch1:         %{name}-py36.patch
Patch2:         %{name}-py37.patch

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-nose
%if 0%{?with_python3_other}
BuildRequires: python%{python3_other_pkgversion}-devel
BuildRequires: python%{python3_other_pkgversion}-setuptools
BuildRequires: python%{python3_other_pkgversion}-nose
%endif


%description %{_description}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}
Requires:       python%{python3_pkgversion}-setuptools
Requires:       python%{python3_pkgversion}-nose

%description -n python%{python3_pkgversion}-%{pkgname} %{_description}


%if 0%{?with_python3_other}
%package -n python%{python3_other_pkgversion}-%{pkgname}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{pkgname}}
Requires:       python%{python3_other_pkgversion}-setuptools
Requires:       python%{python3_other_pkgversion}-nose

%description -n python%{python3_other_pkgversion}-%{pkgname} %{_description}
%endif


%prep
%autosetup -n %{srcname}-%{version} -p0


%build
%py3_build
%if 0%{?with_python3_other}
%py3_other_build
%endif


%install
%py3_install
%if 0%{?with_python3_other}
%py3_other_install
%endif


%check
%{__python3} setup.py nosetests
%if 0%{?with_python3_other}
%{__python3_other} setup.py nosetests
%endif


%files -n python%{python3_pkgversion}-%{pkgname}
%license COPYING.txt
%doc README.rst HACKING.rst
%{python3_sitelib}/lazr/
%{python3_sitelib}/%{srcname}-%{version}*-py%{python3_version}.egg-info/
%{python3_sitelib}/%{srcname}-%{version}*-py%{python3_version}-nspkg.pth

%if 0%{?with_python3_other}
%files -n python%{python3_other_pkgversion}-%{pkgname}
%license COPYING.txt
%doc README.rst HACKING.rst
%{python3_other_sitelib}/lazr/
%{python3_other_sitelib}/%{srcname}-%{version}*-py%{python3_other_version}.egg-info/
%{python3_other_sitelib}/%{srcname}-%{version}*-py%{python3_other_version}-nspkg.pth
%endif


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.3-24
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.0.3-21
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.3-18
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-10
- Dropped the Python subpackage (#1628181)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Aurelien Bompard <abompard@fedoraproject.org> - 2.0.3-8
- Add patch to fix Python 3.7 build

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Aurelien Bompard <abompard@fedoraproject.org> - 2.0.3-3
- Fix build on Python 3.6

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-2
- Rebuild for Python 3.6

* Thu Oct 20 2016 Aurelien Bompard <abompard@fedoraproject.org> - 2.0.3-1
- Initial package.
