%global fontname foundation-icons
%global fontconf 60-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        3.0
Release:        15%{?dist}
Summary:        Foundation Icons font

License:        MIT
URL:            https://zurb.com/playground/foundation-icon-fonts-3
Source0:        https://zurb.com/playground/uploads/upload/upload/288/foundation-icons.zip
Source1:        %{name}-fontconfig.conf

Patch1:         foundation-icons-fonts-3.0-fix_css.patch

BuildArch:      noarch
BuildRequires:  fontpackages-devel

Requires:       fontpackages-filesystem


%description
A custom collection of 283 icons that are stored in a handy font.

This package contains the TrueType font file which is typically used locally.


%package web
Requires:       %{fontname}-fonts = %{version}-%{release}
Summary:        Foundation Icons font css file

%description web
A custom collection of 283 icons that are stored in a handy font.

This package contains the CSS file for use on a webserver.


%prep
%autosetup -n foundation-icons


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

mkdir -p %{buildroot}%{_datadir}/foundation-icons-web/
cp -a foundation-icons.css %{buildroot}%{_datadir}/foundation-icons-web/


%_font_pkg -f %{fontconf} *.ttf

%files web
%{_datadir}/foundation-icons-web/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Xavier Bachelot <xavier@bachelot.org> - 3.0-2
- Package TTF font only and add patch to fix CSS accordingly.
- Update descriptions and summaries.
- Drop commented out appstream support.

* Tue Jun 04 2019 Xavier Bachelot <xavier@bachelot.org> - 3.0-1
- Initial package.
