# SPDX-License-Identifier: MIT
Version:    1.5.1
Release:    2%{?dist}
URL:        https://gitlab.com/rit-fonts/%{fontsource}

%global foundry RIT
%global fontlicense OFL-1.1
%global fontlicenses LICENSE.txt
%global fontdocs README.md

%global fontfamily Meera New
%global fontsource MeeraNew
%global fontsummary    OpenType sans-serif font for Malayalam traditional script

%global fonts fonts/otf/*.otf
%global fontconfs meta/65-meera-new-fonts.conf
%global fontappstreams meta/in.org.rachana.meera-new.metainfo.xml

%global fontdescription %{expand:
MeeraNew is a sans-serif font for Malayalam traditional script designed\
by KH Hussain and developed by Rachana Institute of Typography.
}


Source0:    https://gitlab.com/rit-fonts/%{fontsource}/-/archive/%{version}/%{fontsource}-%{version}.tar.bz2

BuildRequires:    fontforge
BuildRequires:    python3
BuildRequires:    python3-fonttools
BuildRequires:    python3-cffsubr
BuildRequires:    make
Obsoletes:   smc-meera-fonts <= 7.0.3-5%{?dist}

%fontpkg

%prep
%setup -n %{fontsource}-%{version}

%build
%fontbuild
make otf

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
* Tue Aug 22 2023 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.5.1-2
- Change fontconfig priority from 67 to 65

* Sun Aug 20 2023 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.5.1-1
- New release, version 1.5.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 27 2022 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.4.1-1
- New version 1.4.1 with many improvements
- SPDX license

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun May 15 2022 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.3-1
- New version improving x-height to match RIT Rachana and many kerning pairs

* Mon Feb 07 2022 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-2
- Fix Obsoletes: smc-meera-fonts

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.2.1-0
- New release
- Address comments at RHBZ#2031370

* Mon Dec 06 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.2-1
- Obsoletes SMC Meera fonts

* Sun Dec 05 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.2-0
- Update to new upstream release
- Major improvements to OpenType layoutt rules

* Fri Jan 01 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.0-0
- Initial packaging
