
%global fontname naver-nanum-gothic-coding
%global fontconf 65-3-%{fontname}.conf

%global archivename NanumGothicCoding-2.0.zip

Name:		%{fontname}-fonts
Version:	2.000
Release:	20%{?dist}
Summary:	Nanum Gothic Coding family of Korean TrueType fonts

License:	OFL
URL:		http://dev.naver.com/projects/nanumfont/
# NanumGothic_Coding has a mirror redirector for its downloads
# You can get this zip archive by following a link from:
# http://dev.naver.com/projects/nanumfont/download/note/214
Source0:	%{archivename}
Source1:	%{name}-fontconfig.conf
Source2:	%{fontname}.metainfo.xml

BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	/usr/bin/appstream-util
Requires:	fontpackages-filesystem

# NHN has been renamed their company name to Naver at 2014
Provides:   nhn-nanum-gothic-coding-fonts = %{version}-%{release}
Obsoletes:  nhn-nanum-gothic-coding-fonts <= 2.0.0-8


%description
Nanum Gothic Coding fonts are set of Gothic Korean font faces suitable
for source code editing, designed by Sandoll Communication and
published by NAVER Corporation.

%prep
%setup -q -c
for i in *.ttf; do
  case $i in
    *-Bold.ttf)
      mv $i NanumGothic_Coding_Bold.ttf
      ;;
    *)
      mv $i NanumGothic_Coding.ttf
  esac
done


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		   %{buildroot}%{_fontconfig_confdir}

# Add appstream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%check
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml


%_font_pkg -f %{fontconf} *.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec  8 2017 Peng Wu <pwu@redhat.com> - 2.000-9
- Renamed from nhn-nanum-gothic-coding-fonts
