# Rust doesn't create data for a -debuginfo package
%global debug_package %{nil}

# Build- and run-time version of OpenJDK Java
%if 0%{?fedora} || 0%{?rhel} > 9
%global java_version 17
%else
%global java_version 11
%endif

Summary:           Open Source implementation of JSR-56 better known as Java Web Start
Name:              icedtea-web
Version:           1.8.8
Release:           7%{?dist}
# Run the following command after removing applet/unused sources in %%prep:
# licensecheck -r --shortname-scheme=spdx . | sed -e 's/.*: //' | sort -u
License:           GPL-2.0-only AND GPL-2.0-only WITH Classpath-exception-2.0 AND GPL-2.0-or-later AND GPL-2.0-or-later WITH Classpath-exception-2.0 AND LGPL-2.1-or-later AND Zlib
URL:               https://github.com/AdoptOpenJDK/IcedTea-Web
Source0:           https://github.com/AdoptOpenJDK/IcedTea-Web/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
# Remove dependency to dunce (normalizes Windows paths to the most compatible format)
Patch0:            icedtea-web-1.8.8-remove-dunce.patch
# https://access.redhat.com/documentation/en-us/openjdk/11/html/using_alt-java
Patch1:            icedtea-web-1.8.8-alt-java.patch
# Upstream changes since IcedTea-Web 1.8.8
Patch2:            https://github.com/AdoptOpenJDK/IcedTea-Web/compare/icedtea-web-1.8.8...4b3375b9ad68bec6306c38a976f7c0604fea1852.patch#/icedtea-web-1.8.8-upstream-changes.patch
# Disable sun.applet javadocs and plugin man page for --disable-pluginjar
Patch3:            https://github.com/AdoptOpenJDK/IcedTea-Web/pull/907.patch#/icedtea-web-1.8.8-disable-pluginjar.patch
# Use same naming scheme like bash-completion
Patch4:            https://github.com/AdoptOpenJDK/IcedTea-Web/pull/899.patch#/icedtea-web-1.8.8-bash-completion.patch
# Disable man pages for languages without any translation
Patch5:            https://github.com/AdoptOpenJDK/IcedTea-Web/pull/901.patch#/icedtea-web-1.8.8-untranslated-man-pages.patch
# Fix javadoc error related to @param in TimedHashMap.java
Patch6:            https://github.com/AdoptOpenJDK/IcedTea-Web/pull/908.patch#/icedtea-web-1.8.8-javadoc-param.patch
# Reflect removal of Pack200 Tools and API in Java 17 to IcedTea-Web
Patch7:            icedtea-web-1.8.8-java18-no-pack200.patch
ExclusiveArch:     %{java_arches}
BuildRequires:     autoconf
BuildRequires:     automake
BuildRequires:     bc
BuildRequires:     cargo
BuildRequires:     desktop-file-utils
BuildRequires:     java-%{java_version}-openjdk-devel
BuildRequires:     javapackages-local
BuildRequires:     javapackages-tools
BuildRequires:     libappstream-glib
BuildRequires:     pkgconfig(bash-completion)
BuildRequires:     tagsoup
BuildRequires:     zip
Recommends:        bash-completion
Requires:          java-%{java_version}-openjdk
Requires:          javapackages-tools
# Required at runtime if icedtea-web was built against it
Requires:          tagsoup
Requires(post):    alternatives
Requires(post):    GConf2
Requires(postun):  alternatives
Requires(postun):  GConf2
# Cover third party repositories
Obsoletes:         javaws < 1.8.8-1
Provides:          javaws = %{version}-%{release}
Provides:          javaws%{?_isa} = %{version}-%{release}

%description
The IcedTea-Web project provides a free software implementation of Java
Web Start, originally based on the NetX, project.

IcedTea's NetX currently supports verification of signed jars, trusted
certificate storing, system certificate store checking, and provides the
services specified by the jnlp API.

In addition it also provides a full desktop integration, an offline run,
many extended security features, an own policy editor and much more.

%package javadoc
Summary:           API documentation for IcedTea-Web
Requires:          %{name} = %{version}-%{release}
BuildArch:         noarch

