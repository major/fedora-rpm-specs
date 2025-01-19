Name:		jglobus
Version:	2.1.0
Release:	39%{?dist}
Summary:	Globus Java client libraries

#		Everything is Apache 2.0 except for one file that is MIT:
#		ssl-proxies/src/main/java/org/globus/tools/GridCertRequest.java
License:	Apache-2.0 AND MIT
URL:		http://github.com/%{name}/JGlobus
Source0:	%{url}/archive/JGlobus-Release-%{version}.tar.gz
#		DERObjectIdentifier is obsolete
#		https://github.com/jglobus/JGlobus/pull/149
Patch0:		%{name}-DERObjectIdentifier-is-obsolete.patch
#		Don't force SSLv3 in myproxy, allow TLS
#		Backport from git (trunk)
Patch1:		%{name}-dont-force-SSLv3.patch
#		Relax proxy validation to be RFC-3820 compliant
#		https://github.com/jglobus/JGlobus/issues/160
#		https://github.com/jglobus/JGlobus/pull/165
Patch2:		%{name}-key-usage.patch
#		Fix javadoc
#		https://github.com/jglobus/JGlobus/pull/162
Patch3:		%{name}-javadoc.patch
#		Do not accumulate matches in
#		GlobusPathMatchingResourcePatternResolver
#		https://github.com/jglobus/JGlobus/pull/157
Patch4:		%{name}-do-not-accumulate-matches-in-GlobusPathMatchingResou.patch
#		Compatibility with clients that request minimum TLS version 1.2
#		https://github.com/jglobus/JGlobus/pull/166
Patch5:		%{name}-do-not-force-SSLv3-TLSv1-allow-TLSv1.1-TLSv1.2.patch
#		Remove synchronization on CRL in CRLChecker
#		Drop workaround for race condition in BouncyCastle < 1.46
#		Reduced lock contention leads to higher request throughput
#		Backport from git (trunk and 2.1 branch)
Patch6:		%{name}-remove-synchronization-on-CRL-in-CRLChecker.patch
#		Fix "no key" error for PKCS#8 encoded keys
#		https://github.com/jglobus/JGlobus/issues/118
#		https://github.com/jglobus/JGlobus/issues/146
#		https://github.com/jglobus/JGlobus/pull/164
Patch7:		%{name}-support-PKCS8-key-format.patch
#		Only allow TLSv1 and TLSv1.2 (not TLSv1.1)
#		https://github.com/jglobus/JGlobus/pull/166
Patch8:		%{name}-only-allow-TLSv1-and-TLSv1.2-not-TLSv1.1.patch
#		Remove unused FORCE_SSLV3_AND_CONSTRAIN_CIPHERSUITES_FOR_GRAM
#		https://github.com/jglobus/JGlobus/pull/166
Patch9:		%{name}-remove-unused-FORCE_SSLV3_AND_CONSTRAIN_CIPHERSUITES.patch
#		Adapt to changes in bouncycastle 1.61
#		https://github.com/jglobus/JGlobus/pull/168
Patch10:	%{name}-adapt-to-changes-in-PrivateKeyInfo-class.patch
#		DERInteger is obsolete
#		https://github.com/jglobus/JGlobus/pull/177
Patch11:	%{name}-DERInteger-is-obsolete.patch
#		DEROutputStream is private
#		https://github.com/jglobus/JGlobus/pull/177
Patch12:	%{name}-DEROutputStream-is-private.patch
#		ASN1OutputStream constructor is private - use create() method
#		https://github.com/jglobus/JGlobus/pull/183
Patch13:	%{name}-constructor-not-public.patch
#		DERBoolean is obsolete
#		https://github.com/jglobus/JGlobus/pull/185
Patch14:	%{name}-DERBoolean-is-obsolete.patch
#		DERTaggedObject.getObject() was removed - use .getInstance() instead
#		https://github.com/jglobus/JGlobus/pull/186
Patch15:	%{name}-DERTaggedObject.getObject-was-removed-use-.getInstan.patch
#		Reformat file to make linian happy
#		https://github.com/jglobus/JGlobus/pull/187
Patch16:	%{name}-Reformat-package.html-file.patch

BuildArch:	noarch
ExclusiveArch:	%{java_arches} noarch

BuildRequires:	maven-local
BuildRequires:	mvn(commons-codec:commons-codec)
BuildRequires:	mvn(commons-io:commons-io)
BuildRequires:	mvn(commons-logging:commons-logging)
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(log4j:log4j)
BuildRequires:	mvn(org.apache.httpcomponents:httpclient)
BuildRequires:	mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:	mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:	mvn(org.bouncycastle:bcprov-jdk18on)

%description
%{name} is a collection of Java client libraries for Globus Toolkit security,
GRAM, GridFTP and MyProxy.

%package parent
Summary:	Globus Java - parent pom file
License:	Apache-2.0

%description parent
Globus Java libraries parent maven pom file

%package ssl-proxies
Summary:	Globus Java - SSL and proxy certificate support
License:	Apache-2.0 AND MIT
Obsoletes:	%{name}-axisg < %{version}-%{release}
Obsoletes:	%{name}-ssl-proxies-tomcat < %{version}-%{release}

%description ssl-proxies
Globus Java library with SSL and proxy certificate support

%package jsse
Summary:	Globus Java - SSL support
License:	Apache-2.0
Requires:	%{name}-ssl-proxies = %{version}-%{release}

%description jsse
Globus Java library with SSL support

%package gss
Summary:	Globus Java - GSS-API implementation for SSL with proxies
License:	Apache-2.0
Requires:	%{name}-jsse = %{version}-%{release}

