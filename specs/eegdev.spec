Name:           eegdev
Version:        0.2
Release:        %autorelease
Summary:        Library to acquire data from various EEG recording devices

License:        LGPL-3.0-or-later
URL:            https://archiveweb.epfl.ch/cnbi.epfl.ch/index.html%3Fp=228.html
Source0:        http://download.sourceforge.net/eegdev/%{name}-%{version}.tar.bz2
Patch0:         fix-biosemi-on-bigendian.patch
Patch1:         fix-racecond-in-biosemi-tests.patch
Patch2:         fix-biosemi-close-hangups.patch
Patch3:         fix-bison-grammar-file.patch
Patch4:         include-config_h.patch
Patch5:         fix-unaligned-memory-access.patch
Patch6:         work-around-flex-bug.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  automake autoconf libtool
BuildRequires:  gnulib-devel
BuildRequires:  bison flex
# EEGfile backend
BuildRequires:  xdffileio-devel
# Biosemi backend
BuildRequires:  libusbx-devel
# Neurosky backend
BuildRequires:  bluez-libs-devel
# Tobi interface A backend
BuildRequires:  expat-devel
BuildRequires: make
Recommends:     %{name}-plugins%{?_isa}
Provides:       bundled(gnulib)

%description
eegdev is a library that provides a unified interface for accessing various EEG
(and other biosignals) acquisition systems. This interface has been designed to
be both flexible and efficient. The device specific part is implemented by the
mean of plugins which makes adding new device backend fairly easy even if the
library does not support them yet officially.

The core library not only provides to users a unified and consistent interfaces
to the acquisition device but it also provides many functionalities to the
device backends (plugins) ranging from configuration to data casting and scaling
making writing new device backend an easy task.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        plugins
Summary:        Plugins for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    plugins
Plugins for %{name}.

%prep
%autosetup -p1

# drop bundled libs
rm -rf lib/*

# do not run neurosky test (requires /dev/rfcomm0)
sed -i -e '/TESTS += sysneurosky/d' tests/Makefile.am

%build
./autogen.sh
%configure --enable-corelib-build \
  --with-xdf                      \
  --with-act2                     \
  --with-neurosky                 \
  --with-tia                      
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%check
make check

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS
%{_libdir}/lib%{name}.so.*
%dir %{_libdir}/%{name}/
%{_mandir}/man5/%{name}-open-options.5*

%files devel
%doc %{_docdir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}*.h
%{_mandir}/man3/egd_*.3*

%files plugins
%{_libdir}/%{name}/*
%exclude %{_mandir}/man5/%{name}-open-options.5*
%{_mandir}/man5/%{name}-*.5*

%changelog
%autochangelog
