%global major_version 3

Name:           botan3
Version:        3.9.0
Release:        %autorelease
Summary:        Crypto and TLS for C++

License:        BSD-2-Clause
URL:            https://botan.randombit.net/
Source0:        https://botan.randombit.net/releases/Botan-%{version}.tar.xz
Source1:        https://botan.randombit.net/releases/Botan-%{version}.tar.xz.asc
Source2:        https://botan.randombit.net/pgpkey.txt
# https://github.com/randombit/botan/pull/5140
Patch0:         install-fix.patch
# https://github.com/randombit/botan/pull/5040
Patch1:         pyproject.patch
# https://github.com/randombit/botan/pull/5152
Patch2:         shebang-fix.patch

BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-sphinx
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(tss2-esys)
BuildRequires:  pkgconfig(tss2-rc)
BuildRequires:  pkgconfig(tss2-tctildr)
BuildRequires:  pkgconfig(tss2-mu)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  jitterentropy-devel
BuildRequires:  doxygen
BuildRequires:  make

%description
Botan is a BSD-licensed crypto library written in C++. It provides a
wide variety of basic cryptographic algorithms, X.509 certificates and
CRLs, PKCS \#11 certificate requests, a filter/pipe message processing
system, and a wide variety of other features, all written in portable
C++. The API reference, tutorial, and examples may help impart the
flavor of the library. This is the current stable release branch 3.x
of Botan.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n python3-%{name}
Summary:        Python3 bindings for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       python3-libs
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
%{summary}

This package contains the Python3 binding for %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
%{summary}

This package contains HTML documentation for %{name}.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data=%{SOURCE0}
%autosetup -n Botan-%{version} -p1

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_buildrequires

%build
export CXXFLAGS="${CXXFLAGS:-%{optflags}}"

# we have the necessary prerequisites, so enable optional modules
%global enable_modules bzip2,zlib,jitter_rng

%{__python3} ./configure.py \
        --prefix=%{_prefix} \
        --libdir=%{_lib} \
        --docdir=%{_docdir} \
        --cc=gcc \
        --os=linux \
        --cpu=%{_arch} \
        --enable-modules=%{enable_modules} \
        --no-install-python-module \
        --with-sphinx \
        --with-doxygen \
        --with-rst2man \
        --with-cmake-config \
        --distribution-info="$(source /etc/os-release ; echo "$NAME") %{version}-%{release}" \
        --disable-static-library \
        --enable-stack-scrubbing \
        --with-tpm2 \
        --with-sqlite3 \
        --system-cert-bundle=/etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem \
        --with-debug-info

%make_build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_wheel

%install
%make_install
%pyproject_install
%pyproject_save_files -l botan3

# Docs path fix
mv %{buildroot}%{_docdir}/botan-%{version} %{buildroot}%{_pkgdocdir}
rm -rf %{buildroot}%{_pkgdocdir}/handbook/{.doctrees,.buildinfo}

# The following mv are to prevent conflict with botan2
mv %{buildroot}%{_bindir}/botan %{buildroot}%{_bindir}/botan%{major_version}
mv %{buildroot}%{_mandir}/man1/botan.1 %{buildroot}%{_mandir}/man1/botan%{major_version}.1

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./botan-test
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %{py3_test_envvars} %{python3} src/scripts/test_python_packaging.py

%files
%license license.txt
%dir %{_pkgdocdir}
%{_pkgdocdir}/authors.txt
%{_pkgdocdir}/news.txt
%{_pkgdocdir}/pgpkey.txt
%exclude %{_pkgdocdir}/license.txt
%{_libdir}/libbotan-%{major_version}.so.9{,.*}
%{_bindir}/botan%{major_version}
%{_mandir}/man1/botan%{major_version}.1*


%files devel
%{_includedir}/botan-%{major_version}/
%{_libdir}/libbotan-%{major_version}.so
%{_libdir}/pkgconfig/botan-%{major_version}.pc
%{_libdir}/cmake/Botan-%{version}/

%files doc
%license license.txt
%dir %{_pkgdocdir}
%{_pkgdocdir}/handbook/
%{_pkgdocdir}/doxygen/

%files -n python3-%{name} -f %{pyproject_files}

%changelog
%autochangelog
