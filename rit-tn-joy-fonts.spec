# SPDX-License-Identifier: MIT
Version:    1.4.1
Release:    5%{?dist}
URL:        https://gitlab.com/rit-fonts/tnjoy

%global foundry RIT
%global fontlicense OFL
%global fontlicenses LICENSE.txt
%global fontdocs README.md

%global fontfamily TN Joy
%global fontsummary    A traditional orthography font for Malayalam script

%global fonts fonts/otf/*.otf
%global fontconfs meta/67-rit-tn-joy-fonts.conf

%global fontappstreams in.org.rachana.tn-joy.metainfo.xml

%global fontdescription %{expand:
TN Joy is a traditional orthography font for Malayalam script designed by\
K.H. Hussain & P.K. Ashok Kumar and developed by Rachana Institute of Typography.\
This font is named after and dedicated to the activist T.N. Joy.
}


Source0:    https://gitlab.com/rit-fonts/tnjoy/-/archive/%{version}/tnjoy-%{version}.tar.bz2

BuildRequires:    fontforge
BuildRequires:    python3
BuildRequires:    python3-fonttools
BuildRequires:    python3-cffsubr
BuildRequires:    make

%fontpkg

%prep
%setup -n tnjoy-%{version}

%build
%fontbuild
make otf

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
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
