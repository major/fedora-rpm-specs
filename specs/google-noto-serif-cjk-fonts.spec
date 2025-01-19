# SPDX-License-Identifier: MIT

Epoch:   1
Version: 2.003
Release: 2%{?dist}
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
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.003-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug  1 2024 Peng Wu <pwu@redhat.com> - 1:2.003-1
- Update to 2.003

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.002-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.002-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.002-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Oct 10 2023 Peng Wu <pwu@redhat.com> - 1:2.002-2
- Drop some Conflicts from the Noto Serif CJK fonts

* Tue Aug 22 2023 Peng Wu <pwu@redhat.com> - 1:2.002-1
- Update to 2.002

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 24 2023 Peng Wu <pwu@redhat.com> - 1:2.001-3
- Fix dnf upgrade issue

* Thu Mar 16 2023 Peng Wu <pwu@redhat.com> - 1:2.001-2
- Update the spec file with some Obsoletes and Provides

* Fri Feb  3 2023 Peng Wu <pwu@redhat.com> - 1:2.001-1
- Initial Packaging
- Migrate to SPDX license
