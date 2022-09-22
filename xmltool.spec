Name:           xmltool
Version:        3.3
Release:        34%{?dist}
Summary:        Tool to manage XML documents through a Fluent Interface

License:        ASL 2.0
URL:            http://code.google.com/p/xmltool
### upstream only provides binaries or source without build scripts
# tar creation instructions
# svn export http://xmltool.googlecode.com/svn/tags/xmltool-3.3 xmltool
# tar cfJ xmltool-3.3.tar.xz xmltool
Source0:        %{name}-%{version}.tar.xz
Patch0:         fix-deprecated-assembly-goal.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-local
BuildRequires:  maven-remote-resources-plugin
BuildRequires:  maven-source-plugin
BuildRequires:  maven-surefire-provider-testng
BuildRequires:  apache-resource-bundles

%description
XMLTool is a very simple Java library to be able to do all sorts of common 
operations with an XML document. Java developers often end up writing the same 
code for processing XML, transforming, etc. This easy to use class puts it all 
together, using the Fluent Interface pattern to facilitate XML manipulations. 

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}

%if 0%{?fedora} >= 26
%patch0 -p0
%endif

# Fix end-of-line encoding
sed -i 's/\r//' LICENSE.txt

%mvn_file : %{name}

# Remove dep on maven-wagon and maven-license plugins
%pom_xpath_remove "pom:build/pom:extensions"
%pom_remove_plugin com.google.code.maven-license-plugin:maven-license-plugin

# remove maven-compiler-plugin configuration that is broken with Java 11
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

%build
# Disable tests because they require an internet connection to run!
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 3.3-33
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.3-32
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Fabio Valentini <decathorpe@gmail.com> - 3.3-27
- Set javac source and target to 1.8 to fix Java 11 builds.

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 3.3-26
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 05 2019 Filipe Rosset <rosset.filipe@gmail.com> - 3.3-23
- Fix FTBFS fixes rhbz#1606745 and rhbz#1676234

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.3-20
- Escape macros in %%changelog

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 04 2017 Merlin Mathesius <mmathesi@redhat.com> - 3.3-17
- Correct deprecated assembly goal that was eliminated from
  maven-assembly-plugin 3.x to fix FTBFS (BZ#1401633).

* Wed Dec 14 2016 Merlin Mathesius <mmathesi@redhat.com> - 3.3-16
- Add missing BuildRequires for maven-source-plugin to fix FTBFS (BZ#1401633).
- Relocate %%pom_* macros to %%prep section in accordance with Java packaging guidelines.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 25 2015 Alexander Kurtakov <akurtako@redhat.com> 3.3-13
- Rebuild for new style maven metadata.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 3.3-11
- Use Requires: java-headless rebuild (#1067528)

* Thu Aug 29 2013 Mat Booth <fedora@matbooth.co.uk> - 3.3-10
- Update for newer guidelines, rhbz #993147

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 03 2013 Mat Booth <fedora@matbooth.co.uk> - 3.3-8
- Fix FTBFS rhbz #914589.
- Drop pom patch (use macros instead.)
- Include licence file in javadoc package.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.3-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 29 2011 Alexander Kurtakov <akurtako@redhat.com> 3.3-3
- Build with maven 3.
- Adapt to current guidelines.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat May 08 2010 Guido Grazioli <guido.grazioli@gmail.com> - 3.3-1
- Initial packaging
