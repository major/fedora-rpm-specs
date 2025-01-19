%global giturl	https://github.com/radsz/jacop

Name:		jacop
Version:	4.10.0
Release:	2%{?dist}
License:	AGPL-3.0-or-later
Summary:	Java Constraint Programming solver
URL:		http://jacop.osolpro.com/
VCS:		git:%{giturl}.git
Source:		%{giturl}/archive/%{version}/%{name}-%{version}.tar.gz
# Avoid use of deprecated interfaces
Patch:		%{name}-deprecation.patch
# Fix various javadoc errors
# https://github.com/radsz/jacop/pull/73
Patch:		%{name}-javadoc.patch

BuildRequires:	maven-local
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:	mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:	mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:	mvn(org.jacoco:jacoco-maven-plugin)
BuildRequires:	mvn(org.mockito:mockito-all)
BuildArch:	noarch
ExclusiveArch:  %{java_arches} noarch

%description
Java Constraint Programming solver, JaCoP for short, is an open-source
Java library, which provides Java users with Constraint Programming
technology.  JaCoP has been under active development since the year
2001.  Krzysztof Kuchcinski and Radoslaw Szymanek are the core
developers of this Java library.

%package javadoc
Summary:	Javadocs for %{name}

%description	javadoc
This package contains the API documentation for %{name}.

%prep
%autosetup -p1

# Remove plugins not needed for an RPM build
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-jdeps-plugin
%pom_remove_plugin :maven-project-info-reports-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-surefire-report-plugin
%pom_remove_plugin :spotbugs-maven-plugin

# Remove unused slf4j dependencies.
# https://github.com/radsz/jacop/commit/e61795bdd161499173933bd90a7ecfc0804e76df
%pom_remove_dep org.slf4j

# Do not build the Scala interface
%pom_remove_plugin net.alchim31.maven:scala-maven-plugin
%pom_remove_dep org.scala-lang:scala-library
%pom_remove_dep org.scala-lang:scala-compiler
sed -i '\@src/main/scala@d' pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.md
%doc CHANGELOG README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 30 2024 Jerry James <loganjerry@gmail.com> - 4.10.0-1
- Version 4.10.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 4.9.0-5
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Feb  9 2023 Jerry James <loganjerry@gmail.com> - 4.9.0-1
- Version 4.9.0
- Convert License tag to SPDX
- Drop dependency on scala

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 4.8-8
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 4.8-7
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 19 2021 Orion Poplawski <orion@nwra.com> - 4.8-5
- Add missing BR on mvn(junit:junit) (FTBFS bz#1987584)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Jerry James <loganjerry@gmail.com> - 4.8-2
- Fix building the scala classes

* Fri Dec  4 2020 Jerry James <loganjerry@gmail.com> - 4.8-1
- Version 4.8

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Fabio Valentini <decathorpe@gmail.com> - 4.7-3
- Remove unnecessary dependency on maven-javadoc-plugin.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 4.7-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Feb 21 2020 Jerry James <loganjerry@gmail.com> - 4.7-1
- Version 4.7
- Upstream now ships a license file
- Drop unnecessary BRs
- Drop upstreamed -privilege patch

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 14 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.2-7
- Correct FTBFS in rawhide (#1423750)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.2-3
- Rebuild for newer scala.

* Sun Jan 25 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.2-2
- Use the license macro (#1177191#c2)
- Add explicit requires to owners of directories (#1177191#c2)
- Become owner of maven-poms/jacop directory (#1177191#c2)

* Sat Dec 20 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 4.2-1
- Initial jacop spec.
