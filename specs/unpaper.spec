Name:           unpaper
Version:        7.0.0
Release:        13%{?dist}
Summary:        Post-processing of scanned and photocopied book pages
# AUTHORS:      GPL-2.0-only
# constants.h:  GPL-2.0-only
# doc/basic-concepts.md:    GPL-2.0-only
# doc/file-formats.md:      GPL-2.0-only
# doc/image-processing.md:  GPL-2.0-only
# doc/img/*.png.license:    GPL-2.0-only
# doc/unpaper.1.rst:        GPL-2.0-only
# file.c:           GPL-2.0-only
# imageprocess.c:   GPL-2.0-only
# imageprocess.h:   GPL-2.0-only
# LICENSES/0BSD.txt:    0BSD text
# LICENSES/GPL-2.0-only.txt:    GPL-2.0 text
# other files:      GPL-2.0-only
# README.md:        GPL-2.0-only
# version.h.in:     0BSD
## In tests subpackage
# LICENSES/MIT.txt: MIT text
# tests/golden_images/*.license     GPL-2.0-only
# tests/source_images/*.license     GPL-2.0-only
# tests/unpaper_tests.py:           GPL-2.0-only AND MIT
## Not in any binary package
# doc/conf.py:      MIT
# LICENSES/Apache-2.0.txt:      Apache-2.0 text
# meson.build:      MIT
# .dir-locals.el:   MIT
# .editorconfig:    0BSD
# .github/workflows/meson-build-and-test.yml:   Apache-2.0
# .github/workflows/pre-commit.yml: MIT
# .gitignore:       MIT
# .mailmap:         MIT
# .mergify.yml:     MIT
# .pre-commit-config.yaml:  MIT
SourceLicense:  GPL-2.0-only AND 0BSD AND MIT AND Apache-2.0
License:        GPL-2.0-only AND 0BSD
URL:            https://www.flameeyes.eu/projects/%{name}
Source0:        https://www.flameeyes.eu/files/%{name}-%{version}.tar.xz
# Missing a signature, requested by e-mail
# <https://flameeyes.blog/2022/05/10/unpaper-7-0-0-release/>.
#Source1:        https://www.flameeyes.eu/files/%%{name}-%%{version}.tar.xz.sig
## A key exported from keyserver <hkp://pgp.surfnet.nl> on 2022-02-25.
#Source2:        gpgkey-BDAEF3008A1CC62079C2A16847664B94E36B629F.gpg
# 1/2Set an update option to supress a warning with ffmpeg-5.1,
# in upstream after 7.0.0,
# <https://github.com/unpaper/unpaper/issues/113>
Patch0:         unpaper-7.0.0-Use-avformat_alloc_output_context2-to-create-the-out.patch
# 2/2 Set an update option to supress a warning with ffmpeg-5.1,
# in upstream after 7.0.0,
# <https://github.com/unpaper/unpaper/issues/113>
Patch1:         unpaper-7.0.0-Set-the-update-option-to-suppress-the-ffmpeg-5.1-war.patch
BuildRequires:  gcc
#BuildRequires:  gnupg2
BuildRequires:  meson >= 0.57
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  python3-sphinx >= 3.4
# Tests:
BuildRequires:  python3dist(pytest)
# python3-pillow for PIL Python module
BuildRequires:  python3-pillow

%description
unpaper is a post-processing tool for scanned sheets of paper, especially for
book pages that have been scanned from previously created photocopies. The
main purpose is to make scanned book pages better readable on screen after
conversion to PDF. Additionally, unpaper might be useful to enhance the
quality of scanned pages before performing optical character recognition (OCR).

unpaper tries to clean scanned images by removing dark edges that appeared
through scanning or copying on areas outside the actual page content (e.g. dark
areas between the left-hand-side and the right-hand-side of a double-sided
book-page scan).

The program also tries to detect misaligned centering and rotation of pages
and will automatically straighten each page by rotating it to the correct
angle. This process is called "deskewing".

%package tests
Summary:        Tests for %{name}
License:        GPL-2.0-only AND MIT
BuildArch:      noarch
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
# python3-pillow for PIL Python module
Requires:       python3-pillow
Requires:       python3-pytest
# Parallelize tests
Requires:       python3-pytest-xdist

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
#%%{gpgverify} --keyring='%%{SOURCE2}' --signature='%%{SOURCE1}' --data='%%{SOURCE0}'
%autosetup -p1

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a tests %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
export TEST_IMGSRC_DIR=tests/source_images
export TEST_GOLDEN_DIR=tests/golden_images
export TEST_UNPAPER_BINARY=%{_bindir}/unpaper
cd %{_libexecdir}/%{name} && exec pytest -v -n "$(getconf _NPROCESSORS_ONLN)" tests/unpaper_tests.py
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test
%{_fixperms} %{buildroot}/*

%files
%license LICENSES/0BSD.txt LICENSES/GPL-2.0-only.txt
%{_bindir}/unpaper
%{_mandir}/man1/unpaper.*
%doc AUTHORS doc/*.md doc/img NEWS README.md

%files tests
%license LICENSES/MIT.txt
%{_libexecdir}/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 23 2024 Fabio Valentini <decathorpe@gmail.com> - 7.0.0-12
- Rebuild for ffmpeg 7

* Mon Sep 23 2024 Petr Pisar <ppisar@redhat.com> - 7.0.0-11
- Define a license of a source package

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 12 2023 Neal Gompa <ngompa@fedoraproject.org> - 7.0.0-7
- Rebuild for ffmpeg 6.0

* Wed Feb 08 2023 Petr Pisar <ppisar@redhat.com> - 7.0.0-6
- Convert license tags to an SPDX format

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 10 2022 Petr Pisar <ppisar@redhat.com> - 7.0.0-4
- Set an update option to supress a warning with ffmpeg-5.1 (upstream #113)

* Mon Aug 29 2022 Neal Gompa <ngompa@fedoraproject.org> - 7.0.0-3
- Rebuild for ffmpeg 5.1 (#2121070)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Petr Pisar <ppisar@redhat.com> - 7.0.0-1
- 7.0.0 bump
- License changed from (GPLv2) to (GPLv2 and 0BSD and MIT)
- Package the tests

* Tue Mar 08 2022 Neal Gompa <ngompa@fedoraproject.org> - 6.1^20220117.gite515408-2
- Rebuild for ffmpeg 5.0 ABI fix (#2061392)

* Fri Feb 25 2022 Petr Pisar <ppisar@redhat.com> - 6.1^20220117.gite515408-1
- 6.1 bump from upstream git tree
- License changed to GPLv2

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 07 2016 Petr Pisar <ppisar@redhat.com> - 0.3-15
- Modernize spec file

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 0.3-11
- Fix FTBFS with -Werror=format-security (#1037369, #1107039)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3-2
- Autorebuild for GCC 4.3

* Mon Jan 21 2008 Bernard Johnson <bjohnson@symetrix.com> - 0.3-1
- 0.3
- license clarification

* Mon Mar 19 2007 Bernard Johnson <bjohnson@symetrix.com> - 0_2-2
- repackage tgz file without included ELF binary

* Thu Mar 15 2007 Bernard Johnson <bjohnson@symetrix.com> - 0_2-1
- initial release
