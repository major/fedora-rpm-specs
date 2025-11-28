Name: alexvsbus
%global pretty_name Alex vs Bus: The Race

Summary: Help Alex catch the bus on time!
License: GPL-3.0-or-later

Version: 2025.06.16.0
Release: 3%{?dist}

URL: https://github.com/M374LX/alexvsbus
Source0: %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

Source10: alexvsbus.metainfo.xml

# Remove bunbled raylib v5.0 and fix compatibility with raylib v5.5
Patch0: alexvsbus--unbundle-raylib.patch

BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: libappstream-glib
BuildRequires: make

BuildRequires: raylib-devel
BuildRequires: SDL2-devel
BuildRequires: stb_image-devel >= 2.30^20251025gitf1c79c0-2

Requires: %{name}-data = %{version}-%{release}

%description
%{pretty_name} is a free and open source platform runner game in which
a man who depends on public transportation in a developing country needs
to run in order to catch the bus, or else he will have to wait an eternity
for the next bus to come.


%package data
Summary: Data files for %{pretty_name}
License: CC-BY-SA-4.0
BuildArch: noarch

Requires: hicolor-icon-theme

%description data
Data files (graphics, sounds, etc.) required to play %{pretty_name}.


%package doc
Summary: Documentation for %{pretty_name}
License: CC-BY-SA-4.0
BuildArch: noarch

%description doc
User and developer manuals for %{pretty_name}.


%prep
%autosetup -p1
rm -rf raylib/

# Prefer generating a position-independent executable
sed -e 's/ -fPIC / -fPIE -pie /' -i Makefile


%build
%make_build SDL=1


%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 %{name} %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}%{_datadir}/games/
cp -a assets %{buildroot}%{_datadir}/games/%{name}

for ICON_SIZE in 32 128; do
	ICON_DIR="%{buildroot}%{_datadir}/icons/hicolor/${ICON_SIZE}x${ICON_SIZE}/apps"
	install -m 755 -d "${ICON_DIR}"
	install -m 644 "icons/icon${ICON_SIZE}.png" "${ICON_DIR}/%{name}.png"
done

install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 icons/%{name}.desktop %{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 %{SOURCE10} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

install -m 755 -d %{buildroot}%{_docdir}/%{name}
install -m 644 docs/*.md -t %{buildroot}%{_docdir}/%{name}/
cp -a docs/manual %{buildroot}%{_docdir}/%{name}/manual
rm %{buildroot}%{_docdir}/%{name}/manual/manual.pdf


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
%{buildroot}%{_bindir}/%{name} -v


%files
%license LICENSE.txt
%license docs/licenses/GPL-3.0.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/%{name}.metainfo.xml

%files data
%license docs/licenses/CC-BY-SA-4.0.txt
%{_datadir}/games/
%{_datadir}/icons/hicolor/**/apps/%{name}.png

%files doc
%license docs/licenses/CC-BY-SA-4.0.txt
%doc %{_docdir}/%{name}/


%changelog
* Wed Nov 26 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 2025.06.16.0-3
- Rebuilt with latest patched stb_image: memory-safety fixes

* Fri Aug 22 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2025.06.16.0-2
- Move documentation to -doc subpackage
- Remove pre-built .pdf manual from docs

* Tue Jun 17 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2025.06.16.0-1
- Update to v2025.06.16.0

* Mon Jun 16 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2025.06.15.0-1
- Update to v2025.06.15.0

* Sat Mar 29 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2024.11.21.0-2
- Add an AppStream metainfo file
- Include full license text in the packages
- Include documentation in the package

* Wed Feb 05 2025 Artur Frenszek-Iwicki <fedora@svgames.pl> - 2024.11.21.0-1
- Initial packaging
