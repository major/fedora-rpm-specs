Name:		yuicompressor
Version:	2.4.8
Release:	17%{?dist}
Summary:	YUI Compressor - The Yahoo JavaScript and CSS Compressor

#		Source 0 is BSD, Source 1 is MPLv1.1 or GPLv2+
License:	BSD and (MPLv1.1 or GPLv2+)
URL:		https://yui.github.com/%{name}/
Source0:	https://github.com/yui/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
#		The yuicompressor uses the javascript parser from rhino.
#		However, it calls private functions not exported by the
#		rhino jar, so it can not use the jar provided by the
#		distribution. The upstream source unjars a bundled copy of
#		the rhino jar and builds using its precompiled class files.
#		This violates the no precompiled sources guidelines. Only
#		part of the rhino source tree is used by yuicompressor. The
#		upstream sources also contains modified versions of a few
#		of the rhino sources. These changes are restored by patch 0.
#		Source 1 is a slimmed down version of the rhino sources of
#		the same version that is bundled in the upstream sources.
#		Source 2 is the	script used to create Source 1.
Source1:	%{name}-rhino1_7R2.tar.gz
Source2:	%{name}-rhino.sh
#		Man page - copied from Debian
Source3:	%{name}.1
#		Pom file based on template from upstream:
#		https://github.com/yui/yuicompressor/raw/master/maven_central/template/pom.xml.template
Source4:	%{name}.pom
#		This patch restores yuicompressor's changes to the rhino
#		sources overwritten by Source 1
Patch0:		%{name}-rhino.patch
#		Remove references to prebuilt jars in build.xml
Patch1:		%{name}-remove-jars.patch
#		Fix test script - only test yuicompressor, not rhino
Patch2:		%{name}-tests.patch
#		Update source and target for JDK 17
Patch3:		%{name}-java-version.patch

BuildArch:	noarch
ExclusiveArch:	%{java_arches} noarch
BuildRequires:	ant
BuildRequires:	javapackages-local
BuildRequires:	mvn(net.sf:jargs)
Provides:	bundled(rhino) = 1.7R2
# Explicit requires for javapackages-tools since yuicompressor script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools

%description
The YUI Compressor is a JavaScript compressor which, in addition to
removing comments and white-spaces, obfuscates local variables using
the smallest possible variable name. This obfuscation is safe, even
when using constructs such as 'eval' or 'with' (although the
compression is not optimal in those cases) Compared to jsmin, the
average savings is around 20%.

The YUI Compressor is also able to safely compress CSS files. The
decision on which compressor is being used is made on the file
extension (js or css).

%prep
%setup -q -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
# Remove prebuilt jars
rm -rf lib/*
ln -s $(build-classpath jargs) lib

%build
%ant

%install
%mvn_artifact %{SOURCE4} build/%{name}-%{version}.jar
%mvn_install

%jpackage_script com.yahoo.platform.yui.compressor.Bootstrap "" "" jargs:%{name} %{name} true

mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 %{SOURCE3} %{buildroot}%{_mandir}/man1

%check
tests/suite.sh

%files -f .mfiles
%{_bindir}/%{name}
%doc %{_mandir}/man1/%{name}.1*
%doc README.md doc/CHANGELOG
%license LICENSE.TXT LICENSE.txt

%changelog
* Wed Sep 21 2022 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.4.8-17
- Fix test script
  - Don't use /dev/stderr (permission denied)
  - Replace egrep with grep -E

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.4.8-15
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.4.8-14
- Rebuilt for java-17-openjdk as system jdk
- Update source and target for JDK 17

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 2.4.8-9
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue May 05 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.4.8-8
- Update source and target for JDK 11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 31 2018 Severin Gehwolf <sgehwolf@redhat.com> - 2.4.8-4
- Add explicit requirement on javapackages-tools since yuicompressor
  script uses java-functions. See RHBZ#1600426.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 05 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 2.4.8-1
- Initial packaging for Fedora
