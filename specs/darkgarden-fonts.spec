# Due to changes in the Fedora legal environment, rpm spec files are now specifically listed as a "contribution" 
# in/to Fedora (refer to FPCA FAQ here: https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement ).
# Quote: 
# "Q. Are RPM spec files covered by the FPCA?
# A. Sure. They're a contribution, aren't they? :) Nevertheless, they are explicitly named as an example of a contribution, to clear up a past confusion."
# 
# As a result of this change, I have decided to specifically license all of my rpm spec files as GPLv2.
# See program source for a copy of this license.
# 

%global fontname darkgarden
%global fontconf 69-darkgarden.conf

Name:           %{fontname}-fonts
Version:	1.1
Release:        39%{?dist}
Summary:	Dark Garden is a decorative outline font of unusual shape

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://darkgarden.sourceforge.net/

Source0:        http://darkgarden.sourceforge.net/darkgarden-1.1.src.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:     noarch
BuildRequires: fontpackages-devel
BuildRequires: fontforge >= 20061025-1
Requires:      fontpackages-filesystem

%description
Dark Garden is a decorative outline font of unusual shape.
The typeface is based on author's original hand drawings.
The letterform is complex, with all characters decorated
with spikes resembling thorns or flames, character spacing
is very dense. Such a theme makes it a great font for titles,
banners, logos etc. Due to the font's complicated form,
long text passages are not very legible, but short paragraphs
such as titles or lyrics / poetry look very well.

%prep
%setup -q -n darkgarden-1.1 %{SOURCE0}

%build
fontforge -lang=ff -c 'Open($1); Generate($2)' DarkGarden.sfd DarkGarden.ttf

%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%doc COPYING.txt
%doc README.txt
%doc COPYING-GPL.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1-38
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Oct 18 2014 Parag Nemade <pnemade AT redhat DOT com> - 1.1-18
- Add metainfo file to show this font in gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Mar 04 2011 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> - 1.1-12
- Added new license header for spec file.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 15 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net> - 1.1-9
— Make sure F11 font packages have been built with F11 fontforge

* Mon Mar 2 2009 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> 1.1-8
- Fixed fontconfig problems caused by some f***er turning python bindings on.
- Deleted erroneous modifications made by rel-eng.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> 1.1-6
- Fixed errors in previous modifications.

* Sun Jan 11 2009 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> 1.1-5
- Modified spec file to comply with recent policy changes.

* Sat Sep 06 2008 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> 1.1-4
- rebuild with new release of fontforge.

* Sat Aug 02 2008 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com> 1.1-2
- initial import
- bumped release number

* Mon Jul 21 2008 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com>
- Modified spec file to more closely follow fedora's policy
- Checked spec and srpm against rpmlint and mock

* Fri Jul 11 2008 Lyos Gemini Norezel <Lyos.GeminiNorezel@gmail.com>
- Created DarkGarden font package

