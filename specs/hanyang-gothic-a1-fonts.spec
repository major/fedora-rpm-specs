%global git_date   20180313
%global git_commit 16680f8688ffcd467d2eb2146a9ce0343404581d
%global git_commit_short %(c="%{git_commit}"; echo "${c:0:8}")

Version: 163840
Release: 14.%{git_date}git%{git_commit_short}%{?dist}

URL: https://www.hanyang.co.kr/hygothic/

%global foundry  HanYang
%global fontlicense  OFL-1.1
%global fontlicenses  OFL.txt

%global fontfamily  Gothic A1
%global fontsummary  HanYang Gothic A1, an elegant Korean and Latin font

%global fontdescription  %{expand:HanYang I&C Co's Gothic A1 is an elegant font for Korean and Latin text,
available in 9 weights.}

%global fonts  *.ttf
%global fontconfs  %{SOURCE10}


# Archive created by running the gothicA1-fetch.sh script (see Source99)
%global archivename HanYang-GothicA1-%{git_commit}
Source0: %{archivename}.zip

Source10: 60-%{fontpkgname}.xml

# A script to fetch the font files from Google Fonts repo on GitHub
Source99: gothicA1-fetch.sh


%fontpkg


%prep
%setup -q -n %{archivename}


%build
%fontbuild


%install
%fontinstall


%check
%fontcheck


%fontfiles


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 163840-14.20180313git16680f86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 163840-13.20180313git16680f86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 163840-12.20180313git16680f86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 163840-11.20180313git16680f86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 163840-10.20180313git16680f86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 19 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 163840-9.20180313git16680f86
- Convert License tag to SPDX

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 163840-8.20180313git16680f86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 163840-7.20180313git16680f86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 163840-6.20180313git16680f86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 163840-5.20180313git16680f86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 163840-4.20180313git16680f86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 163840-3.20180313git16680f86
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Artur Iwicki <fedora@svgames.pl> - 163840-2.20180313git16680f86
- Add a basic fontconfig file

* Fri May 15 2020 Artur Iwicki <fedora@svgames.pl> - 163840-1.20180313git16680f86
- Initial packaging
