%global srcname doit

Name:           python-%{srcname}
Version:        0.36.0
Release:        4%{?dist}
Summary:        Automation Tool

License:        MIT
URL:            https://pydoit.org/
Source0:        https://pypi.io/packages/source/d/%{srcname}/%{srcname}-%{version}.tar.gz
Patch1:         python-doit_ignore_versions.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  strace
BuildRequires:  python3-devel

%global _description %{expand:
python-doit is a build tool (in the same class as make, cmake, scons,
ant and others)

python-doit can be used as:
  * a build tool (generic and flexible)
  * home of your management scripts (it helps you organize and combine
   shell scripts and python scripts)
  * a functional tests runner (combine together different tools)
  * a configuration management system
  * manage computational pipelines}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_enable_dependency_generator}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%package -n python3-%{srcname}-doc
Summary:        Documentation for %{name}
Requires:       python3-%{srcname} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{srcname}-doc}

%description -n python3-%{srcname}-doc
%{name} documentation

%prep
%autosetup -p1 -n %{srcname}-%{version}

find -type f -exec sed -i '1s=^#! /usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

%generate_buildrequires
%pyproject_buildrequires dev_requirements.txt doc_requirements.txt -r

%build
%pyproject_wheel

cd doc
PYTHONPATH=.. make html SPHINXBUILD=sphinx-build-3
rm -rf _build/html/_sources/ _build/html/.buildinfo
cd -

%install
%pyproject_install

install -p -D -m 0644 bash_completion_doit %{buildroot}%{_sysconfdir}/bash_completion.d/doit
%pyproject_save_files %{srcname}

%check
# Is impossible to run tests because the testsuite is not ready for Python 3
# environment and there is also one unresolved test dependency doit-py
# %{__python3} -m pytest
%py3_check_import %{srcname}

%files -n python3-%{srcname} -f %{pyproject_files}
%{_bindir}/doit
%license LICENSE
%doc README.rst
%{_sysconfdir}/bash_completion.d/doit

%files -n python3-%{srcname}-doc
%license LICENSE
# doc is not present in the tar ball (reported upstream)
#%doc doc/tutorial
%doc doc/_build/html
%doc CHANGES
%doc TODO.txt

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.36.0-2
- Rebuilt for Python 3.13

* Thu Feb  1 2024 José Matos <jamatos@fedoraproject.org> - 0.36.0-1
- Update to 0.36.0
- Update the spec file to more modern Python guidelines

* Thu Feb  1 2024 Maxwell G <maxwell@gtmx.me> - 0.33.1-13
- Remove unused python3-mock test dependency

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 0.33.1-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 0.33.1-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.33.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.33.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep  4 2020 José Matos <jamatos@fedoraproject.org> - 0.33.1-1
- Update to 0.33.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.32.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.32.0-2
- Rebuilt for Python 3.9

* Thu Mar 19 2020 José Matos <jamatos@fedoraproject.org> - 0.32.0-1
- Update to 0.32.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.31.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.31.1-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 15 2019 José Matos <jamatos@fedoraproject.org> - 0.31.1-4
- explictly require python3-setuptools at runtime (see #1695045)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 27 2018 José Matos <jamatos@fedoraproject.org> - 0.31.1-2
- use automated dependency generator.

* Mon Aug 27 2018 José Matos <jamatos@fedoraproject.org> - 0.31.1-1
- update to 0.31.1
- remove bundled egg-info
- identify the license

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.30.3-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Miro Hrončok <mhroncok@redhat.com> - 0.30.3-2
- Fix packaging errors by the previous commit (#1530265)
- The doc package now requires python3-doit, not python-doit
- Add proper obsoletes
- Make the docs actually build by setting SPHINXBUILD
- Add python_provide to the doc subpackage

* Thu Aug 24 2017 Jan Beran <jberan@redhat.com> - 0.30.3-1
- New version (Python 3 only)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.28.0-9
- Python 2 binary package renamed to python2-doit
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.28.0-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28.0-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Aug 26 2015 Pete Travis <immanetize@fedoraproject.org> - 0.28.0-2
- add requires for python-configparser

* Thu Jul  2 2015 José Matos <jamatos@fedoraproject.org> - 0.28.0-1
- update to 0.28

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Sep 24 2014 José Matos <jamatos@fedoraproject.org> - 0.26.0-1
- update to 0.26
- don't own /etc/bash_completion.d/

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.25.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Mar 27 2014 José Matos <jamatos@fedoraproject.org> - 0.25.0-1
- update to 0.25

* Fri Nov 29 2013 José Matos <jamatos@fedoraproject.org> - 0.24.0-1
- update to 0.24

* Thu Nov  7 2013 José Matos <jamatos@fedoraproject.org> - 0.23.0-1
- update to 0.23
- patch that removed distribute bootstrapping during installation is
  gone since this change was incorporated upstream

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 13 2013 José Matos <jamatos@fedoraproject.org> - 0.22.0-1
- update to 0.22
- force removal of the distrute_setup.py to use the system version

* Mon Jun  3 2013 José Matos <jamatos@fedoraproject.org> - 0.21.0-2
- Add license and readme to python3 versions since the package can be
  installed separately

* Fri May  3 2013 José Matos <jamatos@fedoraproject.org> - 0.21.0-1
- update to 0.21.0

* Mon Apr 22 2013 José Matos <jamatos@fedoraproject.org> - 0.20.0-1
- New stable release

* Mon Dec  3 2012 José Matos <jamatos@fedoraproject.org> - 0.18.1-1
- New stable release

* Mon Dec  3 2012 José Matos <jamatos@fedoraproject.org> - 0.18.0-5
- remove python3 doit to allow for the python2 doit so stay in bin

* Sun Dec  2 2012 José Matos <jamatos@fedoraproject.org> - 0.18.0-4
- Remove updated version of distribute_setup

* Sun Dec  2 2012 José Matos <jamatos@fedoraproject.org> - 0.18.0-3
- Require python3-setuptools for the package building

* Sun Dec  2 2012 José Matos <jamatos@fedoraproject.org> - 0.18.0-2
- Add python3 subpackage

* Fri Nov 30 2012 José Matos <jamatos@fedoraproject.org> - 0.18.0-1
- Latest stable release