%description javadoc
This package contains the API documentation for the IcedTea-Web project.

%package devel
Summary:           Pure sources for debugging IcedTea-Web
Requires:          %{name} = %{version}-%{release}
BuildArch:         noarch

%description devel
This package contains the zipped sources of the IcedTea-Web project for
debugging IcedTea-Web.

%prep
%setup -q -n IcedTea-Web-%{name}-%{version}
%patch -P0 -p1 -b .remove-dunce
%patch -P1 -p1 -b .alt-java
%patch -P2 -p1 -b .upstream-changes
%patch -P3 -p1 -b .disable-pluginjar
%patch -P4 -p1 -b .bash-completion
%patch -P5 -p1 -b .untranslated-man-pages
%patch -P6 -p1 -b .javadoc-param
%if 0%{?java_version} >= 17
%patch -P7 -p1 -b .java18-no-pack200
%endif

# Remove applet support
rm -rf plugin netx/sun netx/net/sourceforge/jnlp/{NetxPanel,runtime/RhinoBasedPacEvaluator,util/WindowsDesktopEntry}.java

# Remove unused sources
rm -rf tests win-installer

%build
autoreconf --force --install
%configure \
  --with-pkgversion=fedora-%{release}-%{_arch} \
  --docdir=%{_datadir}/javadoc/%{name} \
  --with-jdk-home=%{_jvmdir}/java-%{java_version}-openjdk \
  --with-jre-home=%{_jvmdir}/jre-%{java_version}-openjdk \
  --program-suffix=.itweb \
  --disable-native-plugin \
  --disable-pluginjar \
  --with-itw-libs=DISTRIBUTION \
  --with-modularjdk-file=%{_sysconfdir}/java/%{name} \
  --enable-shell-launchers
%make_build

%install
%make_install

# Install desktop files
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications javaws.desktop
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications itweb-settings.desktop
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications policyeditor.desktop

# Install MetaInfo file for firefox
install -D -p -m 0644 metadata/%{name}.metainfo.xml $RPM_BUILD_ROOT%{_metainfodir}/%{name}.metainfo.xml

# Install MetaInfo file for javaws
install -D -p -m 0644 metadata/%{name}-javaws.appdata.xml $RPM_BUILD_ROOT%{_metainfodir}/%{name}-javaws.metainfo.xml

# Maven fragments generation
mkdir -p $RPM_BUILD_ROOT%{_javadir}/
ln -s ../%{name}/javaws.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -D -p -m 0644 metadata/%{name}.pom $RPM_BUILD_ROOT%{_mavenpomdir}/%{name}.pom

%mvn_artifact $RPM_BUILD_ROOT%{_mavenpomdir}/%{name}.pom $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# Install source zip for devel package
install -D -p -m 0644 netx.build/lib/src.zip $RPM_BUILD_ROOT%{_datadir}/%{name}/javaws.src.zip

# Create files for %%ghost in %%files
touch $RPM_BUILD_ROOT%{_bindir}/{javaws,itweb-settings,policyeditor}

# Until https://bugzilla.redhat.com/show_bug.cgi?id=2188866 is fixed
rm -f $RPM_BUILD_ROOT%{_datadir}/bash-completion/completions/javaws

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.metainfo.xml

%post
alternatives \
  --install %{_bindir}/javaws         javaws.%{_arch} %{_bindir}/javaws.itweb    %{java_version}0000 --family java-%{java_version}-openjdk.%{_arch} \
  --slave   %{_bindir}/itweb-settings itweb-settings  %{_bindir}/itweb-settings.itweb \
  --slave   %{_bindir}/policyeditor   policyeditor    %{_bindir}/policyeditor.itweb

alternatives \
  --install %{_bindir}/javaws         javaws.%{_arch} %{_bindir}/javaws.itweb.sh %{java_version}0000 --family java-%{java_version}-openjdk.%{_arch} \
  --slave   %{_bindir}/itweb-settings itweb-settings  %{_bindir}/itweb-settings.itweb.sh \
  --slave   %{_bindir}/policyeditor   policyeditor    %{_bindir}/policyeditor.itweb.sh

