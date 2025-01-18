%global fontname fira-code
%global fontconf 60-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        6.2
Release:        10%{?dist}
Summary:        Monospaced font with programming ligatures

License:        OFL-1.1
URL:            https://github.com/tonsky/FiraCode
Source0:        https://github.com/tonsky/FiraCode/releases/download/%{version}/Fira_Code_v%{version}.zip#/%{name}-%{version}.zip
Source1:        %{name}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib

Requires:       fontpackages-filesystem

%description
Fira Code is an extension of the Fira Mono font containing a set of ligatures
for common programming multi-character combinations. This is just a font
rendering feature: underlying code remains ASCII-compatible. This helps to
read and understand code faster. For some frequent sequences like .. or //,
ligatures allow us to correct spacing.


%prep
%autosetup -c


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p ttf/*.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}

ln -s %{_fontconfig_templatedir}/%{fontconf} \
        %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata file
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%check
appstream-util validate-relax --nonet \
        %{buildroot}%{_datadir}/metainfo/%{fontname}.metainfo.xml

%_font_pkg -f %{fontconf} *.ttf
%{_datadir}/metainfo/%{fontname}.metainfo.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 20 2023 Matej Focko <mfocko@redhat.com> - 6.2-6
- migrated to SPDX license

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 07 2021 Michael Kuhn <suraia@fedoraproject.org> - 6.2-1
- Update to 6.2

* Fri Dec 03 2021 Michael Kuhn <suraia@fedoraproject.org> - 6.1-1
- Update to 6.1

* Mon Nov 29 2021 Michael Kuhn <suraia@fedoraproject.org> - 6-1
- Update to 6

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 12 2020 Michael Kuhn <suraia@fedoraproject.org> - 5.2-1
- Update to 5.2

* Thu Jun 11 2020 Michael Kuhn <suraia@fedoraproject.org> - 5.1-1
- Update to 5.1

* Mon Jun 08 2020 Michael Kuhn <suraia@fedoraproject.org> - 5-1
- Update to 5
- Switch to TTF, see https://github.com/tonsky/FiraCode/issues/939

* Mon May 18 2020 Michael Kuhn <suraia@fedoraproject.org> - 4-1
- Update to 4

* Wed Apr 15 2020 Michael Kuhn <suraia@fedoraproject.org> - 3.1-1
- Update to 3.1

* Fri Apr 10 2020 Michael Kuhn <suraia@fedoraproject.org> - 3-1
- Update to 3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Dec 05 2019 Michael Kuhn <suraia@fedoraproject.org> - 2-1
- Initial package
