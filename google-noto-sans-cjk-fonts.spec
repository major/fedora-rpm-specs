# SPDX-License-Identifier: MIT

Epoch:   1
Version: 2.004
Release: 4%{?dist}
URL:     https://github.com/googlefonts/noto-cjk

BuildRequires:            python3

%global foundry           Google
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE

%global fontfamily        Noto Sans CJK
%global fontsummary       Google Noto Sans CJK Fonts
%global fonts             *.ttc
%global fontconfs         65-1-%{fontpkgname}.conf %{SOURCE10} %{SOURCE11}
%global fontdescription   %{expand:
Noto CJK fonts, supporting Simplified Chinese, Traditional Chinese, \
Japanese, and Korean. The supported scripts are Han, Hiragana, Katakana, \
Hangul, and Bopomofo. Latin, Greek, Cyrllic, and various symbols are also \
supported for compatibility with CJK standards.

The google-noto-sans-cjk-fonts package contains Google Noto Sans CJK fonts.
}

Source0:  https://github.com/googlefonts/noto-cjk/releases/download/Sans%{version}/03_NotoSansCJK-OTC.zip
Source1:  genfontconf.py
Source10: 65-%{fontpkgname}.conf
Source11: 65-google-noto-sans-cjk-mono-fonts.conf

%global fontpkgheader     %{expand:
# The Noto Sans CJK fonts have both Variable and non-Variable fonts.
# It will cause some issues if install both VF and non-VF fonts,
# add Conflicts here to only install either VF or non-VF fonts.
Conflicts: google-noto-sans-cjk-vf-fonts
}


%fontpkg

%prep
%autosetup -c

cp %{SOURCE1} .

python3 genfontconf.py "ja" "monospace" "Noto Sans Mono CJK JP" \
        "ja" "sans-serif" "Noto Sans CJK JP" \
        "ko" "monospace" "Noto Sans Mono CJK KR" \
        "ko" "sans-serif" "Noto Sans CJK KR" \
        "zh-cn:zh-sg" "monospace" "Noto Sans Mono CJK SC" \
        "zh-cn:zh-sg" "sans-serif" "Noto Sans CJK SC" \
        "zh-tw:cmn:hak:lzh:nan" "monospace" "Noto Sans Mono CJK TC" \
        "zh-tw:cmn:hak:lzh:nan" "sans-serif" "Noto Sans CJK TC" \
        "zh-hk:zh-mo:yue" "monospace" "Noto Sans Mono CJK HK" \
        "zh-hk:zh-mo:yue" "sans-serif" "Noto Sans CJK HK" \
    | xmllint --format - |tee 65-1-google-noto-sans-cjk-fonts.conf


%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.004-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 24 2023 Peng Wu <pwu@redhat.com> - 1:2.004-3
- Fix dnf upgrade issue
- Resolves: RHBZ#2181349

* Thu Mar 16 2023 Peng Wu <pwu@redhat.com> - 1:2.004-2
- Update the spec file with some Obsoletes and Provides

* Fri Feb  3 2023 Peng Wu <pwu@redhat.com> - 1:2.004-1
- Initial Packaging
- Migrate to SPDX license
