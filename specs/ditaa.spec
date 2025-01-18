Summary:        Diagrams Through ASCII Art
Name:           ditaa
Version:        0.10
Release:        28%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://ditaa.sourceforge.net/
Source0:        https://github.com/stathissideris/ditaa/archive/v%{version}.tar.gz
Source1:        ditaa.wrapper
Patch0:         ditaa-0.9-port-to-batik-1.8.patch
# Patch from Debian to build with JDK 10+
Patch1:         https://sources.debian.org/data/main/d/ditaa/0.10+ds1-1.2/debian/patches/remove-JavadocTaglet.patch
Patch2:         jdk17.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
BuildRequires:  java-devel >= 1:1.6.0
BuildRequires:  ant
BuildRequires:  jpackage-utils
BuildRequires:  batik
BuildRequires:  jericho-html
BuildRequires:  xml-commons-apis
BuildRequires:  apache-commons-cli
Requires:       apache-commons-cli
Requires:       xml-commons-apis
Requires:       jericho-html
Requires:       batik
Requires:       jpackage-utils
Requires:       java-headless >= 1:1.6.0

%description
ditaa is a small command-line utility written in Java, that can
convert diagrams drawn using ASCII art ('drawings' that contain
characters that resemble lines like | / - ), into proper bitmap
graphics.

%prep 
%autosetup -p1
find -name '*.class' -delete
find -name '*.jar' -delete

%build
install -d bin
build-jar-repository -s -p lib commons-cli batik-all xml-commons-apis-ext jericho-html
ant -f build/release.xml

%install
install -D -p -m 0644 releases/%{name}0_9.jar %{buildroot}%{_javadir}/%{name}.jar
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}

%files
%doc COPYING HISTORY
%{_bindir}/%{name}
%{_javadir}/%{name}.jar

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.10-27
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Terje Rosten <terje.rosten@ntnu.no> - 0.10-25
- Use autosetup macro

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 0.10-24
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 0.10-18
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.10-17
- changed bytecode level to 8

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.10-16
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 19 2020 Terje Rosten <terje.rosten@ntnu.no> - 0.10-11
- Add patch from Debian to build with JDK 10+

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0.10-10
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Terje Rosten <terje.rosten@ntnu.no> - 0.10-1
- 0.10
- New upstream location

* Mon Aug 31 2015 Michal Srb <msrb@redhat.com> - 0.9-15.r74
- Fix FTBFS (Resolves: rhbz#1239429)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-14.r74
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-13.r74
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 0.9-12.r74
- Use Requires: java-headless rebuild (#1067528)

* Tue Oct 22 2013 Terje Rosten <terje.rosten@ntnu.no> - 0.9-11.r74
- Switch to unversioned jar (bz #1022093)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-10.r74
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-9.r74
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-8.r74
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 07 2012 Terje Rosten <terje.rosten@ntnu.no> - 0.9-7.r74
- Switch from jakarta- to apache- (bz #818492)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-6.r74
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-5.r74
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 26 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.9-4.r74
- Pull sources from svn do get working ditaa using system jericho

* Tue Jun 22 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.9-3
- Use system jericho-html

* Mon Jun 21 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.9-2
- Be more generic about jdk 1.6 buildreq
- Add req on jdk 1.6
- Include some jars to wrapper

* Sun Jun 20 2010 Terje Rosten <terje.rosten@ntnu.no> - 0.9-1
- initial build
