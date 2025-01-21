Name:           zmat
Version:        0.9.8
Release:        15%{?dist}
Summary:        An easy-to-use data compression library
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/fangq/%{name}
Source0:        https://github.com/fangq/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc-c++ zlib-devel

%description
ZMat is a portable C library to enable easy-to-use data compression
and decompression (such as zlib/gzip/lzma/lzip/lz4/lz4hc algorithms)
and base64 encoding/decoding in an application.
It is fast and compact, can process a large array within a fraction
of a second. Among the supported compression methods, lz4 is the
fastest for compression/decompression; lzma is the slowest but has
the highest compression ratio; zlib/gzip have the best balance
between speed and compression time.


%package devel
Summary:        Development files for zmat - an easy-to-use data compression library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zlib-devel

%description devel
The %{name}-devel package provides the headers files and tools you may need to
develop applications using zmat.


%package static
Summary:        Static library for zmat - an easy-to-use data compression library
Requires:       %{name}-devel

%description static
The %{name}-static package provides the static library you may need to
develop applications using zmat.

%prep
%autosetup -n %{name}-%{version}
chmod a-x src/easylzma/pavlov/*
mv test examples

%build
%set_build_flags
mv fortran90/%{name}lib.f90 include/

pushd src
%make_build clean
%make_build lib CPPOPT="%{optflags} -fPIC"
mv ../lib/lib%{name}.a ../
%make_build clean
%make_build dll CPPOPT="%{optflags} -fPIC"
mv ../lib/lib%{name}.so ../lib/lib%{name}.so.%{version}
mv ../lib%{name}.a ../lib
popd


%install
install -m 755 -pd %{buildroot}/%{_includedir}/
install -m 644 -pt %{buildroot}/%{_includedir}/ include/%{name}lib.h
install -m 644 -pt %{buildroot}/%{_includedir}/ include/%{name}lib.f90

install -m 755 -pd %{buildroot}/%{_libdir}/
install -m 755 -pt %{buildroot}/%{_libdir}/ lib/lib%{name}.so.%{version}
install -m 644 -pt %{buildroot}/%{_libdir}/ lib/lib%{name}.a
pushd %{buildroot}/%{_libdir}
    ln -s lib%{name}.so.%{version} lib%{name}.so
popd


%files
%license LICENSE.txt
%doc README.rst
%doc AUTHORS.txt
%doc ChangeLog.txt
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.1

%files devel
%doc examples
%{_includedir}/%{name}lib.h
%{_includedir}/%{name}lib.f90
%{_libdir}/lib%{name}.so

%files static
%{_libdir}/lib%{name}.a


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.8-14
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 29 2020 Qianqian Fang <fangqq@gmail.com> - 0.9.8-4
- Move sample codes to devel and remove from the main package

* Thu May 28 2020 Qianqian Fang <fangqq@gmail.com> - 0.9.8-3
- Rebuild packages
- Add sample codes directly to the devel package

* Wed May 27 2020 Qianqian Fang <fangqq@gmail.com> - 0.9.8-2
- Update spec file to include demos package

* Mon May 25 2020 Qianqian Fang <fangqq@gmail.com> - 0.9.8-1
- Update to new release v0.9.8

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 14 2019 Qianqian Fang <fangqq@gmail.com> - 0.9.2-1
- Initial package
