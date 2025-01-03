Name:           libphidget22
Version:        1.22.20241219
Release:        1%{?dist}
Summary:        Drivers and API for Phidget devices

# libphidget is LGPL-3.0-or-later
# Bundled mos is BSD 2/3 Clause
License:        LGPL-3.0-or-later and BSD-2-Clause and BSD-3-Clause
URL:            https://www.phidgets.com
Source0:        https://www.phidgets.com/downloads/phidget22/libraries/linux/%{name}/%{name}-%{version}.tar.gz

Provides:       bundled(mos)
Provides:       libphidget = %{version}-%{release}
# Last build was libphidget-2.1.8.20140319-19.fc36
Obsoletes:      libphidget < 2.1.8.20140319-20

BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  avahi-devel
BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  libusb1-devel
BuildRequires:  make
BuildRequires:  gawk
BuildRequires:  udev

Requires:       udev
Requires:       avahi-compat-libdns_sd

%description
Phidgets are a set of "plug and play" building blocks for low cost USB 
sensing and control from your PC.  All the USB complexity is taken care 
of by the robust libphidget API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup
# These headers are supplied by the avahi-compat-libdns_sd-devel package
# We can get rid of the bundled ones
rm -rf src/ext/include/avahi-*


%build
autoreconf -fi
%configure --disable-silent-rules --disable-static --enable-zeroconf=avahi --disable-ldconfig --enable-jni
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
mkdir -p -m 0755 %{buildroot}%{_udevrulesdir}/
install -p -m 0644 plat/linux/udev/99-libphidget22.rules %{buildroot}%{_udevrulesdir}/


%ldconfig_scriptlets


%files
%doc AUTHORS README
%license COPYING
%{_libdir}/*.so.*
%{_udevrulesdir}/99-libphidget22.rules

%files devel
%{_includedir}/mos/
%{_includedir}/phidget22.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Wed Jan 01 2025 Richard Shaw <hobbes1069@gmail.com> - 1.22.20241219-1
- Update to 1.22.20241219.

* Sun Nov 24 2024 Richard Shaw <hobbes1069@gmail.com> - 1.21.20241122-1
- Update to 1.21.20241122.

* Tue Sep 10 2024 Richard Shaw <hobbes1069@gmail.com> - 1.20.20240909-1
- Update to 1.20.20240909.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.20240304-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 21 2024 Richard Shaw <hobbes1069@gmail.com> - 1.19.20240304-1
- Update to 1.19.20240304.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.20240109-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.20240109-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Richard Shaw <hobbes1069@gmail.com> - 1.17.20240109-1
- Update to 1.17.20240109.

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.20230603-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 05 2023 Richard Shaw <hobbes1069@gmail.com> - 1.15.20230603-1
- Update to 1.15.20230603.

* Mon May 29 2023 Richard Shaw <hobbes1069@gmail.com> - 1.15.20230526-1
- Update to 1.15.20230526.

* Tue May 16 2023 Richard Shaw <hobbes1069@gmail.com> - 1.14.20230331-1
- Update to 1.14.20230331.

* Wed Feb 22 2023 Richard Shaw <hobbes1069@gmail.com> - 1.13.20230221-1
- Update to 1.13.20230221.

* Sat Feb 04 2023 Richard Shaw <hobbes1069@gmail.com> - 1.13.20230203-1
- Update to 1.13.20230203.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.20230109-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Richard Shaw <hobbes1069@gmail.com> - 1.13.20230109-1
- Update to 1.13.20230109.

* Tue Sep 20 2022 Richard Shaw <hobbes1069@gmail.com> - 1.12.20220912-1
- Update to 1.12.20220912.

* Sun Sep 11 2022 Richard Shaw <hobbes1069@gmail.com> - 1.11.20220822-1
- Update 1.11.20220822.

* Fri Aug 12 2022 Richard Shaw <hobbes1069@gmail.com> - 1.10.20220530-2
- Update per reviewer comments:
  Update license
  Fix BR on gcc
  Remove remnants of java package from older version
  Fix include in %%files
  Install udev rule in correct location

* Mon Aug  8 2022 Richard Shaw <hobbes1069@gmail.com> - 1.10.20220530-1
- Initial repackaging from libphidget.

