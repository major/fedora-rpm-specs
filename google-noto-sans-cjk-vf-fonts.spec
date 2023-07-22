# SPDX-License-Identifier: MIT

Epoch:   1
Version: 2.004
Release: 3%{?dist}
URL:     https://github.com/googlefonts/noto-cjk

BuildRequires:            python3

%global foundry           Google
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE

%global fontfamily        Noto Sans CJK VF
%global fontsummary       Google Noto Sans CJK Variable Fonts
%global fonts             *.ttc
%global fontconfs         65-0-%{fontpkgname}.conf %{SOURCE10} %{SOURCE11}
%global fontdescription   %{expand:
Noto CJK fonts, supporting Simplified Chinese, Traditional Chinese, \
Japanese, and Korean. The supported scripts are Han, Hiragana, Katakana, \
Hangul, and Bopomofo. Latin, Greek, Cyrllic, and various symbols are also \
supported for compatibility with CJK standards.

The google-noto-sans-cjk-vf-fonts package contains Google Noto Sans CJK Variable fonts.
}

Source0:  https://github.com/googlefonts/noto-cjk/releases/download/Sans%{version}/01_NotoSansCJK-OTF-VF.zip
Source1:  genfontconf.py
Source10: 65-%{fontpkgname}.conf
Source11: 65-google-noto-sans-cjk-mono-vf-fonts.conf

%global obsoletes_epoch_version_release 0:20201206-8

%global obsoletes_pkg()\
%define subpkgname %1\
Obsoletes:      %{subpkgname} < %{obsoletes_epoch_version_release}\
Provides:       %{subpkgname} = %{epoch}:%{version}-%{release}\

%global obsoletes_sans()\
%define langname %1\
%obsoletes_pkg google-noto-sans-cjk-%{langname}-fonts\
%obsoletes_pkg google-noto-sans-mono-cjk-%{langname}-fonts\

%global fontpkgheader     %{expand:

# The Noto Sans CJK fonts have both Variable and non-Variable fonts.
# It will cause some issues if install both VF and non-VF fonts,
# add Conflicts here to only install either VF or non-VF fonts.
Conflicts: google-noto-sans-cjk-fonts

%obsoletes_pkg google-noto-cjk-fonts
%obsoletes_pkg google-noto-cjk-fonts-common
%obsoletes_pkg google-noto-sans-cjk-ttc-fonts

%obsoletes_sans sc
%obsoletes_sans tc
%obsoletes_sans hk
%obsoletes_sans jp
%obsoletes_sans kr

}


%fontpkg

%prep
%autosetup -c

cp -p Variable/OTC/NotoSansCJK-VF.otf.ttc NotoSansCJK-VF.ttc
cp -p Variable/OTC/NotoSansMonoCJK-VF.otf.ttc NotoSansMonoCJK-VF.ttc

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
    | xmllint --format - |tee 65-0-google-noto-sans-cjk-vf-fonts.conf


%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May  4 2023 Peng Wu <pwu@redhat.com> - 1:2.004-2
- Fix obsoletes_sans macro

* Fri Feb  3 2023 Peng Wu <pwu@redhat.com> - 1:2.004-1
- Initial Packaging
- Migrate to SPDX license
