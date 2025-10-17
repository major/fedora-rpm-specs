Name:           pystring
Version:        1.1.4

%global forgeurl https://github.com/imageworks/%{name}
%global commit a09708a4870db7862e1a1aa42658c8e6e36547e7

%forgemeta

Release:        %autorelease
Summary:        Collection of C++ functions emulating Python's string class methods
License:        BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  meson
BuildRequires:  gcc-c++

%description
Pystring is a collection of C++ functions which match the interface and
behavior of Python's string class methods using std::string. Implemented in
C++, it does not require or make use of a Python interpreter. It provides
convenience and familiarity for common string operations not included in the
standard C++ library. It's also useful in environments where both C++ and
Python are used.

Overlapping functionality (such as index and slice/substr) of std::string is
included to match Python interfaces.

Originally developed at Sony Pictures Imageworks.
http://opensource.imageworks.com/

%package devel

Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files and development documentation
for %{name}.

%prep
%forgeautosetup -p1

%build
%meson
%meson_build


%install
%meson_install

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.1*

%files devel
%{_includedir}/%{name}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
%autochangelog
