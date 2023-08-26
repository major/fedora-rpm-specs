%global apiversion 0.1

Name: libetonyek
Version: 0.1.11~20230802.git9c3a8cb
Release: %autorelease
Summary: A library for import of Apple iWork documents

License: MPL-2.0
URL: http://wiki.documentfoundation.org/DLP/Libraries/libetonyek
# Source: http://dev-www.libreoffice.org/src/%%{name}/%%{name}-%%{version}.tar.xz
# Sources have been prepared by cloning the master branch of git repo at
# https://git.libreoffice.org/libetonyek
Source: %{name}-20230802-git9c3a8cb.tar.xz

BuildRequires: automake
BuildRequires: boost-devel
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: glm-devel
BuildRequires: gperf
BuildRequires: help2man
BuildRequires: libtool
BuildRequires: make
BuildRequires: pkgconfig(cppunit)
BuildRequires: pkgconfig(liblangtag)
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(librevenge-generators-0.0)
BuildRequires: pkgconfig(librevenge-stream-0.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(mdds-2.1)
BuildRequires: pkgconfig(zlib)

%description
%{name} is library for import of Apple iWork documents. It supports
documents created by any version of Keynote, Pages or Numbers.

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
Summary: Tools to transform Apple iWork documents into other formats
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Tools to transform Apple iWork documents into other formats. Currently
supported: CSV, HTML, SVG, text, and raw.

%prep
%autosetup -p1 -n %{name}

%build
autoreconf -i -f
%configure --disable-silent-rules --disable-static --disable-werror --with-mdds=2.1
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make_build

%install
%make_install
rm -f %{buildroot}/%{_libdir}/*.la
# we install API docs directly from build
rm -rf %{buildroot}/%{_docdir}/%{name}

# generate and install man pages
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
for tool in key2raw key2text key2xhtml numbers2csv numbers2raw numbers2text pages2html pages2raw pages2text; do
    help2man -N -S '%{name} %{version}' -o ${tool}.1 %{buildroot}%{_bindir}/${tool}
done
install -m 0755 -d %{buildroot}/%{_mandir}/man1
install -m 0644 key2*.1 numbers2*.1 pages2*.1 %{buildroot}/%{_mandir}/man1

%ldconfig_scriptlets

%check
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
if ! %make_build check; then
    cat src/test/*.log
    exit 1
fi

%files
%doc AUTHORS FEATURES NEWS README
%license COPYING
%{_libdir}/%{name}-%{apiversion}.so.*

%files devel
%{_includedir}/%{name}-%{apiversion}
%{_libdir}/%{name}-%{apiversion}.so
%{_libdir}/pkgconfig/%{name}-%{apiversion}.pc

%files doc
%license COPYING
%doc docs/doxygen/html

%files tools
%{_bindir}/key2raw
%{_bindir}/key2text
%{_bindir}/key2xhtml
%{_bindir}/numbers2csv
%{_bindir}/numbers2raw
%{_bindir}/numbers2text
%{_bindir}/pages2html
%{_bindir}/pages2raw
%{_bindir}/pages2text
%{_mandir}/man1/key2raw.1*
%{_mandir}/man1/key2text.1*
%{_mandir}/man1/key2xhtml.1*
%{_mandir}/man1/numbers2csv.1*
%{_mandir}/man1/numbers2raw.1*
%{_mandir}/man1/numbers2text.1*
%{_mandir}/man1/pages2html.1*
%{_mandir}/man1/pages2raw.1*
%{_mandir}/man1/pages2text.1*

%changelog
%autochangelog
