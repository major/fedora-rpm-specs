Name:           opentype-sanitizer
# The following dependent packages have their versions kept in sync with
# opentype-sanitizer, and should be updated at the same time, ideally as a
# multi-build update (i.e., using a side tag).
#
# - python-opentype-sanitizer
Version:        9.1.0
Release:        %autorelease
Summary:        Parses and serializes OpenType/WOFF/WOFF2 font files

# Some test fonts (even after filtering out those that are not freely
# redistributable—see below) have other acceptable licenses, such as OFL-1.1 or
# Bitstream-Vera, and certain build-system files are MIT-licensed; but none are
# installed, so they do not affect the license field of the package.
License:        BSD-3-Clause
URL:            https://github.com/khaledhosny/ots
# This is generated from the upstream tarball (ots-%%{version}.tar.gz) by
# get-source.py, which excludes test fonts that are not redistributable.
Source0:        ots-%{version}-filtered.tar.xz
# Usage: ./get-source.py VERSION
#
# Requires python3, python3-requests, python3-tqdm, and python3-fonttools.
#
# Some test fonts have unknown or restrictive licenses and cannot be
# redistributed in Fedora. We could remove all the test fonts, but the
# more-sophisticated approach in this script allows us to keep as many test
# fonts as possible:
#   1. Fonts with restrictive distributability metadata (fstype in the OS2
#      section) are filtered out.
#   2. Fonts with known-good licenses are included.
#   3. Fonts that have been manually audited for distributability can be
#      recorded in the script source so that they are always included or always
#      filtered out
#   4. Fonts not accepted or rejected in 1–3 above are filtered out as a
#      precaution, and manual auditing is suggested to the script user.
Source1:        get-source.py
# This is also generated from Source1. Since test fonts are now manually
# specified in the meson files, we must patch out those that have been removed.
# This file, a list of SHA1 checksums (which correspond to filenames) makes
# that possible.
Source2:        ots-%{version}-excluded-font-checksums.txt

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libwoff2dec)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(gtest)
# The source package includes several dozen sample “good” fonts to provide a
# minimal set of functional tests. To more thoroughly test “good” fonts,
# HowToTest.md says, “install as many as possible TrueType and OpenType fonts.”
# Rather than adding a huge list of BR’s on arbitrary fonts, and trying to
# ensure that the tests find them, we consider that the bundled “good” fonts
# are adequate for validating the package build (as opposed to developing
# opentype-sanitizer itself).

%global common_description %{expand:
The OpenType Sanitizer (OTS) parses and serializes OpenType files (OTF, TTF)
and WOFF and WOFF2 font files, validating them and sanitizing them as it goes.

The C library is integrated into Chromium and Firefox, and also simple command
line tools to check files offline in a Terminal.

The CSS font-face property is great for web typography. Having to use images in
order to get the correct typeface is a great sadness; one should be able to use
vectors.

However, on many platforms the system-level TrueType font renderers have never
been part of the attack surface before, and putting them on the front line is a
scary proposition... Especially on platforms like Windows, where it’s a
closed-source blob running with high privilege.}

%description %{common_description}


%prep
%autosetup -n ots-%{version} -p1
# Remove bundled dependencies
rm -rf third_party
# Disable tests that use fonts that were filtered out for license issues.
sed -r -i "/$(tr '\n' '|' < '%{SOURCE2}' | sed -r 's@\|+$@@')/d" \
    tests/meson.build


%build
# gtest 1.13.0 requires at least C++14
%meson -Dcpp_std=c++14
%meson_build


%install
%meson_install


%check
%meson_test


%files
%license LICENSE
%doc README.md
%doc docs/*.md

%{_bindir}/ots-idempotent
%{_bindir}/ots-perf
%{_bindir}/ots-sanitize
%{_bindir}/ots-side-by-side
%{_bindir}/ots-validator-checker

%{_mandir}/man1/ots-idempotent.1*
%{_mandir}/man1/ots-perf.1*
%{_mandir}/man1/ots-sanitize.1*
%{_mandir}/man1/ots-side-by-side.1*
%{_mandir}/man1/ots-validator-checker.1*


%changelog
%autochangelog
