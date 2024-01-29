# The version of Subversion that we are compatible with
%global svn_version 1.8.1

Epoch:   1
Name:    svnkit
Version: 1.8.12
Release: 18%{?dist}
Summary: Pure Java library to manage Subversion working copies and repositories

# License located at https://svnkit.com/license.html
License:        TMate and ASL 2.0
URL:            https://www.svnkit.com/
Source0:        https://www.svnkit.com/org.tmatesoft.svn_%{version}.src.zip

# POMs
Source1:        https://repo1.maven.org/maven2/org/tmatesoft/svnkit/svnkit/%{version}/svnkit-%{version}.pom
Source2:        https://repo1.maven.org/maven2/org/tmatesoft/svnkit/svnkit-cli/%{version}/svnkit-cli-%{version}.pom
Source3:        https://repo1.maven.org/maven2/org/tmatesoft/svnkit/svnkit-javahl16/%{version}/svnkit-javahl16-%{version}.pom

# Custom aggregator pom to avoid reliance on gradle
Source4:        svnkit-parent.pom

# SVNKit provides a pure-Java implementation of the Subversion JavaHL API, but it only provides an older
# Subversion JavaHL API, so we need an old version of the JavaHL source to build against. This is that:
#  $ svn export https://svn.apache.org/repos/asf/subversion/tags/1.8.1/subversion/bindings/javahl/src/ javahl-1.8.1
Source5:        javahl-%{svn_version}.tar.gz

# License for the above JavaHL API:
Source6:        https://www.apache.org/licenses/LICENSE-2.0.txt

# svnkit's trilead-ssh2 does not throw InterruptedException from Session.waitForCondition()
# Fedora's trilead-ssh2 does ...
Patch1:         svnkit-1.8.5-SshSession-unreported-exception.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.jcraft:jsch.agentproxy.connector-factory)
BuildRequires:  mvn(com.jcraft:jsch.agentproxy.svnkit-trilead-ssh2)
BuildRequires:  mvn(com.trilead:trilead-ssh2)
BuildRequires:  mvn(de.regnis.q.sequence:sequence-library)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(net.java.dev.jna:jna-platform)
BuildRequires:  mvn(org.tmatesoft.sqljet:sqljet)

%description
SVNKit is a pure java Subversion client library. You would like to use SVNKit
when you need to access or modify Subversion repository from your Java
application, as a standalone program and plugin or web application. Being a
pure java program, SVNKit doesn't need any additional configuration or native
binaries to work on any OS that runs java.

%package cli
Summary: SVNKit based Subversion command line client
# Explicit requires for javapackages-tools since scripts
# use /usr/share/java-utils/java-functions
Requires:       javapackages-tools

%description cli
%{summary}.

%package javahl
Summary: SVNKit based Subversion JavaHL API implementation

%description javahl
%{summary}.

%package javadoc
Summary: Javadoc for SVNKit

%description javadoc
API documentation for SVNKit.

%prep
%setup -q -n %{name}-%{version}

%patch1 -p1

# Delete all pre-built binaries, except for "template.jar" which is important
# for the function of svnkit and contains no actual bytecode:
find -name *.class -delete
find -name *.jar -a ! -name template.jar -delete

cp -pr %{SOURCE1} svnkit/pom.xml
cp -pr %{SOURCE2} svnkit-cli/pom.xml
cp -pr %{SOURCE3} svnkit-javahl16/pom.xml
cp -pr %{SOURCE4} pom.xml

# Build against the bundled version of the JavaHL API source
cp -pr %{SOURCE6} ASL-2.0.txt
(cd svnkit-javahl16/src/main/java/ &&  tar xf %{SOURCE5} --strip-components=1 --skip-old-files)
%pom_remove_dep ":svn-javahl-api" svnkit-javahl16
%pom_remove_dep ":svn-javahl-tests" svnkit-javahl16

# Generate properties file
rev="t$(date -u +%Y%m%d%H%M)"
cat > svnkit/src/main/resources/svnkit.build.properties <<EOF
svnkit.version=%{version}
build.number=$rev

