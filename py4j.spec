%if 0%{?rhel}
%global with_python2 1
%endif
%if 0%{?rhel} >= 7
%global with_python3 1
%endif
%if 0%{?fedora}
%global with_python3 1
%endif

%global encoding UTF-8
#%%global fail_fast 1

# build conditionals for debug performance
%bcond_without test_python
%if 0%{?fail_fast} == 0
%bcond_without test_java
%bcond_without javadoc
%bcond_without html
%endif

Name:           py4j
Version:        0.10.9
Release:        13%{?dist}
Summary:        Dynamically access in Python programs to arbitrary Java objects

License:        BSD
URL:            http://%{name}.sf.net
Source0:        https://github.com/bartdag/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-add-hamcrest-in-classpath.patch
Patch1:         %{name}-Base64-java8.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%if 0%{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-nose
%endif
%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-nose
%endif
%if 0%{?python3_other_pkgversion}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools
BuildRequires:  python%{python3_other_pkgversion}-nose
%endif

%if 0%{?rhel}
BuildRequires:  python2-sphinx
# FIXME use python2 prefix when update is available in repo
BuildRequires:  python-sphinx_rtd_theme
%endif
%if 0%{?fedora}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
%endif

BuildRequires:  ant-junit maven-local

# Fedora unbundles hamcrest from junit
%if 0%{?fedora}
BuildRequires:  hamcrest
%endif

Requires:       %{name}-java = %{version}-%{release}

%global _description \
Py4J enables Python programs running in a Python interpreter\
to dynamically access Java objects in a Java Virtual Machine.\
Methods are called as if the Java objects resided in the Python\
interpreter and Java collections can be accessed through standard\
Python collection methods.\
Py4J also enables Java programs to call back Python objects.\
Py4J is distributed under the BSD license.

%description
%_description

%if 0%{?with_python2}
%package -n python2-%{name}
Summary:        Py4J enables Python2 programs to dynamically access arbitrary Java objects
Requires:       %{name}-java = %{version}-%{release}
%{?python_provide:%python_provide python2-%{name}}
Obsoletes:      %{name} < 0.10.3-1

%description -n python2-%{name}
%_description
This package is for usage with Python2 only.
%endif

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{name}
Summary:        Py4J enables Python3 programs to dynamically access arbitrary Java objects
Requires:       %{name}-java = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}

%description -n python%{python3_pkgversion}-%{name}
%_description
This package is for usage with Python3 version %{python3_version} only.
%endif

%if 0%{?python3_other_pkgversion}
%package -n python%{python3_other_pkgversion}-%{name}
Summary:        Py4J enables Python3 programs to dynamically access arbitrary Java objects
Requires:       %{name}-java = %{version}-%{release}
%{?python_provide:%python_provide python%{python3_other_pkgversion}-%{name}}

%description -n python%{python3_other_pkgversion}-%{name}
%_description
This package is for usage with Python3 version %{python3_other_version} only.
%endif


%package java
Summary:        Py4J Java Library

%description java
%{summary}.


%if %{with javadoc}
%package javadoc
Summary:        Javadoc files for %{name}

%description javadoc
%{summary}.
%endif


%package doc
Summary:        Documentation files for %{name}

%description doc
%{summary}.


%prep
%setup -qn%{name}-%{version}

# remove unneeded stuff
rm -r setup.py
find . -name \*.jar -print -delete

# remove unnecessary dependency on parent POM
%pom_remove_parent %{name}-java/pom.xml

# build jar without version in name
sed -i -r "s|(version=).*|\1|" %{name}-java/ant.properties
sed -i "s|'.*'|''|" %{name}-python/src/%{name}/version.py

# set default java version to avoid some warnings
%if 0%{?fedora}
sed -i "s|1\.6|1.8|g" %{name}-java/build.xml
%else
# java 7 is default for EPEL
sed -i "s|1\.6|1.7|g" %{name}-java/build.xml
%endif

# enable encoding in javadoc
sed -i -r \
 's|<javadoc|\0 encoding="%{encoding}" charset="%{encoding}" docencoding="%{encoding}"|' \
 %{name}-java/build.xml

# unbundle junit (and hamcrest)
%if 0%{?fedora}
%patch0 -p0
%endif
sed -i "s|junit-.*\.jar|$(build-classpath junit)|g" %{name}-java/ant.properties
sed -i -r "s|(<javadoc.*classpath=)\"\"|\1\"$(build-classpath junit)\"|" %{name}-java/build.xml

