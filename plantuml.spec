Name:           plantuml
Version:        1.2022.6
Release:        1%{?dist}
Epoch:          1
Summary:        Program to generate UML diagram from a text description

License:        LGPLv3+
URL:            http://plantuml.com/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-lgpl-%{version}.tar.gz
#Fix compilation under openjdk
#Patch0:         build-with-javac-utf8-encoding.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  xmvn
Requires:       java >= 1.8.0
BuildRequires:  javapackages-local
# Explicit requires for javapackages-tools since plantuml script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools

%description
PlantUML is a program allowing to draw UML diagrams, using a simple
and human readable text description. It is extremely useful for code
documenting, sketching project architecture during team conversations
and so on.

PlantUML supports the following diagram types
  - sequence diagram
  - use case diagram
  - class diagram
  - activity diagram
  - component diagram
  - state diagram

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c -n plantuml
#%patch0 -p1

# Convert from dos to unix line ending
sed -i.orig 's|\r||g' README
touch -r README.orig README
rm README.orig

%build
ant

# build javadoc
export CLASSPATH=$(build-classpath ant):plantuml.jar
%javadoc -source 1.8 -encoding UTF-8 -Xdoclint:none -d javadoc $(find src -name "*.java") -windowtitle "PlantUML %{version}"

%install
# Set jar location
%mvn_file net.sourceforge.%{name}:%{name} %{name}
# Configure maven depmap
%mvn_artifact net.sourceforge.%{name}:%{name}:%{version} %{name}.jar
%mvn_install -J javadoc

%jpackage_script net.sourceforge.plantuml.Run "" "" plantuml plantuml true

%files -f .mfiles
%{_bindir}/plantuml
%doc README
%license COPYING

%files javadoc -f .mfiles-javadoc
%license COPYING

%changelog
* Sat Aug 20 2022 Sandipan Roy <bytehackr@fedoraproject.org> - 1:1.2022.6-1
- Updated version to 1.2022.6

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2022.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1:1.2022.5-2
- Rebuilt for Drop i686 JDKs

* Mon May 16 2022 Sandipan Roy <bytehackr@fedoraproject.org> - 1:1.2022.5-1
- Updated version to 1.2022.5
- Added fix for rhbz#2086392

* Mon Apr 18 2022 Sandipan Roy <bytehackr@fedoraproject.org> - 1:1.2022.4-1
- Updated version to 1.2022.4
- Added fix for rhbz#2076162
- Added fix for rhbz#2076163

* Mon Mar 07 2022 Sandipan Roy <bytehackr@fedoraproject.org> - 1:1.2022.2-1
- Updated version to 1.2022.2

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1:1.2021.16-3
- Rebuilt for java-17-openjdk as system jdk

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2021.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 29 2021 Sandipan Roy <bytehackr@fedoraproject.org> - 1:1.2021.16-1
- Updated version to 1.2021.16

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2021.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2021.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 James Davidson <james@greycastle.net> - 1:1.2021.0-1
- Update to 1.2021.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2019.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Fabio Valentini <decathorpe@gmail.com> - 1:1.2019.1-5
- Fix javadoc generation with Java 11.

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1:1.2019.1-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2019.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2019.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Jan Safranek <jsafrane@redhat.com> - 1.2019.1-1
- Update to 1.2019.1
- Introduce Epoch, upstream versioning schema changed.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8033-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Severin Gehwolf <sgehwolf@redhat.com> - 8033-9
- Add explicit requirement for javapackages-tools for plantuml script.
  See RHBZ#1600426.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8033-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8033-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8033-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8033-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8033-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 gil cattaneo <puntogil@libero.it> 8033-3
- edited javadoc task

* Thu Nov 26 2015 gil cattaneo <puntogil@libero.it> 8033-2
- fix README line ending

* Thu Nov 26 2015 gil cattaneo <puntogil@libero.it> 8033-1
- update to 8033
- minor changes to adapt to current guideline
- resolve some rpmlint problems
- introduce license macro
- fix java8doc doclint problems
- add maven metadata

* Mon Jun 22 2015 Jan Safranek <jsafrane@redhat.com> - 8027-1
- Update to ver. 8027

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8020-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Jan Safranek <jsafrane@redhat.com> - 8020-1
- Update to ver. 8020

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7992-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 18 2014 Jan Safranek <jsafrane@redhat.com> - 7992-1
- Update to ver. 7992

* Thu Aug 29 2013 Jan Safranek <jsafrane@redhat.com> - 7978-1
- Update to ver. 7978

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7951-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7951-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Jan Safranek <jsafrane@redhat.com> - 7951-1
- Update to ver. 7951
- Added README and COPYING

* Mon Jan 21 2013 Jan Safranek <jsafrane@redhat.com> - 7950-1
- Update to ver. 7950
- Use plantuml-gpl as source tarball to get source package without bundled
  libraries
  -> use ant
  -> use LGPLv3+ license

* Thu Dec  6 2012 Jan Safranek <jsafrane@redhat.com> - 7943-1
- Package created

