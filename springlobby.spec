Name:           springlobby
Version:        0.273
Release:        %autorelease
Summary:        Free cross-platform lobby client for the Spring RTS project

# License clarification: http://springlobby.info/issues/show/810
License:        GPLv2
URL:            https://springlobby.springrts.com/
Source0:        https://springlobby.springrts.com/dl/stable/springlobby-%{version}.tar.bz2
ExclusiveArch:  %{ix86} x86_64

BuildRequires:  alure-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dumb-devel
BuildRequires:  gcc-c++ >= 8
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  libcurl-devel
BuildRequires:  libnotify-devel
BuildRequires:  minizip-compat-devel
BuildRequires:  ninja-build
BuildRequires:  openal-devel
BuildRequires:  rb_libtorrent-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_sound-devel
BuildRequires:  SDL-devel
BuildRequires:  wxGTK-devel

# https://github.com/springlobby/springlobby/issues/709
BuildRequires:  jsoncpp-devel

Requires:       hicolor-icon-theme
Requires:       mesa-libGLU%{?_isa}

Recommends:     fluidsynth-libs%{?_isa}
Recommends:     spring%{?_isa}

# There are other "lobbies" for spring, make a virtual-provides
Provides:       spring-lobby = %{version}-%{release}

%description
SpringLobby is a free cross-platform lobby client for the Spring RTS project.


%prep
%autosetup -p1

# Unbunle libs
rm -rf \
    src/downloader/lib/src/lib/minizip


%build
%cmake \
    -B $PWD/%{_vpath_builddir} \
    -G Ninja


%install
%ninja_install -C %{_vpath_builddir}
%find_lang %{name}
rm -rf %{buildroot}%{_docdir}/%{name}/COPYING


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_docdir}/%{name}/
%{_metainfodir}/*.xml


%changelog
%autochangelog
