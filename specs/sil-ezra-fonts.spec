# SPDX-License-Identifier: MIT
Version: 2.51
Release: 17%{?dist}
URL:     https://scripts.sil.org/ezrasil_home

%global foundry           SIL
%global fontlicense       OFL-1.1-RFN
%global fontlicenses      Licenses.txt
%global fontdocs          *.txt
%global fontdocsex        %{fontlicenses}

%global common_description %{expand:
The Ezra SIL font families are fashioned after the square letter forms of the
typography of the Biblia Hebraica Stuttgartensia (BHS), a beautiful Old
Testament volume familiar to Biblical Hebrew scholars.

The different font families are available to provide two different styles of
cantillation marks. They were developed together, but there are some
differences in how they display markings. This was done intentionally.}

%global fontfamily0       Ezra SIL
%global fontsummary0      Ezra SIL, an Hebrew font family
%global fonts0            *.ttf
%global fontsex0          %{fonts1}
%global fontconfngs0      %{SOURCE10}
%global fontdescription0  %{expand:
%{common_description}

The Ezra SIL font family is supposed to render text identically to the printed BHS.}

%global fontfamily1       Ezra SIL SR
%global fontsummary1      Ezra SIL SR, an Hebrew font family
%global fonts1            *SR.ttf
%global fontconfngs1      %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

The Ezra SIL SR font has a different style of cantillation marks which may be
more familiar to users working with other editions.}

%global archivename %{lua:t=string.gsub(rpm.expand("%{fontfamily}%{version}"), "[%p%s]+", "");print(t)}

Source0:  https://scripts.sil.org/cms/scripts/render_download.php?format=file&media_id=%{archivename}.zip&filename=%{archivename}.zip#/%{archivename}.zip
Source10: 65-%{fontpkgname0}.xml
Source11: 65-%{fontpkgname1}.xml

%fontpkg -a

%fontmetapkg

%prep
%setup -q -c -T
unzip -j -q %{SOURCE0}
%linuxtext *.txt

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 25 2022 Akira TAGOH <tagoh@redhat.com>
- 2.51-11
- Fix FTBFS

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.51-5
🐞 Workaround Fedora problems created by rpm commit 93604e2

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.51-4
💥 Actually rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are
  valid

* Thu Apr 02 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.51-3
👻 Rebuild with fonts-rpm-macros 2.0.4 to make sure fontconfig files are valid

* Sat Feb 22 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.51-2
✅ Rebuild with fonts-rpm-macros 2.0.2

* Sat Feb 15 2020 Nicolas Mailhot <nim@fedoraproject.org>
- 2.51-1
✅ Initial packaging