gconftool-2 --set /desktop/gnome/url-handlers/jnlp/command  --type=string '%{_bindir}/javaws.itweb %s' &> /dev/null || :
gconftool-2 --set /desktop/gnome/url-handlers/jnlp/enabled  --type=bool true &> /dev/null || :
gconftool-2 --set /desktop/gnome/url-handlers/jnlps/command --type=string '%{_bindir}/javaws.itweb %s' &> /dev/null || :
gconftool-2 --set /desktop/gnome/url-handlers/jnlps/enabled --type=bool true &> /dev/null || :

%postun
if [ $1 -eq 0 ]; then
  alternatives --remove javaws.%{_arch} %{_bindir}/javaws.itweb
  alternatives --remove javaws.%{_arch} %{_bindir}/javaws.itweb.sh
  gconftool-2 --unset /desktop/gnome/url-handlers/jnlp/command  &> /dev/null || :
  gconftool-2 --unset /desktop/gnome/url-handlers/jnlp/enabled  &> /dev/null || :
  gconftool-2 --unset /desktop/gnome/url-handlers/jnlps/command &> /dev/null || :
  gconftool-2 --unset /desktop/gnome/url-handlers/jnlps/enabled &> /dev/null || :
fi
exit 0

%files
%license COPYING
%doc AUTHORS NEWS README
%dir %{_sysconfdir}/java/%{name}/
%config(noreplace) %{_sysconfdir}/java/%{name}/itw-modularjdk.args
%ghost %{_bindir}/javaws
%{_bindir}/javaws.itweb
%{_bindir}/javaws.itweb.sh
%ghost %{_bindir}/itweb-settings
%{_bindir}/itweb-settings.itweb
%{_bindir}/itweb-settings.itweb.sh
%ghost %{_bindir}/policyeditor
%{_bindir}/policyeditor.itweb
%{_bindir}/policyeditor.itweb.sh
%{_datadir}/applications/javaws.desktop
%{_datadir}/applications/itweb-settings.desktop
%{_datadir}/applications/policyeditor.desktop
%{_datadir}/bash-completion/completions/itweb-settings
%{_datadir}/bash-completion/completions/policyeditor
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/javaws.jar
%{_datadir}/%{name}/javaws_splash.png
%{_javadir}/%{name}.jar
%{_mavenpomdir}/%{name}.pom
%{_metainfodir}/%{name}.metainfo.xml
%{_metainfodir}/%{name}-javaws.metainfo.xml
%{_datadir}/pixmaps/javaws.png
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/itweb-settings.1*
%{_mandir}/man1/javaws.1*
%{_mandir}/man1/policyeditor.1*

%files javadoc
%{_datadir}/javadoc/%{name}/

