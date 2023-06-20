# Doxygen HTML help is not suitable for packaging due to a minified JavaScript
# bundle inserted by Doxygen itself. See discussion at
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555.
#
# We can enable the Doxygen PDF documentation as a substitute.
%bcond doc_pdf 1

Name:           libdxflib
Version:        3.26.4
%global so_version 3
Release:        %autorelease
Summary:        A C++ library for reading and writing DXF files

# The entire source is GPL-2.0-or-later, except:
#   - examples/readwrite/ is under “GNU Library General Public License”; since
#     no version is specified, this is LGPL-2.0-or-later; this affects the
#     License of the -doc subpackage
License:        GPL-2.0-or-later
URL:            https://www.ribbonsoft.com/en/90-dxflib
Source:         https://qcad.org/archives/dxflib/dxflib-%{version}-src.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  qt6-qtbase-devel

%global common_description %{expand:
dxflib is a C++ library for reading and writing DXF files.}

%description %{common_description}


%package        devel
Summary:        Development files for libdxflib
Requires:       libdxflib%{?_isa} = %{version}-%{release}

%description    devel %{common_description}

The libdxflib-devel package contains libraries and header files for
developing applications that use dxflib.


%package        doc
Summary:        Documentation and examples for libdxflib
# See comment above the base package’s License:
License:        GPL-2.0-or-later AND LGPL-2.0-or-later

BuildArch:      noarch

%if %{with doc_pdf}
BuildRequires:  doxygen
BuildRequires:  doxygen-latex
%endif

%description    doc %{common_description}

The libdxflib-doc package contains documentation and examples for dxflib.


%prep
%autosetup -n dxflib-%{version}-src
# Build as a shared library
sed -r -i 's/(CONFIG \+= )staticlib/\1shared/' dxflib.pro

%if %{with doc_pdf}
# We enable the Doxygen PDF documentation as a substitute. We must enable
# GENERATE_LATEX and LATEX_BATCHMODE; the rest are precautionary and should
# already be set as we like them. We also disable GENERATE_HTML, since we will
# not use it.
sed -r -i \
    -e "s/^([[:blank:]]*(GENERATE_LATEX|LATEX_BATCHMODE|USE_PDFLATEX|\
PDF_HYPERLINKS)[[:blank:]]*=[[:blank:]]*)NO[[:blank:]]*/\1YES/" \
    -e "s/^([[:blank:]]*(LATEX_TIMESTAMP|GENERATE_HTML)\
[[:blank:]]*=[[:blank:]]*)YES[[:blank:]]*/\1NO/" \
    dxflib.doxygen
%endif


%build
%{qmake_qt6} VERSION='%{version}'
%make_build

%if %{with doc_pdf}
mkdir -p doc
doxygen dxflib.doxygen
%make_build -C doc/classref/latex
%endif


%install
# The upstream build system does not have install targets.
install -t '%{buildroot}%{_includedir}/dxflib' -D -p -m 0644 src/*.h
# Use cp instead of install to preserve symlinks:
install -d '%{buildroot}%{_libdir}'
cp -p libdxflib.so* '%{buildroot}%{_libdir}'
# However, we currently still have an extra copy of the shared library. Ensure
# that all but the most fully-versioned file are symlinks.
sofile="$(basename "$(
  find '%{buildroot}%{_libdir}' -type f -name 'libdxflib.so.*.*.*' -print -quit
)")"
find '%{buildroot}%{_libdir}' -type f ! -name "${sofile}" \
    -execdir ln -s -v -f "${sofile}" '{}' ';'

# Generate pkgconfig file
install -d %{buildroot}%{_libdir}/pkgconfig
cat << 'EOF' > '%{buildroot}%{_libdir}/pkgconfig/dxflib.pc'
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: dxflib
Description: A C++ library for reading and writing DXF files
Version: %{version}
Libs: -L${libdir} -ldxflib
Cflags: -I${includedir}/dxflib
EOF


%files
%license gpl-2.0greater.txt dxflib_commercial_license.txt
%{_libdir}/libdxflib.so.%{so_version}{,.*}


%files devel
%{_includedir}/dxflib/
%{_libdir}/libdxflib.so
%{_libdir}/pkgconfig/dxflib.pc


%files doc
%license gpl-2.0greater.txt dxflib_commercial_license.txt
%doc examples/
%if %{with doc_pdf}
%doc doc/classref/latex/refman.pdf
%endif


%changelog
%autochangelog
