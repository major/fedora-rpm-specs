%global apiversion 0.10

Name: libwpd
Summary: A library for import of WordPerfect documents
Version: 0.10.3
Release: %autorelease
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Patch0: %{name}-gcc11.patch
URL: http://libwpd.sf.net/
License: LGPL-2.1-or-later OR MPL-2.0

BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: help2man
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(librevenge-generators-0.0)
BuildRequires: pkgconfig(librevenge-stream-0.0)
BuildRequires: pkgconfig(zlib)
BuildRequires: make

%description
%{name} is a library for import of WordPerfect documents.

%package tools
Summary: Tools to transform WordPerfect documents into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform WordPerfect documents into other formats.
Currently supported: HTML, raw, text.

%package devel
Requires: %{name}%{?_isa} = %{version}-%{release}
Summary: Files for developing with libwpd

%description devel
Includes and definitions for developing with libwpd.

%package doc
Summary: Documentation of %{name} API
BuildArch: noarch

%description doc
The %{name}-doc package contains API documentation for %{name}.

%prep
%autosetup -p1

%build
%configure --disable-static --disable-silent-rules
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT/%{_libdir}/*.la
# we install API docs directly from build
rm -rf $RPM_BUILD_ROOT/%{_docdir}/%{name}

# generate and install man pages
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in wpd2html wpd2raw wpd2text; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 wpd2*.1 %{buildroot}/%{_mandir}/man1

%ldconfig_scriptlets

%files
%doc CREDITS NEWS README
%license COPYING.LGPL COPYING.MPL
%{_libdir}/%{name}-%{apiversion}.so.*

%files tools
%{_bindir}/wpd2html
%{_bindir}/wpd2raw
%{_bindir}/wpd2text
%{_mandir}/man1/wpd2html.1*
%{_mandir}/man1/wpd2raw.1*
%{_mandir}/man1/wpd2text.1*

%files devel
%doc HACKING TODO
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc
%{_includedir}/%{name}-%{apiversion}

%files doc
%license COPYING.LGPL COPYING.MPL
%doc docs/doxygen/html
%doc docs/%{name}.dia
%doc docs/%{name}.png

%changelog
%autochangelog
