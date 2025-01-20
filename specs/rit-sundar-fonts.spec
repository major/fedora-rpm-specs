# SPDX-License-Identifier: MIT
Version:    2.3.1
Release:    2%{?dist}
URL:        https://gitlab.com/rit-fonts/Sundar

%global foundry RIT
%global fontlicense OFL-1.1-RFN
%global fontlicenses fonts/LICENSE.txt
%global fontdocs fonts/*.md

%global fontfamily RIT Sundar
%global fontsource Sundar
%global fontsummary    A traditional orthography display font for Malayalam script

%global fonts fonts/otf/*.otf
%global fontconfs %{nil}

%global fontappstreams fonts/in.org.rachana.rit-sundar.metainfo.xml

%global fontdescription %{expand:
‘RIT Sundar’ is a traditional orthography display font for Malayalam script.\
This font is created, named and released in memory of Sundar (Sundar Ramanatha\
Iyer; April 23, 1953 -- November 12, 2016).
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
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Aug 25 2024 Rajeesh K V <rajeeshknambiar@gmail.com> - 2.3.1-1
- New release 2.3.1

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Rajeesh K V <rajeeshknambiar@fedoraproject.org> - 2.3-0
- New upstream version 2.3
- Use prebuilt binary fonts instead of building from source
- Fixes RHBZ #2295562

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 2.2-1
- Address comments at RHBZ#2031375

* Sun Dec 05 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 2.2-0
- Update to new upstream release
- Major improvements to OpenType layoutt rules

* Sun Dec 27 2020 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 2.1.0-0
- Initial packaging
