# Review at https://bugzilla.redhat.com/show_bug.cgi?id=549593
# VCS https://gitlab.xfce.org/xfce/tumbler.git

%global xfceversion 4.20

Name:           tumbler
Version:        4.20.2
Release:        %autorelease
Summary:        D-Bus service for applications to request thumbnails

License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            http://git.xfce.org/xfce/tumbler/
Source0:        https://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  gettext
BuildRequires:  glib2-devel >= 2.72.0
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  intltool
BuildRequires:  libcurl-devel
%{?fedora:BuildRequires: libgsf-devel}
BuildRequires:  libjpeg-devel
%{?fedora:BuildRequires: libopenraw-gnome-devel}
BuildRequires:  libpng-devel
BuildRequires:  libxfce4util-devel >= %{xfceversion}
BuildRequires:  make
BuildRequires:  poppler-glib-devel
BuildRequires:  systemd-rpm-macros


%description
Tumbler is a D-Bus service for applications to request thumbnails for various
URI schemes and MIME types. It is an implementation of the thumbnail
management D-Bus specification described on
http://live.gnome.org/ThumbnailerSpec written in an object-oriented fashion

Additional thumbnailers can be found in the tumbler-extras package


%package extras
Summary:       Additional thumbnailers for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description extras
This package contains additional thumbnailers for file types, which are not used
very much and require additional libraries to be installed.


%package devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for developing applications 
that use %{name}.


%prep
%setup -q

%build
%configure --disable-static

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

# Remove rpaths.
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

# fix permissions for installed libs
chmod 755 %{buildroot}%{_libdir}/*.so

find %{buildroot} -type f -name "*.la" -delete

# rename hye (three letter code) to hy (two letter code) for Armenian
if [ -d %{buildroot}%{_datadir}/locale/hye ]; then
    mv %{buildroot}%{_datadir}/locale/hye %{buildroot}%{_datadir}/locale/hy
fi

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS
%config(noreplace) %{_sysconfdir}/xdg/tumbler/
%{_datadir}/dbus-1/services/org.xfce.Tumbler.*.service
%{_libdir}/libtumbler-*.so.*
%dir %{_libdir}/tumbler-1
%dir %{_libdir}/tumbler-1/plugins
%dir %{_libdir}/tumbler-1/plugins/cache
%{_libdir}/tumbler-1/plugins/cache/tumbler-cache-plugin.so
%{_libdir}/tumbler-1/plugins/cache/tumbler-xdg-cache.so
%{_libdir}/tumbler-1/plugins/tumbler-cover-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-desktop-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-font-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-jpeg-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-odf-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-pixbuf-thumbnailer.so
%{_libdir}/tumbler-1/plugins/tumbler-poppler-thumbnailer.so
%{_libdir}/tumbler-1/tumblerd
%{_datadir}/icons/hicolor/*/*/org.xfce*%{name}*
%{_userunitdir}/tumblerd.service

%files extras
%{_libdir}/tumbler-1/plugins/tumbler-gst-thumbnailer.so
%{?fedora:%{_libdir}/tumbler-1/plugins/tumbler-raw-thumbnailer.so}

%files devel
%{_libdir}/libtumbler-*.so
%{_libdir}/pkgconfig/%{name}-1.pc

%doc %{_datadir}/gtk-doc/

%dir %{_includedir}/%{name}-1
%{_includedir}/%{name}-1/tumbler

%changelog
%autochangelog
