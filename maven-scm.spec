# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Name:           maven-scm
Version:        1.10.0
Release:        16%{?dist}
Summary:        Common API for doing SCM operations
License:        ASL 2.0
URL:            http://maven.apache.org/scm
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        http://archive.apache.org/dist/maven/scm/%{name}-%{version}-source-release.zip

# Patch to migrate to new plexus default container
# This has been sent upstream: https://issues.apache.org/jira/browse/SCM-731
Patch1:         0001-Port-maven-scm-to-latest-version-of-plexus-default.patch
# Workaround upstream's workaround for a modello bug, see: https://issues.apache.org/jira/browse/SCM-518
Patch2:         0002-Fix-vss-modello-config.patch
Patch3:         0003-Port-to-current-plexus-utils.patch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-settings:2.2.1)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.shared:file-management)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.jgit:org.eclipse.jgit)
BuildRequires:  mvn(org.sonatype.plexus:plexus-sec-dispatcher)

%description
Maven SCM supports Maven plugins (e.g. maven-release-plugin) and other
tools (e.g. Continuum) in providing them a common API for doing SCM operations.

%package test
Summary:        Tests for %{name}
Requires:       maven-scm = %{version}-%{release}

%description test
Tests for %{name}.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3 -p1

# Remove unnecessary animal sniffer
%pom_remove_plugin org.codehaus.mojo:animal-sniffer-maven-plugin

%pom_remove_plugin :maven-enforcer-plugin

%pom_change_dep -r :maven-project :maven-compat

# Remove providers-integrity from build (we don't have mks-api)
%pom_remove_dep org.apache.maven.scm:maven-scm-provider-integrity maven-scm-providers/maven-scm-providers-standard
%pom_disable_module maven-scm-provider-integrity maven-scm-providers

# Partially remove cvs support for removal of netbeans-cvsclient
# It still works with cvsexe provider
%pom_remove_dep org.apache.maven.scm:maven-scm-provider-cvsjava maven-scm-client
%pom_remove_dep org.apache.maven.scm:maven-scm-provider-cvsjava maven-scm-providers/maven-scm-providers-standard
%pom_disable_module maven-scm-provider-cvsjava maven-scm-providers/maven-scm-providers-cvs
sed -i s/cvsjava.CvsJava/cvsexe.CvsExe/ maven-scm-client/src/main/resources/META-INF/plexus/components.xml

# Port to commons-lang3
%pom_change_dep -r :commons-lang org.apache.commons:commons-lang3:3.8.1
sed -i "s/org\.apache\.commons\.lang\./org.apache.commons.lang3./" \
    maven-scm-providers/maven-scm-providers-git/maven-scm-provider-gitexe/src/main/java/org/apache/maven/scm/provider/git/gitexe/command/status/GitStatusConsumer.java \
    maven-scm-providers/maven-scm-providers-svn/maven-scm-provider-svnexe/src/main/java/org/apache/maven/scm/provider/svn/svnexe/command/checkout/SvnCheckOutConsumer.java \
    maven-scm-providers/maven-scm-providers-svn/maven-scm-provider-svnexe/src/main/java/org/apache/maven/scm/provider/svn/svnexe/command/remoteinfo/SvnRemoteInfoCommand.java

# Tests are skipped anyways, so remove dependency on mockito.
%pom_remove_dep org.mockito: maven-scm-providers/maven-scm-provider-jazz
%pom_remove_dep org.mockito: maven-scm-providers/maven-scm-provider-accurev

# Don't use deprecated "descriptorId" configuration parameter of Maven
# Assembly Plugin, which was removed in version 3.0.0.
%pom_xpath_replace "pom:plugin[pom:artifactId='maven-assembly-plugin']/pom:configuration/pom:descriptorId" "
    <descriptorRefs>
      <descriptorRef>jar-with-dependencies</descriptorRef>
    </descriptorRefs>" maven-scm-client

