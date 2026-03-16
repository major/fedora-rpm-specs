# Review at https://bugzilla.redhat.com/show_bug.cgi?id=351531

%global majorversion 0.14
%global xfceversion 4.18


Name:           ristretto
Version:        0.14.0
Release:        %autorelease
Summary:        Image-viewer for the Xfce desktop environment
Summary(de):    Bildbetrachter für die Xfce Desktop-Umgebung

License:        GPL-2.0-or-later
URL:            https://docs.xfce.org/apps/ristretto/start
Source0:        https://archive.xfce.org/src/apps/%{name}/%{majorversion}/%{name}-%{version}.tar.xz
#VCS: git:git://git.xfce.org/apps/ristretto

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel >= 2.56.0
BuildRequires:  gtk3-devel >= 3.22.0
BuildRequires:  exo-devel >= 4.16.0
BuildRequires:  libexif-devel >= 0.6.0
BuildRequires:  libxfce4ui-devel >= %{xfceversion}
BuildRequires:  libxfce4util-devel >= %{xfceversion}
BuildRequires:  xfconf-devel >= %{xfceversion}
BuildRequires:  desktop-file-utils
BuildRequires:  appstream
BuildRequires:  file-devel
Requires:       tumbler


%description
Ristretto is a fast and lightweight image-viewer for the Xfce desktop 
environment.

%description -l de
Ristretto ist ein schneller und leichtgewichtiger Bildbetrachter für die Xfce
Desktop-Umgebung.


%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

# Add missing MIME types to the desktop file
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        --add-mime-type=image/x-bmp \
        --add-mime-type=image/x-png \
        --add-mime-type=image/x-pcx \
        --add-mime-type=image/x-tga \
        --add-mime-type=image/xpm \
        --delete-original \
        %{buildroot}%{_datadir}/applications/org.xfce.%{name}.desktop

# Validate AppData file
appstreamcli validate --no-net %{buildroot}%{_metainfodir}/*.appdata.xml

# Fix Armenian locale directory name (hye -> hy)
if [ -d %{buildroot}%{_datadir}/locale/hye ]; then
    mv %{buildroot}%{_datadir}/locale/hye %{buildroot}%{_datadir}/locale/hy
fi

%find_lang %{name}

%check
# No upstream tests are currently available

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/%{name}
%{_datadir}/applications/org.xfce.%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_metainfodir}/org.xfce.%{name}.appdata.xml

%changelog
%autochangelog
