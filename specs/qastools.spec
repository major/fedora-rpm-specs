Name:           qastools
Version:        0.23.0
Release:        11%{?dist}
Summary:        Collection of desktop applications for ALSA
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only

URL:            https://gitlab.com/sebholt/qastools
Source0:        https://gitlab.com/sebholt/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  cmake gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  qt5-qtbase-devel qt5-qtsvg-devel qt5-linguist
BuildRequires:  pkgconfig(alsa)
# For libudev.h
BuildRequires:  systemd-devel

Requires:       qasconfig%{?_isa} = %{version}-%{release}
Requires:       qashctl%{?_isa} = %{version}-%{release}
Requires:       qasmixer%{?_isa} = %{version}-%{release}


%description
QasTools is a collection of desktop applications for the ALSA sound system.


%package -n qascommon
Summary:        Common part of QasTools

%description -n qascommon
Common part of QasTools.


%package -n qasconfig
Summary:	    ALSA configuration browser
Requires:	    qascommon%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description -n qasconfig
Browser for the ALSA configuration tree.


%package -n qashctl
Summary: 	    ALSA complex mixer
Requires:	    qascommon%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description -n qashctl
Mixer for ALSA's more complex "High level Control Interface".


%package -n qasmixer
Summary:        ALSA simple mixer
Requires:       qascommon%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme

%description -n qasmixer
Desktop mixer for ALSA's "Simple Mixer Interface" (alsamixer).


%prep
%autosetup -n %{name}-v%{version}


%build
%cmake -DSKIP_LICENSE_INSTALL:BOOL=ON
%cmake_build


%install
%cmake_install
for file in %{buildroot}/%{_datadir}/applications/*.desktop; do
    desktop-file-validate $file
done
%find_lang %{name} --with-qt --without-mo
# hack
#rm -f %{buildroot}/%{_datadir}/%{name}/l10n/qastools_default.qm


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml


%files
# meta package

%files -n qascommon -f %{name}.lang
%license COPYING
%doc CHANGELOG README.md TODO
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/widgets/

%files -n qasconfig
%{_bindir}/qasconfig
%{_datadir}/applications/qasconfig.desktop
%{_datadir}/icons/hicolor/*/apps/qasconfig.*
%{_mandir}/man1/qasconfig.1.*
%{_metainfodir}/qasconfig.appdata.xml

%files -n qashctl
%{_bindir}/qashctl
%{_datadir}/applications/qashctl.desktop
%{_datadir}/icons/hicolor/*/apps/qashctl.*
%{_mandir}/man1/qashctl.1.*
%{_metainfodir}/qashctl.appdata.xml

%files -n qasmixer
%{_bindir}/qasmixer
%{_datadir}/%{name}/icons/
%{_datadir}/applications/qasmixer.desktop
%{_datadir}/icons/hicolor/*/apps/qasmixer.*
%{_mandir}/man1/qasmixer.1.*
%{_metainfodir}/qasmixer.appdata.xml


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 0.23.0-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 Richard Shaw <hobbes1069@gmail.com> - 0.23.0-1
- Update to 0.23.0.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.21.0-4
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 25 2016 Richard Shaw <hobbes1069@gmail.com> - 0.21.0-1
- Update to latest upstream release.

* Tue Apr 26 2016 Richard Shaw <hobbes1069@gmail.com> - 0.20.0-1
- Update to latest upstream release.

* Sun Feb  7 2016 Richard Shaw <hobbes1069@gmail.com> - 0.18.1-1
- Update to latest upstream release.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.17.2-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Oct 26 2013 TI_Eugene <ti.eugene@gmail.com> - 0.17.2-1
- Vesion bump
- Splitting into separate subpackages
- Spec cleanups

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 18 2012 Richard Shaw <hobbes1069@gmail.com> - 0.17.1-3
- Fix FTBFS for rawhide/GCC 4.7.

* Tue Apr 17 2012 Richard Shaw <hobbes1069@gmail.com> - 0.17.1-2
- Inital release.
- Updated spec file per reviewer comments.
