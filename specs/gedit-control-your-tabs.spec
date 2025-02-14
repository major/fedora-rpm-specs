# https://github.com/jefferyto/gedit-control-your-tabs/issues/21
%global debug_package %{nil}

%global appname controlyourtabs
%global uuid    com.thingsthemselves.gedit.plugins.%{appname}

Name:           gedit-control-your-tabs
Version:        0.5.1
Release:        %autorelease
Summary:        Gedit plugin to switch between document tabs using

License:        GPL-2.0-or-later
URL:            https://github.com/jefferyto/gedit-control-your-tabs
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  libappstream-glib
BuildRequires:  python3-devel

Requires:       gedit >= 3.12

Provides:       bundled(python-gtk-utils) = 0.2.0

%description
A gedit plugin to switch between document tabs using Ctrl+Tab / Ctrl+Shift+Tab
(most recently used order or tab row order) and Ctrl+PageUp / Ctrl+PageDown (tab
row order).


%prep
%autosetup -p1


%install
mkdir -p                %{buildroot}%{_libdir}/gedit/plugins
cp -a %{appname}        %{buildroot}%{_libdir}/gedit/plugins/
rm -r                   %{buildroot}%{_libdir}/gedit/plugins/%{appname}/schemas
rm -r                   %{buildroot}%{_libdir}/gedit/plugins/%{appname}/utils/.editorconfig
rm -r                   %{buildroot}%{_libdir}/gedit/plugins/%{appname}/utils/.gitattributes
rm -r                   %{buildroot}%{_libdir}/gedit/plugins/%{appname}/locale
mkdir -p                %{buildroot}%{_libdir}/gedit/plugins
cp -a %{appname}.plugin %{buildroot}%{_libdir}/gedit/plugins/
mkdir -p                %{buildroot}%{_datadir}/glib-2.0/schemas/
cp -a %{appname}/schemas/%{uuid}.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/

# Byte compiling
%py_byte_compile %{__python3} %{buildroot}%{_libdir}/gedit/plugins/%{appname}/

# Install metainfo
install -m 0644 -Dp data/%{uuid}.metainfo.xml %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%license LICENSE
%doc README.md
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_libdir}/gedit/plugins/%{appname}
%{_libdir}/gedit/plugins/%{appname}.plugin
%{_metainfodir}/*.xml


%changelog
%autochangelog
