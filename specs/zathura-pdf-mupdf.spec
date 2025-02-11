Name:             zathura-pdf-mupdf

Version:          0.4.4
Release:          3%{?dist}
Summary:          PDF support for zathura via mupdf
License:          Zlib
URL:              https://pwmt.org/projects/%{name}/
Source0:          %{url}/download/%{name}-%{version}.tar.xz
Patch1:           0001-configure-for-shared-mupdf-build.patch

BuildRequires:    binutils
BuildRequires:    cairo-devel
# Needed to validate the desktop file
BuildRequires:    desktop-file-utils
BuildRequires:    gcc
BuildRequires:    git-core
BuildRequires:    girara-devel
BuildRequires:    glib2-devel
# Needed to validate appdata
BuildRequires:    libappstream-glib
BuildRequires:    libjpeg-turbo-devel
BuildRequires:    meson >= 0.43
BuildRequires:    mupdf-devel >= 1.23.9-3
BuildRequires:    zathura-devel >= 0.3.9
Requires:         zathura >= 0.3.9

# Old plugins used alternatives
Conflicts:        zathura-pdf-poppler < 0.2.9

%description
This plugin adds PDF support to zathura using the mupdf rendering engine.

%prep
%autosetup -S git -p1

%build
%meson
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

# Clean the old alternatives link
%pre
[ -L %{_libdir}/zathura/pdf.so ] && rm -f %{_libdir}/zathura/pdf.so || :

%files
%license LICENSE
%doc AUTHORS
%{_libdir}/zathura/libpdf-mupdf.so
%{_datadir}/applications/org.pwmt.zathura-pdf-mupdf.desktop
%{_datadir}/metainfo/org.pwmt.zathura-pdf-mupdf.metainfo.xml

