Summary: Library for processing UTF-8 encoded Unicode strings
Name:    utf8proc
Version: 2.11.3
Release: %autorelease
License: MIT AND Unicode-DFS-2015
URL:     http://julialang.org/utf8proc/
Source:  https://github.com/JuliaLang/utf8proc/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
BuildRequires: make
BuildRequires: gcc
BuildRequires: perl-interpreter

%description
utf8proc is a library for processing UTF-8 encoded Unicode strings.
Some features are Unicode normalization, stripping of default ignorable
characters, case folding and detection of grapheme cluster boundaries.
A special character mapping is available, which converts for example
the characters “Hyphen” (U+2010), “Minus” (U+2212) and “Hyphen-Minus
(U+002D, ASCII Minus) all into the ASCII minus sign, to make them
equal for comparisons.

This package only contains the C library.

%package devel
Summary:  Header files, libraries and development documentation for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Contains header files for developing applications that use the %{name}
library.

The documentation for the C library is found in the utf8proc.h header file.
"utf8proc_map" is most likely the function you will be using for mapping UTF-8
strings, unless you want to allocate memory yourself.

%prep
%autosetup
# Disable slow tests and tests which require network access
sed -i '/-C bench/d;/\ttest.* data/d' Makefile
touch data/NormalizationTest.txt data/GraphemeBreakTest.txt data/Lowercase.txt data/Uppercase.txt

%build
%set_build_flags
%make_build

%check
%set_build_flags
make %{?_smp_mflags} check

%install
make install DESTDIR=%{buildroot} prefix=%{_prefix} includedir=%{_includedir} libdir=%{_libdir}
rm %{buildroot}%{_libdir}/libutf8proc.a

%ldconfig_scriptlets

%files
%doc LICENSE.md NEWS.md README.md
%{_libdir}/libutf8proc.so.3*

%files devel
%{_includedir}/utf8proc.h
%{_libdir}/libutf8proc.so
%{_libdir}/pkgconfig/libutf8proc.pc

%changelog
%autochangelog
