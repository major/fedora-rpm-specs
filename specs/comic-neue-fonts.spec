%global fontname comic-neue
%global fontconf 63-%{fontname}

%global common_desc \
Comic Neue is a font created by Craig Rozynski that takes inspiration\
from Comic Sans. It is perfect as a display face, for marking up comments,\
and writing passive aggressive office memos.


Name:           %{fontname}-fonts
Version:        2.51
Release:        12%{?dist}
Summary:        A typeface family inspired by Comic Sans

# Automatically converted from old format: OFL - review is highly recommended.
License:        LicenseRef-Callaway-OFL
URL:            http://comicneue.com/
Source0:        http://comicneue.com/%{fontname}-%{version}.zip
Source1:        %{fontname}-fontconfig.conf
Source2:        %{fontname}-angular-fontconfig.conf

BuildArch:      noarch
BuildRequires:  fontpackages-devel

Requires:       %{name}-common = %{version}-%{release}


%description
%common_desc


%package common
Summary:        Common files of %{name}
Requires:       fontpackages-filesystem

%description common
%common_desc

This package consists of files used by other %{name} packages.


%package -n %{fontname}-angular-fonts
Summary:        A typeface family inspired by Comic Sans, angular variant
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-angular-fonts
%common_desc

The Comic Neue Angular variant features angular terminals rather than round.


%package -n %{fontname}-web-fonts
Summary:        A typeface family inspired by Comic Sans, web files
Requires:       %{name}-common = %{version}-%{release}

%description -n %{fontname}-web-fonts
%common_desc

This package contains Web Open Font Format versions 1 and 2 files.


%prep
%setup -q -c


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p %{fontname}-%{version}/OTF/*/*.otf %{buildroot}%{_fontdir}
install -m 0644 -p %{fontname}-%{version}/WebFonts/*.woff %{buildroot}%{_fontdir}
install -m 0644 -p %{fontname}-%{version}/WebFonts/*.woff2 %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-angular.conf

for fconf in %{fontconf}.conf \
             %{fontconf}-angular.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
        %{buildroot}%{_fontconfig_confdir}/$fconf
done

%_font_pkg -f %{fontconf}.conf ComicNeue-*.otf
%_font_pkg -n angular -f %{fontconf}-angular.conf ComicNeueAngular-*.otf
%_font_pkg -n web ComicNeue*.woff ComicNeue*.woff2


%files common
%defattr(0644,root,root,-)
%doc %{fontname}-%{version}/Booklet-ComicNeue.pdf %{fontname}-%{version}/FONTLOG.txt
%license %{fontname}-%{version}/OFL.txt %{fontname}-%{version}/OFL-FAQ.txt


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.51-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Karel Volný <kvolny@redhat.com> 2.51-1
- new version 2.51 (#1883149)
- updated to improve web font files/added web subpackage in Fedora

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 16 2020 Karel Volný <kvolny@redhat.com> 2.5-1
- new version 2.5 (#1823698)
- updated to be compatible with the Google Fonts Library

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Karel Volný <kvolny@redhat.com> 2.3-1
- new version 2.3 (#1376999)
- added support for Esperanto, low quotation marks, improved CSS

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 02 2015 Karel Volný <kvolny@redhat.com> 2.2-2
- fixes as per review RHBZ#1271787#c3
- removed %%clean
- removed %%defattr
- moved %%_font_pkg to %%install section

* Wed Oct 14 2015 Karel Volný <kvolny@redhat.com> 2.2-1
- Initial release
