Name:           swing-layout
Version:        1.0.4
Release:        33%{?dist}
Summary:        Natural layout for Swing panels
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://swing-layout.dev.java.net/
# https://svn.java.net/svn/swing-layout~svn/trunk/
# the above urls are dead, since the upstream project doesn't exist anymore
Source0:        %{name}-%{version}-src.zip
# from http://java.net/jira/secure/attachment/27303/pom.xml
Source1:        %{name}-pom.xml
# use javac target/source 1.5
Patch0:         %{name}-%{version}-project_properties.patch
Patch1:         %{name}-%{version}-fix-incorrect-fsf-address.patch

BuildRequires:  junit >= 3.8.2
BuildRequires:  javapackages-local
BuildRequires:  java-devel >= 1.3
BuildRequires:  ant
BuildRequires:  dos2unix
Requires:       java-headless >= 1.3

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
Extensions to Swing to create professional cross platform layout.

%prep
%setup -q
dos2unix releaseNotes.txt
%patch -P0 -p0
%patch -P1 -p0
sed -i 's/\r//' COPYING

cat %{SOURCE1} | sed "s|<version>1.0.3</version>|<version>%{version}</version>|"  >  %{name}.pom

%build

%{ant} jar 
%mvn_artifact %{name}.pom dist/%{name}.jar

%install

%mvn_install -J dist/javadoc


%check
%{ant} test

%files -f .mfiles
%doc releaseNotes.txt
%license COPYING

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.4-32
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.0.4-30
- Rebuilt for java-21-openjdk as system jdk

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.4-25
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.4-24
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.0.4-19
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Feb 18 2020 Jiri Andrlik <jandrlik@redhat.com> - 1.0.4-18
- Migrated from deprecated add_maven_depmap macro https://docs.fedoraproject.org/en-US/java-packaging-howto/migration/
- renamed pom.xml to swing_layout.pom in sake of some coherence 
- deleted commented javadoc chunks of code and unsatisfiable if statements
- tried to find new url of sources, but with no luck, upstream is non-existent

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Feb 12 2015 gil cattaneo <puntogil@libero.it> 1.0.4-10
- introduce license macro

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 09 2012 gil cattaneo <puntogil@libero.it> 1.0.4-6
- Adapted to current guideline
- Added maven pom
- Installed license file

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Mar 5 2010 Alexander Kurtakov <akurtako@redhat.com> 1.0.4-2
- Drop gcj_support.

* Tue Jan 26 2010 Victor G. Vasilyev <victor.vasilyevg@sun.com> - 1.0.4-1
- 1.0.4

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Apr 03 2008 Lubomir Kundrak <lkundrak@redhat.com> - 1.0.3-2
- gcj bits
- no insane javadoc links

* Tue Feb 19 2008 Lubomir Kundrak <lkundrak@redhat.com> - 1.0.3-1
- 1.0.3
- Major specfile cleanup for Fedora

* Tue Feb 19 2008 Lubomir Kundrak <lkundrak@redhat.com> - 0:1.0-1jpp
- Shamelessly stolen this from JPackage 1.6 without proper ChangeLog entry

* Mon Nov 12 2005 Jaroslav Tulach <jtulach@netbeans.org> - 0:0.9-1jpp
- First packaged release.
