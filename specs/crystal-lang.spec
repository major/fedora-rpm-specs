# Default to self-hosted routine builds (with bootstrap disabled).
# Use --with bootstrap for initial cold-start bootstrap in Koji side-tags.
%bcond_with bootstrap
%bcond_without doc
%bcond_without check

%global previous_version 1.21.1

Name:           crystal-lang
Version:        1.22.3
Release:        %autorelease
Summary:        The Crystal Programming Language

# Apache-2.0 WITH Swift-exception: Crystal compiler and standard library
# Apache-2.0: bundled lib/sanitize
# Apache-2.0 WITH LLVM-exception OR BSL-1.0: src/float/printer/dragonbox.cr
# BSD-3-Clause: src/float/printer/{cached_powers,diy_fp,grisu3,ieee}.cr
# MIT: bundled lib/markd, lib/reply, and playground vendor assets (ansi_up, codemirror, jquery, materialize, octicons)
License:        Apache-2.0 WITH Swift-exception AND Apache-2.0 AND (Apache-2.0 WITH LLVM-exception OR BSL-1.0) AND BSD-3-Clause AND MIT
URL:            https://crystal-lang.org
Source0:        https://github.com/crystal-lang/crystal/archive/%{version}/crystal-%{version}.tar.gz

# Bootstrap seed tarballs (only used when --with bootstrap is enabled)
%if %{with bootstrap}
Source4:        https://github.com/crystal-lang/crystal/releases/download/%{version}/crystal-%{version}-1-linux-x86_64.tar.gz
Source5:        https://github.com/crystal-lang/crystal/releases/download/%{version}/crystal-%{version}-1-linux-aarch64.tar.gz
%endif

ExclusiveArch:  x86_64 aarch64

BuildRequires:  file
BuildRequires:  findutils
%if 0%{?rhel}
BuildRequires:  gc-devel >= 7.6.0
%else
BuildRequires:  gc-devel >= 8.2.0
%endif
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gmp-devel
BuildRequires:  hostname
BuildRequires:  libedit-devel
BuildRequires:  libevent-devel
BuildRequires:  libffi-devel
BuildRequires:  libunwind-devel
BuildRequires:  libxml2-devel
BuildRequires:  libyaml-devel
%if 0%{?fedora} >= 45
BuildRequires:  llvm22-devel
BuildRequires:  lld22
BuildRequires:  clang22
%else
BuildRequires:  lld
BuildRequires:  llvm-devel >= 15
%endif
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconf-pkg-config
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  rubygem-asciidoctor
BuildRequires:  tar
BuildRequires:  xz
BuildRequires:  zlib-devel

%if ! %{with bootstrap}
BuildRequires:  crystal >= %{previous_version}
%endif

%description
Crystal is a general-purpose, object-oriented programming language designed for
developer productivity and execution performance. It features Ruby-inspired
syntax, static type inference, automated memory management via the Boehm-Demers-
Weiser garbage collector, compile-time macros, and direct native machine code
generation via LLVM.


%package -n crystal
Summary:        The Crystal Programming Language
%if 0%{?rhel}
Requires:       gc-devel%{?_isa} >= 7.6.0
%else
Requires:       gc-devel%{?_isa} >= 8.2.0
%endif
Requires:       gcc
Requires:       libevent-devel%{?_isa}
Requires:       lld
Requires:       pcre2-devel%{?_isa}
Requires:       pkgconf-pkg-config
Recommends:     gmp-devel%{?_isa}
Recommends:     libxml2-devel%{?_isa}
Recommends:     libyaml-devel%{?_isa}
Recommends:     openssl-devel%{?_isa}
Recommends:     shards
Recommends:     zlib-devel%{?_isa}

Provides:       %{name} = %{version}-%{release}
Provides:       %{name}%{?_isa} = %{version}-%{release}
Provides:       bundled(crystal-markd) = 0.6.0
Provides:       bundled(crystal-reply) = 0.3.1
Provides:       bundled(crystal-sanitize) = 0.1.0
Provides:       bundled(js-ansi_up) = 1.3.0
Provides:       bundled(js-codemirror) = 5.38.0
Provides:       bundled(js-jquery) = 2.2.1
Provides:       bundled(js-materialize) = 0.97.5
Provides:       bundled(octicons) = 19.5.0

%description -n crystal
Crystal is a general-purpose, object-oriented programming language designed for
developer productivity and execution performance. It features Ruby-inspired
syntax, static type inference, automated memory management via the Boehm-Demers-
Weiser garbage collector, compile-time macros, and direct native machine code
generation via LLVM.


