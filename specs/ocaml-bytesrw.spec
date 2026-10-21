# Optional dependencies
%bcond libblake3 1
%bcond libmd 1
# Version 4.x of mbedtls is needed, but Fedora has 3.x
%bcond mbedtls 0
%bcond xxhash 1
%bcond zlib 1
%bcond zstd 1

# Convenience macro for setting boolean values
%define confbool() %{expand:%%{?with_%{1}:true}%%{!?with_%{1}:false}}

Name:           ocaml-bytesrw
Version:        0.4.1
Release:        %autorelease
Summary:        Composable byte stream readers and writers for OCaml

License:        ISC
URL:            https://erratique.ch/software/bytesrw
VCS:            git:https://erratique.ch/repos/bytesrw.git
Source:         https://github.com/dbuenzli/bytesrw/archive/v%{version}/bytesrw-%{version}.tar.gz
# Use the zlib-ng interface instead of the compat zlib interface
Patch:          %{name}-zlib-ng.patch

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildSystem:    topkg
BuildOption(build): --dev-pkg false
BuildOption(build): --with-b0 true
BuildOption(build): --with-cmdliner true
BuildOption(build): --with-conf-libblake3 %{confbool libblake3}
BuildOption(build): --with-conf-libmd %{confbool libmd}
BuildOption(build): --with-conf-mbedtls %{confbool mbedtls}
BuildOption(build): --with-conf-xxhash %{confbool xxhash}
BuildOption(build): --with-conf-zlib %{confbool zlib}
BuildOption(build): --with-conf-zstd %{confbool zstd}

BuildRequires:  gcc-c++
BuildRequires:  ocaml >= 4.14.0
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocaml-topkg-devel >= 1.1.1
BuildRequires:  pkgconfig

# Optional dependencies
%if %{with libblake3}
BuildRequires:  pkgconfig(libblake3)
%endif
%if %{with libmd}
BuildRequires:  pkgconfig(libmd)
%endif
%if %{with xxhash}
BuildRequires:  pkgconfig(libxxhash)
%endif
%if %{with zstd}
BuildRequires:  pkgconfig(libzstd) >= 1.3.8
%endif
%if %{with mbedtls}
BuildRequires:  pkgconfig(mbedtls)
%endif
%if %{with zlib}
BuildRequires:  pkgconfig(zlib-ng)
%endif

# Test dependencies, not used until mbedtls is available
#BuildRequires:  ocaml-b0-devel >= 0.0.6
#BuildRequires:  ocaml-cmdliner-devel >= 2.0.0

%description
Bytesrw extends the OCaml Bytes module with composable, memory efficient, byte
stream readers and writers compatible with effect-based concurrency.

Except for byte slice lifetimes, these abstractions intentionally separate
away resource management and the specifics of reading and writing bytes.

The Fedora package is build with optional support for compressed, hashed and
encrypted bytes.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n bytesrw-%{version} -p1

%conf
# Topkg does watermark replacements only if run inside a git checkout.  Github
# tarballs do not come with a .git directory.  Therefore, we do the watermark
# replacement manually.
for fil in $(find . -type f); do
  sed -e 's,%%%%VERSION%%%%,v%{version},' \
      -e 's,%%%%VERSION_NUM%%%%,%{version},' \
      -i.orig $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

%check
# The tests don't work without mbedtls.  Some day, do this:
#%%if %%{without libblake3}
#sed -i '/^let test_blake3/d' B0.ml
#%%endif
#%%if %%{without libmd}
#sed -i '/^let test_md/d' B0.ml
#%%endif
#%%if %%{without xxhash}
#sed -i '/^let test_xxhash/d' B0.ml
#%%endif
#%%if %%{without zstd}
#sed -i '/^let test_zstd/d' B0.ml
#%%endif
#%%if %%{without mbedtls}
#sed -i '/^let test_psa/d' B0.ml
#%%endif
#%%if %%{without zlib}
#sed -i '/^let test_zlib/d' B0.ml
#%%endif
#b0 test

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
