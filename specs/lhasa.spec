Name: lhasa
Summary: Free Software LHA implementation
License: ISC

Version: 0.4.0
Release: 6%{?dist}

URL: https://fragglet.github.io/lhasa/
Source0: https://github.com/fragglet/lhasa/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: make

# Explicitly require libs in the main package
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
Lhasa is a library for parsing LHA (.lzh) archives and a free replacement
for the Unix LHA tool.

Currently it is only possible to read from (i.e. decompress) archives;
generating (compressing) LHA archives may be an enhancement for future
versions. The aim is to be compatible with as many different variants
of the LHA file format as possible, including LArc (.lzs) and PMarc (.pma).

The command line tool aims to be interface-compatible with the non-free
Unix LHA tool (command line syntax and output), for backwards compatibility
with tools that expect particular output.


%package libs
Summary: Free Software LHA implementation

%description libs
Lhasa is a library for parsing LHA (.lzh) archives. Currently it is only
possible to read from (i.e. decompress) archives; generating (compressing)
LHA archives may be an enhancement for future versions. The aim is to be
compatible with as many different variants of the LHA file format as possible,
including LArc (.lzs) and PMarc (.pma).


%package devel
Summary: Development files for Lhasa
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package provides files required to develop programs using Lhasa,
the free software LHA implementation library.


%package doc
Summary: Documentation for Lhasa
BuildArch: noarch

# Some bundled JavaScript files are subject to the MIT license
License: ISC AND MIT
Provides: bundled(js-jquery)

%description doc
This package provides developer documentation (in HTML format)
for Lhasa, the free software LHA implementation library.


%prep
%autosetup
sed -i configure.ac \
	-e 's|TEST_CFLAGS="-DTEST_BUILD"|TEST_CFLAGS="$CFLAGS -DTEST_BUILD"|g'


%build
%global _configure ./autogen.sh
%configure --enable-static=no
%make_build

pushd doc
%make_build html
popd


%install
%make_install

install -m 755 -d %{buildroot}%{_pkgdocdir}
cp -a doc/html %{buildroot}%{_pkgdocdir}


%check
%make_build check


%files
%{_bindir}/lha
%{_mandir}/man1/lha.1*

%files libs
%doc AUTHORS NEWS
%license COPYING
%{_libdir}/liblhasa.so.0*

%files devel
%{_libdir}/liblhasa.so
%{_libdir}/pkgconfig/liblhasa.pc
%{_includedir}/liblhasa-1.0/

%files doc
%license COPYING
%doc %{_pkgdocdir}


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 28 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.4.0-2
- Build documentation in a -doc subpackage

* Sat Oct 28 2023 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.4.0-1
- Initial packaging
