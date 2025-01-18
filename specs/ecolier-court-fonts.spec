# SPDX-License-Identifier: MIT
Version: 20070702
Release: 48%{?dist}
# This used to be published here, copies are all over the web now
#URL:     http://perso.orange.fr/jm.douteau/page_ecolier.htm

%global fontlicense       OFL-1.1
%global fontlicenses      lisez_moi.txt
%global fontdocs          README-Fedora.txt

%global common_description %{expand:
The Écolier court font families were created by Jean-Marie Douteau to mimic the
traditional cursive writing French children are taught in school.

He kindly released two of them under the OFL, which are redistributed in this
package.}

%global fontfamily0       Ecolier Court
%global fontsummary0      Écolier Court, a schoolchildren cursive Latin font family
%global fontpkgheader0    %{expand:
Obsoletes: ecolier-court-fonts-common < %{version}-%{release}
}
%global fonts0            %{SOURCE10}
%global fontconfngs0      %{SOURCE20}
%global fontdescription0  %{expand:
%{common_description}}

%global fontfamily1       Ecolier Lignes Court
%global fontsummary1      Écolier Lignes Court, a schoolchildren cursive Latin font family with lines
%global fontpkgheader1    %{expand:
Obsoletes: ecolier-court-lignes-fonts < %{version}-%{release}
}
%global fonts1            %{SOURCE11}
%global fontconfngs1      %{SOURCE21}

%global fontdescription1  %{expand:
%{common_description}

The « lignes » (lines) Écolier Court font variant includes the Seyes lining
commonly used on schoolchildren notepads.}

Source0:  lisez_moi.txt
Source1:  README-Fedora.txt
Source10: ec_cour.ttf
Source11: ecl_cour.ttf
Source20: 61-%{fontpkgname0}.xml
Source21: 61-%{fontpkgname1}.xml

%fontpkg -a

%fontmetapkg

%prep
%setup -q -c -T
install -m 0644 -p %{SOURCE0} %{SOURCE1} .
%linuxtext *.txt

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20070702-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20070702-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20070702-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20070702-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20070702-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20070702-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20070702-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20070702-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Akira TAGOH <tagoh@redhat.com>
- 20070702-40
- Fix FTBFS

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

 Wed Apr 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070702-35
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070702-34
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070702-33
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Mon Mar 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070702-32
✅ Lint, lint, lint and lint again

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070702-31
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 20070702-29
✅ Convert to fonts-rpm-macros use

* Sat Jul 19 2008 Nicolas Mailhot <nim@fedoraproject.org>
- 20070702-1
✅ Initial packaging
