%global parent  maven-doxia
%global subproj sitetools

Name:           %{parent}-%{subproj}
Version:        1.11.1
Release:        11%{?dist}
Summary:        Doxia content generation framework
License:        Apache-2.0
URL:            https://maven.apache.org/doxia/
VCS:            git:https://github.com/apache/maven-doxia-sitetools.git
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/doxia/doxia-sitetools/%{version}/doxia-%{subproj}-%{version}-source-release.zip
Source1:        https://repo1.maven.org/maven2/org/apache/maven/doxia/doxia-sitetools/%{version}/doxia-%{subproj}-%{version}-source-release.zip.asc
Source2:        https://downloads.apache.org/maven/KEYS

Patch1:         0002-Remove-dependency-on-velocity-tools.patch
# Adapt to recent versions of velocity
Patch2:         %{name}-velocity.patch

BuildRequires:  gnupg2
BuildRequires:  maven-local
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-core)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-logging-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-apt)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-fml)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-fo)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-markdown)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-xdoc)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-xhtml)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-module-xhtml5)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-i18n)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-velocity)
BuildRequires:  mvn(xalan:xalan)
BuildRequires:  mvn(xml-apis:xml-apis)

%description
Doxia is a content generation framework which aims to provide its
users with powerful techniques for generating static and dynamic
content. Doxia can be used to generate static sites in addition to
being incorporated into dynamic content generation systems like blogs,
wikis and content management systems.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup -p1 -n doxia-%{subproj}-%{version}

# migrate to maven 3
%pom_xpath_set //pom:mavenVersion 3.8.6 doxia-integration-tools
%pom_change_dep :maven-artifact-manager :maven-core doxia-integration-tools
%pom_change_dep :maven-project :maven-compat doxia-integration-tools

# complains
%pom_remove_plugin :apache-rat-plugin

%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin
%pom_remove_dep net.sourceforge.htmlunit:htmlunit doxia-site-renderer/pom.xml
%pom_remove_dep -r :velocity-tools

%pom_xpath_inject "pom:plugin[pom:artifactId[text()='modello-maven-plugin']]/pom:configuration" \
    "<useJava5>true</useJava5>" doxia-decoration-model

# There are two backends for generating PDFs: one based on iText and
# one using FOP.  iText module is broken and only brings additional
# dependencies.  Besides that upstream admits that iText support will
# likely removed in future versions of Doxia.  In Fedora we remove
# iText backend sooner in order to fix dependency problems.
#
# See also: http://maven.apache.org/doxia/faq.html#How_to_export_in_PDF
# http://lists.fedoraproject.org/pipermail/java-devel/2013-April/004742.html
rm -rf $(find -type d -name itext)
%pom_remove_dep -r :doxia-module-itext

%mvn_alias :doxia-integration-tools org.apache.maven.shared:maven-doxia-tools

%build
# tests can't run because of missing deps
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.11.1-10
- Rebuilt for java-21-openjdk as system jdk

* Fri Jan 26 2024 Jerry James <loganjerry@gmail.com> - 1.11.1-9
- Adapt to plexus-velocity 2.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 30 2023 Jerry James <loganjerry@gmail.com> - 1.11.1-7
- Enable markdown support
- Adapt to recent versions of velocity

* Wed Jul 19 2023 Jerry James <loganjerry@gmail.com> - 1.11.1-6
- Enable fop support

* Sat Jun 10 2023 Jerry James <loganjerry@gmail.com> - 1.11.1-5
- Remove maven 2 dependencies

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Jerry James <loganjerry@gmail.com> - 1.11.1-3
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.11.1-2
- Rebuilt for Drop i686 JDKs

* Wed Jun  8 2022 Jerry James <loganjerry@gmail.com> - 1.11.1-1
- Version 1.11.1
- Drop upstreamed plexus-utils patch
- Drop old obsoletes
- Verify sources with gpg
- Minor spec file cleanups

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.9.2-7
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.9.2-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Mar 02 2020 Fabio Valentini <decathorpe@gmail.com> - 1.9.2-1
- Update to version 1.9.2.
- Convert patches to unix line endings (following upstream sources).
- Switch to HTTPS URL for sources.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Fabio Valentini <decathorpe@gmail.com> - 1.9.1-2
- Disable fop support.

* Mon Sep 02 2019 Marian Koncek <mkoncek@redhat.com> - 1.9.1-1
- Update to upstream version 1.9.1