%description gss
Globus Java GSS-API implementation for SSL with proxies

%package gram
Summary:	Globus Java - Grid Resource Allocation and Management (GRAM)
License:	Apache-2.0
Requires:	%{name}-gss = %{version}-%{release}

%description gram
Globus Java library with GRAM support

%package gridftp
Summary:	Globus Java - GridFTP
License:	Apache-2.0
Requires:	%{name}-gss = %{version}-%{release}

%description gridftp
Globus Java library with GridFTP support

%package io
Summary:	Globus Java - IO
License:	Apache-2.0
Requires:	%{name}-gram = %{version}-%{release}
Requires:	%{name}-gridftp = %{version}-%{release}

%description io
Globus Java library with IO utilities

%package myproxy
Summary:	Globus Java - MyProxy
License:	Apache-2.0
Requires:	%{name}-gss = %{version}-%{release}

%description myproxy
Globus Java library with MyProxy support

%package javadoc
Summary:	Javadoc for %{name}
License:	Apache-2.0 AND MIT

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n JGlobus-JGlobus-Release-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 12 -p1
%patch -P 13 -p1
%patch -P 14 -p1
%patch -P 15 -p1
%patch -P 16 -p1

# Do not package test classes
%mvn_package org.jglobus:container-test-utils __noinstall
%mvn_package org.jglobus:test-utils __noinstall

# Avoid build dependency bloat
%pom_remove_parent

# Don't do source and release
%pom_remove_plugin org.apache.maven.plugins:maven-release-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin

# Remove source ant target settings (Java 1.5)
%pom_remove_plugin org.apache.maven.plugins:maven-compiler-plugin

# The gaxis module requires axis version 1.x
%pom_disable_module axis

# The tomcat module is not compatible with tomcat 8.5 or later
%pom_disable_module ssl-proxies-tomcat

# Update bouncycastle version
%pom_change_dep -r org.bouncycastle:bcprov-jdk15on org.bouncycastle:bcprov-jdk18on

%build
# Many tests requires network connections and a valid proxy certificate
%mvn_build -f -s -- -Dproject.build.sourceEncoding=UTF-8 -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files parent -f .mfiles-parent 
%license LICENSE

%files ssl-proxies -f .mfiles-ssl-proxies
%doc README.textile
%license LICENSE

%files jsse -f .mfiles-jsse

%files gss -f .mfiles-gss

%files gram -f .mfiles-gram

%files gridftp -f .mfiles-gridftp

%files io -f .mfiles-io

%files myproxy -f .mfiles-myproxy

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 14 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.1.0-37
- Adapt to changes in bouncycastle 1.77

* Thu Mar 07 2024 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.1.0-36
- Update License tags (SPDX)
- Remove old specfile conditionals

* Fri Mar 01 2024 Petra Alice Mikova <pmikova@redhat.com> - 2.1.0-35
- Set Java source/target to 1.8

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 2.1.0-34
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.1.0-28
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.1.0-27
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.1.0-25
- ASN1OutputStream constructor is private - use create() method

* Fri Nov 19 2021 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.1.0-24
- Prepare for JDK 17

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 10 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.1.0-21
- Adapt to changes in bouncycastle 1.67

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.1.0-19
- Remove maven-javadoc-plugin configuration (F33+, EPEL8+)

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.1.0-18
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed May 06 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.1.0-17
- Update source and target for JDK 11
- Add maven-javadoc-plugin configuration for JDK 11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jul 28 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.1.0-15
- Don't do source and release (Fixes build on 32 bit arches on Fedora 30)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.1.0-13
- Only allow TLSv1 and TLSv1.2 (not TLSv1.1)
- Remove unused FORCE_SSLV3_AND_CONSTRAIN_CIPHERSUITES_FOR_GRAM
- Adapt to changes in bouncycastle 1.61

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.1.0-11
- Apply patches from OSG/WLCG

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.1.0-9
- Disble axis and tomcat modules for Fedora >= 28 (missing dependencies)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.1.0-6
- Relax proxy validation to be RFC-3820 compliant
- Fix javadoc

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.1.0-3
- Fix compilation with bouncycastle 1.52
- Adapt to updated license packaging guidelines

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Oct 01 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.1.0-1
- 2.1.0 final release
- Drop patches included upstream
- Disable axis module for EPEL 7

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 06 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.6-4
- Apply patch for bouncycastle 1.47+ for Fedora 21+ and EPEL 7+

* Wed Sep 11 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.6-3
- Use xmvn instead of mvn-rpmbuild

* Thu Aug 15 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.6-2
- Adjust Java version

* Wed Aug 14 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.6-1
- 2.0.6 final release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.5-1
- 2.0.5 final release

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.0.5-0.2.rc2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 29 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.5-0.1.rc2
- 2.0.5 release candidate 2
- New jglobus-myproxy package
- New jglobus-axisg package

* Sat Oct 13 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.4-9.20121013git597e3ac
- Git snapshot

* Wed Oct 10 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.4-8.20121010git8eefd68
- Git snapshot
- Drop patches applied upstream

* Wed Oct 10 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.4-7.20121010git5286c6b
- Git snapshot
- Drop patches applied upstream

* Thu Sep 27 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.4-6
- Drop spring framework dependency (based on pull request in github)
- Allows building on EPEL

* Mon Aug 13 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.4-5
- Build the tomcat module

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 04 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.4-3
- Adapt to changes in automatic maven rpm dependency generation

* Mon Apr 23 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.4-2
- Add MIT license tag

* Fri Apr 13 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 2.0.4-1
- First packaging
