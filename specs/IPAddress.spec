Name:           IPAddress
Version:        5.2.1
Release:        20%{?dist}
Summary:        Library for handling IP addresses and subnets, both IPv4 and IPv6
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/seancfoley/IPAddress
Source0:        https://github.com/seancfoley/IPAddress/archive/v%{version}.tar.gz
Patch1:         removeNonAsciChars.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  ant
# the package builds in jdk8 friendly, but in jdk9+ usable jar/module
BuildRequires:  java-11-openjdk-devel

Requires: java-headless

%description
Library for handling IP addresses and subnets, both IPv4 and IPv6

%prep
%setup -q
%patch -P1 -p1

%build
pushd IPAddress
rm dist/IPAddress.jar
mkdir bin #for classes
#while jdk8 is main, we need both jdks, and prefer the upper one
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
# be aware, the build do not fail in compilation faiure, and you can end with empty, or full of sources jar, as I did first time!
ant "create dist jar" #yah, funny name, as the whole ant-maven-less-with-pom build system
mv dist/IPAddress*.jar dist/IPAddress.jar
#%%mvn_build it looks like pom is useles, and is enough as it is

%install
%mvn_artifact IPAddress/pom.xml IPAddress/dist/IPAddress.jar
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 5.2.1-19
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 5.2.1-17
- Rebuilt for java-21-openjdk as system jdk

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 5.2.1-10
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 5.2.1-9
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 5.2.1-4
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri May 08 2020 Jiri Vanek <jvanek@redhat.com> - 5.2.1-3
- hack with LANG did not worked, pathcing out non asci chars

* Fri May 08 2020 Jiri Vanek <jvanek@redhat.com> - 5.2.1-2
- Fixed build, so the final jar contains also classes and not just sources

* Fri May 08 2020 Jiri Vanek <jvanek@redhat.com> - 5.2.1-1
- Initial packaging
