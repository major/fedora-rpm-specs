%global owner zakariakov
%global commit 93b03026cadd9946f02ba0cecb615714b822cdb5

Name: booksorg
Version: 0.3.1
Release: 13%{?dist}
# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
Summary: Books Organizer
URL: https://github.com/%{owner}/%{name}
Source0: %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildRequires: gcc-c++
BuildRequires: dejavu-serif-fonts
BuildRequires: poppler-qt5-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: desktop-file-utils
BuildRequires: make

Requires: qt5-qtbase

%description
 Books Organizer an organizer for PDF files based on SQLite
 and with a built-in reader.  Bring your favorite PDF pages
 all in one! Make your own extract pages from existing ones.

%prep
%setup -q -n %{name}-%{commit}
%if 0%{?flatpak}
sed -i -e 's|/usr|%{_prefix}|g' booksorganizer.pro
%endif


%build
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/appdata
install -Dp -m 0644 %{name}.appdata.xml %{buildroot}%{_datadir}/appdata
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

#Fix SVG file permissions
chmod 644 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg


%files
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 7 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.1-12
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 23 2020 Mosaab Alzoubi <moceap@hotmail.com> - 0.3.1-3
- Add licence
- Upstream appdata file

* Thu Oct 1 2020 Mosaab Alzoubi <moceap@hotmail.com> - 0.3.1-2
- Review for Fedora Package Review
- Use %%url
- Remove Unneeded lines
- Use only %%buildroot
- Use desktop file validation
- Fix some spellings
- Shorten description lines
- Fix SVG file permissions


* Thu Oct 1 2020 Mosaab Alzoubi <moceap@hotmail.com> - 0.3.1-1
- Updated to 0.3.1
- Built for F33
- Use Qt5

* Mon Mar 27 2017 Mosaab Alzoubi <moceap@hotmail.com> - 0.3-2
- Imported from http://download.opensuse.org/repositories/home:/kovax/CentOS_CentOS-6/src
- Clean the spec
