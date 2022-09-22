Name:    jgrapht
Version: 0.8.1
Release: 28%{?dist}
Summary: A free Java graph library that provides mathematical graph objs and algorithms
License: LGPLv2+
URL:     http://jgrapht.sourceforge.net/
Source0: http://downloads.sourceforge.net/project/jgrapht/JGraphT/Version%200.8.1/jgrapht-%{version}.tar.gz
Patch0:  remove_uneccessary_hardcoded_classpath.patch
Patch1:  jgrapht-0.8.1-disable-doclint.patch

BuildRequires: java-devel >= 1.6
BuildRequires: javapackages-local
BuildRequires: ant

BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch

%description
JGraphT is a free Java graph library that provides mathematical graph-theory 
objects and algorithms.

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0
%patch1 -p0

# remove uneccessary dirs/files
# removing touchgraph/jgraph support as we don't currently have deps packaged
rm -rf src/org/jgrapht/demo/ src/org/jgrapht/experimental/touchgraph src/org/jgrapht/ext/JGraphModelAdapter.java

# remove builting jars/classes
find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
ant jar
ant javadoc

%install
%mvn_artifact thirdparty:%{name}-jdk1.6:%{version} %{name}-jdk1.6.jar
%mvn_file thirdparty:%{name}-jdk1.6 %{name}
%mvn_install -J javadoc

%files -f .mfiles
%doc README.html
%license license-LGPL.txt

%files javadoc -f .mfiles-javadoc
%license license-LGPL.txt

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 0.8.1-27
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.8.1-26
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0.8.1-21
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 gil cattaneo <puntogil@libero.it> 0.8.1-12
- fix FTBFS: disable javadoc linting

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 10 2015 gil cattaneo <puntogil@libero.it> 0.8.1-10
- Add maven metadata
- Adapt to current guideline

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 21 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.8.1-8
- Move to java-headless
- Resolves: rhbz#1068279

* Fri Mar 21 2014 Michael Simacek <msimacek@redhat.com> - 0.8.1-8
- Remove version from JAR name

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Apr  27 2010 <mmorsi@redhat.com> - 0.8.1-2
- use version macro in source uri

* Mon Feb  01 2010  <mmorsi@redhat.com> - 0.8.1-1
- Initial build.
