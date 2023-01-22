%global commit 6e85b564d7d59ecdffc1d2e9e6b595952ffde75b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global realname rosinstall
Name:           python-rosinstall
Version:        0.7.8
Release:        17%{?dist}
Summary:        ROS installation utilities

License:        BSD
URL:            http://www.ros.org/wiki/rosinstall
BuildArch:      noarch
Source0:        https://github.com/vcstools/%{realname}/archive/%{commit}/%{realname}-%{commit}.tar.gz

BuildRequires: make
BuildRequires:  zsh

BuildRequires:  python3-devel
BuildRequires:  python3-mock
BuildRequires:  python3-rosdistro >= 0.3.0
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-vcstools >= 0.1.38
BuildRequires:  python3-wstool >= 0.1.12

%global _description\
rosinstall is a tool to check out ROS source code (or any source code, really)\
from multiple version control repositories and updating these checkouts. Given\
a *.rosinstall file that specifies where to get code, rosinstall will check\
out a working copy for you.

%description %_description

%package -n python3-%{realname}
Summary:        %{summary}
Requires:       python3-vcstools >= 0.1.37
Requires:       python3-PyYAML
Requires:       python3-rosdistro >= 0.3.0
Requires:       python3-catkin_pkg
Requires:       python3-wstool >= 0.1.8
Conflicts:      python2-%{realname} < 0.7.8-5

%description -n python3-%{realname} %_description

%prep
%setup -qn %{realname}-%{commit}
%if 0%{?rhel}
sed -i 's/haiku/default/' doc/conf.py
sed -i 's/:special-members://g' doc/*.rst
%endif

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
pushd doc
make html
make man
rm -rf _build/html/.buildinfo
popd

%py3_build

%install
%py3_install

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 0644 doc/_build/man/%{realname}.1 $RPM_BUILD_ROOT%{_mandir}/man1/


%check
# python-rosinstall tests reach out to github, which won't work in mock.
# Disabling for now
#nosetests

%files -n python3-%{realname}
%license LICENSE
%{_bindir}/*
%{_mandir}/man1/%{realname}.1.*
%{python3_sitelib}/%{realname}
%{python3_sitelib}/%{realname}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.8-13
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.8-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.8-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.8-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.8-5
- Subpackage python2-rosinstall has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.8-2
- Rebuilt for Python 3.7

* Sun May 27 2018 Rich Mattes <richmattes@gmail.com> - 0.7.8-1
- Update to release 0.7.8

* Mon Mar 19 2018 Jan Beran <jberan@redhat.com> - 0.7.7-11
- Fix of missing Python 3 executables (rhbz 1432565)

* Wed Feb 28 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.7-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.7-8
- Python 2 binary package renamed to python2-rosinstall
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.7-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Oct 20 2015 Rich Mattes <richmattes@gmail.com> - 0.7.7-1
- Update to release 0.7.7

* Fri Sep 18 2015 Rich Mattes <richmattes@gmail.com> - 0.7.6-2
- Fix python 3 requires versioning

* Wed Sep 16 2015 Rich Mattes <richmattes@gmail.com> - 0.7.6-1
- Update to release 0.7.6

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Rich Mattes <richmattes@gmail.com> - 0.7.5-2
- Make sure scripts in bindir use python2 instead of python3

* Wed Mar 04 2015 Rich Mattes <richmattes@gmail.com> - 0.7.5-1
- Update to release 0.7.5 (rhbz#1195536)
- Add python3 package

* Tue Dec 30 2014 Rich Mattes <richmattes@gmail.com> - 0.7.4-1
- Update to release 0.7.4

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.7.3-3
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb 08 2014 Rich Mattes <richmattes@gmail.com> - 0.7.3-1
- Update to release 0.7.3

* Mon Aug 19 2013 Rich Mattes <richmattes@gmail.com> - 0.6.29-1
- Update to release 0.6.29

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.28-2.20130601git980042b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 01 2013 Rich Mattes <richmattes@gmail.com> - 0.6.28-1.20130601git980042b0
- Update to release 0.6.28
- Fix github source url

* Mon Mar 18 2013 Rich Mattes <richmattes@gmail.com> - 0.6.26-1.20130318git6d482b2
- Update to release 0.6.26

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 02 2013 Rich Mattes <richmattes@gmail.com> - 0.6.22-1
- Update to release 0.6.22

* Fri Oct 26 2012 Rich Mattes <richmattes@gmail.com> - 0.6.20-1
- Update to release 0.6.20

* Mon Oct 08 2012 Rich Mattes <richmattes@gmail.com> - 0.6.19-2
- Separated build and install steps for setup.py
- Added README and LICENSE

* Sun Sep 02 2012 Rich Mattes <richmattes@gmail.com> - 0.6.19-1
- Update to release 0.6.19

* Wed Jun 06 2012 Rich Mattes <richmattes@gmail.com> - 0.6.17-1
- Update to release 0.6.17

* Wed Apr 25 2012 Rich Mattes <richmattes@gmail.com> - 0.6.15-1
- Initial package
