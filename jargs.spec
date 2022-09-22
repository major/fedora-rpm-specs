Name:           jargs
Version:        1.0
Release:        34%{?dist}
Summary:        Java command line option parsing suite

License:        BSD
URL:            http://jargs.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        https://repository.jboss.org/nexus/content/repositories/thirdparty-releases/net/sf/jargs/1.0/jargs-1.0.pom
#               Update source and target for JDK 17
Patch0:         %{name}-java-version.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  ant
BuildRequires:  junit


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
%{summary}.


%description
This project provides a convenient, compact, pre-packaged and 
comprehensively documented suite of command line option parsers 
for the use of Java programmers. 
Initially, parsing compatible with GNU-style 'getopt' is provided.

%prep
%setup -q
%patch0 -p1
find -name '*.jar' -o -name '*.class' -exec rm -f '{}' \;


%build
%ant runtimejar javadoc


%install
%mvn_artifact %{SOURCE1} lib/%{name}.jar
%mvn_alias net.sf:%{name} %{name}:%{name}
%mvn_install -J doc


%files -f .mfiles
%doc README TODO doc/CHANGES
%license LICENCE


%files javadoc -f .mfiles-javadoc
%license LICENCE


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.0-33
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.0-32
- Rebuilt for java-17-openjdk as system jdk
- Update source and target for JDK 17

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.0-27
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed May 06 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0-26
- Update source and target for JDK 11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 08 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.0-20
- Update for newer guidelines

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 03 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0-15
- Fix FTBFS due to XMvn changes in F21 (#1106822)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0-13
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 12 2013 Mat Booth <fedora@matbooth.co.uk> - 1.0-12
- Add maven pom/depmap, rhbz #821123
- Update for newer guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 19 2009 Guido Grazioli <guido.grazioli@gmail.com> 1.0-5
- sanitized %%files
- fixed Source url again, according to Fedora guidelines
* Sat May 09 2009 Guido Grazioli <guido.grazioli@gmail.com> 1.0-4
- added junit within BuildRequires
- fixed Source url
* Sat May 09 2009 Guido Grazioli <guido.grazioli@gmail.com> 1.0-3
- removed versioned jar
* Sat May 09 2009 Guido Grazioli <guido.grazioli@gmail.com> 1.0-2
- fixed BuildRequires and Requires tags
- made javadoc package require main package
* Wed May 06 2009 Guido Grazioli <guido.grazioli@gmail.com> 1.0-1
- initial packaging
