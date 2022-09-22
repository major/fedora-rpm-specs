Name: surgescript
Summary: Scripting language for games

# All of SurgeScript's original code is licensed under ASL 2.0.
#
# There are a couple files borrowed from other projects
# that use different licenses.
#
# BSD:
# - src/surgescript/util/uthash.h
# - src/surgescript/util/xxh3.h
# - src/surgescript/util/xxhash.c
# - src/surgescript/util/xxhash.h
# Public Domain:
# - src/surgescript/util/xoroshiro128plus.c
# - src/surgescript/util/utf8.c
# - src/surgescript/util/utf8.h
%global license_main  ASL 2.0
%global license_devel ASL 2.0 and BSD and Public Domain

License: %{license_main}

Version: 0.5.6
Release: 1%{?dist}

URL: https://opensurge2d.org
Source0: https://github.com/alemart/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make


%description
SurgeScript is a scripting language for games. It has been designed
with the specific needs of games in mind. Its features include:
- The state-machine pattern: objects are state machines,
  making it easy to create in-game entities
- The composition approach: you may design complex objects
  and behaviors by means of composition
- The hierarchy system: objects have a parent and may have children,
  in a tree-like structure
- The game loop: it's defined implicitly
- Automatic garbage collection, object tagging and more!

SurgeScript is meant to be used in games and in interactive applications.
It's easy to integrate it into existing code, it's easy to extend,
it features a C-like syntax, and it's free and open-source software.

SurgeScript has been designed based on the experience of its developer
dealing with game engines, applications related to computer graphics and so on.
Some of the best practices have been incorporated into the language itself,
making things really easy for developers and modders.


# -- devel

%package devel
Summary: Files for developing applications using %{name}
License: %{license_devel}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains files required for
developing applications using %{name}.

# -- static

%package static
Summary: Files for developing applications using %{name}
License: %{license_devel}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static
This package contains files required for
developing applications using %{name},
using static linking.

# -- subpackages end


%prep
%setup -q


%build
%cmake \
	-DWANT_SHARED=ON  \
	-DWANT_STATIC=ON  \
	-DWANT_EXECUTABLE=ON  \
	-DCMAKE_BUILD_TYPE=Release
%cmake_build


%install
%cmake_install

# "make install" also installs an AppStream metainfo file and an icon
# for the surgescript interpreter, which is a terminal-based program.
# Remove those.
rm -rf %{buildroot}%{_metainfodir}
rm -rf %{buildroot}%{_datadir}/pixmaps/
rmdir %{buildroot}%{_datadir}


%files
%doc docs/
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.%{version}

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files static
%{_libdir}/lib%{name}-static.a
%{_libdir}/pkgconfig/%{name}-static.pc


%changelog
* Fri Sep 02 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.5.6-1
- Update to v0.5.6

* Sat Jul 23 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.5.5-5
- Fix CMake-related FTBFS

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jan 24 2021 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.5.5-1
- Update to v0.5.5

* Wed Jul 29 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.4.4-3
- Update spec to work properly with CMake out-of-source builds

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 16 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.4.4-1
- Update to upstream release v.0.5.4.4
- Remove the /lib -> /lib64 shenanigans from %%prep (issue solved upstream)

* Mon Apr 13 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.4.3-3
- Fix the License: tag
- Fix pkgconfig files having /lib hardcoded

* Mon Apr 13 2020 Artur Iwicki <fedora@svgames.pl> - 0.5.4.3-1
- Initial packaging