%files devel
%{_datadir}/%{name}/javaws.src.zip

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.8.8-5
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Apr 23 2023 Robert Scheck <robert@fedoraproject.org> - 1.8.8-1
- Upgrade to 1.8.8 (#2188867)

* Tue Nov 24 2020 Jiri Vanek <jvanek@redhat.com> - 1.8.4-1
- patched to use alt-java
- returned shell launchers

* Tue Nov 24 2020 Jiri Vanek <jvanek@redhat.com> - 1.8.4-0
- rebased to 1.8.4

* Wed Jul 31 2019 Jiri Vanek <jvanek@redhat.com> - 1.8.2-4
- fixed alternatives removal. Were broken for years

* Wed Jul 31 2019 Jiri Vanek <jvanek@redhat.com> - 1.8.2-3
- added issue1-3 patches to fix CVEs 2019-10181, 2019-10182, 2019-10185

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Jiri Vanek <jvanek@redhat.com> - 1.8.2-1
- Bump to 1.8.2; first from AdoptOpenJDK

* Wed Mar 20 2019 Peter Robinson <pbrobinson@fedoraproject.org> - 1.8-2
- Drop chkconfig dep, 1.7 shipped in f24

* Tue Mar 12 2019 Jiri Vanek <jvanek@redhat.com> - 1.8-1
- Bump to 1.8

* Tue Feb 26 2019 Jiri Vanek <jvanek@redhat.com> - 1.8pre-0.2
- itw-modularjdk.args marked as %%config(noreplace)

* Thu Feb 21 2019 Jiri Vanek <jvanek@redhat.com> - 1.8pre-0.1
- updated to soon to release itw 1.8 with native launchers

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 16 2018 Jiri Vanek <jvanek@redhat.com> - 1.7.1-11
- added upstream patches

* Mon Jul 16 2018 Jiri Vanek <jvanek@redhat.com> - 1.7.1-10
- added upstream patches
- removed most relicts of plugin

* Mon Jul 16 2018 Jiri Vanek <jvanek@redhat.com> - 1.7.1-8
- removed rhino

* Thu May 24 2018 Jiri Vanek <jvanek@redhat.com> - 1.7.1-6
- removed clang

* Mon May 14 2018 Jiri Vanek <jvanek@redhat.com> - 1.7.1-6
- added an applied patch1, oracleForms.patch to make oracle forms working

* Fri Mar 02 2018 Jiri Vanek <jvanek@redhat.com> - 1.7.1-5
- added 1473-1480.patch
- added support for javafx-desc and so allow run of pure-javafx only applications
- --nosecurity enhanced for possibility to skip invalid signatures
- enhanced to allow resources to be read also from j2se/java element (OmegaT)

* Tue Feb 20 2018 Jiri Vanek <jvanek@redhat.com> - 1.7.1-3
- added buildrequires on gcc/gcc-c++
- to follow new packaging guidelines which no longer automatically pulls gcc/c++ to build root

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Jiri Vanek <jvanek@redhat.com> 1.7.1-1
- bump to 1.7.1

* Fri Nov 03 2017 Jiri Vanek <jvanek@redhat.com> 1.7-6
- javaws specific manpage renamed from -suffix to .suffix

* Wed Oct 18 2017 Jiri Vanek <jvanek@redhat.com> 1.7-5
- gathered various patches from upstream

* Wed Aug 23 2017 Jiri Vanek <jvanek@redhat.com> 1.7-4
- removed native plugin, no longer can build (removed xulrunner and gecko devel packages)
- added forgotten slaves of itweb-settings policyeditor
- Own %%{_datadir}/%%{name} dir
- Mark non-English man pages with %%lang
- Install COPYING as %%license
- last three by Ville Skytta <ville.skytta@iki.fi> via #1481270
- added BuildRequires: javapackages-local to introduce deprecated %%add_maven_depmap macro

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jiri Vanek <jvanek@redhat.com> 1.7-1
- updated to itw 1.7

* Wed Jul 19 2017 Jiri Vanek <jvanek@redhat.com> 1.7-0.5
- updated to RC7

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-0.4.pre06
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri May 12 2017 Jiri Vanek <jvanek@redhat.com> 1.7-0.3.pre06
- updated to RC6
- split bash-completion
- added sources (to align with upstream binary release)

* Tue May 02 2017 Jiri Vanek <jvanek@redhat.com> 1.7-0.3.pre05
- gconf calls silenced by "&> /dev/null || :"
- see rhbz1446932

* Fri Apr 28 2017 Jiri Vanek <jvanek@redhat.com> 1.7-0.2.pre05
- updated to rc5
- added support for jnlp://, jnlps:// and jnlp: protocols

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-0.2.pre04
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Jiri Vanek <jvanek@redhat.com> 1.7-0.1.pre04
- updated to rc4
- fixed RHBZ#1412544

* Wed Jan 11 2017 Jiri Vanek <jvanek@redhat.com> 1.7-0.1.pre03
- updated to RC3 of 1.7

* Wed Jan 04 2017 Jiri Vanek <jvanek@redhat.com> 1.7-0.1.pre01
- updated to RC1 of 1.7
- added recommends on bash completion

* Wed Jul 13 2016 Jiri Vanek <jvanek@redhat.com> 1.6.2-3
- minor fix to javadir and jre dir

* Wed Jul 13 2016 Jiri Vanek <jvanek@redhat.com> 1.6.2-2
- added --family to make it part of java's alternatives alignment
- java-javaver-openjdk collected into preferred_java

* Wed Feb 03 2016 Jiri Vanek <jvanek@redhat.com> 1.6.2-1
- updated to 1.6.2
- fixed also rhbz#1303437 - package owns /etc/bash_completion.d but it should not own it

* Thu Jan 28 2016 Jiri Vanek <jvanek@redhat.com> 1.6.1-66
- moved to 1.6.2pre

* Tue Dec 22 2015 Jiri Vanek <jvanek@redhat.com> 1.6.1-5
- generated maven metadata

* Thu Nov 19 2015 Jiri Vanek <jvanek@redhat.com> 1.6.1-4
- installed also javaws metadata

* Wed Oct 14 2015 Jiri Vanek <jvanek@redhat.com> 1.6.1-3
- added and applied three patches scheduled for 1.6.2
- patch2 fileLogInitializationError-1.6.patch to prevent consequences (#1268909)
- patch1 donLogToFileBeforeFileLogsInitiate.patch
- patch0 javadocFixes.patch

* Mon Sep 21 2015 Jiri Vanek <jvanek@redhat.com> 1.6.1-2
- added and applied patch0 javadocFixes.patch

* Fri Sep 11 2015 Jiri Vanek <jvanek@redhat.com> 1.6.1-1
- updated to upstream release 1.6.1
- metadata xml files enhanced for javaws

* Mon Jun 22 2015 Omair Majid <omajid@redhat.com> - 1.6-5
- Comply with newer java packaging guidelines
- Require javapackages-tools in main package
- Don't require jpackage-utils in -javadoc subpackage, since subpackage
  requires the main package

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Jiri Vanek <jvanek@redhat.com> 1.6-3
- added dependence on hamcrest - no longer part of junit

* Wed Apr 29 2015 Jiri Vanek <jvanek@redhat.com> 1.6-2
- enabled check

* Tue Apr 28 2015 Jiri Vanek <jvanek@redhat.com> 1.6-1
- updated to limited audience final release

* Fri Apr 24 2015 Jiri Vanek <jvanek@redhat.com> 1.6-0.1.pre05
- updated to pre06
- handled "Add Tab Completion for icedtea-web" change
- this release contains numerous, not yet upstreamed, but going to release features:
- summary: Fixed resource test to pass for CZ localization
- summary: Added Czech translation for 1.6
- summary: Messages from TextsProvider moved to properties
- summary: various improvements to default set of properties
- summary: Added MultipleDeploymentPropertiesModifier improvement to testsuite

* Fri Apr 17 2015 Jiri Vanek <jvanek@redhat.com> 1.6-0.1.pre05
- updated to pre05

* Tue Apr 14 2015 Jiri Vanek <jvanek@redhat.com> 1.6-0.1.pre04
- updated to pre04

* Mon Mar 16 2015 Jiri Vanek <jvanek@redhat.com> 1.6-0.1.pre03
- updated to pre03
- removed cp javaws.png. Handled by upstream now

* Mon Dec 22 2014 Jiri Vanek <jvanek@redhat.com> 1.6-0.1.pre02
- updated to pre02
- upstreamed patch1, quoteDocsPaths.patch
- temporarily disabled unittests
- fixed jnlp apps shortcut

* Mon Dec 22 2014 Jiri Vanek <jvanek@redhat.com> 1.6-0.1.pre01
- update future 1.6 alpha pre01
- added localised man pages
- removed link to icedtea-web man page (now provided by upstream)

* Thu Nov 27 2014 Jiri Vanek <jvanek@redhat.com> 1.5.2-0
- update to upstream 1.5.2

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 15 2014 Jiri Vanek <jvanek@redhat.com> 1.5.1-0
- update to upstream 1.5.1
- removed all patches (all upstreamed)

* Thu Aug 14 2014 Richard Hughes <richard@hughsie.com> - 1.5-4
- Add MetaInfo file to show an addon in GNOME Software
- See http://icedtea.classpath.org/bugzilla/show_bug.cgi?id=1907 for upstream

* Mon Jun 09 2014 Omair Majid <omajid@redhat.com> - 1.5-3
- Require junit instead of junit4
- Build against OpenJDK 7 explicitly

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 07 2014 Jiri Vanek <jvanek@redhat.com> 1.5-2
- add not yet upstreamed DE localisation of 1.5
  - patch0 DElocalizationforIcedTea-Web1.5-0001.patch
- autoreconf gog -vfi, see RH1077898
- ./configure changed to %%configure, see RH1077287

* Mon Apr 07 2014 Jiri Vanek <jvanek@redhat.com> 1.5-1
- updated to icedtea-web-1.5

* Mon Mar 10 2014 Jiri Vanek <jvanek@redhat.com> 1.5-0.8.pre05
- updated to pre05
  - based on revision 925

* Mon Mar 10 2014 Jiri Vanek <jvanek@redhat.com> 1.5-0.4.pre04
- updated to pre04
  - based on revision 917

* Wed Mar 05 2014 Jiri Vanek <jvanek@redhat.com> 1.5-0.3.pre03
- updated to pre03
  - based on revision 910:0a36108ce4b9

* Wed Feb 26 2014 Jiri Vanek <jvanek@redhat.com> 1.5-0.2.pre02
- added supported tagsoup dependence

* Wed Feb 26 2014 Jiri Vanek <jvanek@redhat.com> 1.5-0.1.pre02
- updated to bleeding edge as tracker before 1.5 actual release
  - based on revision 899
- added policyeditor.desktop
- removed -std=c++11 flag

* Wed Feb 12 2014 Jiri Vanek <jvanek@redhat.com> 1.5-0.1.pre01
- updated to bleeding edge as tracker before 1.5 actual release
- named by https://fedoraproject.org/wiki/Packaging:NamingGuidelines#Pre-Release_packages
  - see commented original source0 line and setup line reusing versions
- the source tarball is based on revision 892

* Tue Feb 04 2014 Jiri Vanek <jvanek@redhat.com> 1.4.2-0
- updated to 1.4.2
- removed upstreamed patches
- added std=c++11 flag to CXXFLAGS (thanx omajid!)
- removed autoreconf

* Tue Dec 17 2013 Jiri Vanek <jvanek@redhat.com> 1.4.1-1
- added and applied patch0, christmasSplash3.diff. Will be upstreamed
- Christmas release for Fedora !-)

* Tue Sep 17 2013 Jiri Vanek <jvanek@redhat.com> 1.4.1-0
- updated to 1.4.1
- add icedtea-web man page
- removed upstreamed patch1 b25-appContextFix.patch
- removed upstreamed patch2 rhino-pac-permissions.patch
- make check enabled again
- should be build for non-standard archs !-)
- removed unused multilib arches (yupii!)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Omair Majid <jvanek@redhat.com> 1.4.0-3
- Added upstream fix for RH982558

