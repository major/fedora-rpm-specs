Name:           weld-parent
Version:        46
Release:        10%{?dist}
Summary:        Parent POM for Weld
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0

URL:            http://weld.cdi-spec.org
Source0:        https://github.com/weld/parent/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)

%description
Parent POM for Weld

%prep
%setup -q -n parent-%{version}

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-remote-resources-plugin
%pom_remove_plugin :maven-source-plugin

%pom_remove_dep :maven-scm-api


%build
%mvn_build

%install
%mvn_install

%files -f .mfiles

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 46-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 46-9
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 46-7
- Rebuilt for java-21-openjdk as system jdk

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 46-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 46-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 46-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 46-2
- Rebuilt for Drop i686 JDKs

* Sat Apr 09 2022 Markku Korkeala <markku.korkeala@iki.fi> - 46-1
- Update to version 46.

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 45-3
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 07 2021 Markku Korkeala <markku.korkeala@iki.fi> - 45-1
- Update to version 45.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 01 2021 Fabio Valentini <decathorpe@gmail.com> - 44-1
- Update to version 44.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 24 2020 Fabio Valentini <decathorpe@gmail.com> - 42-1
- Update to version 42.

* Tue Aug 11 2020 Fabio Valentini <decathorpe@gmail.com> - 41-1
- Update to version 41.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 40-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Mon Feb 17 2020 Alexander Scheel <ascheel@redhat.com> - 40-1
- Update to version 40.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 20 2019 Fabio Valentini <decathorpe@gmail.com> - 39-1
- Update to version 39.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 34-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 34-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 34-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 34-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 06 2017 Michael Simacek <msimacek@redhat.com> - 34-3
- Remove buildnumber-plugin

* Wed Jun 15 2016 gil cattaneo <puntogil@libero.it> 34-2
- Add missing BRs on maven-source-plugin, buildnumber-maven-plugin

* Mon Jun 06 2016 gil cattaneo <puntogil@libero.it> 34-1
- Upstream release 34

* Tue Mar 01 2016 gil cattaneo <puntogil@libero.it> 31-4
- remove enforcer plugin support
- related to rhbz#1308237,1308238
- use BRs mvn()-like
- introduce license macro

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Marek Goldmann <mgoldman@redhat.com> - 31-1
- Upstream release 31

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Oct 23 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 26-2
- Rebuild to regenerate broken POM files
- Related: rhbz#1021484

* Tue Oct 22 2013 Marek Goldmann <mgoldman@redhat.com> - 26-1
- Upstream release 26

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Michal Srb <msrb@redhat.com> - 17-8
- Add ASL 2.0 license text
- Add missing BR: maven-plugin-build-helper, maven-install-plugin

* Tue Feb 19 2013 Marek Goldmann <mgoldman@redhat.com> - 17-7
- Added maven-shared BR

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 17-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Jul 23 2012 Marek Goldmann <mgoldman@redhat.com> - 17-4
- Fixed BR, removed maven plugins from R

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Marek Goldmann <mgoldman@redhat.com> 17-2
- Added build section

* Wed Mar 14 2012 Marek Goldmann <mgoldman@redhat.com> 17-1
- Initial packaging

