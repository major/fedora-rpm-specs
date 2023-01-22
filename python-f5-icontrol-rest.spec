%global srcname f5-icontrol-rest
%global sum F5 BIG-IP iControl REST API client

%if 0%{?fedora} <= 29 && 0%{?rhel} <= 7
%bcond_without python2
%else
%bcond_with    python2
%endif
%if 0%{?fedora} || 0%{?rhel} >= 7
%bcond_without python3
%else
%bcond_with    python3
%endif

Name:           python-%{srcname}
Version:        1.3.15
Release:        9%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/F5Networks/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%if 0%{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-requests >= 2.5.0
BuildRequires:  python2-urllib3
# doc
BuildRequires:  python2-sphinx
BuildRequires:  python2-sphinx_rtd_theme
# tests
BuildRequires:  python2-mock
BuildRequires:  python2-pytest
# Not packaged yet...
#BuildRequires:  python2-pytest-symbols
%{!?el7:BuildRequires:  python2-coveralls}
%{!?el7:BuildRequires:  python2-flake8}
%{?el7:BuildRequires:  python-flake8}
BuildRequires:  python2-mccabe
BuildRequires:  python2-pyflakes
BuildRequires:  python2-requests-mock
BuildRequires:  python2-pytest-cov
%endif

%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-requests >= 2.5.0
BuildRequires:  python%{python3_pkgversion}-urllib3
# doc
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme
# tests
%{!?el7:BuildRequires:  python%{python3_pkgversion}-coveralls}
%{!?el7:BuildRequires:  python%{python3_pkgversion}-flake8}
BuildRequires:  python%{python3_pkgversion}-mccabe
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-pyflakes
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-cov
# Not packaged yet...
#BuildRequires:  python%{python3_pkgversion}-pytest-symbols
%{!?el7:BuildRequires:  python%{python3_pkgversion}-requests-mock}
%endif


%description
Generic python library used by the F5 SDK and other F5 projects to communicate
with BIG-IP® via the REST API.

%if 0%{?with_python2}
%package -n python2-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python2-%{srcname}}
Requires:       python2-requests >= 2.5.0

%description -n python2-%{srcname}
Generic python library used by the F5 SDK and other F5 projects to communicate
with BIG-IP® via the REST API.
%endif

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}
Requires:       python%{python3_pkgversion}-requests >= 2.5.0

%description -n python%{python3_pkgversion}-%{srcname}
Generic python library used by the F5 SDK and other F5 projects to communicate
with BIG-IP® via the REST API.
%endif


%prep
%autosetup -n %{srcname}-python-%{version}
# Remove functional tests, they need a real BIG-IP
rm -rf icontrol/test/functional


%build
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%{!?el7:%{__python3} setup.py build_sphinx}
%{!?el7:rm build/sphinx/html/.buildinfo}
%endif


%install
%if 0%{?with_python2}
%py2_install
%endif
%if 0%{?with_python3}
%py3_install
%endif


%check
%if 0%{?with_python2}
%{__python2} setup.py test
%endif
%if 0%{?with_python3}
%{__python3} setup.py test
%endif


%if 0%{?with_python2}
%files -n python2-%{srcname}
%license LICENSE
%doc CONTRIBUTING.md README.rst SUPPORT.md
%{!?el7:%doc build/sphinx/html/}
%{python2_sitelib}/*
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc CONTRIBUTING.md README.rst SUPPORT.md
%{!?el7:%doc build/sphinx/html/}
%{python3_sitelib}/*
%endif


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.3.15-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.15-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Xavier Bachelot <xavier@bachelot.org> - 1.3.15-2
- Symplify py2 deps
- Dont BR: missing py3 modules on EL7
- Drop EL6 support
- Dont build doc for EL7
- Enable py3 for EL7

* Thu Aug 20 2020 Xavier Bachelot <xavier@bachelot.org> - 1.3.15-1
- Update to 1.3.15

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.13-7
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Xavier Bachelot <xavier@bachelot.org> - 1.3.13-6
- Drop dependency on pep8.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.13-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.13-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 19 2019 Xavier Bachelot <xavier@bachelot.org> - 1.3.13-1
- Update to 1.3.13.
- Prepare for python3 build in EPEL.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Xavier Bachelot <xavier@bachelot.org> - 1.3.11-1
- Update to 1.3.11.
- Don't build python2 sub-package for Fedora 30+ and EL8 (RHBZ#1635602).

* Thu Jul 26 2018 Xavier Bachelot <xavier@bachelot.org> - 1.3.10-1
- Update to 1.3.10.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Xavier Bachelot <xavier@bachelot.org> - 1.3.9-3
- Add missing Requires:.

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.9-2
- Rebuilt for Python 3.7

* Fri Jun 29 2018 Xavier Bachelot <xavier@bachelot.org> - 1.3.9-1
- Update to 1.3.9.

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.6-5
- Rebuilt for Python 3.7

* Mon May 07 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.6-4
- Remove unused tox dependency

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.6-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 21 2018 Xavier Bachelot <xavier@bachelot.org> - 1.3.6-2
- Fix doc.
- Tidy up BR:s for EL6 and EL7.

* Wed Feb 21 2018 Xavier Bachelot <xavier@bachelot.org> - 1.3.6-1
- Update to 1.3.6.

* Mon Dec 18 2017 Xavier Bachelot <xavier@bachelot.org> - 1.3.4-2
- Use tarball from github rather than pypy.
- Fix typo in BuildRequires.
- Add BR: for building docs and running tests.

* Wed Dec 13 2017 Xavier Bachelot <xavier@bachelot.org> - 1.3.4-1
- Initial package.