* Wed Jun 19 2013 Jiri Vanek <jvanek@redhat.com> 1.4.0-2
- added patch1 b25-appContextFix.patch to make it run with future openjdk

* Fri Jun 07 2013 Jiri Vanek <jvanek@redhat.com> 1.4-1
- Adapted to latest openjdk changes
- added build requires for autoconf and automake
- minor clean up
- Updated to 1.4
- See announcement for detail
  - http://mail.openjdk.java.net/pipermail/distro-pkg-dev/2013-May/023195.html
- commented out check - some junit4 incompatibility

* Wed Apr 17 2013 Jiri Vanek <jvanek@redhat.com> 1.3.2-0
- Updated to latest ustream release of 1.3 branch - 1.3.2
  - Security Updates
    - CVE-2013-1927, RH884705: fixed gifar vulnerability
    - CVE-2013-1926, RH916774: Class-loader incorrectly shared for applets with same relative-path
  - Common
    - Added new option in itw-settings which allows users to set JVM arguments when plugin is initialized
  - NetX
    - PR580: http://www.horaoficial.cl/ loads improperly
  - Plugin
    PR1260: IcedTea-Web should not rely on GTK
    PR1157: Applets can hang browser after fatal exception
- Removed upstreamed patch to remove GTK dependency
  - icedtea-web-pr1260-remove-gtk-dep.patch

