%global giturl  https://github.com/flatsurf/e-antic

Name:           e-antic
Version:        2.0.2
Release:        3%{?dist}
Summary:        Real Embedded Algebraic Number Theory In C

License:        LGPL-3.0-or-later
URL:            https://flatsurf.github.io/e-antic/libeantic/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/%{name}-%{version}.tar.gz
# The e-antic sources contain patches to flint, but those patches have already
# been incorporated into the Fedora versions.  Make e-antic skip attempts to
# build the patched files.
Patch:          %{name}-unpatch.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  boost-devel
BuildRequires:  catch2-devel
BuildRequires:  cereal-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(flint)

# Missing dependencies to build docs:
# - byexample: https://github.com/byexamples/byexample
# - standardese: https://github.com/standardese/standardese

# The python interface, pyeantic, requires cppyy, which is currently not
# available in Fedora.

%description
E-ANTIC is a C/C++ library to deal with real embedded number fields,
built on top of ANTIC.  Its aim is to have as fast as possible exact
arithmetic operations and comparisons.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel%{?_isa}
Requires:       cereal-devel%{?_isa}
Requires:       flint-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%conf
# Upstream does not generate the configure script
autoreconf -fi .

# Make catch2 available for testing
mkdir -p libeantic/test/external/catch2/single_include
ln -s %{_includedir}/catch2 libeantic/test/external/catch2/single_include

# Make cereal available for testing
rmdir libeantic/test/external/cereal
ln -s %{_includedir}/cereal libeantic/test/external/cereal

%build
%configure --disable-silent-rules --disable-static \
  --enable-openmp \
  --without-benchmark \
  --without-byexample \
  --without-doc \
  --without-pyeantic \
  --without-realalg \
  --without-sage

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libeantic/libtool

%make_build

%install
%make_install

# We do not want the libtool archives
rm %{buildroot}%{_libdir}/*.la

# Documentation is installed below
rm -fr %{buildroot}%{_docdir}

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} make check

%files
%doc AUTHORS README.md
%license COPYING COPYING.LESSER
%{_libdir}/libeantic.so.3*
%{_libdir}/libeanticxx.so.3*

%files          devel
%{_includedir}/%{name}/
%{_includedir}/libeantic/
%{_libdir}/libeantic.so
%{_libdir}/libeanticxx.so

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Mar  4 2024 Jerry James <loganjerry@gmail.com> - 2.0.2-1
- Version 2.0.2

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 1.3.0-3
- Stop building for 32-bit x86

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec  6 2022 Jerry James <loganjerry@gmail.com> - 1.3.0-1
- Version 1.3.0

* Thu Oct 27 2022 Jerry James <loganjerry@gmail.com> - 1.2.3-1
- Version 1.2.3

* Mon Aug 15 2022 Jerry James <loganjerry@gmail.com> - 1.2.1-4
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul  5 2022 Jerry James <loganjerry@gmail.com> - 1.2.1-3
- Rebuild for flint 2.9.0

* Wed Jun  1 2022 Jerry James <loganjerry@gmail.com> - 1.2.1-2
- Rebuild for arb 2.22.1

* Sat May 21 2022 Jerry James <loganjerry@gmail.com> - 1.2.1-1
- Version 1.2.1
- Bundling cereal 1.3.0 is no longer necessary

* Mon Apr 11 2022 Jerry James <loganjerry@gmail.com> - 1.2.0-1
- Version 1.2.0

* Thu Mar  3 2022 Jerry James <loganjerry@gmail.com> - 1.1.0-1
- Version 1.1.0
- Drop upstreamed -cmp and -odr patches

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Jerry James <loganjerry@gmail.com> - 1.0.3-2
- Replace -negative-int patch with better -cmp patch
- Add -odr patch

* Wed Aug 25 2021 Jerry James <loganjerry@gmail.com> - 1.0.3-2
- Rebuild for flint 2.8.0

* Fri Aug 20 2021 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- Version 1.0.3

* Wed Aug 11 2021 Jerry James <loganjerry@gmail.com> - 1.0.2-1
- Version 1.0.2

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 18 2021 Jerry James <loganjerry@gmail.com> - 1.0.1-2
- Drop the python3-pyeantic subpackage due to missing cppyy

* Thu Jul 15 2021 Jerry James <loganjerry@gmail.com> - 1.0.1-1
- Version 1.0.1
- Add the python3-pyeantic subpackage
- Add -unpatch and -negative-int patches

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug  7 2020 Jerry James <loganjerry@gmail.com> - 0.1.8-1
- Initial RPM