%changelog
* Sat Feb 08 2025 Michael J Gruber <mjg@fedoraproject.org> - 0.4.4-3
- Rebuild (mupdf)

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Dec 23 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.4.4-1
- Update to 0.4.4 (rhbz#2302704)

* Mon Dec 23 2024 Ankur Sinha <sanjay.ankur@gmail.com> - 0.4.3-4
- Rebuild for girara 0.4.5, mupdf 1.25.2

* Tue Nov 12 2024 Sandro Mani <manisandro@gmail.com> - 0.4.3-3
- Rebuild (tesseract)

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 05 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.4.3-1
- Update to 0.4.3 (rhbz#2290478)

* Fri May 10 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.4.1-8
- Rebuild against zathura 0.5.6

* Tue Mar 19 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.4.1-6
- Rebuild against mupdf 1.24.0

* Fri Feb 02 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.4.1-5
- Build against mupdf shared library

* Sun Jan 28 2024 Sandro Mani <manisandro@gmail.com> - 0.4.1-4
- Rebuild (tesseract)

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 09 2023 Michael J Gruber <mjg@fedoraproject.org> - 0.4.1-2
- Rebuild against mupdf 1.23.7

* Wed Oct 11 2023 Michael J Gruber <mjg@fedoraproject.org> - 0.4.1-1
- Update to 0.4.1 (#2238877)

* Sat Oct 07 2023 Sandro Mani <manisandro@gmail.com> - 0.4.0-13
- Rebuild (tesseract)

* Mon Sep 04 2023 Michael J Gruber <mjg@fedoraproject.org> - 0.4.0-12
- build against mupdf 1.23.3

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Sandro Mani <manisandro@gmail.com> - 0.4.0-10
- Rebuild (tesseract)

* Fri Jun 23 2023 Michael J Gruber <mjg@fedoraproject.org> - 0.4.0-9
- build against mupdf 1.22.2

* Thu May 11 2023 Michael J Gruber <mjg@fedoraproject.org> - 0.4.0-8
- build against mupdf 1.22.1

* Sat Apr 15 2023 Michael J Gruber <mjg@fedoraproject.org> - 0.4.0-7
- build against mupdf 1.22.0

* Thu Apr 06 2023 Sandro Mani <manisandro@gmail.com> - 0.4.0-6
- Rebuild (tesseract)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 24 2022 Michael J Gruber <mjg@fedoraproject.org> - 0.4.0-4
- SPDX migration

* Fri Dec 23 2022 Sandro Mani <manisandro@gmail.com> - 0.4.0-3
- Rebuild (tesseract)

* Wed Dec 21 2022 Sandro Mani <manisandro@gmail.com> - 0.4.0-2
- Rebuild (leptonica)

* Mon Nov 28 2022 Michael J Gruber <mjg@fedoraproject.org> - 0.4.0-1
- Update to 0.4.0 (rhbz#2148751)

* Mon Nov 28 2022 Michael J Gruber <mjg@fedoraproject.org> - 0.3.9-2
- build against mupdf 1.21.0

* Tue Aug 23 2022 Michael J Gruber <mjg@fedoraproject.org> - 0.3.9-1
- Update to 0.3.9 (rhbz#2120429)

* Fri Aug 12 2022 Michael J Gruber <mjg@fedoraproject.org> - 0.3.8-8
- build against mupdf 1.20.3

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Sandro Mani <manisandro@gmail.com> - 0.3.8-6
- Rebuild (tesseract)

* Wed Jun 15 2022 Michael J Gruber <mjg@fedoraproject.org> - 0.3.8-5
- build against mupdf 1.20.0

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 0.3.8-4
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Wed Apr 13 2022 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.8-2
- merge https://src.fedoraproject.org/rpms/zathura-pdf-mupdf/pull-request/12
- Remove upstreamed patch
- Restore build with external libraries

* Sat Apr 02 2022 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.8-1
- update to latest release

* Thu Mar 10 2022 Sandro Mani <manisandro@gmail.com> - 0.3.7-7
- Rebuild for tesseract 5.1.0

* Fri Feb 25 2022 Sandro Mani <manisandro@gmail.com> - 0.3.7-6
- Rebuild (leptonica)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 19 2021 Sandro Mani <manisandro@gmail.com> - 0.3.7-4
- Rebuild (tesseract)

* Tue Dec 14 2021 Sandro Mani <manisandro@gmail.com> - 0.3.7-3
- Rebuild (tesseract)

* Tue Oct 12 2021 Michael J Gruber <mjg@fedoraproject.org> - 0.3.7-2
- rebuild for mupdf 1.19.0

* Sat Aug 28 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.7-1
- merge PR from @mjg manually: https://src.fedoraproject.org/rpms/zathura-pdf-mupdf/pull-request/10#
- Update to 0.3.7 (bz #1982324)
- Remove upstreamed patch

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 24 2021 Michael J Gruber <mjg@fedoraproject.org> - 0.3.6-6
- rebuild for mupdf CVE-2021-3407

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 09 2020 Michael J Gruber <mjg@fedoraproject.org> - 0.3.6-4
- link against gumbo

* Thu Oct 08 2020 Michael J Gruber <mjg@fedoraproject.org> - 0.3.6-3
- rebuild for mupdf 1.18.0

* Fri Sep 18 2020 Michael J Gruber <mjg@fedoraproject.org> - 0.3.6-2
- rebuild with jbig2dec 0.19

* Mon Sep 07 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.6-1
- Update to new release

* Tue Jul 28 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.5-4
- Rebuild to require exact jgib2dec version
- #1860987

* Sat May 16 2020 Michael J Gruber <mjg@fedoraproject.org> - 0.3.5-3
- Adjust to mupdf 1.17

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.5-1
- Update to 0.3.5

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Petr Šabata <contyk@redhat.com> - 0.3.4-1
- 0.3.4 bump
- Fixes rhbz#1645552

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Petr Šabata <contyk@redhat.com> - 0.3.3-1
- 0.3.3 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Petr Šabata <contyk@redhat.com> - 0.3.1-1
- 0.3.1 bump
- Don't link against the no longer provided libmupdfthird,
  see rhbz#1438824 for more info

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 16 2016 Petr Šabata <contyk@redhat.com> - 0.3.0-3
- Rebuild against mujs-0-6.20161031gita0ceaf5

* Thu Sep 29 2016 Petr Šabata <contyk@redhat.com> - 0.3.0-2
- Rebuild against mujs-0-5.20160921git5c337af

* Fri Feb 26 2016 Petr Šabata <contyk@redhat.com> - 0.3.0-1
- 0.3.0 bump

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Petr Šabata <contyk@redhat.com> - 0.2.8-4
- Rebuild with mujs-0-1.20150929git0827611

* Wed Jul 01 2015 Petr Šabata <contyk@redhat.com> - 0.2.8-3
- Handle the desktop file properly

* Tue Jun 23 2015 Petr Šabata <contyk@redhat.com> - 0.2.8-2
- Correct the %%files section

* Tue Jun 09 2015 Petr Šabata <contyk@redhat.com> - 0.2.8-1
- Initial packaging
