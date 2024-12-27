# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173670

%global minorversion 0.6
%global xfceversion 4.16

Name:           xfce4-wavelan-plugin
Version:        0.6.4
Release:        %autorelease
Summary:        WaveLAN plugin for the Xfce panel

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-wavelan-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  gettext
BuildRequires:  intltool

Requires:       xfce4-panel >= %{xfceversion}

%description
A plugin for the Xfce panel that monitors a wireless LAN interface. It 
displays stats for signal state, signal quality and network name (SSID).

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
%{_libdir}/xfce4/panel/plugins/libwavelan.so
%{_datadir}/xfce4/panel/plugins/*.desktop

%changelog
%autochangelog
