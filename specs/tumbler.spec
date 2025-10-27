# Review at https://bugzilla.redhat.com/show_bug.cgi?id=549593

%global xfceversion 4.20

Name:           tumbler
Version:        4.20.1
Release:        %autorelease
Summary:        D-Bus service for applications to request thumbnails

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://git.xfce.org/xfce/tumbler/
#VCS git:git://git.xfce.org/xfce/tumbler
Source0:        https://archive.xfce.org/src/xfce/%{name}/%{xfceversion}/%{name}-%{version}.tar.bz2

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  freetype-devel
BuildRequires:  gettext
BuildRequires:  gtk2-devel >= 2.10.0
BuildRequires:  intltool
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  libxfce4util-devel >= %{xfceversion}

# extra thumbnailers
BuildRequires:  gstreamer1-plugins-base-devel
%{?fedora:BuildRequires: libgsf-devel}
%{?fedora:BuildRequires: libopenraw-gnome-devel}


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
chmod 755 $RPM_BUILD_ROOT/%{_libdir}/*.so

find %{buildroot} -type f -name "*.la" -delete

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS
%config(noreplace) %{_sysconfdir}/xdg/tumbler/
%{_datadir}/dbus-1/services/org.xfce.Tumbler.*.service
%{_libdir}/libtumbler-*.so.*
%{_libdir}/tumbler-*/
%{_datadir}/icons/hicolor/*/*/org.xfce*%{name}*
%{_userunitdir}/tumblerd.service
%exclude %{_libdir}/tumbler-*/plugins/tumbler-gst-thumbnailer.so
%exclude %{?fedora: %{_libdir}/tumbler-*/plugins/tumbler-raw-thumbnailer.so}

%files extras
%{_libdir}/tumbler-*/plugins/tumbler-gst-thumbnailer.so
%{?fedora:%{_libdir}/tumbler-*/plugins/tumbler-raw-thumbnailer.so}

%files devel
%{_libdir}/libtumbler-*.so
%{_libdir}/pkgconfig/%{name}-1.pc

%doc %{_datadir}/gtk-doc/

%dir %{_includedir}/%{name}-1
%{_includedir}/%{name}-1/tumbler

%changelog
%autochangelog
