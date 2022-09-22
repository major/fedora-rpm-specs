Name:           buildnumber-maven-plugin
Version:        1.3
Release:        23%{?dist}
Summary:        Build Number Maven Plugin
License:        MIT and ASL 2.0
URL:            http://svn.codehaus.org/mojo/tags/buildnumber-maven-plugin-%{version}
BuildArch: 	noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        http://central.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0:         00-remove-broken-build-config.patch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven:maven-settings:2.0.6)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-api)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-manager-plexus)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-bazaar)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-clearcase)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-cvsexe)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-gitexe)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-hg)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-perforce)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-starteam)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-svn-commons)
BuildRequires:  mvn(org.apache.maven.scm:maven-scm-provider-svnexe)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

%description
This mojo is designed to get a unique build number for each time you build
your project. So while your version may remain constant at 1.0-SNAPSHOT
for many iterations until release, you will have a build number that can
uniquely identify each build during that time. The build number is obtained
from scm, and in particular, at this time, from svn. You can then place that
build number in metadata, which can be accessed from your app, if desired.

The mojo also has a couple of extra functions to ensure you get the proper
build number. First, your local repository is checked to make sure it is
up to date. Second, your local repository is automatically updated, so that
you get the latest build number. Both these functions can be suppressed,
if desired.

Optionally, you can configure this mojo to produce a revision based on a
timestamp, or on a sequence, without requiring any interaction with an
SCM system. Note that currently, the only supported SCM is subversion.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1

cp -p %{SOURCE1} .

%pom_remove_dep com.google.code.maven-scm-provider-svnjava:maven-scm-provider-svnjava
%pom_remove_dep org.tmatesoft.svnkit:svnkit
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-invoker-plugin

# junit dependency was removed in Plexus 1.6
%pom_add_dep junit:junit::test

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt LICENSE-2.0.txt

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.3-22
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.3-21
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Fabio Valentini <decathorpe@gmail.com> - 1.3-16
- Set javac source and target to 1.8 to fix Java 11 builds.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.3-15
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.3-10
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-6
- Regenerate build-requires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-3
- Remove unneeded BR on cobertura-maven-plugin

* Wed Mar 11 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3-2
- Add test dependency on junit

* Fri Jun 13 2014 Alexander Kurtakov <akurtako@redhat.com> 1.3-1
- Update to upstream 1.3 release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2-7
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 24 2013 Mat Booth <fedora@matbooth.co.uk> - 1.2-6
- Remove unneeded BR on maven2-common-poms

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-4
- Remove unneeded BR: maven-idea-plugin

* Thu Feb 28 2013 Weinan Li <weli@redhat.com> - 1.2-3
- remove unnecessary maven-doxia dependencies

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.2-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 29 2013 David Xie <david.scriptfan@gmail.com> - 1.2-1
- Upgrade to 1.2

* Thu Aug 16 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-2
- Install ASL 2.0 license
- Remove rpm bug workaround

* Wed Jul 25 2012 Tomas Radej <tradej@redhat.com> - 1.1-1
- Updated to latest upstream version
- Replaced patches with pom macros

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-5
- Remove dependency on svnkit

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 30 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-3
- Add missing (Build)Requires
- Use new add_maven_depmap macro

* Wed Jun 8 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0-2
- Do not require maven2.
- Guidelines fixes.

* Mon Apr 18 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-1
- Update to latest upstream
- Build with maven 3
- Tweaks according to new guidelines
- Versionless jars & javadocs

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.11.b4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 11 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-0.10.b4
- Added mojo-parent to BR/R

* Wed Sep 1 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-0.9.b4
- Fix build and use new maven plugins names.

* Thu Jun 17 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-0.8.b4
- BR maven2-common-poms.

* Thu Jun 17 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-0.7.b4
- Disable it-tests and changes plugin.

* Thu Jun 17 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-0.6.b4
- Skip tests to be able to rebuild.

* Thu Jun 17 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0-0.5.b4
- Add missing requires.

* Thu May 27 2010 Weinan Li <weli@redhat.com> - 1.0-0.4.b4
- License.txt and Readme.txt added as %%doc

* Thu May 27 2010 Weinan Li <weli@redhat.com> - 1.0-0.3.b4
- Fix javadoc dangling-relative-symlink

* Wed May 26 2010 Weinan Li <weli@redhat.com> - 1.0-0.2.b4
- Add requires on jpackage-utils for javadoc subpackage
- Add standard jpackage-utils requires on main package
- Use global instead of define
- Fix license to MIT
- fix incoherent-version-in-changelog

* Mon May 24 2010 Weinan Li <weli@redhat.com> - 1.0-0.1.b4
- Initial package
