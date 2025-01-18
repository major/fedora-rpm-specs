%global fontname source-serif
%global fontconf 63-%{fontname}.conf

Name:           adobe-source-serif-pro-fonts
Version:        4.005
Release:        7%{?dist}
Summary:        Typeface for setting text in many sizes, weights, and languages

# Automatically converted from old format: OFL - review is highly recommended.
License:        LicenseRef-Callaway-OFL
URL:            https://github.com/adobe-fonts/source-serif
Source0:        https://github.com/adobe-fonts/source-serif/archive/%{version}R.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{fontname}.fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib
Requires:       fontpackages-filesystem

%description
Source Serif is an open-source typeface to complement the Source Sans family.

%prep
%setup -q -n source-serif-%{version}R
sed -i 's/\r//' LICENSE.md

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p OTF/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
        %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%check
appstream-util --nonet validate-relax \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.otf
%{_datadir}/appdata/%{fontname}.metainfo.xml

%doc README.md
%license LICENSE.md

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.005-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 4.005-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.005-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.005-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Michael Kuhn <suraia@fedoraproject.org> - 4.005-1
- Update to 4.005

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.004-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.004-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jan 29 2021 Michael Kuhn <suraia@fedoraproject.org> - 4.004-1
- Update to 4.004

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 12 2019 Michael Kuhn <suraia@fedoraproject.org> - 3.001-1
- Update to 3.001

* Sat Jul 27 2019 Michael Kuhn <suraia@fedoraproject.org> - 3.000-1
- Update to 3.000

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.010.1.010-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Michael Kuhn <suraia@fedoraproject.org> - 2.010.1.010-1
- Update to 2.010 and 1.010

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.007.1.007-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Sep 30 2018 Michael Kuhn <suraia@fedoraproject.org> - 2.007.1.007-1
- Update to 2.007 and 1.007

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Michael Kuhn <suraia@fedoraproject.org> - 2.000-1
- Update to 2.000

* Tue Aug 30 2016 Michael Kuhn <suraia@fedoraproject.org> - 1.017-2
- Fix AppStream metadata
- Validate AppStream metadata during check

* Tue Jan 26 2016 Michael Kuhn <suraia@fedoraproject.org> - 1.017-1
- Initial package.
