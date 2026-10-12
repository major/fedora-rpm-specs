Name:          libiio
Version:       1.0.0
Release:       %autorelease
Summary:       Library for Industrial IO
License:       LGPL-2.0-or-later
URL:           https://analogdevicesinc.github.io/libiio/
Source0:       https://github.com/analogdevicesinc/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: avahi-devel
BuildRequires: bison
BuildRequires: chrpath
BuildRequires: cmake
BuildRequires: flex
BuildRequires: gcc
BuildRequires: libaio-devel
BuildRequires: libserialport-devel
BuildRequires: libusb1-devel
BuildRequires: libxml2-devel
BuildRequires: libzstd-devel
BuildRequires: python3-devel
BuildRequires: python3-setuptools
# Docs
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: man2html

%description
Library for interfacing with Linux IIO devices

libiio is used to interface to Linux Industrial Input/Output (IIO) Subsystem.
The Linux IIO subsystem is intended to provide support for devices that in some 
sense are analog to digital or digital to analog converters (ADCs, DACs). This 
includes, but is not limited to ADCs, Accelerometers, Gyros, IMUs, Capacitance 
to Digital Converters (CDCs), Pressure Sensors, Color, Light and Proximity 
Sensors, Temperature Sensors, Magnetometers, DACs, DDS (Direct Digital 
Synthesis), PLLs (Phase Locked Loops), Variable/Programmable Gain Amplifiers 
(VGA, PGA), and RF transceivers.

%package utils
Summary: Utilities for Industrial IO
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Utilities for accessing IIO using libiio

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package doc
Summary: Development documentation for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description doc
Documentation for development with %{name}.

%package -n python3-iio
Summary: Python 3 bindings for Industrial IO (libiio)
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n python3-iio
Python 3 bindings for Industrial IO

%prep
%autosetup -p1

%generate_buildrequires
cd bindings/python/
%pyproject_buildrequires --pyproject-dependencies

%build
%cmake -DWITH_MAN=on \
       -DUDEV_RULES_INSTALL_DIR=%{_udevrulesdir}

%cmake_build

pushd bindings/python/
%pyproject_wheel
popd

# Sphinx introduces a lot of dependencies
pushd doc/doxygen
(cat doxyfile.in; echo "GENERATE_HTML = YES"; echo "HTML_OUTPUT = html"; echo "GENERATE_XML = NO") | doxygen -
popd

%install
%cmake_install

pushd bindings/python/
%pyproject_install
%pyproject_save_files iio
popd

# Fix rpath
chrpath --delete %{buildroot}/%{_bindir}/iio*
#Remove libtool archives.
find %{buildroot} -name '*.la' -delete

mkdir -p %{buildroot}%{_docdir}/%{name}
cp -aR doc/doxygen/generated/html/ %{buildroot}%{_docdir}/%{name}/html/


%files
%license COPYING.txt
%{_libdir}/%{name}.so.0
%{_libdir}/%{name}.so.1*
%{_mandir}/man3/libiio*
%{_udevrulesdir}/90-libiio.rules

%files utils
%{_bindir}/iio_*
%{_bindir}/iiod
%{_mandir}/man1/iio*

%files devel
%{_includedir}/iio/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%files doc
%doc %{_docdir}/%{name}

%files -n python3-iio -f %{pyproject_files}

%changelog
%autochangelog
