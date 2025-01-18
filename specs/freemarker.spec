Name:           freemarker
Version:        2.3.31
Release:        15%{?dist}
Summary:        The Apache FreeMarker Template Engine
License:        Apache-2.0
URL:            https://freemarker.apache.org
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        http://archive.apache.org/dist/freemarker/engine/%{version}/source/apache-freemarker-%{version}-src.tar.gz
Source1:        http://archive.apache.org/dist/freemarker/engine/%{version}/source/apache-freemarker-%{version}-src.tar.gz.asc
Source2:        http://archive.apache.org/dist/freemarker/KEYS

# enable jdom extension
Patch0:         enable-jdom.patch
# Fix compatibility with javacc 7.0.12
Patch2:         90.patch

BuildRequires:  ant
BuildRequires:  gnupg2
BuildRequires:  ivy-local
BuildRequires:  java-1.8.0-openjdk
BuildRequires:  java-11-openjdk-devel
BuildRequires:  mvn(biz.aQute:bnd)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(dom4j:dom4j)
BuildRequires:  mvn(jakarta.el:jakarta.el-api)
BuildRequires:  mvn(javax.servlet:jsp-api)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(jaxen:jaxen)
BuildRequires:  mvn(jdom:jdom)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.javacc:javacc)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j)
BuildRequires:  mvn(org.slf4j:log4j-over-slf4j)
BuildRequires:  mvn(rhino:js)
BuildRequires:  mvn(xalan:xalan)

%description
Apache FreeMarker is a template engine: a Java library to generate text output
(HTML web pages, e-mails, configuration files, source code, etc.) based on
templates and changing data. Templates are written in the FreeMarker Template
Language (FTL), which is a simple, specialized language (not a full-blown
programming language like PHP).

%prep
%autosetup -p1 -n apache-%{name}-%{version}-src

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

find -type f '(' -name '*.jar' -o -iname '*.class' ')' -print -delete

# Use system ivy settings
rm ivysettings.xml

# Add jakarta.el-api
%pom_add_dep jakarta.el:jakarta.el-api:4.0.0

# Remove saxpath
%pom_remove_dep saxpath:saxpath

# Remove avalon-logkit
%pom_remove_dep avalon-logkit:avalon-logkit
rm src/main/java/freemarker/log/_AvalonLoggerFactory.java

# Remove javarebel-sdk
%pom_remove_dep org.zeroturnaround:javarebel-sdk
rm src/main/java/freemarker/ext/beans/JRebelClassChangeNotifier.java

# Remove jsp classes
rm src/main/java/freemarker/ext/jsp/FreeMarkerJspFactory2.java
rm src/main/java/freemarker/ext/jsp/_FreeMarkerPageContext2.java

# Remove jython:jython
%pom_remove_dep jython:jython
rm src/main/java/freemarker/ext/ant/UnlinkedJythonOperationsImpl.java
rm src/main/java/freemarker/ext/jython/JythonHashModel.java
rm src/main/java/freemarker/ext/jython/JythonModel.java
rm src/main/java/freemarker/ext/jython/JythonModelCache.java
rm src/main/java/freemarker/ext/jython/JythonNumberModel.java
rm src/main/java/freemarker/ext/jython/JythonSequenceModel.java
rm src/main/java/freemarker/ext/jython/JythonVersionAdapter.java
rm src/main/java/freemarker/ext/jython/JythonVersionAdapterHolder.java
rm src/main/java/freemarker/ext/jython/JythonWrapper.java
rm src/main/java/freemarker/ext/jython/_Jython20And21VersionAdapter.java
rm src/main/java/freemarker/template/utility/JythonRuntime.java

# Remove org.python:jython
%pom_remove_dep org.python:jython
rm src/main/java/freemarker/ext/jython/_Jython22VersionAdapter.java
rm src/main/java/freemarker/ext/jython/_Jython25VersionAdapter.java

%mvn_file : %{name}

%build
JAVA_HOME=%{_jvmdir}/java-11 ant \
  -Divy.mode=local \
  -Dsun.boot.class.path=%{_jvmdir}/jre-1.8.0/lib/rt.jar \
  jar maven-pom

%install
%mvn_artifact build/pom.xml build/freemarker.jar
%mvn_install

%files -f .mfiles
%doc README.md RELEASE-NOTES
%license LICENSE NOTICE

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.31-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.31-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 2.3.31-13
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.31-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 2.3.31-10
- migrate to SPDX license

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.31-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Apr  3 2023 Jerry James <loganjerry@gmail.com> - 2.3.31-8
- Add patch for javacc 7.0.12 compatibility

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.31-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.3.31-5
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.3.31-4
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 01 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 2.3.31-2
- Set JAVA_HOME to JDK11

