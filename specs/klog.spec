Name:           klog
Version:        2.3.4
Release:        5%{?dist}
Summary:        A Ham radio logging program for KDE

License:        GPL-2.0-or-later
URL:            https://www.klog.xyz/

Source0:        https://github.com/ea4k/klog/releases/download/%{version}/%{name}-%{version}.tar.gz
Source100:      klog.desktop
Source101:      klog_48x48.png
Source102:      klog_64x64.png
Source103:      klog_128x128.png
Source104:      klog_256x256.png
Source105:      klog_512x512.png
Source106:      xyz.klog.klog.metainfo.xml

ExcludeArch:    i686

BuildRequires:  desktop-file-utils
BuildRequires:  dos2unix
BuildRequires:  gettext
BuildRequires:  hamlib-devel
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtcharts-devel
BuildRequires:  qt5-qtserialport-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtlocation-devel

%if ! 0%{?rhel} < 8
Recommends:     trustedqsl
%endif

%description
# Spelling intentional ignore rpmlint warnings.
KLog is a Ham radio logging program for KDE
Some features include:
    * DXCC award support.
    * Basic IOTA support.
    * Importing from Cabrillo files.
    * Importing from TLF.
    * Adding/Editing QSOs.
    * Save/read to/from disk file the log - ADIF format by default.
    * English/Spanish/Portuguese/Galician/Serbian/Swedish support.
    * QSL sent/received support.
    * Read/Write ADIF.
    * Delete QSOs.
    * DX-Cluster support. 

Some additional features of this application are still under development
and are not yet implemented.


%prep
%autosetup -p1

# Prep icon files
install -p %{SOURCE101} %{SOURCE102} %{SOURCE103} %{SOURCE104} %{SOURCE105} .

# Fix line endings
dos2unix TODO


%build
%qmake_qt5 PREFIX=%{buildroot}%{_prefix} src.pro
%make_build


%install
%make_install

