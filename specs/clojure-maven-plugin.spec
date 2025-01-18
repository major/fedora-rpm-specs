%global upstream    talios
%global groupId     com.theoryinpractise
%global artifactId  clojure-maven-plugin

Name:           %{artifactId}
Version:        1.9.3
Release:        2%{?dist}
Summary:        Clojure plugin for Maven

License:        EPL-1.0
URL:            https://github.com/%{upstream}/%{name}
# wget --content-disposition %%{url}/tarball/%%{version}
Source0:        %{URL}/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.commons:commons-io)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

%description
This plugin has been designed to make working with clojure as easy as
possible, when working in a mixed language, enterprise project.


%prep
%setup -q -n %{artifactId}-%{artifactId}-%{version}

# release plugin is not required for RPM builds
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :ossindex-maven-plugin
%pom_remove_plugin :cyclonedx-maven-plugin

%build
# test1.clj does not get discovered if LANG=C
# also, using 'package' instead of 'install' to avoid
# running integration tests - they do installation tests
# for a lot of packages*versions we do not currently have
export LANG=en_US.utf8
# Do not run tests cause we miss dependencies fest-assert
# and maven-surefire-provider-junit5
%mvn_build -f -j


%install
%mvn_install

%files -f .mfiles
%license epl-v10.html 
%doc README.markdown


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 09 2024 Markku Korkeala <markku.korkeala@iki.fi> - 1.9.3-1
- Update to upstream release 1.9.3, closes rhbz#2312181
- Remove porting to commons-lang3

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.9.2-6
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 24 2023 Markku Korkeala <markku.korkeala@iki.fi> - 1.9.2-3
- Remove build requires dependency  mvn(org.apache.maven:maven-toolchain)

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 22 2023 Markku Korkeala <markku.korkeala@iki.fi> - 1.9.2-1
- Update to upstream release 1.9.2
- Remove unnecessary plugins from pom

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.8.4-7
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.8.4-6
- Rebuilt for java-17-openjdk as system jdk

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1.8.4-1
- Update to 1.8.4 release.

* Fri Jul 24 2020 Fabio Valentini <decathorpe@gmail.com> - 1.8.1-8
- Port to commons-lang3.

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.8.1-7
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Fri May 01 2020 Fabio Valentini <decathorpe@gmail.com> - 1.8.1-6
- Regenerate BuildRequires with xmvn-builddep and drop redundant Requires.

* Sat Apr 04 2020 Markku Korkeala <markku.korkeala@iki.fi> - 1.8.1-5
- Rebuilt for Fedora 33 rawhide

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 25 2019 Markku Korkeala <markku.korkeala@iki.fi> - 1.8.1-3
- Fix license short name to EPL-1.0
- Update BuildRequires to use mvn(org.apache.maven:maven-toolchain)

* Sun Feb 10 2019 Markku Korkeala <markku.korkeala@iki.fi> - 1.8.1-2
- Remove jpackage-utils from (Build)Requires
- Use license macro for file epl-v10.html 
- Remove unnecessary Epoch

* Sat Jan 05 2019 Markku Korkeala <markku.korkeala@iki.fi> - 1.8.1-1
- Update to upstream 1.8.1
- Update to Xmvn macros
- Remove maven-surefire-provider-junit4 and fest-assert build requirement

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.3.10-6
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.3.10-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun  8 2012 Michel Salim <salimma@fedoraproject.org> - 1.3.10-1
- Initial package
