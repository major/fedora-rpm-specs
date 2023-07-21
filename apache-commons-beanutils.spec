%bcond_with bootstrap

Name:           apache-commons-beanutils
Version:        1.9.4
Release:        13%{?dist}
Summary:        Java utility methods for accessing and modifying the properties of arbitrary JavaBeans
License:        ASL 2.0
URL:            http://commons.apache.org/beanutils
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        http://archive.apache.org/dist/commons/beanutils/source/commons-beanutils-%{version}-src.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
%endif

%description
The scope of this package is to create a package of Java utility methods
for accessing and modifying the properties of arbitrary JavaBeans.  No
dependencies outside of the JDK are required, so the use of this package
is very lightweight.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
%{summary}.

%prep
%setup -q -n commons-beanutils-%{version}-src
sed -i 's/\r//' *.txt

%pom_remove_plugin :maven-assembly-plugin

%mvn_alias :{*} :@1-core :@1-bean-collections
%mvn_alias :{*} org.apache.commons:@1 org.apache.commons:@1-core org.apache.commons:@1-bean-collections
%mvn_file : %{name} %{name}-core %{name}-bean-collections
%mvn_file : commons-beanutils commons-beanutils-core commons-beanutils-bean-collections

%build
# Some tests fail in Koji
%mvn_build -f -- -Dmaven.compiler.source=1.7 -Dmaven.compiler.target=1.7 -Dcommons.osgi.symbolicName=org.apache.commons.beanutils

%install
%mvn_install

%files -f .mfiles
%doc RELEASE-NOTES.txt
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.9.4-10
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 02 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.4-8
- Bump Java compiler source/target levels to 1.7

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.4-6
- Bootstrap build
- Non-bootstrap build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.9.4-3
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.4-2
- Mass rebuild for javapackages-tools 201902

* Fri Oct 04 2019 Fabio Valentini <decathorpe@gmail.com> - 1.9.4-1
- Update to version 1.9.4.
- Re-enable test suite.

* Thu Aug 15 2019 Marian Koncek <mkoncek@redhat.com> - 1.9.4-1
- Update to upstream version 1.9.4

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.3-5
- Mass rebuild for javapackages-tools 201901

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 01 2016 Michael Simacek <msimacek@redhat.com> - 1.9.3-1
- Update to upstream version 1.9.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.2-3
- Remove Provides/Obsoletes for javadoc package

* Wed Jul 30 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.2-2
- Fix build-requires on apache-commons-parent

