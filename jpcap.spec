#
#     RPM package specification for Jpcap
#
#     Edited by Patrick Dignan
#     Originally made by Keita Fujii
#

Name: jpcap
Version: 0.7
Release: 34%{?dist}
Summary: A Java library for capturing and sending network packets

License: LGPLv2+ and BSD with advertising
URL: http://netresearch.ics.uci.edu/kfujii/jpcap/
Source: http://netresearch.ics.uci.edu/kfujii/jpcap/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires: jpackage-utils, java-devel >= 1:1.6, libpcap-devel >= 0.9, ant, dos2unix
BuildRequires: make
Requires: jpackage-utils, java-headless >= 1:1.6
ExclusiveArch: %java_arches

%description 
Jpcap is a Java library for capturing and
sending network packets from Java applications.
This Jpcap package requires Java 1.6 or higher 
and libpcap 0.9 or higher.

%package javadoc
Summary:        Javadocs for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
sed -i 's:System.loadLibrary("jpcap"):System.load("'%{_libdir}/%{name}/lib%{name}.so'"):g' src/java/%{name}/JpcapWriter.java
sed -i 's:System.loadLibrary("jpcap"):System.load("'%{_libdir}/%{name}/lib%{name}.so'"):g' src/java/%{name}/JpcapCaptor.java
rm -rf lib/*
dos2unix ChangeLog
dos2unix README
dos2unix doc/javadoc/package-list
dos2unix doc/javadoc/stylesheet.css

%build
export JAVA_HOME=%{java_home}
set JAVA_HOME=%{java_home}
mkdir bin
%{ant} jar
cd src/c
make clean
make %{?_smp_mflags} CC="gcc %{optflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT

install -D src/c/libjpcap.so $RPM_BUILD_ROOT%{_libdir}/%{name}/libjpcap.so
install -D lib/jpcap.jar $RPM_BUILD_ROOT%{_libdir}/%{name}/jpcap.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp doc/javadoc/ $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc README COPYING ChangeLog
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libjpcap.so
%{_libdir}/%{name}/jpcap.jar

%files javadoc
%{_javadocdir}/%{name}


%changelog
* Sat Aug 13 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7-34
- Adopt %%java_arches https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.7-32
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0.7-27
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 0.7-14
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 Patrick Dignan <dignan.patrick at, gmail.com> 0.7-6
- Uses sed to change System.loadLibrary() to System.load and the exact path of the .so file.
* Tue Jan 06 2009 Patrick Dignan <jpdota at, sourceforge.net> 0.7-5
- Fixed End-of-line problems in README, ChangeLog, doc/javadoc/stylesheet.css, and doc/javadoc/package-list
- Fixed Directory ownership of _libdir/name (macros)
- No longer strips the binaries
- Added Fedora specific compilation flags to make
- Fixed x86_64 build by adding -fPIC to make
- JAVA_HOME now set by the java_home macro
- Removed require on libpcap
- Changed SourceURL to use the name and version macros
