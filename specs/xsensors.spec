Name:           xsensors
Version:        0.80
Release:        22%{?dist}
Summary:        An X11 interface to lm_sensors

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Url:            https://github.com/Mystro256/xsensors
Source:         https://github.com/Mystro256/%{name}/archive/%{version}.tar.gz

%if 0%{?rhel} >= 7 || 0%{?fedora}
BuildRequires:  gcc
BuildRequires:  gtk3-devel
BuildRequires:  libappstream-glib
%else
BuildRequires:  gtk2-devel
%endif
BuildRequires:  lm_sensors-devel
BuildRequires:  cairo-devel
BuildRequires:  glib2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  make

# 32bit package serves very little purpose:
ExcludeArch: %{ix86}

%description
Xsensors is a simple GUI program that allows you to read useful data from the
lm_sensors library in a digital read-out like fashion, such as the temperature,
voltage ratings and fan speeds of the running computer.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
%if 0%{?rhel} >= 7 || 0%{?fedora}
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml
%endif

%files
%doc AUTHORS COPYING README ChangeLog
%{_datadir}/%{name}/theme.tiff
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1*
%if 0%{?rhel} >= 7 || 0%{?fedora}
%{_datadir}/appdata/%{name}.appdata.xml
%else
%exclude %{_datadir}/appdata/%{name}.appdata.xml
%endif

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.80-21
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 16 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.80-2
- Added missing scriplet to update iconcache

* Tue Nov 15 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.80-1
- Update to 0.80

* Sun Sep 25 2016 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.75-1
- Update to 0.75

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.73-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.73-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.73-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 3 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.73-1
- New version, fixes bug RH#1076012

* Fri Jan 3 2014 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.72-1
- New version, minor fixes
- Removed unnecessary configure flag
- Removed unnecessary post actions
- Fixed website

* Sat Apr 9 2011 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.71-2
- Added missing build flags

* Sat Apr 9 2011 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.71-1
- Switched to new upstream source

* Sat Feb 19 2011 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.70-2
- Removed build flags
- Added missing dependancy

* Sat Feb 19 2011 Jeremy Newton <alexjnewt AT hotmail DOT com> - 0.70-1
- Initial package SPEC created