# Put TCK tests into a separate sub-package
%mvn_package :%{name}-provider-cvstest test
%mvn_package :%{name}-provider-gittest test
%mvn_package :%{name}-provider-svntest test
%mvn_package :%{name}-test test

%build
# Don't build and unit run tests because
# * accurev tests need porting to a newer hamcrest
# * vss tests fail with the version of junit in fedora
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files test -f .mfiles-test
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.10.0-14
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.10.0-13
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug 13 2020 Fabio Valentini <decathorpe@gmail.com> - 1.10.0-9
- Port to apache commons-lang3.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.10.0-7
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Michael Simacek <msimacek@redhat.com> - 1.10.0-2
- Port to current plexus-utils

* Wed Jun 27 2018 Michael Simacek <msimacek@redhat.com> - 1.10.0-1
- Update to upstream version 1.10.0

* Thu Mar 15 2018 Michael Simacek <msimacek@redhat.com> - 1.9.5-6
- Fix FTBFS - remove enforcer

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 17 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.5-2
- Don't use deprecated config parameter of maven-assembly-plugin

* Fri Aug 12 2016 Michael Simacek <msimacek@redhat.com> - 1.9.5-1
- Update to upstream version 1.9.5

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.4-5
- Regenerate build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.4-3
- Add patch for compatibility with JGit 4.0.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr  2 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.4-1
- Update to upstream version 1.9.4

* Fri Nov 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.2-2
- Add missing dependency on JUnit (SCM-786)

* Wed Sep 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.2-1
- Update to upstream version 1.9.2

