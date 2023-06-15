%global modname moksha.common

Name:           python-moksha-common
Version:        1.2.5
Release:        24%{?dist}
Summary:        Common components for Moksha

License:        ASL 2.0 or MIT
URL:            https://pypi.io/project/moksha.common
Source0:        https://pypi.io/packages/source/m/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch


BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-mock

BuildRequires:  python3-decorator
BuildRequires:  python3-kitchen
BuildRequires:  python3-pytz
BuildRequires:  python3-six

# Its a whole different package now

%global _description\
Common components for Moksha.

%description %_description

%package -n python3-moksha-common
Summary:        Common components for Moksha

Requires:       python3-decorator
Requires:       python3-kitchen
Requires:       python3-pytz
Requires:       python3-six
# /usr/bin/moksha was moved from there:
Conflicts:      python2-moksha-common < 1.2.5-9
%{?python_provide:%python_provide python3-moksha-common}

%description -n python3-moksha-common
Common components for Moksha.

%prep
%setup -q -n %{modname}-%{version}


%build
%py3_build

%install
%py3_install

# Add __init__.py files to namespace packages not installed by setuptools
cp moksha/__init__.py %{buildroot}/%{python3_sitelib}/moksha/

%check
%{__python3} setup.py test

%files -n python3-moksha-common
%doc README COPYING AUTHORS
%{python3_sitelib}/moksha/
%{python3_sitelib}/%{modname}-%{version}*
# The CLI tool.  :)
%{_bindir}/moksha


%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.5-24
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.5-21
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.5-18
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.5-15
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 04 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.5-13
- Subpackage python2-moksha-common has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.5-12
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.5-9
- Move /usr/bin/moksha to python3-moksha-common

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.5-7
- Rebuilt for Python 3.7

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.5-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.5-4
- Python 2 binary package renamed to python2-moksha-common
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Lumír Balhar <lbalhar@redhat.com> - 1.2.5-2
- Fixed namespace package related issue caused by missing init files

* Tue Jul 11 2017 Ralph Bean <rbean@redhat.com> - 1.2.5-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.4-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 25 2015 Ralph Bean <rbean@redhat.com> - 1.2.4-1
- Enable python3 subpackage.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Ralph Bean <rbean@redhat.com> - 1.2.3-1
- Support older versions of python-six.

* Thu Apr 24 2014 Ralph Bean <rbean@redhat.com> - 1.2.2-1
- Fixed up some python3 support.
- Added dep on python-six.

* Mon Oct 14 2013 Ralph Bean <rbean@redhat.com> - 1.2.1-1
- Latest upstream; simply includes a forgotten test config.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Ralph Bean <rbean@redhat.com> - 1.2.0-1
- Bumped to latest upstream.
- Included python3 subpackage but left it disabled by macro.
- Reenabled the test suite.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 10 2012 Ralph Bean <rbean@redhat.com> - 1.0.6-1
- Bumped to 1.0.6.
- Removed Requires on python-paste which has moved to python-moksha-wsgi.

* Wed Sep 19 2012 Ralph Bean <rbean@redhat.com> - 1.0.1-2
- Added Conflicts tag against old moksha.

* Wed Sep 12 2012 Ralph Bean <rbean@redhat.com> - 1.0.1-1
- Upstream bugfixes.

* Wed Sep 05 2012 Ralph Bean <rbean@redhat.com> - 1.0.0-4
- Use optflags instead of RPM_OPT_FLAGS to be consistent.

* Wed Sep 05 2012 Ralph Bean <rbean@redhat.com> - 1.0.0-3
- Relicensed to ASL 2.0 or MIT for the one included MIT file.
- Added RPM_OPT_FLAGS to build section.

* Wed Sep 05 2012 Ralph Bean <rbean@redhat.com> - 1.0.0-2
- Disabled tests since they're behaving strangely in koji.

* Tue Sep 04 2012 Ralph Bean <rbean@redhat.com> - 1.0.0-1
- Initial package for Fedora.  Split from old moksha core.
