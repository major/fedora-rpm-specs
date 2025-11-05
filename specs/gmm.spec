Name:    gmm
Version: 5.4.4
Release: %autorelease
Summary: A generic C++ template library for sparse, dense and skyline matrices
License: LGPL-3.0-or-later AND BSD 3-Clause
URL:     https://getfem.org/gmm.html
Source0: https://download-mirror.savannah.gnu.org/releases/getfem/stable/gmm-%{version}.tar.gz

BuildArch: noarch

BuildRequires: gcc-c++
BuildRequires: perl-interpreter
BuildRequires: make

%description
%{summary}.

%package devel
Summary:A generic C++ template library for sparse, dense and skyline matrices
Provides: %{name} = %{version}-%{release}
Provides: gmm++-devel = %{version}-%{release}
%description devel
%{summary}.


%prep
%autosetup


%build
%configure


%install
%make_install


%check
make check -k || cat tests/test-suite.log ||:


%files devel
%doc README
%license COPYING
%{_includedir}/gmm/


%changelog
%autochangelog

