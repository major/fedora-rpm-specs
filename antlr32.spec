# Need to set this when bootstrapping due to self-dependency
%bcond_with bootstrap

%global bootstrap_version 3.1.3

Name:           antlr32
Version:        3.2
Release:        36%{?dist}
Summary:        ANother Tool for Language Recognition

License:        BSD
URL:            http://www.antlr3.org/
Source0:        http://www.antlr3.org/download/antlr-%{version}.tar.gz

%if %{with bootstrap}
# These artifacts are taken verbatim from maven central with the exception of the
# jar in source 2, which additionally has the java 8 compatibility patch given below
# These sources are only used for bootstrapping antlr32 into a new distro
Source1:        http://repo1.maven.org/maven2/org/antlr/antlr-master/%{bootstrap_version}/antlr-master-%{bootstrap_version}.pom
Source2:        http://repo1.maven.org/maven2/org/antlr/antlr/%{bootstrap_version}/antlr-%{bootstrap_version}.jar
Source3:        http://repo1.maven.org/maven2/org/antlr/antlr/%{bootstrap_version}/antlr-%{bootstrap_version}.pom
Source4:        http://repo1.maven.org/maven2/org/antlr/antlr-runtime/%{bootstrap_version}/antlr-runtime-%{bootstrap_version}.jar
Source5:        http://repo1.maven.org/maven2/org/antlr/antlr-runtime/%{bootstrap_version}/antlr-runtime-%{bootstrap_version}.pom
Source6:        http://repo1.maven.org/maven2/org/antlr/antlr3-maven-plugin/%{bootstrap_version}-1/antlr3-maven-plugin-%{bootstrap_version}-1.jar
Source7:        http://repo1.maven.org/maven2/org/antlr/antlr3-maven-plugin/%{bootstrap_version}-1/antlr3-maven-plugin-%{bootstrap_version}-1.pom
%endif

# This is backported from upstream antlr 3.5.2 for java 8 compatibility
# See https://github.com/antlr/antlr3/commit/e88907c259c43d42fa5e9f5ad0e486a2c1e004bb
Patch0:         java8-compat.patch

# Generate OSGi metadata
Patch1:         osgi-manifest.patch

# Patch to use exec maven plugin as alternative to unavailable antlr2 maven plugin
Patch2:         antlr2-usage.patch

BuildRequires:  maven-local
BuildRequires:  ant-antlr
BuildRequires:  exec-maven-plugin
BuildRequires:  maven-plugin-build-helper
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-plugin-plugin
BuildRequires:  stringtemplate >= 3.2

# Cannot require ourself when bootstrapping
%if %{without bootstrap}
BuildRequires:  %{name}-maven-plugin = %{version}
%endif

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
ANother Tool for Language Recognition, is a grammar parser generator.
This package is compatibility package containing an older version of
in order to support jython. No other packages should declare a
dependency on this one.

%package     maven-plugin
Summary:     Maven plug-in for creating ANTLR-generated parsers
Requires:    %{name}-tool = %{version}-%{release}

%description maven-plugin
Maven plug-in for creating ANTLR-generated parsers.

%package     tool
Summary:     Command line tool for creating ANTLR-generated parsers
Requires:    %{name}-java = %{version}-%{release}
Requires:    stringtemplate >= 3.2

%description tool
Command line tool for creating ANTLR-generated parsers.

%package     java
Summary:     Java run-time support for ANTLR-generated parsers

%description java
Java run-time support for ANTLR-generated parsers.

%package     javadoc
Summary:     API documentation for ANTLR

%description javadoc
%{summary}.

%prep
%setup -q -n antlr-%{version}

%patch0 -b .orig
%patch1 -b .orig
%patch2 -b .orig

# remove pre-built artifacts
find -type f -a -name *.jar -delete
find -type f -a -name *.class -delete

# remove corrupted files
find -name "._*" -delete

# disable stuff we don't need
%pom_disable_module gunit
%pom_disable_module gunit-maven-plugin
%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin
%pom_xpath_remove pom:build/pom:extensions
%pom_xpath_remove pom:build/pom:extensions runtime/Java
%pom_xpath_remove pom:build/pom:extensions antlr3-maven-plugin

# remove compiler plugin configurations that break builds with Java 11
%pom_remove_plugin -r :maven-compiler-plugin

