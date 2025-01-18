%global fontname d-din
%global fontconf 64-%{fontname}
%global asfontname com.datto.%{fontname}

%global desc \
D-DIN is a sans-serif typeface family derived from German DIN \
(Deutsches Institut fuer Normung / German Institute for Standardization) \
font style. \
 \
This font was commissioned by Datto, Inc. from Monotype and is used for \
the company's primary corporate typography.

Name:           %{fontname}-fonts
Version:        1.0
Release:        18%{?dist}
Summary:        Datto D-DIN fonts
# Only the metainfo files are CC-BY-SA
# Automatically converted from old format: OFL and CC-BY-SA - review is highly recommended.
License:        LicenseRef-Callaway-OFL AND LicenseRef-Callaway-CC-BY-SA
URL:            https://www.datto.com/fonts/d-din

Source0:        %{url}/D-DIN_complete-v%{version}.zip
Source1:        %{fontconf}-fontconfig.conf
Source2:        %{fontconf}-condensed-fontconfig.conf
Source3:        %{fontconf}-exp-fontconfig.conf

BuildArch:      noarch
BuildRequires:  %{_bindir}/appstream-util
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

# Eliminate nonsense Provides from fc-query (rhbz#1509790)
%global __provides_exclude ^0$

%description %{desc}


%package -n %{fontname}-condensed-fonts
Summary:        Datto D-DIN condensed fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-condensed-fonts %{desc}

This package provides the condensed fonts variant.

%package -n %{fontname}-exp-fonts
Summary:        Datto D-DIN expanded fonts
Requires:       fontpackages-filesystem

%description -n %{fontname}-exp-fonts %{desc}

This package provides the expanded fonts variant.

%prep
%autosetup -c


%build
# Nothing to build

%install

# Install fonts
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.otf %{buildroot}%{_fontdir}

# Install fontconfig data
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf

install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-condensed.conf

install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-exp.conf

for fconf in %{fontconf}.conf %{fontconf}-condensed.conf %{fontconf}-exp.conf; do
  ln -s %{_fontconfig_templatedir}/$fconf %{buildroot}%{_fontconfig_confdir}/$fconf
done

# Install AppStream metadata
install -m 0755 -d %{buildroot}%{_datadir}/metainfo
install -m 0644 -p *.metainfo.xml %{buildroot}%{_datadir}/metainfo

%check
# Validate AppStream metadata
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml


%_font_pkg -f %{fontconf}.conf D-DIN.otf D-DIN-*.otf
%license OFL-1.1.txt CC-BY-SA-4.0.txt
%doc README FONTLOG.txt
%{_datadir}/metainfo/%{asfontname}.metainfo.xml

%_font_pkg -n condensed -f %{fontconf}-condensed.conf D-DINCondensed*.otf
%license OFL-1.1.txt CC-BY-SA-4.0.txt
%doc README FONTLOG.txt
%{_datadir}/metainfo/%{asfontname}-condensed.metainfo.xml

%_font_pkg -n exp -f %{fontconf}-exp.conf D-DINExp*.otf
%license OFL-1.1.txt CC-BY-SA-4.0.txt
%doc README FONTLOG.txt
%{_datadir}/metainfo/%{asfontname}-exp.metainfo.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0-17
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov  7 2017 Neal Gompa <ngompa@datto.com> - 1.0-1
- Initial import into Fedora (RH#1509777)

* Sun Nov  5 2017 Neal Gompa <ngompa@datto.com> - 1.0-0.2
- Add fontpackages-filesystem Requires to all subpackages
- Update the summary and description to indicate exp means expanded

* Sun Nov  5 2017 Neal Gompa <ngompa@datto.com> - 1.0-0.1
- Initial packaging
