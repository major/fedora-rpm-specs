Name:           Maelstrom
Version:        4.0.2
Release:        %autorelease
Summary:        A space combat game
URL:            http://www.libsdl.org/projects/Maelstrom/

# Maelstrom itself is Zlib.
# rapidxml is BSL or MIT. Even though we unbundle it, it's still a single-header static library.
License:        Zlib AND (BSL-1.0 OR MIT)

Source0:        https://github.com/libsdl-org/Maelstrom/archive/release-%{version}/Maelstrom-release-%{version}.tar.gz

# Even when building against system PhysFS, the vendored PhysFS package
# is required, as it contains some extra PhysFS<->SDL3 glue code.
%global physfs_commit 49cfd5fdd46f38b4c2611556b44ee9b0d308e162
Source1:        https://github.com/icculus/physfs/archive/%{physfs_commit}/physfs-%{physfs_commit}.tar.gz

Source10:        Maelstrom.desktop
Source11:        Maelstrom.appdata.xml

Source20:        Maelstrom-Content-License.txt
Source21:        CC-BY-3.0.txt

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:      cmake
BuildRequires:      desktop-file-utils
BuildRequires:      gcc-c++
BuildRequires:      libappstream-glib

BuildRequires:      cmake(SDL3)
BuildRequires:      cmake(SDL3_net)
BuildRequires:      cmake(PhysFS)
BuildRequires:      rapidxml-devel

Requires:           %{name}-data = %{version}-%{release}

%description
Maelstrom is a space combat game, originally ported from the Macintosh 
platform. Brave pilots get to dodge asteroids and fight off other ships 
at the same time.


%package data
Summary: Data files for Maelstrom
License: CC-BY-3.0
BuildArch: noarch

Requires: hicolor-icon-theme

%description data
This package contains files (graphics, sounds, et cetera)
required to play Maelstrom.


%prep
%autosetup -p1 -n %{name}-release-%{version}
cp -t ./ -a %{SOURCE20} %{SOURCE21}

# Extract PhysFS<->SDL3 glue code from the physfs archive
mkdir -p external/physfs/extras
pushd external/physfs/extras
tar --extract --gunzip --file=%{SOURCE1} --strip-components=2 -- physfs-%{physfs_commit}/extras/physfssdl3.{c,h}
popd

# Unbundle rapidxml
rm utils/rapidxml.{h,hpp}
ln -s %{_includedir}/rapidxml.h utils/
sed '/utils\/rapidxml\.hpp/d' -i CMakeLists.txt


%build
%cmake \
	-DUSE_VENDORED_PHYSFS=FALSE \
	-DUSE_VENDORED_SDL=FALSE \
	-DUSE_VENDORED_SDL_NET=FALSE \
	-DSTEAM=OFF \
	-DSTANDALONE_INSTALL=OFF
%cmake_build


%install
%cmake_install

# Reuse icons from game data
for SIZE in 16 20 24 32 36 40 48 64 72 96 128 192 256 512 1024; do
	ICONDIR="%{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps/"
	install -m 755 -d "${ICONDIR}"
	ln "%{buildroot}/%{_datadir}/%{name}/Data/Icons/icon-${SIZE}.png" "${ICONDIR}/%{name}.png"
done

# Install a desktop file and metainfo file
install -m 755 -d %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE10} %{buildroot}%{_datadir}/applications/%{name}.desktop

install -m 755 -d %{buildroot}%{_metainfodir}
install -m 644 %{SOURCE11} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

# Remove pre-installed documentation files and install them on our own.
# This is done so the docs are in Maelstrom/ dir despite being in Maelstrom-data package.
rm %{buildroot}%{_pkgdocdir}/COPYING
install -m 755 -d %{buildroot}%{_pkgdocdir}
cp -t %{buildroot}%{_pkgdocdir} -a CREDITS README.md Docs

# Remove Steam-specific files
rm -rf %{buildroot}%{_datadir}/%{name}/Data/Steam


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml


%files
%license COPYING
%{_bindir}/Maelstrom
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/Maelstrom.metainfo.xml


%files data
%doc %{_docdir}
%license Maelstrom-Content-License.txt CC-BY-3.0.txt
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
%autochangelog