# Avoid unnecessary dep on stringtemplate from the runtime sub-package
# It's only needed there for the DotGraph utility, it's not an actual runtime dep
%pom_xpath_inject "pom:dependency[pom:artifactId='stringtemplate']" "<optional>true</optional>" runtime/Java
%pom_add_dep org.antlr:stringtemplate:3.2 tool

# separate artifacts into sub-packages
%mvn_package :antlr tool
%mvn_package :antlr-master java
%mvn_package :antlr-runtime java
%mvn_package :antlr3-maven-plugin maven-plugin

# use a valid build target
find -name "pom.xml" | xargs sed -i -e "s|>jsr14<|>1.5<|"

# set a build number
sed -i -e "s|\${buildNumber}|%{release}|" tool/src/main/resources/org/antlr/antlr.properties

%mvn_compat_version 'org.antlr:antlr3-maven-plugin' %{version} %{bootstrap_version}-1
%mvn_compat_version 'org.antlr:antlr{,-master,-runtime}' %{version} %{bootstrap_version}

%build
mkdir -p .m2/org/antlr/antlr-master/%{version}/
cp -p pom.xml .m2/org/antlr/antlr-master/%{version}/antlr-master-%{version}.pom

%if %{with bootstrap}
mkdir -p .m2/org/antlr/antlr-master/%{bootstrap_version}/
cp -p %{SOURCE1} .m2/org/antlr/antlr-master/%{bootstrap_version}/.
mkdir -p .m2/org/antlr/antlr/%{bootstrap_version}/
cp -p %{SOURCE2} %{SOURCE3} .m2/org/antlr/antlr/%{bootstrap_version}/.
mkdir -p .m2/org/antlr/antlr-runtime/%{bootstrap_version}/
cp -p %{SOURCE4} %{SOURCE5} .m2/org/antlr/antlr-runtime/%{bootstrap_version}/.
mkdir -p .m2/org/antlr/antlr3-maven-plugin/%{bootstrap_version}-1/
cp -p %{SOURCE6} %{SOURCE7} .m2/org/antlr/antlr3-maven-plugin/%{bootstrap_version}-1/.
%endif

# a small number of tests always fail for reasons I don't fully understand
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files tool -f .mfiles-tool
%license tool/LICENSE.txt

%files maven-plugin -f .mfiles-maven-plugin
%license tool/LICENSE.txt

%files java -f .mfiles-java
%license tool/LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license tool/LICENSE.txt

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 3.2-33
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.2-32
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Mat Booth <mat.booth@redhat.com> - 3.2-27
- Avoid unnecessary dep on stringtemplate from the runtime sub-package

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.2-26
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jun 03 2020 Fabio Valentini <decathorpe@gmail.com> - 3.2-25
- Override javac source and target with 1.8 to fix build with OpenJDK 11.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 10 2019 Mat Booth <mat.booth@redhat.com> - 3.2-22
- Use bcond for bootstrapping and employ use of license macro

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 15 2017 Mat Booth <mat.booth@redhat.com> - 3.2-18
- Add a patch to use exec maven plugin as an alternative to the potentially
  unavailable antlr2 maven plugin

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jun 20 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-15
- Add missing build-requires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-13
- Remove workaround for rhbz#1276729

* Mon Nov 23 2015 Mat Booth <mat.booth@redhat.com> - 3.2-12
- Don't require optional stringtemplate dep in runtime OSGi metadata

* Wed Nov 18 2015 Mat Booth <mat.booth@redhat.com> - 3.2-11
- Workaround for rhbz#1276729

* Tue Nov 17 2015 Mat Booth <mat.booth@redhat.com> - 3.2-10
- Generate OSGi metadata for runtime jar

* Thu Jun 18 2015 Mat Booth <mat.booth@redhat.com> - 3.2-9
- Fix compat versions again (globs must be quoted)

* Wed Jun 17 2015 Mat Booth <mat.booth@redhat.com> - 3.2-8
- Non-bootstrap build

* Wed Jun 17 2015 Mat Booth <mat.booth@redhat.com> - 3.2-7
- Fix compat version of maven-plugin
- Rebootstrap

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 20 2014 Mat Booth <mat.booth@redhat.com> - 3.2-5
- Use mvn_compat_version macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Mat Booth <mat.booth@redhat.com> - 3.2-3
- Perform a non-bootstrap build

* Mon Jun 02 2014 Mat Booth <mat.booth@redhat.com> - 3.2-2
- Add link to source of back-ported patch

* Thu May 29 2014 Mat Booth <mat.booth@redhat.com> - 3.2-1
- Initial packaging of compatability version of antlr3
