%global modname tw2.core

Name:           python-tw2-core
Version:        2.3.0
Release:        18%{?dist}
Summary:        Web widget creation toolkit based on TurboGears widgets

License:        MIT
URL:            http://toscawidgets.org
Source0:        https://pypi.python.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz

# remove kajiki support because of broken dependencies on Fedora
#Patch1:         python-tw2-core-without-kajiki.patch

BuildArch:      noarch

# For building, generally
# General
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-webob >= 0.9.7
BuildRequires:  python3-simplejson >= 2.0
BuildRequires:  python3-decorator
BuildRequires:  python3-markupsafe
BuildRequires:  python3-speaklater
BuildRequires:  python3-paste-deploy
BuildRequires:  python3-six

# Specifically for the test suite
#BuildRequires:  python3-nose
BuildRequires:  python3-coverage
BuildRequires:  python3-formencode
BuildRequires:  python3-webtest
BuildRequires:  python3-sieve

# Templating languages for the test suite
BuildRequires:  python3-mako
BuildRequires:  python3-genshi
BuildRequires:  python3-chameleon
BuildRequires:  python3-kajiki
BuildRequires:  python3-jinja2

%description

ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the web.

The tw2.core package is lightweight and intended for run-time use only;
development tools are in tw2.devtools.


%package -n python3-tw2-core
Summary: Web widget creation toolkit based on TurboGears widgets
Requires: python3-webob >= 0.9.7
Requires: python3-simplejson >= 2.0
Requires: python3-decorator
Requires: python3-markupsafe
Requires: python3-speaklater
Requires: python3-paste-deploy
Requires: python3-six

%{?python_provide:%python_provide python3-tw2-core}

%description -n python3-tw2-core
ToscaWidgets is a web widget toolkit for Python to aid in the creation,
packaging and distribution of common view elements normally used in the web.

The tw2.core package is lightweight and intended for run-time use only;
development tools are in tw2.devtools.

This package contains the python3 version of the toolkit

%prep
%autosetup -n %{modname}-%{version}

%build
# Fix shebang for python3
sed -i '1s=^#!/usr/bin/\(python\|env python\)[0-9.]*=#!%{__python3}=' tw2/core/testbase/xhtmlify.py
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build \
    --install-data=%{_datadir} --root=%{buildroot}

%files -n python3-tw2-core
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/tw2
%{python3_sitelib}/%{modname}-%{version}*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.3.0-16
- Rebuild for python 3.13

* Sat Jun 15 2024 Python Maint <python-maint@redhat.com> - 2.3.0-15
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 2.3.0-11
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Python Maint <python-maint@redhat.com> - 2.3.0-8
- Rebuilt for Python 3.11

* Thu Apr 21 2022 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.3.0-7
- Removed python-nose and check section according to deprecation of nose

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Python Maint <python-maint@redhat.com> - 2.3.0-4
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.3.0-1
- Update to upstream

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.9-2
- Rebuilt for Python 3.9

* Wed Mar 25 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.2.9-1
- Update to upstream
- Enable kajiki support again

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.2.7-1
- Update to upstream
- Removed py3.8 patch, not needed anymore.

* Thu Oct 03 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.2.6-6
- Removed unittest2 dependency. Not used anymore.
- Removed kajiki support because kajiki has broken dependencies
  in Fedora (python-nine).

* Mon Sep 02 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.2.6-5
- Removed python3-nine as dependency. Not used anymore.

* Thu Aug 29 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.2.6-4
- Removed python3 support

* Thu Aug 29 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.2.6-3
- Updated source URL to https

* Wed Aug 28 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.2.6-2
- Python 3.8 compatibility patch
- Removed extra tokens at end of endif

* Mon Aug 26 2019 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 2.2.6-1
- Update to upstream
- Removed mako-unicode patch applied upstream

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.2.3-12
- Rebuilt for Python 3.7

* Thu Mar 15 2018 Jan Beran <jberan@redhat.com> - 2.2.3-11
- Fix of python3-tw2-core requires both Python 2 and Python 3 (rhbz #1546817)

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.2.3-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.3-9
- Escape macros in %%changelog

* Tue Oct 17 2017 Petr Viktorin <pviktori@redhat.com> - 2.2.3-8
- Python 2 binary package renamed to python2-tw2-core

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.2.3-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan  6 2016 Toshio Kuratomi <toshio@fedoraproject.org> - 2.2.3-2
- Python3 subpackage

* Fri Dec 11 2015 Ralph Bean <rbean@redhat.com> - 2.2.3-1
- new version

* Fri Oct 16 2015 Ralph Bean <rbean@redhat.com> - 2.2.2-3
- Apply patch from upstream to fix unicode issues with mako.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 20 2015 Ralph Bean <rbean@redhat.com> - 2.2.2-1
- new version

* Fri Feb 20 2015 Ralph Bean <rbean@redhat.com> - 2.2.2-1
- new version
- Further fix rhel6 conditionals.

* Thu Nov 13 2014 Ralph Bean <rbean@redhat.com> - 2.2.1.1-5
- Spec bump to deal with ridiculous epel7 merge.  ;(

* Wed Nov 12 2014 Ralph Bean <rbean@redhat.com> - 2.2.1.1-3
- Update rhel6 conditionals.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 28 2014 Ralph Bean <rbean@redhat.com> - 2.2.1.1-1
- Latest upstream.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 28 2013 Ralph Bean <rbean@redhat.com> - 2.1.5-3
- Patch for python-markupsafe usage on el6.

* Thu Feb 28 2013 Ralph Bean <rbean@redhat.com> - 2.1.5-2
- Added requirement on python-markupsafe.
- Added el6 conditional requirement on python-ordereddict.

* Fri Feb 22 2013 Ralph Bean <rbean@redhat.com> - 2.1.5-1
- Latest upstream

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 06 2012 Ralph Bean <rbean@redhat.com> - 2.0.5-4
- Test change for fedmsg hook.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 07 2012 Ralph Bean <rbean@redhat.com> - 2.0.5-2
- Correct directory ownership.

* Tue Apr 24 2012 Ralph Bean <rbean@redhat.com> - 2.0.5-1
- Packaged latest version of tw2.core which fixes streaming WSGI compliance.
- Removed defattr in the files section.
- Removed clean section.  Not supporting EPEL5.
- Removed references to buildroot.

* Mon Apr 16 2012 Ralph Bean <rbean@redhat.com> - 2.0.4-1
- Packaged latest version of tw2.core which fixes tests on py2.6.
- Added awk line to make sure pkg_resources picks up the right WebOb on el6
- Added dependency on python-unittest2

* Wed Apr 11 2012 Ralph Bean <rbean@redhat.com> - 2.0.3-1
- Packaged the latest release of tw2.core.
- Fixed rpmlint - python-bytecode-without-source
- Fixed rpmlint - non-executable-script

* Tue Apr 10 2012 Ralph Bean <rbean@redhat.com> - 2.0.2-1
- Packaged the latest release of tw2.core.
- Added the %%{?dist} macro to Release:

* Wed Apr 04 2012 Ralph Bean <rbean@redhat.com> - 2.0.1-1
- Update for latest tw2.core release.

* Thu Jun 16 2011 Luke Macken <lmacken@redhat.com> - 2.0-0.1.b4
- Initial package
