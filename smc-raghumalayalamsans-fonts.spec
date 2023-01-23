%global fontname smc-raghumalayalamsans
%global fontconf 67-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	2.2.1
Release:	8%{?dist}
Epoch:		1
Summary:	Open Type Fonts for Malayalam script 
License:	GPLv2+
URL:		https://gitlab.com/smc/fonts/raghumalayalamsans
Source0:	%{url}/-/archive/Version%{version}/raghumalayalamsans-Version%{version}.tar.gz
Source1:	%{fontname}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml
BuildArch:	noarch
BuildRequires: make
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib
BuildRequires:	fontforge-devel
BuildRequires:	python3
BuildRequires:	python3-fonttools
Requires:	fontpackages-filesystem
Obsoletes:	smc-raghumalayalam-fonts < 6.1-11
Obsoletes:	smc-fonts-common < 6.1-11

%description
RaghuMalayalam is the name of a digital font - a typeface in 
Malayalam Script to be used for composing text in Malayalam language. 
It has been originally designed in Open Type Format with Unicode standards
and reordering as well as combining characters according to the visual 
syllable standard of IndiX Compugraphy.

%prep
%autosetup -n raghumalayalamsans-Version%{version}
chmod 644 *.txt
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .

%build
make PY=python3
mv build/*.ttf .

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
	%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}

install -Dm 0644 -p %{SOURCE2} \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

ln -s %{_fontconfig_templatedir}/%{fontconf} \
	%{buildroot}%{_fontconfig_confdir}/%{fontconf}

%check
appstream-util validate-relax --nonet \
	%{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%doc README.md
%license LICENSE.txt
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 1:2.2.1-2
- Build from sources

* Mon Feb 17 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 1:2.2.1-1
- New release smc-raghumalayalamsans-fonts-2.2.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1:2.1.2-4
- Font CI test added

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1:2.1.2-2
- Updated License in metainfo and spec cleanup

* Wed Nov 28 2018 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1:2.1.2-1
- first release of smc-raghumalayalamsans fonts
