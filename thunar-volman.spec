# review at https://bugzilla.redhat.com/show_bug.cgi?id=229930
%global xfceversion 4.18
%global _hardened_build 1
%global debug_package %{nil}

Name:           thunar-volman
Version:        4.18.0
Release:        %autorelease
Summary:        Automatic management of removable drives and media for Thunar
License:        GPLv2+
URL:            http://goodies.xfce.org/projects/thunar-plugins/%{name}
#VCS: git:git://git.xfce.org/xfce/thunar-volman
Source0:        http://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  exo-devel >= 0.6.0
BuildRequires:  xfconf >= %{xfceversion}
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libgudev1-devel >= 145
BuildRequires:  libnotify-devel >= 0.4.0
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
Requires:       Thunar >= %{xfceversion}

%description
The Thunar Volume Manager is an extension for the Thunar file manager, which 
enables automatic management of removable drives and media. For example, if 
thunar-volman is installed and configured properly, and you plug in your 
digital camera, it will automatically launch your preferred photo application 
and import the new pictures from the camera into your photo collection.


%prep
%setup

sed -i 's/XFCE;//' thunar-volman-settings/thunar-volman-settings.desktop.in.in


%build
%configure
%make_build


%install
%make_install

%find_lang %{name}

desktop-file-install \
%if (0%{?fedora} && 0%{?fedora} < 19) || (0%{?rhel} && 0%{?rhel} < 7)
    --vendor fedora                        \
%endif
    --dir ${RPM_BUILD_ROOT}%{_datadir}/applications         \
    --add-only-show-in=XFCE                                 \
    --delete-original                                       \
    ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}-settings.desktop


%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS THANKS
%license COPYING
%{_bindir}/thunar-volman
%{_bindir}/thunar-volman-settings
%{_datadir}/icons/*/*/*/*
%{_datadir}/applications/*thunar-volman-settings.desktop


%changelog
%autochangelog
