Name:           gmime30
Version:        3.2.15
Release:        %autorelease
Summary:        Library for creating and parsing MIME messages

# The library is LGPL-2.1-or-later; various files (which we don't package)
# in examples/ and tests/ are GPL-2.0-or-later.
License:        LGPL-2.1-or-later
URL:            https://github.com/jstedfast/gmime
Source0:        https://github.com/jstedfast/gmime/releases/download/%{version}/gmime-%{version}.tar.xz

BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  make
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(gpg-error)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  vala

%description
The GMime suite provides a core library and set of utilities which may be
used for the creation and parsing of messages using the Multipurpose
Internet Mail Extension (MIME).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n gmime-%{version}

%build
%configure --disable-static
%make_build V=1

%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%files
%license COPYING
%doc AUTHORS README
%{_libdir}/libgmime-3.0.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/GMime-3.0.typelib

%files devel
%{_libdir}/libgmime-3.0.so
%{_libdir}/pkgconfig/gmime-3.0.pc
%{_includedir}/gmime-3.0/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GMime-3.0.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/gmime-3.*/
%{_datadir}/vala/

%changelog
%autochangelog
