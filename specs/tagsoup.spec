# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distributio4.3n.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Name:           tagsoup
Version:        1.2.1
Release:        37%{?dist}
Epoch:          0
Summary:        A SAX-compliant HTML parser written in Java 
# AFL/GPLv2+ license for src/java/org/ccil/cowan/tagsoup/PYXScanner.java is
# likely mixup of upstream but needs to be cleared up
# Automatically converted from old format: ASL 2.0 and (GPLv2+ or AFL) - review is highly recommended.
License:        Apache-2.0 AND (GPL-2.0-or-later OR LicenseRef-Callaway-AFL)
Source0:        http://vrici.lojban.org/~cowan/XML/tagsoup/tagsoup-1.2.1-src.zip
URL:            http://vrici.lojban.org/~cowan/XML/tagsoup/
Source1:        https://repo1.maven.org/maven2/org/ccil/cowan/tagsoup/tagsoup/%{version}/tagsoup-%{version}.pom
# fix version
Patch0:         tagsoup-1.2.1-man.patch
Patch1:         sourceTargetJdk8.patch
BuildRequires:  javapackages-local-openjdk25
BuildRequires:  ant-openjdk25 
BuildRequires:  ant-apache-xalan2
BuildRequires:  xalan-j2

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
TagSoup is a SAX-compliant parser written in Java that, instead of
parsing well-formed or valid XML, parses HTML as it is found in the wild: nasty
and brutish, though quite often far from short. TagSoup is designed for people
who have to process this stuff using some semblance of a rational application
design. By providing a SAX interface, it allows standard XML tools to be
applied to even the worst HTML.

%package javadoc
Summary:       Javadoc for %{name}
Requires:      jpackage-utils >= 0:1.6

%description javadoc
Javadoc for %{name}.

%prep
%setup -q

find . -name '*.class' -delete
find . -name "*.jar" -delete

%patch -P0 -p0
%patch -P1 -p1

%build

export CLASSPATH=$(build-classpath xalan-j2-serializer xalan-j2)
ant \
  -Dtagsoup.version=%{version} \
  -Dj2se.apiurl=%{_javadocdir}/java \
  dist docs-api

%install
%mvn_file : %{name}
%mvn_artifact %{SOURCE1} dist/lib/%{name}-%{version}.jar

%mvn_install

mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/

%files -f .mfiles
%{_mandir}/man1/%{name}.1.gz
%doc CHANGES README TODO %{name}.txt
%license LICENSE

%files javadoc
%license LICENSE

%changelog
* Tue Jul 29 2025 jiri vanek <jvanek@redhat.com> - 0:1.2.1-37
- Rebuilt for java-25-openjdk as preffered jdk

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0:1.2.1-34
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 0:1.2.1-32
- Rebuilt for java-21-openjdk as system jdk

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 0:1.2.1-27
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0:1.2.1-26
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 0:1.2.1-21
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon May 04 2020 Jiri Vanek <jvanek@redhat.com.org> - 0:1.2.1-20
- moved to source/target 1.8
- dropped javadoc, jdk  faisl to build it with the tempaltes

* Fri Feb 14 2020 Jiri Vanek <jvanek@redhat.com.org> - 0:1.2.1-19
- package rised from dead and fixed few small issues

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Michael Simacek <msimacek@redhat.com> - 0:1.2.1-13
- Install with XMvn

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 13 2015 gil cattaneo <puntogil@libero.it> 0:1.2.1-9
- introduce license macro

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 29 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.2.1-7
- Use .mfiles generated during build

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.2.1-4
- Remove ppc64 ExcludeArch
- Resolves: rhbz#502328

* Thu Nov 08 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.2.1-3
- Upstream relicensed to ASL 2.0, but likely accidentally left some things

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 09 2012 gil cattaneo <puntogil@libero.it> 0:1.2.1-1
- Upgraded to 1.2.1
- remove ant-nodeps reference
- changed group in javadoc sub package (from Development/Documentation in Documentation)
- add maven metadata
- add manual
- Adapt to current guidelines.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0.1-7
- BR ant-apache-xalan2.

* Tue Dec 21 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0.1-6
- BR java 6.

* Tue Dec 21 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.0.1-5
- Fix FTBFS.
- Drop gcj.
- Adapt to current guidelines.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.1-4.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 24 2009 Milos Jakubicek <xjakub@fi.muni.cz> - 0:1.0.1-3.3
- Fix FTBFS: disabled ppc64 build

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.0.1-3.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.0.1-2.2
- drop repotag
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:1.0.1-2jpp.1
- Autorebuild for GCC 4.3

* Mon Feb 12 2007 Vivek Lakshmanan <vivekl@redhat.com> 0:1.0.1-1jpp.1.fc7
- rpmlint fixes
- Use fedora approved naming convention
- Fix buildroot to conform to Fedora packaging guidelines
- Add LICENSE to the rpm and label as doc
- Remove Vendor and Distribution tags
- Minor formatting fixes
- Use proper javaoc handling
- Add requires and requires(x) on jpackage-utils
- Add GCJ support
- BR on ant-trax and xalan-j2

* Sun Jan 20 2007 Sebastiano Vigna <vigna@dsi.unimi.it> 0:1.0.1-1jpp
- Upgraded to 1.0.1

* Mon Feb 27 2006 Fernando Nasser <fnasser@redhat.com> 0:1.0rc-2jpp
- First JPP 1.7 version

* Fri Jan 28 2005 Sebastiano Vigna <vigna@acm.org> 0:1.0rc-1jpp
- First JPackage version
