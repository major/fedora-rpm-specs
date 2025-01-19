# SPDX-License-Identifier: MIT

%global fontname naver-nanum

BuildArch: noarch

Version: 3.020
Release: 39.20140930%{?dist}
License: OFL-1.1
URL:     http://hangeul.naver.com

%global foundry           Naver
%global fontlicenses      COPYING

%global common_description %{expand:
Nanum fonts are collection of commonly-used Myeongjo and Gothic Korean \
font families, designed by Sandoll Communication and Fontrix. The \
publisher is Naver Corporation.
}



%global fontfamily1       Nanum Barun Gothic
%global fontsummary1      Nanum fonts Barun Gothic font faces
%global fontpkgheader1    %{expand:
Provides:  %{name}-common = %{version}-%{release}
Obsoletes: %{name}-common < %{version}-%{release}
}
%global fonts1            NanumBarunGothic.ttf NanumBarunGothicBold.ttf NanumBarunGothicLight.ttf NanumBarunGothicUltraLight.ttf
%global fontconfs1        %{SOURCE11}
%global fontdescription1  %{expand:
%{common_description}

This package consists of the Nanum fonts Barun Gothic font faces.
}

%global fontfamily2       Nanum Barun Pen
%global fontsummary2      Nanum fonts Barun Pen font faces
%global fontpkgheader2    %{expand:
Provides:  %{name}-common = %{version}-%{release}
Obsoletes: %{name}-common < %{version}-%{release}
}
%global fonts2            NanumBarunpenR.ttf NanumBarunpenB.ttf
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}

This package consists of the Nanum fonts Barun Pen font faces.
}

%global fontfamily3       Nanum Brush
%global fontsummary3      Nanum fonts Brush font faces
%global fontpkgheader3    %{expand:
Provides:  %{name}-common = %{version}-%{release}
Obsoletes: %{name}-common < %{version}-%{release}
}
%global fonts3            NanumBrush.ttf
%global fontconfs3        %{SOURCE13}
%global fontdescription3  %{expand:
%{common_description}

This package consists of the Nanum fonts Brush font faces.
}

%global fontfamily4       Nanum Gothic
%global fontsummary4      Nanum fonts Gothic font faces
%global fontpkgheader4    %{expand:
Provides:  %{name}-common = %{version}-%{release}
Obsoletes: %{name}-common < %{version}-%{release}
}
%global fonts4            NanumGothic.ttf NanumGothicBold.ttf NanumGothicExtraBold.ttf NanumGothicLight.ttf
%global fontconfs4        %{SOURCE14}
%global fontdescription4  %{expand:
%{common_description}

This package consists of the Nanum fonts Gothic font faces.
}

%global fontfamily5       Nanum Myeongjo
%global fontsummary5      Nanum fonts Myeongjo font faces
%global fontpkgheader5    %{expand:
Provides:  %{name}-common = %{version}-%{release}
Obsoletes: %{name}-common < %{version}-%{release}
}
%global fonts5            NanumMyeongjo.ttf NanumMyeongjoBold.ttf NanumMyeongjoExtraBold.ttf
%global fontconfs5        %{SOURCE15}
%global fontdescription5  %{expand:
%{common_description}

This package consists of the Nanum fonts Myeongjo font faces.
}

%global fontfamily6       Nanum Pen
%global fontsummary6      Nanum fonts Pen font faces
%global fontpkgheader6    %{expand:
Provides:  %{name}-common = %{version}-%{release}
Obsoletes: %{name}-common < %{version}-%{release}
}
%global fonts6            NanumPen.ttf
%global fontconfs6        %{SOURCE16}
%global fontdescription6  %{expand:
%{common_description}

This package consists of the Nanum fonts Pen font faces.
}


