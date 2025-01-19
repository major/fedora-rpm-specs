# SPDX-License-Identifier: MIT

BuildArch: noarch

Epoch:   1
Version: 2.004
Release: 8%{?dist}
License: OFL-1.1
URL:     https://github.com/googlefonts/noto-cjk

%global foundry           Google
%global fontlicense       OFL-1.1
%global fontlicenses      LICENSE

%global common_description %{expand:
Noto CJK fonts, supporting Simplified Chinese, Traditional Chinese, \
Japanese, and Korean. The supported scripts are Han, Hiragana, Katakana, \
Hangul, and Bopomofo. Latin, Greek, Cyrllic, and various symbols are also \
supported for compatibility with CJK standards.
}

%global fontfamily1       Noto Sans HK
%global fontsummary1      Google Noto Sans HK Fonts
%global fontpkgheader1    %{expand:
}
%global fonts1            SubsetOTF/HK/*.otf
%global fontconfs1        66-google-noto-sans-hk.conf
%global fontdescription1  %{expand:
%{common_description}

This package contains Google Noto Sans HK fonts.
}

%global fontfamily2       Noto Sans JP
%global fontsummary2      Google Noto Sans JP Fonts
%global fontpkgheader2    %{expand:
}
%global fonts2            SubsetOTF/JP/*.otf
%global fontconfs2        66-google-noto-sans-jp.conf
%global fontdescription2  %{expand:
%{common_description}

This package contains Google Noto Sans JP fonts.
}

%global fontfamily3       Noto Sans KR
%global fontsummary3      Google Noto Sans KR Fonts
%global fontpkgheader3    %{expand:
}
%global fonts3            SubsetOTF/KR/*.otf
%global fontconfs3        66-google-noto-sans-kr.conf
%global fontdescription3  %{expand:
%{common_description}

This package contains Google Noto Sans KR fonts.
}

%global fontfamily4       Noto Sans SC
%global fontsummary4      Google Noto Sans SC Fonts
%global fontpkgheader4    %{expand:
}
%global fonts4            SubsetOTF/SC/*.otf
%global fontconfs4        66-google-noto-sans-sc.conf
%global fontdescription4  %{expand:
%{common_description}

This package contains Google Noto Sans SC fonts.
}

%global fontfamily5       Noto Sans TC
%global fontsummary5      Google Noto Sans TC Fonts
%global fontpkgheader5    %{expand:
}
%global fonts5            SubsetOTF/TC/*.otf
%global fontconfs5        66-google-noto-sans-tc.conf
%global fontdescription5  %{expand:
%{common_description}

This package contains Google Noto Sans TC fonts.
}

Source0:  https://github.com/googlefonts/noto-cjk/releases/download/Sans%{version}/05_NotoSansCJK-SubsetOTF.zip
Source1:  genfontconf.py

Name:     google-noto-sans-cjk-subset-fonts
Summary:  Google Noto Sans CJK Subset Fonts
%description
%wordwrap -v common_description

%fontpkg -a

%prep
%autosetup -c

cp -p %{SOURCE1} .

python3 genfontconf.py "zh-hk" "sans-serif" "Noto Sans HK" | xmllint --format - |tee 66-google-noto-sans-hk.conf

python3 genfontconf.py "ja" "sans-serif" "Noto Sans JP" | xmllint --format - |tee 66-google-noto-sans-jp.conf

python3 genfontconf.py "ko" "sans-serif" "Noto Sans KR" | xmllint --format - |tee 66-google-noto-sans-kr.conf

python3 genfontconf.py "zh-cn:zh-sg" "sans-serif" "Noto Sans SC" | xmllint --format - |tee 66-google-noto-sans-sc.conf

python3 genfontconf.py "zh-tw:zh-mo" "sans-serif" "Noto Sans TC" | xmllint --format - |tee 66-google-noto-sans-tc.conf


%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.004-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.004-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.004-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.004-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 27 2023 Peng Wu <pwu@redhat.com> - 1:2.004-4
- Fix typo
- Resolves: RHBZ#2251535

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.004-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 29 2023 Peng Wu <pwu@redhat.com> - 1:2.004-2
- Update the spec file

* Fri Feb  3 2023 Peng Wu <pwu@redhat.com> - 1:2.004-1
- Initial Packaging
- Migrate to SPDX license
