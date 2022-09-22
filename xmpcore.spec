Name:          xmpcore
Version:       5.1.2
Release:       21%{?dist}
Summary:       Java XMP Library
License:       BSD
URL:           http://www.adobe.com/devnet/xmp.html
Source0:       http://repo1.maven.org/maven2/com/adobe/xmp/%{name}/%{version}/%{name}-%{version}-sources.jar
# from http://repo1.maven.org/maven2/com/adobe/xmp/xmpcore/5.1.2/xmpcore-5.1.2.pom
# customized:
# fix compiler,javadoc-plugin configuration
# fix manifest entries
Source1:       %{name}-%{version}.pom
# from http://download.macromedia.com/pub/developer/xmp/sdk/XMP-Toolkit-SDK-5.1.2.zip
Source2:       %{name}-BSD-License.txt
BuildRequires: buildnumber-maven-plugin
BuildRequires: maven-local
BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch

%description
The XMP Library for Java is based on the
C++ XMPCore library and the API is similar.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -c

mkdir java
mv com java/
rm -r META-INF

cp -p %{SOURCE1} pom.xml
cp -p %{SOURCE2} BSD-License.txt
sed -i 's/\r//' BSD-License.txt

%mvn_file : %{name}

%build

%mvn_build

%install
%mvn_install

%files -f .mfiles
%license BSD-License.txt

%files javadoc -f .mfiles-javadoc
%license BSD-License.txt

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 5.1.2-20
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 5.1.2-19
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 5.1.2-14
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 22 2016 gil cattaneo <puntogil@libero.it> 5.1.2-6
- regenerate build-requires

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 13 2015 gil cattaneo <puntogil@libero.it> 5.1.2-3
- introduce license macro

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Sep 03 2013 gil cattaneo <puntogil@libero.it> 5.1.2-1
- initial rpm
