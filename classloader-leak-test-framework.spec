%bcond_without tests

Name:		classloader-leak-test-framework
%global nwname classloader-leak-prevention-parent
Version:	2.7.0
Release:	5%{?dist}
Summary:	Detection and verification of Java ClassLoader leaks
License:	Apache-2.0
URL:		https://github.com/mjiderhamn/classloader-leak-prevention/tree/master/%{name}
Source0:	https://github.com/mjiderhamn/classloader-leak-prevention/archive/%{nwname}-%{version}.tar.gz

BuildArch:	noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:	maven-local
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.apache.bcel:bcel)

%description
Stand-alone test framework for detecting and/or verifying the existence or
non-existence of Java ClassLoader leaks. It is also possible to test leak
prevention mechanisms to confirm that the leak really is avoided. The framework
is an built upon JUnit.

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n classloader-leak-prevention-%{nwname}-%{version}

rm -r classloader-leak-prevention
cp -r %{name}/* .

%pom_remove_dep com.sun.faces:jsf-api
%pom_remove_dep com.sun.faces:jsf-impl
%pom_remove_dep javax.el:el-api
sed "s;<maven.compiler.source>1.6</maven.compiler.source>;<maven.compiler.source>8</maven.compiler.source>;" -i pom.xml
sed "s;<maven.compiler.target>1.6</maven.compiler.target>;<maven.compiler.target>8</maven.compiler.target>;" -i pom.xml
cat pom.xml | grep -B 3 -A 3 -e 1.6 -e 8

%pom_remove_plugin -r :maven-javadoc-plugin

%build
%if %{with tests}
%mvn_build --xmvn-javadoc
%else
%mvn_build -f --xmvn-javadoc
%endif

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.7.0-2
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.7.0-1
- bumped to newest versio
- moved source/target to 8

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.1.1-18
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 12 2021 Ondrej Dubaj <odubaj@redhat.com> - 1.1.1-15
- Remove maven-javadoc-plugin dependency

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.1.1-12
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri May 15 2020 Ondrej Dubaj <odubaj@redhat.com> - 1.1.1-11
- fixed javadoc build problem

* Thu May 14 2020 Jiri Vanek <jvanek@redhat.com> - 1.1.1-10
- removed javadoc, as it is broken as tooling is not ready for jdk11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1.1-5
- Disable tests and remove dependency on mojarra

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 03 2016 Tomas Repik <trepik@redhat.com> - 1.1.1-1
- initial package