# Manuall install translations because qmake is being stupid.
mkdir -p %{buildroot}%{_datadir}/%{name}/translations
install -pm 0644 build/target/translations/*.qm \
                 %{buildroot}%{_datadir}/%{name}/translations/

# Remove docs installed to wrong location
rm -f %{buildroot}%{_datadir}/%{name}/{COPYING,Changelog}

%find_lang %{name} --with-qt

# Install the provided desktop icon
for size in 48x48 64x64 128x128 256x256 512x512; do
    install -pDm 0644 %{name}_$size.png \
        %{buildroot}%{_datadir}/icons/hicolor/$size/apps/%{name}.png
done

# Install the provided desktop file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
    %{SOURCE100}

# Install the provided AppStream metadata file
install -Dm 0644 %{SOURCE106} \
    %{buildroot}%{_metainfodir}/xyz.klog.klog.metainfo.xml


%files -f %{name}.lang
%doc AUTHORS README TODO NEWS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}/mapqmlfile.qml
%{_datadir}/%{name}/marker.qml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_metainfodir}/xyz.klog.klog.metainfo.xml


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 31 2024 Richard Shaw <hobbes1069@gmail.com> - 2.3.4-4
- Rebuild for Hamlib 4.6.

* Tue Aug 27 2024 Daniel Rusek <mail@asciiwolf.com> - 2.3.4-3
- Add AppStream metadata.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 22 2024 Richard Shaw <hobbes1069@gmail.com> - 2.3.4-1
- Update to 2.3.4.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Richard Shaw <hobbes1069@gmail.com> - 2.3.3-1
- Update to 2.3.3.

* Thu Aug 03 2023 Richard Shaw <hobbes1069@gmail.com> - 2.3.2-1
- Update to 2.3.2.

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Richard Shaw <hobbes1069@gmail.com> - 2.3-1
- Update to 2.3.

* Mon Nov 07 2022 Richard Shaw <hobbes1069@gmail.com> - 2.2.1-2
- Rebuild for updated hamlib 4.5.

* Sun Sep 04 2022 Richard Shaw <hobbes1069@gmail.com> - 2.2.1-1
- Update to 2.2.1.

* Mon Aug 22 2022 Richard Shaw <hobbes1069@gmail.com> - 2.2-1
- Update to 2.2.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Apr 15 2022 Richard Shaw <hobbes1069@gmail.com> - 2.1-1
- Update to 2.1.

* Sat Feb 19 2022 Richard Shaw <hobbes1069@gmail.com> - 1.9-1
- Update to 1.9.

* Sat Jan 29 2022 Richard Shaw <hobbes1069@gmail.com> - 1.8.7-1
- Update to 1.8.7.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 1.8.5-4
- Rebuild for hamlib 4.4.

* Thu Dec 23 2021 Richard Shaw <hobbes1069@gmail.com> - 1.8.5-3
- 36-build-side-49086

* Tue Oct 12 2021 Richard Shaw <hobbes1069@gmail.com> - 1.8.5-2
- Rebuild for hamlib 4.3.1.

* Sun Oct 03 2021 Richard Shaw <hobbes1069@gmail.com> - 1.8.5-1
- Update to 1.8.5.

* Sun Aug 29 2021 Richard Shaw <hobbes1069@gmail.com> - 1.8.4-1
- Update to 1.8.3.

* Tue Aug 24 2021 Richard Shaw <hobbes1069@gmail.com> - 1.8.3-1
- Update to 1.8.3.

* Fri Aug 20 2021 Richard Shaw <hobbes1069@gmail.com> - 1.8.1-1
- Update to 1.8.1.

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jun 27 2021 Richard Shaw <hobbes1069@gmail.com> - 1.6-1
- Update to 1.6.

* Sun May 30 2021 Richard Shaw <hobbes1069@gmail.com> - 1.5.3-2
- Rebuild for hamlib 4.2.

* Mon May 24 2021 Richard Shaw <hobbes1069@gmail.com> - 1.5.3-1
- Update to 1.5.3.

* Tue May 11 2021 Richard Shaw <hobbes1069@gmail.com> - 1.5.2-1
- Update to 1.5.2.

* Sun May 02 2021 Richard Shaw <hobbes1069@gmail.com> - 1.5.1-1
- Update to 1.5.1.

* Sat Feb 06 2021 Richard Shaw <hobbes1069@gmail.com> - 1.4.7-1
- Update to 1.4.7.

* Tue Feb 02 2021 Richard Shaw <hobbes1069@gmail.com> - 1.4.4-3
- Rebuild for hamlib 4.1.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 24 2020 Richard Shaw <hobbes1069@gmail.com> - 1.4.4-1
- Update to 1.4.4.

* Wed Dec 09 2020 Richard Shaw <hobbes1069@gmail.com> - 1.4.3-1
- Update to 1.4.3.

* Tue Dec 08 2020 Richard Shaw <hobbes1069@gmail.com> - 1.4.2-1
- Update to 1.4.2.

* Tue Dec 08 2020 Richard Shaw <hobbes1069@gmail.com> - 1.4.1-1
- Update to 1.4.1.

* Mon Dec 07 2020 Richard Shaw <hobbes1069@gmail.com> - 1.4-1
- Update to 1.4.

* Tue Oct 06 2020 Richard Shaw <hobbes1069@gmail.com> - 1.3.1-1
- Update to 1.3.1.

* Sun Sep 20 2020 Richard Shaw <hobbes1069@gmail.com> - 1.2.2-1
- Update to 1.2.2.

* Tue Aug 11 2020 Richard Shaw <hobbes1069@gmail.com> - 1.2-1
- Update to 1.2.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 1.0-2
- Rebuild for hamlib 4.

* Tue Mar 31 2020 Richard Shaw <hobbes1069@gmail.com> - 1.0-1
- Update to 1.0.

* Wed Feb 05 2020 Richard Shaw <hobbes1069@gmail.com> - 0.9.9.1-1
- Update to 0.9.9.1.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 29 2019 Richard Shaw <hobbes1069@gmail.com> - 0.9.8-1
- Update to 0.9.8.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Richard Shaw <hobbes1069@gmail.com> - 0.9.7.1-1
- Update to 0.9.7.1.

* Sun Mar 03 2019 Richard Shaw <hobbes1069@gmail.com> - 0.9.7-1
- Update to 0.9.7.
- Remove upstreamed patch but still doesn't install translations.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 03 2018 Richard Shaw <hobbes1069@gmail.com> - 0.9.5-1
- Update to 0.9.5.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Richard Shaw <hobbes1069@gmail.com> - 0.9.2.9-1
- Update to 0.9.2.9.

* Tue Jan 23 2018 Richard Shaw <hobbes1069@gmail.com> - 0.9.2.8-1
- Update to latest upstream release.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Richard Shaw <hobbes1069@gmail.com> - 0.5.6-16
- Rebuild for hamlib 3.1.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.6-13
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 1 2011 Randall J. Berry, N3LRX <dp67@fedoraproject.org>  - 0.5.6-5
- Rebuild for Rawhide Fix Broken Deps

* Sat Jul 17 2010 Randall J. Berry, N3LRX <dp67@fedoraproject.org>  - 0.5.6-4
- Edit spec per review

* Fri Jul 16 2010 Randall J. Berry, N3LRX <dp67@fedoraproject.org>  - 0.5.6-3
- Added desktop-file-install/validate per review
- Fixed unowned directories per review

* Mon Jul 12 2010 Randall J. Berry, N3LRX <dp67@fedoraproject.org>  - 0.5.6-2
- Forgot to apply locale files.

* Sun Jul 4 2010 Randall J. Berry, N3LRX <dp67@fedoraproject.org>  - 0.5.6-1
- Upstream Update 0.5.6
- Fixes spurious-executables
- Submit for review

* Mon Jun 28 2010 Randall J. Berry, N3LRX <dp67@fedoraproject.org>  - 0.5.5-1
- First spec build
