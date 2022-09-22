%global fontname redhat
%global fontconf 64-%{fontname}
%global asfontname com.redhat.%{fontname}

%global projname RedHatFont

%global desc \
Red Hat Typeface is a fresh take on the geometric sans genre, \
taking inspiration from a range of American sans serifs \
including Tempo and Highway Gothic. \
 \
The Display styles, made for headlines and big statements, \
are low contrast and spaced tightly, with a large x-height and open counters. \
 \
The Text styles have a slightly smaller x-height and narrower width \
for better legibility, are spaced more generously, and have thinned joins \
for better performance at small sizes. \
 \
The Mono styles are similar to the Text styles, but are adapted \
for better performance to render code and similar text. \
 \
The three families can be used together seamlessly at a range of sizes. \
 \
The fonts were originally commissioned by Paula Scher / Pentagram \
and designed by Jeremy Mickel / MCKL for the new Red Hat identity.

Name:           %{fontname}-fonts
Version:        4.0.3
Release:        1%{?dist}
Summary:        Red Hat Typeface fonts
# Only the metainfo files are CC-BY-SA
License:        OFL and CC-BY-SA
URL:            https://github.com/RedHatOfficial/%{projname}

Source0:        %{url}/archive/%{version}/%{projname}-%{version}.tar.gz
Source1:        %{fontconf}-display-fontconfig.conf
Source2:        %{fontconf}-text-fontconfig.conf
Source3:        %{fontconf}-mono-fontconfig.conf

BuildArch:      noarch
BuildRequires:  %{_bindir}/appstream-util
BuildRequires:  fontpackages-devel

%description %{desc}


%package -n %{fontname}-display-fonts
Summary:        Red Hat Display fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-display-fonts %{desc}

This package provides the Display fonts variant.

%package -n %{fontname}-text-fonts
Summary:        Red Hat Text fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-text-fonts %{desc}

This package provides the Text fonts variant.

%package -n %{fontname}-mono-fonts
Summary:        Red Hat Mono fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-mono-fonts %{desc}

This package provides the Monospace fonts variant.

%prep
%autosetup -n %{projname}-%{version} -p1


%build
# Nothing to build

%install

# Install fonts
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p fonts/*/static/otf/*.otf %{buildroot}%{_fontdir}
install -m 0644 -p fonts/*/static/ttf/*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p fonts/*/*.ttf %{buildroot}%{_fontdir}

# Install fontconfig data
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-display.conf

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-text.conf

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mono.conf

for fconf in %{fontconf}-display.conf %{fontconf}-text.conf %{fontconf}-mono.conf; do
  ln -s %{_fontconfig_templatedir}/$fconf %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Install AppStream metadata
install -m 0755 -d %{buildroot}%{_datadir}/metainfo
install -m 0644 -p metainfo/*.metainfo.xml %{buildroot}%{_datadir}/metainfo

%check
# Validate AppStream metadata
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml


%_font_pkg -n display -f %{fontconf}-display.conf RedHatDisplay*.?tf
%license LICENSE metainfo/LICENSE-METAINFO
%doc README.md CHANGELOG.md *.png
%{_datadir}/metainfo/%{asfontname}-display.metainfo.xml

%_font_pkg -n text -f %{fontconf}-text.conf RedHatText*.?tf
%license LICENSE metainfo/LICENSE-METAINFO
%doc README.md CHANGELOG.md *.png
%{_datadir}/metainfo/%{asfontname}-text.metainfo.xml

%_font_pkg -n mono -f %{fontconf}-mono.conf RedHatMono*.?tf
%license LICENSE metainfo/LICENSE-METAINFO
%doc README.md CHANGELOG.md *.png
%{_datadir}/metainfo/%{asfontname}-mono.metainfo.xml


%changelog
* Wed Aug 03 2022 Neal Gompa <ngompa@fedoraproject.org> - 4.0.3-1
- Update to 4.0.3 (RH#1955487)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 23 2021 Neal Gompa <ngompa13@gmail.com> - 4.0.1-1
- Rebase to 4.0.1 (RH#1917996)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jul 29 2019 Neal Gompa <ngompa13@gmail.com> - 2.3.2-1
- Update to 2.3.2
- Fix typos in the changelog

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Ben Cotton <bcotton@fedoraproject.org> - 2.2.0-2
- Add TrueType font files (RHBZ #1709922)

* Sun May  5 2019 Neal Gompa <ngompa13@gmail.com> - 2.2.0-1
- Initial packaging