* Fri Jun  6 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.2-1
- Update to upstream version 1.9.2
- Remove legacy Provides/Obsoletes for jakarta-commons-beanutils
- Remove RPM bug workaround

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.9.1-2
- Use Requires: java-headless rebuild (#1067528)

* Mon Jan 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.1-1
- Update to upstream version 1.9.1

* Mon Jan  6 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.9.0-1
- Update to upstream version 1.9.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.3-10
- Build with xmvn
- Don't generate extra JARs
- Simplify build dependencies
- Update to current packaging guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.8.3-8
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.8.3-5
- Packaging fixes
- Remove unneeded depmap
- Remove versioned jars and javadocs
- Use maven 3 to build

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.8.3-3
- Add license to javadoc subpackage

* Mon May 24 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.8.3-2
- Added provides to javadoc subpackage

* Fri May 21 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.8.3-1
- Re-did whole spec file, dropped gcj support
- Rename package (jakarta-commons-beanutils->apache-commons-beanutils)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.7.0-12.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.7.0-11.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 23 2008 David Walluck <dwalluck@redhat.com> 0:1.7.0-10.3
- Fedora-specific: enable GCJ support

* Thu Oct 23 2008 David Walluck <dwalluck@redhat.com> 0:1.7.0-10.2
- Fedora-specific: BuildRequires: java-1.6.0-devel

* Thu Oct 23 2008 David Walluck <dwalluck@redhat.com> 0:1.7.0-10.1
- Fedora-specific: remove repolib
- Fedora-specific: enable JDK6 support

* Mon Oct 20 2008 David Walluck <dwalluck@redhat.com> 0:1.7.0-10
- add flag to build with maven

* Fri Sep 19 2008 David Walluck <dwalluck@redhat.com> 0:1.7.0-9
- add jdk6 patch
- fix repolib

* Sun Jun 15 2008 David Walluck <dwalluck@redhat.com> 0:1.7.0-8.jpp5
- fix duplicate files
- correctly unpack sources
- remove spurious gnu-crypto requirement
- remove spurious javadoc package requirements
- fix javadoc directory
- fix build-classpath call
- use macros

* Fri May 30 2008 Permaine Cheung <pcheung@redhat.com> - 0:1.7.0-7
- First JPP5 build

* Tue Jul 24 2007 Ralph Apel <r.apel at r-apel.de> - 0:1.7.0-6jpp
- Make Vendor, Distribution based on macro
- Fix aot build
- Add poms and depmap frags
- Build with maven1 by default
- Add manual subpackage when built with maven

* Tue Mar 13 2007 Vivek Lakshmanan <vivekl@redhat.com> - 0:1.7.0-2jpp.ep1.2
- Fix repolib location

* Tue Mar 13 2007 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-2jpp.ep1.1
- New repolib location

* Mon Mar 05 2007 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-2jpp.el4ep1.3
- Remove pre section used for RHUG cleanup

* Tue Feb 20 2007 Vivek Lakshmanan <vivekl@redhat.com> - 0:1.7.0-2jpp.el4ep1.2
- Add -brew suffix

* Fri Feb 17 2007 Vivek Lakshmanan <vivekl@redhat.com> - 0:1.7.0-2jpp.el4ep1.1
- Add repolib support

* Thu Aug 17 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-5jpp
- Require what is used in post/postun for javadoc

* Fri Jul 14 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-4jpp
- Add AOT bits

* Thu May 11 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-3jpp
- Add header
- Remove unecessary macro definitions

* Wed Feb 22 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-2jpp_1rh
- Merge with upstream

* Wed Apr 27 2005 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-1jpp_3rh
- Fix build so that collections jar is created

* Sat Jan 29 2005 Ralph Apel <r.apel@r-apel.de> - 0:1.7.0-2jpp
- Use the "dist" target to get a full build, including bean-collections

* Thu Oct 21 2004 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-1jpp_1rh
- Import from upstream

* Thu Oct 21 2004 Fernando Nasser <fnasser@redhat.com> - 0:1.7.0-1jpp
- Upgrade to 1.7.0

* Fri Oct 1 2004 Andrew Overholt <overholt@redhat.com> 0:1.6.1-4jpp_6rh
- add coreutils BuildRequires

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:1.6.1-5jpp
- Rebuild with ant-1.6.2

* Fri Jul 2 2004 Aizaz Ahmed <aahmed@redhat.com> 0:1.6.1-4jpp_5rh
- Added trigger to restore symlinks that are removed if ugrading
  from a commons-beanutils rhug package

* Fri Apr  2 2004 Frank Ch. Eigler <fche@redhat.com> 0:1.6.1-4jpp_4rh
- more of the same, for version-suffixed .jar files

* Fri Mar 26 2004 Frank Ch. Eigler <fche@redhat.com> 0:1.6.1-4jpp_3rh
- add RHUG upgrade cleanup

* Fri Mar  5 2004 Frank Ch. Eigler <fche@redhat.com> 0:1.6.1-4jpp_2rh
- RH vacuuming part II

* Thu Mar  4 2004 Frank Ch. Eigler <fche@redhat.com> 0:1.6.1-4jpp_1rh
- RH vacuuming

* Fri May 09 2003 David Walluck <david@anti-microsoft.org> 0:1.6.1-4jpp
- update for JPackage 1.5

* Thu Feb 27 2003 Henri Gomez <hgomez@users.sourceforge.net> 1.6.1-2jpp
- fix ASF license and add packager name

* Wed Feb 19 2003 Henri Gomez <hgomez@users.sourceforge.net> 1.6.1-1jpp
- 1.6.1

* Thu Feb 13 2003 Henri Gomez <hgomez@users.sourceforge.net> 1.6-1jpp
- 1.6

* Thu Oct 24 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.5-1jpp
- 1.5

* Fri Aug 23 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.4.1-1jpp
- 1.4.1

* Tue Aug 20 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.4-1jpp
- 1.4

* Fri Jul 12 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.3-3jpp
- change to commons-xxx.jar instead of commons-xxx.home in ant parameters

* Mon Jun 10 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.3-2jpp
- use sed instead of bash 2.x extension in link area to make spec compatible
  with distro using bash 1.1x

* Fri Jun 07 2002 Henri Gomez <hgomez@users.sourceforge.net> 1.3-1jpp
- 1.3
- added short names in %%{_javadir}, as does jakarta developpers
- first jPackage release
