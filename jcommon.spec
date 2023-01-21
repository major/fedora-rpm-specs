Name: jcommon
Version: 1.0.23
Release: 25%{?dist}
Summary: JFree Java utility classes
License: LGPLv2+
# Github: https://github.com/jfree/jcommon
# There are no tags which we can use to get sources. See:
#   https://github.com/jfree/jcommon/issues/1
# Source retrieved via:
#  bash getsources.sh 1ea10aa82e30e0d60f57e1c562281a3ac7dd5cdd 1.0.23
Source: %{name}-%{version}.tar.gz
URL: http://www.jfree.org/jcommon
BuildRequires: junit
BuildRequires: maven-local
BuildRequires: maven-plugin-bundle
Requires: java-headless, jpackage-utils
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch

Patch0: javadoc-11.patch
Patch1: java17.patch

%description
JCommon is a collection of useful classes used by 
JFreeChart, JFreeReport and other projects.

%package javadoc
Summary: Javadoc for %{name}
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%patch0 -b javadoc-11
%patch1 -b java17
find . -name "*.jar" -exec rm -f {} \;
# remove unnecessary dependency on parent POM
%pom_remove_parent
MVN_BUNDLE_PLUGIN_EXTRA_XML="<extensions>true</extensions>
        <configuration>
          <instructions>
            <Bundle-SymbolicName>org.jfree.jcommon</Bundle-SymbolicName>
            <Bundle-Vendor>Fedora Project</Bundle-Vendor>
            <Bundle-Version>%{version}</Bundle-Version>
            <!-- Do not autogenerate uses clauses in Manifests -->
            <_nouses>true</_nouses>
          </instructions>
        </configuration>"
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_add_plugin org.apache.felix:maven-bundle-plugin . "$MVN_BUNDLE_PLUGIN_EXTRA_XML"
# Change to packaging type bundle so as to be able to use it
# as an OSGi bundle.
%pom_xpath_set "pom:packaging" "bundle"
# temporary while java 11 is being bootstrapped to become the default
# undo javadoc-11.patch while javac is still 1.8.0
if [ "`javac -version 2>&1 | cut -d_ -f 1`" = "javac 1.8.0" ]; then
  sed -i -e /maven.compiler.release/d pom.xml
fi

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.23-23
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.23-22
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Caolán McNamara <caolanm@redhat.com> - 1.0.23-20
- more prep for f36 mass rebuild for java-17-openjdk

* Thu Dec 02 2021 Caolán McNamara <caolanm@redhat.com> - 1.0.23-19
- prep for f36 mass rebuild for java-17-openjdk

* Mon Aug 02 2021 Caolan McNamara <caolanm@redhat.com> 1.0.23-18
- Resolves: rhbz#1987596 add a junit build-depend for FTBFS

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 30 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.23-15
- Remove unnecessary dependency on parent POM.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.0.23-13
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed May 06 2020 Caolan McNamara <caolanm@redhat.com> 1.0.23-12
- bump n-v-r and use maven.compiler.release of 6

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Merlin Mathesius <mmathesi@redhat.com> - 1.0.23-4
- Add missing BuildRequires to fix FTBFS (BZ#1406105).

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Sep 02 2014 Severin Gehwolf <sgehwolf@redhat.com> - 1.0.23-1
- Update to upstream 1.0.23 (using github sources).
- Switch to building with xmvn.

* Tue Sep 02 2014 Severin Gehwolf <sgehwolf@redhat.com> - 1.0.19-1
- Update to upstream 1.0.19 release.

* Tue Jun 10 2014 David Tardon <dtardon@redhat.com> - 1.0.18-6
- Resolves: rhbz#1106929 fix FTBFS

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Caolan McNamara <caolanm@redhat.com> 1.0.18-4
- Resolves: rhbz#1068257 Switch to java-headless (build)requires

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.18-1
- Update to upstream 1.0.18 release.

* Mon Sep 17 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.17-5
- Add proper Bundle-{Version,Name,SymbolicName} via
  bnd.properties file

* Tue Jul 24 2012 Severin Gehwolf <sgehwolf@redhat.com> 1.0.17-4
- Add aqute bnd instructions so as to produce OSGi metadata.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 03 2012 Roman Kennke <rkennke@redhat.com> 1.0.17-2
- Install pom and maven depmap.

* Thu Apr 12 2012 Alexander Kurtakov <akurtako@redhat.com> 1.0.17-1
- Update to latest upstream release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Caolán McNamara <caolanm@redhat.com> 1.0.16-4
- Related: rhbz#749103 drop gcj aot

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Caolan McNamara <caolanm@redhat.com> 1.0.16-2
- make javadoc no-arch when building as arch-dependant aot

* Sat Apr 25 2009 Caolan McNamara <caolanm@redhat.com> 1.0.16-1
- latest version

* Mon Mar 09 2009 Caolan McNamara <caolanm@redhat.com> 1.0.15-1
- latest version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 07 2008 Caolan McNamara <caolanm@redhat.com> 1.0.12-4
- shuffle around

* Thu May 01 2008 Caolan McNamara <caolanm@redhat.com> 1.0.12-3
- fix review problems and add jcommon-xml subpackage

* Wed Apr 30 2008 Caolan McNamara <caolanm@redhat.com> 1.0.12-2
- take loganjerry's fixes

* Mon Feb 25 2008 Caolan McNamara <caolanm@redhat.com> 1.0.12-1
- initial fedora import
