%global pname pympler

%global desc \
Pympler is a development tool to measure, monitor and analyze the memory\
behavior of Python objects in a running Python application.\
\
By pympling a Python application, detailed insight in the size and the lifetime\
of Python objects can be obtained. Undesirable or unexpected runtime behavior\
like memory bloat and other “pymples” can easily be identified.\
\
Pympler integrates three previously separate modules into a single,\
comprehensive profiling tool. The asizeof module provides basic size information\
for one or several Python objects, module muppy is used for on-line monitoring\
of a Python application and module Class Tracker provides off-line analysis of\
the lifetime of selected Python objects.

Name: python-Pympler
Version: 1.1
Release: 3%{?dist}
Summary: Measure, monitor and analyze the memory behavior of Python objects
License: Apache-2.0 and BSD-3-Clause and MIT
# bundled stuff
# pympler/asizeof.py: BSD
# pympler/static/jquery.sparkline.min.js: BSD
# pympler/templates/jquery.flot*.min.js: MIT
URL: http://pythonhosted.org/Pympler/
Source0: https://pypi.python.org/packages/source/P/Pympler/%{pname}-%{version}.tar.gz
Patch0: python-Pympler-no-shebang.patch
BuildArch: noarch

%description
%{desc}

%package -n python3-Pympler
Summary: %{summary}
BuildRequires: python3-bottle
BuildRequires: python3-devel
BuildRequires: python3-matplotlib
BuildRequires: python3-setuptools
BuildRequires: python3-pip
BuildRequires: python3-wheel
Requires: python3-bottle
# http://www.flotcharts.org
Provides: bundled(js-jquery-flot) = 0.8.3
# https://github.com/krzysu/flot.tooltip
Provides: bundled(js-jquery-flot-tooltip) = 0.8.4
# http://omnipotent.net/jquery.sparkline/
Provides: bundled(js-jquery-sparkline) = 2.1.1
# asizeof.py is bundled
Provides: bundled(python%{python3_version}dist(asizeof))
# required by pympler/charts.py, but doesn't throw an exception without
Recommends: python3-matplotlib
# pympler/panels.py is an extension for django-debug-toolbar
Enhances: python3-django-debug-toolbar

%description -n python3-Pympler
%{desc}

%prep
%setup -q -n %{pname}-%{version}
rm pympler/util/bottle.py
chmod -x pympler/asizeof.py
%patch -P 0 -p1 -b .no-shebang


%build
%pyproject_wheel

%install
%pyproject_install

# Disabled due to 3.13 failure: https://github.com/pympler/pympler/issues/163
#%%check
#PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} setup.py test

%files -n python3-Pympler
%license LICENSE
%doc NOTICE README.md
%{python3_sitelib}/Pympler-%{version}.dist-info/
%{python3_sitelib}/pympler

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 05 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.1-1
- 1.1

* Sun Jun 16 2024 Python Maint <python-maint@redhat.com> - 1.0.1-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Gwyn Ciesla <gwync@protonmail.com> - 1.0.1-9
- Fix patch macros, update python macros, SPDX license tags.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 1.0.1-7
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 15 2022 Dominik Mierzejewski <dominik@greysector.net> 1.0.1-5
- work around issues with Python 3.11 (rhbz#2113612)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.0.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 16 2022 Dominik Mierzejewski <rpm@greysector.net> 1.0.1-1
- update to 1.0.1 (#2033793)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Oct 25 2020 Dominik Mierzejewski <rpm@greysector.net> 0.9-1
- update to 0.9 (#1888434)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8-4
- Rebuilt for Python 3.9

* Sat May 02 2020 Dominik Mierzejewski <rpm@greysector.net> 0.8-3
- fix build with Python 3.9 (#1791963)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 02 2019 Dominik Mierzejewski <rpm@greysector.net> 0.8-1
- update to 0.8 (#1771742)
- re-bundle flot (nodejs-flot was retired)
- re-enable failing test (fixed upstream)

* Thu Sep 12 2019 Dominik Mierzejewski <rpm@greysector.net> 0.7-1
- update to 0.7 (#1696870)
- disable one test failing with Python 3.8
  (https://github.com/pympler/pympler/issues/102)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 26 2019 Dominik Mierzejewski <rpm@greysector.net> 0.6-1
- update to 0.6
- mark asizeof.py as bundled (#1649274)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5-3
- Subpackage python2-Pympler has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Dominik Mierzejewski <rpm@greysector.net> 0.5-1
- update to 0.5
- drop obsolete patches
- use pythonX_version macros in files list

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.3-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jun 10 2016 Dominik Mierzejewski <rpm@greysector.net> 0.4.3-2
- drop CC-BY-SA-NC from license list and fix typo
- actually unbundle nodejs-flot
- add a weak dep for python{2,3}-django-debug-toolbar
- drop python shebang from asizeof.py

* Mon May 16 2016 Dominik Mierzejewski <rpm@greysector.net> 0.4.3-1
- update to 0.4.3
- build for python3 as well
- unbundle python-bottle

* Sun Aug 09 2015 Dominik Mierzejewski <rpm@greysector.net> 0.4.2-1
- initial build
