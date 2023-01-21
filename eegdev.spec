Name:           eegdev
Version:        0.2
Release:        16%{?dist}
Summary:        Library to acquire data from various EEG recording devices

License:        LGPLv3+
URL:            http://cnbi.epfl.ch/software/eegdev.html
Source0:        http://download.sourceforge.net/eegdev/%{name}-%{version}.tar.bz2
Patch0:         fix-biosemi-on-bigendian.patch
Patch1:         fix-racecond-in-biosemi-tests.patch
Patch2:         fix-biosemi-close-hangups.patch
Patch3:         fix-bison-grammar-file.patch
Patch4:         include-config_h.patch
Patch5:         fix-unaligned-memory-access.patch

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
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 29 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.2-1
- Initial package
