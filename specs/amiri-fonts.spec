Version: 1.000
Release: 6%{?dist}
URL:     http://www.amirifont.org

%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          README.md README-Arabic.md Documentation-Arabic.html
%global fontdocsex        %{fontlicenses}

%global common_description %{expand:
Amiri is a revival of the beautiful typeface pioneered in early 20th
century by Bulaq Press in Cairo, also known as Amiria Press, after which
the font is named.
}

%global common_description_ar %{expand:
تميزت به مطبعة بولاق منذ أوائل القرن العشرين، والتي عرفت
أيضًا بالمطبعة الأميرية، ومن هنا أخذ الخط اسمه.
}

%global fontfamily0       Amiri
%global fontsummary0      A classical Arabic font in Naskh style
%global fontpkgheader0    %{expand:
Obsoletes: amiri-fonts-common < %{version}-%{release}
}
%global fonts0            Amiri-Regular.ttf Amiri-Italic.ttf Amiri-BoldItalic.ttf Amiri-Bold.ttf
%global fontconfs0        %{SOURCE10}
%global fontdescription0  %{expand:%{common_description}

Amiri is a classical Arabic typeface in Naskh style for typesetting books
and other running text.
%{common_description_ar}

الخط الأميري خط نسخي موجه لطباعة الكتب والنصوص الطويلة.
الخط الأميري هو إحياء ومحاكاة للخط الطباعي الجميل الذي

}

%global fontfamily1       Amiri Quran
%global fontsummary1      Quran type of Amiri fonts
%global fonts1            AmiriQuran.ttf
%global fontconfs1        %{SOURCE11}
%global fontdescription1  %{expand:%{common_description}

This package contains Quran type of Amiri fonts.

%{common_description_ar}

تحتوي هذه الحُزمة على النّمط القرآني من الخط الأميري.
}

%global fontfamily2       Amiri Quran Colored
%global fontsummary2      None
%global fonts2            AmiriQuranColored.ttf
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:%{common_description}
This package contains Quran Colored type of Amiri fonts.

%{common_description_ar}

تحتوي هذه الحزمة على نوع القرآن الملون من الخطوط الأميرية.
}


Source0:  https://github.com/alif-type/amiri/releases/download/%{version}/Amiri-%{version}.zip
Source10: 67-%{fontpkgname0}.conf
Source11: 67-%{fontpkgname1}.conf
Source12: 67-%{fontpkgname2}.conf

%fontpkg -a

%fontmetapkg

%prep
%setup -q -n Amiri-%{version}

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 12 2023 Mosaab Alzoubi <moceap[At]fedoraproject[Dot]org> - 1.000-1
- Update to 1.000
- Slanted types renamed

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.117-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 03 2022 Parag Nemade <pnemade AT redhat DOT com> - 0.117-1
- Convert spec to new fonts packaging guidelines
- Update to new upstream release 0.117

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.113-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.113-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.113-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 15 2021 Mosaab Alzoubi <moceap[At]hotmail[Dot]com> - 0.113-1
- Update to 0.113

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.112-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Mosaab Alzoubi <moceap[At]hotmail[Dot]com> - 0.112-1
- Update to 0.112

* Mon Sep 9 2019 Mosaab Alzoubi <moceap[At]hotmail[Dot]com> - 0.111-1
- Update to 0.111

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.109-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.109-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.109-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.109-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.109-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 28 2017 Mosaab Alzoubi <moceap@hotmail.com> - 0.109-1
- Update to 0.109

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.108-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.108-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 19 2015 Mosaab Alzoubi <moceap@hotmail.com> - 0.108-1
- New version with alot of additions and fixes
- New upstream moved to Github
- Add amiri-quran-colored font
- Use %%license macro
- Clean up spec file

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.107-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.107-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec 31 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.107-1
- Update to 0.107.
- Upstream use zip instead of gz.

* Wed Nov 13 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-9
- Change variable font priority to 67 in font_pkg line.
- Reform Summary.

* Mon Nov 11 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-8
- Re-split into main and Quran fonts.
- Improve Amiri Quran font config.
- Add license files to -common, dropped from others.
- Drop fontpackages-filesystem requires from main package.

* Mon Nov 11 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-7
- Fix Sourceforg link in Source0.
- Decrease instructions to rebuild Amiri from the source.
- Replace -docs by -common.
- Change font priority to 67.
- Improve font config.
- The fonts in one family so it united into 1 main package instead of 2.
- -common to be main package require.

* Mon Oct 28 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-6
- Replaces define by global.

* Mon Oct 28 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-5
- Drop .woff fonts.
- Update description by official one.
- Make this package ready for building if it possible later.

* Sun Oct 20 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-4
- Drop web and meta packages.
- Many Fixes.

* Sat Oct 19 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-3
- Rewritten almost from zero.

* Thu Oct 10 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-2
- Some fixes to be compatible with Fedora rules.

* Fri Oct 4 2013 Mosaab Alzoubi <moceap@hotmail.com> - 0.106-1
- Update version to 0.106
- Update description by adding Amiri summary in Arabic
- Font released in two licenses (GPL2,OFL1.1)
- Make universal source

* Mon Dec 19 2011  Muayyad Salah Alsadi <alsadi@ojuba.org> - 0.100-2
- no need for web version
- make it -fonts not -font (see http://fedoraproject.org/wiki/Packaging:FontsPolicy)

* Mon Dec 19 2011  Ehab El-Gedawy <ehabsas@gmail.com> - 0.100-1
- Initial Packaging
