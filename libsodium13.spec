%global libname libsodium
%global soname  13

Name:           %{libname}%{soname}
Version:        1.0.5
Release:        1%{?dist}
Summary:        Compatibility version of the Sodium crypto library
License:        ISC
URL:            https://libsodium.org
Source0:        https://download.libsodium.org/libsodium/releases/old/unsupported/%{libname}-%{version}.tar.gz

# Conflict with older libsodium packages that ship libraries with the same
# soname as this compat package.
Conflicts:      libsodium < 1.0.6


%description
Sodium is a new, easy-to-use software library for encryption, decryption,
signatures, password hashing and more. It is a portable, cross-compilable,
installable, packageable fork of NaCl, with a compatible API, and an extended
API to improve usability even further. Its goal is to provide all of the core
operations needed to build higher-level cryptographic tools. The design
choices emphasize security, and "magic constants" have clear rationales.

The same cannot be said of NIST curves, where the specific origins of certain
constants are not described by the standards. And despite the emphasis on
higher security, primitives are faster across-the-board than most
implementations of the NIST standards.

This is a compatibility package containing libsodium.so.13.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

# Conflict with libsodium-devel no matter what, since the files conflict.
Conflicts:      libsodium-devel


%description    devel
This package contains libraries and header files for
developing applications that use %{name} libraries.


%prep
%setup -q -n %{libname}-%{version}


%build
%configure \
  --disable-static \
  --disable-silent-rules \
  --disable-opt
%make_build


%install
%make_install
rm %{buildroot}%{_libdir}/%{libname}.la


%check
make check


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%license LICENSE
%{_libdir}/%{libname}.so.%{soname}*


%files devel
%doc AUTHORS ChangeLog README.markdown THANKS
%doc test/default/*.{c,exp,h}
%doc test/quirks/quirks.h
%{_includedir}/sodium.h
%{_includedir}/sodium/
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc


%changelog
* Tue Jan 09 2018 Carl George <carl@george.computer> - 1.0.5-1
- Port from libsodium to libsodium13
- Install license correctly
- Disable native CPU optimizations
- Update summary and descriptions to clarify this is a compatibility package

* Sun Oct 25 2015 Christopher Meng <rpm@cicku.me> - 1.0.5-1
- Update to 1.0.5

* Mon Jul 13 2015 Christopher Meng <rpm@cicku.me> - 1.0.3-1
- Update to 1.0.3

* Fri Jan 23 2015 Christopher Meng <rpm@cicku.me> - 1.0.2-1
- Update to 1.0.2

* Sat Nov 22 2014 Christopher Meng <rpm@cicku.me> - 1.0.1-1
- Update to 1.0.1

* Sat Oct 18 2014 Christopher Meng <rpm@cicku.me> - 1.0.0-1
- Update to 1.0.0

* Sun Aug 24 2014 Christopher Meng <rpm@cicku.me> - 0.7.0-1
- Update to 0.7.0

* Thu Jul 17 2014 Christopher Meng <rpm@cicku.me> - 0.6.1-1
- Update to 0.6.1

* Thu Jul 03 2014 Christopher Meng <rpm@cicku.me> - 0.6.0-1
- Update to 0.6.0

* Fri May 16 2014 Christopher Meng <rpm@cicku.me> - 0.5.0-1
- Update to 0.5.0

* Mon Dec 09 2013 Christopher Meng <rpm@cicku.me> - 0.4.5-3
- Disable silent build rules.
- Preserve the timestamp.

* Wed Nov 20 2013 Christopher Meng <rpm@cicku.me> - 0.4.5-2
- Add doc for devel package.
- Add support for EPEL6.

* Wed Nov 20 2013 Christopher Meng <rpm@cicku.me> - 0.4.5-1
- Update to 0.4.5

* Wed Jul 10 2013 Christopher Meng <rpm@cicku.me> - 0.4.2-2
- Drop useless files.
- Improve the description.

* Wed Jul 10 2013 Christopher Meng <rpm@cicku.me> - 0.4.2-1
- Initial Package.
