# Note to the interested reader:
#   fedpkg mockbuild --without tests
# will make mvn_build macro skip tests.
# See: https://github.com/fedora-java/javapackages/issues/62

%global javacup_or_asm java_cup:java_cup|org\\.ow2\\.asm:asm.*
# Don't have generated mvn()-style requires for java_cup or asm
%global mvn_javacup_or_asm_matcher .*mvn\\(%{javacup_or_asm}\\)
# Don't have generated requires for java-headless >= 1:1.9
%global java_headless_matcher java-headless >= 1:(1\\.9|9)
%global __requires_exclude ^%{mvn_javacup_or_asm_matcher}|%{java_headless_matcher}$

%global homedir %{_datadir}/%{name}
%global bindir %{homedir}/bin

Name:             byteman
Version:          4.0.26
Release:          3%{?dist}
Summary:          Java agent-based bytecode injection tool
# most of the code is LGPL-2.1-or-later
# agent/src/main/java/org/jboss/byteman/agent/adapter/RuleGeneratorAdapter.java is BSD-3-Clause
License:          LGPL-2.1-or-later AND BSD-3-Clause
URL:              http://www.jboss.org/byteman
# wget -O 4.0.16.tar.gz https://github.com/bytemanproject/byteman/archive/4.0.16.tar.gz
Source0:          https://github.com/bytemanproject/byteman/archive/%{version}.tar.gz

BuildArch:        noarch
ExclusiveArch:  %{java_arches} noarch

# Byteman 4.x requires JDK 9+ to build. Require JDK 10 explicitly.
BuildRequires:    java-25-devel >= 1:11
BuildRequires:    maven-local-openjdk25
BuildRequires:    maven-shade-plugin
BuildRequires:    maven-source-plugin
BuildRequires:    maven-plugin-plugin
BuildRequires:    maven-bundle-plugin
BuildRequires:    maven-assembly-plugin
BuildRequires:    maven-failsafe-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-testng
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    maven-surefire-provider-junit5
BuildRequires:    maven-verifier-plugin
BuildRequires:    maven-dependency-plugin
BuildRequires:    java_cup
BuildRequires:    objectweb-asm
BuildRequires:    junit
BuildRequires:    junit5
BuildRequires:    testng

Provides:         bundled(objectweb-asm) = 9.1
Provides:         bundled(java_cup) = 1:0.11b-17
# We are filtering java-headless >= 1:1.9 requirement. Add
# JDK 8 requirement here explicitly which shouldn't match the filter.
Requires:         java-25-headless >= 1:1.8

# Related pieces removed via pom_xpath_remove macros
Patch1:           remove_submit_integration_test_verification.patch
Patch2:           testng7_port.patch

%description
Byteman is a tool which simplifies tracing and testing of Java programs.
Byteman allows you to insert extra Java code into your application,
either as it is loaded during JVM startup or even after it has already
started running. The injected code is allowed to access any of your data
and call any application methods, including where they are private.
You can inject code almost anywhere you want and there is no need to
prepare the original source code in advance nor do you have to recompile,
repackage or redeploy your application. In fact you can remove injected
code and reinstall different code while the application continues to execute.

%package javadoc
Summary:          Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%package rulecheck-maven-plugin
Summary:          Maven plugin for checking Byteman rules.

%description rulecheck-maven-plugin
This package contains the Byteman rule check maven plugin.

%package bmunit
Summary:          TestNG and JUnit integration for Byteman.

%description bmunit
The Byteman bmunit jar provides integration of Byteman into
TestNG and JUnit tests.

%package dtest
Summary:          Remote byteman instrumented testing.

%description dtest
The Byteman dtest jar supports instrumentation of test code executed on
remote server hosts and validation of assertions describing the expected
operation of the instrumented methods.

%prep
%setup -q -n byteman-%{version}

# Fix the gid:aid for java_cup
sed -i "s|net.sf.squirrel-sql.thirdparty-non-maven|java_cup|" agent/pom.xml
sed -i "s|java-cup|java_cup|" agent/pom.xml
sed -i "s|net.sf.squirrel-sql.thirdparty-non-maven|java_cup|" tests/pom.xml
sed -i "s|java-cup|java_cup|" tests/pom.xml

# Remove Submit integration test invocations (agent)
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-failsafe-plugin']/pom:executions/pom:execution[pom:id='submit.TestSubmit']" agent
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-failsafe-plugin']/pom:executions/pom:execution[pom:id='submit.TestSubmit.compiled']" agent
%patch -P1 -p2
%patch -P2 -p2

# Remove Submit integration test invocations (tests)
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-failsafe-plugin']/pom:executions/pom:execution[pom:id='submit.TestSubmit']" tests
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-failsafe-plugin']/pom:executions/pom:execution[pom:id='submit.TestSubmit.compiled']" tests

