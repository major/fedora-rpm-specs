%global fontname typetype-molot
%global fontconf 61-%{fontname}.conf

Name:		%{fontname}-fonts
Version:	1.000
Release:	22%{?dist}
Summary:	A display sans-serif font 

# Automatically converted from old format: OFL - review is highly recommended.
License:	LicenseRef-Callaway-OFL
URL:		http://typetype.ru/
Source0:	http://www.typetype.ru/files/fonts/molot.zip
Source1:	%{name}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
%if 0%{?fedora} >= 21
BuildRequires:	libappstream-glib
%endif
Requires:	fontpackages-filesystem

%description
A display sans-serif font created by Roman Ershov and Jovanny Lemonad

%prep
%autosetup -c


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
		%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
		%{buildroot}%{_fontconfig_confdir}/%{fontconf}

%if 0%{?fedora} >= 21
install -Dm 0644 -p %{SOURCE2} \
		%{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{fontname}.metainfo.xml
%endif

%_font_pkg -f %{fontconf} *.otf

%license "FREE FONT LICENSE.txt"
%if 0%{?fedora} >= 21
%{_datadir}/appdata/%{fontname}.metainfo.xml
%endif

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.000-21
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 21 2016 Luya Tshimbalanga <luya@fedoraproject.org> 1.000-4
- Used upstream url for downloading file

* Sat Aug 20 2016 Luya Tshimbalanga <luya_tfz@thefinalzone.net> 1.000-3
- Removed legacy install line
- Include SIL OFL license

* Fri Aug 19 2016 Luya Tshimbalanga <luya_tfz@thefinalzone.net> 1.000-1
- Initial build
