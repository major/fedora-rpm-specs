# SPDX-License-Identifier: MIT
Version:    1.6.2
Release:    2%{?dist}
URL:        https://gitlab.com/rit-fonts/tnjoy

%global foundry         RIT
%global fontlicense     OFL-1.1-RFN
%global fontlicenses    fonts/LICENSE.txt
%global fontdocs        fonts/README.md

%global fontfamily      TN Joy
%global fontsource      tnjoy
%global fontsummary     A traditional orthography font for Malayalam script

%global fonts           fonts/otf/*.otf
%global fontconfs       fonts/67-tn-joy-fonts.conf

%global fontappstreams  fonts/in.org.rachana.tn-joy.metainfo.xml

%global fontdescription %{expand:
TN Joy is a traditional orthography font for Malayalam script designed by\
K.H. Hussain & P.K. Ashok Kumar and developed by Rachana Institute of Typography.\
This font is named after and dedicated to the activist T.N. Joy.
}


# https://gitlab.com/rit-fonts/%%{fontsource}/-/jobs/artifacts/%%{version}/download?job=build-tag
Source0:    %{fontsource}-%{version}.zip

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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Aug 25 2024 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.6.2-1
- New release 1.6.2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 12 2024 Rajeesh KV <rajeeshknambiar@gmail.com> - 1.6.1-1
- Fix name in fontconfig

* Fri Jul 12 2024 Rajeesh KV <rajeeshknambiar@gmail.com> - 1.6.1-0
- Fix name in fontconfig

* Sun Jul 07 2024 Rajeesh K V <rajeeshknambiar@fedoraproject.org> - 1.6-0
- New upstream version 1.6
- Use prebuilt binary fonts instead of building from source
- Fixes RHBZ #2293879

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.4.1-0
- New release
- Address comments in RHBZ#2031377

* Sun Dec 05 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.4-0
- Update to new upstream release
- Major improvements to OpenType layoutt rules

* Fri Jan 01 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.2-0
- Initial packaging
