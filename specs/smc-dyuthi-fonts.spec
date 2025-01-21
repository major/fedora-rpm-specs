%global fontname smc-dyuthi
%global fontconf 67-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	3.0.2
Release:	12%{?dist}
Epoch:		1
Summary:	Open Type Fonts for Malayalam script
# Automatically converted from old format: OFL - review is highly recommended.
License:	LicenseRef-Callaway-OFL
URL:		https://gitlab.com/smc/fonts/dyuthi
Source0:	%{url}/-/archive/Version%{version}/dyuthi-Version%{version}.tar.gz
Source1:	%{fontname}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml
BuildArch:	noarch
BuildRequires: make
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib
BuildRequires:	brotli-devel
BuildRequires:	fontforge-devel
BuildRequires:	python3
BuildRequires:	python3-fonttools
Requires:	fontpackages-filesystem
Obsoletes:	smc-fonts-common < 6.1-11

%description
Dyuthi is an ornamental typographic design that supports Latin and Malayalam. 
The glyph patterns are based on popular 'bulged ended' type designs 
which used to be popular in Malayalam designs. The font comes in one size 
and is thicker than usual Malayalam fonts, hence is suited for titling and 
headlines. Dyuthi can accompany Meera or Rachana as title font, 
when they are used as body text.

%prep
%autosetup -n dyuthi-Version%{version}
chmod 644 *.txt
rm -rf ttf

%build
make PY=python3

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p build/*.ttf %{buildroot}%{_fontdir}

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
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1:3.0.2-11
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 1:3.0.2-1
- New release smc-dyuthi-fonts-3.0.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1:3.0.1-4
- Font CI test added

* Mon Feb 25 2019 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1:3.0.1-3
- Build font from sources

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 28 2018 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1:3.0.1-1
- first release of smc-dyuthi fonts

