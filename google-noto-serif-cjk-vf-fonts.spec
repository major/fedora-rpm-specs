# SPDX-License-Identifier: MIT

Epoch:   1
Version: 2.001
Release: 1%{?dist}
URL:     https://github.com/googlefonts/noto-cjk

BuildRequires:            python3

%global foundry           Google
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE

%global fontfamily        Noto Serif CJK VF
%global fontsummary       Google Noto Serif CJK Variable Fonts
%global fonts             *.ttc
%global fontconfs         65-0-%{fontpkgname}.conf %{SOURCE10}
%global fontdescription   %{expand:
Noto CJK fonts, supporting Simplified Chinese, Traditional Chinese, \
Japanese, and Korean. The supported scripts are Han, Hiragana, Katakana, \
Hangul, and Bopomofo. Latin, Greek, Cyrllic, and various symbols are also \
supported for compatibility with CJK standards.

The google-noto-serif-cjk-vf-fonts package contains Google Noto Serif CJK Variable fonts.
}

Source0:  https://github.com/googlefonts/noto-cjk/releases/download/Serif%{version}/02_NotoSerifCJK-OTF-VF.zip
Source1:  genfontconf.py
Source10: 65-%{fontpkgname}.conf

%global obsoletes_epoch_version_release 0:20201206-8

%global obsoletes_pkg()\
%define subpkgname %1\
Obsoletes:      %{subpkgname} < %{obsoletes_epoch_version_release}\
Provides:       %{subpkgname} = %{epoch}:%{version}-%{release}\

%global obsoletes_serif()\
%define langname %1\
%obsoletes_pkg google-noto-sans-cjk-%{langname}-fonts\
%obsoletes_pkg google-noto-sans-%{langname}-fonts\

%global fontpkgheader     %{expand:
# The Noto Serif CJK fonts have both Variable and non-Variable fonts.
# It will cause some issues if install both VF and non-VF fonts,
# add Conflicts here to only install either VF or non-VF fonts.
Conflicts: google-noto-serif-cjk-fonts

%obsoletes_pkg google-noto-serif-cjk-ttc-fonts

%obsoletes_serif sc
%obsoletes_serif tc
%obsoletes_serif jp
%obsoletes_serif kr

}

%fontpkg

%prep
%autosetup -c

cp -p Variable/OTC/NotoSerifCJK-VF.otf.ttc NotoSerifCJK-VF.ttc

cp %{SOURCE1} .

python3 genfontconf.py "ja" "serif" "Noto Serif CJK JP" \
        "ko" "serif" "Noto Serif CJK KR" \
        "zh-cn:zh-sg" "serif" "Noto Serif CJK SC" \
        "zh-tw:cmn:hak:lzh:nan" "serif" "Noto Serif CJK TC" \
        "zh-hk:zh-mo:yue" "serif" "Noto Serif CJK HK" \
    | xmllint --format - |tee 65-0-google-noto-serif-cjk-vf-fonts.conf


%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Fri Feb  3 2023 Peng Wu <pwu@redhat.com> - 1:2.001-1
- Initial Packaging
- Migrate to SPDX license
