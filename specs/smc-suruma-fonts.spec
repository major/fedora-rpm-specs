%global fontname smc-suruma
%global fontconf 67-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	3.2.4
Release:	11%{?dist}
Epoch:		1
Summary:	Open Type Fonts for Malayalam script 
# Automatically converted from old format: GPLv3+ with exceptions - review is highly recommended.
License:	LicenseRef-Callaway-GPLv3+-with-exceptions
URL:		https://gitlab.com/smc/fonts/suruma
Source0:	%{url}/-/archive/Version%{version}/suruma-Version%{version}.tar.gz
Source1:	%{fontname}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml
BuildArch:	noarch
BuildRequires: make
BuildRequires:	fontpackages-devel
BuildRequires:	libappstream-glib
BuildRequires:	fontforge
Requires:	fontpackages-filesystem
Obsoletes:	smc-fonts-common < 6.1-11

%description
Suruma-3.2.1 is a rehash of earlier releases. 
The earlier idea of akhand conjuncts for *RA *LA forms is revisited and 
implemented again with the new opentype specs. The new specs do away 
with statically-assigned character properties (by the shaping engine) 
for consonants. Instead, they are font dependent. i.e., post-base forms,
below-base forms etc. are all decided by the the font itself. 
This concept was also used in the initial version of suruma font.

%prep
%autosetup -n suruma-Version%{version}

%build
make

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
%license COPYING
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1:3.2.4-10
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 1:3.2.4-1
- New release smc-suruma-fonts-3.2.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 17 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 1:3.2.3-1
- New release smc-suruma-fonts-3.2.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 24 2019 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1:3.2.2-2
- Font CI test added

* Mon Feb 25 2019 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1:3.2.2-1
- Build font from sources

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 31 2018 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1:3.2.1-2
- Update incorrect license and removed unwanted requires entry

* Wed Nov 28 2018 Vishal Vijayraghavan <vishalvijayraghavan@gmail.com> - 1:3.2.1-1
- first release of smc-suruma fonts
