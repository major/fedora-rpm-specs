%global fontname wqy-microhei
%global fontconf 66-%{fontname}.conf

%global archivename %{fontname}-%{version}-beta

Name:           %{fontname}-fonts
Version:        0.2.0
Release:        0.31.beta%{?dist}
Summary:        Compact Chinese fonts derived from Droid

License:        ASL 2.0 or GPLv3 with exceptions
URL:            http://wenq.org/enindex.cgi?MicroHei(en)
Source0:        http://downloads.sourceforge.net/wqy/%{archivename}.tar.gz
Source1:        %{name}-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

%description
A new Sans Serif CJK font derived from Google's "Droid Sans Fallback"
and covers the entire GBK code points (20932 Han glyphs).

%prep
%autosetup -n %{fontname}

mv README.txt{,.orig}
iconv -f iso8859-1 -t utf8 README.txt.orig > README.txt


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttc %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}



%_font_pkg -f %{fontconf} *.ttc
%license LICENSE_Apache2.txt LICENSE_GPLv3.txt
%doc README.txt


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.31.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.30.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.29.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.28.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.27.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.26.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.25.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.24.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.23.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Akira TAGOH <tagoh@redhat.com> - 0.2.0-0.22.beta
- Modernize the spec file.
- Update the fontconfig priority to make Noto default.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.21.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.20.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.19.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.18.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-0.17.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-0.16.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Aug  5 2014 Peng Wu <pwu@redhat.com> - 0.2.0-0.15.beta
- Fixes fontconfig conf

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-0.14.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May  7 2014 Peng Wu <pwu@redhat.com> - 0.2.0-0.13.beta
- Increase fontconfig conf file priority

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-0.12.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-0.11.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-0.10.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-0.9.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 26 2011  Peng Wu <pwu@redhat.com> - 0.2.0-0.8.beta
- Update wqy-microhei-fonts-fontconfig.conf

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-0.7.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 31 2010  Peng Wu <pwu@redhat.com> - 0.2.0-0.6.beta
- Add fontconfig file back to wqy-microhei-fonts.

* Wed May 26 2010  Peng Wu <pwu@redhat.com> - 0.2.0-0.5.beta
- Clean up rpm spec file and remove unused patches.

* Wed May 26 2010  Peng Wu <pwu@redhat.com> - 0.2.0-0.4.beta
- Improves Simplified Chinese and Traditional Chinese fonts.
  In order to keep the WenQuanYi Zen Hei as default Simplified Chinese font,
  the fontconfig file of this WenQuanYi Micro Hei font is removed.

* Mon Apr 19 2010  Peng Wu <pwu@redhat.com> - 0.2.0-0.3.beta
- get rid of binding="same", fixes [rhbz#578050] (New: lang-specific overrides rule doesn't work as expected).

* Mon Dec  7 2009 Jens Petersen <petersen@redhat.com> - 0.2.0-0.1.beta
- initial packaging for fedora
