%global namedreltag  -alpha-11
%global namedversion %{version}%{?namedreltag}
%global dotreltag    %(echo %{namedreltag} | tr - .)

Name:          maven-native
Version:       1.0
Release:       0.21%{dotreltag}%{?dist}
Summary:       Compile c and c++ source under Maven
# Automatically converted from old format: ASL 2.0 and MIT - review is highly recommended.
License:       Apache-2.0 AND LicenseRef-Callaway-MIT
Url:           https://github.com/mojohaus/maven-native/
Source0:       https://repo1.maven.org/maven2/org/codehaus/mojo/natives/%{name}/%{namedversion}/%{name}-%{namedversion}-source-release.zip
Source1:       plexus_components-bcc.xml
Source2:       plexus_components-generic-c.xml
Source3:       plexus_components-manager.xml
Source4:       plexus_components-msvc.xml

BuildRequires: maven-local
BuildRequires: mojo-parent
BuildRequires: mvn(aopalliance:aopalliance)
BuildRequires: mvn(bcel:bcel)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.sf.cglib:cglib)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires: mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires: mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch

%description
Maven Native - compile C and C++ source under Maven
with compilers such as GCC, MSVC, GCJ etc ...

%package components
Summary:       Maven Native Components

%description components
%{summary}.

%package -n native-maven-plugin
Summary:       Native Maven Plugin

%description -n native-maven-plugin
%{summary}.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

for d in LICENSE ; do
  iconv -f iso8859-1 -t utf-8 $d.txt > $d.txt.conv && mv -f $d.txt.conv $d.txt
  sed -i 's/\r//' $d.txt
done

# use jvm apis
%pom_remove_dep backport-util-concurrent:backport-util-concurrent
%pom_remove_dep backport-util-concurrent:backport-util-concurrent maven-native-api
sed -i "s|edu.emory.mathcs.backport.java.util.concurrent|java.util.concurrent|" \
 maven-native-api/src/main/java/org/codehaus/mojo/natives/compiler/AbstractCompiler.java

sed -i 's|<artifactId>maven-project|<artifactId>maven-compat|' pom.xml
%pom_remove_plugin com.github.ekryd.sortpom:sortpom-maven-plugin
%pom_remove_plugin org.codehaus.plexus:plexus-component-metadata maven-native-components
%pom_remove_plugin org.codehaus.plexus:plexus-component-metadata native-maven-plugin
%pom_add_dep org.apache.maven:maven-compat native-maven-plugin
%pom_add_dep org.apache.maven:maven-core native-maven-plugin

# missing test deps
%pom_add_dep aopalliance:aopalliance::test native-maven-plugin
%pom_add_dep net.sf.cglib:cglib::test native-maven-plugin

%mvn_package ":%{name}" %{name}
%mvn_package ":%{name}-api" %{name}
%mvn_package ":%{name}-components" components
%mvn_package ":%{name}-bcc" components
%mvn_package ":%{name}-generic-c" components
%mvn_package ":%{name}-javah" components
%mvn_package ":%{name}-manager" components
%mvn_package ":%{name}-msvc" components
%mvn_package ":%{name}-mingw" components
%mvn_package ":native-maven-plugin" native-maven-plugin

mkdir -p ./maven-native-components/maven-native-{bcc,generic-c,manager,msvc}/src/main/resources/META-INF/plexus/
for CMP in bcc generic-c manager msvc
do
	cp -a %{_sourcedir}/plexus_components-$CMP.xml ./maven-native-components/maven-native-$CMP/src/main/resources/META-INF/plexus/components.xml
done

%build

#  junit.framework.AssertionFailedError: Failed to create plexus container.
# native-maven-plugin with maven3 test failures:
# Caused by: java.lang.ClassNotFoundException: org.apache.maven.artifact.repository.Authentication
#  java.lang.VerifyError: (class: org/apache/maven/project/MavenProject, 
# method: getSnapshotArtifactRepository signature: ()Lorg/apache/maven/artifact/repository/ArtifactRepository;)
# Incompatible argument to function
# force org.codehaus.plexus plexus-container-default 1.5.5 apis
# test skipped cause: [ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:2.15:test (default-test) on project native-maven-plugin: Execution default-test of goal org.apache.maven.plugins:maven-surefire-plugin:2.15:test failed: There was an error in the forked process
# [ERROR] java.lang.NoClassDefFoundError: org/sonatype/aether/RepositorySystemSession
%mvn_build -f -s --xmvn-javadoc -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles-%{name}
%dir %{_javadir}/%{name}
%license LICENSE.txt

%files components -f .mfiles-components
%license LICENSE.txt

%files -n native-maven-plugin -f .mfiles-native-maven-plugin
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.21.alpha.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0-0.20.alpha.11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.19.alpha.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.0-0.18.alpha.11
- Rebuilt for java-21-openjdk as system jdk

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.17.alpha.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.alpha.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 27 2023 Nicolas De Amicis <deamicis@bluewin.ch> - 1.0-0.15.alpha.11
- Remove dependency plexus-component-api

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.14.alpha.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.13.alpha.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.12.alpha.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.0-0.11.alpha.11
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.0-0.10.alpha.11
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.9.alpha.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.8.alpha.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.7.alpha.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.6.alpha.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Nicolas De Amicis <deamicis@bluewin.ch> - 1.0-0.5.alpha.11
- Removing not used dependency commons-lang

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.0-0.4.alpha.11
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jun 10 2020 Nicolas De Amicis <deamicis@bluewin.ch> - 1.0-0.3.alpha.11
- Use XMvn javadoc

* Wed Apr 08 2020 Nicolas De Amicis <deamicis@bluewin.ch> - 1.0-0.2.alpha.11
- add missing files (plexus components.xml) see bug 1822109

* Thu Feb 20 2020 Nicolas De Amicis <deamicis@bluewin.ch> 1.0-0.1.alpha.11
- update to 1.0-alpha-11

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.17.alpha.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.alpha.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.15.alpha.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.14.alpha.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.13.alpha.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.12.alpha.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.11.alpha.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.10.alpha.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 10 2015 gil cattaneo <puntogil@libero.it> 1.0-0.9.alpha.8
- introduce license macro

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0-0.8.alpha.8
- Rebuild to fix Maven auto-requires

* Sun Jun 22 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.0-0.7.alpha.8
- Bump Release. "0.6.alpha.7" is larger than "0.1.alpha.8" in rpm parlance

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.2.alpha.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 20 2014 gil cattaneo <puntogil@libero.it> 1.0-0.1.alpha.8
- update to 1.0-alpha-8

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0-0.6.alpha.7
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.alpha.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 gil cattaneo <puntogil@libero.it> 1.0-0.4.alpha.7
- switch to XMvn
- minor changes to adapt to current guideline

* Tue Jun 11 2013 gil cattaneo <puntogil@libero.it> 1.0-0.3.alpha.7
- fix license tag

* Tue Oct 30 2012 gil cattaneo <puntogil@libero.it> 1.0-0.2.alpha.7
- fix javac target

* Mon Oct 08 2012 gil cattaneo <puntogil@libero.it> 1.0-0.1.alpha.7
- initial rpm