* Mon Nov 22 2021 Didik Supriadi <didiksupriadi41@fedoraproject.org> - 2.3.31-1
- New upstream release 2.3.31

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jan 23 2021 Nicolas Lécureuil <neoclust@mageia.org> - 2.3.30-3
- Fix build using jakarta-el

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Mat Booth <mat.booth@redhat.com> - 2.3.30-1
- Update to latest upstream release
- Fixing to Java 8 due to requirement for Java 8 boot classpath; this should
  be ported to use the compiler release flag in the future

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.3.29-5
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Apr 01 2020 Mat Booth <mat.booth@redhat.com> - 2.3.29-4
- Rebuild for rawhide

* Tue Mar 24 2020 Mat Booth <mat.booth@redhat.com> - 2.3.29-3
- Fix source encoding for javadoc generation

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Fabio Valentini <decathorpe@gmail.com> - 2.3.29-1
- Update to version 2.3.29.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Mat Booth <mat.booth@redhat.com> - 2.3.28-3
- Allow conditionally building with a reduced dependency set

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 22 2018 Mat Booth <mat.booth@redhat.com> - 2.3.28-1
- Update to latest upstream release
- Drop unnecessary dep on saxpath and avalon

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 06 2017 Mat Booth <mat.booth@redhat.com> - 2.3.27-1
- Update to latest release, project moved to the Apache Foundation
- Drop unnecessary dep on findbugs
- Build against glassfish instead of jboss

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Michael Simacek <msimacek@redhat.com> - 2.3.23-4
- Fix compatibility with javacc 7

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Omair Majid <omajid@redhat.com> - 2.3.23-1
- Update to 2.3.23

* Thu Jul 02 2015 gil cattaneo <puntogil@libero.it> 2.3.19-11
- fix FTBFS
- adapt to current guideline
- fix some rpmlint problems
- enable javadoc task
- enable maven-upload task for generate pom file
- Fix paths to jython

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 09 2014 Omair Majid <omajid@redhat.com> - 2.3.19-9
- Use .mfiles to pick up xmvn metadata
- Don't use obsolete _mavendepmapfragdir macro
- Fix FTBFS issues

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 24 2014 Omair Majid <omajid@redhat.com> - 2.3.19-8
- Require java-headless

* Fri Oct 04 2013 Omair Majid <omajid@redhat.com> - 2.3.19-7
- Fix upstream Source URL for pom file

* Mon Aug 05 2013 Omair Majid <omajid@redhat.com> - 2.3.19-7
- Fix build dependencies

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 01 2012 Omair Majid <omajid@redhat.com> - 2.3.19-4
- Build remaining classes with target 6 too.
- Fixes RHBZ#842594

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 27 2012 Omair Majid <omajid@redhat.com> - 2.3.19-2
- Remove obsolete patches

* Tue Jun 05 2012 gil cattaneo <puntogil@libero.it - 2.3.19-2
- update patch for logging

* Thu May 31 2012 Omair Majid <omajid@redhat.com> - 2.3.19-1
- Add dependency on apache-commons-logging

* Wed May 16 2012 gil cattaneo <puntogil@libero.it> - 2.3.19-1
- update to 2.3.19

* Wed Feb 01 2012 Marek Goldmann <mgoldman@redhat.com> - 2.3.13-14
- Added Maven POM, RHBZ#786383

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 16 2011 Omair Majid <omajid@redhat.com> - 2.3.13-12
- Drop build dependency on struts
- Remove buildroot cleaning and definition
- Remove versioned jars
- Remove dependency of javadoc subpackage on main package

* Mon Feb 28 2011 Omair Majid <omajid@redhat.com> - 2.3.13-12
- Remove dependency on tomcat5

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.13-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 13 2010 Alexander Kurtakov <akurtako@redhat.com> 2.3.13-10
- Adapt to tomcat6-el jar rename.

* Mon Sep 13 2010 Alexander Kurtakov <akurtako@redhat.com> 2.3.13-9
- Add tomcat6-libs BR.
- Use global instead of define.

* Sat Feb 27 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.3.13-8
- fix build patch for use of the javacc 5.0
- patch for encoding
- disable brp-java-repack-jars

* Sat Feb 27 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.3.13-7
- patch for logging
- remove name from the summary

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 01 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.3.13-4
- Redundant dependency upon xerces-j2 is removed (#456276#c6)
- The dos2unix package is added as the build requirements
- The ant-nodeps build-time requirement is added

* Wed Aug 20 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.3.13-3
- The downloads.sourceforge.net host is used in the source URL
- %%{__install} and %%{__cp} are used everywhere
- %%defattr(-,root,root,-) is used everywhere

* Thu Aug 14 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.3.13-2
- Appropriate values of Group Tags are chosen from the official list
- Versions of java-devel & jpackage-utils are corrected
- Name of dir for javadoc is changed
- Manual is removed due to http://freemarker.org/docs/index.html

* Fri Jun 06 2008 Victor G. Vasilyev <victor.vasilyev@sun.com> 2.3.13-1
- Initial version
