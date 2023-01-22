# Enable Python 3 builds for Fedora, EPEL > 7 (resultsdb_api is not built for EPEL 7)
%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_without      python3
%else
%bcond_with         python3
%endif

# Disable Python 2 builds for Fedora > 29, EPEL > 7
%if 0%{?fedora} > 29 || 0%{?rhel} > 7
%bcond_with         python2
%global obsolete2   1
%else
%bcond_without      python2
%global obsolete2   0
%endif

%global sum     Library defining conventions for ResultsDB results
%global desc    This project defines some agreed conventions for reporting results of \
different types to ResultsDB, and provides code (currently a Python library) \
to help with reporting results that conform to the conventions.

%global pagure_namespace    taskotron
%global pagure_name         resultsdb_conventions
%global pagure_version      2.1.0

Name:           resultsdb_conventions
Version:        %{pagure_version}
Release:        9%{?dist}
Summary:        %{sum}

License:        GPLv3+
URL:            https://pagure.io/%{pagure_namespace}/%{pagure_name}
Source0:        https://files.pythonhosted.org/packages/source/r/%{pagure_name}/%{pagure_name}-%{pagure_version}.tar.gz
BuildArch:      noarch

%description
%{desc}

%if 0%{?with_python2}
%package -n python2-resultsdb_conventions
Summary:        %{sum}
%{?python_provide:%python_provide python2-resultsdb_conventions}
Requires:       python2-cached_property
Requires:       python2-productmd
Requires:       python2-resultsdb_api

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
# For tests
BuildRequires:  python2-mock
BuildRequires:  python2-pytest
BuildRequires:  python2-cached_property
BuildRequires:  python2-fedfind
BuildRequires:  python2-productmd
BuildRequires:  python2-resultsdb_api

%description -n python2-resultsdb_conventions
%{desc} This is the
Python 2 build.

%package -n python2-resultsdb_conventions-fedora
Summary:        %{sum} (Fedora module)
%{?python_provide:%python_provide python2-resultsdb_conventions-fedora}
Requires:       python2-resultsdb_conventions = %{version}-%{release}
Requires:       python2-fedfind

%description -n python2-resultsdb_conventions-fedora
%{desc} This subpackage
contains the resultsdb_conventions.fedora module, which has additional
dependencies. This is the Python 2 build.
%endif # with_python2

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-resultsdb_conventions
Summary:        %{sum}
%if 0%{?fedora}
%{?python_provide:%python_provide python%{python3_pkgversion}-resultsdb_conventions}
%endif
%if 0%{?obsolete2}
Obsoletes:      python2-resultsdb_conventions < %{version}-%{release}
%endif # obsolete2
Requires:       python%{python3_pkgversion}-cached_property
Requires:       python%{python3_pkgversion}-productmd
Requires:       python%{python3_pkgversion}-resultsdb_api

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
# For tests
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-cached_property
BuildRequires:  python%{python3_pkgversion}-fedfind
BuildRequires:  python%{python3_pkgversion}-productmd
BuildRequires:  python%{python3_pkgversion}-resultsdb_api

%description -n python%{python3_pkgversion}-resultsdb_conventions
%{desc} This is the
Python 3 build.

%package -n python%{python3_pkgversion}-resultsdb_conventions-fedora
Summary:        %{sum} (Fedora module)
%if 0%{?fedora}
%{?python_provide:%python_provide python%{python3_pkgversion}-resultsdb_conventions-fedora}
%endif
%if 0%{?obsolete2}
Obsoletes:      python2-resultsdb_conventions-fedora < %{version}-%{release}
%endif # obsolete2
Requires:       python%{python3_pkgversion}-resultsdb_conventions = %{version}-%{release}
Requires:       python%{python3_pkgversion}-fedfind

%description -n python%{python3_pkgversion}-resultsdb_conventions-fedora
%{desc} This subpackage
contains the resultsdb_conventions.fedora module, which has additional
dependencies. This is the Python 3 build.
%endif # with_python3

%prep
%autosetup -p1
# this is needed for doing sdist, but not for anything else
sed -i -e '/setuptools_git/d' setup.py

%build
%if 0%{?with_python2}
%py2_build
%endif # with_python2
%if 0%{?with_python3}
%py3_build
%endif # with_python3

%install
%if 0%{?with_python2}
%py2_install
%endif # with_python2
%if 0%{?with_python3}
%py3_install
%endif # with_python3

%check
%if 0%{?with_python2}
%{__python2} setup.py test
%endif # with_python2
%if 0%{?with_python3}
%{__python3} setup.py test
%endif # with_python3

%if 0%{?with_python2}
%files -n python2-resultsdb_conventions
%doc README.md CHANGELOG.md
%license COPYING
%{python2_sitelib}/resultsdb_conventions*
%exclude %{python2_sitelib}/resultsdb_conventions/fedora.py*

%files -n python2-resultsdb_conventions-fedora
%{python2_sitelib}/resultsdb_conventions/fedora.py*
%endif # with_python2

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-resultsdb_conventions
%doc README.md CHANGELOG.md
%license COPYING
%{python3_sitelib}/resultsdb_conventions*
%exclude %{python3_sitelib}/resultsdb_conventions/fedora.py
%pycached %exclude %{python3_sitelib}/resultsdb_conventions/fedora.py
%exclude %{python3_sitelib}/resultsdb_conventions/fedoracoreos.py
%pycached %exclude %{python3_sitelib}/resultsdb_conventions/fedoracoreos.py

%files -n python%{python3_pkgversion}-resultsdb_conventions-fedora
%{python3_sitelib}/resultsdb_conventions/fedora.py
%pycached %{python3_sitelib}/resultsdb_conventions/fedora.py
%{python3_sitelib}/resultsdb_conventions/fedoracoreos.py
%pycached %{python3_sitelib}/resultsdb_conventions/fedoracoreos.py

%endif # with_python3

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.0-7
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.0-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 28 2020 Adam Williamson <awilliam@redhat.com> - 2.1.0-2
- Move fedora cache file into fedora subpackage
- Move fedoracores files into fedora subpackage

* Thu Aug 27 2020 Adam Williamson <awilliam@redhat.com> - 2.1.0-1
- New release 2.1.0 (adds Fedora CoreOS conventions)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.3-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Adam Williamson <awilliam@redhat.com> - 2.0.3-7
- Also obsolete Python 2 -fedora subpackage on F30+

* Thu Nov 22 2018 Adam Williamson <awilliam@redhat.com> - 2.0.3-6
- Disable Python 2 build on F30+, EL8+

* Fri Nov 09 2018 Frantisek Zatloukal <fzatlouk@redhat.com> - 2.0.3-5
- Let's build also python3 packages

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.0.3-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Adam Williamson <awilliam@redhat.com> - 2.0.3-1
- New release 2.0.3: minor tweak for fedfind 4.x

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 24 2017 Adam Williamson <awilliam@redhat.com> - 2.0.2-1
- 2.0.2: new FedoraBodhiResult convention for Bodhi update tests

* Wed Feb 15 2017 Adam Williamson <awilliam@redhat.com> - 2.0.1-1
- Initial package