# unbundle MiGBase64, https://fedorahosted.org/fpc/ticket/537
rm %{name}-java/src/main/java/%{name}/Base64.java
rm %{name}-java/src/test/java/%{name}/Base64Test.java
%patch1 -p1

%if %{with test_java}
# prevent wrong exception warnings
sed -i 's|FINEST|OFF|' %{name}-java/logging.properties
sed -i 's|<junit.*>|\0 <jvmarg value="-Djava.util.logging.config.file=%{name}-java/logging.properties" />|' \
 %{name}-java/build.xml
# remove duplicated summaries
sed -i 's|printsummary="on"||' %{name}-java/build.xml
%endif

%if %{with test_python}
sed -i "s|%{name}\.tests||" %{name}-python/setup.py
# prevent wrong exception warnings
sed -i "s|instance.gateway.shutdown()|if 'gateway' in dir(instance): \0|" \
 %{name}-python/src/%{name}/tests/java_gateway_test.py
# FIXME tls tends to hang, maybe background application too slow?
rm %{name}-python/src/py4j/tests/java_tls_test.py
%endif

# install jar later with maven
sed -i "/data_files/d" %{name}-python/setup.py

# build separately for python3 in special subfolder
%if 0%{?with_python3}
cp -a %{name}-python %{name}-python3
sed -i -r -e 's|(executable=")python|\1%{__python3}|g' \
 -e 's|(executable="nosetests)|\1-%{python3_pkgversion}|g' \
 -e 's|%{name}-python|%{name}-python3|g' \
 %{name}-java/build.xml
%endif


%build
pushd %{name}-java
ant jar
%if %{with javadoc}
ant javadoc
%endif
popd

%if 0%{?with_python2}
pushd %{name}-python
%py2_build
popd
%endif

%if 0%{?with_python3}
pushd %{name}-python3
%py3_build
%{?py3_other_build: %py3_other_build}
popd
%endif

%if %{with html}
# FIXME autodoc does not work for current tarball
sed -i "s|.sphinx.ext.autodoc.* | |" %{name}-web/conf.py
# sphinx is restricted in epel
sphinx-build %{?!rhel: %{?_smp_mflags} -a -b html -v -T} %{name}-web html
rm -r html/.buildinfo html/.doctrees
find html -name \*.js -print -delete
%endif


%install
%if 0%{?with_python2}
pushd %{name}-python
%py2_install
popd
%endif

%if 0%{?with_python3}
pushd %{name}-python3
%py3_install
%{?py3_other_install: %py3_other_install}
popd
%endif

%mvn_artifact %{name}-java/pom.xml %{name}-java/%{name}.jar
%mvn_install -J %{name}-java/javadoc
mkdir -p %{buildroot}%{_datadir}/%{name}
ln -sf %{_javadir}/%{name}/%{name}.jar %{buildroot}%{_datadir}/%{name}


%check
alias comment=true

%if %{with test_java}
comment '----- check test_java -----'
# do build tests only, see above in build for disabled test
#sed -i -r "s|no(test)|\1|" %{name}-java/build.xml
# test go!
ant -f %{name}-java/build.xml java-test
%endif

%if %{with test_python}
comment '----- check test_python -----'
# important: build java tests before, otherwise will not work
sed -i -r "s|no(test)|\1|" %{name}-java/build.xml
ant -f %{name}-java/build.xml build

# FIXME tests fail when in parallel, maybe too few resources?
#export NOSE_PROCESSES=-1
# test go!
ant -f %{name}-java/build.xml python-test 2>&1 |tee python-test.log
# be sure we ran with python3
%if 0%{?with_python3}
if [ ! $(grep -c '\[exec\] Python 3' python-test.log) ]; then
 comment 'error: wrong python version!'
 exit 1
fi
%endif
%endif