svnkit.version.string=SVN/%{svn_version} SVNKit/%{version} (http://svnkit.com/) $rev
svnkit.version.major=$(echo "%{version}" | cut -f1 -d.)
svnkit.version.minor=$(echo "%{version}" | cut -f2 -d.)
svnkit.version.micro=$(echo "%{version}" | cut -f3 -d.)
svnkit.version.revision=$rev

svnkit.svn.version=%{svn_version}
EOF

# Don't install our custom aggregator pom
%mvn_package ":parent" __noinstall

%build
# Upstream builds with ignore test failures set to true, so I guess we shouldn't expect them to work...
# Let's skip tests for now.
%mvn_build -s -f -- -Dproject.buildVersion.baseVersion=%{version} \
  -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dsource=1.8 -DdetectJavaApiLink=false

%install
%mvn_install

# Generate scripts for command line tools
for class in SVN SVNAdmin SVNDumpFilter SVNLook SVNSync SVNVersion ; do
  mainclass=org.tmatesoft.svn.cli.$class
  script=j$(echo $class | tr '[:upper:]' '[:lower:]')
  %jpackage_script "$mainclass" "-Dsun.io.useCanonCaches=false" "" "svnkit:sequence-library:sqljet:antlr32/antlr-runtime-3.2:trilead-ssh2" "$script" true
done

%files -f .mfiles-svnkit
%license LICENSE.txt ASL-2.0.txt
%doc README.txt CHANGES.txt

%files cli -f .mfiles-svnkit-cli
%{_bindir}/*

%files javahl -f .mfiles-svnkit-javahl16

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt ASL-2.0.txt

%changelog
* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.12-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1:1.8.12-14
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1:1.8.12-13
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Mat Booth <mat.booth@redhat.com> - 1:1.8.12-8
- Use https for maven central URLs

* Mon Jul 13 2020 Mat Booth <mat.booth@redhat.com> - 1:1.8.12-7
- Fix javadoc generation when building against JDK 11
- Install ASL 2.0 license

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 22 2018 Mat Booth <mat.booth@redhat.com> - 1:1.8.12-5
- Rebuild for rawhide

* Fri Aug 31 2018 Severin Gehwolf <sgehwolf@redhat.com> - 1:1.8.12-4
- Add explicit javapackages-tools requirement to -cli sub-package
  for scripts using java-functions. See RHBZ#1600426.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.8.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr 13 2018 Mat Booth <mat.booth@redhat.com> - 1:1.8.12-2
- Allow svnkit to be invoked from the command line

* Fri Apr 13 2018 Mat Booth <mat.booth@redhat.com> - 1:1.8.12-1
- Revert to slightly older version due to problems reading the status of working
  copies

* Thu Apr 12 2018 Mat Booth <mat.booth@redhat.com> - 1.8.15-3
- Build javahl API against correct version of javahl sources

* Thu Apr 12 2018 Mat Booth <mat.booth@redhat.com> - 1.8.15-2
- Fix display of version numbers
- Allow building pure-java JavaHL implementation without the presence of
  Subversion

* Wed Mar 21 2018 Mat Booth <mat.booth@redhat.com> - 1.8.15-1
- Update to 1.8.15 release
- Modernise spec file
- Fix failure to build from source
- Conditionally build the javahl module

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Ismael Olea <ismael@olea.org> - 1.8.5-2
- the tomcat servlet api dep is now tomcat-servlet-3.1-api

* Wed Jun 11 2014 Jakub Filak <jfilak@redhat.com> - 1.8.5-1
- Updated to 1.8.5

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 16 2013 Tom Callaway <spot@fedoraproject.org> - 1.7.6-7
- fix pom file for proper naming for trilead-ssh2

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild


* Mon Dec 17 2012 Ismael Olea <ismael@olea.org> - 1.7.6-5
- Code auditing reports all used source code is TMate licensed only
  so license changed
- Added an ASL 1.1 license file obligued by nailgun
- Renamed ASL licenses file names with canonical source URIs

* Mon Dec 17 2012 Ismael Olea <ismael@olea.org> - 1.7.6-4
- better upstream URI for pom file
- better script for detecting non allowed binary artifacts
- removed innecesary duplicated license files
- spec cleaning

* Wed Dec 12 2012 Ismael Olea <ismael@olea.org> - 1.7.6-3
- added a LCENSE-2.0.txt just in SRPM due to nailgun.jar be included in svnkit sources
- minor spec cleaning

* Fri Dec 7 2012 Ismael Olea <ismael@olea.org> - 1.7.6-2
- removed all eclipse-isms and spec cleaning

* Mon Dec 3 2012 Ismael Olea <ismael@olea.org> - 1.7.6-1
- updated to 1.7.6

* Mon Dec 3 2012 Ismael Olea <ismael@olea.org> - 1.7.5-6
- svnkit-jna-3.5.0.patch from Brendan Jones to ride with jna API changes

* Tue Nov 20 2012 Ismael Olea <ismael@olea.org> - 1.7.5-5
- missing dep tomcat-servlet-3.0-api
- stetic changes

* Fri Nov 16 2012 Ismael Olea <ismael@olea.org> - 1.7.5-4
- cleaning mavem-isms
- removing the obsoletes javasvn since it's not in Fedora since F9
- minor spec cleaning

* Tue Oct 9 2012 Ismael Olea <ismael@olea.org> - 1.7.5-3
- fixing build.xml paths

* Sat Oct 6 2012 Ismael Olea <ismael@olea.org> - 1.7.5-2
- adding javadoc
- beautifing build.xml

* Fri Oct 5 2012 Ismael Olea <ismael@olea.org> - 1.7.5-1
- update to 1.7.5-v1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Alexander Kurtakov <akurtako@redhat.com> 1.3.5-1
- Update to upstream 1.3.5.

* Mon Dec 13 2010 Alexander Kurtakov <akurtako@redhat.com> 1.3.4-2
- Fix pom name.
- Adapt to current guidelines.

* Thu Oct 21 2010 Alexander Kurtakov <akurtako@redhat.com> 1.3.4-1
- Update to new upstream 1.3.4.

* Wed Jul 21 2010 Alexander Kurtakov <akurtako@redhat.com> 1.3.3-5
- Add maven depmap and pom.
- Separate javahl in a subpackage.

* Fri Jul 16 2010 Alexander Kurtakov <akurtako@redhat.com> 1.3.3-4
- Move eclipse-platform dependency to the eclipse subpackage.

* Tue Jul 13 2010 Alexander Kurtakov <akurtako@redhat.com> 1.3.3-3
- Fix antlr3 jar rename.

* Tue Jul 13 2010 Alexander Kurtakov <akurtako@redhat.com> 1.3.3-2
- BR antlr3-java.

* Tue Jul 13 2010 Alexander Kurtakov <akurtako@redhat.com> 1.3.3-1
- Update to 1.3.3.
- Patch1 is not applied it looks like fixed upstream in different way.

* Fri Mar 05 2010 Lubomir Rintel <lkundrak@v3.sk> 1.3.2-2
- Cherry-pick r6418 from upstream

* Thu Dec 3 2009 Alexander Kurtakov <akurtako@redhat.com> 1.3.2-1
- Update to 1.3.2.

* Fri Jul 24 2009 Alexander Kurtakov <akurtako@redhat.com> 1.3.0-1
- Update to 1.3.0.

* Mon Apr  6 2009 Robert Marcano <robert@marcanoonline.com> - 1.2.3-2
- Rebuild

* Mon Mar 23 2009 Robert Marcano <robert@marcanoonline.com> - 1.2.3-1
- Update to upstream 1.2.3

* Tue Feb 17 2009 Robert Marcano <robert@marcanoonline.com> - 1.2.2-1
- Update to upstream 1.2.2
- New eclipse-svnkit subpackage with eclipse plugin
- GCJ AOT removed

* Sun Sep  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.1.4-4
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.1.4-3
- Autorebuild for GCC 4.3

* Thu Sep 20 2007 Robert Marcano <robert@marcanoonline.com> - 1.1.4-2
- Fix Obsoletes to include javasvn = 1.1.0

* Mon Sep 10 2007 Robert Marcano <robert@marcanoonline.com> - 1.1.4-1
- Update to upstream 1.1.4
- Build for all supported arquitectures 

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.1.2-4
- Rebuild for selinux ppc32 issue.

* Mon Jun 18 2007 Robert Marcano <robert@marcanoonline.com> 1.1.2-2
- Package review fixes

* Sun Apr 15 2007 Robert Marcano <robert@marcanoonline.com> 1.1.2-1
- Update to upstream 1.1.2
- Add obsoletes of javasvn

* Tue Feb 06 2007 Robert Marcano <robert@marcanoonline.com> 1.1.1-1
- Rename to svnkit
- Update to SVNKit 1.1.1

* Mon Aug 28 2006 Robert Marcano <robert@marcanoonline.com> 1.1.0-0.3.beta4
- Rebuild

* Thu Aug 03 2006 Robert Marcano <robert@marcanoonline.com> 1.1.0-0.2.beta4
- Fix bad relase tag

* Mon Jul 31 2006 Robert Marcano <robert@marcanoonline.com> 1.1.0-0.beta4
- Update to upstream version 1.1.0.beta4, required by subclipse 1.1.4

* Fri Jul 28 2006 Robert Marcano <robert@marcanoonline.com> 1.0.6-2
- Rebuilt to pick up the changes in GCJ (bug #200490)

* Mon Jun 26 2006 Robert Marcano <robert@marcanoonline.com> 1.0.6-1
- Update to upstream version 1.0.6

* Sun Jun 25 2006 Robert Marcano <robert@marcanoonline.com> 1.0.4-4
- created javadoc subpackage
- dependency changed from ganymed to ganymed-ssh2

* Sun Jun 11 2006 Robert Marcano <robert@marcanoonline.com> 1.0.4-3
- rpmlint fixes and debuginfo generation workaround
- doc files added

* Sun May 28 2006 Robert Marcano <robert@marcanoonline.com> 1.0.4-2
- review updates

* Sun May 07 2006 Robert Marcano <robert@marcanoonline.com> 1.0.4-1
- initial version