* Mon Sep 02 2019 Fabio Valentini <decathorpe@gmail.com> - 1.7.5-6
- Disable support for markdown.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 23 2017 Michael Simacek <msimacek@redhat.com> - 1.7.5-1
- Update to upstream version 1.7.5

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 07 2017 Michael Simacek <msimacek@redhat.com> - 1.7.4-3
- Add conditionals for fop and markdown

* Mon Feb 06 2017 Michael Simacek <msimacek@redhat.com> - 1.7.4-2
- Remove dependency on velocity-tools

* Mon Nov 14 2016 Michael Simacek <msimacek@redhat.com> - 1.7.4-1
- Update to upstream version 1.7.4

* Wed Nov 09 2016 Michael Simacek <msimacek@redhat.com> - 1.7.3-1
- Update to upstream version 1.7.3

* Wed Nov 02 2016 Michael Simacek <msimacek@redhat.com> - 1.7.2-1
- Update to upstream version 1.7.2

* Thu May 12 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.7.1-3
- Port to plexus-utils 3.0.24

* Thu May 05 2016 Michael Simacek <msimacek@redhat.com> - 1.7.1-2
- Add Provides and Obsoletes for maven-doxia-tools

* Wed May 04 2016 Michael Simacek <msimacek@redhat.com> - 1.7.1-1
- Update to upstream version 1.7.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.6-1
- Update to upstream version 1.6

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.4-5
- Use Requires: java-headless rebuild (#1067528)

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-4
- Fix unowned directory

* Tue Oct  1 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-3
- Add missing build dependencies

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Michal Srb <msrb@redhat.com> - 1.4-1
- Update to upstream version 1.4
- Remove unneeded patch

* Tue Apr  9 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-4
- Fix BuildRequires

* Tue Apr  9 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-3
- Remove iText PDF backend

* Tue Apr 09 2013 Michal Srb <msrb@redhat.com>
- Remove dependency on velocity-tools

* Wed Feb 06 2013 Michal Srb <msrb@redhat.com> - 1.3-1
- Update to upstream version 1.3
- Migrate from maven-doxia to doxia subpackages (#889145)
- Build with xmvn
- Replace patches with pom_ macros
- Remove unnecessary depmap

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Nov 28 2012 Tomas Radej <tradej@redhat.com> - 1.2-5
- Removed (B)R on plexus-container-default

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 27 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2-3
- Remove dependency on plexux-xmlrpc
- Add BR/R on java 1.7.0+

* Mon Jan 09 2012 Jaromir Capik <jcapik@redhat.com> - 1.2-2
- Migration from plexus-maven-plugin to plexus-containers-component-metadata
- Minor spec file changes according to the latest guidelines

* Fri May  6 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2-1
- Update to latest version (1.2)
- Use maven 3 to build
- Remove version limits on BR/R (not valid anymore anyway)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Alexander Kurtakov <akurtako@redhat.com> 1.1.3-2
- Adapt to current guidelines.

* Tue Sep  7 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.1.3-1
- Update to 1.1.3
- Enable javadoc generation again
- Update maven plugins BRs
- Make dependency on maven-doxia unversioned

* Thu Jun 17 2010 Deepak Bhole <dbhole@redhat.com> - 0:1.1.2-3
- Rebuild with maven 2.2.1
- Remove modello 1.0 patch

* Wed May  5 2010 Mary Ellen Foster <mefoster at gmail.com> 0:1.1.2-2
- Add (Build)Requirement maven-shared-reporting-impl,
  plexus-containers-container-default, jakarta-commons-configuration

* Fri Feb 12 2010 Mary Ellen Foster <mefoster at gmail.com> 0:1.1.2-1
- Update to 1.1.2
- Temporarily disable javadoc until maven2-plugin-javadoc is rebuilt against
  the new doxia

* Mon Dec 21 2009 Alexander Kurtakov <akurtako@redhat.com> 1.0-0.2.a10.2
- BR maven-surefire-provider-junit.

* Tue Sep 01 2009 Andrew Overholt <overholt@redhat.com> 1.0-0.2.a10.1
- Add itext, tomcat5, and tomcat5-servlet-2.4-api BRs

* Fri Aug 28 2009 Andrew Overholt <overholt@redhat.com> 1.0-0.2.a10
- First Fedora build

* Fri Jun 20 2000 Deepak Bhole <dbhole@redhat.com> 1.0-0.1.a10.0jpp.1
- Initial build
