# Upstream uses weird versioning convention
%global upstreamver 2.3_1-opensource

Summary:    QIODevice that compresses data streams
Name:       qtiocompressor
Version:    2.3.1
Release:    %autorelease
License:    GPL-3.0-only OR LGPL-2.1-only WITH Digia-Qt-LGPL-exception-1.1
URL:        http://qt.nokia.com/products/appdev/add-on-products/catalog/4/Utilities/qtiocompressor/

Source0:    https://fale.fedorapeople.org/qtiocompressor/qtiocompressor-%{upstreamver}.tar.gz
Source1:    qtiocompressor.prf
Patch0:     qtiocompressor-qt6.patch

BuildRequires: make
BuildRequires: qt6-qtbase-devel
BuildRequires: zlib-devel

%description
The class works on top of a QIODevice subclass, compressing data before it is
written and decompressing it when it is read. Since QtIOCompressor works on
streams, it does not have to see the entire data set before compressing or
decompressing it. This can reduce the memory requirements when working on large
data sets.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   qt6-qtbase-devel

%description devel
This package contains libraries and header files for developing applications
that use QtIOCompressor.

%prep
%autosetup -p1 -n %{name}-%{upstreamver}

# Drop 'examples' from SUBDIRS to avoid build errors due to missing -lz
sed -i '/SUBDIRS.*examples/d' qtiocompressor.pro

%build
touch .licenseAccepted
./configure -library
%{qmake_qt6}
%make_build

%install
# libraries
mkdir -p %{buildroot}%{_qt6_libdir}
cp -a lib/* %{buildroot}%{_qt6_libdir}
chmod 755 %{buildroot}%{_qt6_libdir}/*.so.*.*.*

# headers
mkdir -p %{buildroot}%{_qt6_headerdir}/QtSolutions
cp -a \
    src/qtiocompressor.h \
    src/QtIOCompressor \
    %{buildroot}%{_qt6_headerdir}/QtSolutions

# qmake support
mkdir -p %{buildroot}%{_qt6_libdir}/qt6/mkspecs/features/
cp -a %{SOURCE1} %{buildroot}%{_qt6_libdir}/qt6/mkspecs/features/

%files
%license LGPL_EXCEPTION.txt LICENSE.*
%doc README.TXT
%{_qt6_libdir}/lib*.so.1*

%files devel
%doc doc
%{_qt6_libdir}/lib*.so
%{_qt6_headerdir}/QtSolutions/
%{_qt6_libdir}/qt6/mkspecs/features/%{name}.prf

%changelog
%autochangelog
