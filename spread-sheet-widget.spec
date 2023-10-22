Name:		spread-sheet-widget
Version:	0.10
Release:	%autorelease
Summary:	A library for Gtk+ which provides a spread sheet widget
License:	GPL-3.0-or-later
URL:		https://www.gnu.org/software/ssw/
Source0:	https://alpha.gnu.org/gnu/ssw/%{name}-%{version}.tar.gz
Source1:	https://alpha.gnu.org/gnu/ssw/%{name}-%{version}.tar.gz.sig
Source2:	BAF59BDF98664CEEF14D2A5A6A233DCD47A92289.gpg
Patch1:		spread-sheet-widget-0001-No-need-to-specify-gtk3-lib-in-pc-file.patch
Patch2:		spread-sheet-widget-0002-Use-more-standard-macros-in-pc-file.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	gnupg2
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	pkgconfig(glib-2.0) >= 2.44
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.18.0
BuildRequires:	texinfo


%description
GNU Spread Sheet Widget is a library for Gtk+ which provides a widget for
viewing and manipulating 2 dimensional tabular data in a manner similar to many
popular spread sheet programs.

The design follows the model-view-controller paradigm and is of complexity O(1)
in both time and space. This means that it is efficient and fast even for very
large data.

Features commonly found in graphical user interfaces such as cut and paste,
drag and drop and row/column labelling are also included.


%package devel
Summary: The development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}


%description devel
Additional header files for development with %{name}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1
autoreconf -ivf


%build
%configure --disable-static
%make_build


%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
rm -f %{buildroot}%{_infodir}/dir


%check
make check


%files
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.*


%files devel
%{_includedir}/ssw-axis-model.h
%{_includedir}/ssw-sheet-axis.h
%{_includedir}/ssw-sheet.h
%{_includedir}/ssw-virtual-model.h
%{_infodir}/%{name}.info*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
%autochangelog
