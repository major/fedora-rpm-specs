Name:		zlib-ng
Version:	2.0.6
Release:	2%{?dist}
Summary:	Zlib replacement with optimizations
License:	zlib
Url:		https://github.com/zlib-ng/zlib-ng
Source0:	https://github.com/zlib-ng/zlib-ng/archive/%{version}/%{name}-%{version}.tar.gz

# Be explicit about the soname in order to avoid unintentional changes.
%global soname libz-ng.so.2

ExclusiveArch:	aarch64 i686 ppc64le s390x x86_64
BuildRequires:	cmake
BuildRequires:	gcc

%description
zlib-ng is a zlib replacement that provides optimizations for "next generation"
systems.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
The %{name}-devel package contains static libraries and header files for
developing application that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
# zlib-ng uses a different macro for library directory.
%cmake -DWITH_SANITIZERS=ON -DINSTALL_LIB_DIR=%{_libdir}
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%{_libdir}/%{soname}
%{_libdir}/libz-ng.so.2.*
%license LICENSE.md
%doc README.md

%files devel
%{_includedir}/zconf-ng.h
%{_includedir}/zlib-ng.h
%{_libdir}/libz-ng.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 14 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 2.0.6-1
- New upstream release 2.0.6

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2.20210625gitc69f78bc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 2.0.2-5.20210625gitc69f78bc5e
- Update to v2.0.5.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2.20210323git5fe25907e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Apr 18 2021 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 2.0.2-1.20210323gite5fe25907e
- Update to v2.0.2.
- Remove the manpage that got removed from upstream.

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-0.4.20200912gite58738845
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Sep 13 2020 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 1.9.9-0.3.20200912gite58738845
- Update to a newer commit.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.9-0.3.20200609gitfe69810c2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 1.9.9-0.2.20200609gitfe69810c2
- Replace cmake commands with new cmake macros

* Mon Jul 06 2020 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 1.9.9-0.1.20200609gitfe69810c2
- Improve the archive name.
- Starte release at 0.1 as required for prerelease.
- Make the devel package require an arch-dependent runtime subpackage.
- Remove %%ldconfig_scriptlets.
- Glob the man page extension.
- Move unversioned shared library to the devel subpackage

* Wed Jul 01 2020 Tulio Magno Quites Machado Filho <tuliom@ascii.art.br> - 1.9.9-0.20200609gitfe69810c2
- Initial commit
