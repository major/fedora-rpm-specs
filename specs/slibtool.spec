# To ensure hardened build on EL7
%global _hardened_build 1

# Fix platform definitions so slibtool build scripts can find binaries
# Matches what's in the gcc packaging
%ifnarch %{arm}
%global _gnu %{nil}
%else
%global _gnu -gnueabi
%endif
%global _host %{_target_platform}
%global _build %{_target_platform}

Name:           slibtool
Version:        0.5.28
Release:        14%{?dist}
Summary:        A skinny libtool implementation, written in C

License:        MIT
URL:            http://git.midipix.org/cgit.cgi/slibtool
Source0:        http://midipix.org/dl/slibtool/%{name}-%{version}.tar.xz

BuildRequires:  gcc, make

# slibtool uses libslibtool internally
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
'slibtool' is an independent reimplementation of the widely used libtool,
written in C. 'slibtool' is designed to be a clean, fast, easy-to-use
libtool drop-in replacement, and is accordingly aimed at package authors,
distro developers, and system integrators. 'slibtool' maintains compatibility
with libtool in nearly every aspect of the tool's functionality as well as
semantics, leaving out (or turning into a no-op) only a small number of
features that are no longer needed on modern systems.

Being a compiled binary, and although not primarily written for the sake of
performance, building a package with 'slibtool' is often faster than with its
script-based counterpart. The resulting performance gain would normally vary
between packages, and is most noticeable in builds that invoke libtool a large
number of times, and which are characterized by the short compilation duration
of individual translation units.


%package libs
Summary:        Backend library for %{name}

%description libs
This package provides libraries for applications to use the functionality
of %{name}.

%package devel
Summary:        Development files for lib%{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package provides files necessary for developing applications
to use functionality provided by %{name}.


%prep
%autosetup -p1


%build
%configure --enable-shared --all-shared \
           --pkgpsrc="https://src.fedoraproject.org/rpms/slibtool/" \
           --pkgdurl="https://apps.fedoraproject.org/packages/slibtool"
%make_build


%install
%make_install


%ldconfig_scriptlets libs

%files
%license COPYING.SLIBTOOL
%doc README NEWS THANKS CONTRIB
%{_bindir}/clibtool*
%{_bindir}/dlibtool*
%{_bindir}/r*libtool
%{_bindir}/slibtool*

%files libs
%license COPYING.SLIBTOOL
%{_libdir}/lib%{name}.so.*

%files devel
%license COPYING.SLIBTOOL
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.28-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.28-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.28-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.28-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Neal Gompa <ngompa13@gmail.com> - 0.5.28-1
- Update to 0.5.28

* Sat Oct 27 2018 Neal Gompa <ngompa13@gmail.com> - 0.5.26-1
- Update to 0.5.26

* Sun Aug 26 2018 Neal Gompa <ngompa13@gmail.com> - 0.5.25-1
- Update to 0.5.25

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Neal Gompa <ngompa13@gmail.com> - 0.5.24-2
- Add missing ldconfig_scriptlets macro for EL7 and F27

* Sat Jul 07 2018 Neal Gompa <ngompa13@gmail.com> - 0.5.24-1
- Update to 0.5.24
- Drop EL7 build hack

* Sat Jul 07 2018 Neal Gompa <ngompa13@gmail.com> - 0.5.23-1
- Update to 0.5.23

* Sat Jul 07 2018 Neal Gompa <ngompa13@gmail.com> - 0.5.22-1
- Update to 0.5.22

* Sat Jul 07 2018 Neal Gompa <ngompa13@gmail.com> - 0.5.21-2
- Fix the build for EL7

* Sat Jul 07 2018 Neal Gompa <ngompa13@gmail.com> - 0.5.21-1
- Update to 0.5.21

* Wed Jun 27 2018 Neal Gompa <ngompa13@gmail.com> - 0.5.20-1
- Initial packaging for Fedora
