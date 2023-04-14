Summary: Cross platform open source e-book reader
Name: coolreader
Version: 3.2.59
Release: 5%{?dist}
License: GPL-2.0-or-later
URL: https://github.com/buggins/coolreader
Source0: https://github.com/buggins/coolreader/archive/cr%{version}/coolreader-cr%{version}.tar.gz
Source1: cr3.appdata.xml

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(libunibreak)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: utf8proc-devel
BuildRequires: libzstd-devel

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

%description
CoolReader is fast and small cross-platform XML/CSS based eBook reader for
desktops and handheld devices. Supported formats: FB2, TXT, RTF, DOC, TCR,
HTML, EPUB, CHM, PDB, MOBI.

%prep
%autosetup -n %{name}-cr%{version}

%build
mkdir -p %{_vpath_builddir}
%cmake \
  -DGUI=QT5 \
  -DCMAKE_BUILD_TYPE=Release \
  -DMAX_IMAGE_SCALE_MUL=2 \
  -DDOC_DATA_COMPRESSION_LEVEL=3 \
  -DDOC_BUFFER_SIZE=0x1400000 \
  -D CMAKE_INSTALL_PREFIX=/usr \
  .

%cmake_build

%install
%cmake_install
install -D -pm 644 %{SOURCE1} %{buildroot}%{_metainfodir}/cr3.appdata.xml

# gather locale files
%find_lang cr3 --with-qt --without-mo

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/cr3.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/cr3.appdata.xml

%files -f cr3.lang
%license LICENSE
%{_bindir}/cr3
%{_datadir}/applications/cr3.desktop
%dir %{_datadir}/cr3
%{_datadir}/cr3/*.css
%{_datadir}/cr3/backgrounds/
%{_datadir}/cr3/hyph/
%{_datadir}/cr3/textures/
%{_datadir}/pixmaps/cr3.*
%{_metainfodir}/cr3.appdata.xml
%{_mandir}/man1/cr3.1*
%doc %{_docdir}/cr3
%doc README.md

%changelog
* Sat Mar 25 2023 Sandro <devel@penguinpee.nl> - 3.2.59-5
- Rebuild for FTBFS (RHBZ#2113154)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.59-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 7 2021 Andy Mender <andymenderunix@fedoraproject.org> - 3.2.59-1
- Bump version to 3.2.59
- Add new build dependencies

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 7 2021 Andy Mender <andymenderunix@fedoraproject.org> - 3.2.54-1
- Update to version 3.2.54

* Sun Feb 7 2021 Andy Mender <andymenderunix@fedoraproject.org> - 3.2.53-1
- Update to version 3.2.53

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 Andy Mender <andymenderunix@fedoraproject.org> - 3.2.51-1
- Update to version 3.2.51
- Remove LICENSE file patch (added to release by upstream)

* Sun Dec 6 2020 Andy Mender <andymenderunix@fedoraproject.org> - 3.2.50-2
- Add missing fribidi BuildRequires (bundled fribidi installed otherwise)
- Add missing fontconfig BuildRequires (fixes font finding)
- Clean up %%cmake call
- Remove unnecessary desktop file patch

* Sat Dec 5 2020 Andy Mender <andymenderunix@fedoraproject.org> - 3.2.50-1
- Update to version 3.2.50
- Add new BuildRequires libunibreak
- Build against Qt5, not Qt4 (Qt5 is tested by upstream)
- Use the cmake(foo) format for Qt5 BuildRequires
- Don't restrict minimal cmake version (3.17.0 in F32 already)
- Fix license from GPLv2 to GPLv2+ (never was GPLv2)
- Switch to out-of-source build (recommended by upstream)
- Properly install locales

* Mon Oct 12 2020 Jeff Law <law@redhat.com> - 3.2.34-5
- Use __cmake_in_source_build

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.34-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.34-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.2.34-1
- Update to 3.2.34

* Wed Nov 06 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.2.33-1
- Update to 3.2.33

* Mon Oct 07 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.2.32-1
- Update to 3.2.32

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 03 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.2.30-1
- Update to 3.2.30

* Sun Feb 24 2019 Sergey Avseyev <sergey.avseyev@gmail.com> - 3.2.29-1
- Initial package
