Name: pipewalker
Summary: Puzzle game about connecting components into a single circuit
License: GPLv3+

Version: 0.9.4
Release: 6%{?dist}

URL: http://pipewalker.sourceforge.net
Source0: https://downloads.sourceforge.net/project/pipewalker/pipewalker/%{version}/pipewalker-%{version}.tar.gz
Source1: %{name}.metainfo.xml

Patch0: %{name}--format-security.patch

BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libappstream-glib
BuildRequires: make

BuildRequires: libGL-devel
BuildRequires: libpng-devel
BuildRequires: SDL-devel

%description
PipeWalker is a puzzle game in which you need to combine the components
into a single circuit: connect all computers to a network server,
bring water to the taps, etc.


%prep
%autosetup -p1

# Fix violation of Icon Theme Specification
sed -e 's/^Icon=pipewalker\.xpm$/Icon=pipewalker/' -i extra/%{name}.desktop


%build
%configure
%make_build


%install
%make_install

install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 -p %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

# Not used in Fedora
rm -rf %{buildroot}%{_datadir}/menu


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%files
%license COPYING
%doc %{_datadir}/doc/%{name}

%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_metainfodir}/%{name}.metainfo.xml


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 24 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.4-2
- Add a metainfo file
- Fix error in desktop file

* Fri Nov 19 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.9.4-1
- Initial packaging
