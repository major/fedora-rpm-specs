# SPDX-License-Identifier: MIT
Version:    2.2
Release:    6%{?dist}
URL:        https://gitlab.com/rit-fonts/Sundar

%global foundry RIT
%global fontlicense OFL
%global fontlicenses LICENSE.txt
%global fontdocs README.md

%global fontfamily RIT Sundar
%global fontsummary    A traditional orthography display font for Malayalam script

%global fonts fonts/otf/*.otf
%global fontconfs %{nil}

%global fontappstreams in.org.rachana.rit-sundar.metainfo.xml

%global fontdescription %{expand:
‘RIT Sundar’ is a traditional orthography display font for Malayalam script.\
This font is created, named and released in memory of Sundar (Sundar Ramanatha\
Iyer; April 23, 1953 -- November 12, 2016).
}


Source0:    https://gitlab.com/rit-fonts/Sundar/-/archive/%{version}/Sundar-%{version}.tar.bz2

BuildRequires:    fontforge
BuildRequires:    python3
BuildRequires:    python3-fonttools
BuildRequires:    python3-cffsubr
BuildRequires:    make

%fontpkg

%prep
%setup -n Sundar-%{version}

%build
%fontbuild
make otf

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
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
