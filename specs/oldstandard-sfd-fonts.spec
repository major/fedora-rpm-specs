%global fontname    oldstandard
%global fontconf    60-%{fontname}.conf

Name:       %{fontname}-sfd-fonts
Version:    2.0.2
Release:    39%{?dist}
Summary:    Old Standard True-Type Fonts

# Automatically converted from old format: OFL - review is highly recommended.
License:    LicenseRef-Callaway-OFL
# Also at https://fonts.google.com/specimen/Old+Standard+TT
URL:        https://fontlibrary.org/en/font/old-standard
Source0:    http://www.thessalonica.org.ru/downloads/oldstandard-2.0.2.src.zip
Source1:    %{name}-fontconfig.conf
Source2:    http://www.thessalonica.org.ru/downloads/oldstand-manual.pdf
Source3:        %{fontname}.metainfo.xml

# guidelines say this can be used

BuildArch:  noarch
BuildRequires:  fontforge,fontpackages-devel
Requires:   fontpackages-filesystem

%description
The Old Standard font family is an attempt to revive
a specific type of Modern (classicist) style of serif
typefaces, very commonly used in various editions
printed in the late 19th and early 20th century,
but almost completely  abandoned later.


%prep
%setup -q -c -n oldstandard-%{version}

for i in $(ls OldStandard*.sfd);do
    sed -i -e 's/OldStandardTT/OldStandardSFD/'  -e 's/Old \Standard \TT/Old \Standard \SFD/' $i;
done
for txt in OFL* ; do
    sed 's/\r//' $txt > $txt.new
    touch -r $txt $txt.new
    mv $txt.new $txt
done

install -m 644 -p %{SOURCE2} .

%build
fontforge -lang=ff -script "-" OldStandard*.sfd <<EOF
i = 1 
while ( i < \$argc )
  Open (\$argv[i], 1)
  Generate (\$fontname + ".otf")
  PrintSetup (5) 
  PrintFont (0, 0, "", \$fontname + "-sample.pdf")
  Close()
  i++ 
endloop
EOF

%install
install -m 755 -d %{buildroot}%{_fontdir}
install -m 644 -p *.otf %{buildroot}%{_fontdir}

install -m 755 -d %{buildroot}%{_fontconfig_templatedir} \
        %{buildroot}%{_fontconfig_confdir}

install -m 644 -p %{SOURCE1} \
    %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
    %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.otf
%doc *.txt *.pdf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.2-38
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 05 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 2.0.2-26
- Use an existing URL
- https://bugzilla.redhat.com/show_bug.cgi?id=1718521

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 10 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 2.0.2-18
- define -> global

* Fri Oct 02 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 2.0.2-17
- Use otf since ttf isnt generated properly

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Oct 18 2014 Parag Nemade <pnemade AT redhat DOT com> - 2.0.2-15
- Add metainfo file to show this font in gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild


* Mon Mar 16 2009 Ankur Sinha <ankursinha at fedoraproject.org> - 2.0.2-7
- changed in accordance with #490369
* Sun Mar 15 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net> - 2.0.2-5
— Make sure F11 font packages have been built with F11 fontforge

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Ankur Sinha <ankursinha@fedoraproject.org>
- 2.0.2-3
- corrected the fontconfig
* Sun Jan 4 2009 Ankur Sinha <ankursinha@fedoraproject.org>
- 2.0.2-2
- Rebuild according to new packaging guidelines
* Mon Dec 15 2008 Ankur Sinha <ankursinha@fedoraproject.org> 
- 2.0.2-1
- Rebuilt for f10 with minor changes to spec file. (#457947 at bugzilla)
- changed version number as per FONTLOG.txt in source zip file.
