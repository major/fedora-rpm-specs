# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           goverlay
Version:        1.6.4
Release:        %autorelease
Epoch:          1
Summary:        Graphical interface to configure MangoHud, vkBasalt, and OptiScaler
ExclusiveArch:  %{fpc_arches}

License:        GPL-3.0-or-later
URL:            https://github.com/benjamimgois/goverlay
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Patch:          goverlay-enable-debuginfo-generation.patch

BuildRequires:  desktop-file-utils
BuildRequires:  fpc-srpm-macros
BuildRequires:  lazarus
BuildRequires:  lazarus-lcl-qt6
BuildRequires:  libappstream-glib
BuildRequires:  libglvnd-devel
BuildRequires:  make

Requires:       hicolor-icon-theme
# https://github.com/benjamimgois/goverlay?tab=readme-ov-file#prerequisites
Requires:       mangohud%{?_isa}
Requires:       mesa-libGLU
Requires:       qt6pas%{?_isa}

Recommends:     git%{?_isa}
Recommends:     mesa-demos%{?_isa}
Recommends:     vkBasalt%{?_isa}
Recommends:     vulkan-tools%{?_isa}

%description
Goverlay helps Linux gamers get the most out of their system by offering an easy
graphical interface to configure MangoHud, vkBasalt, and OptiScaler. Whether you
want performance monitoring, visual enhancements, or smarter upscaling, Goverlay
makes everything accessible in just a few clicks.


%prep
%autosetup -p1


%build
%set_build_flags
%make_build


%install
%make_install prefix=%{_prefix}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_libexecdir}/%{name}
%{_mandir}/man1/*.1*
%{_metainfodir}/*.xml


%changelog
%autochangelog
