# Due to changes in the Fedora legal environment, rpm spec files are now specifically listed as a "contribution" 
# in/to Fedora (refer to FPCA FAQ here: https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement ).
# Quote: 
# "Q. Are RPM spec files covered by the FPCA?
# A. Sure. They're a contribution, aren't they? :) Nevertheless, they are explicitly named as an example of a contribution, to clear up a past confusion."
# 
# As a result of this change, I have decided to specifically license all of my rpm spec files as GPLv2.
# See program source for a copy of this license.
#

%global fontname        thibault
%global conf1           69-essays1743.conf
%global conf2           69-isabella.conf
%global conf3           69-rockets.conf
%global conf4           69-staypuft.conf

%define common_desc \
A collection of fonts from thibault.org,\
including Isabella, Essays1743, StayPuft,\
and Rockets.

Name:           %{fontname}-fonts
Version:        0.1
Release:        43%{?dist}

Summary:        Thibault.org font collection
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+

URL:            http://www.thibault.org/fonts
Source0:        http://www.thibault.org/fonts/essays/essays1743-2.000-1-ttf.tar.gz
Source1:        http://thibault.org/fonts/isabella/Isabella-1.2-ttf.tar.gz
Source2:        http://www.thibault.org/fonts/rockets/Rockets-ttf.tar.gz
Source3:        http://www.thibault.org/fonts/staypuft/StayPuft.tar.gz
Source4:        %{name}-essays1743-fontconfig.conf
Source5:        %{name}-isabella-fontconfig.conf
Source6:        %{name}-rockets-fontconfig.conf
Source7:        %{name}-staypuft-fontconfig.conf

Source10:       %{fontname}-essays1743.metainfo.xml
Source11:       %{fontname}-isabella.metainfo.xml
Source12:       %{fontname}-rockets.metainfo.xml
Source13:       %{fontname}-staypuft.metainfo.xml

#Not included due to legal concerns
#Engadget: A sort of modernistic font done to match the logo of http://www.engadget.com


BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  fontforge >= 20061025-1

%description
%common_desc

%package common
Summary:        Common files for thibault (documentation…)
Requires:       fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.

%package -n %{fontname}-essays1743-fonts

Summary:  Thibault.org Montaigne's Essays typeface font

Requires: %{name}-common = %{version}-%{release}
Obsoletes: %{name}-essays1743 < 0.1-17

%description -n %{fontname}-essays1743-fonts
%common_desc

A font by John Stracke, based on the
typeface used in a 1743 English
translation of Montaigne's Essays.

%_font_pkg -n essays1743 -f %{conf1} Essays1743*.ttf
%{_datadir}/appdata/%{fontname}-essays1743.metainfo.xml

%package -n %{fontname}-isabella-fonts

Summary: Thibault.org Isabella Breviary calligraphic font

Requires: %{name}-common = %{version}-%{release}
Obsoletes: %{name}-isabella < 0.1-17

%description -n %{fontname}-isabella-fonts
%common_desc

This font is called Isabella because it is based on the
calligraphic hand used in the Isabella Breviary, made around 1497, in
Holland, for Isabella of Castille, the first queen of united Spain.

%_font_pkg -n isabella -f %{conf2} Isabella*.ttf
%{_datadir}/appdata/%{fontname}-isabella.metainfo.xml

%package -n %{fontname}-rockets-fonts

Summary:  Thibault.org font, vaguely space themed

Requires: %{name}-common = %{version}-%{release}
Obsoletes: %{name}-rockets < 0.1-17

%description -n %{fontname}-rockets-fonts
%common_desc

This font is called Rockets because it's vaguely space
themed.  The A is, more or less, a 1950s SF rocket; the O is meant to
be Earth, with the Americas visible.  The other capitals are based on
curves from either A or O, to keep the theme consistent.

%_font_pkg -n rockets -f %{conf3} Rockets*.ttf
%{_datadir}/appdata/%{fontname}-rockets.metainfo.xml

%package -n %{fontname}-staypuft-fonts

Summary: Thibault.org font, rounded and marshmellowy

Requires: %{name}-common = %{version}-%{release}
Obsoletes: %{name}-staypuft < 0.1-17

%description -n %{fontname}-staypuft-fonts
%common_desc

A rounded marshmellow type font. Good for frivolous things
like banners, and birthday cards.

%_font_pkg -n staypuft -f %{conf4} StayPuft*.ttf
%{_datadir}/appdata/%{fontname}-staypuft.metainfo.xml

%prep
mkdir -p staypuft
tar xvzf %{SOURCE0}
tar xvzf %{SOURCE1}
tar xvzf %{SOURCE2}
tar xvzf %{SOURCE3} -C staypuft

%build

pushd essays1743
fontforge -lang=ff -c 'Open($1); Generate($2)' Essays1743.sfd ../Essays1743.ttf
fontforge -lang=ff -c 'Open($1); Generate($2)' Essays1743-Bold.sfd ../Essays1743-Bold.ttf
fontforge -lang=ff -c 'Open($1); Generate($2)' Essays1743-BoldItalic.sfd ../Essays1743-BoldItalic.ttf
fontforge -lang=ff -c 'Open($1); Generate($2)' Essays1743-Italic.sfd ../Essays1743-Italic.ttf
popd

