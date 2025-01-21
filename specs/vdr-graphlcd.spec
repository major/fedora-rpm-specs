%global rname   vdr-plugin-graphlcd
%global sname   graphlcd
# version we want to build against
%global vdr_version 2.6.3
# Set vdr_version based on Fedora version
%if 0%{?fedora} >= 42
%global vdr_version 2.7.2
%elif 0%{?fedora} >= 40
%global vdr_version 2.6.9
%endif


Name:           vdr-graphlcd
Version:        1.0.6
Release:        20%{?dist}
Summary:        VDR plugin: Output to graphic LCD
License:        GPL-2.0-or-later
URL:            https://github.com/vdr-projects/vdr-plugin-graphlcd
Source0:        https://github.com/vdr-projects/%{rname}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
Source2:        %{name}.conf.sample
Source3:        %{name}-fonts.conf
Patch0:         0002-graphlcd-Removal-of-deprecated-interface-functions.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  vdr-devel >= %{vdr_version}
BuildRequires:  graphlcd-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}
Requires:       dejavu-sans-fonts
Requires:       bitstream-vera-sans-fonts

%description
graphlcd is a plugin for the Video Disc Recorder and shows information
about the current state of VDR on displays supported by the GraphLCD
driver library.

%prep
%autosetup -p1 -n %{rname}-%{version}

# W: file-not-utf8
iconv -f iso-8859-1 -t utf-8 HISTORY > HISTORY.utf8 ; mv HISTORY.utf8 HISTORY

%build
%make_build

%install
%make_install SKIP_INSTALL_DOC=1

# remove bundling fonts
rm -rf %{buildroot}%{vdr_resdir}/plugins/graphlcd/fonts/{DejaVuSans-Bold,DejaVuSansCondensed}.ttf
ln -s %{_datadir}/fonts/dejavu/{DejaVuSans-Bold,DejaVuSansCondensed}.ttf \
  %{buildroot}%{vdr_resdir}/plugins/graphlcd/fonts/

rm -rf %{buildroot}%{vdr_resdir}/plugins/graphlcd/fonts/{Vera,VeraBd}.ttf
ln -s %{_datadir}/fonts/bitstream-vera/{Vera,VeraBd}.ttf \
  %{buildroot}%{vdr_resdir}/plugins/graphlcd/fonts/

install -Dpm 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/%{sname}.conf

install -Dpm 644 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/sysconfig/vdr-plugins.d/%{sname}.conf.sample

install -Dpm 644 %{SOURCE3} \
    %{buildroot}%{vdr_resdir}/plugins/%{sname}/fonts.conf

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc HISTORY README
%dir %{vdr_resdir}/plugins/%{sname}
%{vdr_resdir}/plugins/%{sname}/fonts
%{vdr_resdir}/plugins/%{sname}/logos
%{vdr_resdir}/plugins/%{sname}/skins
%config(noreplace) %{vdr_resdir}/plugins/%{sname}/*.alias
%config(noreplace) %{vdr_resdir}/plugins/%{sname}/fonts.conf
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{sname}.conf
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{sname}.conf.sample

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.0.6-19
- Rebuilt for new VDR API version 2.7.2

* Mon Sep 30 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.0.6-18
- Add 0002-graphlcd-Removal-of-deprecated-interface-functions.patch for vdr-2.7.x

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.6-17
- convert license to SPDX

* Mon Jul 15 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.0.6-16
- Rebuilt for new VDR API version 2.6.9

* Thu Jul 11 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.0.6-15
- Rebuilt for new VDR API version 2.6.8

* Fri Apr 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.0.6-14
- Rebuilt for new VDR API version

* Fri Jan 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.0.6-13
- Rebuilt for new VDR API version

* Fri Jan 05 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.0.6-12
- Rebuilt for new VDR API version
- Add BR gettext for rawhide

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.0.6-9
- Rebuilt for new VDR API version

* Thu Dec 01 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.0.6-8
- Rebuilt for new VDR API version

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.0.6-6
- Rebuilt for new VDR API version

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.6-4
- Rebuilt for new VDR API version

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 28 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.6-2
- Rebuilt for new VDR API version

* Thu Mar 11 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6

* Wed Feb 17 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Mon Feb 08 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.4-1
- Update to 1.0.4
- Renamed config file (sample) included in RPM are not used and has to be renamed
  fixes (BZ#1926073)

* Thu Jan 28 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.3-1
- Update to 1.0.3

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.2-5
- Add ShowReplayLogo.patch fix (BZ #1917097)

* Sun Jan 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.0.2-4
- Rebuilt for new VDR API version

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.0.2-3
- Rebuilt for new VDR API version

* Wed Aug 19 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.0.2-2
- Update 1.0.2

* Mon Aug 17 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-9
- Rebuilt for new version of graphlcd-base-2.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-5
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 20 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-3
- Rebuilt

* Mon Nov 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-2
- Add BR gcc-c++
- Add BR pkgconfig(freetype2)
- License is GPLv2+ not GPL+
- Convert HISTORY file to utf-8

* Mon Nov 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Sat Nov 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-2
- Add %%{name}-Improved-trim-function.patch

* Tue Nov 06 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-1
- Initial package
