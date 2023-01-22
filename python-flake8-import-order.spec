%global srcname flake8-import-order
%bcond_with pylama

Name:           python-%{srcname}
Version:        0.18.1
Release:        6%{?dist}
Summary:        Flake8 plugin for checking order of imports in Python code

License:        LGPLv3
URL:            https://github.com/PyCQA/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/f/%{srcname}/%{srcname}-%{version}.tar.gz
Patch0:         flake8-import-order-0.9.2-nolama.patch

BuildArch:      noarch

%description
%{summary}.

%package     -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-flake8
BuildRequires:  python%{python3_pkgversion}-pycodestyle
BuildRequires:  python%{python3_pkgversion}-asttokens
Requires:       python%{python3_pkgversion}-flake8
Requires:       python%{python3_pkgversion}-pycodestyle
Requires:       python%{python3_pkgversion}-asttokens
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
%{summary}.


%prep
%setup -q -n %{srcname}-%{version}
%if ! %{with pylama}
%patch0 -p1
rm tests/test_pylama_linter.py
%endif


%build
%py3_build


%install
%py3_install


%check
%if ! %{with pylama}
mv flake8_import_order/pylama_linter.py flake8_import_order/pylama_linter.NOT
%endif

%{__python3} setup.py develop --user
%{__python3} -m pytest -v


%files -n python%{python3_pkgversion}-%{srcname}
%license COPYING
%doc README.rst
%{python3_sitelib}/*


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.18.1-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.1-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.18.1-1
- Update to latest version (#1685087)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.18-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.18-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.18-3
- Subpackage python2-flake8-import-order has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul  9 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.18-1
- Update to 0.18 (#1599108)

* Thu Jul 05 2018 Miro Hrončok <mhroncok@redhat.com> - 0.17.1-2
- Rebuilt for Python 3.7

* Mon Mar 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.17.1-1
- Update to 0.17.1 (#1544280)
- Conditionalize the Python 2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.15-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Nov  9 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.15-1
- Update to 0.15 (#1508184)

* Mon Nov  6 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.14.3-1
- Update to 0.14.2 (#1508184)

* Sun Jul 30 2017 Ville Skyttä <ville.skytta@iki.fi> - 0.13-1
- Update to 0.13

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri May 26 2017 Ville Skyttä <ville.skytta@iki.fi> - 0.12-2
- Run tests with -Wall

* Tue Feb 14 2017 Ville Skyttä <ville.skytta@iki.fi> - 0.12-1
- Update to 0.12

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.11-2
- Rebuild for Python 3.6

* Fri Nov 11 2016 Ville Skyttä <ville.skytta@iki.fi> - 0.11-1
- Update to 0.11

* Mon Oct 24 2016 Orion Poplawski <orion@cora.nwra.com> - 0.9.2-2
- Use %%license
- Minor spec cleanup

* Sun Sep 18 2016 Ville Skyttä <ville.skytta@iki.fi> - 0.9.2-1
- Update to 0.9.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 30 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.6.1-1
- First build
