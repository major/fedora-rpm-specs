# SPDX-License-Identifier: MIT
Version: 3.2.2
Release: 2
URL:     https://gitlab.com/rit-fonts/rit-%{fontfamily}

%global foundry         RIT
%global fontlicense     OFL-1.1-RFN AND MIT
%global fontlicenses    fonts/LICENSE.txt
%global fontdocs        fonts/*.md

%global fontfamily      keraleeyam
%global fontsummary     Display style traditional script font for Malayalam

%global fonts           fonts/otf/*.otf
%global fontconfs       fonts/75-rit-keraleeyam-fonts.conf

%global fontappstreams  fonts/in.org.rachana.%{fontfamily}.metainfo.xml

%global fontdescription   %{expand:
Keraleeyam is a thick sans-serif display style font in condensed form.
It is widely used for designing book covers and titles.
Conjuncts, especially vertical conjuncts are designed for better balance
among upper and lower characters.
}

Source0:  %{url}/-/jobs/artifacts/%{version}/download?job=build-tag#/rit-%{fontfamily}-%{version}.zip

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
* Sat Jun 21 2025 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 3.2.2-2
- Add MIT license used for AppData file

* Sat Jun 14 2025 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 3.2.2-1
- Update source url based on review feedback

* Sat May 31 2025 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 3.2.2-0
- New upstream version with fontconfig

* Fri May 30 2025 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 3.2.1-0
- Updated for review comments
- Use pre-built fonts

* Sun Jan 07 2024 Rajeesh KV <rajeeshknambiar@fedoraproject.org> - 3.1.0
- Initial packaging
