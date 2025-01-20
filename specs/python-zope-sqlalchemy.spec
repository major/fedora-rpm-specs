Name:           python-zope-sqlalchemy
Version:        3.1
Release:        7%{?dist}
BuildArch:      noarch

License:        ZPL-2.1
Summary:        Minimal Zope/SQLAlchemy transaction integration
URL:            https://github.com/zopefoundation/zope.sqlalchemy
Source0:        https://github.com/zopefoundation/zope.sqlalchemy/archive/%{version}.tar.gz

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-zope-testing


%global _description\
The aim of this package is to unify the plethora of existing packages\
integrating SQLAlchemy with Zope's transaction management. As such it seeks\
only to provide a data manager and makes no attempt to define a zopeish way to\
configure engines.

%description %_description

%package -n python3-zope-sqlalchemy
Summary:   Minimal Zope/SQLAlchemy transaction integration with Python 3 support

Requires:           python3-transaction
Requires:           python3-sqlalchemy >= 0.5.1
Requires:           python3-zope-interface >= 3.6.0

%description -n python3-zope-sqlalchemy
The aim of this package is to unify the plethora of existing packages
integrating SQLAlchemy with Zope's transaction management. As such it seeks
only to provide a data manager and makes no attempt to define a zopeish way to
configure engines.

%prep
%setup -q -n zope.sqlalchemy-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}


%files -n python3-zope-sqlalchemy
%doc src/zope/sqlalchemy/README.rst
%doc CHANGES.rst CREDITS.rst
%license COPYRIGHT.txt LICENSE.txt
# Co-own %%{python_sitelib}/zope/
%{python3_sitelib}/zope.sqlalchemy-*
%{python3_sitelib}/zope/sqlalchemy
%exclude %{python3_sitelib}/zope/sqlalchemy/*.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.1-5
- Rebuilt for Python 3.13

* Sun Apr 14 2024 Miroslav Suchý <msuchy@redhat.com> - 3.1-4
- convert license to SPDX

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 12 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 3.1-1
- Update to upstream.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.0-2
- Rebuilt for Python 3.12

* Mon Jun 05 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 3.0-1
- Update to upstream.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 18 2023 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.6-5
- Do not use glob on python sitelib

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.6-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 06 2021 Kevin Fenzi <kevin@scrye.com> - 1.6-1
- Update to 1.6. Fixes rhbz#2001435

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.5-1
- Update to upstream.

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4-2
- Rebuilt for Python 3.10

* Tue Apr 27 2021 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.4-1
- Update to upstream.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3-2
- Rebuilt for Python 3.9

* Fri Apr 17 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 1.3-1
- Update to upstream

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.7-13
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.7-12
- Subpackage python2-zope-sqlalchemy has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.7-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.7-7
- Rebuilt for Python 3.7

* Wed Jan 31 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.7-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.7-5
- Python 2 binary package renamed to python2-zope-sqlalchemy
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.7-2
- Rebuild for Python 3.6

* Mon Oct 10 2016 Randy Barlow <randy@electronsweatshop.com> - 0.7.7-1
- Update to 0.7.7 (#1204328).
- Use https and GitHub to retrieve the source instead of http and PyPI.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Sep 24 2015 Ralph Bean <rbean@redhat.com> - 0.7.6-1
- new version

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Aug 27 2014 Luke Macken <lmacken@redhat.com> - 0.7.5-1
- Update to 0.7.5 (#1111881)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun May 04 2014 Luke Macken <lmacken@redhat.com> - 0.7.4-1
- Update to 0.7.4 (#1012362)
- Require zope.interface >= 3.6.0

* Tue Aug 20 2013 Luke Macken <lmacken@redhat.com> - 0.7.2-3
- Move python3 requires statements into the python3 subpackage (#997674)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Luke Macken <lmacken@redhat.com> - 0.7.2-1
- Update to 0.7.2 (#760950)
- Build a python3 subpackage
- Modernize spec

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1 (#668182)

* Sun Sep 12 2010 Robin Lee <robinlee.sysu@gmail.com> - 0.6-1
- Update to 0.6
- More texts included
- Version of python-sqlalchemy requirement updated

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Feb 02 2010 Luke Macken <lmacken@redhat.com> - 0.4-3
- Specify the ZPL license version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 01 2009 Luke Macken <lmacken@redhat.com> - 0.4-1
- Update to 0.4

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.3-2
- Rebuild for Python 2.6

* Tue Oct 21 2008 Luke Macken <lmacken@redhat.com> - 0.3-1
- Initial package
