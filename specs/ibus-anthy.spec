%global source_version %%(echo "%version" | tr '~' '-')

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%global sub_version                     1.0
%global require_ibus_version            1.5.3
%global with_python3                    1

%if (0%{?fedora} > 33 || 0%{?rhel} > 8)
%bcond_without kasumi_unicode
%else
%bcond_with    kasumi_unicode
%endif

%if %with_python3
# for bytecompile in %%{_datadir}/ibus-anthy
%global __python %{__python3}
%endif

Name:           ibus-anthy
Version:        1.5.19~alpha4
Release:        %autorelease
Summary:        The Anthy engine for IBus input platform
License:        GPL-2.0-or-later
URL:            https://github.com/ibus/ibus/wiki
Source0:        https://github.com/ibus/%{name}/releases/download/%{source_version}/%{name}-%{source_version}.tar.xz
Source1:        https://github.com/ibus/%{name}/releases/download/%{source_version}/%{name}-%{source_version}.tar.xz.sha256sum#/%{name}.tar.xz.sha256sum

# Upstreamed patches.
# Patch0:         %%{name}-HEAD.patch
Patch1:         %{name}-1938129-default-hiragana.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  git
# %%check requires gtk3, ibus-daemon, ps besides ibus-libs
BuildRequires:  gtk3
BuildRequires:  ibus
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  procps-ng
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  pkgconfig(anthy-unicode)
BuildRequires:  pkgconfig(glib-2.0)
# gtk4 and pango requires gobject-introspection-devel
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  /usr/bin/appstream-util

Requires:       ibus >= %{require_ibus_version}
%if %{with kasumi_unicode}
Requires:       kasumi-unicode
%else
Requires:       kasumi
%endif
Requires:       anthy-unicode
Requires:       %{name}-python = %{version}-%{release}

%description
The Anthy engine for IBus platform. It provides Japanese input method from
a library of the Anthy.

%package python
Summary:        Anthy Python files for IBus
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gtk3
Requires:       python3-cairo
Requires:       python3-gobject

%description python
This package contains the Anthy Python files for IBus

%package devel
Summary:        Development tools for IBus
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glib2-devel
Requires:       anthy-unicode-devel

%description devel
The ibus-anthy-devel package contains .so file and .gir files
for developers.

%package  tests
Summary:        Tests for the %{name} package
BuildRequires:  python3-pycotap
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-pycotap

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.


%prep
SAVED_SUM=$(cat %SOURCE1 | awk '{print $1}')
MY_SUM=$(sha256sum %SOURCE0 | awk '{print $1}')
if test x"$SAVED_SUM" != x"$MY_SUM" ; then
    abort
fi
%autosetup -S git -n %{name}-%{source_version}

%build
%meson \
%if %{with kasumi_unicode}
  -Dkasumi-exec=/usr/bin/kasumi-unicode \
%endif
  -Don-off-keys="[ 'Zenkaku_Hankaku', 'Ctrl+space', 'Ctrl+J' ]" \
  -Dinstall-tests=true \
   %{nil}

%meson_build
rm -f $RPM_BUILD_ROOT%{_libdir}/libanthygobject-%{sub_version}.la

%meson_install

rm $RPM_BUILD_ROOT%{_datadir}/ibus-anthy/icons/ibus-anthy.png

%find_lang %{name}

%check
desktop-file-validate \
    $RPM_BUILD_ROOT%{_datadir}/applications/ibus-setup-anthy.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.xml
export LANG=C.UTF-8
locale
%meson_test

%ldconfig_scriptlets libs


%files -f %{name}.lang
%doc AUTHORS COPYING README
# dir {python2_sitearch}/ibus
%{_libdir}/libanthygobject-%{sub_version}.so.*
%{_libdir}/girepository-1.0/Anthy*.typelib
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.anthy.gschema.xml
%dir %{_datadir}/ibus-anthy
%{_datadir}/applications/ibus-setup-anthy.desktop
%{_datadir}/ibus-anthy/dicts
%{_datadir}/icons/hicolor/scalable/apps/ibus-anthy.svg 

%files python
%{_libexecdir}/ibus-*-anthy
%{_datadir}/ibus-anthy/engine
%{_datadir}/ibus-anthy/setup
%{_datadir}/ibus/component/*
%{_metainfodir}/*.xml

%files devel
%{_datadir}/gir-1.0/Anthy*.gir
%{_includedir}/ibus-anthy-%{sub_version}
%{_libdir}/libanthygobject-%{sub_version}.so

%files tests
%dir %{_libexecdir}/installed-tests
%{_libexecdir}/installed-tests/%{name}
%dir %{_datadir}/installed-tests
%{_datadir}/installed-tests/%{name}

%changelog
%autochangelog
