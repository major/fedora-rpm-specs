%global major_version 2

Name:           botan2
Version:        2.19.5
Release:        %autorelease
Summary:        Crypto and TLS for C++11

License:        BSD-2-Clause
URL:            https://botan.randombit.net/
Source0:        https://botan.randombit.net/releases/Botan-%{version}.tar.xz

# Backport: Remove usage of deprecated asio API
Patch0:         37fec38ff97604f964122cd2d33f5d503f319b10.patch
# Fix compilation on GCC 15
Patch1:         f765f0b312f2998498f629d93369babfb2c975b4.patch

BuildRequires:  gcc-c++
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-docutils
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  make

%description
Botan is a BSD-licensed crypto library written in C++. It provides a
wide variety of basic cryptographic algorithms, X.509 certificates and
CRLs, PKCS \#10 certificate requests, a filter/pipe message processing
system, and a wide variety of other features, all written in portable
C++. The API reference, tutorial, and examples may help impart the
flavor of the library. This is the current stable release branch 2.x
of Botan.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
%{summary}

This package contains HTML documentation for %{name}.


%package -n python3-%{name}
Summary:        Python3 bindings for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
%{summary}

This package contains the Python3 binding for %{name}.


%prep
%autosetup -n Botan-%{version} -p1


%build
export CXXFLAGS="${CXXFLAGS:-%{optflags}}"

# we have the necessary prerequisites, so enable optional modules
%global enable_modules bzip2,zlib

%{__python3} ./configure.py \
        --prefix=%{_prefix} \
        --libdir=%{_lib} \
        --docdir=%{_docdir} \
        --cc=gcc \
        --os=linux \
        --cpu=%{_arch} \
        --enable-modules=%{enable_modules} \
        --with-python-version=%{python3_version} \
        --with-sphinx \
        --with-rst2man \
        --distribution-info="$(source /etc/os-release ; echo "$NAME")" \
        --disable-static-library \
        --with-debug-info

# work around https://github.com/randombit/botan/issues/2130
%make_build PYTHON_EXE=%{__python3}

%install
make install PYTHON_EXE=%{__python3} DESTDIR=%{buildroot}

sed -e '1{/^#!/d}' -i %{buildroot}%{python3_sitearch}/botan2.py
%if "%{python3_sitelib}" != "%{python3_sitearch}"
mkdir -p %{buildroot}%{python3_sitelib}
mv %{buildroot}%{python3_sitearch}/botan2.py %{buildroot}%{python3_sitelib}/botan2.py
%endif

# doc installation fixups
mv %{buildroot}%{_docdir}/botan-%{version} %{buildroot}%{_pkgdocdir}
rm -r %{buildroot}%{_pkgdocdir}/handbook/{.doctrees,.buildinfo}


%ldconfig_scriptlets


%files
%license license.txt
%dir %{_pkgdocdir}
%{_pkgdocdir}/*.txt
%{_libdir}/libbotan-%{major_version}.so.19*
%{_bindir}/botan
%{_mandir}/man1/botan.1*


%files devel
%license license.txt
%{_includedir}/*
%{_libdir}/libbotan-%{major_version}.so
%{_libdir}/pkgconfig/botan-%{major_version}.pc


%files doc
%license license.txt
%dir %{_pkgdocdir}
%{_pkgdocdir}/handbook


%files -n python3-%{name}
%license license.txt
%pycached %{python3_sitelib}/%{name}.py


%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./botan-test


%changelog
%autochangelog
