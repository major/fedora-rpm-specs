Name:           blackbox
Version:        0.77
Release:        %autorelease
Summary:        Very small and fast Window Manager
License:        MIT
URL:            https://github.com/bbidulock/blackboxwm
Source0:        https://github.com/bbidulock/blackboxwm/releases/download/%{version}/%{name}-%{version}.tar.lz
Source1:        blackbox.desktop
Source2:        blackbox.session
Patch0:         d3481ee7b7d104ef53ead4d35b9a9254c64bb87a.patch
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
BuildRequires:  libXt-devel
BuildRequires:  lzip
BuildRequires:  make

%description
Blackbox is a window manager for the X Window environment, which is
almost completely compliant with ICCCM specified operation policies.
It features nice and fast interface with multiple workspaces and
simple menus. Fast built-in graphics code that can render solids,
gradients and bevels is used to draw window decorations. Remaining
small in size, blackbox preserves memory and CPU.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libXft-devel%{?_isa}

%description    devel
This package contains the Blackbox Toolbox files, headers and static library
of the utility class library for writing small applications.

%prep
%autosetup -p1
# %%{__global_ldflags} wrongly passed to pkgconfig file
sed -i 's|@LDFLAGS@||g' lib/libbt.pc.in

%build
# Required to cleanly get rid of the useless rpath
sh autogen.sh
autoreconf -fiv
%configure \
    --enable-shared \
    --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete -print

# Install the desktop entry
install -pDm0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/xsessions/blackbox.desktop

# Install GDM session file
install -pDm0755 %{SOURCE2} \
    %{buildroot}%{_sysconfdir}/X11/gdm/Sessions/Blackbox

%find_lang %{name}
%ldconfig_scriptlets

%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS ChangeLog COMPLIANCE NEWS README* RELEASE* THANKS TODO
%license COPYING
%{_sysconfdir}/X11/gdm/Sessions/Blackbox
%{_bindir}/blackbox
%{_bindir}/bsetbg
%{_bindir}/bsetroot
%{_bindir}/bstyleconvert
%{_libdir}/libbt.so.*
%{_datadir}/blackbox/
%{_datadir}/xsessions/blackbox.desktop
%{_mandir}/man1/blackbox.1*
%{_mandir}/man1/bsetbg.1*
%{_mandir}/man1/bsetroot.1*
%{_mandir}/*/man1/blackbox.1*
%{_mandir}/*/man1/bsetroot.1*

%files devel
%{_includedir}/bt/
%{_libdir}/libbt.so
%{_libdir}/pkgconfig/libbt.pc

%changelog
%autochangelog
