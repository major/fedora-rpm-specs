# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173668

%global minorversion 1.3
%global xfceversion 4.16

Name:           xfce4-systemload-plugin
Version:        1.3.3
Release:        %autorelease
Summary:        Systemload monitor for the Xfce panel

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-systemload-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

%if 0%{?fedora} >= 39
ExcludeArch:    %{ix86}
%endif



BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  upower-devel
BuildRequires:  gettext
BuildRequires:  intltool

Requires:       xfce4-panel >= %{xfceversion}

%description
A system-load monitor plugin for the Xfce panel. It displays the current CPU 
load, the memory in use, the swap space and the system uptime.


%prep
%setup -q


%build
%configure --disable-static
%make_build


%install
%make_install

# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# FIXME: make sure debuginfo is generated properly (#795107)
chmod -c +x %{buildroot}%{_libdir}/xfce4/panel/plugins/*.so

%find_lang %{name}


%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.panel.systemload.*

%changelog
%autochangelog
