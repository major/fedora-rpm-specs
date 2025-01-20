# SPDX-License-Identifier: MIT
Version:    1.5.2
Release:    2%{?dist}
URL:        https://gitlab.com/rit-fonts/%{fontfamily}

%global foundry         RIT
%global fontlicense     OFL-1.1-RFN
%global fontlicenses    fonts/LICENSE.txt
%global fontdocs        fonts/README.md fonts/Ezhuthu-character-set.pdf

%global fontfamily      ezhuthu
%global fontsummary     Open Type script style font for Malayalam traditional script

%global fonts           fonts/otf/*.otf
%global fontconfs       %{nil}

%global fontappstreams  fonts/in.org.rachana.ezhuthu.metainfo.xml

%global fontdescription %{expand:
Ezhuthu is a handwriting style font for Malayalam traditional script designed\
by Narayana Bhattathiri and developed by Rachana Institute of Typography.
}

 
# https://gitlab.com/rit-fonts/%%{fontsource}/-/jobs/artifacts/%%{version}/download?job=build-tag
Source0:    %{fontfamily}-%{version}.zip

%fontpkg

%prep
%setup -qc

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Aug 25 2024 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.5.2-1
- New release 1.5.2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 12 2024 Rajeesh KV <rajeeshknambiar@gmail.com> - 1.5.1-0
- Fix name in fontconfig

* Sun Jul 07 2024 Rajeesh K V <rajeeshknambiar@fedoraproject.org> - 1.5.0-0
- New upstream version 1.5.0
- Use prebuilt binary fonts instead of building from source
- Fixes RHBZ #2296161

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 28 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.3-1
- Address comments in RHBZ#2031373

* Sun Dec 05 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.3-0
- Update to new upstream release
- Major improvements to OpenType layoutt rules

* Sun Dec 27 2020 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.2-0
- Initial packaging