# Remove scope=system and systemPath for com.sun:tools
%pom_xpath_remove "pom:profiles/pom:profile/pom:dependencies/pom:dependency[pom:artifactId='tools']/pom:scope" install
%pom_xpath_remove "pom:profiles/pom:profile/pom:dependencies/pom:dependency[pom:artifactId='tools']/pom:systemPath" install
%pom_xpath_remove "pom:profiles/pom:profile/pom:dependencies/pom:dependency[pom:artifactId='tools']/pom:scope" contrib/bmunit
%pom_xpath_remove "pom:profiles/pom:profile/pom:dependencies/pom:dependency[pom:artifactId='tools']/pom:systemPath" contrib/bmunit

# Some tests fail intermittently during builds. Disable them.
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:executions" contrib/bmunit
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration" '<skip>true</skip>' contrib/bmunit

# source/target 1.6 is not supported by 17; default is now 1.8
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" pom.xml
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" pom.xml

# Don't build download, docs modules
%pom_disable_module download


# Don't use javadoc plugin, use XMvn for javadocs
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :central-publishing-maven-plugin
%pom_remove_dep 'org.apache.maven:maven-project' contrib/rulecheck-maven-plugin
%pom_xpath_remove 'pom:execution[pom:id="make-javadoc-assembly"]' byteman

# Put byteman-rulecheck-maven-plugin into a separate package
%mvn_package ":byteman-rulecheck-maven-plugin" rulecheck-maven-plugin

# CNFE being thrown without this for bmunit5 in rawhide and with tests enabled
%pom_add_dep "org.apache.commons:commons-lang3" contrib/bmunit5
# Put byteman-bmunit/byteman-dtest into a separate packages since they
# runtime require junit
%mvn_package ":byteman-bmunit" bmunit
%mvn_package ":byteman-dtest" dtest

%build
export JAVA_HOME=/usr/lib/jvm/java-openjdk
# Use --xmvn-javadoc so as to avoid maven-javadoc-plugin issue
# (fixed in 3.1.0, fedora has 3.0.1):
# See https://issues.apache.org/jira/browse/MJAVADOC-555
#     https://bugs.openjdk.java.net/browse/JDK-8212233
%mvn_build --xmvn-javadoc -f

%install
%mvn_install

install -d -m 755 $RPM_BUILD_ROOT%{_bindir}

install -d -m 755 $RPM_BUILD_ROOT%{homedir}
install -d -m 755 $RPM_BUILD_ROOT%{homedir}/lib
install -d -m 755 $RPM_BUILD_ROOT%{bindir}

install -m 755 bin/bmsubmit.sh $RPM_BUILD_ROOT%{bindir}/bmsubmit
install -m 755 bin/bminstall.sh  $RPM_BUILD_ROOT%{bindir}/bminstall
install -m 755 bin/bmjava.sh  $RPM_BUILD_ROOT%{bindir}/bmjava
install -m 755 bin/bmcheck.sh  $RPM_BUILD_ROOT%{bindir}/bmcheck

for f in bmsubmit bmjava bminstall bmcheck; do
cat > $RPM_BUILD_ROOT%{_bindir}/${f} << EOF
#!/bin/sh

export BYTEMAN_HOME=/usr/share/byteman
export JAVA_HOME=/usr/lib/jvm/java

\$BYTEMAN_HOME/bin/${f} \$*
EOF
done

chmod 755 $RPM_BUILD_ROOT%{_bindir}/*

for m in bmunit dtest install sample submit; do
  ln -s %{_javadir}/byteman/byteman-${m}.jar $RPM_BUILD_ROOT%{homedir}/lib/byteman-${m}.jar
done

# Create contrib/jboss-module-system structure since bminstall expects it
# for the -m option.
install -d -m 755 $RPM_BUILD_ROOT%{homedir}/contrib
install -d -m 755 $RPM_BUILD_ROOT%{homedir}/contrib/jboss-modules-system
ln -s %{_javadir}/byteman/byteman-jboss-modules-plugin.jar $RPM_BUILD_ROOT%{homedir}/contrib/jboss-modules-system/byteman-jboss-modules-plugin.jar

ln -s %{_javadir}/byteman/byteman.jar $RPM_BUILD_ROOT%{homedir}/lib/byteman.jar

%files -f .mfiles
%{homedir}/lib/byteman.jar
%{homedir}/lib/byteman-install.jar
%{homedir}/lib/byteman-sample.jar
%{homedir}/lib/byteman-submit.jar
%{homedir}/contrib/*
%{bindir}/*
%{_bindir}/*
%doc README
%license docs/copyright.txt

%files javadoc -f .mfiles-javadoc
%license docs/copyright.txt

%files rulecheck-maven-plugin -f .mfiles-rulecheck-maven-plugin
%license docs/copyright.txt

%files bmunit -f .mfiles-bmunit
%license docs/copyright.txt
%{homedir}/lib/byteman-bmunit.jar

%files dtest -f .mfiles-dtest
%license docs/copyright.txt
%{homedir}/lib/byteman-dtest.jar

%changelog
* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

%autochangelog
