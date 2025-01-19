Name:           jorbis
Version:        0.0.17
Release:        37%{?dist}
Summary:        Pure Java Ogg Vorbis Decoder
URL:            http://www.jcraft.com/jorbis/
License:        LGPLv2+
Source0:        http://www.jcraft.com/jorbis/%{name}-%{version}.zip
# Some fixes from the jorbis copy embedded in cortada. I've mailed upstream
# asking them to integrate these, for more info also see:
# https://trac.xiph.org/ticket/1565
# Note that although the original git headers were left in place for reference
# the actual patches have been rebased to 0.0.17 !
Patch0:         jorbis-0.0.17-cortado-fixes.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
BuildRequires:  java-devel
Requires:       java-headless
# We used to also package the comment editor example, but that is not so
# useful to end users (esp. the passing of cmdline args as java defines)
Obsoletes:      %{name}-comment <= 0.0.17-3

%description
JOrbis is a pure Java Ogg Vorbis decoder.


%package javadoc
Summary:        Java docs for jorbis

%description javadoc
This package contains the API documentation for jorbis.


%package player
Summary:        Java applet for playing ogg-vorbis files from a browser
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Requires:       java
Requires:       %{name} = %{version}-%{release}

%description player
This package contains JOrbisPlayer a simple java applet for playing
ogg-vorbis files from a browser.
See %{_docdir}/%{name}-player/JOrbisPlayer.html for
an example how to embed and use the applet.


%prep
%setup -q
%patch -P0 -p1


%build
javac com/jcraft/jogg/*.java com/jcraft/jorbis/*.java player/*.java
jar cf jogg.jar com/jcraft/jogg/*.class
jar cf jorbis.jar com/jcraft/jorbis/*.class
jar cf JOrbisPlayer.jar player/*.class
javadoc -d doc -public com/jcraft/*/*.java


%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -a *.jar $RPM_BUILD_ROOT%{_javadir}
cp -a doc $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%doc ChangeLog COPYING.LIB README
%{_javadir}/jogg.jar
%{_javadir}/jorbis.jar

%files javadoc
%doc COPYING.LIB
%{_javadocdir}/%{name}

%files player
%doc player/JOrbisPlayer.html
%{_javadir}/JOrbisPlayer.jar


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.0.17-36
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 0.0.17-34
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 0.0.17-28
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.0.17-27
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0.0.17-22
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 21 2014 Hans de Goede <hdegoede@redhat.com> - 0.0.17-11
- Make the main package require java-headless instead of java,
  the -player subpackage still requires full java (rhbz#1068302)
- Drop the unused jpackage-utils Requires

* Sat Aug 31 2013 Mat Booth <fedora@matbooth.co.uk> - 0.0.17-10
- Fix mention of documentation path in description

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov  9 2010 Hans de Goede <hdegoede@redhat.com> 0.0.17-4
- Provide a clean upgrade path from the old orphaned F-12 jorbis package

* Fri Nov  5 2010 Hans de Goede <hdegoede@redhat.com> 0.0.17-2
- Fix mixed use of spaces and tabs in spec file (#649777)
- Improved ilog2 fix in jorbis-0.0.17-cortado-fixes.patch

* Thu Nov  4 2010 Hans de Goede <hdegoede@redhat.com> 0.0.17-1
- Initial Fedora package
