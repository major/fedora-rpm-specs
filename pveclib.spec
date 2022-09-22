Name:    pveclib
Version: 1.0.4.4
Release: 9%{?dist}
Summary: Library for simplified access to PowerISA vector operations
License: ASL 2.0
URL:     https://github.com/open-power-sdk/pveclib
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch: ppc %{power64}
BuildRequires: make
BuildRequires: libtool autoconf-archive gcc-c++
%{?el7:BuildRequires: devtoolset-9-gcc-c++}

%description
A library of useful vector operations for PowerISA 2.06 or later. Pveclib
builds on the PPC vector built-ins provided by <altivec.h> to provide higher
level operations. These operations also bridge gaps in compiler builtin
support for the latest PowerISA and functional differences between versions
of the PowerISA. The intent is to improve the productivity of application
developers who need to optimize their applications or dependent libraries for
POWER. This release also adds the "vec_int512_ppc.h" interface with supporting
runtime libraries. The DSO support IFUNC selection for power8/9.

%package devel
Summary: Header files for pveclib
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Contains header files for using pveclib operations as inline vector
instructions.

%package static
Summary:  This package contains static libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description static
This package contains static libraries for pveclib.
So far only constant vectors used in conversions.

%prep
%autosetup

%build
%{?el7:source /opt/rh/devtoolset-9/enable}
%configure --docdir=%{_docdir}/%{name}
%make_build

%install
%make_install

%check
%{?el7:source /opt/rh/devtoolset-9/enable}
# do not fail on test failures as builder might not support all required features
make check || :

# we are installing it using doc
find %{buildroot} -type f -name "*.la" -delete
find %{buildroot} -type f -name "libpvec.a" -delete
find %{buildroot} -type l -name "libpvecstatic.so" -delete
find %{buildroot} -type l -name "libpvecstatic.so.0" -delete
find %{buildroot} -type f -name "libpvecstatic.so.0.0.0" -delete
find %{buildroot} -type f -name "libpvecstatic.so.0.0.0*.debug" -delete

%files
%license LICENSE COPYING
%doc COPYING README.md CONTRIBUTING.md ChangeLog.md
%{_libdir}/libpvec.so.1
%{_libdir}/libpvec.so.1.*
%{?el7:%exclude %{_docdir}/%{name}}
%{?el7:%exclude %{_datadir}/licenses/%{name}}

%files devel
%doc README.md
%{_libdir}/libpvec.so
%{_includedir}/pveclib

%files static
%doc README.md
%{_libdir}/libpvecstatic.a

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 23 2021 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 1.0.4.4-7
- Update to pveclib 1.0.4.4 in order to fix bug 1987863.
- Update the source code link.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Munroe S <munroesj52@gmail.com> 1.0.4-1
- Updates for RPM release.
* Fri Jul  3 2020 Dave Love <loveshack@fedoraproject.org> - 1.0.3-3
- BR devtoolset on el7
- Fix duplicated doc and licence installation on el7
* Tue Jul 30 2019 Munroe S <munroesj52@gmail.com> 1.0.3-1
- Updates for RPM release.
* Mon Jul 22 2019 Munroe S <munroesj52@gmail.com> 1.0.2y-1
- Updates for RPM pre-release.
* Fri May 31 2019 Munroe S <munroesj52@gmail.com> 1.0.2-1
- Initial RPM release
