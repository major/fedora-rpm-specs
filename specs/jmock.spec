Name:           jmock
Version:        2.12.0
Release:        19%{?dist}
Summary:        Java library for testing code with mock objects
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.jmock.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/jmock-developers/jmock-library/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Port-to-jakarta.xml.ws-4.0.0.patch

BuildRequires:  maven-local
BuildRequires:  mvn(cglib:cglib)
BuildRequires:  mvn(com.google.auto.service:auto-service)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(jakarta.xml.ws:jakarta.xml.ws-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.bytebuddy:byte-buddy)
BuildRequires:  mvn(org.apache-extras.beanshell:bsh)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-params)
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.ow2.asm:asm)

# required for some unit tests
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit-platform)

%description
Mock objects help you design and test the interactions between the objects in
your programs.
The jMock library:
  * makes it quick and easy to define mock objects, so you don't break the
    rhythm of programming.
  * lets you precisely specify the interactions between your objects, reducing
    the brittleness of your tests.
  * works well with the auto-completion and re-factoring features of your IDE
  * plugs into your favorite test framework
  * is easy to extend.

%package example
Summary:        jMock Examples
%description example
jMock Examples.

%package imposters
Summary:        jMock imposters
%description imposters
jMock imposters.

%package junit3
Summary:        jMock JUnit 3 Integration
%description junit3
jMock JUnit 3 Integration.

%package junit4
Summary:        jMock JUnit 4 Integration
%description junit4
jMock JUnit 4 Integration.

%package junit5
Summary:        jMock JUnit 5 Integration
%description junit5
jMock JUnit 5 Integration.

%package legacy
Summary:        jMock Legacy Plugins
%description legacy
Plugins that make it easier to use jMock with legacy code.

%package testjar
Summary:        jMock Test Jar
%description testjar
Source for JAR files used in jMock Core tests.

%{?javadoc_package}

%prep
# -p1: strip one level directory in patch
# -n: base directory name
%autosetup -p1 -n %{name}-library-%{version}
# remove unnecessary dependency on parent POM
%pom_remove_parent
# remove maven plugins that are not required for RPM builds
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin -r :versions-maven-plugin
%pom_remove_plugin :maven-gpg-plugin testjar
# change dep artifact
%pom_change_dep :jaxws-api jakarta.xml.ws:jakarta.xml.ws-api jmock
# use correct maven artifact for @javax.annotations.Nullable
%pom_change_dep com.google.code.findbugs:annotations com.google.code.findbugs:jsr305 testjar
# don't install imposters-tests and parent package
%mvn_package :jmock-imposters-tests __noinstall
%mvn_package :jmock-parent __noinstall

%build
%mvn_build -s -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files           -f .mfiles-%{name}
%doc README*
%license LICENSE.txt
%files example   -f .mfiles-%{name}-example
%files imposters -f .mfiles-%{name}-imposters
%files junit3    -f .mfiles-%{name}-junit3
%files junit4    -f .mfiles-%{name}-junit4
%files junit5    -f .mfiles-%{name}-junit5
%files legacy    -f .mfiles-%{name}-legacy
%files testjar   -f .mfiles-%{name}-testjar
%license LICENSE.txt

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.12.0-18
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 2.12.0-16
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 2.12.0-12
- Resolve issues related to jakarta.xml.ws 4.0.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 2.12.0-10
- Change BR: jaxws-api to jakarta.xml.ws-api
- Enable enforcer plugin

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.12.0-8
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.12.0-7
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 2.12.0-5
- Don't install jmock-parent subpackage
- Patch is removed upstream (https://github.com/jmock-developers/jmock-library/commit/6eab2dd8e15c81117bd70ee05c150f6b686f916c)
- Ignore tests failure

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 15 2020 Jerry James <loganjerry@gmail.com> - 2.12.0-2
- Add jmock-junit4.13.patch to fix test failure with junit4.13

* Tue Jul 28 2020 Fabio Valentini <decathorpe@gmail.com> - 2.12.0-1
- Update to version 2.12.0.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Mat Booth <mat.booth@redhat.com> - 2.8.2-12
- Allow building against JDK 11

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.8.2-11
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Fabio Valentini <decathorpe@gmail.com> - 2.8.2-9
- Remove unnecessary dependency on parent POM.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 08 2016 gil cattaneo <puntogil@libero.it> 2.8.2-2
- disable test failure

* Sun Mar 06 2016 gil cattaneo <puntogil@libero.it> 2.8.2-1
- updated to 2.8.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 gil cattaneo <puntogil@libero.it> 2.8.1-1
- updated to 2.8.1

* Fri Feb 06 2015 gil cattaneo <puntogil@libero.it> 2.5.1-8
- introduce license macro

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 gil cattaneo <puntogil@libero.it> 2.5.1-6
- Use .mfiles generated during build
- Fix junit dep

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 2.5.1-5
- Use Requires: java-headless rebuild (#1067528)

* Fri Nov 15 2013 gil cattaneo <puntogil@libero.it> 2.5.1-4
- use objectweb-asm3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Apr 19 2012 gil cattaneo <puntogil@libero.it> 2.5.1-1
- initial rpm

