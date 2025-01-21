%global _lto_cflags %{nil}
%global _lib_min_ver 75

Name:		tkrzw
Version:	1.0.32
Release:	2%{?dist}
Summary:	A straightforward implementation of DBM
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	Apache-2.0
URL:		https://dbmx.net/%{name}/
Source0:	https://dbmx.net/%{name}/pkg/%{name}-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	help2man
# zlib-devel
BuildRequires:	pkgconfig(zlib)
# libzstd-devel
BuildRequires:	pkgconfig(libzstd)
# lz4-devel
BuildRequires:	pkgconfig(liblz4)
# xz-devel
BuildRequires:	pkgconfig(liblzma)
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}


%description
Tkrzw is a C++ library implementing DBM with various algorithms. It features
high degrees of performance, concurrency and durability.

%package	libs
Summary:	Libraries for applications using Tkrzw

%description	libs
This package provides the essential shared libraries
for any Tkrzw client program or interface.

%package	devel
Summary:	Development files for Tkrzw
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description	devel
This package contains libraries and header files for
developing applications that use Tkrzw.

%package	doc
Summary:	Tkrzw API documentation
BuildArch:	noarch

%description	doc
This package contains API documentation for developing
applications that use Tkrzw.


%prep
%autosetup
# https://github.com/estraier/tkrzw/issues/41
sed -i 's/MYLIBREV=66/MYLIBREV=69/g' configure.in


%build
autoreconf -vif
%configure  --enable-zlib --enable-lz4 --enable-lzma --enable-zstd
%make_build apidoc all
for bin in \
  tkrzw_build_util tkrzw_str_perf tkrzw_file_perf tkrzw_dbm_perf tkrzw_dbm_util
do
  LD_LIBRARY_PATH=$PWD help2man --no-info --no-discard-stderr \
    --version-string='%{version}' --output="${bin}.1" \
    "./${bin}"
done


%install
%make_install
# Remove static .a file
rm -f %{buildroot}%{_libdir}/lib%{name}.a
# mans
install -d %{buildroot}%{_mandir}/man1
install -t %{buildroot}%{_mandir}/man1 -m 0644 -p tkrzw_*.1


%check
%make_build check-light


%if 0%{?el8}
%ldconfig_scriptlets libs
%endif


%files
%{_bindir}/%{name}_*
%{_mandir}/man1/%{name}_*.1*

%files	libs
%license COPYING
%doc CONTRIBUTING.md
%{_libdir}/lib%{name}.so.{1,1.%{_lib_min_ver}.0}

%files	devel
%doc example
%{_includedir}/%{name}_*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files	doc
%license COPYING
%doc doc api-doc


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 18 2024 TI_Eugene <ti.eugene@gmail.com> - 1.0.32-1
- Version bump

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.31-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 12 2024 TI_Eugene <ti.eugene@gmail.com> - 1.0.31-1
- Version bump

* Thu May 30 2024 TI_Eugene <ti.eugene@gmail.com> - 1.0.29-2
- compression

* Tue May 07 2024 TI_Eugene <ti.eugene@gmail.com> - 1.0.29-1
- Version bump

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 06 2023 TI_Eugene <ti.eugene@gmail.com> - 1.0.27-1
- Version bump

* Wed Mar 01 2023 TI_Eugene <ti.eugene@gmail.com> - 1.0.26-1
- Version bump

* Tue Feb 28 2023 TI_Eugene <ti.eugene@gmail.com> - 1.0.25-1
- Version bump

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Apr 08 2022 TI_Eugene <ti.eugene@gmail.com> - 1.0.24-1
- Version bump

* Wed Mar 09 2022 TI_Eugene <ti.eugene@gmail.com> - 1.0.23-1
- Version bump

* Sun Jan 23 2022 TI_Eugene <ti.eugene@gmail.com> - 1.0.22-1
- Version bump

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 27 2021 TI_Eugene <ti.eugene@gmail.com> - 1.0.21-1
- Version bump

* Thu Nov 18 2021 TI_Eugene <ti.eugene@gmail.com> - 1.0.20-1
- Version bump

* Fri Oct 08 2021 TI_Eugene <ti.eugene@gmail.com> - 1.0.17-1
- Version bump
- ppc64le enabled back

* Sat Sep 25 2021 TI_Eugene <ti.eugene@gmail.com> - 1.0.13-1
- Version bump
- 'make check-light' implemented (https://github.com/estraier/tkrzw/issues/23)
- ppc64le temporary disabled

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 14 2021 TI_Eugene <ti.eugene@gmail.com> - 0.9.16-1
- Version bump
- el8 workaround (gcc10) removed
- 'make check' enabled again

* Tue May 11 2021 TI_Eugene <ti.eugene@gmail.com> - 0.9.15-1
- Version bump
- Added gcc10 as required for el8
- x32 enabled (#1920195)
- 'make check' temporary disabled

* Sun Apr 25 2021 TI_Eugene <ti.eugene@gmail.com> - 0.9.7-1
- Version bump
- All patches removed

* Wed Apr 21 2021 TI_Eugene <ti.eugene@gmail.com> - 0.9.5-1
- Version bump

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 0.9.3-6
- Rebuilt for removed libstdc++ symbol (#1937698)

* Mon Jan 25 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.9.3-5
- Link new RHBZ bug for ExcludeArch

* Thu Jan 21 2021 TI_Eugene <ti.eugene@gmail.com> - 0.9.3-4
- 'Required: pkgconfig' removed from -devel
- spec spaces/tabs resolved
- Added CONTRIBUTING.md to -libs
- examples/ moved from -doc to -devel
- `excludearch i686` proven

* Tue Jan 19 2021 TI_Eugene <ti.eugene@gmail.com> - 0.9.3-3
- Disabled only those tests that lock excessive numbers of pages (and will
  therefore fail on a system with default resource limits)
- Disabled LTO, since it causes test failures on all file-based database tests
- Added COPYING file in files section for -doc subpackage
- Installing doc/ and api-doc/ subdirectories in -doc subpackage
- Added example/ to -doc
- Changed man pages wildcard from ..._*.1.* to ..._*.1*
- Removed -lib/-libs mess
- Excluded i686 arch

* Mon Jan 18 2021 TI_Eugene <ti.eugene@gmail.com> - 0.9.3-2
- License fixes.
- *.so.* names fix
- make_build fix
- -doc fixes
- check fixes
- ldconfig call fix
- compiler flags fixes

* Fri Jan 08 2021 TI_Eugene <ti.eugene@gmail.com> - 0.9.3-1
- Initial packaging.
