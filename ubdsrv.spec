%global forgeurl https://github.com/ming1/ubdsrv
%global commit 483d710ab8630304d13b59c2776f7386a566c467
# Upstream has not tagged any versions so far.
Version:       1.0
%forgemeta

Summary:       Userspace block driver server and ublk tool
Name:          ubdsrv
Release:       3.rc6%{?dist}.1
URL:           %{forgeurl}
Source:        %{forgesource}
License:       LGPLv2+ or MIT

# Basic build requirements.
BuildRequires: gcc, gcc-c++
BuildRequires: make
BuildRequires: autoconf, autoconf-archive, automake, libtool
BuildRequires: liburing-devel >= 2.2
BuildRequires: pkgconf


%description
This package allows you to write Linux block devices in userspace.  It
contains a library which can be linked to programs that implement
Linux userspace block devices, and also the "ublk" program which can
be used to create, list and delete ublk devices.


%package devel
Summary:       Development tools for %{name}
Requires:      %{name}%{_isa} = %{version}-%{release}
Provides:      ublksrv = %{version}-%{release}

%description devel
This package contains development tools for %{name}.


%prep
%forgeautosetup -p1


%build
autoreconf -f -i
%{configure} --disable-static
make V=1 %{?_smp_mflags}


%install
%{make_install}

# Remove libtool droppings.
rm %{buildroot}%{_libdir}/*.la


%files
%license COPYING COPYING.LGPL LICENSE
%doc README.rst
%{_sbindir}/ublk
%{_libdir}/libublksrv.so.0*


%files devel
%license COPYING COPYING.LGPL LICENSE
%doc README.rst
%{_includedir}/ublksrv_aio.h
%{_includedir}/ublksrv.h
%{_includedir}/ublk_cmd.h
%{_includedir}/ublksrv_utils.h
%{_libdir}/libublksrv.so
%{_libdir}/pkgconfig/ublksrv.pc


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3.rc6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 09 2022 Ming Lei <minlei@redhat.com> - 1.0-3.rc6
- Move to a newer tag (1.0-rc6 + a couple of upstream patches)

* Thu Nov 03 2022 Richard W.M. Jones <rjones@redhat.com> - 1.0-2
- Move to a newer tag (1.0-rc3 + a couple of upstream patches)

* Tue Sep 27 2022 Richard W.M. Jones <rjones@redhat.com> - 1.0-1
- New upstream version 1.0
- Remove upstream patches

* Wed Aug 31 2022 Richard W.M. Jones <rjones@redhat.com> - 0.1-3
- Update to latest upstream version
- Fix various build issues

* Tue Aug 30 2022 Richard W.M. Jones <rjones@redhat.com> - 0.1-1
- Initial package
