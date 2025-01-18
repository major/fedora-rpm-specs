%global short_name commons-digester

Name:          apache-%{short_name}
Version:       2.1
Release:       33%{?dist}
Summary:       XML to Java object mapping module
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:       Apache-2.0
URL:           http://commons.apache.org/digester/
BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch

Source0:       http://archive.apache.org/dist/commons/digester/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)

%description
Many projects read XML configuration files to provide initialization of
various Java objects within the system. There are several ways of doing this,
and the Digester component was designed to provide a common implementation
that can be used in many different projects

%package javadoc
Summary:       API documentation for %{name}

%description javadoc
This package contains the %{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src

# Compatibility links
%mvn_alias "%{short_name}:%{short_name}" "org.apache.commons:%{short_name}"
%mvn_file :%{short_name} %{short_name} %{name}

%build
%mvn_build -- -Dcommons.packageId=digester

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1-32
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 2.1-30
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 31 2024 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-29
- Port to apache-commons-parent 65

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.1-23
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.1-22
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Mat Booth <mat.booth@gmail.com> - 2.1-20
- Fix build on Java 17

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 2.1-16
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Fabio Valentini <decathorpe@gmail.com> - 2.1-14
- Add missing maven compiler source and target overrides.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-7
- Regenerate build-requires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1-4
- Remove legacy Obsoletes/Provides for jakarta-commons

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.1-2
- Use Requires: java-headless rebuild (#1067528)

* Wed Aug 21 2013 Mat Booth <fedora@matbooth.co.uk> - 2.1-1
- Update to latest upstream, rhbz #639893
- Update spec for latest guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-15
- Remove unneeded BR: maven-idea-plugin

* Mon Feb 18 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.8.1-14
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug  7 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.8.1-12
- Fix file permissions
- Install LICENSE and NOTICE with javadoc package

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Alexander Kurtakov <akurtako@redhat.com> 1.8.1-9
- Build with maven 3.
- Adapt to current guidelines.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri May 21 2010 Mat Booth <fedora@matbooth.co.uk> - 1.8.1-7
- Correct dep-map names.

* Fri May 14 2010 Mat Booth <fedora@matbooth.co.uk> - 1.8.1-6
- Obsolete jakarta javadoc package.
- Keep legacy depmap around.

* Thu May 13 2010 Mat Booth <fedora@matbooth.co.uk> - 1.8.1-5
- Drop really old obsoletes/provides on short_name.
- Fix requires.

* Tue May 11 2010 Mat Booth <fedora@matbooth.co.uk> - 1.8.1-4
- Not ready for auto OSGi depsolving yet in this package.
- Rename package (jakarta-commons-digester->apache-commons-digester).

* Tue Dec 8 2009 Mat Booth <fedora@matbooth.co.uk> - 1.8.1-3
- Enable OSGi automatic depsolving (from Alphonse Van Assche).

* Sun Nov 8 2009 Mat Booth <fedora@matbooth.co.uk> - 1.8.1-2
- Fix build failure due to targeting too old a JRE
- Add missing doxia build req

* Sun Nov 8 2009 Mat Booth <fedora@matbooth.co.uk> - 1.8.1-1
- Update to 1.8.1
- Rewrite spec file to build using upstream-preferred maven instead of ant
- Install pom and add to maven dep-map
- Fix javadoc package requires

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 0:1.7-10.3
- Convert specfile to UTF-8.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.7-9.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.7-8.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0:1.7-7.3
- fix license tag
- drop repotag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0:1.7-7jpp.2
- Autorebuild for GCC 4.3

* Fri Sep 07 2007 Matt Wringe <mwringe@redhat.com> - 0:1.7-6jpp.2
- Fix unowned dir (/usr/lib/gcj/jakarta-commons-digester)

* Mon Jan 22 2007 Vivek Lakshmanan <vivekl at redhat.com> - 0:1.7-6jpp.1
- Resynch with JPP release

* Tue Jan 16 2007 Vivek Lakshmanan <vivekl at redhat.com> - 0:1.7-5jpp.3
- Update component-info.xml to add scm and tag attribute instead of a comment
- Remove the export of a versioned jar

* Tue Jan 9 2007 Vivek Lakshmanan <vivekl at redhat.com> - 0:1.7-5jpp.2
- Upgrade to latest from JPP and FC6
- Remove old RHUG specific trigger
- Add support for conditional build of repolib package
- Build repolib package by default

* Thu Aug 10 2006 Matt Wringe <mwringe at redhat.com> - 0:1.7-5jpp.1
- Merge with upstream version:
 - Add missing requires for javadoc

* Thu Aug 10 2006 Karsten Hopp <karsten@redhat.de> 1.7-4jpp_3fc
- Requires(post/postun): coreutils

* Sat Jul 22 2006 Jakub Jelinek <jakub@redhat.com> - 0:1.7-4jpp_2fc
- Rebuilt

* Wed Jul 19 2006 Matt Wringe <mwringe at redhat.com> - 0:1.7-4jpp_1fc
- Merged with upstream version

* Wed Jul 19 2006 Matt Wringe <mwringe at redhat.com> - 0:1.7-4jpp
- Removed separate definition of name, version and release.

* Mon Jul 17 2006 Matt Wringe <mwringe at redhat.com> - 0:1.7-3jpp
- Added conditional native compiling

* Wed Apr 26 2006 Fernando Nasser <fnasser@redhat.com> - 0:1.7-2jpp
- First JPP 1.7 build

* Tue Jul 26 2005 Fernando Nasser <fnasser@redhat.com> - 0:1.7-1jpp
- Upgrade to 1.7

* Thu Nov 26 2004 Fernando Nasser <fnasser@redhat.com> - 0:1.6-2jpp
- Rebuild so that rss package is included

* Thu Oct 21 2004 Fernando Nasser <fnasser@redhat.com> - 0:1.6-1jpp
- Upgrade to 1.6

* Sun Aug 23 2004 Randy Watler <rwatler at finali.com> - 0:1.5-4jpp
- Rebuild with ant-1.6.2

* Fri May 09 2003 David Walluck <david@anti-microsoft.org> 0:1.5-3jpp
- update for JPackage 1.5

* Thu May 08 2003 Henri Gomez <hgomez@users.sourceforge.net> 1.5-2jpp
- used correct JPP 1.5 spec file

* Thu May 08 2003 Henri Gomez <hgomez@users.sourceforge.net> 1.5-2jpp
- 1.5
