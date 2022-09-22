Name:           jnr-constants
Version:        0.9.12
Release:        13%{?dist}
Summary:        Java Native Runtime constants 
License:        ASL 2.0
URL:            https://github.com/jnr/%{name}/
Source0:        https://github.com/jnr/%{name}/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)

%description
Provides java values for common platform C constants (e.g. errno).

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete
%mvn_file : %{name}/%{name} %{name} constantine

# remove unnecessary dependency on parent POM
%pom_remove_parent

# Unnecessary for RPM builds
%pom_remove_plugin ":maven-javadoc-plugin"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 0.9.12-12
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 0.9.12-11
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Aug 30 2020 Fabio Valentini <decathorpe@gmail.com> - 0.9.12-7
- Remove unnecessary dependency on parent POM.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0.9.12-5
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 08 2018 Mat Booth <mat.booth@redhat.com> - 0.9.12-1
- Update to latest upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Mat Booth <mat.booth@redhat.com> - 0.9.9-1
- Update to latest release and fix FTBFS

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Alexander Kurtakov <akurtako@redhat.com> 0.9.6-1
- Update to upstream 0.9.6.

* Fri Dec 16 2016 Merlin Mathesius <mmathesi@redhat.com> - 0.9.2-2
- Add missing BuildRequires to fix FTBFS (BZ#1405569).

* Thu May 19 2016 Alexander Kurtakov <akurtako@redhat.com> 0.9.2-1
- Update to upstream 0.9.2 release.

* Mon Apr 18 2016 Alexander Kurtakov <akurtako@redhat.com> 0.9.1-1
- Update to upstream 0.9.1 with osgification.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 16 2015 Alexander Kurtakov <akurtako@redhat.com> 0.9.0-1
- Update to upstream 0.9.0.

* Thu Jun 18 2015 Jeff Johnston <jjohnstn@redhat.com> 0.8.8-2
- Add MANIFEST.MF.

* Tue Jun 16 2015 Alexander Kurtakov <akurtako@redhat.com> 0.8.8-1
- Update to upstream 0.8.8.
- Switch to mvn() style BRs.

* Mon May 11 2015 Michal Srb <msrb@redhat.com> - 0.8.7-2
- Restore symlinks for backward compatibility

* Tue May 5 2015 Alexander Kurtakov <akurtako@redhat.com> 0.8.7-1
- Update to upstream 0.8.7.

* Thu Apr 30 2015 Alexander Kurtakov <akurtako@redhat.com> 0.8.6-1
- Update to upstream 0.8.6.
- Start using mvn_install.

* Thu Jun 12 2014 Alexander Kurtakov <akurtako@redhat.com> 0.8.4-6
- Fix FTBFS.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 0.8.4-4
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8.4-2
- Provide a constantine.jar simlink for gradle.

* Tue Feb 05 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8.4-1
- Updated to version 0.8.4.
- Switch from ant to maven.

* Tue Oct 09 2012 gil cattaneo <puntogil@libero.it> 0.7-6
- add maven pom
- adapt to current guideline

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 02 2010 Mohammed Morsi <mmorsi@redhat.com> - 0.7-2
- Fixed incorrect Source0 url

* Fri Jan 22 2010 Mohammed Morsi <mmorsi@redhat.com> - 0.7-1
- Unorphaned / updated package

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 6 2008 Conrad Meyer <konrad@tylerc.org> - 0.4-2
- Include LICENSE in rpm.

* Fri Nov 28 2008 Conrad Meyer <konrad@tylerc.org> - 0.4-1
- Include symlink from non-versioned jar to versioned jar.
- Bump to 0.4.

* Fri Nov 28 2008 Conrad Meyer <konrad@tylerc.org> - 0.1-1
- Initial package (needed for jruby 1.1.5).
