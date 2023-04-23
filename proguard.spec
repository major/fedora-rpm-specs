Name:           proguard
Version:        6.2.2
Release:        1%{?dist}
Summary:        Java class file shrinker, optimizer, obfuscator and preverifier

License:        GPLv2+
URL:            https://www.guardsquare.com/en/proguard
Source0:        http://downloads.sourceforge.net/%{name}/%{name}%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        README.dist

BuildRequires:  java-devel >= 1:1.8.0
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(org.apache.ant:ant)
Requires:       javapackages-tools
Requires:       jpackage-utils
Requires:       java >= 1:1.6.0
Obsoletes:      %{name}-manual < 5.3.4

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
ProGuard is a free Java class file shrinker, optimizer, obfuscator and
preverifier. It detects and removes unused classes, fields, methods, and
attributes. It optimizes bytecode and removes unused instructions. It
renames the remaining classes, fields, and methods using short meaningless
names. Finally, it preverifies the processed code for Java 6 or for Java
Micro Edition.

%package gui
Summary:        GUI for %{name}
# we convert the favicon.ico to png files of different sizes, so we require
# ImageMagick
BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
Requires:       javapackages-tools
Requires:       %{name} = %{version}-%{release}

%description gui
A GUI for %{name}.

%package -n ant-%{name}
Summary:        Ant task for %{name}
Group:          Development/Libraries/Java

%description -n ant-%{name}
Ant task for %{name}


%prep
%setup -q -n %{name}%{version}

# remove all jar and class files, the snippet from Packaging:Java does 
# not work
find -name '*.jar' -print -delete
find -name '*.class' -print -delete

%pom_disable_module ../gradle buildscripts
%pom_xpath_remove -r pom:addClasspath buildscripts
%pom_remove_plugin -r :maven-source-plugin buildscripts
%pom_remove_plugin -r :maven-javadoc-plugin buildscripts

%mvn_package :*anttask anttask
%mvn_package :*gui gui
%mvn_file :%{name}-base %{name}/%{name}-base %{name}/%{name}

# add README.dist
cp -p %{SOURCE2} .

%build
%mvn_build -f -j -- -f buildscripts/pom.xml -Dsource=8

%install
%mvn_install

mkdir -p %{buildroot}%{_bindir}
%jpackage_script proguard.ProGuard "" "" %{name} %{name} true
%jpackage_script proguard.gui.ProGuardGUI "" "" %{name} %{name}-gui true
%jpackage_script proguard.retrace.ReTrace "" "" %{name} %{name}-retrace true

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "proguard" > %{buildroot}%{_sysconfdir}/ant.d/%{name}

#install the desktop file for proguard-gui
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE1}

%files -f .mfiles
%{_bindir}/%{name}
%{_bindir}/%{name}-retrace
%doc README.md
%license LICENSE.md LICENSE_exception.md

%files -n ant-%{name} -f .mfiles-anttask
%config(noreplace) %{_sysconfdir}/ant.d/%{name}

%files gui -f .mfiles-gui
%{_bindir}/%{name}-gui
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Apr 21 2023 Filipe Rosset <rosset.filipe@gmail.com> - 6.2.2-1
- Update to 6.2.2 + spec cleanup

* Sat Feb 25 2023 Sérgio Basto <sergio@serjux.com> - 6.2.0-1
- Update to 6.2.0 based on https://build.opensuse.org/package/show/openSUSE:Factory/proguard

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 5.3.3-15
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 5.3.3-14
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 5.3.3-9
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.3.3-3
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 26 2017 François Kooman <fkooman@tuxed.net> - 5.3.3-1
- update to 5.3.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 06 2016 François Kooman <fkooman@tuxed.net> - 5.3.2-1
- update to 5.3.2
- new upstream homepage

* Mon Oct 24 2016 François Kooman <fkooman@tuxed.net> - 5.3.1-1
- update to 5.3.1

