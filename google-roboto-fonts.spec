%global pkgname roboto
%global srcname %{pkgname}-unhinted
%global fontname google-roboto
%global fontconf 64-%{fontname}

Name: google-roboto-fonts
Version: 2.138
Release: %autorelease
Summary: Google Roboto fonts

# Only the metainfo.xml files are CC0-1.0
License: Apache-2.0 AND CC0-1.0
URL: https://github.com/google/roboto
Source0: https://github.com/google/%{pkgname}/releases/download/v%{version}/%{srcname}.zip
Source1: %{fontconf}-condensed-fontconfig.conf
Source2: %{fontconf}-fontconfig.conf
Source3: %{fontname}-condensed.metainfo.xml
Source4: %{fontname}.metainfo.xml
BuildArch: noarch

BuildRequires: fontpackages-devel

Obsoletes: %{fontname}-common < 2.134-1

%description
Roboto is a sans-serif typeface family introduced with Android Ice Cream
Sandwich operating system. Google describes the font as "modern, yet
approachable" and "emotional".

%package -n %{fontname}-condensed-fonts
Summary: Google Roboto condensed fonts
Obsoletes: %{fontname}-common < 2.134-1

%description -n %{fontname}-condensed-fonts
Google Roboto condensed fonts.

%prep
%autosetup -c -n %{srcname}

%build

%install
# install fonts
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p Roboto*.ttf %{buildroot}%{_fontdir}

# install fontconfig files
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE2} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE1} %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-condensed.conf
for fconf in %{fontconf}.conf %{fontconf}-condensed.conf; do
  ln -s %{_fontconfig_templatedir}/$fconf %{buildroot}%{_fontconfig_confdir}/$fconf
done

# install appdata
install -m 0755 -d %{buildroot}%{_datadir}/appdata
install -m 0644 -p %{SOURCE3} %{SOURCE4} %{buildroot}%{_datadir}/appdata

%_font_pkg -f %{fontconf}.conf Roboto-*.ttf
%{_datadir}/appdata/%{fontname}.metainfo.xml
%license LICENSE

%_font_pkg -n condensed -f %{fontconf}-condensed.conf RobotoCondensed-*.ttf
%{_datadir}/appdata/%{fontname}-condensed.metainfo.xml
%license LICENSE

%changelog
%autochangelog