%if %{with doc}
%package -n crystal-docs
Summary:        API documentation for the Crystal Programming Language
BuildArch:      noarch
Requires:       crystal = %{version}-%{release}
Provides:       %{name}-docs = %{version}-%{release}

%description -n crystal-docs
This package provides the offline HTML API documentation for the Crystal
programming language standard library.
%endif


%package -n crystal-samples
Summary:        Sample code for the Crystal Programming Language
BuildArch:      noarch
Requires:       crystal = %{version}-%{release}
Provides:       %{name}-samples = %{version}-%{release}

%description -n crystal-samples
This package provides example programs and sample code demonstrating the syntax
and capabilities of the Crystal programming language.


%prep
%autosetup -n crystal-%{version} -p1
cp -p lib/markd/LICENSE LICENSE-markd
cp -p lib/reply/LICENSE LICENSE-reply
cp -p lib/sanitize/LICENSE LICENSE-sanitize

%if %{with bootstrap}
%ifarch x86_64
tar -xzf %{SOURCE4} -C .
%endif
%ifarch aarch64
tar -xzf %{SOURCE5} -C .
%endif
%endif


%build
%if %{with bootstrap}
bootstrap="$(readlink -f ./crystal-%{version}*)"
binarydir=$(find "$bootstrap" -name crystal -type f -executable -exec sh -c "file -i '{}' | grep -q 'charset=binary'" \; -print0 | xargs -0 dirname)
export PATH="$binarydir:$PATH"
%endif

%set_build_flags
export release=1
export debug=1
export verbose=1
export threads=%{_smp_build_ncpus}
export interpreter=1
export CFLAGS="%{build_cflags}"
export CXXFLAGS="%{build_cxxflags}"
export LDFLAGS="%{build_ldflags}"
%if 0%{?fedora} >= 45
export PATH="%{_libdir}/llvm22/bin:$PATH"
export LLVM_CONFIG="%{_libdir}/llvm22/bin/llvm-config"
%else
export LLVM_CONFIG=$(find %{_bindir} -name "llvm-config*" -print -quit)
%endif

%make_build \
    CRYSTAL_CONFIG_PATH="lib:%{_datadir}/crystal/shards:%{_datadir}/crystal/src" \
    CRYSTAL_CONFIG_LIBRARY_PATH="%{_libdir}"

%if %{with doc}
%make_build docs \
    CRYSTAL_CONFIG_PATH="lib:%{_datadir}/crystal/shards:%{_datadir}/crystal/src" \
    CRYSTAL_CONFIG_LIBRARY_PATH="%{_libdir}"
%endif


%install
%make_install \
    PREFIX=%{_prefix} \
    MANDIR=%{_mandir}

# Ensure Crystal shared directories exist
mkdir -p %{buildroot}%{_datadir}/crystal

%if %{with doc}
# Install API documentation
mkdir -p %{buildroot}%{_datadir}/crystal/docs
cp -a docs/* %{buildroot}%{_datadir}/crystal/docs/
%endif

# Install sample code
mkdir -p %{buildroot}%{_datadir}/crystal/samples
cp -a samples/* %{buildroot}%{_datadir}/crystal/samples/


%check
%if %{with check} && ! %{with bootstrap}
# Remove socket tests requiring multicast/network routing in isolated build chroots
rm -f spec/std/socket/udp_socket_spec.cr

%if 0%{?fedora} >= 45
export PATH="%{_libdir}/llvm22/bin:$PATH"
export LLVM_CONFIG="%{_libdir}/llvm22/bin/llvm-config"
%endif
export CC="gcc -fuse-ld=lld"

make std_spec \
    CRYSTAL_CONFIG_PATH="lib:%{_datadir}/crystal/shards:%{_datadir}/crystal/src" \
    CRYSTAL_CONFIG_LIBRARY_PATH="%{_libdir}"
%endif


%files -n crystal
%license LICENSE LICENSES/MIT.txt LICENSE-markd LICENSE-reply LICENSE-sanitize
%doc CHANGELOG.md README.md
%{_bindir}/crystal
%{_mandir}/man1/crystal*.1*
%dir %{_datadir}/crystal
%{_datadir}/crystal/src
%{_datadir}/bash-completion/completions/crystal
%{_datadir}/zsh/site-functions/_crystal
%{_datadir}/fish/vendor_completions.d/crystal.fish

%if %{with doc}
%files -n crystal-docs
%license LICENSE
%dir %{_datadir}/crystal/docs
%doc %{_datadir}/crystal/docs/*
%endif

%files -n crystal-samples
%license LICENSE
%dir %{_datadir}/crystal/samples
%doc %{_datadir}/crystal/samples/*


%changelog
%autochangelog
