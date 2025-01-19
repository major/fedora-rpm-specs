Version:	20170904
Release:	21%{?dist}
URL:		http://fonts.jp/hanazono/

%global	foundry		hanamin
## https://gitlab.com/fedora/legal/fedora-license-data/-/issues/179#note_1331780205
%global	fontlicense	LicenseRef-Fedora-UltraPermissive OR OFL-1.1-RFN
%global	fontlicenses	LICENSE.txt
%global	fontdocs	README.txt THANKS.txt
%global	fontdocsex	%{fontlicenses}

%global	fontfamily	HanaMin
%global	fontsummary	Japanese Mincho-typeface TrueType font
%global	fontpkgheader	%{expand:
Obsoletes:	hanazono-fonts < %{version}-%{release}
Provides:	hanazono-fonts = %{version}-%{release}
}
%global	fonts0		HanaMin*.ttf
%global	fontconfs0	%{SOURCE1}
%global	fontdescription0	%{expand:
Hanazono Mincho typeface is a Japanese TrueType font that developed with
a support of Grant-in-Aid for Publication of Scientific Research Results from
Japan Society for the Promotion of Science and the International Research
Institute for Zen Buddhism (IRIZ), Hanazono University. also with volunteers
who work together on glyphwiki.org.

This font contains 107518 characters in ISO/IEC 10646 and Unicode Standard,
also supports character sets:
 - 6355 characters in JIS X 0208:1997
 - 5801 characters in JIS X 0212:1990
 - 3695 characters in JIS X 0213:2004
 - 6763 characters in GB 2312-80
 - 13053 characters in Big-5
 - 4888 characters in KS X 1001:1992
 - 360 characters in IBM extensions
 - 9810 characters in IICORE
 - Kanji characters in GB18030-2000
 - Kanji characters in Adobe-Japan1-6
}

Source0:	http://ja.osdn.net/projects/hanazono-font/downloads/68253/hanazono-%{version}.zip
Source1:	66-%{fontpkgname0}.conf

%fontpkg -a

%prep
%setup -q -T -c -a 0

%build
%fontbuild -a
for f in %{fontdocs}; do
  sed -e "s/\\r\$//" $f > $f.tmp && touch -r $f $f.tmp && mv $f.tmp $f
done

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr  4 2023 Akira TAGOH <tagoh@redhat.com> - 20170904-16
- Migrated license tag to SPDX.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 13 2020 Akira TAGOH <tagoh@redhat.com> - 20170904-9
- Fix CRLF to LF in docs. (#1825183)

* Fri Apr 17 2020 Akira TAGOH <tagoh@redhat.com> - 20170904-8
- Use new fonts rpm macro.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun  5 2019 Akira TAGOH <tagoh@redhat.com> - 20170904-5
- Install metainfo files under %%{_metainfodir}.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170904-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Akira TAGOH <tagoh@redhat.com> - 20170904-1
- Updates to 20170904.
- Update the priority to change the default font to Noto.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20141012-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20141012-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20141012-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan  4 2016 Akira TAGOH <tagoh@redhat.com>
- Use %%global instead of %%define.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20141012-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 20141012-2
- Add metainfo file to show this font in gnome-software
- Remove %%clean section which is optional now
- Remove buildroot which is optional now
- Remove removal of buildroot in %%install
- Remove group tag

* Wed Oct 15 2014 Akira TAGOH <tagoh@redhat.com> - 20141012-1
- New upstream release. (#1152054)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20131208-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 11 2013 Akira TAGOH <tagoh@redhat.com> - 20131208-1
- New upstream release. (#1039477)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130222-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Akira TAGOH <tagoh@redhat.com> - 20130222-1
- New upstream release. (#914077)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120421-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 25 2012 Akira TAGOH <tagoh@redhat.com> - 20120421-1
- New upstream release.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120202-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Akira TAGOH <tagoh@redhat.com> - 20120202-1
- New upstream release. (#786779)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20110915-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 16 2011 Akira TAGOH <tagoh@redhat.com> - 20110915-1
- New upstream release. (#738594)
- Update License tag to make this dual license with SIL OFL since 20101013.

* Thu May 26 2011 Akira TAGOH <tagoh@redhat.com> - 20110516-1
- New upstream release. (#705302)

* Fri Apr  8 2011 Akira TAGOH <tagoh@redhat.com> - 20101013-1
- New upstream release. (#692826)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100718-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 27 2010 Akira TAGOH <tagoh@redhat.com> - 20100718-1
- New upstream release.
  - contains certain glyphs to cover Japanese (#586213)

* Tue May 25 2010 Akira TAGOH <tagoh@redhat.com> - 20100222-3
- Improve the fontconfig config file to match ja as well.

* Mon Apr 19 2010 Akira TAGOH <tagoh@redhat.com> - 20100222-2
- Get rid of compare="contains".

* Fri Apr 16 2010 Akira TAGOH <tagoh@redhat.com> - 20100222-1
- Update to 20100222.
- Get rid of binding="same" from fontconfig config file. (#578019)

* Fri Nov 27 2009 Akira TAGOH <tagoh@redhat.com> - 20091003-1
- Update to 20091003.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20081012-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20081012-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 24 2008 Akira TAGOH <tagoh@redhat.com> - 20081012-6
- Update the spec file to fit into new guideline. (#477395)

* Fri Nov 14 2008 Akira TAGOH <tagoh@redhat.com> - 20081012-5
- Fix a typo in fontconfig config again.

* Thu Nov 13 2008 Akira TAGOH <tagoh@redhat.com> - 20081012-4
- Try to test the language with the exact match in fontconfig config.

* Wed Nov 12 2008 Akira TAGOH <tagoh@redhat.com> - 20081012-3
- Fix a typo in fontconfig config.

* Mon Nov 10 2008 Akira TAGOH <tagoh@redhat.com>
- Drop -f from fc-cache.
- Improve fontconfig config.

* Mon Nov 10 2008 Akira TAGOH <tagoh@redhat.com> - 20081012-2
- Improve a bit in the spec file.

* Tue Oct 28 2008 Akira TAGOH <tagoh@redhat.com> - 20081012-1
- Initial packaging.

