Summary:	Java Simple Serial Connector
Name:		jssc
Version:	2.8.0
Release:	33%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		http://jssc.scream3r.org
Source:		https://github.com/scream3r/java-simple-serial-connector/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# lack of license file, reported upstream:
# https://github.com/scream3r/java-simple-serial-connector/issues/79
Source1:	http://www.gnu.org/licenses/gpl-3.0.txt
# jni load library patch
Patch0:		%{name}-loadlibrary.patch
# fixes jni header mismatch, reported upstream:
# https://github.com/scream3r/java-simple-serial-connector/issues/80
Patch1:		%{name}-jni-fix.patch

ExclusiveArch:  %{java_arches}

BuildRequires:	gcc-c++
BuildRequires:	java-devel
BuildRequires:	javapackages-local

Requires:	java-headless
Requires:	jpackage-utils

%global jni		%{_libdir}/%{name}
%global jniFullSoName	libjSSC-%{version}.so
%global jniSoName	libjSSC.so


%description
jSSC (Java Simple Serial Connector) - library for working with serial ports
from Java.


%package javadoc
Summary:        Javadoc for %{name} package
BuildArch:      noarch
Requires:       %{name} = %{version}


%description javadoc
This package contains the API documentation for %{name}.


%prep
%setup -q -n java-simple-serial-connector-%{version}
%patch -P0 -p1 -b .loadlibrary
%patch -P1 -p1 -b .jni-fix
cp -a %{SOURCE1} COPYING
# remove prebuild binaries and jni headers
rm -rf src/java/libs
rm -rf src/cpp/*.h


%build
# compile classes
mkdir -p classes/
(cd src/java; javac -h ../cpp -d ../../classes/ -encoding UTF-8 jssc/*.java)
(cd classes; jar -cf ../jssc.jar jssc/*.class)
# generate javadoc
mkdir -p javadoc/
(cd src/java; javadoc -Xdoclint:none -d ../../javadoc/ -encoding UTF-8 jssc/*.java)
# compile native library
g++ %{optflags} %{?__global_ldflags} -fPIC -shared \
    -D jSSC_NATIVE_LIB_VERSION=\"$(echo %{version} | sed 's/\([1-9]\.[0-9]\).*/\1/')\" \
    -I %{java_home}/include \
    -I %{java_home}/include/linux \
    -o %{jniFullSoName} src/cpp/_nix_based/jssc.cpp


%install
# create necessary directories
install -d %{buildroot}%{jni} \
           %{buildroot}%{_javadocdir}/%{name}
# install jni library and symlink
install -m 0755 -p %{jniFullSoName} %{buildroot}%{jni}
ln -srf %{buildroot}%{jni}/%{jniFullSoName} %{buildroot}%{jni}/%{jniSoName}
# install jar, pom files and java docs
%mvn_artifact org.scream3r:%{name}:%{version} %{name}.jar
%mvn_file org.scream3r:%{name}:%{version} %{name}
%mvn_install -J javadoc


%files -f .mfiles
%license COPYING
%doc README.txt
%{jni}/


%files javadoc
%doc %{_javadocdir}/%{name}


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.8.0-32
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 2.8.0-30
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 15 2023 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.8.0-26
- Rebuild to get rid of java 1.8 dependency

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jul 26 2022 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.8.0-24
- Fix FTBFS on F37 (rhbz#2104065)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.8.0-22
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 26 2020 Jeff Law <law@redhat.com> - 2.8.0-18
- Do not force C++11 mode

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.8.0-16
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jun 11 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.8.0-15
- Fix for java-11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.8.0-10
- Add missing BR (gcc-c++)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 05 2015 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.8.0-4
- Simplify BR, install and files sections.

* Wed Nov 25 2015 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.8.0-3
- Change the license to GPLv3.

* Thu Nov 12 2015 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.8.0-2
- Use URL fragment to automatically rename source tarball.

* Mon Nov 02 2015 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 2.8.0-1
- Initial RPM release.
