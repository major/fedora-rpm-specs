%global fontname aftertheflood-sparks
%global fontconf 66-%{fontname}
%global desc After the Flood Sparks is a font that allows for the combination of text and \
visual data to show an idea and evidence in one headline. This builds on the \
principle of Sparklines defined by Edward Tufte and makes them easier to use. \
Sparklines are currently available as plugins or javascript elements. By  \
installing the Sparks font you can use them immediately without the need for \
custom code. \
\
Sparks data needs to be formatted as comma-separated values, with curly brackets \
at both ends of the set, e.g., {30,60,90}. You can also have numbers at the \
beginning and end of the set, which are useful for providing the start and \
end points, e.g., 123{30,60,90}456 – Sparks has numerals built in.


Name:       %{fontname}-fonts
Version:    2.0
Release:    17%{?dist}
Summary:    After the Flood Sparks, a font to display charts within text
# Automatically converted from old format: OFL - review is highly recommended.
License:    LicenseRef-Callaway-OFL
URL:        https://aftertheflood.co/projects/sparks/
Source0:    https://github.com/aftertheflood/sparks/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:    66-%{fontname}-bar.conf
Source2:    66-%{fontname}-dot.conf
Source3:    66-%{fontname}-dot-line.conf
Source4:    %{fontname}.metainfo.xml
Source5:    %{fontname}-bar.metainfo.xml
Source6:    %{fontname}-dot.metainfo.xml
Source7:    %{fontname}-dot-line.metainfo.xml

BuildArch:      noarch

BuildRequires:  fontpackages-devel
BuildRequires:  libappstream-glib

Requires:       fontpackages-filesystem


%description
%{desc}


%package common
Summary: Common files for After the Flood Sparks

%description common
%{desc}

Common files for After the Flood Sparks.


%package -n %{fontname}-bar-fonts
Summary: After the Flood Sparks Bar fonts
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-bar-fonts
%{desc}

This package provides the Bar family.


%package -n %{fontname}-dot-fonts
Summary: After the Flood Sparks Dot fonts
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-dot-fonts
%{desc}

This package provides the Dot family.


%package -n %{fontname}-dot-line-fonts
Summary: After the Flood Sparks Dot-line fonts
Requires: %{name}-common = %{version}-%{release}

%description -n %{fontname}-dot-line-fonts
%{desc}

This package provides the Dot-line family.


%prep
%autosetup -n sparks-%{version}


%build
# Nothing to do


%install
# install fonts
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 output/otf/*.otf %{buildroot}%{_fontdir}

# install fontconfig files
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-bar.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-dot.conf
install -m 0644 -p %{SOURCE3} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-dot-line.conf

for fconf in %{fontconf}-bar.conf %{fontconf}-dot.conf %{fontconf}-dot-line.conf; do
    ln -s %{_fontconfig_templatedir}/$fconf \
          %{buildroot}%{_fontconfig_confdir}/$fconf
done

# install appdata
install -m 0755 -d %{buildroot}%{_datadir}/metainfo
install -m 0644 -p %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} \
        %{buildroot}%{_datadir}/metainfo

appstream-util validate-relax --nonet \
               %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

               
%files common
%license OFL.txt
%doc AUTHORS.txt CONTRIBUTORS.txt FONTLOG.txt README.md 
%{_datadir}/metainfo/%{fontname}.metainfo.xml


%_font_pkg -n bar -f %{fontconf}-bar.conf Sparks-Bar-*.otf
%{_datadir}/metainfo/%{fontname}-bar.metainfo.xml


%_font_pkg -n dot -f %{fontconf}-dot.conf Sparks-Dot-*.otf
%{_datadir}/metainfo/%{fontname}-dot.metainfo.xml


%_font_pkg -n dot-line -f %{fontconf}-dot-line.conf Sparks-Dotline-*.otf
%{_datadir}/metainfo/%{fontname}-dot-line.metainfo.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0-16
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 2.0-1
- initial RPM release
