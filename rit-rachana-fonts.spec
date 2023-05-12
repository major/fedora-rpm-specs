# SPDX-License-Identifier: MIT
Version:    1.4.3
Release:    1%{?dist}
URL:        https://gitlab.com/rit-fonts/%{fontsource}

%global foundry RIT
%global fontlicense OFL-1.1
%global fontlicenses LICENSE.txt
%global fontdocs *.md

%global fontfamily RIT Rachana
%global fontsource RIT-Rachana
%global fontsummary    OpenType font for Malayalam traditional script

%global fonts fonts/otf/*.otf
%global fontconfs meta/65-0-rit-rachana-fonts.conf

%global fontappstreams meta/in.org.rachana.rit-rachana.metainfo.xml

%global fontdescription %{expand:
RIT Rachana is opetype font for Malayalam traditional script designed by Hussain K H.
It covers Unicode 13.0 and entire character set in 'definitive character set' of Malayalam. 
}


Source0:    https://gitlab.com/rit-fonts/RIT-Rachana/-/archive/%{version}/%{fontsource}-%{version}.tar.bz2

BuildRequires:    fontforge
BuildRequires:    python3
BuildRequires:    python3-fonttools
BuildRequires:    python3-cffsubr
BuildRequires:    make
Obsoletes:   smc-rachana-fonts <= 7.0.3

%fontpkg

%prep
%setup -n RIT-Rachana-%{version}

%build
%fontbuild
make otf

%install
%fontinstall

%check
%fontcheck

%fontfiles


%changelog
* Wed May 10 2023 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.4.3-1
- Bugfix update, version 1.4.3

* Sat Feb 18 2023 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.4.2-1
- Bugfix update, version 1.4.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov 27 2022 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.4.1-1
- New version with many improvements (Unicode 15.0, size reduction, shaping...)
- Spec update for SPDX license tag

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 06 2022 Rajeesh K V <rajeeshknambiar@gmail.com> - 1.3.1-1
- New bugfix release 1.3.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.3-2
- Address review comments on RHBZ#2031365

* Mon Dec 06 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.3-1
- Obsoletes SMC Rachana fonts

* Sun Oct 10 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.3-0
- New upstream release 1.3

* Fri Jun 25 2021 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.2-0
- New upstream release 1.2

* Thu Dec 17 2020 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 1.1-0
- Initial packaging