pushd Isabella
fontforge -lang=ff -c 'Open($1); Generate($2)' Isabella-first.sfd ../Isabella.ttf
popd

pushd rockets
fontforge -lang=ff -c 'Open($1); Generate($2)' Rockets.sfd ../Rockets.ttf
popd

pushd staypuft
fontforge -lang=ff -c 'Open($1); Generate($2)' StayPuft.sfd ../StayPuft.ttf
popd

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE4} \
        %{buildroot}%{_fontconfig_templatedir}/%{conf1}


install -m 0644 -p %{SOURCE5} \
        %{buildroot}%{_fontconfig_templatedir}/%{conf2}

install -m 0644 -p %{SOURCE6} \
        %{buildroot}%{_fontconfig_templatedir}/%{conf3}

install -m 0644 -p %{SOURCE7} \
        %{buildroot}%{_fontconfig_templatedir}/%{conf4}

for fconf in %{conf1} \
                %{conf2} \
                %{conf3} \
                %{conf4} ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE10} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-essays1743.metainfo.xml
install -Dm 0644 -p %{SOURCE11} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-isabella.metainfo.xml
install -Dm 0644 -p %{SOURCE12} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-rockets.metainfo.xml
install -Dm 0644 -p %{SOURCE13} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-staypuft.metainfo.xml

%files common
%doc essays1743/COPYING essays1743/README
%doc Isabella/COPYING.LIB Isabella/README.txt
%doc rockets/COPYING.LIB rockets/README.txt
%doc staypuft/COPYING.LIB staypuft/README.txt

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.1-42
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Oct 18 2014 Richard Hughes <richard@hughsie.com> - 0.1-23
- Add a MetaInfo file for the software center; this is a font we want to show.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 7 2012 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> - 0.1-18
- Fixed error in Isabella build section

* Sat Jan 7 2012 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> - 0.1-17
- Fixed error in Essays build section

* Sun Dec 25 2011 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> - 0.1-16
- Updated Essays1743 and Isabella to current versions.

* Fri Mar 4 2011 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> - 0.1-15
- Added new license header for spec file.

* Sun Feb 7 2010 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> - 0.1-14
- More source errors

* Sun Feb 7 2010 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> - 0.1-13
- Fix souces errors

* Sun Feb 7 2010 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> - 0.1-12
- Update Isabella font to current version
- Rebuild for F13

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 15 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net> - 0.1-10
— Make sure F11 font packages have been built with F11 fontforge


#thibault
* Mon Mar 2 2009 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> 0.1-9
- Edited to censor to fit the whining nature of Fedora PC Freaks.

* Mon Mar 2 2009 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> 0.1-8
- Typo.

* Mon Mar 2 2009 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> 0.1-7
- Fontforge script errors fixed.

* Mon Mar 2 2009 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> 0.1-6
- Fixed error in fontforge script that was 
- caused by some f***er turning on python bindings.

* Mon Mar 2 2009 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> 0.1-5
- Fixed errors in previous modifications.
- Updated for latest policy changes.
- Deleted erroneous edits made by jkeating.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 11 2009 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> 0.1-3
- Modified spec file to comply with new policy changes.

* Sat Sep 06 2008 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> 0.1-2
- Rebuild for new fontforge release.

* Fri Jul 18 2008 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com>
- Fixed minor issues found during review.

* Mon Jul 15 2008 Matt Domsch <mdomsch@fedoraproject.org>
- Rewrote spec file to comply with fedora's policies

* Thu Jul 10 2008 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com>
- Removed the Engadget font due to legal concerns

* Wed Jul 09 2008 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com>
- Fixed post and postun issues to stay in specs that Fedora requires.
- Fixed define issues.
- Created multiple source rpm
- Fixed issues with setup block

* Fri Jul 04 2008 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com>
- compiled collection of thibault.org fonts into single rpm

#rockets
* Sun Jan 29 2006 John Stracke <francis@thibault.org>
- based on specfile of Isabella-ttf.

#engadget
* Sun Aug 28 2005 John Stracke <francis@thibault.org>
- based on specfile of isabella-ttf.

#isabella
* Sun Jul 03 2005 John Stracke <francis@thibault.org>
- Finally getting rid of the Greek-letters-pretending-to-be-ligatures
  and moving them up to the Private Use Area.

* Sun Oct 31 2004 John Stracke <francis@thibault.org>
- adding reference to bold (added italic a bit ago)

#essays1743
* Sun Oct 31 2004 John Stracke <francis@thibault.org>
- adding reference to bold (added italic a bit ago)

* Wed Oct 06 2004 John Stracke <francis@thibault.org>
- based on specfile of RedHat 9 urw-fonts.

#isabella
* Wed Oct 06 2004 John Stracke <francis@thibault.org>
- based on specfile of RedHat 9 urw-fonts.

