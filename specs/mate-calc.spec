Name:          mate-calc
Version:       1.28.0
Release:       %autorelease
Summary:       MATE Desktop calculator
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz

# https://github.com/mate-desktop/mate-calc/commit/fe495df
Patch1:        mate-calc_0001-a11y-Allow-the-screen-reader-to-announce-status-chan.patch
# https://github.com/mate-desktop/mate-calc/commit/7ef327f
Patch2:        mate-calc_0002-Fix-invalid-memory-access-with-invalid-powers.patch

BuildRequires: bison
BuildRequires: desktop-file-utils
BuildRequires: flex
BuildRequires: gtk3-devel
BuildRequires: libmpc-devel
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mpfr-devel


%description
mate-calc is a powerful graphical calculator with financial, logical and scientific modes.
It uses a multiple precision package to do its arithmetic to give a high degree of accuracy.

%prep
%autosetup -p1

%build
%configure \
    --disable-schemas-compile

make %{?_smp_mflags} V=1

%install
%{make_install}


desktop-file-install                               \
        --delete-original                          \
        --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name} --with-gnome --all-name


%files -f %{name}.lang
%doc AUTHORS COPYING README.md
%{_mandir}/man1/*
%{_bindir}/mate-calc
%{_bindir}/mate-calc-cmd
%{_bindir}/mate-calculator
%{_datadir}/metainfo/mate-calc.appdata.xml
%{_datadir}/applications/mate-calc.desktop
%{_datadir}/glib-2.0/schemas/org.mate.calc.gschema.xml


%changelog
%autochangelog
