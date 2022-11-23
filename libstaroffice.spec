%global apiversion 0.0

Name: libstaroffice
Version: 0.0.7
Release: %autorelease
Summary: A library for import of binary StarOffice documents

License: LGPL-2.1-or-later OR MPL-2.0
URL: https://github.com/fosnola/libstaroffice/wiki
Source: https://github.com/fosnola/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: help2man
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(librevenge-generators-0.0)
BuildRequires: pkgconfig(librevenge-stream-0.0)
BuildRequires: pkgconfig(zlib)
BuildRequires: make

%description
%{name} is a library for import of binary StarOffice documents.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%package tools
Summary: Tools to transform StarOffice documents into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform StarOffice documents into other formats. Currently
supported: CSV, HTML, plain text, SVG, raw.

%prep
%autosetup -p1

%build
%configure --disable-static --disable-silent-rules --enable-zip
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
# rhbz#1001245 we install API docs directly from build
rm -rf %{buildroot}/%{_docdir}/%{name}

# generate and install man pages
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in sd2raw sd2svg sd2text sdc2csv sdw2html; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 sd2*.1 sd?2*.1 %{buildroot}/%{_mandir}/man1

%ldconfig_scriptlets

%files
%doc CREDITS NEWS README
%license COPYING.LGPL COPYING.MPL
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%doc ChangeLog
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files doc
%license COPYING.LGPL COPYING.MPL
%doc docs/doxygen/html

%files tools
%{_bindir}/sdw2html
%{_bindir}/sd2raw
%{_bindir}/sd2svg
%{_bindir}/sd2text
%{_bindir}/sdc2csv
%{_mandir}/man1/sdw2html.1*
%{_mandir}/man1/sd2raw.1*
%{_mandir}/man1/sd2svg.1*
%{_mandir}/man1/sd2text.1*
%{_mandir}/man1/sdc2csv.1*

%changelog
%autochangelog
