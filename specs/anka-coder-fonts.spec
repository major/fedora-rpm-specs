%global fontname anka-coder
%global fontconf 65-%{fontname}
%global hgrev 4348cf4ec395


%global common_desc \
The Anka/Coder family is a mono spaced, courier-width (60% of height; em size \
2048x1229) font that contains characters from 437, 866, 1251, 1252 and some \
other code pages and can be used for source code, terminal windows etc. \
There are 3 font sets (regular. italic, bold, bold-italic each): 1. \
Anka/Coder (em size 2048x1229) 2. Anka/Coder Condensed (condensed by \
12.5%; em size 2048x1075) 3. Anka/Coder Narrow (condensed by 25%; em \
size 2048x922)

Name:           %{fontname}-fonts
Version:        1.100
Release:        0.23.20130409hg%{hgrev}%{?dist}
Summary:        A mono spaced, courier-width font

# Automatically converted from old format: OFL - review is highly recommended.
License:        LicenseRef-Callaway-OFL
URL:            http://code.google.com/p/anka-coder-fonts/

# Generated from an hg clone since sfd sources were available
# hg clone https://code.google.com/p/anka-coder-fonts/
# tar -cvzf anka-coder-fonts-20130409-hg.tar.gz --exclude="\.hg" anka-coder-fonts/
Source0:        anka-coder-fonts-20130409-hg.tar.gz
Source1:        %{name}-norm.conf
Source2:        %{name}-condensed.conf
Source3:        %{name}-narrow.conf
Source4:        %{fontname}.metainfo.xml
Source5:        %{fontname}-condensed.metainfo.xml
Source6:        %{fontname}-narrow.metainfo.xml
Source7:        %{fontname}-norm.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  fontforge
Requires:       fontpackages-filesystem

%description
%common_desc

%package common
Summary:        Common files of %{name}
Requires:       fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.


%package -n %{fontname}-norm-fonts
Summary:        Normal version of %{name}
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-norm-fonts
%common_desc

"Anka/Coder Norm" simply supplements the family. 


%_font_pkg -n norm -f %{fontconf}-norm.conf AnkaCoder-b.ttf AnkaCoder-bi.ttf AnkaCoder-i.ttf AnkaCoder-r.ttf
%doc AnkaCoder-b-sample.pdf AnkaCoder-bi-sample.pdf AnkaCoder-i-sample.pdf AnkaCoder-r-sample.pdf
%{_datadir}/appdata/%{fontname}-norm.metainfo.xml

# Repeat for every font family ➅
%package -n %{fontname}-condensed-fonts
Summary:        Condensed version of %{name}
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-condensed-fonts
%common_desc

"Anka/Coder Condensed" can be used for both printing and screen 
viewing of source code, also as for displaying terminal windows.


%_font_pkg -n condensed -f %{fontconf}-condensed.conf AnkaCoder-C87*.ttf
%doc AnkaCoder-C87-b-sample.pdf AnkaCoder-C87-bi-sample.pdf AnkaCoder-C87-i-sample.pdf AnkaCoder-C87-r-sample.pdf
%{_datadir}/appdata/%{fontname}-condensed.metainfo.xml

%package -n %{fontname}-narrow-fonts
Summary:        Narrow version of %{name}
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-narrow-fonts
%common_desc

"Anka/Coder Narrow" was developed for printing of source code; it \
is too tight for screen resolution.

%_font_pkg -n narrow -f %{fontconf}-narrow.conf AnkaCoder-C75*.ttf
%doc AnkaCoder-C75-b-sample.pdf AnkaCoder-C75-bi-sample.pdf AnkaCoder-C75-i-sample.pdf AnkaCoder-C75-r-sample.pdf
%{_datadir}/appdata/%{fontname}-narrow.metainfo.xml

%prep
%setup -q -n %{name}

%build
for family in "AnkaCoder" "AnkaCoder Condensed" "AnkaCoder Narrow"
do
pushd "$family"
fontforge -lang=ff -script "-" *.sfd <<EOF
i = 1 
while ( i < \$argc )
  Open (\$argv[i], 1)
  Generate (\$fontname + ".ttf")
  PrintSetup (5) 
  PrintFont (0, 0, "", \$fontname + "-sample.pdf")
  Close()
  i++
endloop
EOF
mv *.ttf ../ -v
mv *.pdf ../ -v
popd
done

sed -i 's/\r//' AnkaCoder/OFL.txt

%install
install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-norm.conf

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-condensed.conf

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-narrow.conf

mkdir -p %{buildroot}/%{_datadir}/appdata/
cp %{SOURCE4} %{buildroot}/%{_datadir}/appdata/  -v
cp %{SOURCE5} %{buildroot}/%{_datadir}/appdata/  -v
cp %{SOURCE6} %{buildroot}/%{_datadir}/appdata/  -v
cp %{SOURCE7} %{buildroot}/%{_datadir}/appdata/  -v

for fconf in %{fontconf}-norm.conf \
             %{fontconf}-condensed.conf \
             %{fontconf}-narrow.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done



%files common
%license AnkaCoder/OFL.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.23.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.100-0.22.20130409hg4348cf4ec395
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.21.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.20.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.19.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.18.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.17.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.16.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.15.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.14.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.13.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.12.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.11.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.10.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.9.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.8.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.7.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.6.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.5.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.100-0.4.20130409hg4348cf4ec395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.100-0.3.20130409hg
- Update as per reviewer comments: rbhz 949954
- Mark license with new license macro
- do not own appdata dir
- removed defattr - not needed
- remove rm -rf at beginning of install section
- use prerelease release tag
- 

* Tue Jul 28 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.100-2
- Include metainfo information

* Tue Apr 09 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.100-1
- Initial rpmbuild

