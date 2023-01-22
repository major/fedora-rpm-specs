# SPDX-License-Identifier: MIT
Version:    1.2
Release:    4%{?dist}
URL:        https://gitlab.com/rit-fonts/%{fontfamily}

%global foundry RIT
%global fontlicense OFL
%global fontlicenses LICENSE.txt
%global fontdocs README.md

%global fontfamily panmana
%global fontsource Panmana
%global fontsummary    Open Type body text font for Malayalam traditional script

%global fonts fonts/otf/*.otf
%global fontconfs %{nil}

%global fontappstreams in.org.rachana.panmana.metainfo.xml

%global fontdescription %{expand:
Panmana is a body text font for Malayalam traditional script designed\
by KH Hussain and developed by Rachana Institute of Typography.\
The font is named after and dedicated to Prof. Panmana Ramachandran Nair.
}


Source0:    https://gitlab.com/rit-fonts/%{fontsource}/-/archive/%{version}/%{fontsource}-%{version}.tar.bz2

BuildRequires:    fontforge
BuildRequires:    python3
BuildRequires:    python3-fonttools
BuildRequires:    python3-cffsubr
BuildRequires:    make

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
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 28 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.2.1
- Address comments in RHBZ#2031374

* Sun Dec 05 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.2-0
- Update to new upstream release
- Major improvements to OpenType layoutt rules

* Fri Jan 01 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.0-0
- Initial packaging
