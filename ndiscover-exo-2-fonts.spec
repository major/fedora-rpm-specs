# SPDX-License-Identifier: MIT
%global forgeurl    https://github.com/NDISCOVER/Exo-2.0
%global commit      22a4e995451acbc50634a8399c4a0ded6aa7d75e
%forgemeta

Version: 2.000
Release: 7%{?dist}
URL:     %{forgeurl}

%global foundry           NDISCOVER
%global fontlicense       OFL
%global fontlicenses      OFL.txt
%global fontdocs          *txt *md
%global fontdocsex        %{fontlicenses}

%global fontfamily        Exo 2
%global fontsummary       Exo 2, a contemporary geometric sans serif font family
%global fonts             fonts/otf/*otf fonts/vf/*ttf
%global fontconfngs       %{SOURCE10}
%global fontdescription   %{expand:
Exo 2 is a complete redrawing of Exo, a contemporary geometric sans serif
font family that tries to convey a technological/futuristic feeling while keeping
an elegant design. Exo is a very versatile font, so it has 9 weights (the
maximum on the web) and each with a true italic version. Exo 2 has a more
organic look that will perform much better at small text sizes and in long
texts.}

Source0:  %{forgesource}
Source10: 60-%{fontpkgname}.xml

%fontpkg

%prep
%forgesetup

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Feb 24 2022 Akira TAGOH <tagoh@redhat.com>
- 1.100-6.20200215git55728cf
- Fix FTBFS

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.100-4.20200215git55728cf
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.100-3.20200215git55728cf
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.100-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 1.100-1.20191208git0e2d90b
✅ Initial packaging