# Need to convert from Windows executable to tar ball to avoid to use p7zip
#Source:    http://appdown.naver.com/naver/font/NanumFont/setup/NanumFontSetup_TTF_ALL_hangeulcamp.exe
# wget http://appdown.naver.com/naver/font/NanumFont/setup/NanumFontSetup_TTF_ALL_hangeulcamp.exe
# 7z x NanumFontSetup_TTF_ALL_hangeulcamp.exe
# tar zcvf NanumFont.tar.gz -C \$WINDIR/Fonts/ .
Source0:  NanumFont.tar.gz
# License text was taken from the upstream web on May 13 2014:
# http://help.naver.com/ops/step2/faq.nhn?faqId=15879
Source1:  %{name}-license.txt
Source11: 66-%{fontpkgname1}.conf
Source12: 66-%{fontpkgname2}.conf
Source13: 66-%{fontpkgname3}.conf
Source14: 66-%{fontpkgname4}.conf
Source15: 66-%{fontpkgname5}.conf
Source16: 66-%{fontpkgname6}.conf

Name:     %{fontname}-fonts
Summary:  Nanum family of Korean TrueType fonts
%description
%wordwrap -v common_description

%fontpkg -a

%fontmetapkg


%prep
%autosetup -c
cp %{SOURCE1} COPYING

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-39.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-38.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-37.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-36.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Mar  9 2023 Peng Wu <pwu@redhat.com> - 3.020-35.20140930
- Drop Obsoletes and Provides for nhn-nanum-fonts
- Update to follow New Fonts Packaging Guidelines

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-34.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 27 2022 msuchy <msuchy@redhat.com> - 3.020-33.20140930
- Migrate to SPDX license

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-32.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-31.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-30.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-29.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-28.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-27.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-26.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 3.020-25.20140930
- Install metainfo files under %%{_metainfodir}.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-24.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Akira TAGOH <tagoh@redhat.com> - 3.020-23.20140930
- Update the fontconfig priority again.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-22.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul  5 2018 Peng Wu <pwu@redhat.com> - 3.020-21.20140930
- Convert from Windows executable to tar ball to avoid to use p7zip

* Tue Jan 30 2018 Akira TAGOH <tagoh@redhat.com> - 3.020-20.20140930
- Update the priority to change the default font to Noto.

* Fri Dec 22 2017 Peng Wu <pwu@redhat.com> - 3.020-19.20140930
- Obsoletes nhn-nanum-gothic-light-fonts in naver-nanum-gothic-fonts package

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-18.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-17.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.020-16.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.020-15.20140930
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 3.020-14.20140930
- Add metainfo file to show this font in gnome-software
- Remove group tag from -common package

* Thu Oct  9 2014 Daiki Ueno <dueno@redhat.com> - 3.020-13.20140930
- new upstream release
- add -barun-pen-fonts subpackage
- add Light and UltraLight weight to -barun-gothic-fonts

* Thu Jul 17 2014 Daiki Ueno <dueno@redhat.com> - 3.020-12.20131007
- add missing Provides/Obsoletes for each subpackage (suggested by
  Jens Petersen in https://bugzilla.redhat.com/show_bug.cgi?id=1097985#c6)

* Thu Jul 10 2014 Daiki Ueno <dueno@redhat.com> - 3.020-11.20131007
- fix broken dependencies

* Tue Jun  3 2014 Daiki Ueno <dueno@redhat.com> - 3.020-10.20131007
- rename from nhn-nanum-fonts
- add fontconfig config file for NanumBarunGothic

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.020-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.020-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 26 2012 Daiki Ueno <dueno@redhat.com> - 3.020-7
- fix broken deps

* Thu Nov 22 2012 Daiki Ueno <dueno@redhat.com> - 3.020-6
- cleanup spec file

* Wed Nov 21 2012 Daiki Ueno <dueno@redhat.com> - 3.020-5
- include license file

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.020-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul  4 2012 Daiki Ueno <dueno@redhat.com> - 3.020-3
- simplify the last change

* Wed Jul  4 2012 Daiki Ueno <dueno@redhat.com> - 3.020-2
- fix <test> usage in fontconfig files (Closes: #837521)

* Mon Feb  6 2012 Daiki Ueno <dueno@redhat.com> - 3.020-1
- new upstream release
- update the priority
  nhn-nanum-fonts -> 65-0, un-core-fonts -> 65-1, baekmuk-ttf-fonts -> 65-2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Mar 30 2011 Daiki Ueno <dueno@redhat.com> - 3.010-1
- initial packaging for Fedora

