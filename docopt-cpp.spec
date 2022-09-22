%global forgeurl0 %{url}

Name:           docopt-cpp
Version:        0.6.3
Release:        %autorelease
Summary:        C++11 Port of docopt

License:        MIT or Boost
URL:            https://github.com/docopt/docopt.cpp

%forgemeta
Source0:        %{forgesource0}

# https://github.com/docopt/docopt.cpp/pull/145
Patch1:         %{url}/pull/145.patch#/docopt-0.6.3-run-tests.patch

BuildRequires:  cmake gcc-c++
BuildRequires:  rpmautospec redhat-rpm-config
# Needed for tests
BuildRequires:  python3-devel

%global common_description %{expand:docopt creates beautiful command-line interfaces

Isn't it awesome how getopt (and boost::program_options for you fancy folk!)
generate help messages based on your code?! These timeless functions have been
around for decades and have proven we don't need anything better, right?

Hell no! You know what's awesome? It's when the option parser is generated
based on the beautiful help message that you write yourself! This way you
don't need to write this stupid repeatable parser-code, and instead can
write only the help message-the way you want it.
}

%description
%{common_description}
This is a port of the docopt.py module (https://github.com/docopt/docopt),
and we have tried to maintain full feature parity (and code structure)
as the original.

This port is written in C++11 and also requires a good C++11 standard library
(in particular, one with regex support).

%package devel
Summary:        Developer files for a docopt C++11 port
Requires:       cmake-filesystem
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{common_description}
Contains developer headers and a library. Install if docopt.cpp is used in
a code to be compiled.

%prep
%forgeautosetup -p1


%build
%cmake -DWITH_TESTS=on
%cmake_build


%install
%cmake_install
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libdocopt.a


%check
pushd "%{__cmake_builddir}"
%python3 run_tests
popd


%files
%license LICENSE-Boost-1.0 LICENSE-MIT
%doc README.rst
%{_libdir}/libdocopt.so.0*

%files devel
%{_includedir}/docopt
%{_libdir}/cmake/docopt
%{_libdir}/libdocopt.so
%{_libdir}/pkgconfig/docopt.pc


%changelog
%autochangelog