* Wed Feb 20 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.3.1-5
- Resolves: rhbz#875496
- Build with $RPM_LD_FLAGS and %%{_smp_mflags}
- Run unit tests during build

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Deepak Bhole <dbhole@redhat.com> 1.3.1-3
- Resolves: rhbz#889644, rhbz#895197
- Added patch to remove GTK dependency

* Thu Dec 20 2012 Jiri Vanek <jvanek@redhat.com> 1.3.1-2
- Moved to be build with GTK3

* Wed Nov 07 2012 Deepak Bhole <dbhole@redhat.com> 1.3.1-1
- Resolves: RH869040/CVE-2012-4540

* Mon Sep 17 2012 Deepak Bhole <dbhole@redhat.com> 1.3-1
- Updated to 1.3
- Resolves: rhbz#720836: Epiphany fails to execute Java applets

* Tue Jul 31 2012 Deepak Bhole <dbhole@redhat.com> 1.2.1-1
- Updated to 1.2.1
- Resolves: RH840592/CVE-2012-3422
- Resolves: RH841345/CVE-2012-3423

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 03 2012 Deepak Bhole <dbhole@redhat.com> 1.2-4
- Resolves rhbz#814585
- Fixed java-plugin provides and added one for javaws

* Tue Apr 17 2012 Deepak Bhole <dbhole@redhat.com> 1.2-3
- Updated summary
- Fixed virtual provide