* Wed Sep 21 2016 François <fkooman@tuxed.net> - 5.3-1
- update to 5.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 25 2015 François Kooman <fkooman@tuxed.net> - 5.2.1-2
- build/ changed to buildscripts/

* Wed Mar 25 2015 François Kooman <fkooman@tuxed.net> - 5.2.1-1
- update to 5.2.1

* Wed Nov 05 2014 François Kooman <fkooman@tuxed.net> - 5.1-1
- update to 5.1

* Fri Aug 22 2014 François Kooman <fkooman@tuxed.net> - 5.0-1
- update to 5.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 07 2014 Michael Simacek <msimacek@redhat.com> - 4.11-2
- Adapt to current packaging guidelines (rhbz#1022159)

* Mon Dec 30 2013 François Kooman <fkooman@tuxed.net> - 4.11-1
- update to 4.11

* Tue Aug 13 2013 F. Kooman <fkooman@tuxed.net> - 4.10-2
- forgot to remove old patch completely

* Tue Aug 13 2013 F. Kooman <fkooman@tuxed.net> - 4.10-1
- update to 4.10

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 20 2013 F. Kooman <fkooman@tuxed.net> - 4.9-2
- bump spec

* Wed Mar 20 2013 F. Kooman <fkooman@tuxed.net> - 4.9-1
- update to 4.9

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 24 2013 F. Kooman <fkooman@tuxed.net> - 4.8-2
- bump spec

* Tue Sep 04 2012 F. Kooman <fkooman@tuxed.net> - 4.8-1
- update to 4.8

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 28 2012 F. Kooman <fkooman@tuxed.net> - 4.7-1
- update to 4.7

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 13 2011 F. Kooman <fkooman@tuxed.net> - 4.6-1
- update to 4.6

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 15 2010 François Kooman <fkooman@tuxed.net> - 4.5.1-1
- update to 4.5.1

* Fri Jun 11 2010 François Kooman <fkooman@tuxed.net> - 4.5-3
- rename proguardgui to proguard-gui (and update .desktop file)
- rename retrace to proguard-retrace
- update README.dist to reflect these changes

* Tue Jun 08 2010 François Kooman <fkooman@tuxed.net> - 4.5-2
- permission fix no longer needed

* Mon Jun  7 2010 François Kooman <fkooman@tuxed.net> - 4.5-1
- update to 4.5 (see http://proguard.sourceforge.net/downloads.html)
- remove GCJ bits as GUI doesn't work with GCJ

* Sun Jan 10 2010 François Kooman <fkooman@tuxed.net> - 4.4-5
- own directory /usr/share/java/proguard
- don't include proguardgui.jar in proguard main package

* Thu Sep  3 2009 François Kooman <fkooman@tuxed.net> - 4.4-4
- create a subpackage for the GUI

* Wed Jul 29 2009 François Kooman <fkooman@tuxed.net> - 4.4-3
- put the manual in a sub package
- fix permissions of launch scripts to 0755 instead of +x to fix rpmlint 
  warning

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 François Kooman <fkooman@tuxed.net> - 4.4-1
- update to ProGuard 4.4

* Wed Jun 10 2009 François Kooman <fkooman@tuxed.net> - 4.3-4
- move creation of icon inside spec
- add GenericName key in .desktop file for KDE users
- make the jar files versioned and create unversioned symlinks to them

* Tue Jun 9 2009 François Kooman <fkooman@tuxed.net> - 4.3-3
- more consistent use of name macro, consistent RPM_BUILD_ROOT variable naming
- indicate that proguard is a directory in files section
- remove redundant attr macro for gcj in files section
- require Java >=1.5
- Use favicon as icon for ProGuard
- keep timestamps when copying files

* Mon Jun 8 2009 François Kooman <fkooman@tuxed.net> - 4.3-2
- add .desktop file + requires
- describe why there are launch scripts included 
- add a README.dist describing how to use ProGuard now that it is packaged
- add GCJ AOT stuff

* Sat Jun 6 2009 François Kooman <fkooman@tuxed.net> - 4.3-1
- Initial Fedora package