%if 0%{?with_python2}
%files -n python2-%{name}
%license %{name}-python/LICENSE.txt
%doc README.rst
%{python2_sitelib}/*.egg-info
%{python2_sitelib}/%{name}/
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{name}
%license %{name}-python/LICENSE.txt
%doc README.rst
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{name}/
%endif

%if 0%{?python3_other_pkgversion}
%files -n python%{python3_other_pkgversion}-%{name}
%license %{name}-python/LICENSE.txt
%doc README.rst
%{python3_other_sitelib}/*.egg-info
%{python3_other_sitelib}/%{name}/
%endif

%files java -f .mfiles
%license %{name}-java/LICENSE.txt
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.jar

%files doc
%license %{name}-web/LICENSE.txt
%doc %{name}-web/TODO
%if %{with html}
%doc html/
%endif

%if %{with javadoc}
%files javadoc -f .mfiles-javadoc
%license %{name}-java/LICENSE.txt
%endif


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 0.10.9-12
- Rebuilt for Drop i686 JDKs

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.10.9-11
- Rebuilt for Python 3.11

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.10.9-10
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.10.9-7
- Fix path to hamcrest JAR

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.10.9-7
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 30 2020 Fabio Valentini <decathorpe@gmail.com> - 0.10.9-5
- Remove unnecessary dependency on parent POM.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 0.10.9-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.9-2
- Rebuilt for Python 3.9

* Sat Feb 08 2020 Raphael Groner <projects.rg@smart.ms> - 0.10.9-1
- new version

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.8.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.8.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Raphael Groner <projects.rg@smart.ms> - 0.10.8.1-1
- new version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep 29 2018 Raphael Groner <projects.rg@smart.ms> - 0.10.7-3
- drop python2 subpackage in Fedora but not EPEL7
- add python3 subpackages in epel7
- simplify execution of sphinx

* Wed Sep 19 2018 Petr Viktorin <pviktori@redhat.com> - 0.10.7-2
- Remove the Python 2 subpackage
  rhbz#1628178

* Sun Jul 15 2018 Raphael Groner <projects.rg@smart.ms> - 0.10.7-1
- new version
- adjust patch for Base64 replacement
- drop support for java 7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.6-5
- Rebuilt for Python 3.7

* Tue Feb 27 2018 Raphael Groner <projects.rg@smart.ms> - 0.10.6-4
- add Obsoletes to indicate rename of subpackage, rhbz#1548046

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Feb 07 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10.6-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Sep 19 2017 Raphael Groner <projects.rg@smart.ms> - 0.10.6-1
- new version

* Mon Sep 18 2017 Raphael Groner <projects.rg@smart.ms> - 0.10.5-3
- enforce explicitly python3 for sphinx and nosetests
- add more debugging for check

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Raphael Groner <projects.rg@smart.ms> - 0.10.5-1
- bump version, rhbz#1385653

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10.4-2
- Rebuild for Python 3.6

* Sat Dec 10 2016 Raphael Groner <projects.rg@smart.ms> - 0.10.4-1
- new version

* Thu Sep 01 2016 Raphael Groner <projects.rg@smart.ms> - 0.10.3-1
- new version
- add python2 prefixed subpackage
- add python_provide macro

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jul 10 2016 Raphael Groner <projects.rg@smart.ms> - 0.10.2.1-1
- new version

* Wed May 11 2016 Raphael Groner <projects.rg@smart.ms> - 0.10.1-1
- new version

* Thu Apr 21 2016 Raphael Groner <projects.rg@smart.ms> - 0.10-1
- bump to v0.10, rhbz#1327918

* Fri Mar 25 2016 Raphael Groner <projects.rg@smart.ms> - 0.9.2-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1 (#1297698)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 05 2015 Raphael Groner <projects.rg@smart.ms> - 0.9-1
- official upstream release

* Tue Jul 21 2015 Raphael Groner <projects.rg@smart.ms> - 0.9-0.5.pre.20150720git1cda77a
- new snapshot of upstream
- run tests with python3
- use sed with regions

* Sat May 23 2015 Raphael Groner <projects.rg@smart.ms> - 0.9-0.4.pre.20150503gitd9a950d
- unbundle MiGBase64
- improve checks
- improve sphinx html
- add build conditionals

* Wed May 06 2015 Raphael Groner <projects.rg@smart.ms> - 0.9-0.3.pre.20150503gitd9a950d
- new snapshot of upstream
- remove some obsolete files
- fix Summary and URL
- fix rpmlint warnings

* Thu Apr 30 2015 Raphael Groner <projects.rg@smart.ms> - 0.9-0.2.pre.20141101git9a8ab93
- fix pathes and maven
- add python-sphinx to generate additional documentation

* Mon Apr 27 2015 Raphael Groner <projects.rg@smart.ms> - 0.9-0.1.pre.20141101git9a8ab93
- initial
