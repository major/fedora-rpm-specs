Name:           qvr
Version:        4.0.1
Release:        %autorelease
Summary:        QT library for VR applications

License:        MIT
URL:            https://marlam.de/qvr
Source0:        %{url}/releases/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/%{name}-%{version}.tar.gz.sig
Source2:        https://marlam.de/key.txt

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  make
BuildRequires:  texlive-amsmath
BuildRequires:  texlive-beamer
BuildRequires:  texlive-babel-english
BuildRequires:  texlive-dvips
BuildRequires:  texlive-ec
BuildRequires:  texlive-latex
BuildRequires:  texlive-textpos

BuildRequires:  libxkbcommon-devel
BuildRequires:  openvr-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  vrpn-devel

%description
QVR is a library that makes writing Virtual Reality (VR) applications very
easy. It is based on Qt and requires no other libraries.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libxkbcommon-devel
Requires:       openvr-devel
Requires:       qt6-qtbase-devel
Requires:       vrpn-devel

%description    devel
This package provides development headers and libraries for %{name}.

%package        doc
Summary:        Additional documentation for %{name}
BuildArch:      noarch

%description    doc
This package provides additional documentation for %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
# Build docs
pushd doc/intro-slides
%make_build
popd

pushd libqvr
%cmake -DQVR_BUILD_DOCUMENTATION=ON
%cmake_build
popd

%install
pushd libqvr
%cmake_install

%check
pushd libqvr
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.4{,.*}

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/QVR-%{version}/

%files doc
%doc doc/intro-slides/%{name}.pdf
%doc %{_docdir}/libqvr

%changelog
%autochangelog
