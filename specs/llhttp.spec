# This package is rather exotic. The compiled library is a typical shared
# library with a C API. However, it has only a tiny bit of C source code. Most
# of the library is written in TypeScript, which is transpiled to C, via LLVM
# IR, using llparse (https://github.com/nodejs/llparse)—all of which happens
# within the NodeJS ecosystem.
#
# Historically, this package “built like” a NodeJS package, with a
# dev-dependency bundle from NPM that we used to transpile the original
# TypeScript sources to C downstream. We stopped doing this with release 9.3.0
# since this would have required using a pre-compiled esbuild executable from
# NPM, which would not have been acceptable. Instead, we use the upstream
# “release” tarball with pre-generated C source and header files included.
# This release archive lacks the original TypeScript source code for the
# generated C code, so we need to include it in an additional source. For
# details, see:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/what-can-be-packaged/#pregenerated-code
#
# Now that nodejs-esbuild is packaged, we could consider using it, but the
# complexity of switching back to this approach and properly auditing and
# handling the dev-dependency bundle is unpleasant enough that we plan to keep
# using the upstream “release” tarball with pre-generated C source and header
# files included.

# This package is a dependency of libgit2 which in turn is one of rpmautospec.
# When upgrading to a version with a new soname, this package needs to provide
# both in order to bootstrap itself and libgit2. Set %%bootstrap and
# %%previous_so_version for this (and unset and rebuild later).
%bcond bootstrap 0

Name:           llhttp
Version:        9.4.4
%global so_version 9.4
%global previous_so_version 9.3
Release:        %autorelease
Summary:        Port of http_parser to llparse

# SPDX
License:        MIT
URL:            https://github.com/nodejs/llhttp
Source0:        %{url}/archive/refs/tags/release/v%{version}/llhttp-release-v%{version}.tar.gz
# Contains the original TypeScript sources, which we must include in the source
# RPM per packaging guidelines.
Source1:        %{url}/archive/v%{version}/llhttp-%{version}.tar.gz

BuildSystem:    cmake

BuildRequires:  gcc
# There is no C++ involved, but CMake searches for a C++ compiler.
BuildRequires:  gcc-c++

%if %{with bootstrap}
%if "%{_lib}" == "lib64"
BuildRequires:  libllhttp.so.%{previous_so_version}()(64bit)
%else
BuildRequires:  libllhttp.so.%{previous_so_version}
%endif
%endif

%description
This project is a port of http_parser to TypeScript. llparse is used to
generate the output C source file, which could be compiled and linked with the
embedder's program (like Node.js).


%package devel
Summary:        Development files for llhttp

Requires:       llhttp%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
The llhttp-devel package contains libraries and header files for
developing applications that use llhttp.


%install -a
%if %{with bootstrap}
cp --verbose --preserve %{_libdir}/libllhttp.so.%{previous_so_version}{,.*} \
    %{buildroot}%{_libdir}
%endif


# The same obstacles that prevent us from re-generating the C sources from
# TypeScript also prevent us from running the tests, which rely on NodeJS.


%files
# Files LICENSE and LICENSE-MIT are duplicates.
%license LICENSE
%doc README.md
%{_libdir}/libllhttp.so.%{so_version}{,.*}
%if %{with bootstrap}
%{_libdir}/libllhttp.so.%{previous_so_version}{,.*}
%endif


%files devel
%{_includedir}/llhttp.h
%{_libdir}/libllhttp.so
%{_libdir}/pkgconfig/libllhttp.pc
%{_libdir}/cmake/llhttp/


%changelog
%autochangelog
