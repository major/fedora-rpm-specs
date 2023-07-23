Name:           sqljet
Version:        1.1.10
Release:        27%{?dist}
Summary:        Pure Java SQLite

License:        GPLv2
URL:            http://sqljet.com/
Source0:        http://sqljet.com/files/%{name}-%{version}-src.zip

Source4:        %{name}-build.xml
Source5:        %{name}-pom.xml

BuildRequires:  ant
BuildRequires:  antlr
BuildRequires:  antlr32-java
BuildRequires:  antlr32-tool
BuildRequires:  easymock3
BuildRequires:  junit
BuildRequires:  stringtemplate
BuildRequires:  hamcrest
BuildRequires:  javapackages-local
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch

%description
SQLJet is an independent pure Java implementation of a popular SQLite database
management system. SQLJet is a software library that provides API that enables
Java application to read and modify SQLite databases.

%package        javadoc
Summary:        Javadoc for %{name} 
%description    javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

find \( -name '*.class' -o -name '*.jar' \) -delete

rm -rf gradlew.bat gradlew gradle

cp %{SOURCE4} build.xml
cp %{SOURCE5} pom.xml

cat > sqljet.build.properties <<EOF
sqljet.version.major=1
sqljet.version.minor=1
sqljet.version.micro=10
sqljet.version.build=local

antlr.version=3.2
sqlite.version=3.8.3
EOF


%build
export CLASSPATH=$(build-classpath antlr32/antlr-runtime-3.2 antlr32/antlr-3.2 antlr stringtemplate easymock3 junit hamcrest-core)
ant jars osgi javadoc pom

%install
%mvn_artifact pom.xml build/sqljet.jar
%mvn_file ":sqljet" sqljet
%mvn_install -J build/javadoc

%files -f .mfiles
%license LICENSE.txt
%doc README.txt CHANGES.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 25 2022 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.10-25
- Fix FTBFS against hamcrest

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.1.10-23
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.1.10-22
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Mat Booth <mat.booth@redhat.com> - 1.1.10-17
- Remove unneeded dep on antlr3

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.1.10-16
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Jun 29 2020 Jeff Johnston <jjohnstn@redhat.com> - 1.1.10-15
- Enable building using Java 11
- remove classpathref for Javadoc as CLASSPATH contains all that is needed

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 11 2018 Mat Booth <mat.booth@redhat.com> - 1.1.10-10
- Modernise spec file
- Fix failures to build from source

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 26 2015 Kalev Lember <klember@redhat.com> - 1.1.10-5
- Drop sqljet-browser subpackage (#1266662)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 10 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.10-3
- Rebuilt to fix FTBFS, fix maven-fragments stuff, fixes rhbz #1107368 and #1107370

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 19 2014 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.10-1
- Update to 1.1.10 upstream release.

* Tue Dec 10 2013 Filipe Rosset <rosset.filipe@gmail.com> - 1.1.8-1
- Update to 1.1.8 upstream release.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 23 2013 Alexander Kurtakov <akurtako@redhat.com> 1.1.7-1
- Update to 1.1.7 upstream release.
- Fix browser startup script.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 9 2012 Ismael Olea <ismael@olea.org> - 1.1.4-3
- spec maven enhancements

* Sat Oct 6 2012 Ismael Olea <ismael@olea.org> - 1.1.4-2
- beautifing build.xml

* Fri Oct 5 2012 Ismael Olea <ismael@olea.org> - 1.1.4-1
- update to 1.1.4

* Tue Jul 31 2012 Alexander Kurtakov <akurtako@redhat.com> 1.0.4-8
- Make jars readable.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Ville Skyttä <ville.skytta@iki.fi> - 1.0.4-6
- Fix unexpanded versions in osgi manifest.
- Fix build with antlr3 >= 3.4.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 5 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0.4-4
- Fix the browser with latest netbeans.

* Tue Jun 28 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0.4-3
- Bump release.
- Adapt to latest netbeans-platform changes.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Alexander Kurtakov <akurtako@redhat.com> 1.0.4-1
- Update to new upstream version.

* Tue Dec 21 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0.3-4
- Fix versions in pom.xml file causing parsing problems

* Tue Dec 14 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0.3-3
- Versionless jars
- Changes accroding to new guidelines (no buildroot/clean section)
- Add license to javadoc subpackage
- Install maven metadata

* Sat Aug 28 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0.3-2
- Fix build with latest netbeans.
- Fix sqljet-browser run script.

* Tue May 18 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0.3-1
- New version.

* Wed Apr 21 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0.2-3
- Fix build with new antlr3.
- Fix startup script for the browser.
- Add missing semicolon in the desktop file.

* Mon Feb 15 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0.2-2
- Rebuild for netbeans-platform update. (rhbz#564657)

* Thu Jan 14 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0.2-1
- Update to 1.0.2.

* Thu Dec 3 2009 Alexander Kurtakov <akurtako@redhat.com> 1.0.1-3
- Require antlr3.

* Mon Nov 30 2009 Alexander Kurtakov <akurtako@redhat.com> 1.0.1-2
- Fix build and review comments.

* Thu Nov 26 2009 Alexander Kurtakov <akurtako@redhat.com> 1.0.1-1
- Initial package.
