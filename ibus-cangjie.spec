%global module_name ibus_cangjie
%global forgeurl https://github.com/Cangjians/ibus-cangjie
%global archiveext tar.xz

Name:             ibus-cangjie
Summary:          IBus engine to input Cangjie and Quick
Version:          2.4
Release:          %autorelease

%forgemeta

License:          GPL-3.0-or-later
URL:              http://cangjians.github.io/projects/%{name}
Source0:          https://github.com/Cangjians/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Patches from upstream to require specific versions of imports
Patch0:           0001-Properly-import-gi-modules-to-avoid-PyGIWarning.patch
Patch1:           0001-src-setup.py-Require-correct-Gio-and-GLib-version.patch
# Extra patch not yet in upstream to fix a crash in the setup tool,
# this patch needs the two patches from  upstream as well to fix the crash,
# it will not work on its own.
# Upstream pull request for this patch: https://github.com/Cangjians/ibus-cangjie/pull/100
Patch2:           fix-crash-in-setup-tool.patch

BuildArch:        noarch

BuildRequires:    desktop-file-utils
BuildRequires:    gcc
BuildRequires:    ibus-devel
BuildRequires:    intltool
BuildRequires:    python3-devel
BuildRequires:    autoconf, automake

# For the unit tests
BuildRequires:    gobject-introspection
BuildRequires:    gtk3
BuildRequires:    python3-cangjie >= 1.2
BuildRequires:    python3-gobject
BuildRequires: make

Requires:         gobject-introspection
Requires:         gtk3
Requires:         python3-canberra
Requires:         python3-cangjie >= 1.2
Requires:         python3-gobject

%description
Common files needed by the IBus engines for users of the Cangjie and Quick
input methods.


%package engine-cangjie
Summary:          Cangjie input method for IBus
Requires:         %{name} = %{version}-%{release}

%description engine-cangjie
IBus engine for users of the Cangjie input method.

It is primarily intended to Hong Kong people who want to input Traditional
Chinese, as they are (by far) the majority of Cangjie users.

However, it should work for others as well (e.g to input Simplified Chinese).


%package engine-quick
Summary:          Quick (Simplified Cangjie) input method for IBus
Requires:         %{name} = %{version}-%{release}

%description engine-quick
IBus engine for users of the Quick (Simplified Cangjie) input method.

It is primarily intended to Hong Kong people who want to input Traditional
Chinese, as they are (by far) the majority of Quick users.

However, it should work for others as well (e.g to input Simplified Chinese).


%prep
%autosetup -p1 -n %{name}-%{version}


%build
autoreconf -fiv
%configure
make %{?_smp_mflags}


%install
%make_install

%find_lang %{name}


%check
make check

# Upstream doesn't validate their desktop files
desktop-file-validate %{buildroot}/%{_datadir}/applications/ibus-setup-cangjie.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/ibus-setup-quick.desktop


%files -f %{name}.lang
%doc AUTHORS README.md
%license COPYING
%{_bindir}/ibus-setup-cangjie
%{python3_sitelib}/%{module_name}
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.cangjians.ibus.*.gschema.xml
%{_datadir}/icons/hicolor/*/intl/*

# Using %%{_prefix}/lib is allowed here because the package is exempt from
# multilib (because it is noarch), see:
#     https://fedoraproject.org/wiki/Packaging:Guidelines#Multilib_Exempt_Locations
%{_prefix}/lib/%{name}

%files engine-cangjie
%{_datadir}/applications/ibus-setup-cangjie.desktop
%{_datadir}/appdata/cangjie.appdata.xml
%{_datadir}/ibus/component/cangjie.xml

%files engine-quick
%{_datadir}/applications/ibus-setup-quick.desktop
%{_datadir}/appdata/quick.appdata.xml
%{_datadir}/ibus/component/quick.xml


%changelog
%autochangelog
