# SPDX-License-Identifier: MIT

Epoch:   1
Version: 2.001
Release: 3%{?dist}
URL:     https://github.com/googlefonts/noto-cjk

BuildRequires:            python3

%global foundry           Google
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE

%global fontfamily        Noto Serif CJK
%global fontsummary       Google Noto Serif CJK Fonts
%global fonts             OTC/*.ttc
%global fontconfs         65-1-%{fontpkgname}.conf %{SOURCE10}
%global fontdescription   %{expand:
Noto CJK fonts, supporting Simplified Chinese, Traditional Chinese, \
Japanese, and Korean. The supported scripts are Han, Hiragana, Katakana, \
Hangul, and Bopomofo. Latin, Greek, Cyrllic, and various symbols are also \
supported for compatibility with CJK standards.

The google-noto-serif-cjk-fonts package contains Google Noto Serif CJK fonts.
}

Source0:  https://github.com/googlefonts/noto-cjk/releases/download/Serif%{version}/04_NotoSerifCJKOTC.zip
Source1:  genfontconf.py
Source10: 65-%{fontpkgname}.conf

%global fontpkgheader     %{expand:
# The Noto Serif CJK fonts have both Variable and non-Variable fonts.
# It will cause some issues if install both VF and non-VF fonts,
# add Conflicts here to only install either VF or non-VF fonts.
Conflicts: google-noto-serif-cjk-vf-fonts
}


%fontpkg

%prep
%autosetup -c

cp %{SOURCE1} .

python3 genfontconf.py "ja" "serif" "Noto Serif CJK JP" \
        "ko" "serif" "Noto Serif CJK KR" \
        "zh-cn:zh-sg" "serif" "Noto Serif CJK SC" \
        "zh-tw:cmn:hak:lzh:nan" "serif" "Noto Serif CJK TC" \
        "zh-hk:zh-mo:yue" "serif" "Noto Serif CJK HK" \
    | xmllint --format - |tee 65-1-google-noto-serif-cjk-fonts.conf


%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Fri Mar 24 2023 Peng Wu <pwu@redhat.com> - 1:2.001-3
- Fix dnf upgrade issue

* Thu Mar 16 2023 Peng Wu <pwu@redhat.com> - 1:2.001-2
- Update the spec file with some Obsoletes and Provides

* Fri Feb  3 2023 Peng Wu <pwu@redhat.com> - 1:2.001-1
- Initial Packaging
- Migrate to SPDX license
