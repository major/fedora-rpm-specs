%global forgeurl https://github.com/ming1/ubdsrv
%global commit 930546782d3996c686c6a5852bd670c67041b86c
# Upstream has not tagged any versions so far.
Version:       0.1
%forgemeta

Summary:       Userspace block driver server and ublk tool
Name:          ubdsrv
Release:       3%{?dist}
URL:           %{forgeurl}
Source:        %{forgesource}
License:       LGPLv2+ or MIT

# Patches to fix various build issues.
# Sent upstream 2022-08-31
Patch1:        0001-include-Install-ublksrv_aio.h.patch
Patch2:        0002-build-Install-ublk-in-sbin-don-t-install-demos.patch
Patch3:        0003-build-Add-EXTRA_DIST-rules-as-necessary.patch
Patch4:        0004-build-Add-a-maintainer-rule-for-checking-EXTRA_DIST.patch
Patch5:        0005-build-Install-ublksrv.pc-in-normal-pkgconf-location.patch

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
%doc README
%{_sbindir}/ublk
%{_libdir}/libublksrv.so.0*


%files devel
%license COPYING COPYING.LGPL LICENSE
%doc README
%{_includedir}/ublksrv_aio.h
%{_includedir}/ublksrv.h
%{_includedir}/ublk_cmd.h
%{_libdir}/libublksrv.so
%{_libdir}/pkgconfig/ublksrv.pc


%changelog
* Wed Aug 31 2022 Richard W.M. Jones <rjones@redhat.com> - 0.1-3
- Update to latest upstream version
- Fix various build issues

* Tue Aug 30 2022 Richard W.M. Jones <rjones@redhat.com> - 0.1-1
- Initial package
