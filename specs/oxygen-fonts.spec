%global fontname oxygen
%global fontconf 61-%{fontname}

Name:           %{fontname}-fonts
Version:        5.4.3
Release:        26%{?dist}
Summary:        Oxygen fonts created by the KDE Community

# See LICENSE-GPL+FE for details about the exception
# Automatically converted from old format: OFL or GPLv3 with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-OFL OR LicenseRef-Callaway-GPLv3-with-exceptions
URL:            http://www.kde.org
Source0:        http://download.kde.org/stable/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        %{fontconf}-sans.conf
Source2:        %{fontconf}-mono.conf

# essentially a noarch pkg here, no real -debuginfo needed (#1192729)
%define debug_package   %{nil}

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel
BuildRequires:  fontforge
BuildRequires:  fontpackages-devel
Requires:       fontpackages-filesystem

# main (meta)package, largely for upgrade path
Requires: %{fontname}-mono-fonts = %{version}-%{release}
Requires: %{fontname}-sans-fonts = %{version}-%{release}

%description
Oxygen fonts created by the KDE Community.

%package common
Summary:        Common files for Oxygen font
Requires:       fontpackages-filesystem
BuildArch:      noarch
%description    common
%{summary}.

%package -n %{fontname}-mono-fonts
Summary:        Oxygen Monospaced Font
Requires:       %{name}-common = %{version}-%{release}
BuildArch:      noarch
%description    -n %{fontname}-mono-fonts
%{summary}.

%package -n %{fontname}-sans-fonts
Summary:        Oxygen Sans-Serif Font
Requires:       %{name}-common = %{version}-%{release}
BuildArch:      noarch
%description    -n %{fontname}-sans-fonts
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}

%build
%{cmake_kf5} %{?fontforge} -DOXYGEN_FONT_INSTALL_DIR=%{_fontdir}
%cmake_build


%install
%cmake_install

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-sans.conf
install -m 0644 -p %{SOURCE2} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}-mono.conf

ln -s %{_fontconfig_templatedir}/%{fontconf}-sans.conf \
      %{buildroot}/%{_fontconfig_confdir}/%{fontconf}-sans.conf
ln -s %{_fontconfig_templatedir}/%{fontconf}-mono.conf \
      %{buildroot}/%{_fontconfig_confdir}/%{fontconf}-mono.conf

%_font_pkg -n sans -f %{fontconf}-sans.conf Oxygen-Sans*.ttf
%_font_pkg -n mono -f %{fontconf}-mono.conf OxygenMono*.ttf

%files
# empty metapackage

%files common
%doc COPYING-GPL+FE.txt COPYING-OFL GPL.txt README.md

%files devel
%{_libdir}/cmake/OxygenFont/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 5.4.3-25
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 2020 Parag Nemade <pnemade AT redhat DOT com> - 5.4.3-15
- Update for new cmake macros (out of source builds)
- Update to use new DTD id in fontconfig files

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.4.3-8
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.4.3-3
- %%build: use %%cmake_kf5

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 05 2015 Daniel Vrátil <dvratil@fedoraproject.org> - 5.4.3-1
- Plasma 5.4.3

* Thu Oct 01 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.4.2-1
- 5.4.2

* Wed Sep 09 2015 Rex Dieter <rdieter@fedoraproject.org> - 5.4.1-1
- 5.4.1

* Fri Aug 21 2015 Daniel Vrátil <dvratil@redhat.com> - 5.4.0-1
- Plasma 5.4.0

* Thu Aug 13 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.95-1
- Plasma 5.3.95

* Thu Jun 25 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.2-1
- Plasma 5.3.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.1-1
- Plasma 5.3.1

* Mon Apr 27 2015 Daniel Vrátil <dvratil@redhat.com> - 5.3.0-1
- Plasma 5.3.0

* Fri Mar 20 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.2-1
- Plasma 5.2.2

* Mon Mar 09 2015 Rex Dieter <rdieter@fedoraproject.org> 5.2.1-1
- 5.2.1

* Sat Feb 14 2015 Rex Dieter <rdieter@fedoraproject.org> 5.2.0-3
- oxygen-fonts-debuginfo-5.2.0-2 is empty (#1192729)

* Fri Feb 13 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-2
- Fix noarch bug: -devel installs into %%{_libdir}, which is arch-dependent

* Thu Jan 29 2015 Daniel Vrátil <dvratil@redhat.com> - 5.2.0-1
- oxygen-font 5.2.0, remove the fontforge rawhide workaround

* Mon Oct 20 2014 Rex Dieter <rdieter@fedoraproject.org> 5.1.0-2
- provide oxygen-fonts (meta)package, fixes upgrade path (#1154369)

* Thu Oct 09 2014 Daniel Vrátil <dvratil@redhat.com> - 5.1.0-1
- oxygen-font 5.1.0

* Tue Sep 30 2014 Daniel Vrátil <dvratil@redhat.com> - 0.4.2-5
- Fix incorrect use of macros in Requires

* Mon Sep 29 2014 Parag Nemade <pnemade@redhat.com> - 0.4.2-4
- Use correct typefaces

* Thu Sep 25 2014 Daniel Vrátil <dvratil@redhat.com> - 0.4.2-3
- Fix fontconfig.files (RHBZ#1146505)
- Create subpackages for sans and mono fonts

* Tue Sep 16 2014 Daniel Vrátil <dvratil@redhat.com> - 0.4.2-2
- oxygen-fonts 0.4.2

* Wed Aug 20 2014 Daniel Vrátil <dvratil@redhat.com> - 0.4.0-2
- drop dependency on KF5

* Wed Jul 16 2014 Daniel Vrátil <dvratil@redhat.com> - 0.4.0-1
- oxygen-fonts 0.4.0

* Sun Jun 29 2014 Daniel Vrátil <dvratil@redhat.com> - 0.3.95-2
- fix license
- fix rpmlint warnings

* Thu Apr 03 2014 Daniel Vrátil <dvratil@redhat.com> - 0.3.95-1
- Initial vrsion
