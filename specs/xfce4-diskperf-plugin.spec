# Review: https://bugzilla.redhat.com/bugzilla/show_bug.cgi?id=173660

%global _hardened_build 1
%global minorversion 2.7
%global xfceversion 4.16

Name:           xfce4-diskperf-plugin
Version:        2.7.1
Release:        %autorelease
Summary:        Disk performance plugin for the Xfce panel

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://goodies.xfce.org/panel-plugins/{%name}
#VCS: git:git://git.xfce.org/panel-plugins/xfce4-diskperf-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/%{minorversion}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  xfce4-panel-devel >= %{xfceversion}
BuildRequires:  gettext
BuildRequires:  intltool
Requires:       xfce4-panel >= %{xfceversion}

%description
The DiskPerf plugin displays disk/partition performance (bytes transfered per
second) based on data provided by the kernel.

%prep
%autosetup

%build
%configure --disable-static
%make_build


%install
%make_install

# remove la file
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang %{name}


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS
%license COPYING
%{_libdir}/xfce4/panel/plugins/*.so
%{_datadir}/xfce4/panel/plugins/*.desktop


%changelog
%autochangelog
