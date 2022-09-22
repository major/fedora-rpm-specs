%bcond_with         clatexmath

%global forgeurl    https://github.com/blackhole89/notekit/

%global uuid        com.github.blackhole89.notekit

Name:       notekit
Version:    0.1
Release:    9%{?dist}
Summary:    Hierarchical markdown notetaking application with tablet support

%global commit      66a31147f83b93542f0c53f0eda65b1576bc4756
%forgemeta

# The app is under the GPLv3+ license while the fonts are under the Charter
# license.
License:    GPLv3+ and Charter
URL:        %{forgeurl}
Source0:    %{forgesource}

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
%if %{with clatexmath}
BuildRequires:  cLaTeXMath-devel
%endif
BuildRequires:  gtkmm30-devel
BuildRequires:  gtksourceviewmm3-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  zlib-devel
Requires:       hicolor-icon-theme

%description
This program is a structured notetaking application based on GTK+ 3.
Write your notes in instantly-formatted Markdown, organise them in a
tree of folders that can be instantly navigated from within the program,
and add hand-drawn notes by mouse, touchscreen or digitiser.

%prep
%forgeautosetup

%build
%meson %{!?with_clatexmath:-Dclatexmath=false}

%meson_build

%install
%meson_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml

%files
%doc README.md
%license LICENSE "data/fonts/Charter license.txt"
%{_bindir}/%{name}
%{_metainfodir}/%{uuid}.metainfo.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/icons/hicolor/*/apps/%{uuid}.*
%{_datadir}/%{name}/

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 03 2021 Björn Esser <besser82@fedoraproject.org> - 0.1-7
- Rebuild (jsoncpp)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 18 2021 Lyes Saadi <fedora@lyes.eu> - 0.1-5
- Updating due to the addition of new important features
- 66a31147f83b93542f0c53f0eda65b1576bc4756

* Sat May 08 2021 Lyes Saadi <fedora@lyes.eu> - 0.1-4
- Updating the patch and importing into Fedora

* Wed Apr 21 2021 Lyes Saadi <fedora@lyes.eu> - 0.1-3
- Adding conditional to enable/disable cLaTeXMath
- Disabling cLaTeXMath by default due to licensing issues

* Sun Mar 14 2021 Lyes Saadi <fedora@lyes.eu> - 0.1-2
- Removing the git-core dependency
- Checking for the validity of the Desktop and Metainfo files
- Adding a License breakdown
- Marking the Charter License as a License
- "Unglobing" the icons/hicolor folder

* Tue Jan 12 2021 Lyes Saadi <fedora@lyes.eu> - 0.1-1
- Updating to 0.1

* Wed Nov 18 2020 Lyes Saadi <fedora@lyes.eu> - 0-2
- Updating to latest commit
- Switching to meson
- Enabling cLaTeXMath
- Adding metainfo
- Adding back Charter fonts as I recently learned to read

* Thu Oct 22 2020 Lyes Saadi <fedora@lyes.eu> - 0-1.git5ecb632
- Updating to latest commit
- Replacing the patch by a simple sed

* Tue May 05 2020 Lyes Saadi <fedora@lyes.eu> - master-2
- Updating to latest commit
- Making the spec file compliant to Fedora's Guidelines

* Wed Sep 11 2019 Lyes Saadi <fedora@lyes.eu> - master-1
- Creating the spec file
