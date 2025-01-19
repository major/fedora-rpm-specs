Name:           libslz
Version:        1.2.1
Release:        3%{?dist}
Summary:        StateLess Zip

License:        MIT
URL:            http://www.libslz.org/
Source:         https://github.com/wtarreau/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make


%description
SLZ is a fast and memory-less stream compressor which produces an output that
can be decompressed with zlib or gzip. It does not implement decompression at
all, zlib is perfectly fine for this.

The purpose is to use SLZ in situations where a zlib-compatible stream is
needed and zlib's resource usage would be too high while the compression ratio
is not critical. The typical use case is in HTTP servers and gateways which
have to compress many streams in parallel with little CPU resources to assign
to this task, and without having to limit the compression ratio due to the
memory usage. In such an environment, the server's memory usage can easily be
divided by 10 and the CPU usage by 3.


%package devel

Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
Development files for SLZ, the zenc and zdec commands that respectively
compress using SLZ and dump the decoding process.


%prep
%autosetup -p1


%build
%make_build CFLAGS="%{optflags}" LIB_LFLAGS='%{?__global_ldflags}'


%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} STRIP=/bin/true
rm %{buildroot}%{_libdir}/*.a


%files
%doc README
%license LICENSE
%{_libdir}/*.so.*


%files devel
%{_libdir}/*.so
%{_bindir}/*
%{_includedir}/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 28 2024 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.2.1-1
- Bump version to 1.2.1
- Drop upstreamed patch

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb 17 2023 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.2.0-8
- Bump release for SPDX license review (already correct)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 2020 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.2.0-1
- Bump version to 1.2.0
- Switch upstream to github mirror for convenience

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.1.0-8
- Drop ldconfig invocations: https://fedoraproject.org/wiki/Packaging:Scriptlets#Shared_Libraries
- Update upstream URL

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Dridi Boukelmoune <dridi@fedoraproject.org> - 1.1.0-6
- BR: gcc after https://fedoraproject.org/wiki/Packaging:C_and_C++ update

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 - Dridi Boukelmoune <dridi@fedoraproject.org> - 1.1.0-2
- Fix %%__global_ldflags usage for el6

* Sat Feb 11 2017 - Dridi Boukelmoune <dridi@fedoraproject.org> - 1.1.0-1
- Initial spec.
