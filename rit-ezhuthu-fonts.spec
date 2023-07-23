# SPDX-License-Identifier: MIT
Version:    1.3
Release:    5%{?dist}
URL:        https://gitlab.com/rit-fonts/%{fontfamily}

%global foundry RIT
%global fontlicense OFL
%global fontlicenses LICENSE.txt
%global fontdocs README.md Ezhuthu-character-set.pdf

%global fontfamily ezhuthu
%global fontsummary    Open Type script style font for Malayalam traditional script

%global fonts fonts/otf/*.otf
%global fontconfs %{nil}

%global fontappstreams in.org.rachana.ezhuthu.metainfo.xml

%global fontdescription %{expand:
Ezhuthu is a handwriting style font for Malayalam traditional script designed\
by Narayana Bhattathiri and developed by Rachana Institute of Typography.
}


Source0:    https://gitlab.com/rit-fonts/%{fontfamily}/-/archive/%{version}/%{fontfamily}-%{version}.tar.bz2

BuildRequires:    fontforge
BuildRequires:    python3
BuildRequires:    python3-fonttools
BuildRequires:    python3-cffsubr
BuildRequires:    make

%fontpkg

%prep
%setup -n %{fontfamily}-%{version}

%build
%fontbuild
make otf

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
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
