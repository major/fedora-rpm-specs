%{?python_enable_dependency_generator}

%global modname javabridge

%global commit0 61942d217dd2edbd0733a99710493e4a993a9e63
%global date0   20211221
%global scommit0 %(c=%{commit0}; echo ${c:0:7}) 

Name:           python-%{modname}
Version:        1.0.19
Release:        10.%{date0}git61942d2%{?dist}
Summary:        Python wrapper for the Java Native Interface

License:        MIT
URL:            https://github.com/LeeKamentsky/python-%{modname}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{modname}-%{scommit0}.tar.gz
Patch0:         %{modname}-rhino-noversion.patch

%global _description\
The javabridge Python package makes it easy to start a Java virtual machine (JVM)\
from Python and interact with it. Python code can interact with the JVM using a\
low-level API or a more convenient high-level API.

%description
%_description
An python module which provides a convenient example.

%package -n python%{python3_pkgversion}-%{modname}
Summary:        %{summary}
BuildRequires:  java-devel
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-Cython
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-nose
BuildRequires:  gcc
BuildRequires:  javapackages-local
BuildRequires:  rhino
Requires:       rhino
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}

# https://github.com/LeeKamentsky/python-javabridge/issues/170
ExclusiveArch:  i686 x86_64

%description -n python%{python3_pkgversion}-%{modname}
%_description

%prep
%autosetup -p1 -n%{name}-%{commit0}
# unbundle
find . -name \*.jar -print -delete
ln -s $(find-jar org.mozilla:rhino) %{modname}/jars

%build
export JAVA_HOME=%{_prefix}/lib/jvm/java
%py3_build
%{__python3} setup.py build_sphinx
find docs/_build -name .\* -print -delete

%install
export JAVA_HOME=%{_prefix}/lib/jvm/java
%py3_install

%check
export JAVA_HOME=%{_prefix}/lib/jvm/java
export PYTHONPATH=tests-install:%{buildroot}%{python3_sitelib}
%{__python3} setup.py develop --install-dir=tests-install
%{__python3} setup.py nosetests

# Note that there is no %%files section for the unversioned python module
%files -n python%{python3_pkgversion}-%{modname}
%license LICENSE
%doc README.rst
%doc docs/_build/html
%{python3_sitearch}/%{modname}-*.egg-info/
%{python3_sitearch}/%{modname}/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-10.20211221git61942d2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.0.19-9.20211221git61942d2
- Rebuilt for Python 3.11

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.19-8.20211221git61942d2
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-7.20211221git61942d2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Raphael Groner <raphgro@fedoraproject.org> - 1.0.19-6.20211221git61942d2
- add fix for compatibility with python 3.11, rhbz#2033557

* Mon Oct 18 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 1.0.19-5
- Don't hardcode paths to JAR

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.19-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 08 2020 Raphael Groner <raphgro@fedoraproject.org> - 1.0.19-1
- bump to v1.0.19

* Mon Sep 07 2020 Charalampos Stratakis <cstratak@redhat.com> - 1.0.18-8.20190729gitc7ccaed
- Explicitly define the JAVA_HOME env variable, Resolves: rhbz#1865294

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-7.20190729gitc7ccaed
- Second attempt - Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-6.20190729gitc7ccaed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.18-5.20190729gitc7ccaed
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-4.20190729gitc7ccaed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Raphael Groner <projects.rg@smart.ms> - 1.0.18-3.20190729gitc7ccaed
* use new snapshot
- exclusive x86

* Sat Jul 27 2019 Raphael Groner <projects.rg@smart.ms> - 1.0.18-2.20190723git16d6c91
- use latest git snapshot to support cython with python3

* Sat May 11 2019 Raphael Groner <projects.rg@smart.ms> - 1.0.18-1
- initial
