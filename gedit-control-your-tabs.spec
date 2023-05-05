%global pname   controlyourtabs
%global uuid    com.thingsthemselves.gedit.plugins.%{pname}

Name:           gedit-control-your-tabs
Version:        0.3.5
Release:        %autorelease
Summary:        Gedit plugin to switch between document tabs using

License:        GPLv3+
URL:            https://github.com/jefferyto/gedit-control-your-tabs
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  libappstream-glib
BuildRequires:  python3-devel

Requires:       gedit%{?_isa} >= 3.8

Provides:       bundled(python-gtk-utils) = 0.2.0

%description
A gedit plugin to switch between document tabs using Ctrl+Tab / Ctrl+Shift+Tab
(most recently used order or tab row order) and Ctrl+PageUp / Ctrl+PageDown (tab
row order).


%prep
%autosetup -p1


%install
mkdir -p                %{buildroot}%{_libdir}/gedit/plugins
cp -a %{pname}          %{buildroot}%{_libdir}/gedit/plugins/
rm -r                   %{buildroot}%{_libdir}/gedit/plugins/%{pname}/schemas
rm -r                   %{buildroot}%{_libdir}/gedit/plugins/%{pname}/utils/.editorconfig
rm -r                   %{buildroot}%{_libdir}/gedit/plugins/%{pname}/utils/.gitattributes
rm -r                   %{buildroot}%{_libdir}/gedit/plugins/%{pname}/locale
mkdir -p                %{buildroot}%{_libdir}/gedit/plugins
cp -a %{pname}.plugin   %{buildroot}%{_libdir}/gedit/plugins/
mkdir -p                %{buildroot}%{_datadir}/glib-2.0/schemas/
cp -a %{pname}/schemas/%{uuid}.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas/

# Byte compiling
%py_byte_compile %{__python3} %{buildroot}%{_libdir}/gedit/plugins/%{pname}/

# Install metainfo
install -m 0644 -Dp data/%{uuid}.metainfo.xml %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml


%files
%license LICENSE
%doc README.md
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_libdir}/gedit/plugins/%{pname}
%{_libdir}/gedit/plugins/%{pname}.plugin
%{_metainfodir}/*.xml


%changelog
%autochangelog
