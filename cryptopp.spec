# Per upstream recommendations.
# https://www.cryptopp.com/wiki/Link_Time_Optimization
%define _lto_cflags %{nil}

Name:           cryptopp
Version:        8.8.0
Release:        %autorelease
Summary:        C++ class library of cryptographic schemes
License:        Boost
URL:            https://www.cryptopp.com

%define v_tag %(v=%{version}; echo ${v//./_})
%define v_file %(v=%{version}; echo ${v//./})

Source0:        %{url}/cryptopp%{v_file}.zip
Source1:        %{url}/cryptopp%{v_file}.zip.sig
Source2:        %{url}/signing.html#/keyring.gpg
Source10:       https://github.com/noloader/cryptopp-autotools/releases/download/CRYPTOPP_%{v_tag}/cryptopp-autotools%{v_file}.zip
Source11:       https://github.com/noloader/cryptopp-autotools/releases/download/CRYPTOPP_%{v_tag}/cryptopp-autotools%{v_file}.zip.sig

# Should be <major>+<minor>:<patch>:<minor> (this is confusing -_-)
Patch0:         fix-autotools-version-info.patch

# fix "undefined reference to `AdhocTest'" when linking to the shared object
Patch1:         remove-adhoc.patch

BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  glibc-common

BuildRequires:  doxygen

BuildRequires:  gcc
BuildRequires:  gcc-c++

BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  automake

BuildRequires:  dos2unix
BuildRequires:  gnupg2

Obsoletes:  %{name}-progs < 8.8.0-3

# Obsoletes pycryptopp to avoid breaking upgrades
Obsoletes:  pycryptopp < 0.7
Provides:   pycryptopp = 0.7


%description
Crypto++ Library is a free C++ class library of cryptographic schemes.
See http://www.cryptopp.com/ for a list of supported algorithms.

One purpose of Crypto++ is to act as a repository of public domain
(not copyrighted) source code. Although the library is copyrighted as a
compilation, the individual files in it are in the public domain.

%package devel
Summary:        Header files and development documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-doc < 8.8.0-3
Provides:       %{name}-doc < 8.8.0-3

%description devel
Crypto++ Library is a free C++ class library of cryptographic schemes.

This package contains the header files and development documentation
for %{name}.

%package static
Summary:        Static libraries for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
Crypto++ Library is a free C++ class library of cryptographic schemes.

This package contains static libraries for %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE11}' --data='%{SOURCE10}'

%autosetup -c -p1 -a 10
find . -type f -name "*.zip" -exec rm "{}" \;
dos2unix License.txt Readme.txt
find . -not -type d -exec file "{}" ";" -print0 | grep -z CRLF | cut -d':' -z -f1 | xargs -0 dos2unix

%build
autoreconf -vi
# Upstream recommends -O3, define NDEBUG to prevent sensitive data leaking on crash
export CXXFLAGS="$(echo "%{optflags}" | sed -e 's/-O2//') -O3 -DNDEBUG"
%configure
%make_build all-am docs

%install
%make_install
rm %{buildroot}%{_bindir}/cryptest
rm -rf %{buildroot}%{_datadir}/%{name}/
mkdir -p %{buildroot}%{_libdir}/pkgconfig
install -p -m 0644 libcryptopp.pc %{buildroot}%{_libdir}/pkgconfig/libcryptopp.pc

%check
./cryptest v

%files
%{_libdir}/libcryptopp.so.8*
%doc Readme.txt
%license License.txt

%files devel
%doc html-docs/*
%{_includedir}/cryptopp
%{_libdir}/libcryptopp.so
%{_libdir}/pkgconfig/libcryptopp.pc

%files static
%{_libdir}/libcryptopp.a

%changelog
%autochangelog
