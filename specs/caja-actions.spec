Summary: Caja extension for customizing the context menu
Name:    caja-actions
Version: 1.28.0
Release: %autorelease
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+

URL: https://github.com/raveit65/%{name}
Source0: https://github.com/raveit65/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires: caja-devel
BuildRequires: dblatex
BuildRequires: desktop-file-utils
BuildRequires: libgtop2-devel
BuildRequires: libSM-devel
BuildRequires: libuuid-devel
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: yelp-tools

Requires:       %{name}-doc = %{version}-%{release}


%description
Caja actions is an extension for Caja, the MATE file manager.
It provides an easy way to configure programs to be launch on files 
selected in Caja interface

%package doc
Summary: Documentations for %{name}
BuildArch: noarch

%description doc
This package contains the documentation for %{name}

%package devel
Summary: Development tools for the caja-actions
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains headers and shared libraries needed for development
with caja-actions.

%prep
%autosetup -p1

%build
%configure \
    --disable-gtk-doc \
    --enable-html-manuals \
    --enable-pdf-manuals \
    --enable-deprecated

make %{?_smp_mflags} V=1

%install
%{make_install}

find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name "*.a" -exec rm -f {} ';'

# clean docs dirs
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/INSTALL
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/ChangeLog-2008
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/ChangeLog-2009
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/ChangeLog-2010
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/ChangeLog-2011
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/ChangeLog-2012
rm -f $RPM_BUILD_ROOT%{_docdir}/%{name}/MAINTAINERS

%find_lang %{name} --with-gnome --all-name


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/cact.desktop


%ldconfig_scriptlets


%files
%doc AUTHORS COPYING COPYING-DOCS ChangeLog NEWS README
%{_bindir}/caja-actions-run
%{_bindir}/caja-actions-config-tool
%{_bindir}/caja-actions-new
%{_bindir}/caja-actions-print
%{_libexecdir}/caja-actions/
%{_libdir}/caja-actions/
%{_libdir}/caja/extensions-2.0/libcaja-actions-menu.so
%{_libdir}/caja/extensions-2.0/libcaja-actions-tracker.so
%{_datadir}/caja-actions/
%{_datadir}/icons/hicolor/*/apps/caja-actions.*
%{_datadir}/applications/cact.desktop

%files doc -f %{name}.lang
%{_docdir}/caja-actions/html/
%{_docdir}/caja-actions/pdf/
%{_docdir}/caja-actions/objects-hierarchy.odg

%files devel
%{_includedir}/caja-actions/


%changelog
%autochangelog
