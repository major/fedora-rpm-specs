# This package is a component of sbt, but needs sbt to build.  Use this to
# bootstrap when sbt is not available.
%bcond_with sbt

# Scal build version
%global scala_version 2.13

Name:           scalacheck
Version:        1.17.0
Release:        2%{?dist}
Summary:        Property-based testing for Scala

License:        BSD-3-Clause
URL:            https://scalacheck.org/
Source0:        https://github.com/typelevel/scalacheck/archive/v%{version}/%{name}-%{version}.tar.gz

%if %{without sbt}
# We don't generate a POM from the ant build
Source1:       https://repo1.maven.org/maven2/org/scalacheck/%{name}_%{scala_version}/%{version}/%{name}_%{scala_version}-%{version}.pom
Source2:       %{name}.mf
Source3:       Generate.java
%endif

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.scala-sbt:test-interface)
%if %{without sbt}
BuildRequires:  mvn(org.scala-lang:scala-compiler)
%else
BuildRequires:  sbt
%endif

%description
ScalaCheck is a library written in Scala and used for automated
property-based testing of Scala or Java programs.  ScalaCheck was
originally inspired by the Haskell library QuickCheck, but has also
ventured into its own.

ScalaCheck has no external dependencies other than the Scala runtime,
and works great with sbt, the Scala build tool.  It is also fully
integrated in the test frameworks ScalaTest, specs2, and LambdaTest.
You can of course also use ScalaCheck completely standalone, with its
built-in test runner.

%prep
%autosetup

%if %{with sbt}
cp -r /usr/share/java/sbt/ivy-local .
mkdir boot
%endif

%mvn_file org.%{name}:%{name}_%{scala_version} %{name}

%build
%if %{without sbt}
# Generate files
GENDIR=$PWD/core/shared/src/main/scala/org/scalacheck
cd project
cp -p %{SOURCE3} .
CLASSPATH=.:$(build-classpath scala/scala-library)
scalac -g:vars codegen.scala
javac -cp $CLASSPATH Generate.java
java -cp $CLASSPATH Generate $GENDIR
cd -

# Build the jar
mkdir target
files="project/codegen.scala $(find core/shared/src/main/scala -name \*.scala)"
files="$files $(find core/shared/src/main/scala-2.13+ -name \*.scala)"
files="$files $(find core/jvm/src/main -name \*.scala)"
scalac -g:vars -release 11 -classpath $(build-classpath test-interface) \
  -d target $files
cd target
sed 's/@VERSION@/%{version}/g' %{SOURCE2} > %{name}.mf
jar -c -m %{name}.mf -f %{name}.jar org
cd -
%mvn_artifact %{SOURCE1} target/%{name}.jar
%else
export SBT_BOOT_DIR=$PWD/boot
export SBT_IVY_DIR=$PWD/ivy-local
sbt package deliverLocal publishM2Configuration
%mvn_artifact target/scala-%{scala_version}/%{name}_%{scala_version}-%{version}.pom target/scala-%{scala_version}/%{name}_%{scala_version}-%{version}.jar
%endif

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG.markdown README.markdown doc/UserGuide.md
%license LICENSE

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Sep 16 2022 Jerry James <loganjerry@gmail.com> - 1.17.0-1
- Version 1.17.0
- Convert License tag to SPDX

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.16.0-2
- Rebuilt for Drop i686 JDKs

* Fri Apr  8 2022 Jerry James <loganjerry@gmail.com> - 1.16.0-1
- Version 1.16.0

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.15.4-4
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu May  6 2021 Jerry James <loganjerry@gmail.com> - 1.15.4-1
- Version 1.15.4

* Wed Feb 24 2021 Jerry James <loganjerry@gmail.com> - 1.15.3-1
- Version 1.15.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Jerry James <loganjerry@gmail.com> - 1.15.2-1
- Version 1.15.2

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-17
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.11.3-15
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 06 2015 gil cattaneo <puntogil@libero.it> 1.11.3-6
- Fix FTBFS RHBZ#1107280
- Introduce license macro

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 10 2014 William Benton <willb@redhat.com> - 1.11.3-3
- rebuild

* Thu Jan 30 2014 William Benton <willb@redhat.com> - 1.11.3-2 
- rebuild now that all of our dependencies are in stable

* Wed Jan 29 2014 William Benton <willb@redhat.com> - 1.11.3-1 
- added optional but on-by-default Ant build (thanks to Gil Cattaneo for contributing this!)

* Mon Dec 23 2013 William Benton <willb@redhat.com> - 1.11.0-1 
- initial package