* Tue Mar 13 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2-2
- Enable building on ARM platforms

* Mon Mar 05 2012 Deepak Bhole <dbhole@redhat.com> 1.2-1
- Updated to 1.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 Deepak Bhole <dbhole@redhat.com> 1.1.4-3
- Resolves rhbz#757191
- Bumped min_openjdk_version to -60 (latest)

* Thu Nov 24 2011 Deepak Bhole <dbhole@redhat.com> 1.1.4-2
- Resolves: rhbz#742887. Do not own directories not created by the package

* Tue Nov 08 2011 Deepak Bhole <dbhole@redhat.com> 1.1.4-1
- Updated to 1.1.4
- Added npapi-fix patch so that the plug-in compiles with xulrunner 8

* Thu Sep 01 2011 Deepak Bhole <dbhole@redhat.com> 1.1.2-1
- Updated to 1.1.2
- Removed all patches (now upstream)
- Resolves: rhbz#734890

* Tue Aug 23 2011 Deepak Bhole <dbhole@redhat.com> 1.1.1-3
- Added patch to allow install to jre dir
- Fixed requirement for java-1.7.0-openjdk

* Tue Aug 09 2011 Deepak Bhole <dbhole@redhat.com> 1.1.1-2
- Fixed file ownership so that debuginfo is not in main package

* Wed Aug 03 2011 Deepak Bhole <dbhole@redhat.com> 1.1.1-1
- Bump to 1.1.1
- Added patch for PR768 and PR769

* Wed Jul 20 2011 Deepak Bhole <dbhole@redhat.com> 1.0.4-1
- Bump to 1.0.4
- Fixed rhbz#718164: Home directory path disclosure to untrusted applications
- Fixed rhbz#718170: Java Web Start security warning dialog manipulation

* Mon Jun 13 2011 Deepak Bhole <dbhole@redhat.com> 1.0.3-1
- Update to 1.0.3
- Resolves: rhbz#691259

* Mon Apr 04 2011 Deepak Bhole <dbhole@redhat.com> 1.0.2-2
- Fixed incorrect macro value for min_openjdk_version
- Use %%posttrans instead of %%post, so that upgrade from old plugin works

* Mon Apr 04 2011 Deepak Bhole <dbhole@redhat.com> 1.0.2-1
- Initial build