* Mon Jul 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.1-1
- Update to upstream version 1.9.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Michael Simacek <msimacek@redhat.com> - 1.9-3
- Drop manual requires

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.9-2
- Use Requires: java-headless rebuild (#1067528)

* Wed Jan  8 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9-1
- Update to upstream version 1.9

* Tue Aug 27 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-2
- Remove BR: mockito

* Sun Aug 25 2013 Mat Booth <fedora@matbooth.co.uk> - 1.8.1-1
- Fix removal of cvs java provider, rhbz #962273
- Update to latest upstream
- Drop upstreamed patches

* Sat Aug 24 2013 Mat Booth <fedora@matbooth.co.uk> - 1.7-10
- Remove use of deprecated macros, rhbz #992204
- Don't ship test jars in main package
- Install NOTICE file

* Sat Aug 24 2013 Mat Booth <fedora@matbooth.co.uk> - 1.7-9
- Add patch to build against newer plexus default container, rhbz #996199
- Drop unneeded BRs

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-7
- Remove BR: maven2-common-poms

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-7
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.7-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Nov 15 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7-4
- Install LICENSE file

* Tue Aug 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.7-3
- Remove unneeded mockito build dependency
- Use new pom_ macros instead of patches

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Tomas Radej <tradej@redhat.com> - 1.7-1
- Updated to latest upstream version
- plexus-maven-plugin -> plexus-component-metadata

* Mon Apr 23 2012 Guido Grazioli <guido.grazioli@gmail.com> - 1.6-3
- Fix typo

* Mon Apr 23 2012 Guido Grazioli <guido.grazioli@gmail.com> - 1.6-2
- Remove -client-with-dependencies jar to get rid of duplicate libraries
- Switch off maven execution debug output

* Mon Apr 09 2012 Guido Grazioli <guido.grazioli@gmail.com> - 1.6-1
- Update to 1.6 release
- Fix typo in description
- Remove unused patches 001 (mockito now available), 004 and 006
- Update patch 007 (plexus-containers-component-metadata)
- Move source encoding setting to separate patch

* Fri Feb  3 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.5-5
- Remove cvsjava provider to get rid of netbeans-cvsclient dep

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 18 2011 Bruno Wolff III <bruno@wolff.to> 1.5-3
- Fix issue with bad requires by maven-scm-test

* Tue Nov 15 2011 Jaromir Capik <jcapik@redhat.com> 1.5-2
- Migration from plexus-maven-plugin to plexus-containers-component-metadata

* Tue Apr 5 2011 Alexander Kurtakov <akurtako@redhat.com> 0:1.5-1
- Update to upstream 1.5 release.
- Build with maven 3.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 11 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.4-5
- Drop buildroot definition
- Use mavenpomdir macro
- Make jars versionless (for real)

* Mon Jan 3 2011 Alexander Kurtakov <akurtako@redhat.com> 0:1.4-4
- Drop tomcat BRs.
- No more versioned jar and javadoc.

* Wed Sep 08 2010 Guido Grazioli <guido.grazioli@gmail.com> 0:1.4-2
- Fix BR
- Remove unused patch

* Tue Sep 07 2010 Guido Grazioli <guido.grazioli@gmail.com> 0:1.4-1
- Update to upstream 1.4 (#626455)
- Require netbeans-cvsclient instead of netbeans-ide (#572165)

* Mon May 10 2010 Guido Grazioli <guido.grazioli@gmail.com> 0:1.2-6
- Link netbeans-lib-cvsclient jar in the right place.
- Switch to xz compression.
- Sanitize files owned.
- Use %%global.

* Mon Feb 8 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.2-5
- Fix BR/Rs for netbeans-ide[version] to netbeans-ide rename.

* Thu Sep 17 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.2-4
- Fix maven-scm-plugin depmap.

* Sat Sep 12 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.2-3
- BR maven-surefire-provider-junit.
- BR plexus-maven-plugin.
- BR maven2-plugin-assembly.

* Sat Sep 12 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.2-2
- Add doxia-sitetools BR.

* Sat Sep 12 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.2-1
- Update to upstream 1.2.

* Tue Sep 01 2009 Andrew Overholt <overholt@redhat.com> 1.0-0.5.rc1.2
- Bump release

* Tue Sep 01 2009 Andrew Overholt <overholt@redhat.com> 1.0-0.5.rc1.1
- Add tomcat5, tomcat5-servlet-2.4-api,
  maven-shared-plugin-testing-harness, and tomcat5-jsp-2.0-api BRs

* Mon Aug 31 2009 Andrew Overholt <overholt@redhat.com> 1.0-0.5.rc1
- 1.0 RC1 (courtesy Deepak Bhole)
- Remove gcj support
- Add netbeans-ide11 requirement
- Change name on surefire plugin BR

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.4.b3.1.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 23 2009 Deepak Bhole <dbhole@redhat.com> - 0:1.0-0.3.b3.1.7
- Remove ppc64 arch exclusion

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0-0.3.b3.1.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.0-0.2.b3.1.6
- drop repotag

* Thu Jun 26 2008 Deepak Bhole <dbhole@redhat.com> 1.0-0.2.b3.1jpp.5
- Fix mapping for the scm plugin

* Thu May 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.0-0.2.b3.1jpp.4
- fix license tag

* Thu Feb 28 2008 Deepak Bhole <dbhole@redhat.com> 1.0-0.2.b3.1jpp.3
- Rebuild

* Fri Sep 21 2007 Deepak Bhole <dbhole@redhat.com> 0:1.0-0.1.b3.2jpp.2
- Rebuild with excludearch for ppc64

* Tue Feb 27 2007 Tania Bento <tbento@redhat.com> 0:1.0-0.1.b3.2jpp.1
- Fixed %%Release.
- Fixed %%BuildRoot.
- Removed %%Vendor.
- Removed %%Distribution.
- Removed %%post and %%postun sections for javadoc.
- Fixed instructions on how to generate source drop.
- Marked documentation files as %%doc in %%files section.
- Fixed %%Summary.
- Fixed %%description.

* Tue Oct 17 2006 Deepak Bhole <dbhole@redhat.com> - 0:1.0-0.b3.2jpp
- Update for maven 9jpp.

* Tue Sep 18 2006 Deepak Bhole <dbhole@redhat.com> - 0:1.0-0.b3.1jpp
- Initial build
