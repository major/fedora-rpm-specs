Name:       orocos-bfl
%global commit cf72962177bc8287eb9dab19d6aea61b9212b04b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global checkout 20190423git%{shortcommit}
Version:    0.8.99
Release:    %autorelease -s %{checkout}
Summary:    A framework for inference in Dynamic Bayesian Networks

# Explanation from upstream for multiple licenses:
# "The technical reason we could not longer use the LGPL license for RTT/BFL
# software was that the LGPL is not compatible with C++ templates, which are
# used extensively in the RTT/BFL libraries. The 'runtime exception' says
# explicitly that using the C++ templates (or any other function) of the RTT
# software does not make your derived work GPL. The derived work may be
# distributed under any license you see fit."
# see http://www.orocos.org/orocos/license
License:    GPLv2 with exceptions and LGPLv2+
URL:        http://www.orocos.org/bfl/
Source0:    https://github.com/toeklk/orocos-bayesian-filtering/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  ginac-devel

%description
The Bayesian Filtering Library (BFL) provides an application independent
framework for inference in Dynamic Bayesian Networks, i.e., recursive
information processing and estimation algorithms based on Bayes' rule, such as
(Extended) Kalman Filters, Particle Filters, etc.  These algorithms can, for
example, be run on top of the Realtime Services, or be used for estimation in
Kinematics & Dynamics applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel, ginac-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for %{name}.


%prep
%setup -q -n orocos-bayesian-filtering-%{commit}/orocos_bfl

%build
export LDFLAGS='-ldl'
%cmake \
  -DGINAC_SUPPORT:BOOL=ON \
  -DLIBRARY_TYPE:STRING="shared"
%cmake_build

%cmake_build --target docs

%check
%cmake_build --target check


%install
%cmake_install

# tests are installed here, remove them
rm -rf %{buildroot}%{_bindir}/bfl

%files
%doc README.md
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files doc
%doc %{_vpath_builddir}/doc/html
%license COPYING


%changelog
%autochangelog
