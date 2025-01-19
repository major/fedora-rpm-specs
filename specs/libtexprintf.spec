Name:           libtexprintf
Version:        1.25
Release:        5%{?dist}
Summary:        Formatted Output with tex-like syntax support

License:        GPL-3.0-only
URL:            https://github.com/bartp5/libtexprintf
Source:         %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz
# Ensure printf command has a format specifier
# https://github.com/bartp5/libtexprintf/pull/24
Patch:          clean-printf.patch

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

%description
The utftex program and underlying libtexprintf library provide tools to
pretty print math in mono-space fonts, using a tex-like syntax. It
produces UTF-8 encoded text. The program was inspired by asciiTeX, and
the improved asciiTeX fork. However, utftex supports much more TeX
syntax and contains extensive Unicode tables to map latex commands
to Unicode symbols. Use libtexprintf/utftex to unlock the math
capabilities of Unicode in mono-space text applications.

Note that how the equations look depends strongly on the font you use.
Naturally, one needs a monospace font with good Unicode support for
the symbols you use. A good monospace font for math is, for example,
JuliaMono.

%package devel
Summary: Development headers for libtexprintf
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for libtexprintf including header file.

%package tools
Summary: The utftex and utfinfo binaries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
utftex is a command line utility to format math.
utfstringinfo is a command line utility to analyze UTF8-strings.

%package static
Summary: Static libtexprintf library
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description static

Provides static libtexprintf library for use in compiling
applications that need it.


%prep
%autosetup -p1


%build
autoreconf -i
%configure
%make_build


%install
%make_install


%check
make check

%files
%doc README.md
%doc NEWS
%doc AUTHORS
%doc ChangeLog
%license COPYING
%{_libdir}/libtexprintf.so.1.0.0
%{_libdir}/libtexprintf.so.1
%{_mandir}/man3/texprintf.3*

%files static
%{_libdir}/libtexprintf.a

%files tools
%{_bindir}/utfstringinfo
%{_bindir}/utftex
%{_mandir}/man1/utfstringinfo.1*
%{_mandir}/man1/utftex.1*

%files devel
%{_includedir}/texprintf.h
%{_libdir}/libtexprintf.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 04 2023 Benson Muite <benson_muite@emailplus.org> - 1.25-1
- Initial packaging
