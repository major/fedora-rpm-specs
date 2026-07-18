# INFO: Package contains data-only, no binaries, so no debuginfo is needed
%global debug_package %{nil}

# Installed destination is now xkeyboard-config-2, but upstream package
# name is the same
%global pkgconfig_name xkeyboard-config-2

#global gitdate 20110415
#global gitversion 19a0026b5

Summary:    X Keyboard Extension configuration data
Name:       xkeyboard-config
Version:    2.48
Release:    %autorelease
License:    HPND AND HPND-sell-variant AND X11 AND X11-distribute-modifications-variant AND MIT AND MIT-open-group AND xkeyboard-config-Zinoviev
URL:        http://www.freedesktop.org/wiki/Software/XKeyboardConfig

%if 0%{?gitdate}
Source0:    %{name}-%{gitdate}.tar.bz2
Source1:    make-git-snapshot.sh
Source2:    commitid
%else
Source0:    https://xorg.freedesktop.org/archive/individual/data/%{name}/%{name}-%{version}.tar.xz
Source1:    https://xorg.freedesktop.org/archive/individual/data/%{name}/%{name}-%{version}.tar.xz.sig
Source3:    SergeyUdaltsov-C933A145.gpg
%endif

BuildArch:  noarch

BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  git-core
BuildRequires:  gnupg2
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(x11) >= 1.4.3
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildRequires:  pkgconfig(xproto) >= 7.0.20
BuildRequires:  python3-pytest
BuildRequires:  xkbcomp

%description
This package contains configuration data used by the X Keyboard Extension (XKB),
which allows selection of keyboard layouts when using a graphical interface.

%package devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   pkgconfig

%description devel
Development files for %{name}.

%prep
%if ! 0%{?gitdate}
gpgv2 --keyring %{SOURCE3} %{SOURCE1} %{SOURCE0}
%endif
%autosetup -S git

%build
%meson -Dcompat-rules=true -Dxorg-rules-symlinks=true
%meson_build

%install
%meson_install

# Replace with relative symlink
rm $RPM_BUILD_ROOT%{_datadir}/X11/xkb
ln -srf $RPM_BUILD_ROOT%{_datadir}/%{pkgconfig_name} $RPM_BUILD_ROOT%{_datadir}/X11/xkb

%find_lang %{pkgconfig_name}
%find_lang %{name}

%check
%meson_test

# Note: 2.45 changed the install location from the decades-old /usr/share/X11/xkb
# to a package-specific /usr/share/xkeyboard-config-2. Upstream installs a symlink
# for /usr/share/X11/xkb since those two dirctories are guaranteed to be the same.
#
# The "official" script [1] is buggy if an .rpmmoved directory already exists so
# this is an approximation taken from OpenSuSE [2]
# [1] https://fedoraproject.org/wiki/Packaging:Directory_Replacement#Replacing_a_symlink_with_a_directory_or_a_directory_with_any_type_of_file
# [2] https://build.opensuse.org/request/show/1294803
%pretrans -p <lua>
-- Define the path to directory being replaced below.
-- DO NOT add a trailing slash at the end.
local path = "%{_datadir}/X11/xkb"
local st = posix.stat(path)

if st and st.type == "directory" then
  local target = path .. ".rpmmoved"
  local suffix = 1

  while posix.stat(target) do
    suffix = suffix + 1
    target = path .. ".rpmmoved" .. suffix
  end

  os.rename(path, target)
end

%files -f %{pkgconfig_name}.lang -f %{name}.lang
%license COPYING
%doc AUTHORS README.md docs/README.* docs/HOWTO.*
%{_mandir}/man7/%{name}.*
%{_mandir}/man7/%{pkgconfig_name}.*
%{_datadir}/X11/xkb
%{_datadir}/%{pkgconfig_name}/
%ghost %attr(0755, root, root) %dir %{_datadir}/X11/xkb.rpmmoved

%files devel
%{_datadir}/pkgconfig/%{pkgconfig_name}.pc
%{_datadir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
